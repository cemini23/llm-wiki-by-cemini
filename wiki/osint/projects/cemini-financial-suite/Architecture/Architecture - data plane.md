---
title: Architecture - data plane (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave4]
keywords: [Cemini-Financial-Suite, /opt/cemini, e8fd49f]
deploy-root: /opt/cemini
scanned-commit: e8fd49f
provenance: prod-briefs-out-architecture-2026-06-01-wave4
ai-first: true
module: data plane
path: db/
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

Prod `data plane` @ e8fd49f.

# Data plane — Postgres, Redis, ArcticDB, Deephaven

## Division of responsibility

| Store | Primary use | Path / service |
|-------|-------------|----------------|
| **TimescaleDB** | Canonical SQL: ticks, playbook, trades, PM tables | `postgres`, @projects/cemini-financial-suite/Architecture/Architecture - db.md |
| **Redis** | `intel:*` pub/sub, `trade_signals`, streams | `redis`, `core/intel_bus.py` |
| **ArcticDB** | Bulk equity bars + live QuantOS library (LMDB volume) | `core/storage/arctic_manager.py`, EMS volume `arcticdb_data` |
| **Deephaven** | Analytics UI (compose optional) | `deephaven` in `compose.ui.yml` |
| **JSONL archives** | Playbook, audit intents, PM logs | `archives/`, `logs/` on host |

## ArcticDB (evidence)

- `ArcticDBManager` — `ARCTIC_URI` default `lmdb:///data/arcticdb`
- Libraries: `ARCTIC_EQUITY_LIBRARY` (`equity_bars`), `ARCTIC_LIVE_LIBRARY` (`quantos_historical`)
- EMS mounts `arcticdb_data:/data/arcticdb` (`compose.execution.yml`)
- Bulk benchmark path on librarian documented in `briefs/2026-05-23_laptop-vs-prod-research-handoff.md` (Step 189)

## Deephaven

Declared in `docker/compose.ui.yml` with `deephaven_data` volume. **Usage wiring in app code:** minimal in this tree — treat as operator analytics shell unless extended.

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - ems.md
- @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md

## @user notes
