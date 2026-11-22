---
title: Prediction-market state litigation and the federal preemption fight (Nov 2026)
type: concept
maturity: draft
related:
  - sources/substack-rss-event-horizon-2026-11-18-i-want-my-money-back-after-watching-the-senate-h.md
  - sources/substack-rss-event-horizon-2026-11-20-kalshi-utah-and-the-consequences-of-playing-chic.md
  - concepts/prediction-market-venue-competition-2026.md
  - sources/substack-rss-event-horizon-2026-11-16-episode-41-weather-markets-with-interactive-brok.md
  - concepts/cme-settlement-mechanics-for-prediction-markets.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: how are US states trying to stop sports event contracts, and how does the CFTC respond?

Built from one newsletter issue (Event Horizon, 2026-11-16) reporting court and agency actions.

## Narrative

The conflict is over whether CFTC-regulated event contracts preempt state gambling law. Both sides now act through courts rather than through negotiation.

State side. States have learned that a cease-and-desist is easy to ignore, because the operator sues and continues trading. The newer tactic is an emergency court order that binds at once. Louisiana obtained an industry-wide temporary restraining order covering sports, election, and award contracts against Kalshi, Polymarket US, Robinhood, Crypto.com, Coinbase, Underdog, Novig, ProphetX, ForecastEx, and Gemini.

Federal side. The CFTC sues the state. Louisiana is reported as the twelfth state sued; Arkansas the eleventh. The agency frames the orders as interference with its exclusive jurisdiction under the Commodity Exchange Act, and has also filed amicus briefs in four federal appellate courts and one state supreme court.

What it means for a bot. Venue availability is now a correctness input, not a market view. An operator that is live in one state can be enjoined in another on a court's schedule, so geofence coverage and venue selection belong in the execution path. The reported Kalshi volume on 14 November was $5.32bn, 73% parlays — the market being litigated is the parlay market.

### The appellate split (2026-11-22 update)

The circuits are split. The 9th, 6th and 4th Circuits have rejected Kalshi's attempts to block state enforcement, each for different reasons. The 4th Circuit affirmed Maryland 2-1 on 18 November, with two majority judges giving different reasons and a third dissent. The 3rd Circuit held Kalshi exempt from state gambling laws. The split raises the odds that the Supreme Court takes the question. [Source: @sources/substack-rss-event-horizon-2026-11-18-i-want-my-money-back-after-watching-the-senate-h.md]

### Criminal exposure (2026-11-22 update)

Utah's Third Judicial District Court requires the Kalshi co-founders to appear in person for arraignment on 13 felony counts on 4 December. A shutdown in New York would matter more than in almost any state outside California, Texas and Florida. [Source: @sources/substack-rss-event-horizon-2026-11-20-kalshi-utah-and-the-consequences-of-playing-chic.md]

### The congressional path (2026-11-22 update)

The Senate passed a bill to bar prediction markets from listing contracts on terrorism, assassination, war, military operations or an individual's death; it goes to the House. In parallel, 43 state attorneys general plus DC formally asked the CFTC to withdraw the rule that would define sports event contracts as swaps. Pew reports at least 15 states considered prediction-market legislation in 2026, and three enacted tax laws: North Carolina, Kentucky and Illinois.

The operator rule stands: venue availability is a correctness input. An injunction, a criminal arraignment or a federal pause can change the tradable list faster than any market signal.

[TENTATIVE] Newsletter accounts of filings. Docket numbers and the count of states were not checked against court records.

## Snippets

> "States have seen the playbook that has been run in other states by the prediction market industry (mostly Kalshi)."

> "the state's eleventh-hour 'emergency' lawsuit seeking to shut down the entire prediction market industry is naked lawfare"
