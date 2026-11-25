---
title: Back-of-the-envelope cost of a rolling index hedge
type: concept
maturity: draft
related:
  - sources/substack-rss-moontower-2026-11-15-back-of-the-envelope-hedging-cost.md
  - sources/substack-rss-moontower-2026-11-15-moontower-336.md
  - concepts/deep-rl-delta-vega-hedging.md
  - sources/arxiv-delta-vega-hedging-deep-rl-2611.32790.md
updated: 2026-11-25
---
## Raw Concept

Question this page answers: what does a rolling long-put hedge on a broad index actually cost in return, once the variance it removes is counted?

Method from Moontower Meta (2026-11-15). No backtest is recorded here; the numbers are the author's arithmetic.

## Narrative

Three quantities decide the answer: premium paid, how often the put pays, and the variance it removes.

Premium. At 3% a year over 25 years, about 75% of starting capital goes to insurance.

Payoff frequency. A 15% OTM put pays meaningfully in a crash year, barely in a moderate decline, and nothing in a flat or rising year. In a 25-year sample that is roughly one large payoff, two small ones, and 22 zeros.

Variance. A crash that would have been -40% caps near -18%. Because variance weights the square of the miss, capping that one year removes about three quarters of its variance, and because a single crash year can carry a third of sample variance, total variance falls by about a quarter. Volatility falls from about 16% to about 14%, which cuts vol drag by about 0.3 points.

Net. A hedge costing 1.8 points of arithmetic return and saving about 0.3 points of drag costs roughly 1.5 points of CAGR. The break-even premium for a typical risk preference sits between 1% (clearly worth it) and 5% (marginal).

The transferable rule: price the hedge against the variance it removes, not against the premium alone.

[TENTATIVE] Restates one author's arithmetic. The vol-drag and variance-share figures are approximations, not measured.

## Snippets

> "The put cost 1.8% per year, but because it reduced drag as well, it only lops ~1.5% from CAGR."
