---
title: Architecture - data plane (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
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

Prod `data plane` @ 8faf94e.

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

| Item | Evidence |
|------|----------|
| Compose | `deephaven` in `docker/compose.ui.yml` — port **10000**, volume `deephaven_data` |
| Notebooks mount | `../ui:/notebooks/ui:ro` — loads `ui/dashboard.py` |
| App code | `ui/dashboard.py` — `deephaven.ui` + Postgres reads (`raw_market_ticks`, `ai_trade_logs`) |
| Hardening | `tests/test_docker_user_audit.py` — PENDING_HARDENING (Java `/cache/` uid) |

Operator analytics shell over TimescaleDB; not on the trading hot path.

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - ems.md
- @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md

## @user notes
