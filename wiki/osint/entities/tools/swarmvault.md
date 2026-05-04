---
title: SwarmVault — Karpathy LLM Wiki Compiler (candidate llm-wiki-compiler replacement)
type: entity
tags: [wiki-tooling, karpathy-pattern, mcp-server, ollama, sqlite, librarian-candidate, evaluation-pending]
keywords: [swarmvault, llm-wiki-compiler-replacement, three-layer-architecture, tree-sitter, hybrid-search, obsidian-export, mcp-native]
related:
  - sources/5-4-links-tool-eval.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/librarian-server-architecture.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/llm-wiki.md
  - entities/infrastructure/ollama.md
maturity: draft
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/5-4-links-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 18, **Adopt** tier verdict
- @concepts/wiki-tooling-evaluation.md — parent decision document; SwarmVault now sits alongside `atomicmemory/llm-wiki-compiler` as candidate tooling for the librarian layer. **WTE re-eval triggered**: llm-wiki-compiler v0.4.0 deployment-blocked by hardcoded `CONCEPTS_DIR` flat-layout assumption (see WTE Phase 3 footnote)
- @concepts/librarian-server-architecture.md — librarian server hosts the wiki compiler runtime; SwarmVault is the alternative implementation candidate for that slot
- @sources/atomicmemory-llm-wiki-compiler.md — original Adopt decision (K2 era, 2026-04-28); now potentially superseded depending on SwarmVault path-resolution audit
- @sources/llm-wiki.md — Karpathy's original gist; both tools target the same pattern
- @entities/infrastructure/ollama.md — runtime dependency for embeddings (`nomic-embed-text` per SwarmVault docs)

## Raw Concept

Identified as Adopt-tier in the 2026-05-04 Gemini DR sweep (`@sources/5-4-links-tool-eval.md` URL 18). The discovery is operationally significant because llm-wiki-compiler (the prior K2-era Adopt for the librarian layer) is currently **deployment-blocked** at v0.4.0 due to a hardcoded `CONCEPTS_DIR = "wiki/concepts"` flat-layout assumption that breaks against this workspace's nested `concepts/` + `entities/` + `sources/` structure. kb-server was adopted as a workaround (see `@concepts/wiki-tooling-evaluation.md` Phase 3 status), but kb-server is not a Karpathy-pattern compiler — it's a static-RAG endpoint.

SwarmVault is the first candidate to surface that **claims** to fill the same Karpathy LLM Wiki slot llm-wiki-compiler was adopted for, with a similar architecture (three-layer + Markdown + SQLite + Ollama + MCP server) and a permissive MIT license.

This page tracks the evaluation: does SwarmVault avoid the flat-layout assumption that broke llm-wiki-compiler? Does it support nested wiki directory structures natively? What's the actual deployment story?

## Narrative

### Identity & maturity (per Gemini DR eval)

- **URL**: https://github.com/swarmclawai/swarmvault
- **License**: MIT
- **Stack**: Node.js / TypeScript, distributed via npm/pnpm
- **Storage**: Markdown files + SQLite (full-text + semantic embeddings hybrid search)
- **Embeddings**: native local provider support (Ollama, `nomic-embed-text`)
- **MCP**: built-in MCP server
- **Maturity**: v3.6.0, 63 releases, 169 commits, 368 stars, formal STABILITY.md and SCALE.md docs
- **Distribution**: `@swarmvaultai/cli` package via `npm install -g`

### Claimed architectural alignment with Karpathy LLM Wiki

The Gemini DR eval describes SwarmVault as:

> "a highly refined, local-first knowledge compiler engineered explicitly around the Karpathy LLM Wiki design pattern. It constructs a durable, persistent three-layer architecture (Raw sources, compiled Wiki, programmatic Schema) utilizing raw Markdown files for long-term storage and SQLite for instantaneous hybrid search... It natively parses over 30 programming languages via tree-sitter AST, integrates flawlessly with local LLMs such as Ollama, and exposes a built-in MCP server, allowing external agents like Claude Code to seamlessly query and traverse the compiled knowledge graph."
> [Source: 5_4 links.docx URL 18]

**This is the same architectural shape as our wiki**: three layers (raw / wiki / schema), Markdown-first storage, MCP-native query surface. If SwarmVault's path-resolution logic is more flexible than llm-wiki-compiler's, it's a viable drop-in replacement.

### Critical open questions before adoption

[NEEDS VERIFICATION 2026-05-04] — these are the load-bearing unknowns:

1. **Does SwarmVault assume flat directory layout?** llm-wiki-compiler v0.4.0's blocker was hardcoded `CONCEPTS_DIR = "wiki/concepts"`. The Gemini DR eval mentions "three-layer architecture" but doesn't confirm whether the wiki layer accepts arbitrary nested directories (`concepts/`, `entities/`, `sources/` + their sub-trees).
2. **Frontmatter compatibility?** This wiki's frontmatter has explicit fields (`type`, `tags`, `keywords`, `related[]`, `maturity`, `created`, `updated`) that follow `@CLAUDE.md`'s schema. SwarmVault may have its own opinionated schema that conflicts.
3. **Bidirectional `related[]` link semantics?** The wiki convention is bidirectional cross-links (`wiki_lint.py` enforces this). SwarmVault's "knowledge graph" may have its own link format incompatible with our `@path/to/page.md` syntax.
4. **MCP server tool surface?** What tools does SwarmVault's MCP server expose? llm-wiki-compiler exposes 7 tools; how does SwarmVault compare? Does it offer the operations the cemini brain actually needs (text-search, semantic-search, related-pages-traversal, full-page-fetch)?
5. **Compile-trigger model?** llm-wiki-compiler runs in `--review` mode (LLM-curated edits) or watch mode (file-watch). What's SwarmVault's equivalent? Does it support our hourly-cron `sync_wiki_to_librarian.sh` flow, or is it always-on file-watch?
6. **Tree-sitter AST overhead.** SwarmVault advertises 30+ language tree-sitter parsing — but our wiki is 99% markdown, not source code. Does the tree-sitter machinery add unnecessary RAM/CPU overhead for our use case?
7. **`graph export --obsidian`** is mentioned in the eval — does this go bidirectional (Obsidian ↔ SwarmVault) or one-way? Critical for the laptop ↔ librarian sync model.

### Resource envelope (claimed)

- **Resident RAM**: "easily fit within the strict ~300-500 MB Node RAM allowance, successfully preserving the 1.4-2.6 GB resident memory headroom mandated for the CPX21 server configuration" [Source: 5_4 links.docx URL 18]
- **Disk**: SQLite hybrid-search engine for ~380 markdown pages — actual size [NEEDS VERIFICATION 2026-05-04]
- **CPU**: lightweight Node.js daemon — exact tree-sitter parsing overhead under load [NEEDS VERIFICATION 2026-05-04]

These are the same envelope claims llm-wiki-compiler made. Per K8 server-probe, the CPX21 has 4 GB RAM with ~2.6 GB headroom after Ollama + nomic-embed-text. SwarmVault should fit, but verification on actual node process RSS is required before commit.

### Adoption decision path

**Phase 0 — Source audit (laptop, ~30 min wall-clock)** [pending user authorization]:
1. `git clone https://github.com/swarmclawai/swarmvault /tmp/swarmvault-eval/`
2. Inspect path-resolution logic (`src/`, look for `CONCEPTS_DIR` / `WIKI_DIR` / `path.join` patterns)
3. Inspect frontmatter parser (does it match our schema, or impose its own?)
4. Inspect related-link/cross-link format
5. Inspect MCP server tool definitions
6. Decide GO/NO-GO based on path-resolution + frontmatter compatibility

**Phase 1 — Smoke test on laptop wiki (if Phase 0 passes)**:
1. `npm install -g @swarmvaultai/cli`
2. Point at a *copy* of `wiki/` (not the canonical), let it build SQLite indices
3. Verify it walks the nested directory tree and resolves `@path` cross-links
4. Run a `swarmvault doctor` (per Gemini DR mention) for self-health-check output
5. Test the MCP server end-to-end with Claude Code

**Phase 2 — Librarian deployment (if Phase 1 passes)**:
1. Deploy `@swarmvaultai/cli` to `cemini-librarian:/opt/cemini-wiki/`
2. Connect to existing Ollama instance (`nomic-embed-text` already running)
3. Replace kb-server's role (or run side-by-side initially)
4. Update `concepts/librarian-server-architecture.md` Phase 3 entry with new state

**Phase 3 — Decommission llm-wiki-compiler v0.4.0**:
- If SwarmVault works end-to-end: archive llm-wiki-compiler from disk, retire kb-server (or keep as static-RAG companion).
- If SwarmVault fails Phase 1 or Phase 2: stay on kb-server, document lessons, await llm-wiki-compiler v0.5+ or another candidate.

### Risk/caveat list

- **Tree-sitter overhead** for a markdown-only wiki may be wasted resources [NEEDS VERIFICATION 2026-05-04]
- **Bus factor** — 169 commits + 368 stars is moderate; if the maintainer disappears, we're back to zero. Same risk as llm-wiki-compiler.
- **STABILITY.md / SCALE.md documentation** is a positive maturity signal but doesn't substitute for end-to-end testing in our environment.
- **MCP tool surface mismatch** may force us to write a translation layer between SwarmVault's MCP and our brain's expected tool calls (similar to the kb-server adapter work).
- **License remains MIT**: clean for IP-sale, no AGPL/GPL contamination concerns.

## Snippets

- **Architecture summary**: "constructs a durable, persistent three-layer architecture (Raw sources, compiled Wiki, programmatic Schema) utilizing raw Markdown files for long-term storage and SQLite for instantaneous hybrid search (combining full-text indexing with semantic embeddings)." [Source: 5_4 links.docx URL 18]

- **MCP-native query surface**: "exposes a built-in MCP server, allowing external agents like Claude Code to seamlessly query and traverse the compiled knowledge graph." [Source: 5_4 links.docx URL 18]

- **Obsidian compatibility claim**: "The tool provides the `graph export --obsidian` command, allowing seamless, bidirectional syncing with the solo developer's local laptop environment." [Source: 5_4 links.docx URL 18]

- **Recommendation tier**: "Adopt. This repository is the exact algorithmic tool defined by the stringent architectural requirements for System 2 (Wiki / librarian server). It operationalizes the specific Karpathy LLM Wiki pattern, interfaces with MCP and Ollama natively out of the box, and supports native Obsidian markdown extraction." [Source: 5_4 links.docx URL 18]

- **Maturity signals**: "Highly stable, marked at Version 3.6.0. Demonstrates 63 releases, 169 commits, and 368 stars. Includes formal STABILITY.md and SCALE.md architectural documentation." [Source: 5_4 links.docx URL 18]

## Dead Ends

*(none yet — pre-evaluation phase. Phase 0 source audit is the gating step.)*
