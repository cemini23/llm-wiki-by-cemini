---
title: Architecture - services (prod)
type: architecture-module
module: services
path: services/
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, gap-close]
keywords: [Cemini-Financial-Suite, /opt/cemini, de5ad93]
deploy-root: /opt/cemini
scanned-commit: de5ad93
provenance: prod-briefs-out-architecture-2026-06-01-gap-close
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md — project hub
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md — MOC

## For future Claude

Prod module `services` @ de5ad93; gap-close handoff.

# services — Long-running sidecars & domain services

Largest Python package in the monorepo (141 source files @ `de5ad93`). Docker images for many intelligence/ingestion containers build from here. Import rules: may use `cemini_contracts`, `core`, `shared`, `intelligence`, `risk` (`check_imports.py`).

## Subdirectories (compose-backed)

<!-- @generated:start -->
| Path | Compose service(s) | Role |
|------|-------------------|------|
| `llm_analyst/` | `llm_analyst` | Polymarket CLOB adapters, conductor/autots clients, PM execution helpers |
| `tradingview_mcp/` | `tradingview_mcp` | TradingView MCP sidecar |
| `structured_generation/` | (library) | Structured LLM outputs |
| `telegram_dispatcher/` | `telegram_dispatcher` | Operator notifications |
| `picobot/` | `picobot` | Picobot integration |
| `claude_code_router/` | — | Router utilities |
| `optimization/` | — | UCB / Monte Carlo (optional `TOT_ENABLED` in brain) |
| `risk/` | — | Monte Carlo, risk helpers for agents |
| `paper_trader/` | — | Paper trading utilities |
| `websocket/` | — | WS clients |
| `webhooks/` | — | Inbound webhooks |
| `rbac/` | — | RBAC helpers |
<!-- @generated:end -->

## Top-level modules (selected)

| Module | Role |
|--------|------|
| `hyperliquid_shadow_logger.py` | HL funding / shadow logging (`hyperliquid-shadow-logger`) |
| `crypto_spot_shadow_logger.py` | Crypto spot shadow |
| `forex_shadow_logger.py` | Forex shadow |
| `kalshi_shadow_logger.py` | Kalshi shadow telemetry |
| `news_sentiment_harvester.py` | `news_sentiment_harvester` container |
| `conviction_aggregator.py` | Conviction composite for intel bus |
| `hitl_approval_gate.py` | Human-in-the-loop gate |
| `pipeline_phase_gate.py` | Pipeline phase registry enforcement |
| `pm_btc_position_gate.py` | PM BTC up/down position gate |
| `ensemble_combiner.py` | Ensemble signal combination |
| `byzantine_consensus.py` | Multi-agent consensus contracts impl |

## What is NOT in `services/`

- **Brain cycle:** `agents/orchestrator.py` (container `brain`)
- **EMS process:** `ems/main.py` (container `ems_executor`)
- **Playbook loop:** `trading_playbook/runner.py` (container `playbook`)

## Related docs

- @projects/cemini-financial-suite/Architecture/Architecture - Polymarket.md — PM-specific paths under `llm_analyst/`
- @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md

## @user notes
