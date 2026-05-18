---
title: Non-Latency-Sensitive Arbitrage Strategies — Prediction Markets
type: concept
tags: [concept, trading-strategy, arbitrage, prediction-markets, polymarket, kalshi, standing-order]
keywords: [dutch book, sum-of-outcomes arb, yes-no complement arb, cross-venue slow contracts, calendar arbitrage, resolution-date arb, standing-order arbitrage, logical arbitrage]
related:
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/favorite-longshot-bias.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @concepts/cross-venue-arbitrage-pattern.md — the *latency-sensitive* sibling: BTC 1h contracts, ms-scale windows, atomic execution. This page is the complement — strategies whose edge is a *logical/accounting* inconsistency that does not decay in milliseconds
- @concepts/favorite-longshot-bias.md — the structural mispricing FLB describes is one *source* of the inconsistencies these strategies harvest

## Raw Concept

Prompted by an operator note (2026-05-18) that arbitrage strategies were added to the Cemini bot for the first time, with an explicit request to focus on **strategies that do not require low latency**.

The existing @concepts/cross-venue-arbitrage-pattern.md covers the fast case (BTC 1h, races to take a fleeting quote). This page covers the slow case: four strategies where the edge is a *standing* logical or accounting inconsistency. You place limit (maker) orders and wait; you are not racing anyone. Execution-speed risk is replaced by capital-lockup, fee-drag, and resolution-rule risk.

## Narrative

### Why these are "non-latency-sensitive"

A latency-sensitive arb (the BTC page) is a *race*: a quote is briefly mispriced, several bots see it, the fastest taker wins, and the window closes in milliseconds. Your infrastructure has to be fast or you get nothing — and worse, you get adverse-selected (you only win the fills nobody faster wanted).

The four strategies below are different. The edge is a **logical inconsistency in a set of prices that all have to be true at the same time**:

- A set of mutually exclusive outcomes whose probabilities must sum to 1.
- A YES and a NO that must sum to $1.
- Two venues pricing the *same* settled outcome.
- Two dates where one event logically implies the other.

That inconsistency does not evaporate in milliseconds. It sits in the book until someone closes it, often for minutes to days, because closing it requires *capital* (you must hold the position to resolution), not *speed*. So you can:

- Post **limit/maker orders** at your target prices and wait to be filled (often earning a maker rebate instead of paying a taker fee).
- Run the scanner on an ordinary cloud host (`cemini-prod` is fine — no co-location needed).
- Poll on a relaxed cadence (seconds to minutes), not a tight loop.

The trade-off: your risk moves. It is no longer "did I get filled before the fast bot." It is now **capital lockup** (money tied up until resolution), **fee/gas drag** (a capped edge is easily eaten by costs), **leg risk** (one leg fills, the other does not), and **resolution-rule risk** (the "same" event resolves differently than you assumed).

### Universal cost gate

Every strategy here produces a *known, capped* profit. So before placing anything, gate on:

```
net_edge = gross_edge
         − taker_fees (per leg, both venues)
         − maker_rebates earned (negative cost, if posting passively)
         − Polygon gas (Polymarket legs)
         − slippage on size
         − safety_margin

PLACE only if net_edge > 0.
```

Then **annualize** to compare against alternatives:

```
annualized_return ≈ (net_edge / capital_locked) × (365 / days_to_resolution)
```

A 2% locked edge that resolves tomorrow is excellent. The same 2% locked for 11 months is mediocre — it competes with a T-bill. A long-dated arb is only worth the capital if the annualized number clears your hurdle rate. This is the single most common mistake in slow arb: treating a capped, time-locked return as if it were instantaneous.

---

### Strategy 1 — YES/NO complement arb (single binary market)

**The inconsistency.** In one binary market, a YES share and a NO share together pay exactly $1 at resolution (one wins, one loses). Therefore `YES_ask + NO_ask` should be ≥ $1.00. When it is **< $1.00**, buy one of each: you spend `YES_ask + NO_ask`, you collect $1 at resolution, profit is locked.

**Worked example.** Polymarket market, YES ask $0.62, NO ask $0.36. Buy both for $0.98. At resolution exactly one side pays $1.00. Gross edge = $0.02/share. Net it against gas + any fees + safety margin; if still positive, size it.

**Why no latency.** You are not predicting the outcome — you own both sides. Nothing about the event matters. You post two limit buys at your target prices and wait. If only the cheaper leg fills, you hold an unfilled order on the other; no loss, just no trade yet.

**Risks specific to it.**
- Capital is locked until resolution; annualize.
- On Polymarket, YES and NO are separate CLOB tokens — depth on each side differs; the executable size is the *thinner* of the two books.
- A 1–3¢ raw edge is routinely eaten by gas + slippage. The cost gate is doing real work here.
- Resolution-rule edge cases: ensure the market truly resolves to exactly one of {YES, NO} with no "void/50-50" branch that would break the $1 payout assumption.

### Strategy 2 — Dutch-book / sum-of-outcomes arb (one venue, multi-outcome)

**The inconsistency.** A market with N **mutually exclusive and collectively exhaustive** outcomes (e.g. "which party wins the seat": A / B / C / other). Exactly one resolves YES → exactly one share pays $1. So the YES asks across all N outcomes should sum to ≥ $1.00. When `Σ YES_ask(i) < $1.00`, buy one share of *each* outcome: total cost < $1, guaranteed $1 payout. (Equivalently on the NO side: if `Σ NO_ask(i) > N − 1`, the NO legs are rich.)

**Worked example.** A 4-candidate market with YES asks $0.40 / $0.31 / $0.18 / $0.07 = $0.96. Buy all four for $0.96; one pays $1.00. Gross edge $0.04. Net against 4× gas/fees + slippage — note costs scale with N, so a wide market needs a wider raw gap.

**Why no latency.** Same as Strategy 1, generalized. The N prices are quoted by different participants who do not coordinate, so the set drifts out of consistency and *stays* there until an arber sweeps it. You post N limit orders and wait.

**Risks specific to it.**
- **Exhaustiveness is the whole game.** If the outcome set is *not* truly collectively exhaustive (a missing "none of the above" / "other" bucket), the YES legs do **not** guarantee a $1 payout — the real event can land outside your basket and every leg loses. Verify the market's resolution text lists a catch-all, or that the listed outcomes genuinely cover the space.
- Cost scales with N: N legs of gas/fees. Wide markets need a bigger gap to clear the gate.
- Leg risk scales with N too: filling 3 of 4 legs leaves a directional position. Either complete the basket or unwind.
- Some markets have correlated/overlapping outcomes that are *not* mutually exclusive — those are not Dutch-bookable.

### Strategy 3 — Cross-venue arb on slow contracts

**The inconsistency.** The *same* real-world outcome is listed on both Polymarket and Kalshi. If the two venues price it apart by more than round-trip cost, buy the cheap venue / sell (or buy the complement on) the rich venue; at resolution both settle to the same truth and the spread is yours.

**How this differs from the BTC page.** @concepts/cross-venue-arbitrage-pattern.md targets BTC 1h contracts — high volatility, the cross-venue gap opens and closes in seconds, so it *is* a latency race. Restrict this strategy to **long-dated, low-volatility** contracts instead: election outcomes, season-long sports (division/championship winners), macro thresholds (a rate decision months out), regulatory approvals. There the gap opens because of *flow imbalance* (one venue's users are net-long) and persists for **hours to days** — no race.

**Worked example.** "Party X wins the 2026 governor race" — Polymarket YES $0.55, Kalshi YES $0.61 for the equivalent contract. Buy Polymarket YES at $0.55, buy Polymarket NO (or sell Kalshi YES) to lock. The $0.06 gap sits for days because the markets are slow. Post limit orders on both venues, fill over minutes.

**Why no latency.** A months-to-resolution contract barely moves intraday. The cross-venue gap is a slow-flow phenomenon; a relaxed poll (every few seconds to minutes) catches it. `cemini-prod` connectivity is sufficient — no co-location.

**Risks specific to it.**
- **Same-contract identification** — Polymarket and Kalshi word "the same" event differently. Misidentification = you arbitraged *two different contracts* and hold real directional risk. Curate the contract map by hand.
- **Resolution-rule divergence** — Polymarket resolves via UMA optimistic oracle; Kalshi via internal ToS determination. Usually identical, occasionally not. For each pair, confirm the resolution criteria match *before* going live (edge cases: postponed games, ambiguous source-of-truth, void conditions).
- **Capital locked for the full contract life** — possibly months. Annualize hard; a 6¢ edge locked 8 months may not beat alternatives.
- **Leg risk** — one venue fills, the other does not → unhedged directional position. See the partial-fill recovery options in @concepts/cross-venue-arbitrage-pattern.md.
- **Jurisdiction** — venue access and server-region geo-blocks apply (see @concepts/cemini-deployment.md and the Polymarket geo-routing work).

### Strategy 4 — Calendar / resolution-date arb (logical monotonicity)

**The inconsistency.** Two contracts on the *same underlying* with *different resolution dates*, where one outcome **logically implies** the other, so their prices must obey an inequality. When the quoted prices violate it, the violation is a pure logical arbitrage — no opinion on the underlying needed.

The classic relation is **monotonicity of "ever happens by date T"**: if an event resolving YES by an earlier date implies it also resolves YES by a later date (e.g. "BTC trades above $X at any point before [date]"), then

```
P(event by later date)  ≥  P(event by earlier date)
```

If the market quotes the **near-dated YES above the far-dated YES**, that is impossible — buy the cheap far-dated YES, sell the rich near-dated YES (or buy its NO). At the earlier date one of two things is true and either way you are covered; the locked edge is the inverted gap.

**Worked example.** "Fed cuts rates by July" YES $0.70 and "Fed cuts rates by September" YES $0.64. A cut by July is also a cut by September, so the September YES must be ≥ the July YES. It is 6¢ *lower* → buy September YES at $0.64, buy July NO at $0.30 (cost $0.94). Logic check: if a cut happens by July, July YES pays — but you hold July NO... so this requires pairing the *implied* leg correctly. The clean construction: **buy the under-priced far YES and sell the over-priced near YES** of the implication, sized so the dominated states net positive. Construct the exact leg pairing per contract; the principle is the monotonic inequality, the execution is contract-specific.

**Why no latency.** A monotonicity violation is a *modeling error by the market*, not a fleeting quote. It can persist for days because few participants think across two separate date-stamped contracts. Slow poll, limit orders.

**Risks specific to it.**
- **The implication must actually hold.** "Above $X *at* date" (a snapshot) does **not** nest the way "above $X *ever by* date" (a barrier) does — a snapshot can be true in May and false in July. Only barrier/"ever" style contracts, or correctly nested threshold pairs, are monotone. Verify the resolution text defines a *cumulative* event before assuming the inequality.
- **Resolution-source consistency** — both dates must resolve off the same data source and definition, or the "same underlying" assumption breaks.
- Capital locked until the *later* date; annualize.
- Leg construction is the subtle part — get the pairing of which leg you buy vs sell wrong and you have a directional bet, not an arb. Paper-trade each new contract template first.

---

### Cemini-side application

- **Run as a standalone scanner service** on `cemini-prod`. No co-location, no special connectivity. A relaxed poll loop (every few seconds for cross-venue, every few minutes for the within-venue logical checks) is sufficient.
- **Post maker orders** at target prices; let fills come to you. Earning the rebate instead of paying the taker fee can be the difference between a positive and negative net edge.
- **Depends on the same venue integration foundation** as the fast arb: Polymarket CLOB stack (py-clob-client, python-order-utils — see @concepts/polymarket-api-reference.md) and Kalshi (@concepts/kalshi-api-reference.md). Strategies 1, 2, 4 need only *one* venue; Strategy 3 needs both.
- **Backtest before live** — historical price-divergence stats inform realistic edge thresholds (see @concepts/prediction-market-historical-analysis.md). A scanner that fires on raw gaps without the cost gate will "find" arbs that are net-negative after gas.
- **Sizing** — these are capped, near-certain payoffs, so they tolerate larger size than a directional bet, but executable size is bounded by book depth (the thinner leg) and by how much capital you are willing to lock to resolution. See @concepts/kelly-sizing-quarter.md for the sizing discipline.

### Strategy comparison

| Strategy | Venues | Edge source | Window | Main risk |
|---|---|---|---|---|
| 1 — YES/NO complement | 1 | YES+NO ask < $1 | minutes–hours | capital lockup, gas eats thin edge |
| 2 — Dutch-book | 1 | Σ YES asks < $1 | minutes–hours | outcome set not exhaustive; N× costs |
| 3 — Cross-venue (slow) | 2 | venue price gap | hours–days | contract misID, resolution divergence |
| 4 — Calendar / date | 1 (or 2) | monotonicity violation | hours–days | implication doesn't actually nest |

## Snippets

- **Operator scope note** (2026-05-18): arb strategies "just added ... to the bot for the first time"; explicit instruction to "focus on ones that don't require low latency." This page documents the four standing-order strategies selected; the latency-sensitive BTC case stays in @concepts/cross-venue-arbitrage-pattern.md. [Source: operator session 2026-05-18]

## Dead Ends

*(none yet — first synthesis. Record here any arb template that proved un-runnable, e.g. a multi-outcome market that looked Dutch-bookable but lacked a catch-all bucket, or a date pair whose contracts turned out to be snapshot-style and non-monotone — so the same dead end is not re-walked.)*
