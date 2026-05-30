---
title: Polymarket Agents — Official Sanctioned Developer Framework (MIT)
type: entity
tags: [tool, prediction-markets, polymarket, mit, adopt-tier, official-sanctioned, agent-framework]
keywords: [polymarket-agents, official-framework, autonomous-ai, polymarket-trading, agent-deployment, polymarket-stack-foundation]
related:
  - sources/links-3-5-4-tool-eval.md
  - sources/polymarket-5-5-tool-eval.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md
  - concepts/polymarket-wallet-alpha-pipeline.md
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-python-order-utils.md
  - entities/tools/polymarket-trackers.md
  - concepts/polymarket-market-making-architectures.md
  - entities/tools/ai-polymarket-agent.md
  - sources/trading-posts-compilation-k84-2026-05-30.md
  - sources/multi-wiki-tool-eval-v4-k84-2026-05-30.md
maturity: draft
created: 2026-05-05
updated: 2026-05-24
---

## Relations

- @sources/links-3-5-4-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 18, **Adopt** tier
- @sources/polymarket-5-5-tool-eval.md — companion 2026-05-05 batch on the broader Polymarket stack
- @sources/caiovicentino-polymarket-mcp-server.md — Wave 5 Adopt; works alongside Polymarket Agents in the LLM-bridge layer
- @entities/platforms/polymarket.md — Polymarket venue entity
- @entities/tools/polymarket-python-order-utils.md — companion Adopt; order-signing layer
- @entities/tools/ai-polymarket-agent.md — K55 third-party MCP claim overturned to **NO-GO** (2026-05-28); prefer official `Polymarket/agents` + existing MCP bridges
- @sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md — K64 Post 1: custom 4-check Claude loop + Kelly on top of framework
- @concepts/polymarket-wallet-alpha-pipeline.md — “brain” layer in wallet-alpha stack

## Raw Concept

Polymarket Agents is the **officially sanctioned** developer framework for building autonomous AI agents that trade on Polymarket. MIT-licensed (clean for IP-sale). Adopt-tier verdict in K30 links-3-5_4 batch — per eval, this is **the canonical foundation** for any Polymarket integration.

## Narrative

- **URL**: `https://github.com/Polymarket/agents` [CONFIRMED 2026-05-24, K64 + prior eval]
- **License**: MIT (~3.6k★)
- **Status**: **officially sanctioned** by Polymarket (rare for prediction-market platforms)
- **Maturity**: per eval, "comprehensive utility suite"

### Why Adopt for Cemini's Polymarket integration

Per K30 plan, the canonical Polymarket integration stack is:

| Component | Source | Role |
|-----------|--------|------|
| **Polymarket Agents** | This entity | Official-sanctioned framework foundation |
| **python-order-utils** | `@entities/tools/polymarket-python-order-utils.md` | Order signing + cryptography |
| **py-clob-client** | Polymarket-internal (reference) | CLOB API wrapping |
| **caiovicentino/polymarket-mcp-server** | `@sources/caiovicentino-polymarket-mcp-server.md` | MCP bridge to Cemini's brain |

Polymarket Agents is the load-bearing foundation — the other three plug into it. All four are MIT-licensed.

### Integration with Cemini

Cemini already targets Kalshi as primary venue + Polymarket as secondary. The K28 + K30 brief stack adds Polymarket via the canonical stack above. Polymarket Agents becomes the **trading-side primitive** that Cemini's `services/llm_analyst/` calls into for any Polymarket order placement, position management, or market data retrieval.

Architectural flow (proposed):
```
DeepSeek brain (decides "open Polymarket position on contract X")
  → conductor (routes to Polymarket-flavored taxonomy class)
    → polymarket-mcp-server (MCP tool surface)
      → Polymarket Agents (framework)
        → python-order-utils (sign order)
          → py-clob-client (POST to Polymarket CLOB)
            → Polymarket exchange
```

### K64 operator pattern (@farxxxxx1)

Strip default agent logic; run **four-check** Claude loop (base rate, news, whale presence, crowd bias) + quarter-Kelly sizing before consensus execution layer. See @concepts/polymarket-wallet-alpha-pipeline.md.

### Open questions [NEEDS VERIFICATION 2026-05-05]

- Maturity signals (commits, latest version, release cadence) beyond star count
- Whether it's actively maintained (eval claims "comprehensive utility suite" but doesn't quote commit-dates)
- Relationship to Polymarket's official `py-clob-client` — does Polymarket Agents wrap py-clob-client, or are they parallel libraries?
- Test coverage + production deployment signal

### Adoption path

This is gated as part of the broader K30 **Polymarket Stack Adoption brief** (to be staged at `briefs/2026-05-05_polymarket-stack-adoption.md`). Don't fragment across separate briefs — the four components ship as a unit.

## Snippets

- **Adopt-tier framing** (K30 eval): "Officially sanctioned developer framework and comprehensive utility suite constructed to empower users to build and deploy autonomous AI." [Source: links 3 5_4.docx URL 18]

- **Recommendation tier**: "Adopt — execute installat[ion] into the production stack." [Source: links 3 5_4.docx URL 18]
