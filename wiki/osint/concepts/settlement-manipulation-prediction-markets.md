---
title: Settlement manipulation in prediction markets (K138)
type: concept
tags: [concept, polymarket, kalshi, manipulation, microstructure, k138]
keywords: [settlement manipulation, cash settlement, five-minute contract, spot push, horizon remedy, oracle, Binance]
related:
  - sources/arxiv-settlement-manipulation-pm-2606.31675-2026-07-01.md
  - concepts/polymarket-bot-architecture.md
  - concepts/pm-capital-lock-up-settlement-discount.md
  - concepts/cme-settlement-mechanics-for-prediction-markets.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/kalshi-implied-macro-belief-distributions.md
maturity: draft
created: 2026-07-01
updated: 2026-10-25
---

## Relations

- @sources/arxiv-settlement-manipulation-pm-2606.31675-2026-07-01.md — Dai, Jia, Yu (2606.31675)
- @concepts/polymarket-bot-architecture.md — retail bot build patterns; hazard overlay
- @concepts/pm-capital-lock-up-settlement-discount.md — distinct mechanism (lock-up discount vs spot push)

## Raw Concept

What prompted this page: K138 arXiv **2606.31675** — first rigorous model + Polymarket 5-min BTC empirical footprint for **cash-settlement manipulation** on asset-oracle PM contracts.

## Narrative

### Mechanism

Binary PM contract settles on **observable spot price** at horizon \(T\). Manipulator:

1. Buys PM side (public)
2. Trades spot in final seconds to **push oracle** toward winning side
3. Spot reverts post-settlement (transitory push, not information)

Spot maker cannot distinguish manipulator from informed flow → **less informative settlement price** but **more displayed liquidity** (adverse-selection relief paradox).

### Empirical signature (Polymarket 5-min BTC)

| Signal | 5-min contract | 15-min contract |
|--------|----------------|-----------------|
| Final-10s Binance spot flow spike | Sharp | Attenuated |
| Post-settlement reversal | Large γ slope | Much smaller |
| Manipulator profit vs retail | Material | Largely absent |

### Design remedy

**Lengthen horizon** — longer window aggregates ordinary spot information; fixed push less often pivotal. Complements (does not replace) oracle diversification and TWAP/volume-weighted settlement designs `[NEEDS VERIFICATION 2026-07-01]` for prod implementation.

### Cemini posture

| Lane | Action |
|------|--------|
| **pm-kalshi exploratory bot** | **NO-GO** on 5-min crypto up/down; gate ≥15-min or non-spot-oracle markets |
| **LP / maker** | Widen or avoid settlement-window quotes on asset-oracle binaries |
| **Research** | Track Kalshi crypto event contract horizons vs manipulation footprint |

Brief: `briefs/2026-07-01_k138-pm-settlement-manipulation-guard-prod.md`

## Snippets

> "Rather than making the underlying market more informative, they degrade its price discovery and transfer wealth from ordinary traders to those who manipulate them." [Source: arxiv-2606.31675-settlement-manipulation-in-prediction-markets.pdf §1 (retrieved 2026-07-01)]
