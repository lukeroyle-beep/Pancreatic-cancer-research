"""Offline integrity check for the archived phase III corpus and decisions."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


def rows(name):
    with (Path(__file__).resolve().parent / name).open() as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def main():
    members = rows("membership.tsv")
    screened = rows("screen.tsv")
    execution = json.loads(Path(__file__).with_name("execution.json").read_text())
    membership = {r["source_id"] for r in members}
    ledger = {"MED:" + r["pmid"] for r in screened}
    if not (len(membership) == len(members) == len(screened) == execution["union"] and ledger == membership):
        raise ValueError("Screening ledger and membership disagree")
    for query in rows("queries.tsv"):
        keys = sorted(r["source_id"] for r in members if r[query["index"]] == "1")
        digest = hashlib.sha256(("\n".join(keys)+"\n").encode()).hexdigest()
        if len(keys) != int(query["hits"]) or digest != query["sorted_id_sha256"]:
            raise ValueError("Inconsistent search counts or identifiers for " + query["index"])
    if any(not r["screen_decision"] or not r["screen_reason"] for r in screened):
        raise ValueError("Unscreened record")
    if sum(r["pubmed"] == r["europepmc"] == "1" for r in members) != execution["intersection"]:
        raise ValueError("Inconsistent published overlap")
    print(f"Verified {len(membership)} identifiers and screening decisions")
    for decision, count in sorted(Counter(r["screen_decision"] for r in screened).items()):
        print(f"{count:3} {decision}")


if __name__ == "__main__":
    main()
