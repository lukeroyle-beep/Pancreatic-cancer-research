"""Re-run the PCR-001 index census and focused search. Python 3.12, standard library."""
import argparse
import csv
import gzip
import hashlib
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

END_DATE = "2026-11-27"
DISEASE = ["pancreatic ductal adenocarcinoma", "pancreatic adenocarcinoma", "pancreatic cancer", "PDAC"]
THEMES = {
    "dependencies": ["dependency", "dependencies", "synthetic lethality", "synthetic lethal", "essentiality", "CRISPR screen"],
    "kras": ["KRAS", "K-RAS", "Kirsten rat sarcoma"],
    "resistance": ["chemoresistance", "drug resistance", "treatment resistance", "therapeutic resistance", "chemotherapy resistance", "acquired resistance"],
    "microenvironment": ["tumor microenvironment", "tumour microenvironment", "immune evasion", "stroma", "cancer-associated fibroblasts"],
    "combinations": ["repurpos*", "combination therapy", "combination therapies", "drug combination", "synerg*"],
    "rna": ["RNA therapeutics", "RNA therapy", "antisense oligonucleotide", "siRNA", "small interfering RNA", "mRNA vaccine", "RNA vaccine", "messenger RNA vaccine", "RNA interference"],
    "computational": ["target discovery", "target identification", "drug target prediction", "DepMap", "network pharmacology", "computational drug repurposing"],
}
UPDATES = ["reviews_update", "preprints_update", "trials_update"]
HISTORICAL = ["systematic_reviews", "phase3"]
GENES = ["CDS1", "CDS2", "CDP-diacylglycerol synthase"]
CONTEXT = ["pancreatic cancer", "pancreatic ductal adenocarcinoma", "PDAC", "synthetic lethality"]
SENSITIVITY = CONTEXT + ["synthetic lethal", "cancer", "cancers", "tumor", "tumour", "carcinoma", "mesenchymal"]
LOCKS = {name: threading.Lock() for name in ("pubmed", "europepmc")}
LAST = dict.fromkeys(LOCKS, 0.0)
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"


def clause(terms, db):
    values = []
    for term in terms:
        quoted = f'"{term}"' if " " in term or "-" in term else term
        values.append(f"{quoted}[tiab]" if db == "pubmed" else f"TITLE_ABS:{quoted}")
    return "(" + " OR ".join(values) + ")"


def query(label, db):
    start = "1900-01-01"
    if label.startswith("focus"):
        context = CONTEXT if label == "focus_v1" else SENSITIVITY
        body = f"{clause(GENES, db)} AND {clause(context, db)}"
    elif label == "preprints" or label in UPDATES or label in HISTORICAL:
        start = "2025-01-01" if label == "preprints" else "2026-11-01"
        if label in HISTORICAL:
            start = "1900-01-01"
        terms = sorted(set(term for group in THEMES.values() for term in group))
        subset = "preprint[pt]" if db == "pubmed" else "SRC:PPR"
        if label == "reviews_update":
            subset = '("systematic review"[pt] OR "meta-analysis"[pt])' if db == "pubmed" else '(PUB_TYPE:"systematic review" OR PUB_TYPE:"meta-analysis")'
        if label == "systematic_reviews":
            subset = '"systematic review"[pt]' if db == "pubmed" else 'PUB_TYPE:"systematic review"'
        if label == "phase3":
            subset = '"clinical trial, phase iii"[pt]' if db == "pubmed" else 'PUB_TYPE:"clinical trial, phase iii"'
        if label == "trials_update":
            subset = '"randomized controlled trial"[pt]' if db == "pubmed" else 'PUB_TYPE:"randomized controlled trial"'
        body = f"{clause(DISEASE, db)} AND {clause(terms, db)} AND {subset}"
    else:
        body = f"{clause(DISEASE, db)} AND {clause(THEMES[label], db)}"
    date = f'("{start.replace("-", "/")}"[dp] : "{END_DATE.replace("-", "/")}"[dp])'
    if db == "europepmc":
        date = f"FIRST_PDATE:[{start} TO {END_DATE}]"
    return f"({body} AND {date})"


def fetch(db, url, params):
    for attempt in range(5):
        with LOCKS[db]:
            time.sleep(max(0, 0.5 - (time.monotonic() - LAST[db])))
            LAST[db] = time.monotonic()
        try:
            req = Request(url + "?" + urlencode(params), headers={"User-Agent": "PCR-001-bibliographic-review/1.0"})
            with urlopen(req, timeout=90) as response:
                return json.load(response)
        except (URLError, TimeoutError, ValueError, ConnectionError) as exc:
            if isinstance(exc, HTTPError) and exc.code not in (408, 425, 429, 500, 502, 503, 504):
                raise
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)


def pubmed_ids(term, lower=1, upper=99999999, first=True):
    ranged = term if first else f"({term}) AND {lower}:{upper}[uid]"
    data = fetch("pubmed", EUTILS, {"db": "pubmed", "term": ranged, "retmode": "json",
                                    "retmax": 9999, "tool": "pcr001_review"})
    result = data["esearchresult"]
    if "ERROR" in result or "error" in result:
        raise RuntimeError(result)
    count = int(result["count"])
    if count > 9999:
        if lower == upper:
            raise RuntimeError("Cannot partition PubMed result further")
        mid = (lower + upper) // 2
        left, _ = pubmed_ids(term, lower, mid, False)
        right, _ = pubmed_ids(term, mid+1, upper, False)
        ids = left | right
    else:
        ids = {"MED:" + uid for uid in result["idlist"]}
    if len(ids) != count:
        raise RuntimeError(f"PubMed count mismatch {len(ids)} versus {count}")
    return ids, count


def europe_ids(term):
    ids = set()
    cursor = "*"
    seen_cursors = set()
    expected = None
    while cursor not in seen_cursors:
        seen_cursors.add(cursor)
        data = fetch("europepmc", EPMC, {"query": term, "format": "json", "resultType": "idlist",
                                         "pageSize": 1000, "cursorMark": cursor})
        count = int(data["hitCount"])
        if expected is None:
            expected = count
        if expected != count:
            raise RuntimeError("Europe PMC returned a changing hitCount")
        records = data["resultList"].get("result", [])
        ids.update(item["source"] + ":" + item["id"] for item in records)
        if len(ids) == count:
            return ids, count
        cursor = data.get("nextCursorMark")
        if not cursor or not records:
            break
    raise RuntimeError(f"Europe PMC count mismatch {len(ids)} versus {expected}")


def write_tsv(path, header, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True, help="new, empty directory for a dated run")
    parser.add_argument("--only", nargs="+", choices=[*THEMES, *UPDATES, *HISTORICAL, "preprints", "focus_v1", "focus_v2"])
    parser.add_argument("--database", nargs="+", choices=["pubmed", "europepmc"], default=["pubmed", "europepmc"])
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if any(args.output.iterdir()):
        parser.error("output directory must be empty")
    jobs = [(label, db) for label in args.only or [*THEMES, "preprints", "focus_v1", "focus_v2"]
            for db in args.database]
    start = datetime.now(timezone.utc).isoformat()

    def run(job):
        label, db = job
        term = query(label, db)
        ids, count = pubmed_ids(term) if db == "pubmed" else europe_ids(term)
        print(f"{db} {label}: {count}", file=sys.stderr, flush=True)
        return label, db, term, sorted(ids), count

    with ThreadPoolExecutor(max_workers=6) as pool:
        jobs_out = list(pool.map(run, jobs))
    memberships = {}
    query_rows = []
    for label, db, term, ids, count in jobs_out:
        for doc_id in ids:
            memberships.setdefault(doc_id, {}).setdefault(db, []).append(label)
        digest = hashlib.sha256(("\n".join(ids)+"\n").encode()).hexdigest()
        query_rows.append((label, db, count, digest, term))
    write_tsv(args.output / "queries.tsv", ["arm", "index", "hits", "sorted_id_sha256", "executed_query"], query_rows)
    # Stable compression avoids depending on the filename or wall clock.
    with (args.output / "membership.tsv.gz").open("wb") as stream:
        with gzip.GzipFile(filename="", fileobj=stream, mode="wb", mtime=0) as gz:
            gz.write(b"source_id\tpubmed_arms\teuropepmc_arms\n")
            for key, indexes in sorted(memberships.items()):
                row = [key, ",".join(sorted(indexes.get("pubmed", []))), ",".join(sorted(indexes.get("europepmc", [])))]
                gz.write(("\t".join(row)+"\n").encode())
    details = {"started_utc": start, "finished_utc": datetime.now(timezone.utc).isoformat(),
               "python": sys.version.split()[0], "date_cutoff": END_DATE, "source_id_union": len(memberships),
               "pubmed_endpoint": EUTILS, "europepmc_endpoint": EPMC}
    (args.output / "execution.json").write_text(json.dumps(details, indent=2)+"\n")


if __name__ == "__main__":
    main()
