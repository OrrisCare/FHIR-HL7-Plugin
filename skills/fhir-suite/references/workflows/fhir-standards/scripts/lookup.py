#!/usr/bin/env python3
"""Search the bundled HL7 metadata offline; never sends queries or patient data."""
import argparse
import json
from pathlib import Path
import re

DATA = Path(__file__).resolve().parents[1] / "references" / "indexes"


def search(records, query):
    terms = re.findall(r"[a-z0-9]+", query.lower())
    if not terms:
        return []
    ranked = []
    for record in records:
        text = json.dumps(record, ensure_ascii=False).lower()
        if all(term in text for term in terms):
            names = [str(record.get(k, "")).lower() for k in ("id", "name", "title", "type")]
            score = sum(10 for name in names if name == query.lower())
            score += sum(1 for name in names for term in terms if term in name)
            ranked.append((-score, str(record.get("id", record.get("url", ""))), record))
    return [r[2] for r in sorted(ranked, key=lambda r: (r[0], r[1]))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--kind", choices=("all", "resources", "artifacts", "pages"), default="all")
    parser.add_argument("--limit", type=int, default=12)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    records = []
    for kind in ("resources", "artifacts", "pages"):
        if args.kind in (kind, "all"):
            records.extend(dict(record, index_kind=kind) for record in json.loads((DATA / f"{kind}.json").read_text()))
    results = search(records, args.query)
    print(json.dumps({"release": "5.0.0", "matches": len(results), "returned": min(len(results), args.limit),
                      "results": results[:args.limit]}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
