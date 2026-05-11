---
title: "Perplexity MCP Server (official)"
type: entity
tags: [tool, mcp-server, live-web-search, perplexity, cemini-prod-candidate, k38]
keywords: [perplexity, mcp, adopt, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 7)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/perplexityai/modelcontextprotocol`
- **Tier (per source brief)**: **Adopt**
- **License**: Apache-2.0 / MIT typical for Perplexity OSS — verify in repo

## Narrative

Official MCP server for Perplexity's API Platform. TypeScript service. Exposes sonar-pro + sonar-reasoning-pro live-web search/reasoning models to MCP-compatible agents. Standardized translation proxy.

### Integration vector

Adopt into both workflow (analyst research) and Cemini prod (Docker-isolated). Closes the **live web search** gap in the algorithmic trading pipeline without custom scraping.

### Risks

Hard vendor dependency on Perplexity API → recurring costs + rate-limit risk during volatile market events. TypeScript service adds slight devops complexity vs Python/FastAPI stack.

[Source: Link Evaluation Brief Trading Stack.docx, URL 7]
