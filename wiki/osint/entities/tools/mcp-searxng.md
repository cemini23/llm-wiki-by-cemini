---
title: mcp-searxng — Self-hosted SearXNG search MCP
type: entity
tags: [entity, tool, mcp, osint, privacy, k146]
keywords: [mcp-searxng, searxng, ihor-sokoliuk, MIT, web_url_read]
related:
  - sources/eval-github-repo-mcp-plan-2026-07-05.md
  - entities/tools/tavily-mcp.md
  - entities/tools/brightdata-mcp.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @sources/eval-github-repo-mcp-plan-2026-07-05.md — K146 Adopt
- @entities/tools/tavily-mcp.md — hosted RAG alternative

## Raw Concept

K146 Phase-0 on [ihor-sokoliuk/mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `ihor-sokoliuk/mcp-searxng` |
| **License** | **MIT** |
| **Stars / pushed** | ~1k★; pushed 2026-07-05 |
| **Verdict** | **Adopt** — default OSINT web search MCP (self-hosted SearXNG) |
| **Ops** | Requires local SearXNG instance; `SEARXNG_FANOUT` for parallel queries |

Preferred over commercial proxy MCP for routine federation digest lanes.

## Snippets

> "Integrating a self-hosted SearXNG proxy via the searxng_web_search tool." [Source: eval-github-repo-mcp-plan-2026-07-05.md]
