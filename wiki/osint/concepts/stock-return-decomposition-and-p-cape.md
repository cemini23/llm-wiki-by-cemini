---
title: Stock-return decomposition and P-CAPE
type: concept
maturity: draft
related:
  - sources/substack-rss-moontower-2026-11-22-making-sense-of-returns.md
  - sources/substack-rss-moontower-2026-11-22-moontower-337.md
  - concepts/equity-fair-value-evaluation.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: how do payout, retention and return on equity set the expected return of an equity index, and how does P-CAPE use that?

Built from two Moontower posts (2026-11-22).

## Narrative

**The identity.** Holding the multiple constant, a stock's expected return is

`E[r] = payout * (E/P) + (1 - payout) * ROE`

The first term is the dividend: payout ratio times earnings yield. The second is growth from retained earnings reinvested at ROE.

Two extremes bracket real companies:

- 100% payout: `E[r] = E/P`, the earnings yield, with no growth.
- 0% payout: `E[r] = ROE`, everything compounds inside the business.

**S&P 500 numbers.** Dividend yield is about 1%, roughly 20% of earnings, so about 80% is retained. At a 22% ROE, `0.80 * 22% = 17.6%`, plus 1% gives about 18.7%. If all retention went to buybacks, which earn the earnings yield rather than ROE, the return would be about 5.46%. The range is about 5.5% to 19%, and the split between reinvestment and buybacks is the key unknown. [TENTATIVE: inputs are the author's estimates]

**P-CAPE.** Elm Wealth adjusts the CAPE denominator for retained earnings. For each of the last ten years, take the unpaid portion of earnings, compound it forward at that year's cyclically adjusted earnings yield, then average. Price over that number is P-CAPE; its reciprocal is the return forecast. Elm reports that P-CAPE explained 35% of the variance in 10-year forward real returns against 24% for plain CAPE (33% vs 15% since 1950). Its 30 September 2026 assumption is a 2.92% real US equity return, about 5.12% nominal at a 2.20% breakeven.

**Two cautions.** Most return volatility comes from the multiple, not earnings, so an earnings-only range is too wide. And current earnings and ROE depend partly on circular booking of unfilled AI-infrastructure orders.

**The check to run.** When a valuation says "earnings yield plus growth", ask what share of retention earns the ROE and what share is spent on buybacks.

**2026 caveat on the date.** Today is 2026-11-22; the parenthetical dates in the source are as published. The Elm assumption is as of 2026-09-30.
