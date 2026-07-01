---
title: "Settlement Manipulation in Prediction Markets — arXiv 2606.31675"
type: source
tags: [arxiv, polymarket, kalshi, prediction-markets, manipulation, k138, pdf]
keywords: [settlement manipulation, cash settlement, five-minute bitcoin, spot order flow, horizon, Stanford, Dai Jia Yu]
related:
  - concepts/settlement-manipulation-prediction-markets.md
  - concepts/polymarket-bot-architecture.md
  - concepts/pm-capital-lock-up-settlement-discount.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
maturity: draft
read_status: read
created: 2026-07-01
updated: 2026-07-01
clusters: [prediction-markets, polymarket, kalshi]
---

## Relations

- @concepts/settlement-manipulation-prediction-markets.md — primary synthesis
- @concepts/polymarket-bot-architecture.md — 5-min crypto bot hazard context
- @entities/platforms/polymarket.md — platform entity update

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Settlement Manipulation in Prediction Markets |
| **Authors** | David Dai, Ruizhe Jia, Shihao Yu |
| **arXiv** | 2606.31675v1 |
| **Type** | PDF (134 pp) |
| **sha256** | `5dc7e9b48622f43415f18a02e6053cd7c4f2633547d2e392e337e5b52b4dd8ca` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.31675-settlement-manipulation-in-prediction-markets.pdf` |
| **Retrieved** | 2026-07-01 |
| **Read status** | read (abstract, intro, model sketch, Figure 1) |

## Narrative

Shows **asset-price prediction contracts** (Polymarket 5-min BTC up/down, Kalshi crypto event contracts) are structurally vulnerable to **cash-settlement manipulation**: manipulator buys PM contract then pushes **underlying spot** in final seconds before oracle close.

### Model harms

- Wealth transfer: PM liquidity traders → manipulators + PM market makers
- **Price discovery degrades** on underlying spot despite **higher spot liquidity** (adverse-selection masking)
- Remedy in model + data: **lengthen contract horizon** — 5-min shows sharp Binance spot flow spike + post-settlement reversal; **15-min largely attenuated**

### Regulatory / design hook

CFTC Core Principle 3 — contracts must be "not readily susceptible to manipulation"; paper argues asset-price PM contracts raise exactly this concern `[CONFIRMED]` vs election/sports oracle literature.

**Cemini relevance:** pm-kalshi bot brief — block or gate 5-min crypto up/down lanes; prefer ≥15-min or non-oracle-spot settlement for any prod bot touching BTC spot settlement.

## Snippets

> "After the launch of Polymarket's five-minute Bitcoin contract, settlement-time spot order flow spikes, causing large price reversals after settlement." [Source: arxiv-2606.31675-settlement-manipulation-in-prediction-markets.pdf abstract (retrieved 2026-07-01)]

> "The remedy is direct: lengthen the horizon." [Source: arxiv-2606.31675-settlement-manipulation-in-prediction-markets.pdf §1 (retrieved 2026-07-01)]
