---
title: Architecture - shared and intelligence (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave4]
keywords: [Cemini-Financial-Suite, /opt/cemini, e8fd49f]
deploy-root: /opt/cemini
scanned-commit: e8fd49f
provenance: prod-briefs-out-architecture-2026-06-01-wave4
ai-first: true
module: shared and intelligence
path: shared/
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md

## For future Claude

Prod `shared and intelligence` @ e8fd49f.

# shared/ & intelligence/ — ML feature & vector layer

## shared/ (31 source files)

Import rules: `cemini_contracts`, `core` only. Used by `rl_training`, `services`, `debate_protocol`.

| Module | Role |
|--------|------|
| `training_budget.py` | Training budget guards |

## intelligence/ (9 source files)

Import rules: `cemini_contracts`, `core`. Vector / embedding stack for memory retrieval.

| Module | Role |
|------|------|
| `vector_store.py`, `embedder.py` | Embeddings storage |
| `retriever.py`, `realtime_worker.py` | Retrieval workers |
| `seeder.py`, `config.py` | Bootstrap / config |

MCP: `query_similar_situations` reads memory layer via @projects/cemini-financial-suite/Architecture/Architecture - cemini_mcp.md.

## research/ (37 files)

Step experiments, benchmarks (e.g. step108 langextract, step189 ArcticDB). Not production runtime — see `research/` and `briefs/2026-05-23_*` handoffs.

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - agents.md — optional RL / TOT paths
- @projects/cemini-financial-suite/Architecture/Architecture - data plane.md

## @user notes
