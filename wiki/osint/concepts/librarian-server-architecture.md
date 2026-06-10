---
title: Librarian Server Architecture (dedicated-host pattern for 24/7 wiki-as-library availability to the deployed Cemini brain)
type: concept
tags: [concept, architecture, infrastructure, librarian-tooling, hosting-topology, 24-7-reliability, cemini-brain, mcp-server, planned-not-built]
keywords: [librarian-server, hetzner-cx32, dedicated-host, three-server-topology, sync-model, mcp-bridge, 24-7-availability, crypto-market-reliability, librarian-doctrine]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/scatter-gather-topology.md
  - concepts/context-compression-resume-pattern.md
  - sources/arxiv-less-context-better-agents-2606.10209-2026-06-10.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/deepseek-api.md
  - entities/infrastructure/localai.md
  - entities/infrastructure/ollama.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - sources/llm-wiki.md
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/playwright-mcp-microsoft.md
  - concepts/ai-organisation-design.md
  - concepts/mcp-tool-marketplace.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - sources/agriciDaniel-claude-obsidian.md
  - sources/bytemover-agent-native-memory.md
  - sources/alash3al-stash.md
  - entities/infrastructure/cemini-stack.md
  - concepts/cemini-deployment.md
  - entities/tools/obsidian-llm-wiki-local.md
  - entities/tools/pageindex.md
  - entities/tools/sift-kg.md
  - entities/tools/swarmvault.md
  - entities/infrastructure/cemini-egress-fi.md
  - concepts/cemini-ai-assistant.md
  - concepts/interaction-native-knowledge-harness.md
  - sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - sources/arxiv-inference-scaling-llms-2605.19775.md
  - concepts/laptop-prod-research-split.md
  - sources/cemini-laptop-prod-research-handoff-2026-05-23.md
  - concepts/cemini-repository-topology.md
maturity: validated
hub: true
created: 2026-04-28
updated: 2026-06-10
---

## Relations

- @concepts/wiki-tooling-evaluation.md — parent decision document; this page expands the "Hosting topology" sub-decision (Option C) into a full architectural plan with migration phases
- @concepts/scatter-gather-topology.md — the LangGraph topology whose analyst nodes will query the librarian server's MCP endpoint at decision time. **This is the load-bearing use case** that drives the 24/7 availability requirement on this page
- @concepts/context-compression-resume-pattern.md — the cpr-pattern Python port (from agentmemory) lands naturally on the librarian server, not on the production trading-stack server (which is RAM-constrained per K8 server-probe)
- @concepts/ip-sale-readiness.md — multi-server topology becomes part of the IP-sale deal: acquirer gets production trading stack + librarian server + sync workflow. Reliability story improves (no laptop-as-SPOF for the brain's knowledge layer); documentation burden grows slightly (two-server runbook)
- @entities/infrastructure/hetzner.md — the production trading-stack server. Companion to (not replaced by) the new librarian server; both live in the Hetzner Cloud ecosystem on the same vendor / control panel / SSH workflow
- @entities/infrastructure/deepseek-api.md — the LLM brain client whose code (`services/llm_analyst/deepseek_client.py`) will be extended to query the librarian server's MCP endpoint when constructing analyst-node prompts
- @entities/infrastructure/localai.md — local-inference runtime that the librarian server unblocks: the new dedicated host has the RAM/CPU headroom + storage to evaluate LocalAI without touching production trading-stack
- @entities/infrastructure/ollama.md — peer alternative to LocalAI; same architectural slot. Embeddings-only deployment (`nomic-embed-text` 274 MB / ~500 MB resident) lands on the librarian server as the **first concrete deployment of any Ollama-family runtime**, ending the multi-month retracted-state on `ollama.md`
- @sources/atomicmemory-llm-wiki-compiler.md — the wiki-compiler runtime (Node ≥18, ~1 GB) that runs on the librarian server with `llmwiki serve` exposing 7 MCP tools to the brain
- @sources/agentmemory-rohitg00-cpr-impl.md — the cpr-pattern reference implementation whose pipeline shape (PostToolUse → SHA-256 dedup → privacy filter → LLM compress → BM25+Vector+Graph RRF) ports into Python on the librarian server alongside the wiki-compiler
- @sources/llm-wiki.md — Karpathy gist; the foundational pattern source. The librarian server is the **physical realization** of the gist's "the wiki is the codebase" framing — same codebase the LLM maintains, just on its own dedicated host
- @sources/bytemover-agent-native-memory.md — K13 Promotion #3; CLAUDE.md pattern source. ByteRover's Context Tree (Domain > Topic > Subtopic > Entry) is the organizational pattern behind the wiki's directory structure. The two-tier memory guardrail (filesystem for docs, DB for ticks) applies to the librarian's storage architecture.
- @sources/alash3al-stash.md — Wave 5A Adopt → deployed 2026-05-02. Episodic memory layer on librarian (v0.2.9, MCP SSE :8080, HTTP :9090). Two-layer memory architecture: kb-server (static wiki RAG) + stash (dynamic episodic memory — episodes, facts, working context, contradictions, causal links, hypotheses, goals, failure records). Postgres 16 + pgvector, Ollama-backed embeddings (nomic-embed-text) + reasoning (qwen2.5:0.5b).
- @ccc-wiki/entities/mcp-servers/librarian-kb-server.md — CCC-side entity page on the librarian's MCP-serving surface (laptop-only meta-wiki on Cemini's Claude Code workflow; carries the cross-federation routing notes)
- @ccc-wiki/concepts/cross-wiki-routing.md — CCC-side concept on where new content belongs in the federation; references this page as the serving-layer canon
- @entities/infrastructure/cemini-egress-fi.md — the third Hetzner server (Helsinki, Finland); same vendor as the librarian, different DC. Candidate Cemini AI host that would query this librarian's kb-server + stash over a transatlantic hop
- @concepts/cemini-ai-assistant.md — proposed user-facing assistant; a new consumer of this librarian's kb-server (static wiki RAG) and stash (episodic memory)
- @concepts/interaction-native-knowledge-harness.md — InKH temporal graph + wiki audit; kb-server/stash as partial implementation
- @sources/arxiv-interaction-native-knowledge-harness-2606.01886.md — financial harness paper (K99 cross-wiki from CCC)

## Raw Concept

`[DECISION 2026-04-28]` Architectural commitment to a dedicated Hetzner Cloud server hosting the workspace librarian (llm-wiki-compiler + Ollama + nomic-embed-text + canonical wiki copy) separately from both the local laptop (current canonical editor) and the production trading-stack Hetzner host. **Driver**: crypto markets run 24/7; the deployed Cemini brain (`services/llm_analyst/deepseek_client.py` analyst nodes operating against the LangGraph scatter-gather topology) must be able to query the wiki/library for context **at any time** market signals fire, with no laptop-availability dependency, no lid-closed-sleep risk, and no home-network-reliability dependency. Laptop-as-host fails this SLA; sync-to-existing-Hetzner (Option A in `wiki/concepts/wiki-tooling-evaluation.md`) is feasible but loads the already-tight 7 GB RAM production box and creates SPOF risk on shared infrastructure. **Option C — new dedicated CX-class server** is the committed path.

This page is the planning-of-record for the migration from current state (laptop-only librarian, no MCP exposure to brain) to target state (three-server topology with always-on MCP endpoint serving the brain).

## Narrative

### The decision

`[DECISION 2026-04-28]` — User-committed: **Option C from `concepts/wiki-tooling-evaluation.md` "Hosting topology" — dedicated Hetzner CX-class server hosting the librarian.**

User framing (verbatim 2026-04-28): *"it is going to be of utmost importance that the deployed cemini brain can query the library at any time as crypto markets are 24/7 and who knows when its going to need info."*

This reframes the librarian from a research/curation tool (the laptop-only model that has worked through K1–K8 + WTE) to an **operational dependency** for the deployed trading stack. The reliability bar moves accordingly: from "convenient when working" to "available whenever the market is."

#### Alternatives rejected (and why)

- **Option A: sync to existing Hetzner production server** — feasible but adds Node + nomic-embed-text + llm-wiki-compiler runtime (~700 MB RAM resident) to the already-tight 7 GB box (per K8 server-probe `free -g` 2026-04-28). Creates a single point of failure shared with the production trading stack — librarian outage = trading-stack outage and vice-versa. Production-stack memory pressure becomes a librarian-uptime risk. **Operationally too coupled.**
- **Option B: migrate wiki to existing Hetzner production server** — same RAM constraint as Option A AND breaks the librarian doctrine documented in the `retracted_deepseek_ollama.md` memory file: *"the wiki lives on this laptop precisely because the server cannot carry the full knowledge-and-LLM loop locally."* The doctrine's load-bearing rationale (server can't host the full local LLM brain stack) extends to wiki tooling. **Doctrine-incompatible.**
- **Option D: self-host (Raspberry Pi 5 / Mac mini / NUC at home)** — depends on home internet uptime, requires port forwarding or Tailscale tunnel, exposes home network surface to the brain's query traffic. Hetzner Cloud's data-center reliability beats home ISP reliability for a 24/7 SLA target. **Reliability-incompatible.**
- **Cancelled: external drive purchase + Ollama-on-laptop (Path C of `wiki/concepts/wiki-tooling-evaluation.md`)** — was the original 2026-04-28 plan; superseded by this server decision because the dedicated server provides 80 GB SSD natively (no external drive needed for librarian purposes) and removes the laptop-as-host reliability problem entirely. External drive is no longer being purchased.

### Why dedicated, why now

The crypto market 24/7 reframe surfaces a latent SLA the WTE evaluation page implicitly assumed but didn't make load-bearing:

- **Trading hours requirement** — equity markets close. Crypto markets don't. The deployed brain on the production Hetzner host runs `gdelt_harvester` / `polygon_ingestor` / `coinbase_ingestor` (per K5 / K8 container manifest enumeration on `hetzner.md`) that ingest 24/7 — and the analyst nodes that consume those ingest streams may need wiki context at any hour. Laptop-as-host means: brain attempts MCP query → laptop is closed/asleep/offline → analyst node has no wiki context → degraded decision quality OR fallback to API-only mode.
- **Network reliability** — laptop is on home wifi (residential ISP, NAT, possible IP rotation). Hetzner-to-laptop is also Hetzner-to-residential-ISP. Hetzner-to-Hetzner is intra-data-center or intra-region: low-millisecond latency, 99.9%+ SLA, no NAT.
- **Hardware reliability** — laptop drives, fans, batteries, lid-sleep states. Server hardware in a data center is more reliable per unit time, especially with Hetzner Cloud snapshot-based recovery.
- **Decoupling** — production trading-stack failures should not take out the librarian, and vice-versa. Option A (shared host) couples them; Option C (separate hosts) decouples them.

### Target topology (three-server)

```
┌──────────────────────────────────────────────────────────────────┐
│  LAPTOP (canonical editor)                                       │
│  /Users/claudiobarone/Desktop/OSINT WORKSPACE/                   │
│    wiki/                <- canonical curated source of truth     │
│    research for cemini/ <- raw sources (NOT synced)              │
│    briefs/              <- distribution staging (existing scp)   │
│    .claude/             <- Claude Code session context           │
│                                                                  │
│  Workflow: Claude Code librarian sessions (this conversation),   │
│  Obsidian editing, K-pass deep reads, lint runs, manual ingest.  │
│                                                                  │
│  Triggers sync: rsync wiki/ → librarian server (cron + manual)   │
└──────────────────────────────────┬───────────────────────────────┘
                                   │  rsync over SSH (push)
                                   │  daily cron + manual trigger
                                   ▼
┌──────────────────────────────────────────────────────────────────┐
│  LIBRARIAN SERVER (NEW — Hetzner CPX21 Ashburn, committed)       │
│  3 vCPU · 4 GB RAM · 80 GB NVMe · 2 TB traffic · $13.99/mo       │
│  /opt/librarian/                                                 │
│    wiki/                <- synced copy of laptop canonical       │
│    .llmwiki/            <- llm-wiki-compiler state + indices     │
│    .ollama/             <- nomic-embed-text                      │
│  Services (systemd):                                             │
│    - ollama serve       <- port 11434 (embeddings + reasoning)   │
│    - kb-server serve    <- port 3838 (wiki FTS5 + MCP)           │
│    - stash serve        <- port 8080 MCP / 9090 HTTP (memory)    │
│    - sshd               <- for laptop sync + admin access        │
│  Disk envelope: 80 GB NVMe                                       │
│    - ~8 GB OS + Node + Ollama + Postgres runtimes                │
│    - ~1 GB wiki copy + .llmwiki/ indices                         │
│    - ~274 MB nomic-embed-text                                    │
│    - ~500 MB qwen2.5:0.5b                                        │
│    - ~200 MB stash Postgres 16                                   │
│    - ~69 GB headroom                                             │
│  RAM envelope: 4 GB                                              │
│    - ~600 MB-1 GB OS + sshd + housekeeping                       │
│    - ~500 MB Ollama + nomic-embed-text resident                  │
│    - ~500 MB qwen2.5:0.5b (consolidation, loaded on-demand)      │
│    - ~300-500 MB Node runtime + kb-server                        │
│    - ~200 MB Postgres 16 + pgvector (stash DB)                   │
│    - ~50 MB stash Go binary                                      │
│    - ~1-1.75 GB headroom                                         │
│  NOTE: 4 GB RAM is adequate for current services. Adding a       │
│  chat model (e.g. qwen3:8b ~4.9 GB) requires CPX31 (8 GB) —     │
│  Hetzner snapshot upgrade ~10 min downtime.                      │
└──────────────────────────────────┬───────────────────────────────┘
                                   │  MCP over HTTP+SSE (intra-Hetzner)
                                   │  the production brain queries here
                                   ▼
┌──────────────────────────────────────────────────────────────────┐
│  PRODUCTION HETZNER SERVER (existing, unchanged)                 │
│  /opt/cemini/                                                    │
│    services/llm_analyst/deepseek_client.py                       │
│        + extended to query librarian MCP for analyst-node        │
│          context before scatter-gather Send-API fan-out          │
│    agents/orchestrator.py                                        │
│        + LangGraph nodes call librarian MCP at need              │
│    [40 deployed containers per K5/K8 server probe — unchanged]   │
│  Disk: existing                                                  │
│  RAM: 7 GB (per K8) — NOT loaded with librarian; load unchanged  │
└──────────────────────────────────────────────────────────────────┘
```

#### Why this topology preserves the librarian doctrine

The `CLAUDE.md` schema's distribution layer ("Stage candidates in `briefs/` first; never push directly to the server") is preserved:
- Laptop remains the **canonical editor** (where K-pass deep reads happen, where this conversation runs)
- Sync to librarian server is **deliberate** (rsync via SSH, cron + manual trigger) — same shape as `briefs/` distribution to production
- Librarian server is a **downstream consumer**, not an alternate canonical
- The two-server-on-Hetzner pattern is the same shape as workspace ↔ production: one curates, the other consumes; sync is intentional

The doctrine evolution: previously "laptop curates, production consumes briefs"; now "laptop curates, librarian consumes wiki, production brain consumes librarian MCP." Three-stage instead of two-stage; same direction of flow.

### Sizing the librarian server

Hetzner Cloud CPX-tier (AMD EPYC) Ashburn region pricing as quoted 2026-04-28:

| Tier | vCPU | RAM | NVMe | Traffic | $/mo | Verdict for librarian |
|---|---|---|---|---|---|---|
| **CPX21** ✅ committed | 3 | 4 GB | 80 GB | 2 TB | **$13.99** | **Sufficient for stated requirement (embeddings-only spec).** Resident-RAM math: ~600 MB-1 GB OS + ~500 MB Ollama+nomic-embed-text + ~300-500 MB Node+llm-wiki-compiler = ~1.4-2 GB total → **~2-2.6 GB headroom.** 80 GB NVMe is wildly over-provisioned for the workload (~7-8 GB used → 72 GB headroom). |
| CPX31 | 4 | 8 GB | 160 GB | 3 TB | $24.99 | **Future-flexibility tier** — adds room for one quantized 7B-class chat model (qwen3:8b ~4.9 GB resident) alongside librarian services, OR cpr-pattern Postgres + pgvector colocated. **Defer until usage signals it's needed**; Hetzner snapshot-based upgrade from CPX21 → CPX31 is ~10 min downtime. |
| CPX41 | 8 | 16 GB | 240 GB | 4 TB | ~$50/mo | Overprovisioned for librarian alone. Justified only if running fully-local 14B-class chat models (qwen3:14b ~9 GB resident) routinely. |

**Default: CPX21 — committed 2026-04-28.** $13.99/mo = ~$168/yr. The "more than the production server" question (raised by user 2026-04-28) was the trigger for sizing-down from the earlier CPX31 default; CPX21 is the **right size for the stated spec, not "future flexibility insurance."** Hetzner snapshot-based upgrade to CPX31 is available later if usage signals chat-model-on-librarian becomes needed.

Vendor selection rationale: Hetzner-same-vendor-as-production wins on (a) intra-DC / intra-region latency for the production-brain → librarian-MCP query path, (b) unified ops surface (same Hetzner Cloud control panel, same SSH workflow, same monitoring scrape pattern), (c) competitive pricing — surveyed alternatives 2026-04-28: OVHcloud VPS Comfort ~$11/mo (savings $3/mo, vendor-diversification cost), Vultr/Linode/DigitalOcean $24/mo at this tier (more expensive), Contabo VPS M $9.50/mo with 16 GB RAM (genuinely cheaper but lower-tier SLA — inappropriate for the 24/7 critical reliability target), Oracle Cloud Free Tier $0 with 24 GB RAM ARM (genuinely free but account-reclamation horror stories + ARM-only friction make it operationally risky for "the brain depends on this").

`[NEEDS VERIFICATION 2026-04-28]` Hetzner Cloud Ashburn pricing should be re-checked at provisioning time; tier specs and pricing change.

### Migration plan (phased)

**Phase 0 — Smoke test (already queued as WTE-1 in ROADMAP)**

Run llm-wiki-compiler on the laptop with Path A (Claude Code zero-config Anthropic auth) in `--review` mode. ~30 min wall-clock. Validates:
- Tool works on our 380-page wiki at all
- Candidate review queue doesn't try to overwrite K-series hand-curated frontmatter
- LLM cost in the ~$0.60 first-compile estimate
- MCP retrieval surfaces cluster-hub pages correctly for cluster-level queries

**Pass-gate**: if smoke test reveals adoption-blocking issues, the entire migration plan is paused while alternatives are evaluated. **No CX server provisioned until smoke passes.**

**Phase 1 — Provision dedicated server**

- Sign up for Hetzner Cloud (or add to existing account if user already has one for production server)
- Provision **CPX21 in Ashburn** (same region as production server for low intra-DC latency)
- OS: Ubuntu 22.04 LTS or Debian 12 (matches production-stack OS family — keep ops surface unified)
- Configure: SSH key auth, ufw firewall (allow SSH from laptop + intra-DC traffic to production server only), **no public exposure of MCP endpoint** (production brain queries via Hetzner internal IP only)
- Install: Node ≥18, Ollama, llm-wiki-compiler global npm package
- Pull: `ollama pull nomic-embed-text`
- Set up `/opt/librarian/` directory tree

**Effort**: ~2 hours wall-clock if Hetzner-Cloud-fluent; first-time slower

**Phase 2 — Initial wiki sync**

- From laptop: `rsync -avz --delete wiki/ user@librarian-server:/opt/librarian/wiki/`
- This is one-time bulk sync; subsequent syncs are incremental (rsync's standard mode)
- Sync excludes raw sources (`research for cemini/`, `market dataset/`) — those stay on laptop
- Sync excludes `briefs/` — those follow the existing scp-to-production pattern, distinct from wiki distribution

**Phase 3 — Server-side compile + MCP serve** `[DONE 2026-04-29 — kb-server adopted in place of llm-wiki-compiler per Option C]`

- ✅ Node 22.22.2 + npm 10.8.2 installed on librarian (NodeSource setup_22.x)
- ✅ Ollama daemon installed + nomic-embed-text pulled (274 MB, listening on 127.0.0.1:11434, systemd-managed)
- ⚠️ llm-wiki-compiler v0.4.0 installed but **deployment-blocked**: hardcoded `CONCEPTS_DIR = "wiki/concepts"` flat-layout assumption is incompatible with our nested `concepts/` + `entities/` + `sources/` wiki. Smoke-tested 2026-04-28; LLM (DeepSeek API) correctly identifies pages from `wiki/index.md` but post-LLM slug-resolver mangles paths. Diagnosed in `cli.js`. Retained on disk for potential future compile-mode use, not running as a service. **See @concepts/wiki-tooling-evaluation.md "Wave 1 — REVISED" section for full diagnosis.**
- ✅ **kb-server (Wave 1 Option C)** installed + systemd-managed. `willynikes2/knowledge-base-server` (MIT, Obsidian-vault-native, FTS5 + Xenova local embeddings + 16-tool MCP). Empirically validated against our 395-page nested wiki: ingested in 0.7 seconds, all FTS5 queries return correct nested-path pages. Listens on `:3838`, scoped to `10.0.0.0/16` only via Hetzner Cloud Firewall.
- ✅ Smoke-test queries verified end-to-end: OMC paper (sources/), librarian-server-architecture (concepts/), nvda ticker (entities/tickers/) all resolve correctly with FTS5 BM25 ranking.

**Sub-tasks status**:
- ✅ **Read-only allowlist** `[DONE 2026-04-29 — Phase 3.5]`: patched `/opt/kb-server/src/mcp.js` and `/opt/kb-server/src/mcp-http.js` to honor `KB_TOOL_ALLOWLIST` env var. Allowlist set to `kb_search,kb_search_smart,kb_context,kb_read,kb_list,kb_vault_status,kb_safety_check` (7 read-only tools). Verified via stdio MCP `tools/list` — write tools (`kb_write`, `kb_ingest`, `kb_classify`, `kb_promote`, `kb_synthesize`, `kb_capture_*`) blocked. Patch lineage tracked at `cemini-librarian:/opt/cemini-wiki/.llmwiki/PATCHES.md`.
- ✅ **Sync automation** `[DONE 2026-04-29 — Phase 3.5]`: `scripts/sync_wiki_to_librarian.sh` does rsync + post-rsync `kb ingest`; macOS crontab entry `0 * * * *` runs it hourly. Logs to `~/Library/Logs/cemini-wiki-sync.log`. Tested manually; rsync + kb ingest both green.
- ✅ **Private-network bind** `[DONE 2026-04-29 — Phase 3.5e]`: cemini-prod attached to cemini-private at `10.0.0.3`; librarian at `10.0.0.2`. Patched `/opt/kb-server/src/server.js` to honor `KB_HOST` env var (defaults to `0.0.0.0` when unset; current setting `KB_HOST=10.0.0.2`). kb-server now listens on `10.0.0.2:3838` only — verified `ss -tlnp` shows the explicit bind, public IP `:3838` connection refused, localhost `:3838` connection refused, only the private-network IP answers. cemini-prod fetches `http://10.0.0.2:3838/` in **6.2ms** (sub-millisecond intra-DC latency as designed). Three-layer defense-in-depth: Hetzner Cloud Firewall (network) + explicit bind (process) + KB_TOOL_ALLOWLIST (application).
- ✅ **Prod → librarian SSH (2026-05-23)** `[CONFIRMED]`: From **inside** cemini-prod, `ssh cemini-librarian` via public ProxyJump looped/failed. **Use private net:** `ssh cemini-librarian-internal`, `ssh root@10.0.0.2`, or `./scripts/ssh_librarian.sh` on prod. Laptop unchanged: `ssh cemini-librarian` (ProxyJump). Handoff bundle for OSINT agents: `cemini-librarian:/opt/cemini-bulk/research/cemini-handoff/` — see @concepts/laptop-prod-research-split.md.
- ✅ **DeepSeek API key** provisioned at `/etc/llmwiki/env` (separately env-managed; configured for llmwiki — kb-server uses local Xenova embeddings instead, no DeepSeek dependency for serving).

**Effort**: ~5 hours total (Phase 3 + Phase 3.5; both landed 2026-04-29)

**Phase 4 — Wire production brain → librarian MCP**

- Extend `services/llm_analyst/deepseek_client.py` to query librarian MCP before scatter-gather Send-API fan-out (or as a per-analyst-node tool call)
- Brain LangGraph nodes call librarian MCP for wiki context as part of analyst-prompt construction
- Audit-trail integration: log each (query, response, ts) tuple to the existing pg_tamperlog (or its successor per `concepts/cryptographic-audit-trail.md` resolved-as-prescribed-not-built status)
- **Server-side dev work — out of scope for this workspace.** Stages in `briefs/` first per the librarian doctrine

**Effort**: ~3-5 engineer-days (server-side; not workspace-side)

**Phase 5 — Sync cron**

- Laptop crontab: `0 * * * * rsync ...` (hourly) or daily depending on update cadence
- Manual trigger preserved (e.g. after a substantive K-pass deep-read landing)
- Server-side incremental compile triggered by file-watch on `/opt/librarian/wiki/` (llm-wiki-compiler watch mode) or by post-rsync hook

**Effort**: ~1 hour

**Phase 6 — Monitoring + tuning** `[DONE 2026-04-29 (workspace-side); brief shipped to cemini-prod]`

**Sub-tasks status**:
- ✅ **6a — Librarian instrumentation**: `node_exporter` v1.8.2 systemd-managed on `cemini-librarian:10.0.0.2:9100` (private-network bound). Laptop-side `scripts/librarian_healthcheck.sh` cron at `*/5 * * * *` probing both `/api/v1/health` and `/metrics`; logs to `~/Library/Logs/cemini-librarian-health.log`. First run green (load1=0.01, mem_avail=3.2GB, disk_avail=61GB).
- ✅ **6b — Weekly Hetzner snapshots** (infrastructure staged; gated on user adding API token): `/opt/scripts/librarian_weekly_snapshot.sh` + `librarian-weekly-snapshot.{service,timer}` systemd files on librarian. Script uses curl directly against Hetzner Cloud API (no hcloud CLI dependency); rolling 4-week retention with auto-rotation; cost ~€0.95/mo. Stage-2: user generates Hetzner Cloud API token, saves to `/etc/hetzner/api-token`, enables timer.
- ✅ **6c — Cemini-prod observability brief**: `briefs/2026-04-29_librarian-observability-prod-integration.md` (295 lines) shipped to `cemini-prod:/opt/cemini/briefs/`. Defines Hetzner Cloud Firewall prereq (port 9100 inbound from 10.0.0.0/16), 2 Prometheus scrape jobs (system + blackbox), Promtail install on librarian forwarding kb-server.log + librarian-weekly-snapshot.log + systemd-journal to Loki on cemini-prod, 3 Grafana dashboards (librarian system health / kb-server activity / cross-server LSA migration health), 4 alerting rules (LibrarianDown / DiskNearFull / MemoryPressure / HighLoad).

**Effort actual**: ~3 hours workspace-side (Phases 6a + 6b infrastructure + brief). Server-stack-side execution of 6c is cemini-prod's Claude Code session task.

**Closure marker**: workspace mirrors `[ADOPTED]` once cemini-prod files `briefs/<date>_phase6c-completion-report.md` confirming Grafana dashboards live + alerts tested + Promtail forwarding logs.

**Phase 7 — Stash episodic memory `[DONE 2026-05-02]`**

Deployed alash3al/stash v0.2.9 on the librarian as the episodic memory layer — the Wave 5A Adopt verdict executed. Two-layer memory architecture now operational:

```
kb-server (:3838)          stash (:8080 MCP / :9090 HTTP)
├─ static wiki pages       ├─ episodes (timestamped events)
├─ source/entity/concept   ├─ facts (extracted assertions)
├─ markdown → RAG          ├─ working context (1h TTL)
└─ curated knowledge       ├─ contradictions (flagged conflicts)
                           ├─ causal links (fact → fact)
                           ├─ hypotheses (testable claims)
                           ├─ goals (tracked objectives)
                           └─ failure records (post-mortem log)
```

kb-server answers "what does the wiki say?" Stash answers "what happened, what did we learn, what are we tracking?"

Deployment details: pre-built binary v0.2.9 (Go 1.25.5 required, not available on Ubuntu 22.04). Postgres 16 + pgvector 768-dim. Ollama `nomic-embed-text` for embeddings, `qwen2.5:0.5b` (~500 MB) for consolidation reasoning — zero API cost. Systemd-managed (`stash.service`). Consolidation every 5 minutes, 168h window, similarity threshold 0.85. Primary namespace: `/cemini`. Bootstrap memories stored: CeminiSuite platform architecture overview + key facts.

RAM impact: Postgres ~200 MB + Stash Go binary ~50 MB + qwen2.5:0.5b ~500 MB = ~750 MB additional resident on the librarian's 4 GB envelope (~2.25 GB available after all services). Fits comfortably.

Full deployment record: `briefs/2026-05-02_stash-deployment-record.md`.

### Sync model `[REVISED 2026-04-28 — raw-layer migration to librarian]`

Wiki canonical = laptop (preserves librarian doctrine for the curated layer). **Raw layer canonical = librarian** (revised 2026-04-28 to free laptop disk and consolidate audit-grade backups; previously laptop-only). Sync is deliberate (rsync via SSH).

| Path | Canonical | Synced? | Notes |
|---|---|---|---|
| `wiki/` (laptop) → `cemini-librarian:/opt/cemini-wiki/wiki/` | Laptop | **Yes** | Canonical curated wiki — load-bearing for MCP serving |
| `wiki/log.md` | Laptop | Yes | Append-only log; rsync handles append cleanly |
| `wiki/index.md` | Laptop | Yes | Hand-maintained content-oriented catalog |
| `wiki/dashboard.md` | Laptop | Yes | Dataview queries — runs on Obsidian (laptop primary) |
| `briefs/` | Laptop (transient) | **No (separate channel)** | Distribution staging; uses scp to `/opt/cemini/briefs/` on production server. Production brain reads briefs as one-off context; librarian doesn't need them |
| `cemini-librarian:/opt/cemini-bulk/research/` | **Librarian (revised)** | One-way scp on ingest | 283 PDFs/docx (642 MB). Raw layer — immutable. `[MIGRATED 2026-04-28]` from laptop's `research for cemini/`. Backed up via Hetzner daily snapshots |
| `cemini-librarian:/opt/cemini-bulk/market-dataset/` | **Librarian (revised)** | One-way scp on update | 17.6k files (1.6 GB). Static historical data. `[MIGRATED 2026-04-28]` |
| `research to be indexed/` (laptop) | Laptop (transient) | **No** | Drop zone for new raw sources. Files move to librarian post-ingest, deleted from laptop |
| `.local/` | Laptop | **No** | Gitignored secrets + server connection details |
| `.claude/` | Laptop | **No** | Claude Code session context |
| `ROADMAP.md` / `LESSONS.md` / `CLAUDE.md` | Laptop | Optional | Reference-only on librarian; not load-bearing for MCP |

**Eventual consistency**: wiki sync max 1hr stale on hourly cron; raw-layer sync at the moment of ingest (not periodic — every new source flows scp-once-then-stays). Citation auditability is preserved because raw files exist persistently on a backed-up server, not because they exist on the laptop.

**Why raw layer moved to librarian (2026-04-28 revision)**: laptop disk pressure (90% capacity) made the original "laptop-only raw" stance untenable. Librarian has 65 GB free vs laptop's 21 GB. Audit-grade backup is *stronger* on the librarian (Hetzner daily snapshots + manual weekly retention) than on the laptop (Time Machine, easy to forget). Side-benefit: raw sources are now reachable from the brain via the same SSH/MCP channels, opening future "cite back to original PDF" capabilities.

### What unblocks

Specific items on `ROADMAP.md` that the librarian server unblocks:

- **WTE-1 → WTE adoption** decision (Phase 0 → Phase 1+ if smoke passes)
- **"Memory storage / reading / indexing — wiki growth"** subsection (most rows): LangGraph checkpointer wiring, cpr-pattern wiring, pgvector wiki-search, wiki-as-RAG embedding store — **most slot onto the librarian server cleanly** rather than fighting for RAM on the production trading-stack box
- **Open question: Hetzner host upgrade** — partially addressed (this is a separate dedicated box, not an in-place upgrade of production)
- **`entities/infrastructure/localai.md` / `ollama.md` / `deepseek-r1-14b.md` retraction lineage** — librarian server has the room to evaluate local-runtime paths without touching production. Embeddings-only Ollama (`nomic-embed-text`) becomes the **first concrete deployment of any Ollama-family runtime in the Cemini stack history**, ending the multi-month retracted-state on `ollama.md`

### What stays on the laptop `[REVISED 2026-04-28]`

- **Canonical wiki editing surface** — Obsidian + Dataview + git workflow stays exactly as today. The laptop is where K-passes happen, where this Claude Code session runs, where `wiki_lint.py` is human-triggered, where briefs are written
- **`research to be indexed/` drop zone** — transient laptop-side staging where new raw sources land before ingest. Post-ingest, files are scp'd to librarian and deleted from laptop
- **Briefs** — `briefs/` distribution to `cemini-prod:/opt/cemini/briefs/` on production server unchanged (existing scp workflow)
- **Claude Code librarian sessions** — read `wiki/` files directly via filesystem; no MCP needed for the laptop's own Claude Code instance to work with the wiki. For raw-source reads, ssh/scp from librarian as needed
- **Git canonical history** — `.git` stays on laptop; librarian server's `wiki/` is a derived working copy, not a git repo

### What moved to the librarian (2026-04-28)

- **Raw sources** — `research for cemini/` (formerly laptop) → `cemini-librarian:/opt/cemini-bulk/research/`. 283 PDFs/docx (642 MB).
- **Market dataset** — `market dataset/` (formerly laptop) → `cemini-librarian:/opt/cemini-bulk/market-dataset/`. 17.6k files (1.6 GB).
- **Workspace bulk freed**: ~2.3 GB. Laptop free space went from 21 GB → 23 GB (90% → 89% capacity).
- **Reads from librarian**: `ssh cemini-librarian "cat /opt/cemini-bulk/research/<file>"` for inspection; `scp cemini-librarian:/opt/cemini-bulk/research/<file> /tmp/` for local Preview/Adobe sessions. No mounts required; ad-hoc fetch as needed.

### Operational requirements (24/7 SLA)

The user-stated requirement (*"of utmost importance that the deployed cemini brain can query the library at any time as crypto markets are 24/7"*) translates to concrete SLA targets:

| Requirement | Target | How met |
|---|---|---|
| Availability | 99.9%+ (≤8.76 hr/yr downtime) | Hetzner Cloud SLA matches; CX32 in same region as production server keeps blast radius small |
| Recovery time | < 1 hr after node failure | Weekly snapshots + `hcloud-cli` script for snapshot-based rebuild |
| MCP query latency | p99 < 500ms | Intra-DC latency ~1-5ms; embeddings + index lookup ~100-300ms; total well within budget |
| Sync freshness | ≤ 1 hr stale | Hourly cron; manual trigger for fresh-data-required moments |
| Backup retention | ≥ 4 weeks | Hetzner snapshots monthly + offsite backup of canonical laptop wiki via git remote |
| Monitoring | Real-time | Existing Grafana/Loki/Prometheus stack scrapes new server (same Hetzner region = trivial setup) |
| Authentication | Hardened | SSH key only; MCP endpoint not exposed publicly (intra-DC traffic only); production brain queries via internal IP |

### IP-sale implications

The multi-server topology becomes part of any future IP-sale due-diligence:

- **Acquirer gets**: production trading stack (existing) + librarian server (new) + sync workflow + 380-page wiki (canonical) + dashboard + lint pipeline + MCP-bridge spec
- **Documentation burden**: increases modestly (two-server runbook instead of one-server runbook)
- **Reliability story**: improves materially. No-laptop-as-SPOF for the brain's knowledge layer. Hetzner-class reliability throughout
- **Cost line**: $13.99/mo (CPX21) + ~$1/mo snapshots = ~$15/mo additional ongoing OpEx ≈ $180/yr (visible to acquirer; trivial relative to trading-stack envelope)
- **Architectural defensibility**: an acquirer reading the architecture sees: "two-server topology, deliberate decoupling, server-class librarian dedicated to knowledge layer, brain queries it via MCP." This is the kind of architectural maturity that strengthens the IP-sale narrative alongside the K-series prescribed-vs-deployed reframing pattern. Cross-link to `concepts/ip-sale-readiness.md`

### Future expansion (post-migration)

The librarian server's CPX21 baseline headroom (~2-2.6 GB free RAM, ~72 GB free NVMe after services) creates room for some follow-on work without an upgrade. Anything requiring more RAM gates on a CPX21 → CPX31 upgrade (~$11/mo extra; ~10 min snapshot-based downtime to swap):

**Fits on CPX21** (no upgrade needed):
1. **Larger embedding models** — upgrade nomic-embed-text → mxbai-embed-large (670 MB / ~1 GB resident) → bge-m3 (1.2 GB / ~1.5 GB resident) as retrieval-quality benchmarks dictate. RAM math still fits in 4 GB envelope
2. **cpr-pattern reference impl (Python port from agentmemory)** — pipeline shape (Compress / Preserve / Resume) ports into Python with modest RAM footprint (~200-500 MB per service). Compress phase calls DeepSeek API (no local model); Preserve goes to librarian-local Postgres + pgvector (~500 MB-1 GB); Resume reads back into librarian MCP responses. Tight on CPX21 once pgvector is added; CPX31 if it grows
3. **Wiki-as-RAG embedding store** — librarian's nomic-embed-text instance double-duties: embeddings for llm-wiki-compiler's semantic search + embeddings for the brain's per-query RAG retrieval. One pgvector instance, two consumers; same RAM envelope as item 2

**Requires CPX31 upgrade** ($24.99/mo):
4. **Chat model on Ollama** — host one quantized 7B-class chat model (qwen3:8b ~4.9 GB resident) for fully-local Karpathy compile + as a LocalAI-equivalent for deployed-stack experimentation per `entities/infrastructure/localai.md` retraction lineage. Doesn't fit on CPX21's 4 GB; needs CPX31's 8 GB
5. **Multiple chat models or larger (14B-class)** — needs CPX41 ($50+/mo). Out of current scope

**Requires second instance**:
6. **Backup librarian** — second CPX21 in different Hetzner region as warm standby; rsync from primary librarian; snapshot fail-over for >4-9s downtime. Adds ~$15/mo. Defer unless 24/7 SLA targets need higher than Hetzner Cloud single-instance baseline (99.9%+)

**Upgrade path**: snapshot CPX21 → destroy → restore on CPX31 from the same snapshot. Hetzner Cloud advertises ~10 min downtime for this; in practice often 5-15 min depending on snapshot size. Can be done during pre-scheduled maintenance window when crypto-market signal-fire risk is acceptable

### Status

`[PHASES 0-6 SHIPPED; PHASE 7 (STASH) DEPLOYED 2026-05-02]` The librarian server is operational with kb-server (static wiki RAG) and stash (dynamic episodic memory). Phases 0-3.5 (provision, sync, kb-server, allowlist, cron) `[DONE 2026-04-29]`. Phase 4 (brain → librarian MCP) `[DONE 2026-04-30]`. Phase 5 (sync cron) `[DONE 2026-04-29]`. Phase 6 (monitoring + tuning) `[DONE 2026-04-29 workspace-side]`. Phase 7 (stash episodic memory) `[DONE 2026-05-02]`.

Maturity progression:
- `validated` (2026-04-28, planning-of-record)
- → `validated` (2026-05-02, phases 0-7 shipped; promoted-to-core gate is ≥30 days operational stability with all services including stash)

Future updates to this page should stamp each phase's commit SHA + ship date as it lands.

## Snippets

### From `concepts/wiki-tooling-evaluation.md` (parent decision document)

> "[DECISION 2026-04-28]: smoke-test path = Claude Code zero-config Anthropic auth. Ollama-for-embeddings deferred pending external storage."

> "Path C — Ollama embeddings sidecar (deferred — hardware-gated): When external storage lands and the laptop has comfortable headroom for a local Ollama instance […] This deferred posture matches the lineage on `entities/infrastructure/localai.md` / `entities/infrastructure/ollama.md` / `entities/infrastructure/deepseek-r1-14b.md` — local-runtime stories the workspace and the deployed Cemini stack can both adopt cleanly *if and when* hardware lands; until then, hosted/external paths fill the slot."

[Cross-doc note 2026-04-28: the Path C posture is now superseded — laptop-Ollama deferred indefinitely; embeddings will live on the new dedicated librarian server instead. External drive purchase cancelled.]

### User decision quote (2026-04-28)

> "we are going to want to go with option C then for sure and im going to not buy the drive. We can run the smoke test as is but plan for this all to be migrated to a server at some point here soon. Plan documents accordingly. it is going to be of utmost importance that the deployed cemini brain can query the library at any time as crypto markets are 24/7 and who knows when its going to need info."

### From `wiki/sources/llm-wiki.md` (Karpathy gist — the foundational pattern)

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

[Topology mapping: laptop = the IDE host (where editing happens); librarian server = the build server (where the codebase compiles + runs + serves queries); production trading-stack server = the runtime consumer (where the codebase's outputs land in deployed-product behavior).]

### From the K8 server-state calibration finding (2026-04-28)

> "**128 GB RAM (doc claim)** vs **7 GB total RAM** (`free -g` 2026-04-28) — **~18× over actual**."

[This is the load-bearing data point for rejecting Option A (sync to existing Hetzner) as a permanent solution. The production server's 7 GB envelope is already tight; adding Node + Ollama + nomic-embed-text + llm-wiki-compiler index would push the box. Dedicated CX32 = 8 GB just for librarian = clean separation.]
