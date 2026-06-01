---
title: Architecture - ems (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
module: ems
path: ems/
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

Prod `ems` @ 8faf94e.

# EMS — Execution Management System

Order routing and broker execution. Split across a **thin service package** (`ems/`) and **shared library** (`core/ems/`).

## Service entry (`ems/`)

<!-- @generated:start -->
| File | Role |
|------|------|
| `main.py` | Async Redis subscriber; validates `TradeSignalEnvelope`; calls `core.ems.router` |
| `kalshi_rest.py`, `kalshi_rest_legacy.py` | Kalshi REST v2 client for executor |
| `kalshi_market_status.py` | Freshness / active-market gate via sync Redis |
| `kalshi_ping.py` | Health probe |
<!-- @generated:end -->

## Redis / governor

| Setting | Default / role |
|---------|----------------|
| Channel | **`trade_signals`** — async listener in `main.py` |
| `GOVERNOR_URL` | `http://risk_governor:8004` — pre-trade HTTP check |
| `PAPER_MODE` | Env `PAPER_MODE` (default false string; paper adapter registered) |
| Kalshi client | `KalshiRESTv2`, environment `demo` in code default |

`main.py` initializes adapters: `PaperBrokerAdapter`, `CoinbaseAdapter`, `RobinhoodAdapter`, `HardRockBetAdapter`, optional `HyperliquidAdapter`, `OANDAAdapter`, plus `KalshiRESTv2`. Calls risk governor at `GOVERNOR_URL` (default `http://risk_governor:8004`). `PAPER_MODE` from env.

## Library (`core/ems/`)

| Area | Files |
|------|-------|
| Router | `router.py`, `smart_order_router.py` |
| Adapters | `adapters/{paper,coinbase,robinhood,hyperliquid,oanda,kalshi_rest,kalshi_fix,...}.py` |
| Gates | `freshness_gate.py`, `cvar_gate.py`, `position_gate.py`, `trust_gate.py`, `llm_gate.py` |
| Review | `rejection_reviewer.py` |

## Docker

| Property | Value |
|----------|-------|
| Service | `ems` in `docker/compose.execution.yml` |
| Image | `cemini-ems:latest` |
| Container | `ems_executor` |
| User | `1000:1000` (non-root) |
| Volumes | ArcticDB data, tokens mount, Kalshi private key, archives, scripts |

## Upstream / downstream

- **Upstream:** Redis channels carrying `TradeSignalEnvelope` from `agents/` brain cycle; governor decisions from `risk_governor`.
- **Downstream:** Broker APIs (Kalshi demo env default in `main.py`), Postgres `trade_history` per README data pipeline.

## Related compose services

`kalshi_autopilot`, `rover_scanner`, `risk_governor`, `opportunity_screener` in `docker/compose.execution.yml`.

## @user notes
