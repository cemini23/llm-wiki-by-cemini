---
title: Architecture - cemini_mcp (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
module: cemini_mcp
path: cemini_mcp/
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

Prod `cemini_mcp` @ 8faf94e.

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
| `notify_operator` | Tier 2 — see below |
<!-- @generated:end -->

### `notify_operator` (tier 2, non-read-only)

From `server.py`: validates `OperatorAlert`, **XADD** `stream:intel:operator_alerts` (MAXLEN ~1000). Phase 1 routes via **picobot** → Telegram (`telegram_dispatcher` service). RBAC tier 2 — failures return error dict, do not raise on hot path. Channels: `telegram` (wired), `discord` / `slack` / `whatsapp` validate but may no-op.

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
