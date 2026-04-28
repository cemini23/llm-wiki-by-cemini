---
title: "atomicmemory/llm-wiki-compiler — open-source compiler implementing Karpathy's LLM Wiki pattern (covers GitHub + llmwiki.app landing page)"
type: source
tags: [github, npm, mcp-server, karpathy-pattern, wiki-compiler, knowledge-base, librarian-tooling, adoption-candidate]
clusters: [llm-agents]
keywords: [llm-wiki-compiler, llmwiki, karpathy, two-phase-compile, hash-incremental, candidate-review-queue, confidence-metadata, contradicted-by, mcp]
related:
  - concepts/wiki-tooling-evaluation.md
  - sources/llm-wiki.md
  - sources/wastedcode-memex.md
  - sources/willynikes2-knowledge-base-server.md
  - sources/emtwiki-deployed-example.md
  - entities/infrastructure/deepseek-api.md
  - entities/infrastructure/localai.md
  - entities/frameworks/fastmcp.md
  - concepts/librarian-server-architecture.md
  - sources/kepano-obsidian-skills.md
  - sources/obsidian-second-brain-eugeniughelbur.md
  - sources/bare-bones-memory-southpolesteve.md
maturity: validated
read_status: read
created: 2026-04-28
updated: 2026-04-28
---

## Relations

- @concepts/wiki-tooling-evaluation.md — synthesis page that ranks this as **primary adoption candidate** for the workspace librarian; documents 7-of-10 Karpathy-pattern coverage
- @sources/llm-wiki.md — Karpathy's 2025 gist that this project implements (foundational pattern source for both projects)
- @sources/wastedcode-memex.md — sibling Karpathy-pattern implementation, simpler (filesystem-only, no embeddings, no MCP)
- @sources/willynikes2-knowledge-base-server.md — sibling memory-engine + MCP server with three-tier (hot/warm/cold) architecture; more opinionated
- @entities/infrastructure/deepseek-api.md — DeepSeek API works via `OPENAI_BASE_URL` swap; same multi-provider config pattern this project uses
- @entities/infrastructure/localai.md — LocalAI is one of the local-runtime targets (`LLMWIKI_PROVIDER=openai` + `OPENAI_BASE_URL=http://localai:8080/v1`)
- @entities/frameworks/fastmcp.md — this project's MCP server (`llmwiki serve`) parallels the Cemini stack's `cemini_mcp` FastMCP container; can coexist (separate transport / endpoint)

## Raw Concept

- **Original title**: llm-wiki-compiler — *The knowledge compiler. Raw sources in, interlinked wiki out.*
- **Author**: ethanj + 5 other contributors (FrankMa1, ishan5ain, PipDscvr, goforu, socraticblock)
- **Type**: GitHub repo + npm package + landing page
- **URLs**: https://github.com/atomicmemory/llm-wiki-compiler / https://llmwiki.app/
- **Retrieved**: 2026-04-28 (via Exa `crawling_exa`)
- **Stars**: 701 (as of 2026-04-28 ingest); **License**: MIT 🟢
- **Created**: 2026-04-05; **Last push**: 2026-04-23; **Latest release at ingest time**: v0.2.0 (2026-04-16)
- **Latest release as of WTE-1 smoke test 2026-04-28**: **v0.5.1** — 3 minor versions newer than our ingest baseline; project shipped rapidly between docs read and smoke test. Smoke test confirms v0.5.1 CLI surface matches the v0.2.0 README we synthesized from; subcommand names + behavior unchanged. No `compile` schema breakage observed. Worth a re-read of changelogs when the librarian-server Phase 3 lands to capture any new semantic-search or MCP-tool additions
- **Stack**: TypeScript (99.8%), Node.js ≥ 18
- **Read status**: read (deep-read landing page + README; comparing against schema; supplemented 2026-04-28 with WTE-1 smoke-test findings — see @concepts/wiki-tooling-evaluation.md "Path A SMOKE-TEST PARTIAL-PASS" section)

## Narrative

`atomicmemory/llm-wiki-compiler` is the most complete open-source implementation of Karpathy's LLM Wiki gist (which is the schema's foundational pattern source — see `sources/llm-wiki.md`). It implements **7 of the 10 operations** Karpathy describes, leaving only image / Marp slides / fine-tuning unimplemented (none of which differentiates against competitors).

**Core architecture** — same three-layer raw / wiki / schema as the workspace `CLAUDE.md`:
- **Raw sources** in `sources/` (immutable, LLM reads but never modifies)
- **Wiki** as `wiki/concepts/`, `wiki/queries/`, `wiki/index.md` (LLM-generated; Obsidian-compatible `[[wikilinks]]`)
- **Schema** via configuration files + frontmatter conventions

**Frontmatter shape** documented in README:
```yaml
title: Knowledge Compilation
summary: Techniques for converting knowledge representations...
sources:
  - knowledge-compilation.md
confidence: 0.82           # 0–1, LLM-reported confidence
provenanceState: merged    # extracted | merged | inferred | ambiguous
contradictedBy:
  - slug: probabilistic-reasoning
inferredParagraphs: 1      # paragraphs the LLM marked as inferred (vs cited)
createdAt: "2026-04-05T12:00:00Z"
updatedAt: "2026-04-05T12:00:00Z"
```

**Two-phase pipeline**: Phase 1 extracts all concepts from all sources; Phase 2 generates pages. Eliminates order-dependence; catches failures before writing anything; merges concepts shared across multiple sources into single pages.

**Hash-based incremental compile**: only changed sources go through the LLM. Everything else is skipped via SHA-256 hash check. Critical for keeping LLM cost bounded as the wiki grows.

**Compounding queries**: `llmwiki query --save` writes the answer as a wiki page and immediately rebuilds the index. Future queries use saved answers as context.

**Candidate review queue** (`llmwiki compile --review`): LLM output is staged as candidates in `.llmwiki/candidates/` rather than landing in `wiki/` directly. Approve / reject loop with `llmwiki review approve <id>` / `llmwiki review reject <id>`. Acquires `.llmwiki/lock` to serialize against concurrent compile runs. **Aligns with the workspace's hand-curated discipline** — the LLM proposes, the human (or a higher-authority agent) approves before pages land.

**Multi-provider** via env vars:
- Default: `LLMWIKI_PROVIDER=anthropic` (uses `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN`); reads from `~/.claude/settings.json` `env` block as fallback (zero-config when Claude Code is already set up)
- OpenAI-compatible: `LLMWIKI_PROVIDER=openai` + `OPENAI_BASE_URL` (works with local llama-server, LocalAI, etc.)
- Ollama: `LLMWIKI_PROVIDER=ollama` + `OLLAMA_HOST`

The multi-provider story matches the `entities/infrastructure/deepseek-api.md` operative architecture: same `OPENAI_BASE_URL` swap idiom, same OpenAI-SDK shape. Adopting llm-wiki-compiler means the workspace librarian gets the same provider-portability the Cemini stack already targets.

**MCP server** (`llmwiki serve --root <path>`): exposes 7 tools (`ingest_source`, `compile_wiki`, `query_wiki`, `search_pages`, `read_page`, `lint_wiki`, `wiki_status`) and 5 resources (`llmwiki://index`, `llmwiki://concept/{slug}`, `llmwiki://query/{slug}`, `llmwiki://sources`, `llmwiki://state`) over stdio transport. Read-only tools work without API keys; LLM-using tools check provider config per call. **This is the bridge** that lets the dev-stack DeepSeek brain on Hetzner query the workspace wiki via MCP without re-deploying the Track B `wiki_search` server-side. Closes the laptop ↔ server gap.

**Lint pass** (`llmwiki lint`): includes 3 rules that surface the per-page metadata — `low-confidence` flags pages below threshold, `contradicted-page` flags pages with non-empty `contradictedBy`, `excess-inferred-paragraphs` flags pages with too many inferred-vs-cited paragraphs. Direct machine-readable analog to our K-series stale-claim detection (which is currently lint-invisible — `[RETRACTED]` and `[NEEDS VERIFICATION]` are inline text, not surfaced in `wiki_lint.py` section 7 except as a stale-tag age check).

**Karpathy-pattern coverage** (per the project's own self-assessment table in README, cross-checked against `sources/llm-wiki.md`):

| Karpathy concept | This project | Status |
| --- | --- | --- |
| Data ingest | `llmwiki ingest` | Implemented |
| Compile wiki | `llmwiki compile` | Implemented |
| Q&A | `llmwiki query` | Implemented |
| Output filing (save answers back) | `llmwiki query --save` | Implemented |
| Auto-recompile | `llmwiki watch` | Implemented |
| Linting / health-check pass | `llmwiki lint` | Implemented |
| Agent integration | `llmwiki serve` (MCP server) | Implemented |
| Image support | — | Not yet implemented |
| Marp slides | — | Not yet implemented |
| Fine-tuning | — | Not yet implemented |

Workspace status quo coverage = 4 of 10 (Schema / Wiki structure / Lint / Manual ingest workflow). llm-wiki-compiler adoption raises coverage to 7 of 10 in one move.

**Limitations called out by the project** (not glossed over):
- Early software; best for small, high-signal corpora (a few dozen sources). Our wiki is 373 pages — scale-test needed before committing.
- Query routing is index-based (not yet chunked-retrieval-with-reranking; that's on the next-up roadmap).
- Truncation is honest: sources exceeding character limit get `truncated: true` in frontmatter with original char count recorded.

**Open roadmap items** the project lists:
- Claim-level provenance with source ranges
- First-class schema layer with typed page kinds (concept / entity / comparison / overview)
- Multimodal ingest (images, PDFs, transcripts)
- Chunked retrieval with reranking
- Export bundle (`llms.txt`, JSON, JSON-LD, GraphML, Marp)
- Session-history adapters (Claude / Codex / Cursor exports)

The "typed page kinds" item is interesting — it's the same axis our schema already differentiates on (`type: source | entity | concept | brief`). Future contribution-back potential if we adopt.

## Snippets

### S1 — Karpathy-pattern framing (`README.md`)

> "Inspired by Karpathy's [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) pattern: instead of re-discovering knowledge at query time, compile it once into a persistent, browsable artifact that compounds over time."

### S2 — RAG-vs-Compile distinction (`README.md`, "Why not just RAG?")

> "RAG retrieves chunks at query time. Every question re-discovers the same relationships from scratch. Nothing accumulates. llmwiki **compiles** your sources into a wiki. Concepts get their own pages. Pages link to each other. When you ask a question with `--save`, the answer becomes a new page, and future queries use it as context. Your explorations compound. This is complementary to RAG, not a replacement. RAG is great for ad-hoc retrieval over large corpora. llmwiki gives you a persistent, structured artifact to retrieve from."

### S3 — Two-phase incremental pipeline (`README.md`, "How it works")

> "Two-phase pipeline. Phase 1 extracts all concepts from all sources. Phase 2 generates pages. This eliminates order-dependence, catches failures before writing anything, and merges concepts shared across multiple sources into single pages. Incremental. Only changed sources go through the LLM. Everything else is skipped via hash-based change detection. Compounding queries. `llmwiki query --save` writes the answer as a wiki page and immediately rebuilds the index. Saved answers show up in future queries as context."

### S4 — Confidence + contradicted-by metadata (`README.md`, "Page metadata")

> "Compiled pages can carry epistemic metadata in frontmatter so consumers know how trustworthy each page is. […] When multiple sources merge into one slug, metadata is reconciled: min confidence, provenanceState = 'merged', union of contradictedBy (deduped by slug), max inferredParagraphs. `llmwiki lint` adds three rules that surface this metadata: low-confidence — flags pages with confidence below a threshold; contradicted-page — flags pages with non-empty contradictedBy; excess-inferred-paragraphs — flags pages with too many inferred paragraphs without citations."

### S5 — MCP server architecture differentiation (`README.md`, "MCP Server")

> "Where [llm-wiki-kit](https://github.com/iamsashank09/llm-wiki-kit) gives agents raw CRUD against wiki pages, llmwiki exposes the **automated pipelines**: agents get intelligent compilation, incremental change detection, and semantic query routing built in."

### S6 — Karpathy-quote framing (`llmwiki.app/`, landing page)

> "*The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass.*" — Andrej Karpathy
