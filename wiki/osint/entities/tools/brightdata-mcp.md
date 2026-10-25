---
title: brightdata-mcp — Enterprise scraping MCP (Bright Data)
type: entity
tags: [entity, tool, mcp, osint, k146]
keywords: [brightdata-mcp, CAPTCHA, proxy, markdown extraction, MIT]
related:
  - sources/eval-multi-wiki-github-mcp-2026-07-05.md
  - entities/tools/mcp-searxng.md
  - entities/tools/firecrawl-mcp-server.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/octobrowser.md
maturity: draft
created: 2026-07-05
updated: 2026-10-25
---

## Relations

- @sources/eval-multi-wiki-github-mcp-2026-07-05.md — K146 Adopt
- @entities/tools/mcp-searxng.md — self-hosted search alternative
- @entities/tools/firecrawl-mcp-server.md — sibling fetch MCP

## Raw Concept

K146 Phase-0 on [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `brightdata/brightdata-mcp` |
| **License** | **MIT** |
| **Stars / pushed** | ~2.5k★; pushed 2026-06-21 |
| **Verdict** | **Adopt** — OSINT/CeminiDFS fetch when self-hosted searxng insufficient |
| **Caveat** | Commercial proxy dependency + API keys; prefer `mcp-searxng` for routine OSINT |

Wiki-only unless operator enables Bright Data account. No cemini-prod scp by default.

## Snippets

> "Encapsulating enterprise-level web scraping proxy arrays directly behind a unified MCP interface." [Source: eval-multi-wiki-github-mcp-2026-07-05.md]
