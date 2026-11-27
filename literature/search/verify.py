"""Verify archived per-query counts, identifier digests and completed screening denominators."""
import csv
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def records(stream):
    return list(csv.DictReader(stream, delimiter="\t"))


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def verify_run(name):
    directory = HERE / name
    with gzip.open(directory / "membership.tsv.gz", "rt", encoding="utf-8") as stream:
        rows = records(stream)
    ids = [row["source_id"] for row in rows]
    meta = json.loads((directory / "execution.json").read_text())
    require(len(set(ids)) == len(ids) == meta["source_id_union"], f"{name}: invalid identifier union")
    with (directory / "queries.tsv").open() as stream:
        queries = records(stream)
    for query in queries:
        column = query["index"] + "_arms"
        matches = sorted(row["source_id"] for row in rows if query["arm"] in row[column].split(","))
        require(len(matches) == int(query["hits"]), f"{name}: count mismatch {query['arm']}")
        digest = hashlib.sha256(("\n".join(matches) + "\n").encode()).hexdigest()
        require(digest == query["sorted_id_sha256"], f"{name}: digest mismatch {query['arm']}")
    print(f"{name}: {len(queries)} queries and {len(rows)} source identifiers verified")
    return rows


def verify_screen(name, expected_ids):
    with (HERE / name).open() as stream:
        rows = records(stream)
    ids = [row["source_id"] for row in rows]
    require(len(set(ids)) == len(rows) and set(ids) == expected_ids, f"{name}: incomplete or duplicated screen")
    for row in rows:
        require(all(row[k].strip() for k in ["decision", "decision_reason", "source_link", "screen_basis"]), f"{name}: incomplete row")
        if row["decision"] == "version":
            require(row["related_version_id"] in expected_ids, f"{name}: missing paired record")
    print(f"{name}: all {len(rows)} source records have dispositions")


if __name__ == "__main__":
    census = verify_run("census")
    update = verify_run("november")
    historical = verify_run("historical")
    focus = {r["source_id"] for r in census if "focus_" in r["pubmed_arms"] + r["europepmc_arms"]}
    verify_screen("focus-screen.tsv", focus)
    verify_screen("november-screen.tsv", {r["source_id"] for r in update})
    verify_screen("historical-screen.tsv", {r["source_id"] for r in historical})
