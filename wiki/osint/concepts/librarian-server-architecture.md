---
title: Librarian Server Architecture (dedicated-host pattern for 24/7 wiki-as-library availability to the deployed Cemini brain)
type: concept
tags: [concept, architecture, infrastructure, librarian-tooling, hosting-topology, 24-7-reliability, cemini-brain, mcp-server, planned-not-built]
keywords: [librarian-server, hetzner-cx32, dedicated-host, three-server-topology, sync-model, mcp-bridge, 24-7-availability, crypto-market-reliability, librarian-doctrine]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/scatter-gather-topology.md
  - concepts/context-compression-resume-pattern.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/hetzner.md
  - entities/infrastructure/deepseek-api.md
  - entities/infrastructure/localai.md
  - entities/infrastructure/ollama.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - sources/llm-wiki.md
maturity: validated
created: 2026-04-28
updated: 2026-04-28
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
│    - ollama serve       <- port 11434 (embeddings only)          │
│    - llmwiki serve      <- MCP endpoint (stdio or HTTP+SSE)      │
│    - sshd               <- for laptop sync + admin access        │
│  Disk envelope: 80 GB NVMe                                       │
│    - ~5 GB OS + Node + Ollama runtime                            │
│    - ~1 GB wiki copy + .llmwiki/ indices                         │
│    - 274 MB nomic-embed-text                                     │
│    - ~72 GB headroom (room for future model collection or        │
│      cpr-pattern Postgres data)                                  │
│  RAM envelope: 4 GB                                              │
│    - ~600 MB-1 GB OS + sshd + housekeeping                       │
│    - ~500 MB Ollama + nomic-embed-text resident                  │
│    - ~300-500 MB Node runtime + llm-wiki-compiler                │
│    - ~2-2.6 GB headroom                                          │
│  NOTE: 4 GB RAM is sized for the stated embeddings-only spec.    │
│  Chat models on Ollama (e.g. qwen3:8b ~4.9 GB resident) require  │
│  upgrading to CPX31 (8 GB) — Hetzner Cloud snapshot-based        │
│  upgrade ~10 min downtime; defer until usage signals it          │
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

**Phase 3 — Server-side compile + MCP serve**

- On librarian server: `cd /opt/librarian && llmwiki compile` (full first compile)
- Review for correctness (server-side equivalent of `--review` queue)
- Stand up `llmwiki serve` as a systemd service (auto-restart on failure, persists across reboots)
- Test MCP endpoint locally: smoke-test query against the wiki

**Effort**: ~1-2 hours

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

**Phase 6 — Monitoring + tuning**

- Add librarian server to existing Grafana / Prometheus / Loki observability stack (Hetzner same-region target = trivial)
- Track: MCP request latency, compile-pass duration, embeddings-call cost (if Path B with DeepSeek API later swapped in for chat)
- Tune: compile cadence, sync frequency, MCP-tool selection
- Snapshot policy: weekly Hetzner Cloud snapshots (~$0.012/GB/mo per Hetzner; CPX21 80 GB max snapshot footprint ~$1/mo)

**Effort**: ongoing; ~1 hour initial setup

### Sync model

Laptop is canonical (preserves librarian doctrine). Sync is deliberate (rsync via SSH). What syncs:

| Path | Synced? | Notes |
|---|---|---|
| `wiki/` | **Yes** | Canonical wiki — the load-bearing artifact for the librarian server |
| `wiki/log.md` | Yes | Append-only log; rsync handles the append cleanly |
| `wiki/index.md` | Yes | Auto-generated index |
| `wiki/dashboard.md` | Yes | Dataview queries — runs on whichever Obsidian instance you connect (laptop primary) |
| `briefs/` | **No** | Distribution staging; uses existing manual scp to `/opt/cemini/briefs/` on production server. Different distribution channel, different consumer (production brain reads briefs as one-off context; librarian server doesn't need briefs) |
| `research for cemini/` | **No** | Raw sources — immutable per librarian doctrine. Stay on laptop |
| `market dataset/` | **No** | Raw market data; stays on laptop until ROADMAP item E (storage compaction) is decided |
| `.local/` | **No** | Gitignored secrets and local-only config |
| `.claude/` | **No** | Claude Code session context; stays local |
| `ROADMAP.md` / `LESSONS.md` / `CLAUDE.md` | Optional | Useful as reference on server but not load-bearing for MCP queries |

**Eventual consistency**: max 1hr stale on hourly cron, plus the duration of the incremental compile (typically seconds-to-minutes for a single-page change per llm-wiki-compiler hash-incremental design).

### What unblocks

Specific items on `ROADMAP.md` that the librarian server unblocks:

- **WTE-1 → WTE adoption** decision (Phase 0 → Phase 1+ if smoke passes)
- **"Memory storage / reading / indexing — wiki growth"** subsection (most rows): LangGraph checkpointer wiring, cpr-pattern wiring, pgvector wiki-search, wiki-as-RAG embedding store — **most slot onto the librarian server cleanly** rather than fighting for RAM on the production trading-stack box
- **Open question: Hetzner host upgrade** — partially addressed (this is a separate dedicated box, not an in-place upgrade of production)
- **`entities/infrastructure/localai.md` / `ollama.md` / `deepseek-r1-14b.md` retraction lineage** — librarian server has the room to evaluate local-runtime paths without touching production. Embeddings-only Ollama (`nomic-embed-text`) becomes the **first concrete deployment of any Ollama-family runtime in the Cemini stack history**, ending the multi-month retracted-state on `ollama.md`

### What stays on the laptop

- **Canonical wiki editing surface** — Obsidian + Dataview + git workflow stays exactly as today. The laptop is where K-passes happen, where this Claude Code session runs, where `wiki_lint.py` is human-triggered, where briefs are written
- **Raw sources** — `research for cemini/` (PDFs / docx) and `market dataset/` (Stocks/, ETFs/, kaggle/) remain laptop-only per librarian doctrine ("immutable; the LLM reads them but never modifies them")
- **Briefs** — `briefs/` distribution to `/opt/cemini/briefs/` on production server unchanged (existing scp workflow)
- **Claude Code librarian sessions** — read wiki/ files directly via filesystem; no MCP needed for the laptop's own Claude Code instance to work with the wiki
- **Git canonical history** — `.git` stays on laptop; librarian server's `/opt/librarian/wiki/` is a derived working copy, not a git repo

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

`[PLANNED 2026-04-28 — NOT BUILT]` This page documents the architectural commitment + plan; **none of the migration phases have started.** Phase 0 (WTE-1 smoke test) is the gating decision — runs on laptop with Claude Code zero-config; if smoke fails, the whole plan pauses while alternatives are evaluated.

Maturity progression target:
- `validated` (today, planning-of-record)
- → `core` (after Phase 1+ ships and the librarian server is operationally stable for ≥30 days)

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
