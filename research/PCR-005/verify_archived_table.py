"""Check the published LockedDesign 1.0.0 table without running design software."""
import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


def inspect(path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != "e8d326a068dcebced14ca727869d1323405b37da26020e913b6c4ac0370a14cd":
        raise ValueError("Archived table differs from the inspected release")

    methods = Counter()
    groups = defaultdict(list)
    structures = set()
    cells = set()
    with path.open(encoding="utf-8", newline="") as stream:
        rows = csv.reader(stream)
        headings = next(rows)
        lengths = [i for i, name in enumerate(headings) if name == "n"]
        if len(lengths) != 2:
            raise ValueError("Expected two columns named n in this release")
        cell, seed, structure, algorithm = (
            headings.index(name) for name in ("param_counter", "seed", "ss", "algo")
        )
        for line, row in enumerate(rows, start=2):
            if len(row) != len(headings) or row[lengths[0]] != row[lengths[1]]:
                raise ValueError(f"Column count or target lengths disagree on line {line}")
            methods[row[algorithm]] += 1
            cells.add(row[cell])
            structures.add(row[structure])
            groups[row[cell], row[seed]].append((row[structure], row[algorithm]))

    for key, pair in groups.items():
        if (len(pair) != 2 or pair[0][0] != pair[1][0]
                or {method for _, method in pair} != {"rndC", "locked2C"}):
            raise ValueError(f"Incomplete or mismatched target pair at {key}")

    return {
        "archive_sha256": digest,
        "rows": sum(methods.values()),
        "rows_by_algorithm_label": dict(methods),
        "parameter_cells": len(cells),
        "paired_target_draws": len(groups),
        "distinct_target_structures": len(structures),
        "length_columns_checked": len(lengths),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", type=Path)
    print(json.dumps(inspect(parser.parse_args().results), indent=2, sort_keys=True))
