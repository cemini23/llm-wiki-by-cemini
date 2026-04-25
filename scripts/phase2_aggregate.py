#!/usr/bin/env python3
"""Aggregate entities/concepts across all 5 phase-1 manifests."""
import json
from collections import Counter, defaultdict
from pathlib import Path

MANIFESTS = [
    "/tmp/phase1_agent1_small.json",
    "/tmp/phase1_agent2_method.json",
    "/tmp/phase1_agent3_infra_strat.json",
    "/tmp/phase1_agent4_crypto.json",
    "/tmp/phase1_agent4_unblocked_docx.json",
]

entity_counter = Counter()
concept_counter = Counter()
ticker_counter = Counter()
entity_sources = defaultdict(set)
concept_sources = defaultdict(set)

def iter_entries(data):
    """Yield (slug, entry) pairs regardless of dict/list shape."""
    if isinstance(data, dict):
        if "completed_sources" in data:
            for e in data["completed_sources"]:
                yield e.get("slug", "?"), e
        elif "entries" in data:
            for e in data["entries"]:
                yield e.get("slug", "?"), e
        else:
            # dict of slug -> entry
            for k, v in data.items():
                if isinstance(v, dict) and ("title" in v or "entities" in v):
                    yield k, v
    elif isinstance(data, list):
        for e in data:
            if isinstance(e, dict):
                yield e.get("slug", "?"), e

for path in MANIFESTS:
    p = Path(path)
    if not p.exists():
        print(f"MISSING: {path}")
        continue
    data = json.loads(p.read_text())
    manifest_name = p.stem
    for slug, entry in iter_entries(data):
        for e in entry.get("entities", []) or []:
            if isinstance(e, str):
                entity_counter[e] += 1
                entity_sources[e].add(slug)
        for c in entry.get("concepts", []) or []:
            if isinstance(c, str):
                concept_counter[c] += 1
                concept_sources[c].add(slug)
        for t in entry.get("tickers_mentioned", []) or entry.get("tickers", []) or []:
            if isinstance(t, str):
                ticker_counter[t] += 1

print("=" * 60)
print(f"TOTAL unique entities: {len(entity_counter)}")
print(f"TOTAL unique concepts: {len(concept_counter)}")
print(f"TOTAL unique tickers:  {len(ticker_counter)}")
print()
print("TOP 40 ENTITIES (by mentions across manifests):")
for name, n in entity_counter.most_common(40):
    src_count = len(entity_sources[name])
    print(f"  {n:3d}  [{src_count:2d} srcs]  {name}")
print()
print("TOP 40 CONCEPTS (by mentions):")
for name, n in concept_counter.most_common(40):
    src_count = len(concept_sources[name])
    print(f"  {n:3d}  [{src_count:2d} srcs]  {name}")
print()
print("TOP 30 TICKERS:")
for t, n in ticker_counter.most_common(30):
    print(f"  {n:3d}  {t}")

# Write full aggregation for downstream use
out = {
    "entities": [
        {"name": n, "mentions": c, "source_count": len(entity_sources[n]),
         "sources": sorted(entity_sources[n])}
        for n, c in entity_counter.most_common()
    ],
    "concepts": [
        {"name": n, "mentions": c, "source_count": len(concept_sources[n]),
         "sources": sorted(concept_sources[n])}
        for n, c in concept_counter.most_common()
    ],
    "tickers": [
        {"ticker": t, "mentions": c} for t, c in ticker_counter.most_common()
    ],
}
Path("/tmp/phase2_aggregated.json").write_text(json.dumps(out, indent=2))
print()
print("Wrote /tmp/phase2_aggregated.json")
