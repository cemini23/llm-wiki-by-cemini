---
title: "Hyperliquid agent self-tuning trading — ops caution"
type: concept
tags: [concept, hyperliquid, agents, llm, k88]
keywords: [betashop, hyperliquid agent, fine-tuning, drawdown]
related:
  - sources/trading-posts-compilation-42-2026-05-31.md
  - entities/platforms/hyperliquid.md
  - concepts/perps-dex-funding-carry-strategy.md
  - concepts/perp-dex-price-discovery-lead-lag.md
maturity: draft
created: 2026-05-31
updated: 2026-06-09
---

## Relations

- @sources/trading-posts-compilation-42-2026-05-31.md — Post 39 (@betashop)
- @entities/platforms/hyperliquid.md — venue context
- @concepts/perp-dex-price-discovery-lead-lag.md — agents reading HL tape lag Binance ~700 ms [TENTATIVE]

## Raw Concept

K88 @betashop case study: HL trading agent suffered **−16 points in 48h**, then **self fine-tuned** — illustrates infrastructure + eval loop requirements for LLM-driven perps agents.

## Narrative

**Steal-from pattern:** automated eval → parameter/skill adjustment loop, not "point LLM at HL and print." **`[TENTATIVE]`** — specific agent identity and PnL unverified. Do not brief prod auto-trading without shadow metrics + kill switch (same posture as MAPPO/RL gates).

## Snippets

> "If you think you can just point your LLM at Hyperliquid and print money, you're seriously underestimating the infrastructure." [Source: Posts.docx K88 Post 39, @betashop paraphrase]
