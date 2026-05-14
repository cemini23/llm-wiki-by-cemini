---
title: "LAP (Lean API Platform) — OpenAPI/GraphQL/AsyncAPI compiler to custom @lap text grammar"
type: entity
category: tool
tags: [entity, tool, api-compilation, openapi, graphql, asyncapi, k44, steal-from-conditional-phase-0-2026-05-14, k44-use-case-invalid-mcp-generation, single-author-stale-49d]
keywords: [lap-platform, openapi-3-x, graphql-sdl, asyncapi, lap-text-grammar, token-optimization, context-injection, apache-2-license, NOT-mcp-server-generator]
related:
  - sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @concepts/cemini-license-posture.md — Apache-2.0 IP-sale-safe

## Raw Concept

A Python framework that compiles API specifications (OpenAPI 3.x, GraphQL, AsyncAPI) into a **custom `@lap` text grammar for token-optimized context injection** — NOT an MCP server generator, as K44 doc-level eval implied. **Apache-2.0, 245 stars verified (vs claimed 241), last commit 2026-03-26 (49d stale), 1 author**. K44 verdict needs material correction.

## Narrative

### Phase-0 audit verdict (2026-05-14): STEAL-FROM-CONDITIONAL

**Critical finding (G6): the K44 use case is invalid.** LAP compiles API specs into a proprietary `@lap` text grammar designed for direct LLM context injection (token-efficient prompt assembly). It does **NOT** generate MCP servers, executable tool definitions, or runtime API wrappers. The K44 framing ("compile kb-server's OpenAPI spec into a working MCP server") is unsupported by the source repo.

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo discovery | **PASS** | `Lap-Platform/LAP` resolved; single author (no satellite repos) |
| G1 | Star + maturity | **CONDITIONAL** | 245★ verified (+4 drift vs claimed 241), Apache-2.0, **last commit 2026-03-26 (49d stale)**, single-author bus factor |
| G2 | License | **PASS** | Apache-2.0 verbatim |
| G3 | Compilation output format | **PASS — as designed** | Produces `@lap` text grammar files (custom DSL); validated against OpenAPI/GraphQL/AsyncAPI inputs |
| G4 | GraphQL SDL token overhead | **UNVERIFIED** | K44 NEEDS VERIFICATION flag stands; no published benchmarks on large schemas |
| G5 | TypeScript SDK | **MISSING** | K44 claimed TypeScript SDK; repo is **Python-only**. K44 eval claim incorrect |
| G6 | **MCP server generation** | **FAIL — INVALID K44 USE CASE** | **LAP does NOT generate MCP servers.** Output is `@lap` text grammar for LLM context injection, not executable tool definitions. The kb-server → MCP automation use case in K44 is unsupported by the source |
| G7 | Token-optimization claim | **PARTIAL** | Compaction logic exists; specific compression ratios unpublished; no comparison vs raw OpenAPI prompt |
| G8 | Stale-maintenance risk | **FLAG** | 49 days since last commit; single author; **DEFER trigger: 2026-06-14** (if 90+ days stale by then, downgrade to REJECT) |

**Verdict: STEAL-FROM-CONDITIONAL** — but for a different use case than K44 proposed.

### Corrected use case: token-optimized context injection (~30 min POC)

The genuinely valuable extraction is the **token-compaction grammar** for injecting API specs into Claude Code / Codex context windows without burning the full OpenAPI JSON budget. POC scope:

1. Run `lap compile` against `kb-server`'s OpenAPI spec → produce `@lap` text file
2. Measure token count delta vs raw OpenAPI JSON in a Claude Code prompt
3. Verify the LLM can answer "which endpoint to call for X" using the `@lap` representation as effectively as with raw OpenAPI

If token reduction is ≥40% and answer accuracy is preserved, the grammar is portable as a prompt-engineering pattern (not as runtime infrastructure).

### Original K44 use case (kb-server → MCP) — INVALID

**Do NOT pursue.** LAP does not produce MCP servers. The existing path for kb-server → MCP exposure remains hand-coded tool definitions (already done) or future direct OpenAPI → MCP tooling (different ecosystem; LAP is not it).

### Stale-commit DEFER trigger

If `Lap-Platform/LAP` has no new commits by **2026-06-14** (90 days from last commit), downgrade this entity from STEAL-FROM-CONDITIONAL to REJECT. Single-author + extended dormancy crosses the abandoned-after-pump threshold.

## Snippets

> "LAP specializes in compiling disparate API specifications—including OpenAPI 3.x, GraphQL, and AsyncAPI—into standardized, agent-native formats optimized for Claude Code and Codex."
[Source: K44 eval ¶49 — but note "agent-native format" = custom `@lap` text grammar, NOT MCP server. K44 framing requires correction.]
