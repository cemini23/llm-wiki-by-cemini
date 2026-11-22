---
title: "Moontower #337 — taking enough risk, ANT, returns math, t-statistics"
type: source
maturity: draft
related:
  - concepts/market-structure-efficiency-and-edge-decay.md
  - concepts/stock-return-decomposition-and-p-cape.md
  - sources/substack-rss-moontower-2026-11-22-hillstone.md
  - sources/substack-rss-moontower-2026-11-22-making-sense-of-returns.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Moontower #337 |
| Author | Kris Abdelmessih (Moontower Meta) |
| Type | newsletter, RSS, omnibus issue |
| Location | `research to be indexed/osint/substack-rss-moontower-2026-11-22-moontower-337.md` |
| Retrieved | 2026-11-22 |
| Published | 2026-11-22 |
| Read status | read |

## Narrative

The weekly issue republishes two essays, "Hillstone" and "making sense of returns", and adds two sections. The full detail is on the two source pages; this page covers the extra material.

**ANT.** Anthropic went public on Thursday and closed about 17% above its IPO price, then traded back near the IPO price on Friday. It raised close to $100bn and closed near a $2tn valuation including unvested shares. The author has no view on the company, but poses the strategic question: if the race is an intelligence arms race, does the payoff require being the last firm standing, and would that firm then outrank a government? [Source: substack-rss-moontower-2026-11-22-moontower-337.md]

**Statistics section.** Two short pieces on significance. Kaabar divides a strategy's average return by its standard error: 0.05% a day with 1% daily volatility over 1,000 days gives t of about 1.58, which is not significant. Cohen reduces a two-way split test to `D squared > N`, where D is half the gap and N the total count, which is an absolute z-score above 2. The practical rule from Cohen: at small N you can only detect large differences. At N=50 the winner must almost double the loser; at N=1,800 a 10% difference becomes detectable. [Source: substack-rss-moontower-2026-11-22-moontower-337.md]

**The caution that matters for the operator.** Backtest results from short samples are usually not significant. Strategy changes should be large, not cosmetic, until the sample is big enough. Tag the t-stat arithmetic as arithmetic; tag the applicability to a small live book `[TENTATIVE]`.

## Snippets

> "The smaller the N, the bigger the difference needs to be, to be detectable." [Source: substack-rss-moontower-2026-11-22-moontower-337.md]
