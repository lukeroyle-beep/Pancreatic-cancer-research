"""Retrieve the unthemed phase III sensitive search; no third-party dependencies."""
import argparse
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from retrieve import DISEASE, END_DATE, clause, europe_ids, pubmed_ids, write_tsv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True, help="New empty output directory")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if any(args.output.iterdir()):
        parser.error("Use an empty output directory")
    pm = f'({clause(DISEASE, "pubmed")} AND "clinical trial, phase iii"[pt] AND ("1900/01/01"[dp] : "{END_DATE.replace("-", "/")}"[dp]))'
    eu = f'({clause(DISEASE, "europepmc")} AND PUB_TYPE:"clinical trial, phase iii" AND FIRST_PDATE:[1900-01-01 TO {END_DATE}])'
    with ThreadPoolExecutor(max_workers=2) as pool:
        pm_future = pool.submit(pubmed_ids, pm)
        eu_future = pool.submit(europe_ids, eu)
        pm_ids, pm_count = pm_future.result()
        eu_ids, eu_count = eu_future.result()
    union = sorted(pm_ids | eu_ids)
    write_tsv(args.output / "membership.tsv", ["source_id", "pubmed", "europepmc"], [
        (key, int(key in pm_ids), int(key in eu_ids)) for key in union
    ])
    rows = []
    for label, ids, q, count in [("pubmed", pm_ids, pm, pm_count), ("europepmc", eu_ids, eu, eu_count)]:
        digest = hashlib.sha256(("\n".join(sorted(ids))+"\n").encode()).hexdigest()
        rows.append((label, count, digest, q))
    write_tsv(args.output / "queries.tsv", ["index", "hits", "sorted_id_sha256", "query"], rows)
    details = {"retrieved_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version.split()[0],
               "cutoff": END_DATE, "union": len(union), "intersection": len(pm_ids & eu_ids)}
    (args.output / "execution.json").write_text(json.dumps(details, indent=2)+"\n")


if __name__ == "__main__":
    main()
