---
title: unusualwhales-mcp — Unusual Whales MCP server (phields)
type: entity
tags: [tool, mcp, unusual-whales, tipdrop, k133]
keywords: [phields, unusualwhales-mcp, hono, typescript, mcp, options-flow]
related:
  - sources/eval-github-batch-unusualwhales-2026-06-28.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/lazy-tool.md
maturity: draft
created: 2026-06-28
updated: 2026-06-28
---

## Relations

- @sources/eval-github-batch-unusualwhales-2026-06-28.md — K133 Adopt row

## Raw Concept

K133 Phase-0 on [phields/unusualwhales-mcp](https://github.com/phields/unusualwhales-mcp) — third-party MIT MCP bridge to Unusual Whales REST API (options flow, dark pool, congressional trades per docx eval).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `phields/unusualwhales-mcp` |
| **License** | **MIT** (`gh api` 2026-06-28) |
| **Stars / pushed** | 4★; pushed 2025-08-04 |
| **Stack** | TypeScript, Hono, MCP (stdio / SSE / streamable HTTP) |
| **Verdict** | **Adopt** (TipDrop laptop eval + CCC MCP pattern reference) |
| **Steal** | Transport layers, retry/timeouts, tool surface mapping to UW endpoints |

**Not prod CeminiSuite.** TipDrop-only unless operator promotes. Prefer cross-check against **unusual-whales/unusual-whales-official-mcp** (MIT, 71★) before prod TipDrop wiring.

**Compliance:** sanitize all MCP tool output before DRY_RUN Discord — NFA / CFTC 4.41 (see TipDrop `@concepts/compliance-copy.md`).

Brief: `../projects/tipdrop-workspace-kit/briefs/2026-06-28_k133-unusualwhales-mcp-adopt.md`

## Snippets

> MIT TypeScript Hono MCP server for Unusual Whales API — docx Adopt, gh-verified 2026-06-28. [Source: eval-github-batch-unusualwhales-2026-06-28.md]
