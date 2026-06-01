---
title: Architecture - cemini_mcp (prod)
type: architecture-module
module: cemini_mcp
path: cemini_mcp/
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

Prod module `cemini_mcp` @ de5ad93; gap-close handoff.

# cemini_mcp — Read-Only MCP Intelligence Server

Exposes Cemini `intel:*` Redis state and selected Postgres risk readers as typed MCP tools for operator agents and UI backends.

## Layout

<!-- @generated:start -->
| File | Role |
|------|------|
| `server.py` | FastMCP tool definitions (`@mcp.tool`) — canonical tool count |
| `readers.py` | Redis GET + staleness detection; Postgres risk reader |
| `config.py` | `REDIS_HOST`, `REDIS_PASSWORD`, `MCP_PORT`, etc. |
| `cemini_ai_proxy.py`, `conviction_ui_data.py`, `*_ui_data.py` | UI/MCP data facades for design surfaces |
| `pm_backtest_engine.py`, `pm_backtest_store.py` | PM backtest helpers |
| `Dockerfile` | Container image for compose `cemini_mcp` service |
| `tests/test_tools.py` | Asserts tool inventory count (source of truth per CLAUDE.md) |
<!-- @generated:end -->

## Tool inventory (@8f319d9)

<!-- @generated:start -->
**29** `@mcp.tool` functions in `server.py` (see `cemini_mcp/tests/test_tools.py` — `len(tools) == 29`).

| Tool | Tier notes |
|------|------------|
| `get_regime_status`, `get_signal_detections`, `get_playbook_snapshot`, `get_strategy_mode` | Regime / playbook |
| `get_risk_metrics`, `get_data_health`, `get_stream_health` | Risk / health |
| `get_conviction`, `get_ensemble_signal`, `get_agent_weights`, `get_regime_adjusted_weights`, `get_ticker_conviction`, `get_trust_scores` | Conviction / ensemble |
| `get_fred_macro`, `get_sector_rotation`, `get_vol_surface`, `get_earnings_calendar`, `get_geopolitical_risk`, `get_sentiment` | Macro / sectors |
| `get_kalshi_intel`, `get_contract_pricing` | Kalshi |
| `query_similar_situations`, `get_debate_summary`, `get_decision_journal`, `get_pnl_attribution`, `get_walk_forward_results`, `get_fuzzy_scalar` | Memory / debate |
| `wiki_search` | kb-server bridge |
| `notify_operator` | Tier 2 — `destructive: True` (operator alert; not read-only) |
<!-- @generated:end -->

## Runtime (`cemini_mcp/CLAUDE.md`)

- FastMCP 3.x, streamable HTTP, **port 8002 (localhost only)**
- Most tools: **read-only** — no order placement via MCP except `notify_operator`

## Compose

Service `cemini_mcp` in `docker/compose.intelligence.yml` (intelligence stack alongside `brain`, `llm_analyst`, optional MCP sidecars `tradingview_mcp`, `autots_mcp`).

## Data mapping

See `cemini_mcp/CLAUDE.md` table: Redis keys → tools (e.g. `intel:playbook_snapshot`, `intel:kalshi_orderbook_summary`, geopolitical keys).

## kb-server

`wiki_search` tool bridges to indexed wiki on kb-server (host documented in runbooks as `10.0.0.2:3838`); enforcement logic lives in `core/wiki_enforcement.py` used by brain, not inside MCP write path.

## @user notes
