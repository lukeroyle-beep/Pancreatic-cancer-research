"""Verify file identity, eligibility and feature coverage without reporting response values."""

import argparse
from collections import Counter
import csv
import gzip
from hashlib import sha256
import json
from math import isfinite
from pathlib import Path
from urllib.request import urlopen

from openpyxl import load_workbook


STUDY = "https://www.ebi.ac.uk/biostudies/files/S-EPMC9023604/"
ASSETS = {
    "hgnc.tsv": (
        "https://storage.googleapis.com/public-download-files/hgnc/archive/archive/quarterly/tsv/hgnc_complete_set_2026-10-02.tsv",
        "2b4224ea847df2fc6982f5b2a52804c5d92fbb8810b134afb636f6029452dc03"),
    "tiriac_s4.xlsx": ("https://ndownloader.figshare.com/files/39996295",
                       "d80eb561b653f9a2c78d7db79e9c9220a105d3c8bbe8ece700a7698ed0abc8c8"),
    "tiriac_s5.xlsx": ("https://ndownloader.figshare.com/files/39996292",
                       "a267f9f490c21a2fe407421bf0ac767b274b1691ee8528997ddc3e33d3cd4e70"),
    "shi_metadata.xlsx": (STUDY + "41467_2022_29857_MOESM4_ESM.xlsx",
                          "a89e694d1271454272d237e60d087cd3954a6e03cc27f188a8ad8920bb97f621"),
    "shi_response.xlsx": (STUDY + "41467_2022_29857_MOESM11_ESM.xlsx",
                          "68843d04c8871619ab3c1666dea5d8e5d90bdffc64b0ab41e1f27d21ff0e3503"),
    "shi_expression.tsv.gz": (
        "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE194nnn/GSE194249/suppl/GSE194249_PDPCOs_FPKM.txt.gz",
        "479517fbed1d8f5bb9d141b6b932b6ab56ba2ba72d4394d13aea2a3da0a50f27"),
}


def load_assets(directory):
    directory.mkdir(parents=True, exist_ok=True)
    for name, (url, digest) in ASSETS.items():
        path = directory / name
        if path.exists():
            data = path.read_bytes()
        else:
            with urlopen(url, timeout=120) as response:
                data = response.read()
        if sha256(data).hexdigest() != digest:
            raise ValueError(f"Unexpected contents for {name}")
        if not path.exists():
            path.write_bytes(data)


def sheet_rows(directory, name, sheet):
    workbook = load_workbook(directory / name, read_only=True, data_only=True)
    try:
        return list(workbook[sheet].values)
    finally:
        workbook.close()


def numeric(value):
    return type(value) in (float, int) and isfinite(value)


def audit(directory):
    source = sheet_rows(directory, "tiriac_s4.xlsx", "Chemo ")
    gem_column = source[1].index("Gemcitabine")
    reference = {row[0] for row in source[2:] if numeric(row[gem_column])}
    signature = sheet_rows(directory, "tiriac_s5.xlsx", "GEM profile")
    negative = {symbol for symbol, rho in signature if numeric(rho) and rho < -0.38}
    with gzip.open(directory / "shi_expression.tsv.gz", "rt") as file:
        rows = csv.reader(file, delimiter="\t")
        expression_ids = next(rows)[1:]
        symbol_counts = Counter(row[0] for row in rows)
    missing = negative - symbol_counts.keys()
    alternatives = {}
    with (directory / "hgnc.tsv").open(encoding="utf-8", newline="") as nomenclature:
        for gene in csv.DictReader(nomenclature, delimiter="\t"):
            if gene["symbol"] in missing:
                candidates = (gene["prev_symbol"] + "|" + gene["alias_symbol"]).split("|")
                alternatives[gene["symbol"]] = sorted({x for x in candidates if x in symbol_counts})
    if alternatives.keys() != missing:
        raise ValueError("Missing signature symbol absent from HGNC snapshot")
    response = sheet_rows(directory, "shi_response.xlsx", "Sheet1")
    gem_row, = [row for row in response if row[0] == "GEM"]
    measured = {label for label, value in zip(response[1][1:], gem_row[1:], strict=True)
                if numeric(value)}
    metadata = sheet_rows(directory, "shi_metadata.xlsx", "84 PDPCOs")
    joined = [dict(zip(metadata[1], row, strict=True)) for row in metadata[2:]
              if row[1] in measured and row[1] in expression_ids]
    pdac = [row for row in joined
            if row["Tumor Other Histologic Subtype"] == "Pancreatic Ductal Adenocarcinoma"]
    if len({row["Sample ID"] for row in joined}) != len(joined):
        raise ValueError("Repeated clinical sample ID")
    return {
        "reference_models_with_gemcitabine": len(reference),
        "signature_rows_with_numeric_rho": sum(numeric(row[1]) for row in signature),
        "negative_signature_symbols": len(negative),
        "unique_exact_matches_in_expression": sum(symbol_counts[symbol] == 1 for symbol in negative),
        "external_expression_distinct_symbols": len(symbol_counts),
        "missing_exact_symbols_and_hgnc_alias_hits": alternatives,
        "shi_gemcitabine_models": len(measured),
        "shi_joined_models": len(joined),
        "shi_joined_pdac": len(pdac),
        "number_of_samples_per_patient_field": Counter(row["Number of Samples Per Patient"] for row in pdac),
        "specimen_type": Counter(row["Sample Type"] for row in pdac),
        "prior_neoadjuvant_therapy": Counter(row["Neoadjuvant Therapy Prior To Resection "] for row in pdac),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path, help="Public file cache outside the repository")
    args = parser.parse_args()
    load_assets(args.cache)
    print(json.dumps(audit(args.cache), indent=2, sort_keys=True))
