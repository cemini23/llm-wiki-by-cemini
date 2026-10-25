---
title: When do prophets profit in prediction markets? (2607.06166)
type: source
tags: [source, arxiv, prediction-markets, kalshi, pm, k151]
keywords: [proper betting, scoring rules, CLOB, Kalshi, ROI, Sharpe]
related:
  - concepts/prediction-markets-efficiency-wolfers-zitzewitz.md
  - concepts/prediction-market-statistical-arbitrage.md
  - concepts/instrumental-probability-learnable-alpha.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/proper-betting-clob-prediction-markets.md
maturity: validated
read_status: deep-read
created: 2026-07-09
updated: 2026-10-25
---

## Relations

- @concepts/prediction-markets-efficiency-wolfers-zitzewitz.md — classical AMM accuracy↔profit equivalence
- @entities/platforms/kalshi.md — live deployment venue

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.06166](https://arxiv.org/abs/2607.06166) |
| **Authors** | Gu, Kagan (Kalshi Research), Sun, Wu, Xu |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.06166-when-do-prophets-profit-in-prediction-markets-au.pdf` |

## Narrative

Resolves AMM-era equivalence breakdown on **CLOB** venues (Kalshi, Polymarket). For any strictly proper scoring rule **S**, exhibits **proper betting** strategy depending only on forecaster belief **p** and market price **q** — positive expected profit when **p** beats **q** under **S** with sufficient liquidity. Essentially unique robust profitability guarantee. Decomposes profit: score gap + Bregman divergence + liquidity loss (explains profit without accuracy edge). **Empirical:** proper betting only strategy converting AI forecast accuracy to profit across thousands of forecasts. **Live Kalshi:** +80.33% ROI, Sharpe 3.35 over one month. **Prod brief** → `pm-*` sizing/execution layer above raw model forecasts.

## Snippets

> "Proper betting is the only strategy that reliably converts accuracy into profit" [Source: arXiv:2607.06166 abstract — paraphrase]

> "A month-long live deployment on Kalshi achieves +80.33% return on investment with a Sharpe ratio of 3.35." [Source: arXiv:2607.06166 abstract]
