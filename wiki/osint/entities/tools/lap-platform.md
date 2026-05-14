---
title: "LAP (Lean API Platform) — OpenAPI/GraphQL/AsyncAPI compiler to agent-native tools"
type: entity
category: tool
tags: [entity, tool, api-compilation, openapi, graphql, asyncapi, mcp-server-generation, k44, steal-from-doc-level-pending-phase-0]
keywords: [lap-platform, openapi-3-x, graphql-sdl, asyncapi, agent-native-format, langchain, apache-2-license, kb-server-rest-mcp-conversion]
related:
  - sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md
  - concepts/cemini-license-posture.md
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @concepts/cemini-license-posture.md — Apache-2.0 IP-sale-safe

## Raw Concept

A Python+TypeScript framework that compiles API specifications (OpenAPI 3.x, GraphQL, AsyncAPI) into standardized agent-native formats optimized for Claude Code and Codex. **Apache-2.0, 241 stars, v0.7.0 release, last commit 2026-03-26**. K44 primary fit: CCC-wiki. Cross-route to OSINT-wiki: extract methodology for compiling the kb-server REST API into executable MCP server tools.

## Narrative

K44 verdict: **Steal-from**. The Cemini relevance here is specific: the `kb-server` REST API currently requires either manual MCP wrapping or hand-coded tool definitions per consumer. LAP's compilation logic, if it works as advertised, would automate that translation — compile `kb-server`'s OpenAPI spec into a working MCP server.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/Lap-Platform/LAP`)
- G2: License verification (Apache-2.0 confirmed)
- G3: Run the compiler against `kb-server`'s OpenAPI spec; verify output is a valid MCP server
- G4: TypeScript SDK overhead on large GraphQL SDL schemas (the K44 eval flagged this as NEEDS VERIFICATION)

**Cross-route relevance to OSINT**: if the compilation logic works, this becomes the missing automation for kb-server → MCP exposure. Currently any new endpoint added to `kb-server` requires hand-edit of the MCP tool list; LAP would eliminate that.

## Snippets

> "LAP specializes in compiling disparate API specifications—including OpenAPI 3.x, GraphQL, and AsyncAPI—into standardized, agent-native formats optimized for Claude Code and Codex."
[Source: K44 eval ¶49]
