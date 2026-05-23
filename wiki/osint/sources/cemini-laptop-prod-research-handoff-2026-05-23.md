---
title: "Cemini prod → OSINT handoff — FLOX, Kronos A/B, ArcticDB, librarian SSH (2026-05-23)"
type: source
tags: [source, brief, cemini-internal, infrastructure, handoff, prod]
keywords: [laptop-vs-prod, flox, kronos, arcticdb, librarian-internal, step109, step189, step197]
related:
  - concepts/laptop-prod-research-split.md
  - entities/tools/flox.md
  - entities/tools/arcticdb.md
  - sources/shiyu-coder-kronos.md
  - concepts/librarian-server-architecture.md
maturity: validated
created: 2026-05-23
updated: 2026-05-23
read_status: read
---

## Relations

- @concepts/laptop-prod-research-split.md — synthesized deployment split
- @entities/tools/flox.md — Step 197 laptop build
- @entities/tools/arcticdb.md — Step 189 benchmark artifact
- @sources/shiyu-coder-kronos.md — Step 109 A/B outcome
- @concepts/librarian-server-architecture.md — `10.0.0.2` internal SSH

## Raw Concept

- **Title**: Laptop vs prod — FLOX, Kronos A/B, librarian SSH (operator handoff)
- **Origin**: cemini-prod → staged on cemini-librarian for laptop pickup
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/cemini-handoff/`; local copy `briefs/2026-05-23_laptop-vs-prod-research-handoff.md`
- **Retrieved**: 2026-05-23
- **Read status**: read

## Narrative

Full operator brief covering: (1) **FLOX** on laptop only — not prod, not A/B; (2) **Kronos A/B** on prod — completed **REJECT**; (3) **ArcticDB** live benchmark on librarian — strong tail-query speedup; (4) **prod→librarian SSH** via private `10.0.0.2`.

Prod files touched: `~/.ssh/config` (`cemini-librarian-internal`), `scripts/ssh_librarian.sh`, `research/step189_arcticdb/benchmark_parquet_vs_arctic.py`, `briefs/step189_arcticdb_benchmark_live.json`.

Re-run Kronos: `python3 scripts/kronos_ab_test.py` on prod with Postgres + `.env` loaded.

## Snippets

| Metric (Kronos A/B) | Baseline | Kronos |
|---------------------|----------|--------|
| Directional accuracy | 0.000 | 0.000 |
| ECE | 0.05 | 0.21 |
| Verdict | | **REJECT** |

[Source: cemini-handoff/briefs/2026-05-23_kronos-ab-test-results.md]

| Metric (200k rows) | pandas | ArcticDB |
|--------------------|--------|----------|
| read / tail-1000 | 0.112s / 0.109s | 0.014s / **0.011s** |

[Source: cemini-handoff/briefs/step189_arcticdb_benchmark_live.json]
