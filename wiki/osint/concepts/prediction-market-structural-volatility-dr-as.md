---
title: Prediction-market structural volatility (DR-AS)
type: concept
tags: [concept, prediction-markets, volatility, kalshi, k163]
keywords: [DR-AS, Wright-Fisher, Glosten-Milgrom, binary contract vol, interval score]
related:
  - sources/arxiv-2607.08199-prediction-market-volatility-structural-2026-07-14.md
  - entities/platforms/kalshi.md
  - concepts/proper-betting-clob-prediction-markets.md
  - concepts/polymarket-bot-architecture.md
maturity: draft
created: 2026-07-14
updated: 2026-07-14
---

## Relations

- @sources/arxiv-2607.08199-prediction-market-volatility-structural-2026-07-14.md — K163 deep-read
- @entities/platforms/kalshi.md — panel venue

## Raw Concept

Conditional variance for binary prediction-market prices should encode (1) remaining binary uncertainty and time-to-resolution and (2) adverse selection from spreads × activity — not only lagged squared returns.

## Narrative

**DR-AS (deadline-resolution + adverse-selection):**

- **Deadline channel:** `h²_DR ≈ p(1-p)/τ` — peaks at p≈0.5; intensifies as τ→0 (Wright-Fisher / absorbing boundaries).
- **Order-flow channel:** `h²_AS ≈ K · ν(V) · s²/4` — Glosten-Milgrom spread as adverse-selection variance, scaled by volume activity.
- **Best forecast class empirically:** residual GARCH on top of DR-AS baseline beats plain ARCH/GARCH on Kalshi hourly panel (Xi et al. 2607.08199).

**Operator use (pm-kalshi):**

1. Size / quote width with `p(1-p)/τ` as primary risk scalar before Kelly.
2. Widen further when spreads widen and volume spikes together (AS term).
3. Expect sports contracts to be jumpier near events; economics closer to smooth DR.
4. Do not refit per-category blindly — paper finds pooled structure transfers.

REFERENCE — no library install.
