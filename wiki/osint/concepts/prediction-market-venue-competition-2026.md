---
title: Prediction-market venue competition and the superapp path (Nov 2026)
type: concept
maturity: draft
related:
  - sources/substack-rss-event-horizon-2026-11-17-is-kalshi-worth-as-much-as-robinhood.md
  - sources/substack-rss-event-horizon-2026-11-19-kalshi-eyes-on-demand-prediction-markets-for-con.md
  - sources/substack-rss-event-horizon-2026-11-20-kalshi-utah-and-the-consequences-of-playing-chic.md
  - sources/substack-rss-event-horizon-2026-11-23-episode-42-the-cftc-now-and-then-with-tölt-strat.md
  - sources/substack-rss-wublock-2026-11-24-october-2026-tradfi-perpetual-futures-volume-rep.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/companies/draftkings.md
  - concepts/prediction-market-state-litigation-2026-11.md
  - concepts/prediction-market-regulation-2026.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: who is competing for prediction-market volume, and where does the moat sit in late 2026?

Built from four Event Horizon issues (2026-11-17 to 2026-11-20) and the venue volume tables they publish.

## Narrative

**The volume ladder.** Trailing seven-day volume reported by TickerTracker across the four issues:

| Venue | 7-day volume |
|---|---|
| Kalshi | about $28bn |
| Polymarket US | about $3.7bn |
| DraftKings DKeX | about $1.4bn |
| Underdog Exchange | about $0.95bn |
| CDNA (Crypto.com) | about $0.9bn |
| Novig | about $0.85bn |
| Rothera | about $0.42bn |
| ProphetX | about $60m |

Source: substack-rss-event-horizon-2026-11-17, -18, -19, -20. The ladder is stable across four days, so it is a structural share, not a one-day print.

**Kalshi's expansion path.** Reported $65bn valuation raise. It bought FB Securities, a small broker, and planned equity trading within two months. It added 36 single-stock perpetuals, including TSMC and SK Hynix. It is working with Compute Desk on AI-compute futures. It is testing on-request markets. It launched a gas-price hedge for rideshare drivers. In short, it is moving from event contracts to a multi-asset venue.

**Polymarket's path.** Polymarket US is small by volume but expanding product: short-duration oil and natural-gas markets after crypto up-or-down contracts passed $1bn in six weeks. Polymarket is reachable through Talos for non-US institutional clients, and live inside Pump.fun for permitted jurisdictions.

**Incumbent response.** FanDuel plans a couple of hundred million dollars of prediction-market investment in 2026. DraftKings and FanDuel gained share as prediction-market volume passed $125bn. Coinbase plans in-house event contracts in the first half of 2027; today it rents Kalshi's markets.

**Where the moat sits.** Reported Kalshi volume is roughly 65% to 70% parlays in every issue. Sports and crypto split the rest. The liquidity is in parlay-style products, not in niche event markets. A bot that wants depth should plan around the parlay and sports books, and treat niche markets as thin.

**The counterweight.** Venue legality moves week to week. Kalshi faces criminal charges in Utah and action in New York; three appellate circuits have rejected its preemption claims and one has accepted them. A venue-share table is a snapshot of a market whose legal perimeter can change.

**Reading for the retail bot.** Diversify venue support but weight liquidity by the parlay/sports share. Track legal events as availability risk, not as market news.

**Shipped in CeminiParlays — `5b9aca1` (2026-11-24).** `src/ceminiparlays/venue_mix.py`
runs quarter-Kelly per venue on the fee-adjusted price, weights each venue by its
addressable sports share, then caps each venue, each correlated group, and the whole
slate. It asserts every bound held before returning, and the result cannot exceed the
Kelly sum. Covered by `tests/test_venue_mix.py`.

[Source: CeminiParlays git 5b9aca1, verified 2026-11-25]
