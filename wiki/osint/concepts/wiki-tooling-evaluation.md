---
title: Wiki & Memory Tooling — Evaluation of Adoption Candidates
type: concept
tags: [wiki-tooling, memory, knowledge-base, librarian-layer, ip-sale-readiness, evaluation, decision-pending, karpathy-pattern]
keywords: [llm-wiki-compiler, memex, knowledge-base-server, falkordb, agentmemory, emtwiki, karpathy-pattern, mcp-server, graphrag, three-layer-architecture]
related:
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/willynikes2-knowledge-base-server.md
  - sources/wastedcode-memex.md
  - sources/emtwiki-deployed-example.md
  - sources/falkordb-graphrag-eval.md
  - sources/agentmemory-rohitg00-cpr-impl.md
  - sources/llm-wiki.md
  - concepts/context-compression-resume-pattern.md
  - concepts/scatter-gather-topology.md
  - concepts/cryptographic-audit-trail.md
  - concepts/ip-sale-readiness.md
  - entities/infrastructure/localai.md
  - entities/infrastructure/deepseek-api.md
  - entities/frameworks/fastmcp.md
maturity: validated
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @sources/atomicmemory-llm-wiki-compiler.md — Karpathy-pattern compiler; **primary adoption candidate**; covers GitHub + `llmwiki.app` landing page
- @sources/willynikes2-knowledge-base-server.md — SQLite + FTS5 + embeddings memory engine + 16-tool MCP server; sidecar value gated on multi-agent need
- @sources/wastedcode-memex.md — Filesystem-only (no embeddings) Claude-Code-programmatic-mode wrapper with namespace isolation; adoption-rejected on Linux/CAP_SYS_ADMIN friction
- @sources/emtwiki-deployed-example.md — deployed example wiki (San Juan College EMT-Basic curriculum, NM EMS Bureau-aligned); reference-only proof the pattern works in high-stakes domains
- @sources/falkordb-graphrag-eval.md — sparse-matrix property-graph DB with native HNSW; SSPL-licensed (poison for IP-sale on the deployed stack); workspace-side experiment candidate
- @sources/agentmemory-rohitg00-cpr-impl.md — Apache-2.0 cpr-pattern reference implementation in TypeScript; **steal-architectural-details candidate**, not deploy
- @sources/llm-wiki.md — Karpathy's 2025 gist; the foundational pattern source the schema is built against (K2-validated 2026-04-26)
- @concepts/context-compression-resume-pattern.md — K8 promotion; the Compress/Preserve/Resume pattern that agentmemory implements end-to-end
- @concepts/scatter-gather-topology.md — wiki-as-RAG would be queried by the scatter-gather analyst nodes; tooling decision touches this concept's open P1 ticket
- @concepts/cryptographic-audit-trail.md — confidence + contradicted-by metadata in llm-wiki-compiler is machine-readable analog to the cryptographic-audit-trail's tamper-anchored claim ledger; complementary, not redundant
- @concepts/ip-sale-readiness.md — license posture is the dominant axis on adoption (SSPL/AGPL/PolyForm-Noncommercial all rejected on this page; MIT/Apache-2.0 candidates pre-vetted)
- @entities/infrastructure/localai.md — operational LLM-runtime slot for any locally-hosted compile/query loop; matches the same `base_url` swap pattern adopted tools would use
- @entities/infrastructure/deepseek-api.md — operative LLM brain today; multi-provider tools (llm-wiki-compiler, knowledge-base-server) all support DeepSeek via `OPENAI_BASE_URL` swap
- @entities/frameworks/fastmcp.md — deployed Cemini MCP layer; any adopted tool's MCP server must coexist (separate transport / separate URL) with the existing 130-tool `cemini_mcp` container

## Raw Concept

User-dropped 7 candidates across two turns (2026-04-28) for evaluating against the workspace librarian and the cpr-pattern wiring item: FalkorDB, `rohitg00/agentmemory`, `atomicmemory/llm-wiki-compiler` (+ landing page `llmwiki.app/`), `willynikes2/knowledge-base-server`, `wastedcode/memex`, `emtwiki.endusergeek.com/`. Underlying question — explicit in the user's framing on the prior turn ("any other improvements to get us to llm wiki by karpathy status of operational efficiency"): **should the workspace continue hand-rolling Karpathy's LLM Wiki pattern, adopt one of these tools, or steal architectural details and build the missing 30%?**

This page synthesizes the candidates against the schema in `CLAUDE.md` and the existing ROADMAP open questions ("Operational efficiency toward Karpathy LLM Wiki standard," "Memory storage / reading / indexing — wiki growth," "Wiki-as-RAG embedding store"). Decision gate: pick a path before the next K-series cited-unread queue continuation, OR commit to hand-rolling the remaining ~6 of 10 Karpathy operations.

## Narrative

### Where we are today (status quo)

The workspace librarian currently implements **4 of 10** Karpathy LLM Wiki operations directly:
- ✅ **Schema** — `CLAUDE.md` codifies the three-layer raw/wiki/schema architecture, page-type templates, frontmatter shape, bidirectional `related:` discipline
- ✅ **Wiki structure** — `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, hash-stable slugs, dated frontmatter, append-only `wiki/log.md`
- ✅ **Lint** — `scripts/wiki_lint.py` (orphans, bidir gaps, dangling, missing @paths, cited-unread, frontmatter quality, stale `[NEEDS VERIFICATION]` tags)
- ✅ **Manual ingest workflow** — `CLAUDE.md` "Operations" section: read → discuss → source page → identify entities/concepts → update related → log

NOT implemented (manual today, or absent):
- ❌ **Automated ingest** — no LLM-driven entity/concept extraction → page generation; we hand-write each new page
- ❌ **Hash-based incremental compile** — we re-write what we change; nothing tracks "what source-page has drifted from its underlying source PDF"
- ❌ **Compounding query → save-back loop** — manually filed via `briefs/`; not idempotent; no machine-readable provenance
- ❌ **Watch mode** — no auto-recompile on file change (cron is the closest equivalent)
- ❌ **MCP server** — the workspace wiki is not exposed as an MCP server; the dev-stack `cemini_mcp` (130-tool FastMCP container) is a separate concern
- ❌ **Confidence + contradicted-by metadata** — we use inline `[CONFIRMED]` / `[TENTATIVE]` / `[NEEDS VERIFICATION]` / `[RETRACTED]` tags. Not machine-readable per-page; not surfaced in lint; doesn't drive retrieval ranking

The K-series deep-read pattern (J/K/K2/K3/K4/K5/K6/K7/K8) and the K8 stale-snapshot finding (~18× off on RAM, ~6× off on FastMCP tool count) suggest the **stale-claim-vs-deployed-state drift** is a recurring failure mode the schema doesn't yet machine-defend against. Confidence + `contradictedBy[]` per-page metadata would let lint surface drift candidates the way bidir-gap detection surfaces structural drift today.

### The seven candidates — comparison table

| Candidate | License | Stack | Stars | Maturity | Architectural fit | Adoption cost | Migration cost |
|---|---|---|---|---|---|---|---|
| **llm-wiki-compiler** (atomicmemory) | MIT 🟢 | TypeScript, Node ≥18 | 701 | Active (v0.2.0 2026-04-16) | **Highest** — direct Karpathy impl; same three-layer + frontmatter shape | Low (`npm install -g`) | **Low** — hash-incremental against existing wiki; Obsidian-compatible |
| **memex** (wastedcode) | MIT 🟢 | TypeScript, Node ≥20, Linux mount-namespace, CAP_SYS_ADMIN | 56 | New (2026-04-06 created) | High — filesystem-only, no embeddings, "Claude is smart enough to grep" | Medium (sudo daemon, namespace setup) | Low (filesystem-native) |
| **knowledge-base-server** (willynikes2) | MIT 🟢 | JavaScript, Node ≥18, Express :3838, SQLite + FTS5 + Xenova embeddings | 162 | Newer (2026-03-07) | Medium — opinionated three-tier (hot/warm/cold) memory + 16-tool MCP | Medium (Express daemon + auth + setup wizard) | **High** — re-ingest 373 pages into SQLite |
| **FalkorDB** | **🔴 SSPL v1** | C/Python, Redis-module, GraphBLAS | 4164 | Mature (v4.18.1) | High *for the wiki-as-graph* (bidir `related:` is already a graph) | Low (Docker) | Medium (write Cypher importer for our 373 pages) |
| **agentmemory** (rohitg00) | Apache-2.0 🟢 | TypeScript, Node + iii-engine | 1945 | Active (v0.9.2 2026-04-22) | **Lowest as runtime** (TS+iii-engine doesn't fit Cemini's Python stack); **highest as reference impl** for cpr-pattern | High (Node runtime + iii-engine on 7 GB Hetzner = no) | Don't migrate; steal pipeline shape into Python |
| **emtwiki.endusergeek.com** | n/a (deployed wiki) | Likely memex or mkdocs | n/a | Live (2026-04-05 last update) | n/a — deployed example | Reference only | n/a |
| **Status quo (hand-roll)** | n/a (own tools) | Python 3 (`wiki_lint.py` / `bootstrap_inbox.py` / `build_cluster_hubs.py`) | n/a | 4 of 10 Karpathy ops; substantive K-series read pace | Native | Zero | Zero, but ongoing manual cost |

### Architectural axis 1: filesystem-first vs database-first

The candidates split cleanly along this axis:

**Filesystem-first** (markdown files are the source of truth; tools read/write them in place):
- Status quo (Python tools + Obsidian + lint indices)
- llm-wiki-compiler (writes to `wiki/concepts/`, `wiki/queries/`, `wiki/index.md`; Obsidian-compatible)
- memex (literally only operates on `/workspace/*.md` inside a mount namespace)
- emtwiki (deployed example — appears filesystem-based)

**Database-first** (the DB is the source of truth; markdown is an export or sync layer):
- knowledge-base-server (SQLite + FTS5 is canonical; Obsidian sync is bidirectional but the DB is the brain)
- FalkorDB (graph is canonical; markdown is import/export only)
- agentmemory (iii-engine KV store + in-memory vector index canonical)

**Cemini-side preference: filesystem-first.** Reasons: (a) git is the version-control story we already have; (b) Markdown is the format every editor + every LLM understands without translation; (c) the `wiki/log.md` audit trail + hash-stable slugs already give us reproducibility; (d) database-first tools require either a "DB is canonical, markdown is export" mental shift (heavy migration) or a "DB shadows markdown, sync drift is a real risk" architecture (operational complexity). The K-series stale-snapshot pattern shows we already deal with one drift problem (source-vs-deployed-state); we don't want to add a second (DB-vs-markdown).

**Acceptable database-first slot:** workspace-side experiment with FalkorDB or knowledge-base-server **as a derived index over the existing markdown wiki** — markdown stays canonical, DB rebuilds nightly from filesystem scan. Reverses the migration risk: if the experiment fails, delete the DB; nothing was lost.

### Architectural axis 2: Karpathy LLM Wiki pattern coverage

The Karpathy gist (`sources/llm-wiki.md`, K2-validated) describes 10 operations. Coverage matrix:

| Karpathy op | Status quo | llm-wiki-compiler | memex | knowledge-base-server | agentmemory |
|---|---|---|---|---|---|
| Data ingest | ✅ manual | ✅ `llmwiki ingest` | ✅ `memex ingest` | ✅ `kb_ingest` | ✅ PostToolUse hook |
| Compile wiki | ❌ manual | ✅ `llmwiki compile` (2-phase) | ✅ daemon job queue | ✅ classify + promote pipeline | ✅ LLM compress |
| Q&A | ❌ manual | ✅ `llmwiki query` | ✅ `memex query` | ✅ `kb_search`/`kb_search_smart` | ✅ retrieval R@5 95.2% (own bench) |
| Output filing (save back) | ✅ via `briefs/` | ✅ `--save` | ✅ "good answers filed back" | ✅ `kb_promote` | ✅ knowledge graph indexing |
| Auto-recompile (watch) | ❌ | ✅ `llmwiki watch` | ❌ | ✅ vault sync | ✅ 12 hooks |
| Lint / health-check | ✅ `wiki_lint.py` | ✅ `llmwiki lint` (incl. `low-confidence`, `contradicted-page`, `excess-inferred-paragraphs`) | ✅ `memex lint` | ❌ | ❌ |
| Agent integration (MCP) | ❌ | ✅ `llmwiki serve` (7 tools, 5 resources) | ❌ | ✅ 16 MCP tools + REST | ✅ MCP + REST + leases |
| Image support | ❌ | ❌ (roadmap) | ✅ (Claude reads images) | ✅ (PDF text extraction; not images) | ❌ |
| Marp slides | ❌ | ❌ (roadmap) | ❌ | ❌ | ❌ |
| Fine-tuning | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Coverage** | **4 of 10** | **7 of 10** | **5 of 10** | **6 of 10** | **5 of 10** |

llm-wiki-compiler is the most complete Karpathy-pattern implementation in the candidate set — 7-of-10 to our 4-of-10. The 3 it doesn't cover (image / Marp slides / fine-tuning) are the same 3 nobody covers; not differentiating.

### Recommended path forward

**Adopt:** **`llm-wiki-compiler`** for the workspace librarian layer.

Rationale:
1. Implements 7-of-10 Karpathy operations as off-the-shelf functionality; we'd need ~3-6 engineer-weeks of Python tooling work to match that natively
2. Hash-based incremental compile means it can run on our existing 373-page wiki without re-ingesting (verify via `--review` candidate queue before any pages land)
3. MIT-licensed — passes the IP-sale poison-pill filter
4. Multi-provider — works with Claude Code today; swappable to DeepSeek API or local LocalAI later via `OPENAI_BASE_URL` (matches the same architectural pattern as `entities/infrastructure/deepseek-api.md`)
5. **Confidence + `contradictedBy[]` per-page metadata** directly addresses the K-series stale-snapshot problem — pages that get retracted carry machine-readable contradiction metadata, not just inline `[RETRACTED]` text
6. **MCP server** (`llmwiki serve`) means the dev-stack DeepSeek brain on Hetzner could query the workspace wiki via MCP — closes the laptop ↔ server gap that's been a recurring constraint, without requiring server-side knowledge-base re-deployment (Track B remains scoped to its own stack)
7. Obsidian-compatible `[[wikilinks]]` — preserves the existing Obsidian + Dataview workflow (see `L` row in ROADMAP Done)
8. Candidate review queue (`--review`) — stages LLM output as candidates rather than letting it overwrite hand-curated pages directly. Aligns with "human reads, LLM writes" but keeps a confirm-before-merge gate

**Steal-from:** **`agentmemory`** (Apache-2.0).

Rationale: literally an end-to-end cpr-pattern implementation. We cannot deploy the runtime on the Cemini stack (TS + iii-engine + 7 GB Hetzner = wrong architecture) but the pipeline is reference-grade for the prescribed Compress/Preserve/Resume wiring on the dev stack:
- **SHA-256 dedup** with 5-min window — direct primitive to lift into the cpr-pattern Compress phase
- **Privacy filter** (strip API keys, secrets) — directly relevant given the 2026-04-24 retraction work where the wiki was caught implying claims about credentials and proprietary state
- **BM25 + Vector + Knowledge-Graph RRF (Reciprocal Rank Fusion)** — better retrieval shape than pgvector-alone for the wiki-as-RAG path
- **OFF-by-default auto-compaction** (`AGENTMEMORY_AUTO_COMP`) — operational safety pattern; never compress without explicit gate

Implementation: re-implement the same shape in Python on the deployed Cemini stack alongside the prescribed LangGraph `PostgresSaver` checkpointer + DeepSeek summarization-node + pgvector storage trio (see `concepts/context-compression-resume-pattern.md` and the K8-promoted ROADMAP "Memory storage / reading / indexing" subsection).

**Defer:** **`FalkorDB`** + **`knowledge-base-server`**.

- *FalkorDB*: SSPL-blocker for the deployed Cemini stack (poison-pill family with AGPL — acquirer DD will flag it). Could be a workspace-side experiment ("derived index over markdown") if the SSPL workspace-only-tooling distinction holds, but the experiment doesn't need to happen until llm-wiki-compiler's embeddings approach is benchmarked first.
- *knowledge-base-server*: more opinionated than llm-wiki-compiler; sidecar value comes from multi-agent shared brain (Claude + Codex + Gemini share KB) that we don't currently need. Re-evaluate if the workflow ever expands to multi-agent.

**Reject:** **`memex`** for adoption.

Reasons: Linux-only (CAP_SYS_ADMIN namespace); fewer features than llm-wiki-compiler (no MCP, no embeddings, no candidate review); lighter ecosystem (1 contributor vs 6). Conceptually the cleanest minimal take ("just files, no RAG") and very on-brand for our filesystem-first preference, but llm-wiki-compiler covers the same minimal core *plus* the missing 3 operations. Keep memex on the radar as a reference implementation for "what minimal Karpathy looks like" but don't adopt.

**Reference-only:** **`emtwiki.endusergeek.com`** — deployed example, not a tool. Demonstrates the pattern is mature enough for high-stakes domains (EMT-Basic certification with NREMT psychomotor + cognitive exam alignment, San Juan College program). Useful as a pedagogical example of Karpathy-pattern wiki at scale (~50+ pages, multi-section curriculum, quick-reference tables linking findings → interventions). The existence of *deployed* examples (not just GitHub-active tools) raises the floor on "is this pattern production-ready" — yes.

### Decision gates — what would flip this recommendation

1. **If `llm-wiki-compiler` overwrites our hand-curated frontmatter** — adoption cost rises sharply. **Test before committing**: `npm install -g llm-wiki-compiler && llmwiki compile --review` against `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/` with `LLMWIKI_PROVIDER=anthropic` (using the existing Claude-Code-configured Anthropic auth). Inspect candidate diff. If the candidate queue tries to overwrite our K-series hand-curated source pages, bail and either (a) configure exclusions, (b) point it at a copy of the wiki, (c) reject and keep status quo.

2. **If LLM-cost during initial compile is prohibitive** — at 373 pages × incremental compile, even Anthropic Haiku adds up. Estimate first: 373 pages × ~1.5K tokens ingest + ~500 tokens compile ≈ 745K tokens × Haiku $0.80/1M input ≈ **~$0.60 first compile**, ~5-10× lower for incremental compiles. Manageable if accurate; verify empirically before committing.

3. **If the MCP server doesn't reliably wrap the wiki tools we need** — the 7 tools (`ingest_source`, `compile_wiki`, `query_wiki`, `search_pages`, `read_page`, `lint_wiki`, `wiki_status`) cover most of what the dev-stack DeepSeek client would query. Verify after install: spin up the MCP server, point a Claude Desktop or Claude Code instance at it, run a smoke-test query against the wiki. If retrieval is poor (e.g. cluster-hub pages don't surface for cluster-level queries), evaluate fallback (custom MCP server wrapping the Python tools).

4. **If we want to keep the librarian *and* the dev stack on Python** — that's a real preference, not just inertia. llm-wiki-compiler being Node introduces a `npm install` + Node runtime that we don't currently have on the workspace. Cost is low but non-zero (Node is widely available; this isn't a deal-breaker). Note: the *server* stack stays Python; this only adds Node to the *workspace* (laptop). Same separation as the Obsidian community plugins (M-task) and Dataview (L-task) — workspace-side tooling can be polyglot.

5. **If a sixth/seventh candidate emerges** — e.g. `iamsashank09/llm-wiki-kit` (mentioned by llm-wiki-compiler README as a lower-level alternative — "raw CRUD against wiki pages") could be a leaner option if the full compile pipeline is too opinionated. Worth a stub-source-page on next pass.

### What this means for the existing ROADMAP

Specific impacts on the ROADMAP sections expanded in the K8 commit (`69bdc57`):

- **"Operational efficiency — toward Karpathy LLM Wiki standard"** subsection: adopting `llm-wiki-compiler` closes 3 of the listed items in one move (cited-unread backlog reduction *partial*; periodic lint as session-start ritual *via `llmwiki watch` + lint*; dashboard maturity *via MCP `wiki_status` tool*). The compile/query loop also closes the prescribed-but-absent compounding-queries pattern.
- **"Memory storage / reading / indexing — wiki growth"** subsection: agentmemory's pipeline becomes the reference implementation for cpr-pattern wiring (the LangGraph `PostgresSaver` checkpointer + DeepSeek summarization-node + pgvector storage trio is now no longer "design from scratch" but "port the agentmemory pipeline shape into Python"). Reduces engineering effort for that ROADMAP item from open-design to port-and-adapt.
- **"Wiki-as-RAG embedding store"** item: llm-wiki-compiler's built-in semantic-search layer (provider-configurable; embeddings via Ollama or OpenAI-compatible local server) directly addresses this item. The decision shifts from "build a separate pgvector index over the wiki" to "use the embeddings llm-wiki-compiler maintains as part of its compile pipeline."
- **Open question: "Which conductor?"** — *no impact*. Conductor decision is orthogonal to wiki-tooling adoption.
- **Open question: "Which LLM brain (locally)?"** — *minor impact*. llm-wiki-compiler's multi-provider config matches the same `OPENAI_BASE_URL` swap pattern as the deepseek-api / localai pages. If we adopt llm-wiki-compiler with `LLMWIKI_PROVIDER=ollama` or LocalAI later, the swap is one env-var.

### Path to commitment

Recommended sequence (stamps on this concept page as decisions land):
1. **Smoke test** llm-wiki-compiler in `--review` mode against a wiki copy, ~30 min. Reads only; produces no-op until approved.
2. If smoke passes: **stamp** this page `maturity: validated` → `core` and update the recommendation row to `[ADOPTED 2026-04-XX]` with the real-world cost numbers measured.
3. **Mirror in ROADMAP**: move "Wiki-tooling decision" from Open questions to Soon, then to Done with the test-result commit SHA.
4. **Steal-from agentmemory**: open a separate concept-page-or-brief for the cpr-pattern Python port plan; coordinate with the K8 LangGraph-checkpointer ROADMAP row.

If smoke fails: this page becomes the **"why we kept hand-rolling"** retraction-of-record, including the specific failure mode that bailed.

## Snippets

### From `sources/atomicmemory-llm-wiki-compiler.md` (covers GitHub + llmwiki.app)

> "Inspired by Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern: instead of re-discovering knowledge at query time, compile it once into a persistent, browsable artifact that compounds over time."

> "RAG: query → search chunks → answer → forget / llmwiki: sources → compile → wiki → query → save → richer wiki → better answers"

> "*The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass.*" — Andrej Karpathy (quoted on llmwiki.app)

### From `sources/wastedcode-memex.md`

> "Just files, no RAG. The wiki is a directory of markdown files. No vector databases, no embeddings, no retrieval pipelines. Claude is already smart enough to grep through files, read what's relevant, and figure out what to update. The simplest architecture that works."

> "Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that." [Vannevar Bush 1945 Memex framing — contrast to the `web-as-graveyard-of-tabs` framing in llm-wiki-compiler.]

### From `sources/willynikes2-knowledge-base-server.md`

> "Hot: Active project context, recent sessions, current decisions / Warm: Accumulated lessons, research, validated workflows / Cold: Raw captures, archived sources, old terminal logs. Why three tiers? Without tiering, a search for 'authentication' returns every raw article you ever clipped alongside your actual auth architecture decision. The tiers ensure agents get signal, not noise."

### From `sources/agentmemory-rohitg00-cpr-impl.md`

> "PostToolUse hook fires → SHA-256 dedup (5min window) → Privacy filter (strip secrets, API keys) → Store raw observation → LLM compress → structured facts + concepts + narrative → Vector embedding (6 providers + local) → Index in BM25 + vector + knowledge graph"

### From `sources/falkordb-graphrag-eval.md`

> "Graph RAG retrieves relevant results for aggregation queries 3x more often (23% vs 8%) and for cross-document reasoning 4x more often (33% vs 8%). [...] For specific document search, Vector RAG is better (54% vs 35%). Graph RAG is not a replacement for vector search. It is a computation layer on top of it." [AIMultiple benchmark, 2026-03-20]
