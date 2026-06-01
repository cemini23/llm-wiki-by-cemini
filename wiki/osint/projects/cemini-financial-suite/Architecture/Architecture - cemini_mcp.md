---
title: Architecture - cemini_mcp (prod)
type: architecture-module
module: cemini_mcp
path: cemini_mcp/
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

Prod module note for `cemini_mcp/` @ e3674e4; ingested from cemini-prod handoff pack.

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

## Runtime (`cemini_mcp/CLAUDE.md`)

- FastMCP 3.x, streamable HTTP, **port 8002 (localhost only)**
- **Read-only** — no order placement via MCP
- Tool groups: regime/signals/playbook, risk/health, conviction/ensemble, macro/sectors, Kalshi/contracts, memory/debate/PnL, `wiki_search`

## Compose

Service `cemini_mcp` in `docker/compose.intelligence.yml` (intelligence stack alongside `brain`, `llm_analyst`, optional MCP sidecars `tradingview_mcp`, `autots_mcp`).

## Data mapping

See `cemini_mcp/CLAUDE.md` table: Redis keys → tools (e.g. `intel:playbook_snapshot`, `intel:kalshi_orderbook_summary`, geopolitical keys).

## kb-server

`wiki_search` tool bridges to indexed wiki on kb-server (host documented in runbooks as `10.0.0.2:3838`); enforcement logic lives in `core/wiki_enforcement.py` used by brain, not inside MCP write path.

## @user notes
