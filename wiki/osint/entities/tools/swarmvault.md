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
  - entities/tools/codegraph.md
  - entities/tools/pageindex.md
maturity: validated
created: 2026-05-04
updated: 2026-05-12
---

## Relations

- @sources/5-4-links-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 18, **Adopt** tier verdict
- @concepts/wiki-tooling-evaluation.md — parent decision document; SwarmVault now sits alongside `atomicmemory/llm-wiki-compiler` as candidate tooling for the librarian layer. **WTE re-eval triggered**: llm-wiki-compiler v0.4.0 deployment-blocked by hardcoded `CONCEPTS_DIR` flat-layout assumption (see WTE Phase 3 footnote)
- @concepts/librarian-server-architecture.md — librarian server hosts the wiki compiler runtime; SwarmVault is the alternative implementation candidate for that slot
- @sources/atomicmemory-llm-wiki-compiler.md — original Adopt decision (K2 era, 2026-04-28); now potentially superseded depending on SwarmVault path-resolution audit
- @sources/llm-wiki.md — Karpathy's original gist; both tools target the same pattern
- @entities/infrastructure/ollama.md — runtime dependency for embeddings (`nomic-embed-text` per SwarmVault docs)
- @cybersecurity-wiki/entities/tools/maltego.md — cross-wiki backlink: sibling Cybersecurity wiki's Maltego page cites SwarmVault as the OSINT-tradecraft anchor in its sister wiki

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

### Phase 0 audit — completed 2026-05-04, verdict NO-GO

Cloned to `/tmp/swarmvault-audit/`, inspected source. Six load-bearing questions answered:

| # | Question | Verdict | Evidence |
|---|----------|---------|----------|
| Q1 | Supports nested wiki layout? | **FAIL** | `packages/engine/src/vault.ts:2781-2787` hardcodes seven required top-level directories (`wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/code/`, `wiki/outputs/`, `wiki/projects/`, `wiki/candidates/`), each with `index.md`. **No subdirectory nesting under entities/** — would not index `wiki/entities/tools/foo.md`. Same architectural disease as llm-wiki-compiler v0.4.0. |
| Q2 | Frontmatter compatibility | PASS | gray-matter parser preserves arbitrary fields (`vault.ts:6454`); our `type/tags/keywords/related/maturity/created/updated` pass through |
| Q3 | Cross-link syntax | **FAIL** | Uses `[[path/to/page\|Display Title]]` Obsidian-wikilink syntax. No recognition of our `@path/to/page.md` syntax. No bidirectional-link enforcement. Migration would require rewriting all 3,249 `@path` instances in our wiki. |
| Q4 | MCP tool surface | PASS | 48 tools, including all required: `search_pages` (FTS5), `query_vault` (embeddings + graph), `read_page`, `query_graph`, `get_neighbors`, `doctor_vault`, `retrieval_status` |
| Q5 | Compile-trigger model | PASS | Both `swarmvault compile` (on-demand CLI) and `swarmvault watch` (file-watch mode). Compatible with hourly cron sync. |
| Q6 | Maturity signals | PASS | v3.7.2 (newer than Gemini DR's claimed v3.6.0), STABILITY.md (11.7 KB, formal Stable/Experimental/Internal classification), SCALE.md (5.8 KB, tested up to 50k sources / 150k pages / 400k graph nodes) |

### NO-GO reasoning

Q1 is the load-bearing blocker, identical to the failure mode of llm-wiki-compiler v0.4.0 (hardcoded `CONCEPTS_DIR = "wiki/concepts"`) that triggered our adoption of kb-server as workaround.

Workspace state at audit time:
- 99 entity files nested 1-deep across 10 subdirs (`entities/tools/` ×13, `entities/tickers/` ×30, `entities/infrastructure/` ×12, `entities/data-sources/` ×13, `entities/frameworks/` ×11, `entities/platforms/` ×9, `entities/security/` ×4, `entities/observability/` ×4, `entities/models/` ×2, `entities/components/` ×1)
- 3,249 `@path` cross-link instances across the wiki
- concepts/ and sources/ are flat (no nesting issue there)

Three theoretical adaptation paths considered + rejected:

1. **Flatten the wiki**: rename 99 entities (`entities/tools/foo.md` → `entities/foo.md` with category encoded into filename or moved to frontmatter). Loses directory-as-category browsing. Updates ~3,249 cross-link strings + wiki/index.md tree structure. **Cost too high relative to marginal gain over kb-server.**
2. **Pre-process on sync**: rewrite paths during laptop→librarian sync. Workspace keeps nested; librarian sees flat. Adds complex bidirectional sync logic, drift risk, hard-to-debug edge cases.
3. **Fork swarmvault**: modify `vault.ts:2781-2787` to walk arbitrary subdirectories. Maintenance burden + diverges from upstream + still need cross-link migration (Q3).

**Decision**: stay on kb-server. The Karpathy compile loop loss vs SwarmVault is real but acceptable; kb-server provides the static-RAG functionality the brain currently needs. SwarmVault is structurally not a fit without restructuring either swarmvault or our wiki, neither justified by current pain points.

### Conditions under which this verdict could flip

- Upstream swarmvault adds config-driven category-tree support (would unblock Q1)
- We migrate to flat layout for unrelated reasons (e.g. another tool also requires it, or cross-tool standardization argues for it)
- Q3's `@path` → `[[wikilink]]` migration becomes attractive for other reasons (Obsidian wikilinks would work elsewhere too)

### What we keep from this audit

- `concepts/wiki-tooling-evaluation.md` updated with Phase 0 outcome
- License-pattern catalog unchanged (SwarmVault is MIT-clean; no licensing contribution)
- swarmvault evaluated and shelved — future Gemini DR sweeps can skip re-evaluating it unless one of the unblock conditions above changes

### Cleanup

`/tmp/swarmvault-audit/` removed post-audit.

## Snippets

- **Architecture summary**: "constructs a durable, persistent three-layer architecture (Raw sources, compiled Wiki, programmatic Schema) utilizing raw Markdown files for long-term storage and SQLite for instantaneous hybrid search (combining full-text indexing with semantic embeddings)." [Source: 5_4 links.docx URL 18]

- **MCP-native query surface**: "exposes a built-in MCP server, allowing external agents like Claude Code to seamlessly query and traverse the compiled knowledge graph." [Source: 5_4 links.docx URL 18]

- **Obsidian compatibility claim**: "The tool provides the `graph export --obsidian` command, allowing seamless, bidirectional syncing with the solo developer's local laptop environment." [Source: 5_4 links.docx URL 18]

- **Recommendation tier**: "Adopt. This repository is the exact algorithmic tool defined by the stringent architectural requirements for System 2 (Wiki / librarian server). It operationalizes the specific Karpathy LLM Wiki pattern, interfaces with MCP and Ollama natively out of the box, and supports native Obsidian markdown extraction." [Source: 5_4 links.docx URL 18]

- **Maturity signals**: "Highly stable, marked at Version 3.6.0. Demonstrates 63 releases, 169 commits, and 368 stars. Includes formal STABILITY.md and SCALE.md architectural documentation." [Source: 5_4 links.docx URL 18]

## Dead Ends

*(none yet — pre-evaluation phase. Phase 0 source audit is the gating step.)*
