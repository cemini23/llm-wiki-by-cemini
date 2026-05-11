---
title: "9Router — Token-Compressing LLM Proxy"
type: entity
tags: [tool, llm-proxy, token-compression, cemini-prod-candidate, k38]
keywords: [9router, adopt, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 15)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/decolua/9router`
- **Tier (per source brief)**: **Adopt**
- **License**: [NEEDS VERIFICATION 2026-05-11] License needs verification.

## Narrative

AI routing proxy between LLM agents and upstream API providers (OpenAI/DeepSeek/Anthropic). OpenAI-compatible endpoint at localhost:20128. Heuristics like "Caveman Mode" + automatic string compression to reduce tool_result token footprints. Claims ~65% token reduction.

### Integration vector

Adopt into Cemini prod. As LangGraph + MCP tool outputs grow (large JSON from IBKR/Kalshi), reducing token volume directly impacts trading profitability.

### Risks

Proxy adds network hops + text-processing latency. **Caveman mode heuristic compression** may corrupt precise numerical financial data — strict allowlist of compression-safe content types required.

[Source: Link Evaluation Brief Trading Stack.docx, URL 15]
