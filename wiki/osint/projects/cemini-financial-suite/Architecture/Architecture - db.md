---
title: Architecture - db (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave4]
keywords: [Cemini-Financial-Suite, /opt/cemini, e8fd49f]
deploy-root: /opt/cemini
scanned-commit: e8fd49f
provenance: prod-briefs-out-architecture-2026-06-01-wave4
ai-first: true
module: db
path: db/
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
  - projects/cemini-financial-suite/Architecture/Architecture - db ERD.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md
- @projects/cemini-financial-suite/Architecture/Architecture - db ERD.md

## For future Claude

Prod `db` @ e8fd49f.

# db — TimescaleDB schema & migrations

Postgres 16 + TimescaleDB + pgvector. Migrations via **dbmate** (`docker/compose.infra.yml` → `dbmate` service). Canonical ops doc: `db/README.md`.

## Credentials (verified in db/README)

| Field | Value |
|-------|-------|
| User | `admin` (not `cemini`) |
| Database | `qdb` |
| Host (containers) | `postgres` |
| Port | `5432` |
| Password | `${POSTGRES_PASSWORD}` from `.env` |

## Migration workflow

```bash
dbmate new my_migration_name
# apply via docker + data_net (see db/README)
./scripts/dump_schema.sh --docker   # never raw dbmate dump
```

Every migration must include `-- migrate:up` and `-- migrate:down` or dbmate no-ops silently.

## Schema dump rule

`scripts/dump_schema.sh` excludes `_timescaledb_internal` chunks — prevents daily hypertable chunk churn in `db/schema.sql`.

## Major table families (logical — not full ERD)

| Family | Examples / consumers |
|--------|---------------------|
| Market ticks | `raw_market_ticks` — ingestion → brain/analytics |
| Playbook | `playbook_logs` — `trading_playbook` JSONB |
| Trades / audit | EMS trade history, audit archives |
| PM / Kalshi extensions | Migrations under `db/migrations/` for sleeve-specific tables |

**Logical ERD:** @projects/cemini-financial-suite/Architecture/Architecture - db ERD.md (52 tables, domain diagram).

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md — `postgres`, `dbmate`, exporters
- @projects/cemini-financial-suite/Architecture/Architecture - trading_playbook.md — `playbook_logs`
- @projects/cemini-financial-suite/Architecture/Architecture - data plane.md — ArcticDB vs Postgres division

## @user notes
