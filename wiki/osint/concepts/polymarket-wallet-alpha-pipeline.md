---
title: Polymarket wallet-alpha pipeline — screen winners, scan mispricing, consensus trade
type: concept
tags: [concept, polymarket, bot-architecture, copy-trading, wallet-analytics, k64]
keywords: [poly_data, wallet-screening, polymarket-cli, polymarket-agents, kelly, volume-exit, whale-check, farxxxxx1]
related:
  - sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md
  - entities/tools/warproxxx-poly-data.md
  - entities/tools/polymarket-agents.md
  - entities/people/farxxxxx1-polymarket.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/hermes-onchain-forensics-pipeline.md
  - sources/trading-posts-compilation-6-2026-05-29.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-24
updated: 2026-05-29
---

## Relations

- @sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md — K64 Post 1 primary source
- @entities/tools/warproxxx-poly-data.md — historical trade + wallet layer (GPL — patterns only)
- @entities/tools/polymarket-agents.md — MIT agent framework
- @concepts/polymarket-bot-architecture.md — shared lessons (pre-resolution exit, realistic backtests)
- @concepts/polymarket-copy-trading-strategy.md — whale / top-wallet monitoring adjacency
- @concepts/prediction-market-historical-analysis.md — 86M trade dataset use case
- @concepts/hermes-onchain-forensics-pipeline.md — K78 token-level diligence stack (Nansen x402)
- @sources/trading-posts-compilation-6-2026-05-29.md — K78 source

## Raw Concept

K64 @farxxxxx1 documents a **four-layer Polymarket bot** glued by Claude: (0) wallet alpha from `poly_data`, (1) CLI market scan, (2) multi-check agent brain + Kelly, (3) multi-agent consensus execution, (4) volume-aware exits **before** resolution.

## Narrative

### Pipeline stages

```text
poly_data (wallets) → polymarket-cli (mispriced markets) → agents+Claude (thesis) → execution consensus → volume exit
```

| Stage | Filter / action |
|-------|-----------------|
| **0 Wallet screen** | Makers with ≥100 trades, WR>70%, rank by sum PnL → watchlist (~47 in author run) |
| **1 Market scan** | `gap`, `depth`, `hours_to_resolution` gates; ~93% eliminated |
| **2 Brain** | 4/4 checks: base rate, 6h news, whale in market?, crowd bias; conf>75% → quarter-Kelly size |
| **3 Entry** | ≥2/3 strategy agents vote BUY (else half size on 1/3) |
| **4 Exit** | 85% of expected edge captured; 10m volume >3× avg; 24h stale flat |

### Cemini relevance

- **Adversary / signal:** whale-check step formalizes “informed minority” monitoring — pairs with Parity/ColdMath-style wallet forensics (K61).
- **GPL boundary:** do **not** import `poly_data` code — replicate wallet aggregates via Data-API + internal warehouse (pmxt / ArcticDB path).
- **Execution realism:** pre-resolution exit + volume trigger aligns with @concepts/polymarket-bot-architecture.md (don't hold to settlement; slippage on thin books).
- **Stats [TENTATIVE]:** author-reported 74% WR / $11.4k — require independent wallet replay before prod sizing.

### What failed (author)

Sports markets, sub-$10k volume, settlement holds, running 7 strategies concurrently.

## Snippets

> "poly_data tells you WHO is winning. polymarket-cli tells you WHAT is mispriced." [Source: @sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md]
