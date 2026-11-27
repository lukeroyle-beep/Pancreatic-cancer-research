"""Check aggregate metadata and published table entries. Usage in feasibility.md."""

import argparse
import csv
import hashlib
import io
import json
import tempfile
import urllib.request
import zipfile
from collections import Counter
from pathlib import Path
from shutil import copyfileobj

from openpyxl import load_workbook


FIGSHARE = "https://ndownloader.figshare.com/files/"
SANGER = "41586_2026_10830_MOESM3_ESM.zip"
FILES = {
    "screen_metadata.csv": (FIGSHARE + "64494441", "af29e349dd19676029950d6799fec4efcefcb9b314f7622b4fcc6d564803472a"),
    "paralog_dependency_tests_full.csv": (FIGSHARE + "64494540", "b8b1987c3b18a9a6574cc91280ef6e275f07975cefc90e6ed4f5efed6af6e7a8"),
    "pdac_classical_dependency_tests_full.csv": (FIGSHARE + "64494543", "8da8fcb789771303408d5ba006ef3a10ddd58ba9943c235d12dcc6a87a6004f3"),
    SANGER: ("https://pmc-oa-opendata.s3.amazonaws.com/PMC13581617.1/" + SANGER, "7e83b7551c9c272de0bc0455ea9a0e7803a8043d15d9cfedf5a1c3e609a2a6e2"),
}


def verify_inputs(folder, download):
    folder.mkdir(parents=True, exist_ok=True)
    for name, (url, expected) in FILES.items():
        path = folder / name
        if not path.exists() and download:
            with tempfile.NamedTemporaryFile(dir=folder, delete=False) as tmp:
                temp_path = Path(tmp.name)
                try:
                    with urllib.request.urlopen(url, timeout=120) as response:
                        copyfileobj(response, tmp)
                    tmp.flush()
                    with temp_path.open("rb") as raw:
                        if hashlib.file_digest(raw, "sha256").hexdigest() != expected:
                            raise ValueError(f"Downloaded content changed for {name}")
                    temp_path.replace(path)
                finally:
                    temp_path.unlink(missing_ok=True)
        with path.open("rb") as raw:
            if hashlib.file_digest(raw, "sha256").hexdigest() != expected:
                raise ValueError(f"Unexpected content for {name}")


def read_rows(sheet):
    values = sheet.values
    headers = next(values)
    return [dict(zip(headers, row)) for row in values if row[0] is not None]


def find_entry(folder, name, marker):
    with (folder / name).open(newline="") as raw:
        matches = [r for r in csv.DictReader(raw)
                   if r["Dependency"] == "CDS2 (8760)" and r["Biomarker"] == marker]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one row for {marker}")
    return matches[0]


def summarise(folder):
    with (folder / "screen_metadata.csv").open(newline="") as raw:
        broad = [r for r in csv.DictReader(raw) if r["OncotreeCode"] == "PAAD"
                 and r["PassesQC"] == "TRUE" and r["HasExprData"] == "TRUE"]
    formats = {fmt: {"screens": sum(r["ScreenType"] == fmt for r in broad),
                     "models": len({r["ModelID"] for r in broad if r["ScreenType"] == fmt})}
               for fmt in sorted({r["ScreenType"] for r in broad})}
    with zipfile.ZipFile(folder / SANGER) as archive:
        workbook = load_workbook(io.BytesIO(archive.read("supplementary_table_2_revision.xlsx")),
                                 read_only=True, data_only=True)
    try:
        pancreatic = [r for r in read_rows(workbook["data_availability"])
                      if r["primary_tumour_type"] == "Pancreatic"]
        paired = [r for r in pancreatic if r["RNAseq_available"] == r["CRISPR_available"] == "Yes"]
        samples = {r["sample_ID"] for r in paired}
        clinical = [r for r in read_rows(workbook["clinical_data"]) if r["sample_ID"] in samples]
        if len(samples) != len(clinical) or any(r["individual_ID"] is None for r in paired):
            raise ValueError("Ambiguous sample metadata")
    finally:
        workbook.close()
    return {
        "broad_quality_passing_PAAD_with_expression": formats,
        "sanger_pancreatic_models": len(pancreatic),
        "sanger_paired_models": len(paired),
        "sanger_paired_donors": len({r["individual_ID"] for r in paired}),
        "sanger_paired_broad_overlap_annotation": dict(Counter(r["overlap_Broad_DepMap"] for r in paired)),
        "sanger_paired_morphology": dict(Counter(r["ICD-O-3 Code and Morphology"] for r in clinical)),
        "published_paralog_row": find_entry(folder, "paralog_dependency_tests_full.csv", "CDS1 (1040)"),
        "published_program_row": find_entry(folder, "pdac_classical_dependency_tests_full.csv", "PDAC-classical"),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cache", type=Path)
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    verify_inputs(args.cache, args.download)
    print(json.dumps(summarise(args.cache), indent=2, sort_keys=True))
