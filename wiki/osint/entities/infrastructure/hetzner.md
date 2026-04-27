---
title: Hetzner
type: entity
tags: [infrastructure, vps, hosting, cemini-deployment]
keywords: []
related:
  - sources/3-10-cryptographic-research.md
  - sources/3-17-git-research-pt2.md
  - sources/3-9-pm-research.md
  - sources/forex-research-3-18.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/deepseek-api.md
  - sources/crypto-3-4-11.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26

# K5 update (2026-04-26): container count corrected 18-26 → 40 per server probe; Swarm-inactive call-out added; full container manifest enumerated.
---

## Relations

- @sources/3-10-cryptographic-research.md
- @sources/3-17-git-research-pt2.md
- @sources/3-9-pm-research.md
- @sources/forex-research-3-18.md
- @concepts/ip-sale-readiness.md
- @entities/infrastructure/deepseek-api.md — host that holds the API client + key

## Raw Concept

Synthesized from 4 source(s) referencing this entity across the Cemini research corpus. Category: infrastructure.

## Narrative

Hetzner is a German VPS provider hosting the Cemini production stack.
The current deployment is a single CPU-only dedicated server: AMD EPYC,
128GB RAM, **40 Docker containers** via docker-compose (server probe
2026-04-26 K5; up from "18–26" earlier in the corpus and from
"approximately 18" in the v11.0 self-assessment per
@sources/3-9-pm-research.md para 2). Not Kubernetes, not Swarm
(`docker info | grep Swarm` returns `Swarm: inactive` — single-node;
the source's "active migration pathway toward Docker Swarm" framing is
either aspirational or has been deferred). Cost efficiency over
horizontal scale.

Documented architectural facts across the corpus (server-verified
2026-04-26):

- **CPU-only constraint** — quant strategies rely on Polars/NumPy/CPU-native ML, not GPU acceleration. `[RETRACTED 2026-04-24]` Earlier phrasing here implied a local LLM (DeepSeek-R1-14B on Ollama) runs on the host; that is not deployed. See @entities/infrastructure/deepseek-r1-14b.md and @entities/infrastructure/ollama.md for the retraction notes.
- Server reference: `root@<see .local/server.md>`, path `/opt/cemini`.
- **Deployed container set** (40 total): infra (`postgres`, `redis`, `pgadmin`, `portainer`, `cloudflare_tunnel`, `db_maintenance`); observability stack (`grafana_viz`, `prometheus`, `alertmanager`, `loki`, `tempo`, `alloy`, `cadvisor`, `node_exporter`, `postgres_exporter`, `redis_exporter`); ingest layer (`alpaca_ingestor`, `cemini_coinbase_ingestor`, `polygon_ingestor`, `oanda_streamer`, `kalshi_autopilot`, `gdelt_harvester`, `edgar_pipeline`, `finnhub_calendar`, `fred_monitor`, `macro_scraper`, `open_meteo_harvester`, `ccxt_normalizer`); intelligence + execution (`brain`, `cemini_mcp`, `cemini_os`, `cemini_proxy`, `coach_analyzer`, `ems_executor`, `opportunity_screener`, `playbook_runner`, `pnl_attribution`, `risk_governor`, `rover_scanner`, `deephaven`).
- IP-sale story: the whole stack reproduces from one docker-compose up
  on commodity CPU hardware — no vendor lock-in, no hyperscaler SLAs,
  no GPU-hour bills to untangle for the acquirer.

## Snippets

*(populate as source stubs are deep-read.)*
