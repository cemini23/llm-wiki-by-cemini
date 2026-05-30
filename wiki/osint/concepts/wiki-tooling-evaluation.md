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
  - sources/wave-5-1-link-eval-stacks.md
  - sources/wave-5-1-link-eval-more.md
  - sources/wave-5-1-link-eval-even-more.md
  - concepts/librarian-server-architecture.md
  - sources/gemini-dr-link-eval-2026-04-28.md
  - sources/omc-talent-container-paper.md
  - concepts/ai-organisation-design.md
  - sources/vibe-trading-hkuds.md
  - sources/langextract-google.md
  - sources/sentrux-ast-sensor.md
  - sources/claude-code-harness-chachamaru.md
  - sources/kepano-obsidian-skills.md
  - sources/obsidian-second-brain-eugeniughelbur.md
  - sources/playwright-mcp-microsoft.md
  - sources/bare-bones-memory-southpolesteve.md
  - sources/gemini-dr-wave3-link-eval-2026-04-28.md
  - sources/black-scholes-iv-explicit-schadner-2026.md
  - sources/4-5-links-2.md
  - sources/agent-browser-vercel-labs.md
  - concepts/high-signal-paper-patterns.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave4b-osint-2026-04-29.md
  - sources/mercurialsolo-claudectl.md
  - sources/upstash-context7.md
  - sources/last30days-skill-mvanhorn.md
  - sources/tradesdontlie-tradingview-mcp.md
  - sources/7onez-cti-expert.md
  - sources/spaceshift-sateais-api.md
  - concepts/mcp-tool-marketplace.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - sources/multi-wiki-tool-eval-v4-k84-2026-05-30.md
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/alash3al-stash.md
  - sources/shiyu-coder-kronos.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - sources/agriciDaniel-claude-obsidian.md
  - sources/piebald-claude-code-system-prompts.md
  - sources/bytemover-agent-native-memory.md
maturity: validated
hub: true
created: 2026-04-28
updated: 2026-04-30
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
- @concepts/librarian-server-architecture.md — child decision document expanding the "Hosting topology" sub-decision (Option C — dedicated Hetzner CPX21 librarian server) into a full architectural plan with migration phases, sizing math, and 24/7 operational SLA targets. **Where this WTE page resolved "which tool"; that page resolves "where it runs."**
- @sources/bytemover-agent-native-memory.md — K13 Promotion #3; ByteRover is the canonical "filesystem-first" architecture in WTE's filesystem-vs-database taxonomy; validates the filesystem-first approach for qualitative knowledge management against the DB-heavy alternatives evaluated here

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

### Provider configuration & smoke-test recipe

[DECISION 2026-04-28]: smoke-test path = **Claude Code zero-config Anthropic auth**. Ollama-for-embeddings deferred pending external storage (user noted ~25 GB free on the laptop — see ROADMAP item E "Storage compaction"; embeddings models + Ollama runtime are practical but not comfortable on current free disk). Index-based query routing is llm-wiki-compiler's default per its own README "Limitations" section, so the smoke test runs cleanly without semantic embeddings; embeddings layer is additive when the hardware lands.

#### Path A — Claude Code zero-config `[SMOKE-TEST PARTIAL-PASS 2026-04-28; ZERO-CONFIG CLAIM RETRACTED]`

```bash
# Original recipe — DOES NOT WORK as-is in default Claude Code installations:
npm install -g llm-wiki-compiler
cd "/Users/claudiobarone/Desktop/OSINT WORKSPACE"
llmwiki compile --review
```

**Smoke-test result (2026-04-28)** — sandbox at `briefs/2026-04-28_wte-1-smoke-sandbox/`. Five of six steps passed:

1. ✅ Install via `npx -y llm-wiki-compiler --version` works without sudo (Node v24.13.0 on macOS; npm 11.6.2; `/usr/local` not user-writable so global install would need sudo, but npx-driven invocation avoids that)
2. ✅ Version resolved: **v0.5.1** (newer than the v0.2.0 our `sources/atomicmemory-llm-wiki-compiler.md` page documents — project shipped 3 minor versions since our 2026-04-28 ingest)
3. ✅ CLI surface (`llmwiki --help`) matches our wiki source page: `ingest / compile / review / query / watch / lint / schema / serve` subcommands present
4. ✅ Schema introspection (`llmwiki schema show`) — default schema has 4 page kinds (`concept` / `entity` / `comparison` / `overview`) — different vocabulary from our (`source` / `entity` / `concept` / `brief`) but compile pipeline doesn't enforce schema as a hard gate
5. ✅ Ingest works: `llmwiki ingest <local-file>` copies the file into `sources/` with a llmwiki-specific frontmatter wrapper (non-destructive; preserves original content)
6. ❌ **Compile fails on auth wall** — `Error: Anthropic credentials are required for the "anthropic" provider`

**Why the auth wall fired** — the README's "Path A zero-config" promise depends on a precondition that is NOT met by default in Claude Code installations:

- `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` env-var **names** are present in Claude Code's subprocess shell env, but their **values are empty strings** (length 0). The pre-flight `env | grep ANTHROPIC` showed the variable names; only `echo -n $VAR | wc -c` revealed the empty values.
- `~/.claude/settings.json` has only `sshConfigs` and `enabledPlugins` keys — **no `env` block**. The README's secondary fallback (`reads ~/.claude/settings.json env block`) only works if the user has manually added one with their Anthropic API key.
- `CLAUDE_CODE_OAUTH_TOKEN` is present (108 chars) but llm-wiki-compiler does not accept OAuth tokens — only Anthropic API keys (`sk-ant-...`).

**This is a real finding, not a tooling bug.** The "zero-config" framing in the README assumes the user has previously configured an Anthropic API key in their Claude Code `settings.json` env block (which some installations do; ours doesn't). For our setup, adoption requires explicit API-key configuration via shell env, local `.env` file, or manually-added `env` block in `settings.json`.

**Decision (2026-04-28)**: Compile pass deferred until the librarian server is provisioned (Phase 1 of @concepts/librarian-server-architecture.md). At Phase 3 on the librarian server, the existing **DeepSeek API key from `/opt/cemini/.env` is the natural auth source** (already managed as a server-stack credential; no new payment / new account / laptop-side env-var-fiddling). Smoke test on laptop is partial-pass-sufficient: tool is real, installs cleanly, CLI surface matches expectations, ingest works, compile auth-config can be handled at server provisioning time.

**Updated recipe — for the librarian server (Phase 3)**, NOT for the laptop:

```bash
# On the librarian server (Hetzner CPX21), once provisioned:
export LLMWIKI_PROVIDER=openai
export LLMWIKI_MODEL=deepseek-v4-flash   # or deepseek-v4-pro; legacy deepseek-chat / deepseek-reasoner aliases are deprecated
export OPENAI_API_KEY=$DEEPSEEK_API_KEY   # already in /opt/cemini/.env on production server; copy to librarian server env at provisioning
export OPENAI_BASE_URL=https://api.deepseek.com
cd /opt/librarian
llmwiki compile --review
```

The DeepSeek-no-embeddings caveat from Path B below still applies — semantic-embedding layer comes from the librarian server's own Ollama + nomic-embed-text instance per @concepts/librarian-server-architecture.md.

#### Path B — DeepSeek API (production deployment if smoke passes)

DeepSeek's hosted Chat Completions API is OpenAI-compatible (per `entities/infrastructure/deepseek-api.md`), so `llm-wiki-compiler`'s OpenAI provider points at it directly:

```bash
export LLMWIKI_PROVIDER=openai
export LLMWIKI_MODEL=deepseek-v4-flash   # or deepseek-v4-pro; legacy deepseek-chat / deepseek-reasoner aliases are deprecated
export OPENAI_API_KEY=$DEEPSEEK_API_KEY   # the key already in /opt/cemini/.env
export OPENAI_BASE_URL=https://api.deepseek.com
```

[VERIFIED 2026-05-04] DeepSeek's API does **not** ship an embeddings endpoint — re-confirmed against `api-docs.deepseek.com` 2026-05-04: only `/chat/completions` is exposed. A DeepSeek GitHub issue (`deepseek-ai/DeepSeek-R1#802`, Feb 2026) explicitly enumerates DeepSeek as "Embedding API ❌" in its current state and proposes adding one. So Path B is **chat-only**: the embeddings layer either uses index-based fallback (default; acceptable) or routes to a separate provider via `OPENAI_EMBEDDINGS_BASE_URL`.

#### Path C — Ollama embeddings sidecar `[SUPERSEDED 2026-04-28]`

`[SUPERSEDED 2026-04-28 — Path C now lives on the dedicated librarian server, not on the laptop. External drive purchase cancelled. See @concepts/librarian-server-architecture.md for the committed plan.]`

Original framing (retained for lineage): the laptop-side Ollama embeddings sidecar was the 2026-04-28 morning plan; the user-stated 24/7 crypto-market reliability requirement that surfaced 2026-04-28 afternoon (*"of utmost importance that the deployed cemini brain can query the library at any time as crypto markets are 24/7"*) made laptop-as-host the wrong physical location. Embeddings will live on a dedicated Hetzner CPX21 librarian server (Ashburn, $13.99/mo) instead — see @concepts/librarian-server-architecture.md for topology, sizing, migration phases, and operational SLA targets.

The retracted laptop-side recipe (kept here so future readers don't re-derive what was tried):

```bash
# RETRACTED 2026-04-28 — superseded by server-side deployment
brew install ollama
ollama pull nomic-embed-text   # ~270 MB; free; runs on-device
export LLMWIKI_EMBEDDING_MODEL=nomic-embed-text
export OPENAI_EMBEDDINGS_BASE_URL=http://localhost:11434/v1
```

### Hosting topology — laptop vs sync-to-server vs dedicated-server

`[DECISION 2026-04-28]: Option C — dedicated Hetzner CPX21 librarian server (Ashburn, $13.99/mo) committed.` Full architectural plan + migration phases at @concepts/librarian-server-architecture.md.

Trigger: user-stated 24/7 reliability requirement — *"it is going to be of utmost importance that the deployed cemini brain can query the library at any time as crypto markets are 24/7 and who knows when its going to need info."* This reframes the librarian from a research/curation tool (laptop-only model that worked through K1-K8 + WTE) to an **operational dependency** for the deployed trading stack. Reliability bar moves from "convenient when working" to "available whenever the market is" — and crypto markets are always.

| Option | $/mo | Verdict | Rejection reason |
|---|---|---|---|
| **A** Laptop-as-MCP-host (laptop runs llm-wiki-compiler `serve`, brain queries laptop over network) | $0 | ❌ Rejected | Laptop sleeps when lid closes, drops home wifi, IP rotates on residential ISP. Fails the 24/7 SLA target. |
| **B** Sync to existing production Hetzner server (laptop curates, prod hosts) | $0 | ❌ Rejected | Production server is already at 7 GB RAM (per K8 server-probe `free -g` 2026-04-28). Adding Node + Ollama + nomic-embed-text + llm-wiki-compiler index = ~700 MB extra resident. Couples librarian outage to trading-stack outage. SPOF risk. |
| **C** Dedicated Hetzner CPX21 librarian server (Ashburn) ✅ committed | $13.99 | **✅ ADOPTED 2026-04-28** | Server-class always-on; intra-Hetzner low-latency to production brain; doesn't load the constrained production box; clean architectural decoupling. See sizing/topology/migration in @concepts/librarian-server-architecture.md |
| **D** Self-host (Pi 5 / Mac mini / NUC at home) | $80-599 one-time | ❌ Rejected | Home internet reliability dependence; port forwarding / Tailscale tunnel; home-network exposure surface; the laptop-but-bigger problem |
| Migrate wiki to existing Hetzner production server | $0 | ❌ Rejected | Same RAM constraint as Option B; **breaks librarian doctrine** (per `retracted_deepseek_ollama.md` memory: *"the wiki lives on this laptop precisely because the server cannot carry the full knowledge-and-LLM loop locally"*) |

**Sizing**: CPX21 (3 vCPU / 4 GB RAM / 80 GB NVMe / 2 TB traffic / $13.99) sufficient for embeddings-only spec — see @concepts/librarian-server-architecture.md "Sizing the librarian server" for the 4 GB RAM math (~2-2.6 GB headroom after services). CPX31 ($24.99) tier exists as snapshot-based upgrade path if usage signals chat-model-on-librarian becomes needed.

**Vendor**: Hetzner-same-as-production wins on intra-DC latency + unified ops + competitive pricing. Cross-provider survey 2026-04-28 (OVHcloud / Vultr / Linode / DigitalOcean / Contabo / Oracle Free Tier) captured in @concepts/librarian-server-architecture.md.

**External drive purchase cancelled** as a result of this decision — dedicated server's 80 GB NVMe replaces the laptop-external-drive-for-Ollama need entirely. ROADMAP item E (storage compaction) re-enters scope on its own timeline (independent from librarian decision).

### Decision gates — what would flip this recommendation

1. **If `llm-wiki-compiler` overwrites our hand-curated frontmatter** — adoption cost rises sharply. **Test before committing**: `npm install -g llm-wiki-compiler && llmwiki compile --review` against `/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/` with `LLMWIKI_PROVIDER=anthropic` (using the existing Claude-Code-configured Anthropic auth). Inspect candidate diff. If the candidate queue tries to overwrite our K-series hand-curated source pages, bail and either (a) configure exclusions, (b) point it at a copy of the wiki, (c) reject and keep status quo.

2. **If LLM-cost during initial compile is prohibitive** — at 373 pages × incremental compile, even Anthropic Haiku adds up. Estimate first: 373 pages × ~1.5K tokens ingest + ~500 tokens compile ≈ 745K tokens × Haiku $0.80/1M input ≈ **~$0.60 first compile**, ~5-10× lower for incremental compiles. Manageable if accurate; verify empirically before committing.

3. **If the MCP server doesn't reliably wrap the wiki tools we need** — the 7 tools (`ingest_source`, `compile_wiki`, `query_wiki`, `search_pages`, `read_page`, `lint_wiki`, `wiki_status`) cover most of what the dev-stack DeepSeek client would query. Verify after install: spin up the MCP server, point a Claude Desktop or Claude Code instance at it, run a smoke-test query against the wiki. If retrieval is poor (e.g. cluster-hub pages don't surface for cluster-level queries), evaluate fallback (custom MCP server wrapping the Python tools).

4. **If we want to keep the librarian *and* the dev stack on Python** — that's a real preference, not just inertia. llm-wiki-compiler being Node introduces a `npm install` + Node runtime that we don't currently have on the workspace. Cost is low but non-zero (Node is widely available; this isn't a deal-breaker). Note: the *server* stack stays Python; this only adds Node to the *workspace* (laptop). Same separation as the Obsidian community plugins (M-task) and Dataview (L-task) — workspace-side tooling can be polyglot.

5. **If a sixth/seventh candidate emerges** — e.g. `iamsashank09/llm-wiki-kit` (mentioned by llm-wiki-compiler README as a lower-level alternative — "raw CRUD against wiki pages") could be a leaner option if the full compile pipeline is too opinionated. Worth a stub-source-page on next pass.

### K28 + K30 candidate updates (post-deployment landscape)

The candidate list expanded after the K28 SwarmVault audit and K30 ingest:

| Candidate | Status (as of 2026-05-05) | Notes |
|-----------|---------------------------|-------|
| **kb-server** | DEPLOYED on librarian (canonical serving layer) | 397 docs indexed, FTS-style retrieval. Stable. |
| **llm-wiki-compiler** | DEPLOYMENT-BLOCKED at v0.4.0 | Hardcoded `CONCEPTS_DIR = "wiki/concepts"` flat-layout assumption breaks against our nested structure. Retained on disk; not running as service. |
| **SwarmVault** (K28 candidate) | **NO-GO 2026-05-04** | Same flat-layout disease as llm-wiki-compiler. Audit at `@entities/tools/swarmvault.md`. |
| **PageIndex** (K30 candidate, `@entities/tools/pageindex.md`) | **NO-GO 2026-05-05** | "Vectorless reasoning-based RAG" (MIT, VectifyAI/PageIndex). Phase-0 audit verdict: single-file API only (600+ index instances for the wiki); agentic reasoning at query time (~$0.001-0.005/query vs kb-server's $0); cross-link graph + frontmatter metadata both lost. Right tool for long-form professional documents, wrong tool for flat wiki retrieval. Stays shelved unless Cemini begins indexing long-form documents as a separate retrieval tier. |
| **Deep GraphRAG** (K30 reference, `@sources/deep-graphrag-2601-11144.md`) | **Deferred — re-evaluate if wiki develops graph-density signal** | 3-stage hierarchical retrieval (inter-community → community-refine → entity-fine) + DW-GRPO trained Knowledge Integration Module. Architecturally distinct from kb-server/PageIndex (graph-community-aware vs flat). Now that PageIndex NO-GO is recorded, Deep GraphRAG is the only remaining librarian-tooling alternative on file — but the alternative isn't urgent: kb-server works. **Upgrade to candidate if (a) Cemini's wiki develops cross-link graph density that flat retrieval clearly fails on, OR (b) the user decides graph-aware retrieval is operationally worth the complexity**. Until then, holds reference-only status. |

The SwarmVault NO-GO and PageIndex audit (still pending) together set the gate for whether a third Karpathy-pattern alternative needs to be evaluated. Deep GraphRAG is the most architecturally interesting candidate-in-waiting because it doesn't share the flat-layout assumption with the other two — its hierarchy IS the design. But it adds graph-community detection complexity that's not justified unless flat-RAG approaches definitively underperform. Re-evaluate when one of those gates triggers.

### What this means for the existing ROADMAP

Specific impacts on the ROADMAP sections expanded in the K8 commit (`69bdc57`):

- **"Operational efficiency — toward Karpathy LLM Wiki standard"** subsection: adopting `llm-wiki-compiler` closes 3 of the listed items in one move (cited-unread backlog reduction *partial*; periodic lint as session-start ritual *via `llmwiki watch` + lint*; dashboard maturity *via MCP `wiki_status` tool*). The compile/query loop also closes the prescribed-but-absent compounding-queries pattern.
- **"Memory storage / reading / indexing — wiki growth"** subsection: agentmemory's pipeline becomes the reference implementation for cpr-pattern wiring (the LangGraph `PostgresSaver` checkpointer + DeepSeek summarization-node + pgvector storage trio is now no longer "design from scratch" but "port the agentmemory pipeline shape into Python"). Reduces engineering effort for that ROADMAP item from open-design to port-and-adapt. **And it lands on the librarian server, not on the constrained production trading-stack box** — see @concepts/librarian-server-architecture.md "Future expansion" section.
- **"Wiki-as-RAG embedding store"** item: llm-wiki-compiler's built-in semantic-search layer (provider-configurable; embeddings via Ollama or OpenAI-compatible local server) directly addresses this item. The decision shifts from "build a separate pgvector index over the wiki" to "use the embeddings llm-wiki-compiler maintains as part of its compile pipeline" — running on the librarian server's Ollama instance.
- **New ROADMAP rows** (added 2026-04-28 with this page + @concepts/librarian-server-architecture.md): librarian server provisioning + migration phases (Phase 1-6 per the architecture page).
- **Closed ROADMAP open question**: "Workspace external-storage purchase" — superseded by the dedicated librarian server (server's 80 GB NVMe replaces the external-drive role for librarian purposes). External drive remains an *optional independent track* if user wants headroom for ROADMAP item E storage compaction (research corpus + market dataset migration), but it's no longer gating anything.
- **Open question: "Which conductor?"** — *no impact*. Conductor decision is orthogonal to wiki-tooling adoption.
- **Open question: "Which LLM brain (locally)?"** — *minor impact*. llm-wiki-compiler's multi-provider config matches the same `OPENAI_BASE_URL` swap pattern as the deepseek-api / localai pages. If we adopt llm-wiki-compiler with `LLMWIKI_PROVIDER=ollama` or LocalAI later, the swap is one env-var. The librarian server is the natural experimentation venue for this without touching production.
- **Open question: "Hetzner host upgrade"** — *partially addressed*. The dedicated CPX21 librarian server is a separate dedicated box, not an in-place upgrade of production. Production-server upgrade question still open if the trading stack itself needs more RAM (per K8 finding); librarian decision is independent.

### Path to commitment

Recommended sequence (stamps on this concept page as decisions land):
1. **Smoke test** llm-wiki-compiler in `--review` mode using **Path A (Claude Code zero-config)** on the laptop, ~30 min. Reads only; produces no-op until approved. `[DECISION 2026-04-28]: Path A confirmed; Path B (DeepSeek) reserved for production deployment on the librarian server if smoke passes; Path C (laptop-Ollama embeddings) superseded — embeddings will live on the dedicated librarian server.`
2. If smoke passes: **stamp** this page `maturity: validated` → `core` and update the recommendation row to `[ADOPTED 2026-04-XX]` with the real-world cost numbers measured.
3. **Hosting decision**: `[DECISION 2026-04-28]: Option C — dedicated Hetzner CPX21 librarian server.` Full migration plan at @concepts/librarian-server-architecture.md (Phase 0 = WTE-1 smoke test on laptop; Phase 1 = provision CPX21 in Ashburn; Phase 2 = initial wiki sync; Phase 3 = server-side compile + MCP serve; Phase 4 = wire production brain; Phase 5 = sync cron; Phase 6 = monitoring).
4. **Mirror in ROADMAP**: WTE-1 row already queued; new migration-phase rows added pending smoke-test result.
5. **Steal-from agentmemory**: open a separate concept-page-or-brief for the cpr-pattern Python port plan; coordinate with the K8 LangGraph-checkpointer ROADMAP row. **Most natural deployment target for cpr-pattern is the librarian server**, not the constrained production trading-stack box.

If smoke fails: this page becomes the **"why we kept hand-rolling"** retraction-of-record, including the specific failure mode that bailed; @concepts/librarian-server-architecture.md is paused at Phase 0 (no provisioning) until alternatives are evaluated.

### `[OUTCOME 2026-04-29]` — Wave 1 librarian-tooling decision REVISED

**llm-wiki-compiler v0.4.0 deployment-blocked**: smoke-tested against the live librarian server's synced wiki, the v0.4.0 query path-resolver hardcodes `CONCEPTS_DIR = "wiki/concepts"` (single flat directory) and cannot find pages in our nested `concepts/` + `entities/` + `sources/` layout. The LLM (DeepSeek API) correctly identifies the right page via reasoning over our `wiki/index.md`, but the post-LLM slug-resolver mangles paths (e.g., returns `conceptslibrarian-server-architecture` from `concepts/librarian-server-architecture.md` after stripping `/`). End-to-end query path is broken for our wiki layout. Diagnosed by inspecting `/usr/lib/node_modules/llm-wiki-compiler/dist/cli.js`. Stack confirmed working at every layer except this one: DeepSeek inference 5.7s, Ollama daemon, llmwiki ingest, llmwiki lint all functional.

**Three options evaluated**:
- **A — Flatten our wiki** to `wiki/concepts/` only: rejects librarian doctrine + 60+ existing inline `@path/` references would break; **rejected**
- **B — Symlink farm** at `/opt/cemini-wiki/wiki/concepts/` symlinking all nested .md files flat: technical debt forever, fragile to upstream llmwiki changes, basename-collision risk; **rejected**
- **C — Replace serving layer** with a different MCP server that natively walks nested directories: longest path but cleanest answer; **adopted**

`[ADOPTED 2026-04-29]: Option C — replace llmwiki query/serve with @sources/willynikes2-knowledge-base-server.md (kb-server)` — installed at `cemini-librarian:/opt/kb-server/`, systemd-managed (`kb-server.service`), Node 22 + better-sqlite3 + Xenova embeddings + Obsidian-vault-bidirectional-sync. **Critical empirical proof**: ingested all 395 wiki pages from `/opt/cemini-wiki/wiki/` (nested layout) in 0.7 seconds. FTS5 BM25 search returns the right pages including from deeply-nested paths like `entities/tickers/nvda.md` and `sources/omc-talent-container-paper.md`. Three test queries verified end-to-end: OMC abstraction → top hit `omc-talent-container-paper`; "librarian server architecture" → 10 results, top hit correct page; "NVDA" → top hit `nvda` ticker page.

**llm-wiki-compiler retained on disk** at `/usr/lib/node_modules/llm-wiki-compiler/` for potential future compile-mode use (auto-classify, candidate review, watch-and-recompile) if/when our wiki layout is restructured to be more compatible. Not running as a service; not consuming RAM.

**Read-only safety**: kb-server ships 16 MCP tools, ~10 of which can write/rewrite vault content (`kb_classify`, `kb_promote`, `kb_synthesize`, `kb_write`, `kb_capture_*`). For our serving needs we only require the read subset (`kb_search`, `kb_search_smart`, `kb_context`, `kb_read`, `kb_list`). Pending: configure tool-allowlist filter at the MCP boundary so the brain can only call read tools, never write. Documented as a Phase 3 decision in @concepts/librarian-server-architecture.md.

**Network exposure**: kb-server listens on `0.0.0.0:3838`; Hetzner Cloud Firewall scopes port 3838 inbound to `10.0.0.0/16` only. The brain on cemini-prod (once attached to the same private network) reaches it via `cemini-librarian-private:3838`. No public exposure.

**Sync cadence**: manual rsync + `kb ingest` after substantive wiki edits. Phase 5 of LSA migration plan converts this to hourly cron (or file-watch on the laptop) — pending.

The Wave 1 register is otherwise unchanged: `agentmemory` stays Steal-from-as-pattern, `FalkorDB`+`memex`+`emtwiki` decisions preserved.

## Wave 2 — Gemini Deep Research findings (2026-04-28)

After Wave 1 (this page above) decided **adopt llm-wiki-compiler**, the user authored a Gemini Deep Research brief at `briefs/2026-04-28_gemini-deep-research-link-evaluation-prompt.md` (gitignored) and ran 24 URLs through Gemini 2.5 Deep Research mode. Result: `Evaluating Code for Trading and Wiki 4_28.docx` → ingested 2026-04-28 as @sources/gemini-dr-link-eval-2026-04-28.md.

**Wave 2 doesn't change the Wave 1 librarian decision.** None of the 24 URLs are direct alternatives to llm-wiki-compiler. Wave 2 instead expanded the evaluation surface to: agent harnesses, trading-stack libraries, Obsidian + Claude Code skills, browser automation, license-poison-pill family expansions, ingest-layer extractors. The findings reshape *what else* gets adopted/stolen-from/rejected without disturbing the Wave 1 spine.

### Wave 2 register summary (decisions added 2026-04-28)

**Adopt-for-Cemini (production stack — 2 candidates, both new addition decisions):**
- `[ADOPT-PENDING-VERIFICATION 2026-04-28]` @sources/vibe-trading-hkuds.md — MIT, Python+FastAPI+MCP, 29 expert agent swarms + 7 backtest engines + CCXT. Drops onto `agents/orchestrator.py` via `@mcp.tool` decorators. **Pre-deploy gates**: strip React frontend; swap yfinance for Polygon/Alpaca; verify shadow-account state persistence; aggressive Docker memory caps.
- `[ADOPT-PENDING-VERIFICATION 2026-04-28]` @sources/langextract-google.md — Apache-2.0, Python, source-grounded JSON-schema extraction. Replaces brittle regex/LangChain extractors in EDGAR + GDELT ingest layers. **Block ship until DeepSeek strict-schema JSON-enforcement compatibility is verified** (test protocol documented on the source page).

**Adopt-for-Workflow (laptop — 6 candidates, all new):**
- `[ADOPT 2026-04-28]` @sources/kepano-obsidian-skills.md — eliminates Markdown syntax hallucinations in rapid wiki curation; `obsidian-bases` sub-skill provides flawless YAML templates
- `[ADOPT 2026-04-28]` @sources/obsidian-second-brain-eugeniughelbur.md — 31 commands + 4 cron agents; runs on laptop only (NEVER on librarian server — autonomous-rewriting collides with llm-wiki-compiler's static-compiler philosophy); requires git-tracked vault before every cron run; Perplexity Sonar Pro bridge for cited research
- `[ADOPT 2026-04-28]` @sources/claude-code-harness-chachamaru.md — sub-10ms hooks enforcing `Plan→Work→Review→Ship`; secret-leak prevention; main-branch force-push prevention. Pin Claude Code version (heuristically tuned for `claude-opus-4-7`)
- `[ADOPT 2026-04-28]` @sources/sentrux-ast-sensor.md — Rust + tree-sitter AST quality governor with deterministic 0–10000 score; MCP-server-mode for live agent feedback; CI/CD-mode for hard quality gates
- `[ADOPT 2026-04-28]` @sources/playwright-mcp-microsoft.md — DOM accessibility-tree exposure for LLMs (deterministic, not pixel-screenshot-based); **Defer for Cemini production** until 14-day soak passes; Microsoft official, Apache-2.0
- `[ADOPT 2026-04-28]` @sources/bare-bones-memory-southpolesteve.md — `AGENTS.md` + `active-projects.md` + `session-logs/` directory protocol; pure methodology, zero runtime, IP-taint risk = 0 despite license-not-found

**Steal-from (3 candidates):**
- `mercury-agent` (MIT, TS) — extract SQLite FTS5 schemas + JSONL episodic-log compaction algorithms. Don't deploy. Patterns applicable to `wiki_lint.py` enhancements
- `AutoHedge` (MIT, Python+Swarms) — extract Director/Quant/Risk/Execution prompt structures, port to LangGraph nodes. Don't import the Swarms framework (less deterministic than LangGraph; Solana/Jupiter focus is misaligned with Cemini's Alpaca/OANDA/Coinbase)
- `mattpocock/skills` (MIT) — extract `/grill-me` + `/caveman` + `/tdd` patterns. Don't load whole library (context-saturation risk)

**Reference-only (1):** `agency-agents` — 147 personas; study for prompt-engineering insights. Validated 2026-04-28 by OMC paper which uses agency-agents as Type-2 prompt source

**Reject — license poison-pills (3):**
- `everywall/ladder` (GPL-3.0) — confirms IP-sale-readiness GPL-3.0 reject extension
- `Fincept-Corporation/FinceptTerminal` (AGPL-3.0 + Commercial dual) — confirms AGPL-3.0 transitive-taint reject
- `mksglu/context-mode` (ELv2) — adds Elastic License 2.0 to the source-available-not-OSI reject family alongside SSPL/PolyForm-Noncommercial

**Reject — domain mismatch / closed-source (5):** `hyperframes` (video rendering), `agentic-inbox` (Cloudflare lock-in), `toprank` (SEO/Ads), `claude-ads` (PPC audit), `sci-bot.ru` (proprietary closed-source, no API, Sci-Hub-affiliated)

**Defer — pending verification (1):** `camofox-browser` (MIT) — RAM profiling required for the C++-patched Firefox fork before deploying to Hetzner

**Unavailable (2):** `plurai.ai/papers` (mis-routes to sci-bot.ru), `Google-Finance-Api` (404)

### Spot-check protocol — established and validated this wave

Every Adopt + Steal-from URL went through Exa `crawling_exa` against the GitHub repo root in a single batched call (10 URLs ≈ ~1 Exa unit cost). All 10 verified — claimed licenses match, repos exist, star counts within 0–28% drift (mercury-agent the worst at ~28% overstatement, immaterial to a Steal-from recommendation). The protocol is now **codified at @sources/gemini-dr-link-eval-2026-04-28.md** as a reusable 9-step pattern for future Gemini DR waves:

1. Save report to `research to be indexed/`
2. Read fully (chunked if >25k tokens)
3. Build upstream brief if absent
4. Batch-crawl every Adopt + Steal-from URL via `crawling_exa` (one call)
5. Compare claimed license + stars + last-push against Exa metadata; flag drifts >25% on stars or license mismatch
6. Promote ONLY spot-check-verified Adopt URLs to dedicated `wiki/sources/<slug>.md`
7. Capture Reject + Reference-only + Steal-from + Defer URLs in canonical Gemini DR report's table only — no dedicated stub pages
8. Update the upstream concept page (here: WTE) with a "Wave N — Gemini DR" section
9. Lint, two-commit, push

### Wave 2's effects on this page's recommendations

- Wave 1 recommendation register (llm-wiki-compiler adopted, agentmemory steal-from-as-pattern, FalkorDB+kb-server defer, memex reject, emtwiki reference-only) — **unchanged**.
- Wave 2 adds 8 new Adopt source pages and 3 Steal-from references that don't compete with Wave 1.
- License-poison-pill family on @concepts/ip-sale-readiness.md gains 3 confirmations (GPL-3.0, AGPL-3.0, ELv2) from Wave 2.
- The OMC paper (sibling ingest @sources/omc-talent-container-paper.md) validates Wave 2's Reference-only classification of `agency-agents` — OMC explicitly uses agency-agents as Type-2 prompt source, not as deployable artefact, exactly matching the wiki's "study, don't install" recommendation.
- @concepts/ai-organisation-design.md (sibling concept page from OMC ingest) introduces a third abstraction layer (organisation-level) above multi-agent-coordination — orthogonal to this WTE page's library-tooling decision but worth cross-referencing for any future Cemini orchestrator-replacement question.

## Wave 3 — Gemini Deep Research findings (2026-04-28; ingested 2026-04-29)

Wave 3 docx (`Evaluating Code for Trading & Wiki Stacks.docx`) was first checked mid-session for Option C relevance — the conclusion was that **none of its 13 URLs solved the nested-wiki MCP serving problem**, validating the kb-server adoption decision. Wave 3 then ingested as its own pass per the 9-step protocol from `@sources/gemini-dr-link-eval-2026-04-28.md`.

### Wave 3 register summary (decisions added 2026-04-29)

**Adopt-Cemini-Wiki-Workflow (1)** — first triple-Adopt across all three waves:
- `[ADOPT 2026-04-29]` @sources/black-scholes-iv-explicit-schadner-2026.md — **Wave 3's headline finding**. Closed-form Black-Scholes IV explicit formula (CC BY 4.0, U. Liechtenstein, 27 Apr 2026 paper). Replaces `scipy.optimize.brentq` iterative solving with a single inverse-Gaussian quantile evaluation; claims 3.4× speedup at machine precision. Block production deploy until empirical reproduction on Cemini's Polars + Polygon data confirms the speedup claim.

**Adopt-Workflow with HALT → REJECT (1)** `[RESOLVED 2026-04-29 — LICENSE-FILE INSPECTED]`:
- `[REJECT 2026-04-29]` Gitlawb/openclaude — manual LICENSE-file inspection via Exa `crawling_exa` against the raw LICENSE URL revealed **self-disclosed unauthorized redistribution of Anthropic proprietary code**. LICENSE file states verbatim: *"The underlying derived code remains subject to Anthropic's copyright. This project does not have Anthropic's authorization to distribute their proprietary source."* The MIT-modifications-only framing is a paper veneer over a copyright-infringement disclosure. Reject for laptop, librarian, AND production. Do not extract patterns. **New license poison-pill pattern**: vendor-IP-redistribution-without-authorization — distinct from copyleft (GPL/AGPL/SSPL/etc.) which are legitimate-but-restrictive licenses; this is a project explicitly disclosing its own copyright-infringement exposure.

**Steal-from (5)**:
- `gepa-ai/gepa` (MIT, 3836 ★) — `dspy.GEPA` reflective prompt-mutation; run laptop-only against design-time prompts, hardcode results into `agents/orchestrator.py`
- `czl9707/build-your-own-openclaw` (MIT, 1284 ★) — extract Phase-3 multi-agent routing + Phase-4 concurrency patterns to LangGraph; skip LiteLLM dependency
- `Mathieu2301/TradingView-API` (ISC, 3214 ★) — reverse-engineer JS WebSocket protocol, rewrite as Python `websockets`/`httpx`. Caveat: TOS-violation territory
- `matrixorigin/Memoria` (Apache-2.0, 206 ★) — extract `branch_id`/`parent_commit` schema for PostgreSQL; skip MatrixOne dependency
- `stefan-jansen/machine-learning-for-trading` (MIT per file inspection, 17061 ★, **last push 2024-08-18**) — strip-mine `04_alpha_factor_research` and `24_alpha_factor_library`; transcribe pandas-1.0 → Polars LazyFrames. Severe framework-obsolescence flag

**Reference-only (3)**: `hidemyemail-generator` (MIT, niche), `Mesa filesystem` (cloud SaaS, branched-FS architectural pattern), `warpdotdev/warp` (AGPL-3.0 — laptop-only, server-banned)

**Reject (1)**: `subramanya1997/markdownfs` (license unverified Rust in-memory VFS — auto-reject + zero utility for our problem)

**Unavailable (2)**: google/skills, molab.marimo.io

### Spot-check verdict (Exa `crawling_exa` 2026-04-29)

8 URLs batch-crawled. **Two material findings beyond simple drift**:
- `Gitlawb/openclaude` — license = `Other (NOASSERTION)` confirms Gemini's halt-flag; adoption blocked until manual LICENSE-file inspection
- `stefan-jansen/machine-learning-for-trading` — last push 2024-08-18, ~20 months stale; Steal-from-with-staleness-flag is correct

The 9-step protocol caught both correctly. Worth noting that Wave 3's lower yield (1 clean Adopt vs Wave 2's 2) tracks with the lower URL count — the protocol stays sound, but the source pool's signal density isn't constant.

### Wave 3's effects on this page's recommendations

- Wave 1 + Wave 2 register (llm-wiki-compiler decision; 8 Wave-2 Adopts) — **unchanged**.
- Wave 3 contributes 1 new dedicated source page (`@sources/black-scholes-iv-explicit-schadner-2026.md`) targeting the Cemini quant pipeline; the librarian server is unaffected by this finding.
- License poison-pill family gets one new Exa confirmation (warp = AGPL-3.0 ✅) and one new HALT pattern (`NOASSERTION` license-detection result → halt until LICENSE-file is manually inspected).
- The Memoria-pattern Steal-from (branch_id/parent_commit columns in PostgreSQL) is the highest-leverage Wave 3 pattern for the Cemini stack — adds Git-style memory branching to the LangGraph orchestrator's existing state-tracking with no new database dependency.

## Wave 5 — Gemini Deep Research findings (2026-04-30; ingested 2026-04-30)

Wave 5 was a **dual docx pair** following the Wave 4 pattern: Wave 5A (`Codebase Evaluation for Trading & Wiki 4_30.docx`, 6 URLs, Cemini-stack focus) + Wave 5B (`another Evaluating Code for Trading & Wiki Stacks 4_30.docx`, 18 URLs, mixed/Polymarket focus). Both ingested 2026-04-30.

### Wave 5A register summary (decisions added 2026-04-30)

**Adopt-Cemini-Wiki-Workflow (1):**
- `[ADOPT 2026-04-30]` @sources/alash3al-stash.md — Apache-2.0, Go (81.5%), 407★, 1 contributor; 8-stage memory-consolidation pipeline (episodes → facts → relationships → causal links → goal tracking → failure patterns → hypothesis verification → confidence decay) backed by PostgreSQL + pgvector. Same Karpathy-pattern thesis as `@sources/atomicmemory-llm-wiki-compiler.md`, but operates as **internal episodic memory** rather than external compiled wiki — pairs with kb-server (deployed librarian) and context7 (external API knowledge). Bus-factor caveat (1 contributor, fork-and-maintain required) but architectural fit is clean.

**Steal-from with status-change (1):**
- `[STEAL-FROM-UPGRADED-FROM-DEFER 2026-04-30]` @sources/shiyu-coder-kronos.md — MIT, Python (81.9%), **22,172★**, 20 contributors, AAAI 2026 acceptance (Nov 2025). Wave 4A had marked Kronos as Defer; Wave 5A's deeper read upgrades to Steal-from based on the AAAI acceptance + 22k stars + 20 contributors + repo-level MIT confirmation. The **Steal-from-the-tokenizer-not-the-model pattern**: extract `KronosTokenizer` (continuous OHLCV → discrete tokens) for use against Cemini's own ticker/OHLC stream; do NOT deploy the full Kronos forecasting model (license is open through Kronos-base 102.3M, but Kronos-large 499.2M is closed). Pairs with `@sources/microsoft-qlib.md` as operational quant-RL stack: qlib provides pipeline + training + factor library; Kronos provides the tokenizer that turns market data into LLM-consumable sequences.

**Reference-only (2):**
- firnflow — clean license + sound architecture but missing infrastructure prerequisites (S3 stack); **infrastructure-prerequisite-block pattern** documented as new Reference-only sub-cause
- zeroboot — minimal-bootstrap reference; valuable as illustration but no Cemini deployment surface

**Reject (2):** the_well + WorldSeed — both fail Filter 3 (no Cemini-domain overlap) and have other negative signals

### Wave 5B register summary (decisions added 2026-04-30)

**Adopt-Cemini-Stack (1):**
- `[ADOPT 2026-04-30]` @sources/caiovicentino-polymarket-mcp-server.md — MIT, Python (80.7%), 395★, 1 contributor (fork-and-pin pattern); 45 tools across 5 categories (markets / trades / portfolio / orders / data). The **dual-MCP-Polymarket pattern** with kukapay's `@sources/polymarket-predictions-mcp.md`: kukapay = real-time-odds (read-only); caiovicentino = trade-execution + market discovery + portfolio (read+write). Both required for the deployable Polymarket-informed-flow analyst service `@sources/polymarket-informed-minority-gomezcram-2026.md` proposes. 6 enumerated risks (bus-factor, secret management, rate-limiter under load, single release, regulatory exposure, transitive deps).

**Steal-from (5)**:
- @sources/agriciDaniel-claude-obsidian.md — MIT, Python+Shell, 3,581★, 1 contributor; Karpathy-pattern visual-Obsidian-vault wrapper with `/wiki` `/save` `/autoresearch` slash commands. **Three-way Karpathy-pattern stack** with atomicmemory's compiler (headless feature-rich) + wastedcode's memex (headless minimal). Highest-value extract: the `/autoresearch` skill (multi-step research → wiki page → backref pattern in a single command).
- @sources/piebald-claude-code-system-prompts.md — MIT, JavaScript, **9,684★** (highest in Wave 5B), 114 releases through v2.1.123 on 2026-04-29. Anthropic-deployed Claude Code system-prompts extracted across 114 versions. **Prompt-extraction-pattern**: study how Anthropic's harness has evolved release-over-release; structural inspiration only (Anthropic IP boundary — never verbatim copy). DeepSeek-V4-Pro-Think XML adherence verification gate before any Cemini analyst-prompt port.
- BridgeWard arbitrage adapter (Polymarket cluster), poly-maker market-making bot (Polymarket cluster), Polymarket-BTC-15-Min-Bot (Polymarket cluster) — all Steal-from pattern references in the Wave 5B canonical brief, no dedicated source pages.

**Reject (3)**: poly_data (license-metadata-discrepancy: GPL-3.0 LICENSE vs MIT pyproject.toml metadata; LICENSE file canonical → Reject). NautilusTrader-as-rejection-trigger pattern surfaces in URLs 12 and 17 (NautilusTrader's LGPL-3.0 transitive taint).

**Reference-only (4):**

**Unavailable (5)**: 5/18 URLs returned no content; queued for future re-fetch attempts.

### Wave 5 — new patterns documented this wave

1. **Status-upgrade-on-deeper-evaluation** — Kronos: Wave 4A Defer → Wave 5A Steal-from. Mirror direction of Vibe-Trading's Wave 2 Adopt → Wave 4 Steal-from downgrade. Status changes at re-evaluation are a normal pattern in this wiki — not flip-flopping; second-look reveals new evidence (AAAI 2026 acceptance + repo-level metadata) that wasn't visible at first read.

2. **Adopt-and-follow-upstream vs Adopt-but-fork-and-pin** — Wave 5 stratifies the Adopt tier: qlib (Microsoft, 40k★) follows upstream; stash + polymarket-mcp-server + claude-obsidian (1 contributor each) require fork-and-pin maintenance. Bus-factor is the deciding axis. Adopt-but-fork-and-pin shouldn't be confused with Steal-from — it's still Adopt (you DEPLOY the project), but Cemini owns the maintenance going forward.

3. **Steal-from-the-tokenizer-not-the-model** — Wave 5A Kronos. Open-source ML projects often have a clean-license preprocessing layer + closed/restricted model weights. Cemini's adoption surface is the preprocessing layer; the model weights are closed-source from the perspective of Cemini's deployment.

4. **Prompt-extraction-pattern** — Wave 5B piebald. **Content vs runtime distinction**: extracting deployed system prompts from a vendor harness (here, Anthropic's Claude Code) is content-level reverse-engineering, not runtime IP. The IP boundary depends on use: structural inspiration is permissible; verbatim copy into Cemini's analyst prompts crosses the boundary. DeepSeek-V4-Pro-Think XML adherence verification gates the question of whether Cemini's analyst-prompt format CAN absorb extracted prompt patterns at all.

5. **License-metadata-discrepancy resolution** — Wave 5B poly_data. SPDX/repo-level metadata can disagree with the LICENSE file (here: pyproject.toml says MIT; LICENSE file says GPL-3.0). LICENSE file is canonical for IP-sale-readiness gating. New IP-sale-readiness sub-pattern (see @concepts/ip-sale-readiness.md).

6. **Infrastructure-prerequisite-block pattern** — Wave 5A firnflow. Clean license + sound architecture is necessary but not sufficient for Cemini Adopt; missing infrastructure prerequisites (here: S3 stack) drop a candidate to Reference-only without crossing into Reject. Distinct from Defer (which is gated on a verifiable test); infrastructure-prerequisite-block is gated on a Cemini-side decision to provision the prerequisite.

7. **NautilusTrader-as-rejection-trigger** — Wave 5B URLs 12 + 17. NautilusTrader's LGPL-3.0 license creates transitive taint for any project that takes it as a dependency. The Cemini-stack rejection rule: if a candidate's LICENSE is clean but its core dependency is LGPL-3.0+, the candidate inherits the taint at deployment.

8. **Dual-MCP-Polymarket pattern** — Wave 5B caiovicentino + kukapay. Two MCPs covering complementary surfaces (read-only-odds + read+write-trading) form a more complete deployment toolchain than either alone. Pattern applicable to other prediction-market venues (Kalshi: read MCP exists, write MCP doesn't yet; Manifold: neither exists).

9. **Three-way Karpathy-pattern stack** — Wave 5B claude-obsidian + wastedcode-memex + atomicmemory-llm-wiki-compiler. The same Karpathy-pattern thesis stratifies on substrate: filesystem-namespace (memex) / compile-pipeline (llm-wiki-compiler) / vault-overlay (claude-obsidian). All three are MIT; all three are LLM-curated; all three compound. Adoption-orthogonal: a Cemini deployment could use any one, two, or all three at different layers.

### Wave 5's effects on this page's recommendations

- Wave 1-4 register (kb-server deployed, llm-wiki-compiler retained, agentmemory steal-from, 8 Wave-2 Adopts, BSIV Wave-3 Adopt) — **unchanged**.
- Wave 5A adds 2 dedicated source pages: stash (Adopt-Wiki-Workflow Karpathy-pattern internal-episodic-memory layer) + Kronos (Steal-from with status-change documentation).
- Wave 5B adds 3 dedicated source pages: caiovicentino's Polymarket MCP (Adopt-Cemini-stack, dual-MCP pattern with kukapay's MCP) + claude-obsidian (Steal-from, third Karpathy-pattern member) + piebald's claude-code-system-prompts (Steal-from, prompt-extraction-pattern with Anthropic IP caveat).
- 9 new cross-wave patterns documented (1-9 above).
- License poison-pill family: GPL-3.0 confirmation (poly_data), LGPL-3.0 transitive taint (NautilusTrader), license-metadata-discrepancy resolution sub-pattern (poly_data).

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
