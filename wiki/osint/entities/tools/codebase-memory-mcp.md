---
title: DeusData/codebase-memory-mcp — Tree-sitter code intelligence MCP
type: entity
tags: [entity, tool, mcp, ccc, k134]
keywords: [codebase-memory-mcp, tree-sitter, sqlite, call-graph, token-reduction]
related:
  - sources/eval-github-repos-plan-multi-wiki-2026-06-29.md
  - sources/3-28-links-1.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/mattpocock-skills.md
  - "@ccc-wiki/entities/tools/codebase-memory-mcp.md"
maturity: draft
created: 2026-06-29
updated: 2026-06-29
---

## Relations

- @sources/eval-github-repos-plan-multi-wiki-2026-06-29.md — K134 Adopt
- @sources/3-28-links-1.md — prior steal-from mention (67× token reduction claim)
- @ccc-wiki/entities/tools/codebase-memory-mcp.md — CCC-primary federation deploy canon

## Raw Concept

K134 Adopt re-eval of [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) — C + Tree-sitter + SQLite knowledge graph exposed via MCP.

## Narrative

Indexes repo ASTs into persistent graph; **14 MCP tools** for call-graph, architecture overview, HTTP route discovery. Docx claims ~99% token reduction vs grep-read loops.

**Phase-0 (2026-06-29):** **CONDITIONAL-GO** — MIT confirmed; 20.7k★; 186 open issues. Pre-install gates: (1) verify static binary checksum / build from source on laptop; (2) MCP tool allowlist — read-only graph queries only; (3) compare vs lazy-tool catalog before duplicating prod-mcp paths.

**Laptop adoption (2026-06-29):** Binary `~/.local/bin/codebase-memory-mcp` v0.8.1; federation sync via `scripts/sync_federation_codebase_memory_mcp.sh` (18 workspaces + global `~/.cursor/mcp.json`). Prod brief: `2026-06-29_k134-codebase-memory-cursor-federation-prod.md` on cemini-prod.

**Primary surface:** CCC-wiki federation repo comprehension; optional TipDrop kit extension (docx overlap flag).

**Reject overlap:** Not a wiki compiler — nested-wiki serving still laptop git + Read/grep.

## Snippets

> "get_architecture enables comprehensive codebase overviews at ~1,500 tokens vs ~100,000 file-by-file." [Source: 3_28 links 1.docx §3; reinforced K134 eval URL 6]
