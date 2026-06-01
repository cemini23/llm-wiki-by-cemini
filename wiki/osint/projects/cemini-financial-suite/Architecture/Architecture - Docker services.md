---
title: Architecture - Docker services (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
module: Docker services
path: docker/
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
  - projects/cemini-financial-suite/Architecture/Architecture - prod-snapshot-2026-06-01.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md
- @projects/cemini-financial-suite/Architecture/Architecture - prod-snapshot-2026-06-01.md

## For future Claude

Prod `Docker services` @ 8faf94e.

# Docker services — Compose catalog

Entry: `docker-compose.yml` includes sub-files under `docker/`. Networks: `edge_net`, `app_net`, `data_net`. This table is **declared** topology (not a live `docker compose ps` snapshot).

## compose.infra.yml

| Service | Role |
|---------|------|
| `postgres` | TimescaleDB (`qdb`) |
| `redis` | Password-protected pub/sub + `intel:*` |
| `pgadmin` | DB admin UI |
| `dbmate` | Migrations |
| `db_maintenance` | Maintenance jobs |
| `pnl_attribution` | PnL attribution worker |
| `redis-exporter`, `postgres-exporter` | Metrics |

## compose.ingestion.yml

| Service | Role |
|---------|------|
| `polygon_feed`, `alpaca_feed` | Equity/crypto OHLCV |
| `macro_scraper`, `gdelt_harvester`, `fred_monitor` | Macro / geo |
| `edgar_pipeline`, `open_meteo_harvester` | Filings / weather inputs |
| `oanda_streamer`, `finnhub_calendar`, `ccxt_normalizer`, `coinbase_ingestor` | FX / crypto normalize |

## compose.intelligence.yml

| Service | Role |
|---------|------|
| `brain` | LangGraph orchestrator (`agents/`) |
| `signal_generator` | QuantOS profile (**disabled** by default) |
| `analyzer` | Analyzer node |
| `playbook` | `trading_playbook` runner |
| `cemini_mcp` | Read-only MCP :8002 |
| `tradingview_mcp`, `autots_mcp` | Optional MCP sidecars (profiles) |
| `llm_analyst` | PM / analyst workloads |
| `picobot`, `telegram_dispatcher` | Bots / alerts |
| `stocktwits_harvester`, `x_sentiment_harvester`, `news_sentiment_harvester`, `social_score_aggregator` | Sentiment pipeline |

## compose.execution.yml

| Service | Role |
|---------|------|
| `ems` | `ems_executor` — `trade_signals` consumer |
| `kalshi_autopilot` | Kalshi scan loop |
| `rover_scanner` | Kalshi discovery / logit |
| `risk_governor` | Pre-trade HTTP gate |
| `opportunity_screener` | Screener |

## compose.polymarket.yml (+ phase overrides)

| Service | Role |
|---------|------|
| `polymarket-predictions-mcp`, `polymarket-trading-mcp` | PM MCP adapters |
| `lp-rewards-bot`, `lp-flox-ws`, `inventory-flattener` | LP / inventory |
| `fill-reconciler`, `reconcile-positions` | Fill reconciliation |

## compose.hyperliquid.yml / compose.crypto.yml / compose.forex.yml / compose.arb.yml

| File | Service |
|------|---------|
| hyperliquid | `hyperliquid-shadow-logger` |
| crypto | `crypto-spot-shadow-logger` |
| forex | `forex-shadow-logger` |
| arb | `prediction-arb-detector` |

## compose.ui.yml

| Service | Role |
|---------|------|
| `cemini_os` | Streamlit UI :8501 |
| `grafana`, `nginx`, `cloudflared` | Metrics + perimeter |
| `deephaven` | Analytics UI |
| `portainer` | Container UI |

## compose.observability.yml

`prometheus`, `alertmanager`, `loki`, `alloy`, `tempo`, `node-exporter`, `cadvisor`, `blackbox_exporter`

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md — logical data-flow diagram
- @projects/cemini-financial-suite/Architecture/Architecture - deploy-systemd.md — host timers not in compose

## @user notes
