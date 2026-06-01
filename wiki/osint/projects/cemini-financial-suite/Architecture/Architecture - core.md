---
title: Architecture - core (prod)
type: architecture-module
module: core
path: core/
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff]
keywords: [Cemini-Financial-Suite, /opt/cemini, deploy-monorepo]
deploy-root: /opt/cemini
scanned-commit: e3674e4
provenance: prod-briefs-out-architecture-2026-06-01
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md

## For future Claude

Prod module note for `core/` @ e3674e4; ingested from cemini-prod handoff pack.

# core — Shared Brain Contracts & Platform Logic

Largest shared Python package for cross-cutting trading intelligence, validation gates, and EMS library code. Scan: 107 source files under `core/`.

## Major sub-areas (directory listing)

<!-- @generated:start -->
| Subpath | Evidence | Role |
|---------|----------|------|
| `core/ems/` | 19 adapter/router modules | Broker adapters, gates (CVaR, freshness, trust, LLM), `smart_order_router.py` |
| `core/schemas/` | `trading_signals.py` etc. | Signal types consumed by agents + EMS |
| `core/intel_bus.py` | `IntelPublisher`, `IntelReader` | Redis `intel:*` pub/sub helpers |
| `core/intel_bus_v2.py`, `intel_streams.py` | larger modules | Extended intel streaming |
| `core/hyperliquid_funding/` | package | HL funding carry / risk helpers |
| `core/pm_kl_execution/` | package | Polymarket ↔ Kalshi execution alignment |
| `core/debate/`, `core/data/` | packages | Debate + data utilities |
| `core/wiki_enforcement.py` | gate + abort logging | kb-server / wiki policy enforcement for orchestrator |
| `core/failure_corrective.py` | module | Failure rollup / corrective hooks |
| `core/kalshi_slippage.py` | module | Kalshi slippage modeling |
<!-- @generated:end -->

## Intel bus (integration contract)

`IntelPublisher` / `IntelReader` in `core/intel_bus.py` connect brain, harvesters, and `cemini_mcp` readers to Redis keys documented in `cemini_mcp/CLAUDE.md` (e.g. `intel:playbook_snapshot`, `intel:geopolitical_risk`).

## EMS library vs EMS service

- **Library:** `core/ems/` — adapters (paper, robinhood, coinbase, hyperliquid, oanda, kalshi_*), router, gates.
- **Service entry:** `ems/main.py` — Docker `ems_executor` process subscribing to Redis signals.

## Contracts boundary

Runtime validation uses `cemini_contracts.safe_validate` and typed payloads (`TradeSignalEnvelope`, `IntelPayload`, `GovernorDecision`) imported from the sibling `cemini_contracts/` package (78 source files).

## db/ sibling

`db/` (85 files) holds SQL migrations and schema; pairs with TimescaleDB service in `docker/compose.infra.yml`. Not duplicated here — see `db/README.md`.

## @user notes
