---
title: Prediction-market moat — trade-out quality beats price
type: concept
related:
  - entities/companies/draftkings.md
  - sources/substack-rss-event-horizon-2026-11-09-episode-40-the-misery-index-with-adjacent-market.md
  - concepts/k296-feeds-wave.md
  - sources/substack-rss-event-horizon-2026-11-10-the-moat-for-prediction-markets-is-trading-not-p.md
  - concepts/prediction-market-regulation-2026.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/parlay-market-making.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/kalshi-retail-lp.md
updated: 2026-11-10
---

## Raw Concept

Which product attribute makes a prediction market win against a sportsbook, if price is not it? Prompted by the Event Horizon argument in the 2026-11-10 post.

## Narrative

### The claim

Price is not the differentiator between prediction markets and sportsbooks. The evidence is the history of online betting:

- Betfair has good prices and is a small share of UK betting.
- DraftKings and FanDuel rarely have the best price and dominated the first decade of legal US sports betting.

Marketing, user experience, and bonus value decide outcomes. [Source: substack-rss-event-horizon-2026-11-10-the-moat-for-prediction-markets-is-trading-not-p.md]

### What prediction markets add

The differentiator is **the ability to trade out of a position**, and the quality of that experience:

| Attribute | Prediction market | Sportsbook cash-out |
|---|---|---|
| Availability | almost always | sometimes, no rule |
| Display | live, continuous position value | one offer at one moment |
| Granularity | sell part of the position | all or nothing |

[Source: substack-rss-event-horizon-2026-11-10-the-moat-for-prediction-markets-is-trading-not-p.md]

### Why it is the load-bearing claim

If trade-out is the moat, the competitive variables move from quoted price to:

1. **book depth and continuity** — can the exit happen at the time the trader wants;
2. **maker economics** — a rebate structure that keeps makers quoting;
3. **settlement and withdrawal speed** — the exit is not complete until funds move.

This reframes the retail-bot question. The question is not "is this quote better than the sportsbook". It is "can I enter and exit at a fair price, at the time I choose, in the size I choose".

### The counter-evidence to keep in view

The same post records a hard fact that sits next to the thesis. About **75% of Kalshi volume is parlay product**. Parlays are a sportsbook product in structure, not a trade-out product. So the growth is coming from a segment where the trade-out property matters least. [Source: substack-rss-event-horizon-2026-11-10-the-moat-for-prediction-markets-is-trading-not-p.md]

Two readings are possible and the source does not choose between them:

- The parlay growth is an on-ramp, and customers migrate to trade-out markets later.
- The parlay growth is the business, and the trade-out property is a niche product.

`[OPEN QUESTION 2026-11-10]`

### What to measure

- **Volume-weighted spread and depth** on a fixed basket of single contracts, by hour.
- **Exit fill ratio** — share of position that can be exited at or inside one tick of the displayed price.
- **Withdrawal latency**, not quoted, but observed.

## Snippets

> "The ability for users to trade out of their positions ... seems like one of the differentiating factors that really matter in the long term." [Source: substack-rss-event-horizon-2026-11-10-the-moat-for-prediction-markets-is-trading-not-p.md]

> "Sportsbooks do have a 'cashout' function, but compared to prediction markets, the UX is terrible." [Source: substack-rss-event-horizon-2026-11-10-the-moat-for-prediction-markets-is-trading-not-p.md]

> "At prediction markets, you can sell a part of your bet/position instead of all of it." [Source: substack-rss-event-horizon-2026-11-10-the-moat-for-prediction-markets-is-trading-not-p.md]

## Dead Ends

- **Building a price-shopping thesis.** The source argues price is not what wins.
- **Assuming parlay growth validates the trade-out thesis.** The parlay segment does not need trade-out.
