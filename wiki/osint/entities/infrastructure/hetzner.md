---
title: Hetzner
type: entity
tags: [infrastructure, vps, hosting, cemini-deployment]
keywords: []
related:
  - sources/3-10-algorithmic-trading-ip-sale-audit.md
  - sources/3-10-cryptographic-research.md
  - sources/3-17-git-research-pt2.md
  - sources/3-9-pm-research.md
  - sources/forex-research-3-18.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/deepseek-api.md
  - sources/crypto-3-4-11.md
  - sources/4-5-links.md
  - entities/infrastructure/localai.md
  - concepts/librarian-server-architecture.md
  - sources/sherry-ternary-quantization-tencent-2026.md
  - sources/alash3al-stash.md
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
  - sources/3-26-b.md
  - sources/scaling-roadmap-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-30

# K5 update (2026-04-26): container count corrected 18-26 → 40 per server probe; Swarm-inactive call-out added; full container manifest enumerated.
# K6 update (2026-04-27): bidir backlink added for sources/3-10-algorithmic-trading-ip-sale-audit.md (audit's deployed-state inventory referenced "18 Docker containers" — reconciled with K5 40-container probe in K6 prescribed-vs-deployed gap table).
# K11 server-state body-of-truth refresh (2026-04-30): RAM corrected 128 GB → 7 GB (~18× overstatement resolved); containers 40→41; disk/cpu/kernel added; FastMCP 3.1.0 + tool-count restructure documented; container manifest refreshed.
---

## Relations

- @sources/3-10-algorithmic-trading-ip-sale-audit.md — K6 2026-04-27 — audit's prescribed-vs-deployed gap table cited "18 Docker containers" as the deployed-state baseline; reconciled in K6 with K5's 40-container server probe (consistent with the seven-week diff between source's 2026-03-10 publication and 2026-04-26 server probe)
- @sources/3-10-cryptographic-research.md
- @sources/3-17-git-research-pt2.md
- @sources/3-9-pm-research.md
- @sources/forex-research-3-18.md
- @concepts/ip-sale-readiness.md
- @entities/infrastructure/deepseek-api.md — host that holds the API client + key
- @sources/4-5-links.md — K8 deep-read 2026-04-28 — the doc's "128GB RAM CPU-only Hetzner VPS" claim is **~18× over** actual server state per `free -g` 2026-04-28 (7 GB total RAM). Strongest stale-snapshot finding to date in the K-series; documented in the K8 source page's server-state calibration table. The lineage of the "128 GB" figure is the 2026-04-23 hetzner.md frontmatter NEEDS-VERIFICATION baseline, not first-hand server measurement
- @entities/infrastructure/localai.md — K8 promotion 2026-04-28 — local-inference runtime targeting this host. Deployment is hardware-gated (matches the @entities/infrastructure/ollama.md / @entities/infrastructure/deepseek-r1-14b.md retraction lineage); the 7 GB constraint amplifies LocalAI's CPU-optimized + GGUF-quantized story rather than weakening it

## Raw Concept

Synthesized from 4 source(s) referencing this entity across the Cemini research corpus. Category: infrastructure.

## Narrative

Hetzner is a German VPS provider hosting the Cemini production stack.
The current deployment is a single CPU-only VPS: **AMD EPYC-Milan**,
**2 vCPUs** (1 core × 2 threads), **7 GB RAM** (7,743 MB total, ~1.5 GB
available — [RESOLVED 2026-04-30 K11] corrected from the "128 GB" figure
that propagated through early wiki pages via inheritance from the
2026-04-23 frontmatter baseline, not first-hand measurement), **75 GB
NVMe** (62 GB used, 86%), Linux 5.15.0-176-generic, uptime 2 days as of
2026-04-30 probe. **41 Docker containers** via docker-compose (server
probe 2026-04-30 K11; up from 40 per K5 2026-04-26; up from "18–26"
earlier in the corpus). Not Kubernetes, not Swarm (`docker info | grep
Swarm` returns `Swarm: inactive` — single-node; the source's "active
migration pathway toward Docker Swarm" framing is either aspirational
or has been deferred). Cost efficiency over horizontal scale.

Documented architectural facts across the corpus (server-verified
2026-04-30 K11):

- **CPU-only constraint** — quant strategies rely on Polars/NumPy/CPU-native ML, not GPU acceleration. `[RETRACTED 2026-04-24]` Earlier phrasing here implied a local LLM (DeepSeek-R1-14B on Ollama) runs on the host; that is not deployed. See @entities/infrastructure/deepseek-r1-14b.md and @entities/infrastructure/ollama.md for the retraction notes.
- Server reference: `root@<see .local/server.md>`, path `/opt/cemini`.
- **Deployed container set** (41 total, server probe 2026-04-30): infra (`postgres` timescale/timescaledb:latest-pg16, `redis` redis:7-alpine, `pgadmin`, `portainer`, `cloudflare_tunnel`, `db_maintenance`, `cemini_proxy` nginx:alpine); observability stack (`grafana_viz`, `prometheus`, `alertmanager`, `loki`, `tempo`, `alloy`, `cadvisor`, `node_exporter`, `postgres_exporter`, `redis_exporter`); ingest layer (`alpaca_ingestor`, `cemini_coinbase_ingestor`, `polygon_ingestor`, `oanda_streamer`, `kalshi_autopilot`, `gdelt_harvester`, `edgar_pipeline`, `finnhub_calendar`, `fred_monitor`, `macro_scraper`, `open_meteo_harvester`, `ccxt_normalizer`); intelligence + execution (`brain`, `cemini_mcp`, `cemini_os`, `coach_analyzer`, `ems_executor`, `opportunity_screener`, `playbook_runner`, `pnl_attribution`, `risk_governor`, `rover_scanner`); prediction-market agents (`polymarket-trading-mcp`, `polymarket-predictions-mcp` — new since K8 2026-04-28). **Gone since K5**: `deephaven` (no longer in container manifest).
- IP-sale story: the whole stack reproduces from one docker-compose up
  on commodity CPU hardware — no vendor lock-in, no hyperscaler SLAs,
  no GPU-hour bills to untangle for the acquirer.

## Snippets

*(populate as source stubs are deep-read.)*
