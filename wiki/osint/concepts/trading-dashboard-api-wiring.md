---
title: Trading dashboard API wiring — design UI to cemini_mcp REST
type: concept
tags: [concept, frontend, backend, api, fastapi, redis, cemini-prod, ui, k75]
keywords: [ui_routes, cemini_mcp, custom_route, api_envelope, design-pages, watchlist, redis-intel, snapshot-delta, nginx]
related:
  - concepts/cemini-ai-assistant.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/production-trading-blind-spots.md
  - concepts/equity-fair-value-evaluation.md
  - concepts/polymarket-api-reference.md
  - entities/infrastructure/cemini-stack.md
  - entities/infrastructure/cemini-egress-fi.md
maturity: validated
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/cemini-ai-assistant.md — Cemini AI chat gateway (egress-fi); separate from design/ static pages
- @concepts/trading-bot-logging-discipline.md — UI `status: error` should trigger ops logs, not silent mock data
- @concepts/production-trading-blind-spots.md — row 10: stale UI vs live prod
- @concepts/equity-fair-value-evaluation.md — screener/conviction APIs expose related intel
- @concepts/polymarket-api-reference.md — external PM APIs; UI reads internal Redis/intel layer
- @entities/infrastructure/cemini-stack.md — `cemini_mcp`, `cemini_proxy`, Redis, Postgres
- @entities/infrastructure/cemini-egress-fi.md — laptop `ui/serve.py` proxy pattern for AI chat

## Raw Concept

What prompted this page: gap between static `design/*.html` pages and prod backends. Read-only audit of cemini-prod (2026-05-28): **`cemini_mcp` hosts both MCP tools and REST `/api/*` routes** via `ui_routes.py` + inline routes in `server.py`. Laptop `ui/` folder proxies Cemini AI only — not the full trading dashboard.

## Narrative

### Architecture (prod)

```
design/*.html (static, served via nginx / cemini_proxy)
    → fetch("/api/...")
        → cemini_mcp container (FastMCP + Starlette custom_route)
            → Redis intel:* readers (IntelReader / readers.read_intel)
            → Postgres via docker exec psql OR async services
            → optional proxy to cemini-egress-fi (Cemini AI)
```

**Not the primary UI path**: Streamlit (`ui/app.py` exists on prod tree but **not in running container set** per @entities/infrastructure/cemini-stack.md). **Grafana** = ops/metrics UI; **design/** = product/analyst HTML dashboards.

### Response envelope

Most routes use `cemini_contracts.api_responses.envelope()`:

```json
{
  "status": "live" | "empty" | "error",
  "data": { ... },
  "source": "intel:polymarket_snapshot",
  "ttl_seconds": 300,
  "error": "optional"
}
```

Frontend must treat `empty` and `error` differently from `live` — @concepts/production-trading-blind-spots.md row 10.

CORS: `_API_HEADERS = {"Access-Control-Allow-Origin": "*", ...}` on selected routes.

### Route inventory (cemini_mcp, 2026-05-28)

**Core dashboard** (`server.py`):

| Route | Purpose |
|-------|---------|
| `GET /health` | MCP server health |
| `GET /metrics` | Prometheus |
| `GET /api/watchlist` | Live prices + signals for ticker grid |
| `GET /api/regime` | Macro weather regime |
| `GET /api/conviction` | Aggregate conviction |
| `GET /api/signals` | Signal detections |
| `GET /api/action-card` | Action card bundle |
| `GET /api/data-health` | Ingest freshness |
| `GET /api/sentiment` / `/api/sentiment/all` | Sentiment quadrants |
| `GET /api/debate` / `/api/ensemble` | LangGraph debate outputs |
| `GET /api/ticks` | CAGG market_ticks_1min |
| `GET /api/regime-history` | Playbook logs |
| `GET /api/stream-health` | Redis `stream:intel:*` diagnostic |
| `GET /api/kalshi/markets` | Kalshi intel wrapper |
| `GET /api/kalshi/edge` | Contract pricing / fair value |
| `GET /api/calendar/events` | Master calendar |
| `GET /api/earnings/calendar` | Earnings events |

**Registered in `ui_routes.py`**:

| Route | Purpose |
|-------|---------|
| `/api/polymarket/markets` | FLOX or intel snapshot → market rows |
| `/api/polymarket/shadow-log` | Shadow trades (Postgres) |
| `/api/polymarket/edge` | Edge assessments |
| `/api/polymarket/lp-rewards` | LP dashboard |
| `/api/polymarket/updown/execution` | BTC up/down fill telemetry |
| `/api/screener/watchlist` | Watchlist + screener shape |
| `/api/screener/breadth` | Breadth payload |
| `/api/backtest/*` | Backtest status + runs |
| `/api/polymarket/backtest/*` | PM-specific backtests + FLOX |
| `/api/weather/*` | Weather desk health/paper/falsification |
| `/api/pm-kl-stat-arb/*` | Cross-venue stat arb |
| `/api/risk/state` | Risk ops panel |
| `/api/conviction/breakdown` | Channel breakdown |
| `/api/conviction/debate-cards` | Debate card feed |
| `/api/forex/status` | Forex desk |
| `/api/cemini-ai/health` | Proxy to egress-fi gateway |
| `POST /api/cemini-ai/chat` | Proxy chat to egress-fi |

**Other FastAPI surfaces**:

| Service | Port role | Endpoints |
|---------|-----------|-----------|
| `risk_governor` | 8004 | `/health`, `/evaluate`, `/kill`, `/pnl`, `/close` |
| Cemini AI gateway | egress-fi :8088 | `/health`, `/chat` (laptop `ui/serve.py` proxies) |

### Data flow patterns

1. **Redis intel bus** — producers (ingestors, brain, executors) publish `intel:*`; UI routes read via `readers.read_intel()`. TTL + `source` in envelope.
2. **Postgres subprocess** — `ui_data_providers._pg_query()` docker-execs `psql` for shadow trades / paper logs (read-only).
3. **MCP tool reuse** — some routes wrap existing `@mcp.tool` handlers (DRY between agent and UI).
4. **Async offload** — heavy routes use `asyncio.to_thread()` to avoid blocking Starlette.

### Wiring a new design page

1. Add HTML under prod `design/` (or laptop mirror for dev).
2. Implement provider in `cemini_mcp/*_ui_data.py` or extend `ui_data_providers.py`.
3. Register `@mcp.custom_route("/api/...", methods=["GET"])` in `ui_routes.py` or `server.py`.
4. Return `envelope()` with honest `status` — never fake `live` from mock constants.
5. Document Redis key or SQL source in provider docstring.
6. Frontend: poll interval ≥ `ttl_seconds`; show `source` in footer for debug.

### Real-time (future / partial)

Current design pages are **poll-based REST**. For sub-second strips:

- Snapshot on load via REST (`/api/watchlist`, `/api/ticks`)
- Deltas via WebSocket + Redis pub/sub (stack already has Redis; pattern in FastAPI+Redis WS blueprints)
- Do not add synchronous logging or blocking DB in WS handlers

### Laptop dev (`ui/README.md`)

- `ui/serve.py` — local proxy **only for Cemini AI** (port 8288 → egress-fi :8088)
- Trading design pages expect to hit prod MCP `/api/*` through nginx/tunnel — not the laptop proxy

## Snippets

> "Data providers for design/ UI HTTP routes (read-only, no trading)." [Source: cemini-prod `cemini_mcp/ui_data_providers.py` module docstring]

> "Register design/ UI HTTP routes on the Cemini MCP server." [Source: cemini-prod `cemini_mcp/ui_routes.py` module docstring]

## Dead Ends

- **Modifying gateway CORS for every new page** — envelope + nginx path preferred; AI proxy is special case.
- **Direct browser → Postgres** — all reads go through MCP server boundary.
