---
title: Architecture — prod snapshot 2026-06-01 (prod)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave5]
keywords: [Cemini-Financial-Suite, /opt/cemini, 8faf94e]
deploy-root: /opt/cemini
scanned-commit: 8faf94e
provenance: prod-briefs-out-architecture-2026-06-01-wave5
ai-first: true
module: prod-snapshot
path: scripts/generate_prod_snapshot.py
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Docker services.md
  - projects/cemini-financial-suite/Architecture/OPEN-GAPS.md
  - entities/infrastructure/cemini-stack.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - Index.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md
- @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md
- @entities/infrastructure/cemini-stack.md

## For future Claude

Ephemeral docker compose ps + systemd @ snapshot; regenerate via generate_prod_snapshot.py.

# Prod runtime snapshot (2026-06-01)

**Ephemeral:** Regenerate with `python3 scripts/generate_prod_snapshot.py`. Do not treat as architecture truth — compare to @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md.

## Docker compose (`docker compose ps`)

```
SERVICE                      STATE     STATUS
alloy                        running   Up 9 days (healthy)
alpaca_feed                  running   Up 3 days
blackbox_exporter            running   Up 9 days (healthy)
brain                        running   Up 26 hours
cadvisor                     running   Up 9 days (healthy)
ccxt_normalizer              running   Up 9 days
coinbase_ingestor            running   Up 9 days
llm_analyst                  running   Up 3 days
cemini_mcp                   running   Up 2 days (healthy)
nginx                        running   Up 9 days (healthy)
cloudflared                  running   Up 9 days
analyzer                     running   Up 4 days (healthy)
db_maintenance               running   Up 9 days
deephaven                    running   Up 4 days (healthy)
edgar_pipeline               running   Up 3 days
finnhub_calendar             running   Up 9 days
forex-shadow-logger          running   Up 9 days
gdelt_harvester              running   Up 3 days
grafana                      running   Up 9 days
hyperliquid-shadow-logger    running   Up 4 days
kalshi_autopilot             running   Up 26 hours
loki                         running   Up 9 days (healthy)
macro_scraper                running   Up 9 days
oanda_streamer               running   Up 9 days
opportunity_screener         running   Up 9 days (healthy)
pgadmin                      running   Up 9 days
playbook                     running   Up 5 days
pnl_attribution              running   Up 9 days
polymarket-predictions-mcp   running   Up 9 days
polymarket-trading-mcp       running   Up 2 days
fill-reconciler              running   Up 2 days
inventory-flattener          running   Up 2 days
lp-flox-ws                   running   Up 2 days
lp-rewards-bot               running   Up 2 days
reconcile-positions          running   Up 9 days
portainer                    running   Up 9 days
postgres                     running   Up 9 days (healthy)
prometheus                   running   Up 9 days (healthy)
redis                        running   Up 7 days (healthy)
redis-exporter               running   Up 9 days (healthy)
risk_governor                running   Up 9 days (healthy)
rover_scanner                running   Up 4 days
tempo                        running   Up 9 days (healthy)
tradingview_mcp              running   Up 9 days (healthy)
```

**Running:** 44 · **Declared in compose files:** 63

### Not running (declared but absent from `ps`)

- `alertmanager`
- `alloy`
- `alpaca_feed`
- `analyzer`
- `autots_mcp`
- `blackbox_exporter`
- `brain`
- `cadvisor`
- `ccxt_normalizer`
- `cemini_mcp`
- `cemini_os`
- `cloudflared`
- `coinbase_ingestor`
- `crypto-spot-shadow-logger`
- `db_maintenance`
- `dbmate`
- `deephaven`
- `edgar_pipeline`
- `ems`
- `fill-reconciler`
- `finnhub_calendar`
- `forex-shadow-logger`
- `fred_monitor`
- `gdelt_harvester`
- `grafana`
- `hyperliquid-shadow-logger`
- `inventory-flattener`
- `kalshi_autopilot`
- `llm_analyst`
- `loki`
- `lp-flox-ws`
- `lp-rewards-bot`
- `macro_scraper`
- `news_sentiment_harvester`
- `nginx`
- `node-exporter`
- `oanda_streamer`
- `open_meteo_harvester`
- `opportunity_screener`
- `pgadmin`
- `picobot`
- `playbook`
- `pnl_attribution`
- `polygon_feed`
- `polymarket-predictions-mcp`
- `polymarket-trading-mcp`
- `portainer`
- `postgres`
- `postgres-exporter`
- `prediction-arb-detector`
- `prometheus`
- `reconcile-positions`
- `redis`
- `redis-exporter`
- `risk_governor`
- `rover_scanner`
- `signal_generator`
- `social_score_aggregator`
- `stocktwits_harvester`
- `telegram_dispatcher`
- `tempo`
- `tradingview_mcp`
- `x_sentiment_harvester`

**Notable:** `ems` executor absent → no live `trade_signals` consumer unless started manually. `cemini_os` may appear under container name `cemini_os` while compose service label differs.

## systemd timers (`cemini-*`)

```
Mon 2026-06-01 17:10:02 UTC 2min 19s left Mon 2026-06-01 17:05:02 UTC 2min 40s ago  cemini-chaos-cleanup.timer            cemini-chaos-cleanup.service
Mon 2026-06-01 17:10:02 UTC 2min 19s left Mon 2026-06-01 17:05:02 UTC 2min 40s ago  cemini-health-snapshot.timer          cemini-health-snapshot.service
Mon 2026-06-01 17:11:31 UTC 3min 48s left Mon 2026-06-01 16:56:31 UTC 11min ago     cemini-pm-near-resolution.timer       cemini-pm-near-resolution.service
Mon 2026-06-01 17:17:38 UTC 9min left     Mon 2026-06-01 16:17:38 UTC 50min ago     cemini-wc-calendar-guard.timer        cemini-wc-calendar-guard.service
Mon 2026-06-01 18:00:00 UTC 52min left    Mon 2026-06-01 16:00:02 UTC 1h 7min ago   cemini-weather-nwp-stack.timer        cemini-weather-nwp-stack.service
Mon 2026-06-01 18:09:59 UTC 1h 2min left  Mon 2026-06-01 14:09:59 UTC 2h 57min ago  cemini-wc-shadow-plan.timer           cemini-wc-shadow-plan.service
Mon 2026-06-01 18:34:16 UTC 1h 26min left Mon 2026-06-01 14:34:16 UTC 2h 33min ago  cemini-pm-lp-health.timer             cemini-pm-lp-health.service
Mon 2026-06-01 19:47:40 UTC 2h 39min left Mon 2026-06-01 13:47:40 UTC 3h 20min ago  cemini-pm-kl-align.timer              cemini-pm-kl-align.service
Mon 2026-06-01 19:48:40 UTC 2h 40min left Mon 2026-06-01 13:48:40 UTC 3h 19min ago  cemini-wc-scan.timer                  cemini-wc-scan.service
Mon 2026-06-01 20:34:13 UTC 3h 26min left Mon 2026-06-01 14:34:13 UTC 2h 33min ago  cemini-pm-forecast-revision.timer     cemini-pm-forecast-revision.service
Mon 2026-06-01 20:58:32 UTC 3h 50min left Mon 2026-06-01 14:58:32 UTC 2h 9min ago   cemini-pm-weather-paper.timer         cemini-pm-weather-paper.service
Mon 2026-06-01 22:19:46 UTC 5h 12min left Mon 2026-06-01 16:19:46 UTC 47min ago     cemini-pm-btc-updown-paper.timer      cemini-pm-btc-updown-paper.service
Tue 2026-06-02 04:12:47 UTC 11h left      Mon 2026-06-01 04:04:47 UTC 13h ago       cemini-disk-cleanup.timer             cemini-disk-cleanup.service
Tue 2026-06-02 06:04:52 UTC 12h left      Mon 2026-06-01 06:09:55 UTC 10h ago       cemini-ots-upgrade.timer              cemini-ots-upgrade.service
Tue 2026-06-02 06:18:17 UTC 13h left      Mon 2026-06-01 06:16:12 UTC 10h ago       cemini-ops-daily.timer                cemini-ops-daily.service
Tue 2026-06-02 07:15:00 UTC 14h left      Mon 2026-06-01 07:15:06 UTC 9h ago        cemini-pm-weather-resolve.timer       cemini-pm-weather-resolve.service
Tue 2026-06-02 07:15:00 UTC 14h left      Mon 2026-06-01 07:15:06 UTC 9h ago        cemini-wc-pnl-daily.timer             cemini-wc-pnl-daily.service
Tue 2026-06-02 08:15:00 UTC 15h left      Mon 2026-06-01 08:15:03 UTC 8h ago        cemini-pm-weather-falsification.timer cemini-pm-weather-falsification.service
Tue 2026-06-02 08:32:05 UTC 15h left      Mon 2026-06-01 08:30:21 UTC 8h ago        cemini-pm-mcp-shadow-probe.timer      cemini-pm-mcp-shadow-probe.service
Sun 2026-06-07 03:00:00 UTC 5 days left   Sun 2026-05-31 03:00:00 UTC 1 day 14h ago cemini-weather-nwp-train.timer        cemini-weather-nwp-train.service
Sun 2026-06-07 08:00:00 UTC 5 days left   Sun 2026-05-31 08:00:00 UTC 1 day 9h ago  cemini-wc-cross-venue-reconcile.timer cemini-wc-cross-venue-reconcile.service
Sun 2026-06-07 09:30:00 UTC 5 days left   Sun 2026-05-31 09:30:00 UTC 1 day 7h ago  cemini-pm-weather-emos-promote.timer  cemini-pm-weather-emos-promote.service
Sun 2026-06-07 09:45:00 UTC 5 days left   Sun 2026-05-31 09:45:00 UTC 1 day 7h ago  cemini-pm-weather-k66-promote.timer   cemini-pm-weather-k66-promote.service
Mon 2026-06-08 08:00:00 UTC 6 days left   Mon 2026-06-01 08:00:00 UTC 9h ago        cemini-wc-discover.timer              cemini-wc-discover.service
```

## Related

- @projects/cemini-financial-suite/Architecture/Architecture - deploy-systemd.md
- @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md
