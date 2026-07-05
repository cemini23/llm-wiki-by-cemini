---
title: "GitHub Repo Evaluation Plan.docx — MCP server stack (2026-07-05)"
type: source
tags: [tool-evaluation, mcp, multi-wiki, k146, docx]
keywords: [chrome-devtools-mcp, serena, firecrawl-mcp-server, unity-mcp, tavily-mcp, mcp-searxng, snyk-mcp]
related:
  - sources/eval-multi-wiki-github-mcp-2026-07-05.md
  - entities/tools/chrome-devtools-mcp.md
  - entities/tools/firecrawl-mcp-server.md
  - entities/tools/tavily-mcp.md
  - entities/tools/mcp-searxng.md
  - entities/tools/unity-mcp.md
  - entities/tools/serena.md
  - entities/tools/snyk-studio-mcp.md
  - entities/tools/hf-mcp-server.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
read_status: read
created: 2026-07-05
updated: 2026-07-05
clusters: [wiki-tooling, agent-harness]
---

## Relations

- @sources/eval-multi-wiki-github-mcp-2026-07-05.md — K146 sibling batch
- @entities/tools/chrome-devtools-mcp.md — K141 Adopt reaffirmed
- @entities/tools/firecrawl-mcp-server.md — **MIT MCP server** (distinct from AGPL `firecrawl/firecrawl`)
- @entities/tools/tavily-mcp.md — Adopt; xsp-killer + CeminiDFS RAG fetch
- @entities/tools/mcp-searxng.md — Adopt; self-hosted search proxy
- @entities/tools/unity-mcp.md — Adopt; castle-sim / game-dev
- @entities/tools/serena.md — Steal-from; LSP semantic retrieval
- @entities/tools/snyk-studio-mcp.md — Adopt; CVE gate for agent codegen
- @entities/tools/hf-mcp-server.md — Adopt; HF hub MCP

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Advanced Model Context Protocol (MCP) Server Evaluation and Pipeline Integration Analysis |
| **URLs** | 19 |
| **sha256** | `8fcac3413feacb9823e4235841f751e562454484b32cd9ba5ed8384aa1eca68c` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repo Evaluation Plan.docx` |
| **Retrieved** | 2026-07-05 (Gemini report) |
| **Read status** | read + Phase-0 (`scripts/adopt_k146_phase0.sh`) |

## Narrative

Docx tier rollup (corrected after `gh api`):

| Tier | Repos |
|------|-------|
| **Adopt** | chrome-devtools-mcp (Apache-2.0), firecrawl-mcp-server (MIT), unity-mcp, tavily-mcp, mcp-searxng, imagesorcery-mcp, hf-mcp-server, snyk/studio-mcp (Apache-2.0) |
| **Steal-from** | serena, pmb-ai, scrapegraph-mcp, rigour, topos |
| **Defer** | stackql-mcp, longbridge-mcp |
| **Reference** | todoist-ai (DRYRUN pattern) |
| **Reject** | notion-mcp-server (sunset/OAuth), pagerduty-mcp, deepwiki |

**Critical license note:** `@entities/tools/firecrawl.md` remains **REJECT** for self-hosted `firecrawl/firecrawl` (AGPL-3.0). This batch's **Adopt** is **`firecrawl/firecrawl-mcp-server`** (MIT) — API-client MCP, not the core scraper repo.

**Active-project routing:** CeminiDFS fetch stack brief; unity-mcp → game-dev wiki; tavily-mcp → xsp-killer intel lane (prod brief only if operator confirms scp); chrome-devtools-mcp → CCC default browser MCP (refresh K141).

## Snippets

> "Chrome DevTools MCP … requires the --no-usage-statistics execution flag to prevent operational data leakage." [Source: GitHub Repo Evaluation Plan.docx URL 1 (retrieved 2026-07-05)]

> "Firecrawl … MIT … distinct from custom scraping scripts." [Source: GitHub Repo Evaluation Plan.docx URL 3 — maps to firecrawl-mcp-server (retrieved 2026-07-05)]
