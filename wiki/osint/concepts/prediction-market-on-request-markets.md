---
title: On-request prediction markets — RFQ-created markets
type: concept
maturity: draft
related:
  - sources/substack-rss-event-horizon-2026-11-19-kalshi-eyes-on-demand-prediction-markets-for-con.md
  - entities/platforms/kalshi.md
  - concepts/polymarket-weather-trading-strategy.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: how do on-request prediction markets change market discovery and maker economics?

Built from Event Horizon (2026-11-19), which reports Kalshi documentation for on-request markets and a flight-market page that later returned a 404.

## Narrative

**The model.** A user requests a market that does not exist yet, for example the weather at a specific place and time, or whether a named concert is postponed. Market makers then quote it. This is a request-for-quote pattern applied to event contracts. [TENTATIVE: documentation was seen and then removed; the permanent feature set is unconfirmed]

**What changes.**

- *Discovery.* The listable universe is no longer bounded by a venue's editorial choice. The long tail can be created on demand. A bot that screens a fixed series list will miss markets that appear only after a request.
- *Pricing.* A new market has no history. The first quotes are the only information, and the maker sets the spread against model risk, not observed flow.
- *Liquidity.* Depth is thin at birth. The RFQ flow tells you who is willing to make a price before public trading starts.

**Documented examples.** Weather outcomes at a location and time; concert postponement or cancellation; single-flight status, delay and cancellation. The flight page was live and then removed, so treat flights as unconfirmed.

**Operator reading for a retail PM bot.**

- A discovery layer should watch for new-series announcements, not only the public market list.

**Shipped in CeminiParlays — `5b9aca1` (2026-11-24).** `src/ceminiparlays/discovery.py`
diffs venue snapshots against a persisted state file and prints only net-new series,
newly opened props, and RFQ listings. Team tokens fold through the roster alias table,
so JAC and JAX, WSH and WAS, land on one code. Covered by `tests/test_discovery.py`.

[Source: CeminiParlays git 5b9aca1, verified 2026-11-25]
- A maker-side strategy should price RFQ markets from a model with an explicit prior, because there is no flow to copy.
- A taker-side strategy should avoid opening size in a market whose first quotes are wide and un-informed.

**Risk.** On-request markets widen the manipulation and insider-information surface. A maker should assume a bespoke market attracts the person with the local knowledge.

**Related.** Weather discovery and the sports-market taxonomy pages cover the existing listed-market analogues.
