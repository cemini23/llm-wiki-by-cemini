---
title: "Arithmetic models for commodity futures, vanilla, and calendar-spread options"
type: source
related:
  - concepts/k294-osint-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-23
---

## Raw Concept

Title: Arithmetic models for commodity futures, vanilla, and calendar-spread options
Authors: Malthe Rauh Johansen, Nina Lange, David Skovmand, University of Copenhagen
Type: arXiv preprint (2610.28071)
Inbox file: `research to be indexed/osint/arxiv-2610.28071-arithmetic-models-for-commodity-futures-vanilla.pdf`
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.28071-arithmetic-models-for-commodity-futures-vanilla.pdf`
Retrieved: 2026-10-23
Read status: skimmed (abstract)

## Narrative

The authors fit an unscented Kalman filter to WTI futures, vanilla options, and calendar-spread options, 2013-2024.

Three stochastic-volatility factors are needed for the level and the slope of the volatility term structure. Hedges on those factors remove almost all of the daily risk of a vanilla-option portfolio.

A fit that omits calendar-spread options overprices them. It overstates the decorrelation between adjacent futures. Adding the spreads removes the overpricing and improves those hedges, with a small loss on vanilla pricing and hedging.

The arithmetic model fits futures and vanilla options better than its geometric counterpart. It also hedges the vanillas slightly better.

Filed for the volatility-factor and calibration method. **No trade.**
