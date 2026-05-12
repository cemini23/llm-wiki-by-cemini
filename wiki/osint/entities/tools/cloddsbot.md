---
title: "CloddsBot — Multi-Agent Trading Terminal"
type: entity
tags: [tool, trading-bot, multi-agent, nodejs, steal-from, k38]
keywords: [cloddsbot, steal-from, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
license_verified: MIT
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 9)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/alsk1992/CloddsBot`
- **Tier (per source brief)**: **Steal-from**
- **License** [VERIFIED 2026-05-11]: **MIT** (clean for pattern extraction per Cemini license posture). Maturity: 254★ / last push 2026-05-08 / ~3.5 months old.

## Narrative

Self-hosted AI-driven algorithmic trading terminal. Anthropic Claude primary + 8 LLM providers. 4 specialized agents: market analysis, alerts, execution. Native Web3: Solana DeFi, EVM, Hyperliquid, Binance perps. Node.js runtime.

### Integration vector

Steal-from: port to Python the **multi-agent routing logic**, **risk-engine math**, **prediction-market integrations**, **MCP tool schemas**. Do NOT adopt Node.js runtime (mismatch with Cemini Python stack).

### Risks

TypeScript→Python translation of async order execution is high-risk for financial losses if mistranslated. Massive scope (21 messaging platforms, multiple blockchains) — extract narrowly.

[Source: Link Evaluation Brief Trading Stack.docx, URL 9]
