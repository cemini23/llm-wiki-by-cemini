---
title: "eBay MCP Server (YosefHayim)"
type: entity
tags: [tool, mcp-server, scaling-pattern, zod, k37]
keywords: [ebay, mcp, steal-from, three-surface-eval]
related:
  - sources/evaluating-urls-system-integration.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-urls-system-integration.md` — source evaluation brief (URL 20)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/YosefHayim/ebay-mcp`
- **Tier (per source brief)**: **Steal-from**
- **License**: [NEEDS VERIFICATION 2026-05-11] License needs verification.

## Narrative

Local MCP wrapper exposing the entire eBay Sell API to tool-calling AI assistants (Claude Desktop, Cursor). 300+ distinct tools without routing collapse or LLM parameter hallucination. Uses Zod for runtime schema enforcement.

### Integration vector

Steal-from: study `src/` directory to learn **MCP-server scaling beyond 300 tools** — tool routing, Zod schema discipline, hierarchical tool namespace structures. **No eBay-data adoption** — operational domains do not intersect with Cemini.

### Risks

Maintaining 100% operational coverage of a third-party corporate API ecosystem (eBay) is fraught — deprecated endpoints break silently.

[Source: Evaluating Urls System Integration.docx, URL 20]
