---
title: Architecture - ui (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
module: ui
path: ui/
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

Prod `ui` @ 8faf94e.

# ui & design — Operator surfaces

Two surfaces: **Streamlit app** (container) and **static HTML desk** (nginx).

## Streamlit — `ui/`

| File | Role |
|------|------|
| `app.py` | Cemini OS entry |
| `dashboard.py`, `performance.py` | Dashboards |
| `replay.py`, `replay_helpers.py` | Replay tooling |
| `cemini_ai_client.py` | AI assistant client |

Compose: `cemini_os` (`docker/compose.ui.yml`) — port **8501** behind nginx.

## Static desk — `design/`

Served on **port 80** by `cemini_proxy` / nginx — **not** MCP port 8002.

Evidence: `design/README.md` — hub at `/design/index.html`, shared CSS/JS tokens.

### Data-mode badges

`CeminiBadges` (`design-badges.js`): LIVE, PARTIAL, STALE, MOCK, GATED, SIMULATED, OFFLINE.

Kalshi cards need `intel:logit_assessments` for full fair value — else **PARTIAL** (orderbook only).

### Page → API map (sample)

| Page | API |
|------|-----|
| kalshi.html | `/api/kalshi/markets`, `/api/kalshi/market-cards` |
| polymarket.html | `/api/polymarket/markets` |
| conviction.html | `/api/conviction`, `/api/regime` |

Full routes: `grep custom_route cemini_mcp/server.py` (REST on MCP host).

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - cemini_mcp.md
- @projects/cemini-financial-suite/Architecture/Architecture - logit_pricing.md — Kalshi fair value intel
- @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md — `nginx`, `grafana`, `deephaven`

## @user notes
