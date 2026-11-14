---
title: "Event Horizon — Episode 40: the Misery Index with Adjacent Markets' Lucas Kohorst"
type: source
related:
  - concepts/k296-feeds-wave.md
  - concepts/prediction-market-regulation-2026.md
  - concepts/prediction-market-trade-out-moat.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/kalshi-retail-lp.md
  - concepts/parlay-market-making.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Episode 40: The Misery Index With Adjacent Markets' Lucas Kohorst |
| Author | Event Horizon (with Daniel O'Boyle, InGame) |
| Type | newsletter with podcast, RSS teaser |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md` |
| Retrieved | 2026-11-09 |
| File | substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md |
| Read status | read |

## Narrative

### The Misery Index

Lucas Kohorst, co-founder of Adjacent Markets, describes a product that uses prediction markets to measure how miserable people are. The episode notes give no index definition, weights, or history. The concept is `[TENTATIVE]` and the index construction is unresolved. [OPEN QUESTION 2026-11-10]

The useful point is the asset class: **a composite sentiment index built from event-contract prices**. That is a different product from a single binary market, and it needs a weighting scheme, a rebalancing rule, and a resolution policy for each component.

### Volume records

Kalshi set successive volume records in the week.

| Date | Kalshi volume | Parlays | Sports | Crypto |
|---|---|---|---|---|
| Nov 7 | $5.33bn (record) | 75.6% | 17.1% | 6.81% |

The next issue in the wave reports a further record of $5.36bn on November 8, with a 74.6% parlay share.

The parlay share is the structural fact. **About three quarters of Kalshi volume is parlay product**, not single event contracts.

Seven-day trailing volume (ending November 7, DCMs only):

| Exchange | Seven-day volume |
|---|---|
| Kalshi | $29.0bn |
| Polymarket US | $3.89bn |
| DraftKings DKeX | $1.43bn |
| Novig | $703m (through Nov 6) |
| Underdog | $699m |
| Crypto.com/NADEX | $668m |
| Rothera | $405m |
| ProphetX | $37.5m |

[Source: substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md]

### Legal and regulatory pressure

The week after the midterms produced a dense legal cluster.

- **CFTC versus states.** Legal Sports Report says the new interpretation makes the legal situation harder, because Michigan and Nevada already hold injunctions. The California Nations Indian Gaming Association condemned the directive as an attempt to undermine court orders and tribal sovereignty. Chairman James Siva called prediction markets "illegal gaming". [Source: substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md]
- **Kalshi lost in two circuit courts.** Appeals courts rejected its attempts to block state gambling laws in Connecticut, New York, and Nevada. The Arkansas attorney general filed a new suit.
- **States block the products.** Ohio's OCCC reported that MooMoo, Robinhood, and Gemini stopped new sports event contracts. Coinbase agreed to stop from November 13. Utah's attorney general said the largest apps are pulling out of the state.
- **Political risk.** Maxine Waters, bidding to chair House Financial Services, pledged to curb "predatory platforms, including prediction markets". Politico reported that Democrats plan an aggressive oversight regime.

### The Vanderbilt finding

Researchers at Vanderbilt identified suspicious prediction market activity before two New York Times/Siena poll releases. One Polymarket user placed bets worth **$191,277** on Senator Pete Ricketts to win re-election in the early hours of October 31. The Times/Siena poll showing Ricketts six points ahead was published about an hour later. [Source: substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md]

The researchers did not conclude that the user had inside information. The case is a pattern, not a proof.

### Accuracy

- The **New York Times** analysis found that for most of the midterm race, prediction markets performed no better than poll-based forecasts. They performed better only as Election Day neared and polling went stale. [Source: substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md]
- A **Brennan Center** study found that Kalshi odds shift voters' expectations. A candidate at 67% odds was 10 percentage points more likely to be named the likely winner than a candidate at 50% odds. More than 80% of voters want tighter regulation or a ban.

The two findings point in opposite directions for the same product: the odds are not a better forecast, and they change what people believe.

## Snippets

> "Kalshi volume: $5.33 billion (new record). Parlays: 75.6% of volume." [Source: substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md]

> "For most of the midterm race, prediction markets performed no better than election forecasts ... But as Election Day neared, prediction markets performed better as forecasts and polling became stale." [Source: substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md]

> "Pure and simple, prediction markets are illegal gaming." — James Siva, CNIGA [Source: substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md]

## Dead Ends

- **Using the Misery Index as a trading signal.** The index construction is not in the source. No weights, no history, no backtest.
- **Reading parlay share as event-contract share.** Three quarters of Kalshi volume is parlay product. A model built on single binary contracts must size against the remaining quarter.
