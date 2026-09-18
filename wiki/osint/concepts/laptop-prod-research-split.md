---
title: "Laptop vs prod — Cemini research deployment split"
type: concept
tags: [concept, infrastructure, cemini-internal, research-ops, flox, kronos, arcticdb]
keywords: [laptop, cemini-prod, flox, kronos, arcticdb, egress-fi]
related:
  - meta/librarian-decommission-2026-06-14.md
  - sources/cemini-laptop-prod-research-handoff-2026-05-23.md
  - entities/tools/flox.md
  - entities/tools/arcticdb.md
  - sources/shiyu-coder-kronos.md
  - concepts/librarian-server-architecture.md
  - entities/infrastructure/cemini-egress-fi.md
  - concepts/cemini-repository-topology.md
  - projects/osint-workspace/OSINT Workspace.md
  - projects/osint-workspace/Architecture/Architecture - briefs.md
  - projects/cemini-financial-suite/Cemini Financial Suite.md
maturity: validated
created: 2026-05-23
updated: 2026-09-18
---

## Relations

- @meta/librarian-decommission-2026-06-14.md — Arctic/stash/kb-server offline; raw bulk on egress-fi
- @entities/tools/arcticdb.md — laptop `.local/arctic-market-dataset/` path
- @entities/tools/lazy-tool.md — kb_search unavailable without librarian

- @sources/cemini-laptop-prod-research-handoff-2026-05-23.md — canonical operator brief (from prod → librarian pickup)
- @entities/tools/flox.md — Step 197 **laptop/dev only** (cmake build, not A/B)
- @entities/tools/arcticdb.md — Step 189 live benchmark on librarian bulk data
- @sources/shiyu-coder-kronos.md — Step 109 prompt A/B on prod — **REJECT** 2026-05-23
- @concepts/librarian-server-architecture.md — prod→librarian SSH via `10.0.0.2`
- @entities/infrastructure/cemini-egress-fi.md — HL + PM order egress (live)
- @concepts/cemini-repository-topology.md — git/repo layout vs machine split (orthogonal concerns)
- @projects/osint-workspace/OSINT Workspace.md — laptop repo where wiki + `briefs/` staging live
- @projects/osint-workspace/Architecture/Architecture - briefs.md — gitignored briefs handoff to `/opt/cemini/briefs/`
- @projects/cemini-financial-suite/Cemini Financial Suite.md — deploy monorepo on prod (`/opt/cemini`)

## Raw Concept

`[SUPERSEDED 2026-06-14]` Librarian host deleted — see @meta/librarian-decommission-2026-06-14.md. Historical handoff on **cemini-librarian** (`/opt/cemini-bulk/research/cemini-handoff/`, 2026-05-23).

## Narrative

### Where to work (2026-09-18)

| Step | Task | Run on |
|------|------|--------|
| **OSINT wiki / ingest** | Pages, briefs, lint; raw archive → egress-fi | **Laptop** (+ **egress-fi** bulk) |
| **Lane A / live trading** | XSP, PM, HL, Kalshi | **No host** — Ashburn `cemini-prod` deleted. Wiki/briefs only. No xsp/pm scp. |
| **GuruWatcher** | 15-min alert-only Discord | **egress-fi** (`/opt/guru-watcher`). Never auto-arm watches. Never place orders. |
| **189 ArcticDB / equity backtest** | `refresh_arctic_equity_bars.py`, `.local/arctic-market-dataset/` | **Laptop** |
| **109 Kronos** | (rejected) prompt A/B | **Do not re-run on a deleted prod** |
| **197 FLOX** | C++ benchmark | **Laptop / dev** |

### Historical — where to work (2026-06-14, prod still live)

| Step | Task | Run on |
|------|------|--------|
| **OSINT wiki / ingest** | Pages, briefs, lint; raw archive → egress-fi | **Laptop** (+ **egress-fi** bulk) |
| **Lane A / live trading** | XSP, PM, HL, Kalshi | **cemini-prod** (+ **egress-fi** for HL/PM orders) |
| **189 ArcticDB / equity backtest** | `refresh_arctic_equity_bars.py`, `.local/arctic-market-dataset/` | **Laptop** |
| **109 Kronos** | (rejected) prompt A/B | **cemini-prod** if re-run |
| **197 FLOX** | C++ benchmark | **Laptop / dev** |

### Historical — where to work (pre-decommission)

| Step | Task | Run on |
|------|------|--------|
| **197 FLOX** | C++ connector **build + latency benchmark** | **Laptop / dev host** (cmake, g++, cargo). **Not** cemini-prod (no cmake; ~7 GB RAM). **Not an A/B test.** |
| **109 Kronos** | DeepSeek prompt **A/B** (baseline vs `<kronos_tokens>`) | **cemini-prod** (Postgres `market_ticks_1min` + API keys) |
| **189 ArcticDB** | Live CSV vs Arctic tail-query benchmark | **cemini-librarian** (bulk `market-dataset/`); invoke from prod via private net |
| **OSINT wiki** | Ingest briefs + commit | **This laptop workspace** |

### FLOX ≠ Kronos

- **FLOX Phase 1** = compile + ingest latency benchmark (`cmake -DFLOX_BUILD_CONNECTORS=ON`).
- **Kronos Phase 2** = analyst-prompt A/B on historical ticks.

Do not conflate them in planning or Cursor workspace choice.

### Librarian SSH (fixed 2026-05-23)

From **inside cemini-prod**, `ssh cemini-librarian` via public ProxyJump failed (key loop). **Fix:** private net **`10.0.0.2`** — use `cemini-librarian-internal` or `ssh root@10.0.0.2` or `./scripts/ssh_librarian.sh` on prod.

From **laptop**: `ssh cemini-librarian` (ProxyJump via prod public IP) — unchanged.

### Kronos A/B verdict (prod, 2026-05-23)

10 pairs (BTC-USD only; SPY/NVDA/ETH absent in `market_ticks_1min` last 7d). **REJECT** — 0% directional accuracy both arms; ECE worse with Kronos; CI width gate fail. **Do not enable** Kronos token block in analyst prompts on this sample. Log: `/opt/cemini/logs/kronos_ab_full.log`.

### ArcticDB live benchmark (librarian, 2026-05-23)

200k rows from S&P500 Kaggle CSV: tail-1000 **0.109s pandas vs 0.011s ArcticDB**. Migration remains operator-gated; supports adopt case for repeated tail/range queries on `market-dataset/`.

### Completed 2026-05-23 (this session)

| Step | Outcome |
|------|---------|
| **197 FLOX** | Phase 1a/1b **PASS** on librarian; **Phase 2 live** — `flox-phase2-ws.service` → `intel:polymarket_flox_ws`; prod `FLOX_PHASE2_ENABLED=true` |
| **189 ArcticDB** | **Migrated** `market-dataset` → `lmdb:///opt/cemini-bulk/arctic-market-dataset` (`equity_bars`, 8,507 symbols) |

### Pickup path

`[SUPERSEDED 2026-06-15]` Raw sources: `cemini-egress-fi:/opt/cemini-bulk/research/<wiki-id>/`. Historical: `cemini-librarian:/opt/cemini-bulk/research/cemini-handoff/` (deleted host).

## Snippets

> "You do not need to switch Cursor workspace for Kronos A/B if prod agent can reach Postgres — it is running on prod now." [Source: cemini-handoff/2026-05-23_laptop-vs-prod-research-handoff.md]

> "FLOX Phase 1 is a compile and ingest latency benchmark. Kronos Phase 2 is the prompt A/B." [Source: cemini-handoff/concepts/laptop-prod-research-split.md]
