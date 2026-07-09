---
title: Proper betting on CLOB prediction markets
type: concept
tags: [concept, prediction-markets, kalshi, execution, k151]
keywords: [proper scoring rule, Bregman divergence, CLOB, Kelly failure, Kalshi ROI]
related:
  - sources/arxiv-prophets-profit-prediction-markets-2607.06166-2026-07-09.md
  - concepts/prediction-markets-efficiency-wolfers-zitzewitz.md
  - concepts/prediction-market-statistical-arbitrage.md
  - concepts/instrumental-probability-learnable-alpha.md
  - entities/platforms/kalshi.md
maturity: draft
created: 2026-07-09
updated: 2026-07-09
---

## Relations

- @sources/arxiv-prophets-profit-prediction-markets-2607.06166-2026-07-09.md — primary (Kalshi Research co-author)

## Raw Concept

Classical Hanson AMM theory ties forecast accuracy to profit, but **CLOB** venues (Kalshi, Polymarket) break naive heuristics — Kelly and max-margin bets can lose despite beating the market on proper scores. Gu et al. (2607.06166) construct **proper betting** tied to scoring rule **S**: bet from beliefs **p** and market **q** only; profit decomposes into score gap + Bregman divergence − liquidity loss.

## Narrative

**Implication for CeminiSuite PM bot:** raw model calibration ≠ P&L. Execution layer must map forecasts → proper bets, not Kelly-on-mid. Live Kalshi agent: **+80.33% ROI**, Sharpe **3.35** (1 month). AI leaderboards lose money without this layer (Yang et al. 2025 cite in paper).

## Snippets

> "Proper betting is essentially the only strategy with robust profitability guarantee" [Source: arXiv:2607.06166 — paraphrase from abstract]
