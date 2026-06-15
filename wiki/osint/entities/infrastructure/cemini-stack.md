---
title: Cemini Stack — Prod + Egress Trading Topology
type: entity
tags: [infrastructure, cemini-deployment, hetzner, prod, egress-fi]
keywords: [CPX31, Hetzner Cloud, Docker Compose, prod, egress-fi, librarian-decommissioned]
related:
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/redis.md
  - entities/infrastructure/timescaledb.md
  - entities/infrastructure/pgvector.md
  - entities/infrastructure/deepseek-api.md
  - concepts/librarian-server-architecture.md
  - meta/librarian-decommission-2026-06-14.md
  - concepts/cemini-deployment.md
  - concepts/cemini-license-posture.md
  - entities/tools/pybroker.md
  - entities/infrastructure/cemini-egress-fi.md
  - concepts/pnl-attribution-versioning.md
  - concepts/trading-dashboard-api-wiring.md
  - concepts/trading-bot-logging-discipline.md
  - concepts/equity-fair-value-evaluation.md
  - concepts/cemini-repository-topology.md
  - concepts/cemini-knowledge-application-architecture.md
  - projects/osint-workspace/Architecture/Architecture - ui.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/OPEN-GAPS.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - prod-snapshot-2026-06-01.md
maturity: core
created: 2026-05-03
updated: 2026-06-14
# Server-state probe baseline (2026-05-03): both hosts probed live; specs recorded match `free -h` / `df -h` / `nproc` output. Refresh on every spec change. K89 probe 2026-05-31: 44 containers, disk ~40%, swap ~78%.
---

## Relations

- @entities/infrastructure/hetzner.md — host provider for both servers
- @entities/infrastructure/redis.md — pub/sub layer in the production data plane
- @entities/infrastructure/timescaledb.md — primary persistence in production
- @entities/infrastructure/pgvector.md — vector-similarity layer co-tenant with TimescaleDB on production; also used by stash on librarian
- @entities/infrastructure/deepseek-api.md — LLM brain (hosted, not self-served)
- @meta/librarian-decommission-2026-06-14.md — **authoritative** fleet posture as of 2026-06-14
- @concepts/librarian-server-architecture.md — historical two-server RAG design (librarian host deleted)
- @concepts/cemini-deployment.md — installation procedure layered on top of this topology
- @concepts/cemini-license-posture.md — license obligations attached to deployed components
- @entities/infrastructure/cemini-egress-fi.md — the third Hetzner server (Helsinki, order-routing relay); this page's two-server framing predates it. Originally provisioned at Falkenstein 2026-05-19 as `cemini-poly-proxy`; rebuilt at Helsinki 2026-05-20 for joint Polymarket + Hyperliquid coverage
- @concepts/pnl-attribution-versioning.md — `pnl_attribution` container + versioned trade PnL (prod audit 2026-05-28)
- @concepts/trading-dashboard-api-wiring.md — `cemini_mcp` `/api/*` routes for design/ UI
- @concepts/trading-bot-logging-discipline.md — Grafana/Loki observability layer on this stack
- @concepts/equity-fair-value-evaluation.md — `core/equity_valuation.py` on prod brain path
- @concepts/cemini-repository-topology.md — deploy monorepo (`Cemini-Financial-Suite`) vs wiki federation
- @concepts/cemini-knowledge-application-architecture.md — K89 prod audit; swap/disk probe refresh 2026-05-31
- @projects/osint-workspace/Architecture/Architecture - ui.md — laptop `ui/` dev chat proxy tunnels to `cemini-egress-fi` gateway
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md — compose services on prod @ e3674e4
- @projects/cemini-financial-suite/Cemini Financial Suite.md — deploy monorepo hub
- @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md — runtime-matrix gap (compose profiles actually up)
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md — prod compose map @ 8faf94e
- @projects/cemini-financial-suite/Architecture/Architecture - prod-snapshot-2026-06-01.md — live compose ps 2026-06-01

## Raw Concept

What Cemini physically *is* on the wire: which servers, which sizes, which OS, which containers, and how the two halves talk. This page is the umbrella for the production deployment — sibling pages cover individual components ([hetzner.md](../infrastructure/hetzner.md) for the host provider, individual data-plane component pages for redis/postgres/etc.). The deployment *procedure* (how to set this up from scratch) lives at @concepts/cemini-deployment.md.

Created 2026-05-03 in response to the user's request for a setup-and-recommendations document covering server class, RAM/disk requirements, OS choice, and US-vs-EU regional considerations.

## Narrative

### Fleet topology — prod + egress (2026-06-14)

`[DECOMMISSIONED 2026-06-14]` The librarian host (`cemini-librarian`) was **deleted**. Live Hetzner fleet:

| Role | Host alias | Status | Notes |
| --- | --- | --- | --- |
| Production (trading) | `cemini-prod` | **ON** | CPX31, Ashburn; ~44 containers (K89 baseline) |
| Order egress (HL + PM) | `cemini-egress-fi` | **ON** | Helsinki; SSH tunnel from prod |
| Knowledge / RAG | `cemini-librarian` | **DELETED** | Was CPX21 kb-server + stash + Arctic |

Wiki and raw-source canon: **laptop git** only. See @meta/librarian-decommission-2026-06-14.md.

### Historical — two-server prod + librarian (pre-2026-06-14)

Cemini previously ran **two Ashburn servers** joined by private network `10.0.0.2`:

| Role | Host alias | Hetzner SKU | vCPU | RAM | Disk | OS | Probed 2026-05-03 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Production (trading + intelligence) | `cemini-prod` | CPX31 | 2 | 8 GB allocated (7.6 GB measured) | 80 GB local + 25 GB volume | Ubuntu 22.04.5 LTS | **44** containers (K89 probe 2026-05-31); disk **~40%** used; **swap ~78%** ⚠ |
| Librarian (RAG + episodic memory) | `cemini-librarian` | CPX21 | 3 | 4 GB allocated (3.7 GB measured) | 80 GB local | Ubuntu 24.04.4 LTS | **deleted 2026-06-14** |

Connection details (SSH targets, IPs) live in `.local/server.md` — gitignored, never committed.

### Why librarian existed (historical)

The two-server split is intentional and provides four operational properties that a single combined host would not:

1. **Different blast radius** — a runaway brain process or memory leak on production cannot OOM-kill the librarian's MCP endpoint, and vice versa. Trading uptime is decoupled from RAG-cache uptime.
2. **Different RAM/CPU profiles** — production needs RAM headroom for 41 containers + Postgres working set + Redis streams; librarian needs CPU for embedding generation (Ollama nomic-embed-text + stash 8-stage pipeline) but lighter RAM. The CPX31/CPX21 split matches the workload.
3. **Different update cadence** — librarian can run rolling kb-server / stash updates without touching trading. Production locks down during market hours.
4. **Future-proofing for episodic memory** — stash deployment on librarian (2026-05-02 per @sources/alash3al-stash.md) gives Cemini a two-layer memory architecture (kb-server for static wiki RAG + stash for dynamic episodic memory) without consuming production RAM.

A single-server alternative is technically feasible at higher RAM (16 GB+) but loses all four properties. Not recommended.

### Production server (cemini-prod) — what runs

41 Docker containers via `docker-compose` (server probe 2026-04-30, last K11 refresh; **44 running** per K89 audit 2026-05-31; deployment manifest at `/opt/cemini/docker-compose.yml`). Container groupings:

- **Infrastructure (7)**: `postgres` (timescale/timescaledb:latest-pg16), `redis` (redis:7-alpine), `pgadmin`, `portainer`, `cloudflare_tunnel`, `db_maintenance`, `cemini_proxy` (nginx:alpine).
- **Observability (10)**: `grafana_viz`, `prometheus`, `alertmanager`, `loki`, `tempo`, `alloy`, `cadvisor`, `node_exporter`, `postgres_exporter`, `redis_exporter`.
- **Ingest layer (12)**: `alpaca_ingestor`, `cemini_coinbase_ingestor`, `polygon_ingestor`, `oanda_streamer`, `kalshi_autopilot`, `gdelt_harvester`, `edgar_pipeline`, `finnhub_calendar`, `fred_monitor`, `macro_scraper`, `open_meteo_harvester`, `ccxt_normalizer`.
- **Intelligence + execution (10)**: `brain`, `cemini_mcp`, `cemini_os`, `coach_analyzer`, `ems_executor`, `opportunity_screener`, `playbook_runner`, `pnl_attribution`, `risk_governor`, `rover_scanner`.
- **Prediction-market agents (2)**: `polymarket-trading-mcp`, `polymarket-predictions-mcp`.

Not Kubernetes, not Swarm (`docker info | grep Swarm` → `inactive`). Single-node `docker compose up -d` orchestration. Deliberate cost-efficiency choice over horizontal scale (see @sources/3-10-algorithmic-trading-ip-sale-audit.md for IP-sale rationale).

### Librarian server (cemini-librarian) — what runs

- **kb-server** (Option C serving layer) — patched to honor `KB_TOOL_ALLOWLIST` env; exposes 7 read-only MCP tools (`kb_search`, `kb_search_smart`, `kb_context`, `kb_read`, `kb_list`, `kb_vault_status`, `kb_safety_check`). Write tools blocked at MCP boundary. See `.local/server.md` for patch lineage.
- **stash** (alash3al/stash, Apache-2.0) — Go binary, 8-stage memory consolidation pipeline, Postgres + pgvector backend, MCP SSE :8080 / HTTP :9090 (binds to all interfaces). Deployed 2026-05-02 per @sources/alash3al-stash.md. **MCP wired into all three Claude Code contexts 2026-05-04**: laptop via SSH tunnel `localhost:8088 → librarian:8080` (Hetzner-firewalled at the public edge); `ssh cemini-librarian` direct to `localhost:8080`; `ssh cemini-prod` direct to `10.0.0.2:8080` over the Hetzner private network. Brave-search MCP wired the same day across all three contexts. See @concepts/cemini-deployment.md §9a for the wiring matrix.
- **Ollama** — systemd-managed on :11434 (localhost-only); deployed 2026-04-28 per probe 2026-05-04. Two models loaded: `nomic-embed-text:latest` (137M params F16, ~274 MB on disk) for embeddings + `qwen2.5:0.5b` (494M params Q4_K_M, ~397 MB on disk) for small-reasoning tasks. Used by stash's 8-stage memory consolidation pipeline; available to kb-server for vector search.
- **rsync target** — receives hourly `wiki/` syncs from the laptop via `scripts/sync_wiki_to_librarian.sh` (macOS crontab `0 * * * *`).
- **Canonical raw-source store** — `/opt/cemini-bulk/research/` (~283 PDFs/docx, 642 MB) and `/opt/cemini-bulk/market-dataset/` (~17.6k files, 1.6 GB). Migrated from laptop 2026-04-28.

### Inter-server data flow

```
Laptop (curator)
  ↓ rsync (hourly cron)
Librarian /opt/cemini-wiki/wiki/   ←── kb-server MCP queries from production brain
Librarian /opt/cemini-bulk/         ←── scp on raw-source ingest
                                       ↑
                                       │ (private network)
                                       ↓
Production /opt/cemini/  → DeepSeek API (cloud) → trading decisions
                        → polymarket / kalshi / alpaca / etc. (external)
```

The brain on production queries the librarian over the private Hetzner network for static wiki context (kb-server) and dynamic episodic memory (stash). The brain *itself* runs against the DeepSeek hosted API — no LLM weights are local on either server (see @entities/infrastructure/deepseek-api.md, and the @entities/infrastructure/deepseek-r1-14b.md / @entities/infrastructure/ollama.md retraction notes).

### Known operational findings (2026-05-03 probe; K89 refresh 2026-05-31)

- **Production disk pressure** — K89 probe: **~40%** used of 75 GB (improved vs 90% May 2026 earlier probe). Confirm volume mount for Postgres if not already migrated.
- **Production swap usage** — K89: **~4.7G / 6G swap (~78%)** during off-hours probe → memory pressure persists. Symptomatic of 44 containers on 8 GB RAM; track alongside @concepts/cemini-knowledge-application-architecture.md G07.
- **OS version drift** — production on Ubuntu 22.04.5, librarian on 24.04.4. Not blocking; recommend aligning on 24.04.x at next production rebuild.

### Region & regulatory considerations

Both hosts are currently in **Ashburn, VA (US)** per `.local/server.md` (librarian) [NEEDS VERIFICATION 2026-05-03 — production region not re-probed]. Regional choice is not arbitrary — it interacts with Polymarket/Kalshi geo-blocking. See @concepts/cemini-deployment.md "Regional choice" section for the operator-residency vs server-region decision matrix.

## Snippets

*(populate from operational probes as they accumulate.)*

## Dead Ends

*(none recorded yet for this page.)*
