---
title: "rohitg00/agentmemory — Apache-2.0 reference implementation of the cpr (compress / preserve / resume) pattern with PostToolUse hooks, SHA-256 dedup, BM25+Vector+Graph RRF fusion"
type: source
tags: [github, npm, mcp-server, persistent-memory, cpr-pattern, compress-preserve-resume, posttooluse-hook, rrf-fusion, agent-memory, reference-impl]
clusters: [llm-agents]
keywords: [agentmemory, rohitg00, iii-engine, posttooluse, sha-256-dedup, privacy-filter, rrf-reciprocal-rank-fusion, bm25-vector-graph, claude-md, mcp]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/context-compression-resume-pattern.md
  - sources/willynikes2-knowledge-base-server.md
  - sources/falkordb-graphrag-eval.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/fastmcp.md
  - entities/infrastructure/deepseek-api.md
  - concepts/librarian-server-architecture.md
  - sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - concepts/interaction-native-knowledge-harness.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
read_status: read
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @sources/arxiv-interaction-native-knowledge-harness-2606.01886.md — InKH temporal graph + RRF contrast (K99)
- @concepts/interaction-native-knowledge-harness.md — financial harness mapping
- @concepts/wiki-tooling-evaluation.md — synthesis page; **steal-architectural-details candidate** (Apache-2.0 license-clean; pipeline shape is reference-grade for the prescribed Python cpr-pattern wiring; runtime architecture wrong for our Python+7-GB-Hetzner constraints)
- @concepts/context-compression-resume-pattern.md — K8 promotion concept page; agentmemory is the **end-to-end working implementation** of the 3-phase Compress / Preserve / Resume pattern this concept page documents
- @sources/willynikes2-knowledge-base-server.md — sibling memory engine; opposite axis (kb-server = three-tier hot/warm/cold framing; agentmemory = compress-preserve-resume framing); both implement compounding-context loops
- @sources/falkordb-graphrag-eval.md — agentmemory's RRF fusion (BM25 + Vector + Graph) is what FalkorDB does natively as Cypher + HNSW; different shapes of the same hybrid-retrieval problem
- @entities/frameworks/langgraph.md — LangGraph's `PostgresSaver` checkpointer is the prescribed-not-built foundation for what agentmemory implements end-to-end (with iii-engine KV instead of Postgres); cross-stack architectural parallel
- @entities/frameworks/fastmcp.md — agentmemory exposes its functionality via MCP server (Apache-2.0); deployable alongside Cemini's `cemini_mcp` (130-tool FastMCP container) on different transports
- @entities/infrastructure/deepseek-api.md — agentmemory's "LLM compress" step calls a configurable LLM (6 providers + local); the same shape adopted in Python on the deployed Cemini stack would invoke the DeepSeek hosted API for the Compress phase

## Raw Concept

- **Original title**: agentmemory — *#1 Persistent memory for AI coding […] agent remembers everything*
- **Author**: Rohit Ghumare (rohitg00) + 7 other contributors
- **Type**: GitHub repo + npm package + (Apache-2.0)
- **URL**: https://github.com/rohitg00/agentmemory / https://agent-memory.dev (homepage)
- **Retrieved**: 2026-04-28 (via Exa `crawling_exa` + `web_search_exa` for license verification)
- **Stars**: 1945 ⭐⭐⭐
- **License**: **Apache 2.0** 🟢 (clean for IP sale)
- **Created**: 2026-02-25; **Last push**: 2026-04-22; **Latest release**: v0.9.2 (2026-04-22)
- **Stack**: TypeScript (83.3%), HTML (8.6%), JavaScript (6.0%), CSS (1.6%), Python (0.5%), Node.js ≥ 20, **iii-engine** as proprietary worker layer
- **Read status**: read (deep-read README; license verified against `LICENSE` file via Exa search; iii-engine dependency-layer flagged as proprietary-worker-stack)

## Narrative

agentmemory is a **TypeScript-first memory engine + MCP server** explicitly framed as "the implementation" of Karpathy's gist for persistent agent memory ("The gist extends […] search. agentmemory is the implementation"). It silently captures what an agent does via Claude Code (or any MCP client) PostToolUse hooks, compresses observations into searchable memory, and injects relevant context at session start.

For the Cemini wiki-tooling evaluation, **the architectural pipeline is more valuable than the runtime** — agentmemory's compress-preserve-resume pipeline shape, ported into Python, would directly implement the prescribed cpr-pattern wiring on the deployed Cemini stack (LangGraph `PostgresSaver` checkpointer + DeepSeek summarization-node + pgvector storage trio).

### The full pipeline (verbatim from README)

```
PostToolUse hook fires
  -> SHA-256 dedup (5min window)
  -> Privacy filter (strip secrets, API keys)
  -> Store raw observation
  -> LLM compress -> structured facts + concepts + narrative
  -> Vector embedding (6 providers + local)
  -> Index in BM25 + vector + knowledge graph
```

Each stage is independently liftable into Python:

1. **PostToolUse hook** ↔ Cemini equivalent: a LangGraph node-output capture, OR a FastMCP tool-call wrapper. Either is implementable in ~30 LOC.
2. **SHA-256 dedup with 5-min window** — primitive directly portable. Hash the observation; if hash within 5 min already seen, drop.
3. **Privacy filter** — strip API keys, secrets. Critical given the 2026-04-24 retraction work caught wiki claims about credentials. Implementable as a regex-based scrubber + allowlist.
4. **Store raw observation** — postgres / pgvector row insert.
5. **LLM compress** — call DeepSeek API (or Anthropic) to convert raw observation into `(facts[], concepts[], narrative_summary)`. Same shape as the cpr-pattern Compress phase.
6. **Vector embedding (6 providers + local)** — sentence-transformers in Python; same multi-provider story as `entities/infrastructure/deepseek-api.md`.
7. **Index in BM25 + vector + knowledge graph** — RRF fusion (Reciprocal Rank Fusion) merges three rankings into one. Better retrieval than vector-alone for cross-cutting queries.

### Reciprocal Rank Fusion (RRF) — the retrieval innovation worth stealing

agentmemory uses RRF to combine 3 rankings:
- **BM25** (keyword match) — finds specific terms and exact phrases
- **Vector similarity** (semantic) — finds related-meaning content
- **Knowledge graph** (relationships) — finds connected concepts via traversal

RRF formula: for each item, `rrf_score = sum(1 / (k + rank_in_each_ranking))`, where `k` is typically 60. Robust to outlier rankings (no single retrieval method dominates). Reported retrieval R@5 95.2% on the project's own benchmark (vs MemGPT 68.5%, Mem0 83.2% on LoCoMo) — take with salt since same-author benchmarking, but the RRF technique is well-established academically.

For the wiki-tooling-evaluation, this is the **better retrieval story than llm-wiki-compiler's index-based query routing** for cross-document Cemini-side queries. If agentmemory's pipeline gets ported to Python:
- **BM25** ↔ trivial to add via `rank-bm25` Python library or PostgreSQL FTS
- **Vector** ↔ pgvector + sentence-transformers
- **Knowledge graph** ↔ either Cypher-over-FalkorDB-as-derived-index OR plain PostgreSQL recursive CTE over the `related:` edges (no separate graph DB needed)

### Configuration safety: AGENTMEMORY_AUTO_COMP=OFF by default

The README's strongest operational safety note:

> "AGENTMEMORY_AUTO_COMP — OFF by default (#138). When on, every PostToolUse fires the LLM the observation — expect significant token spend on active sessions"

**Compression is gated.** Defaults to OFF. Only fires when explicitly enabled. This is exactly the right operational posture: don't burn DeepSeek API tokens on every tool call by default; let the operator opt in. Same posture our workspace already takes (`scripts/wiki_lint.py` runs human-triggered, not on-every-edit) and same posture the cpr-pattern concept page should specify when ported to Python.

### Why we cannot deploy the runtime as-is

Three reasons block adoption-as-runtime:

1. **TypeScript primary stack.** Cemini deployed stack is Python (FastAPI + LangGraph + Polars + pgvector + Redis). Adding Node.js to the 7 GB Hetzner host is a heavy ask for what could be a Python port.
2. **iii-engine proprietary dependency layer.** README's "What iii-engine replaces" table:

| Traditional stack | agentmemory uses |
|---|---|
| Express.js / Fastify | iii HTTP Triggers |
| SQLite / Postgres + pgvector | iii KV State + in-memory vector index |
| SSE / Socket.io | iii Streams (WebSocket) |
| pm2 / systemd | iii-engine worker management |
| Prometheus / Grafana | iii OTEL + health monitor |

iii-engine is the runtime substrate. It's not separately documented in the README. Its license is also not explicit in what we crawled — would require a separate `crawling_exa` against the iii-engine repo to verify it's not GPL/AGPL/SSPL/PolyForm-Noncommercial. Until verified, **iii-engine is a transitive license risk** even though agentmemory itself is Apache-2.0. (Adoption-blocker even if we wanted Node on the server.)

3. **Memory footprint.** 21,800 LOC + 800 tests + iii-engine + Node.js runtime adds up to several GB of process memory at minimum. On the 7 GB Hetzner host already running 40 Docker containers, this is a hard squeeze.

### What we adopt: the pipeline, in Python, in-house

**Concrete port plan** (sketched here; should land in a separate brief or concept-page-extension):

1. Module: `services/cemini_memory/cpr_pipeline.py`
2. Hooks: LangGraph node post-call hook OR FastMCP tool-call wrapper writes observation to a `cemini_memory.raw_observations` Postgres table
3. SHA-256 dedup: 5-min window via `SELECT … WHERE hash = $1 AND ts > NOW() - interval '5 minutes'`
4. Privacy filter: regex scrubber on `OPENAI_API_KEY`, `DEEPSEEK_API_KEY`, `KALSHI_API_KEY`, `POLYGON_API_KEY`, `OANDA_*`, `BREX_*`, `IBKR_*`, etc.; deny-by-default
5. Compress: async DeepSeek API call returning `(facts[], concepts[], narrative)` JSON
6. Vector embedding: sentence-transformers `all-MiniLM-L6-v2` (the same Xenova model knowledge-base-server uses; ~80 MB) → pgvector
7. BM25: PostgreSQL FTS index on the narrative + facts text
8. Knowledge graph: existing `related:` edges in the wiki + a new `cemini_memory.observation_links` table for inter-observation graph
9. RRF fusion query: PostgreSQL CTE combining BM25 rank + pgvector cosine rank + recursive-CTE graph distance
10. `AGENTMEMORY_AUTO_COMP_ENABLED=false` env flag — OFF by default; gated by operator

Total Python LOC estimate: **~600-800 LOC** (vs agentmemory's 21,800 TS LOC). Most of the bulk in agentmemory is iii-engine integration + Node tooling + dashboard; the actual pipeline core is leaner than the LOC suggests.

## Snippets

### S1 — Pipeline (`README.md`)

> "PostToolUse hook fires → SHA-256 dedup (5min window) → Privacy filter (strip secrets, API keys) → Store raw observation → LLM compress → structured facts + concepts + narrative → Vector embedding (6 providers + local) → Index in BM25 + vector + knowledge graph"

### S2 — Auto-compression safety default (`README.md`)

> "AGENTMEMORY_AUTO_COMP — OFF by default (#138). When on, every PostToolUse fires the LLM the observation — expect significant token spend on active sessions"

### S3 — Karpathy gist framing (`README.md`)

> "The gist extends [...] search. agentmemory is the implementation."

### S4 — iii-engine dependency table (`README.md`)

| Traditional stack | agentmemory uses |
|---|---|
| Express.js / Fastify | iii HTTP Triggers |
| SQLite / Postgres + pgvector | iii KV State + in-memory vector index |
| SSE / Socket.io | iii Streams (WebSocket) |
| pm2 / systemd | iii-engine worker management |
| Prometheus / Grafana | iii OTEL + health monitor |

### S5 — Retrieval R@5 comparison (`README.md`)

> "Retrieval R@5: 95.2% [agentmemory] vs 68.5% (MemGPT) vs 83.2% (LoCoMo, Mem0)"

[Same-author benchmark; the underlying RRF technique is academically established but the specific numbers should be reproduced in our own evaluation before commitment.]

### S6 — Apache-2.0 license + DCO requirement (`CONTRIBUTING.md` via Exa)

> "Apache-2.0 license applies to every contribution. Sign-off is required on every commit (see DCO below). […] No attribution headers ('Generated with Claude Code', 'Co-Authored-By: Claude', etc.) in commits or PR descriptions."

[Apache-2.0 confirmed. Note: their CONTRIBUTING.md disallows Claude attribution headers in PRs — would need to handle if we ever upstream changes; doesn't affect us using their code.]
