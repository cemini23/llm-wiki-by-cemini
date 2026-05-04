---
title: Cemini Stack — Two-Server Production Topology
type: entity
tags: [infrastructure, cemini-deployment, hetzner, two-server]
keywords: [CPX21, CPX31, Hetzner Cloud, Ubuntu 22.04, Ubuntu 24.04, Docker Compose, kb-server, librarian, production]
related:
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/redis.md
  - entities/infrastructure/timescaledb.md
  - entities/infrastructure/pgvector.md
  - entities/infrastructure/deepseek-api.md
  - concepts/librarian-server-architecture.md
  - concepts/cemini-deployment.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-03
updated: 2026-05-03

# Server-state probe baseline (2026-05-03): both hosts probed live; specs recorded match `free -h` / `df -h` / `nproc` output. Refresh on every spec change.
---

## Relations

- @entities/infrastructure/hetzner.md — host provider for both servers
- @entities/infrastructure/redis.md — pub/sub layer in the production data plane
- @entities/infrastructure/timescaledb.md — primary persistence in production
- @entities/infrastructure/pgvector.md — vector-similarity layer co-tenant with TimescaleDB on production; also used by stash on librarian
- @entities/infrastructure/deepseek-api.md — LLM brain (hosted, not self-served)
- @concepts/librarian-server-architecture.md — librarian-side architectural rationale (Option C kb-server pattern)
- @concepts/cemini-deployment.md — installation procedure layered on top of this topology
- @concepts/cemini-license-posture.md — license obligations attached to deployed components

## Raw Concept

What Cemini physically *is* on the wire: which servers, which sizes, which OS, which containers, and how the two halves talk. This page is the umbrella for the production deployment — sibling pages cover individual components ([hetzner.md](../infrastructure/hetzner.md) for the host provider, individual data-plane component pages for redis/postgres/etc.). The deployment *procedure* (how to set this up from scratch) lives at @concepts/cemini-deployment.md.

Created 2026-05-03 in response to the user's request for a setup-and-recommendations document covering server class, RAM/disk requirements, OS choice, and US-vs-EU regional considerations.

## Narrative

### Two-server topology — recommended

Cemini production runs on **two Hetzner Cloud VPS instances** in the same region, joined by a private network:

| Role | Host alias | Hetzner SKU | vCPU | RAM | Disk | OS | Probed 2026-05-03 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Production (trading + intelligence) | `cemini-prod` | CPX31 | 2 | 8 GB allocated (7.6 GB measured) | 80 GB local + 25 GB volume | Ubuntu 22.04.5 LTS | 41 containers, Docker 29.2.1 + Compose v5.0.2; **disk 90% used** ⚠ |
| Librarian (RAG + episodic memory) | `cemini-librarian` | CPX21 | 3 | 4 GB allocated (3.7 GB measured) | 80 GB local | Ubuntu 24.04.4 LTS | kb-server + stash + Node 20+; disk 20% used |

Connection details (SSH targets, IPs) live in `.local/server.md` — gitignored, never committed.

### Why two servers (separation of concerns)

The two-server split is intentional and provides four operational properties that a single combined host would not:

1. **Different blast radius** — a runaway brain process or memory leak on production cannot OOM-kill the librarian's MCP endpoint, and vice versa. Trading uptime is decoupled from RAG-cache uptime.
2. **Different RAM/CPU profiles** — production needs RAM headroom for 41 containers + Postgres working set + Redis streams; librarian needs CPU for embedding generation (Ollama nomic-embed-text + stash 8-stage pipeline) but lighter RAM. The CPX31/CPX21 split matches the workload.
3. **Different update cadence** — librarian can run rolling kb-server / stash updates without touching trading. Production locks down during market hours.
4. **Future-proofing for episodic memory** — stash deployment on librarian (2026-05-02 per @sources/alash3al-stash.md) gives Cemini a two-layer memory architecture (kb-server for static wiki RAG + stash for dynamic episodic memory) without consuming production RAM.

A single-server alternative is technically feasible at higher RAM (16 GB+) but loses all four properties. Not recommended.

### Production server (cemini-prod) — what runs

41 Docker containers via `docker-compose` (server probe 2026-04-30, last K11 refresh; deployment manifest at `/opt/cemini/docker-compose.yml`). Container groupings:

- **Infrastructure (7)**: `postgres` (timescale/timescaledb:latest-pg16), `redis` (redis:7-alpine), `pgadmin`, `portainer`, `cloudflare_tunnel`, `db_maintenance`, `cemini_proxy` (nginx:alpine).
- **Observability (10)**: `grafana_viz`, `prometheus`, `alertmanager`, `loki`, `tempo`, `alloy`, `cadvisor`, `node_exporter`, `postgres_exporter`, `redis_exporter`.
- **Ingest layer (12)**: `alpaca_ingestor`, `cemini_coinbase_ingestor`, `polygon_ingestor`, `oanda_streamer`, `kalshi_autopilot`, `gdelt_harvester`, `edgar_pipeline`, `finnhub_calendar`, `fred_monitor`, `macro_scraper`, `open_meteo_harvester`, `ccxt_normalizer`.
- **Intelligence + execution (10)**: `brain`, `cemini_mcp`, `cemini_os`, `coach_analyzer`, `ems_executor`, `opportunity_screener`, `playbook_runner`, `pnl_attribution`, `risk_governor`, `rover_scanner`.
- **Prediction-market agents (2)**: `polymarket-trading-mcp`, `polymarket-predictions-mcp`.

Not Kubernetes, not Swarm (`docker info | grep Swarm` → `inactive`). Single-node `docker compose up -d` orchestration. Deliberate cost-efficiency choice over horizontal scale (see @sources/3-10-algorithmic-trading-ip-sale-audit.md for IP-sale rationale).

### Librarian server (cemini-librarian) — what runs

- **kb-server** (Option C serving layer) — patched to honor `KB_TOOL_ALLOWLIST` env; exposes 7 read-only MCP tools (`kb_search`, `kb_search_smart`, `kb_context`, `kb_read`, `kb_list`, `kb_vault_status`, `kb_safety_check`). Write tools blocked at MCP boundary. See `.local/server.md` for patch lineage.
- **stash** (alash3al/stash, Apache-2.0) — Go binary, 8-stage memory consolidation pipeline, Postgres + pgvector backend, MCP SSE :8080 / HTTP :9090. Deployed 2026-05-02 per @sources/alash3al-stash.md. Laptop MCP wiring landed 2026-05-04 via SSH local-port-forward (`ssh -f -N -L 8088:localhost:8080 cemini-librarian`) + `~/.claude.json` `mcpServers.stash` SSE entry; ports 8080/9090 are Hetzner-firewalled, so the tunnel is the only valid public-side path. See @concepts/cemini-deployment.md §9 for the worked example.
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

### Known operational findings (2026-05-03 probe)

- **Production disk pressure** — 64 GB used of 75 GB (90%). 25 GB attached volume present but its mount point and current utilization are not reflected in this probe. Action item: confirm volume usage and consider migrating Postgres data directory if not already on the volume.
- **Production swap usage** — 3 GB of 6 GB swap in active use during probe → memory pressure. Symptomatic of running 41 containers on 8 GB RAM; mitigated by current container resource limits but worth tracking.
- **OS version drift** — production on Ubuntu 22.04.5, librarian on 24.04.4. Not blocking; recommend aligning on 24.04.x at next production rebuild.

### Region & regulatory considerations

Both hosts are currently in **Ashburn, VA (US)** per `.local/server.md` (librarian) [NEEDS VERIFICATION 2026-05-03 — production region not re-probed]. Regional choice is not arbitrary — it interacts with Polymarket/Kalshi geo-blocking. See @concepts/cemini-deployment.md "Regional choice" section for the operator-residency vs server-region decision matrix.

## Snippets

*(populate from operational probes as they accumulate.)*

## Dead Ends

*(none recorded yet for this page.)*
