---
title: "Moontower Meta — back-of-the-envelope hedging cost"
type: source
maturity: draft
related:
  - concepts/back-of-envelope-hedging-cost.md
updated: 2026-11-16
---

## Raw Concept

- **Title:** back-of-the-envelope hedging cost
- **Author:** Kris Abdelmessih (Moontower Meta / Party at the Moontower)
- **Type:** Blog post, free RSS tier
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-moontower-2026-11-15-back-of-the-envelope-hedging-cost.md`
- **Retrieved:** 2026-11-15
- **URL:** https://moontowermeta.com/back-of-the-envelope-hedging-cost/
- **Read status:** read

## Narrative

The post is a numeracy exercise, not a strategy recommendation. The setup: buy a one-year 15% out-of-the-money SPX put for 3% of capital each 1 January, hold the rest in SPX, and roll annually. Price is assumed, not taken from the market.

The arithmetic. Paying 3% a year for 25 years spends about 75% of starting capital on insurance. A 15% OTM put pays meaningfully only in 2008, a little around 2001-2002 and 2022, and nothing in the other 22 years. Assuming the put pushes in two years and makes about 7x once, the hedge costs roughly 1.8% of arithmetic return per year.

The counterweight is variance. In 2008 the unhedged loss was about -40%; hedged, it caps near -18%. Measured as a miss from an average year, 50 squared against 26 squared gives about one quarter of the variance. Because one year carried about a third of sample variance, the put removes about a quarter of total variance, so volatility falls from about 16% to about 14% and vol drag from about 1.3% to about 1.0%. Net effect on CAGR is roughly -1.5%, between a third and a half of the historical equity risk premium.

The stated range: at a 1% premium the trade is a clear yes; at 5% it is marginal. The author's point is that trained estimation beats waiting for a backtest.

[Source: substack-rss-moontower-2026-11-15-back-of-the-envelope-hedging-cost.md]

## Snippets

> "3% a year for 25 years is 75% of your starting capital spent on insurance."

> "Without the put, 2008 was down 40%, but with the put, your loss caps at -18%."

> "The put cost 1.8% per year, but because it reduced drag as well, it only lops ~1.5% from CAGR."
