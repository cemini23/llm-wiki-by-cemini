---
title: "Moontower — making sense of returns (earnings, retention, P-CAPE)"
type: source
maturity: draft
related:
  - concepts/stock-return-decomposition-and-p-cape.md
  - concepts/equity-fair-value-evaluation.md
  - sources/substack-rss-moontower-2026-11-22-hillstone.md
  - sources/substack-rss-moontower-2026-11-22-moontower-337.md
updated: 2026-11-22
read_status: read
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | making sense of returns |
| Author | Kris Abdelmessih (Moontower Meta) |
| Type | newsletter, RSS |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-moontower-2026-11-22-making-sense-of-returns.md` |
| Retrieved | 2026-11-22 |
| Published | 2026-11-22 |
| Read status | read |

## Narrative

The post decomposes a stock's return into a dividend part and a reinvestment part, holding the multiple constant:

`E[r] = payout * (E/P) + (1 - payout) * ROE`

At 100% payout the return is the earnings yield. At 0% payout it is ROE. [Source: substack-rss-moontower-2026-11-22-making-sense-of-returns.md]

For the S&P 500 the dividend yield is about 1%, roughly 20% of earnings, so about 80% is retained. At a 22% ROE, `0.80 * 22% = 17.6%`, plus 1% gives about 18.7%. The author calls that too aggressive, because part of retention goes to buybacks, which earn the earnings yield, not ROE. If all retention went to buybacks, the return would be about 5.46%. So the range is roughly 5.5% to 19%, holding the multiple constant, and the split of retained earnings between reinvestment and buybacks is the key unknown. [Source: substack-rss-moontower-2026-11-22-making-sense-of-returns.md]

He compares this with Elm Wealth's P-CAPE. P-CAPE adjusts the CAPE denominator for retained earnings compounded forward at each year's cyclically adjusted earnings yield. Elm reports that P-CAPE beat plain CAPE at forecasting: it explained 35% of the variance in 10-year forward real returns against 24% for CAPE. Elm's 30 September 2026 capital market assumption is a 2.92% real expected US equity return, about 5.12% nominal with a 2.20% breakeven. [Source: substack-rss-moontower-2026-11-22-making-sense-of-returns.md]

Two cautions the author states: most return volatility comes from the multiple, not earnings, so an earnings-only range is too wide; and current earnings and ROE depend partly on circular booking of unfilled AI-infrastructure orders.

The transferable check: when a valuation rests on "earnings yield plus growth", ask what share of retention earns the ROE and what share goes to buybacks.

## Snippets

> "The formula assumes every retained dollar earns the average ROE. A lot of SPX retention goes to buybacks, which only returns the earnings yield, not ROE." [Source: substack-rss-moontower-2026-11-22-making-sense-of-returns.md]
