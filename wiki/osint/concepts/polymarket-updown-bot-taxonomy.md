---
title: Polymarket Up/Down Bot Taxonomy — 6 Microstructure Bot Types
type: concept
tags: [concept, polymarket, trading-bot, prediction-markets, microstructure, up-down-markets, arbitrage, k52]
keywords: [polymarket-updown-bots, arbitrage-bot, directional-arbitrage, repricing-bot, fair-value-model, cross-timeframe-bot, order-book-imbalance-bot, near-resolution-bot, repricing-lag, limit-orders]
related:
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - concepts/polymarket-bot-architecture.md
  - concepts/non-latency-arbitrage-strategies.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/prediction-market-statistical-arbitrage.md
  - concepts/market-microstructure.md
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - concepts/polymarket-lp-rewards-farming.md
  - entities/people/gustafssonkotte.md
maturity: draft
created: 2026-05-18
updated: 2026-05-20
---

## Relations

- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — Post 2 (@RetroValix), the source this page synthesizes
- @concepts/polymarket-bot-architecture.md — the *engineering* playbook (6-layer websocket, latency, backtesting); this page is the *strategy* taxonomy that sits on top of it
- @concepts/non-latency-arbitrage-strategies.md — Type 1 here (Up+Down < \$1) is the same edge as that page's "YES/NO complement arb"
- @concepts/cross-venue-arbitrage-pattern.md — Type 4 (cross-timeframe lag) is the within-venue cousin of cross-venue arb
- @concepts/prediction-market-statistical-arbitrage.md — the quant-formalized version of Types 3 & 5 (fair-value / imbalance) — micro-price and OBI math
- @concepts/market-microstructure.md — the general microstructure backdrop all 6 types exploit
- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — K55 Post 3 (@Gustafssonkotte) describes a Type-3/Type-5 fair-value+imbalance bot on 5-min BTC markets, with explicit multi-module architecture
- @concepts/multi-module-bot-conflict-detector-pattern.md — K55: structural addition for any taxonomy-type bot — conflict-detector pattern + time-aware sizing for short-resolution markets

## Raw Concept

What prompted this page: K52 ingest of @RetroValix's X post, which claims to have analyzed 1,000 profitable bots on Polymarket short-crypto Up/Down markets and grouped them into 6 types. The post is a *strategy* taxonomy — it complements @concepts/polymarket-bot-architecture.md (which is the *engineering* playbook for building any such bot). This page records the taxonomy so a "what strategy class does bot X run" question has a home.

## Narrative

### The unifying claim

Short-crypto Up/Down markets (5-min / 15-min "will BTC be higher at close") look like a coin-flip on direction. The post's thesis: profitable bots do **not** predict direction — they trade **market microstructure**. The underlying asset moves first; fair probability changes second; Polymarket reprices the contract third. Between those steps a window opens. Every one of the 6 types is a different way of acting inside that lag, *before* the market fully corrects.

### The 6 types

**1 — Arbitrage Bot.** Buys both sides (Up + Down) whenever their combined ask is below \$1.00 (e.g. Up 45¢ + Down 46¢ = 91¢). Exactly one side pays \$1 at resolution → locked profit in any outcome. Edge is *price structure*, not prediction. This is the same edge as the "YES/NO complement arb" in @concepts/non-latency-arbitrage-strategies.md.

**2 — Directional Arbitrage Bot.** Starts from an arbitrage base (Up + Down < \$1) but tilts size toward the side its model says is undervalued — the second side becomes a partial hedge. Pure arb caps upside; the directional tilt adds an EV source while the arb structure caps downside. Arbitrage used as a *protective framework* for a directional bet.

**3 — Repricing / Fair-Value Model Bot.** Builds its own fair-price estimate from the underlying (BTC/ETH spot) and compares it to the lagging Polymarket price; buys the side that is cheaper than fair value. No longer pure arbitrage — it forms a view of what a side *should* be worth right now. Profitability depends entirely on recomputing fair probability faster than the market updates.

**4 — Cross-Timeframe / Multi-Market Bot.** Trades several related markets at once — e.g. the 5-min and 15-min BTC Up/Down contracts. Both react to the same BTC move, but not synchronously: one contract can reprice while the other lags. The bot buys whichever timeframe has not yet caught up to fair value, hedging through the neighboring market. The within-venue cousin of cross-venue arb.

**5 — (Order-Book) Imbalance Bot.** Trades the *structure* around the price rather than the price itself: book skew, uneven repricing, weak position structure, mispricing between related markets. Does not wait for Up+Down < \$1 — it builds a two-sided position in parts around the imbalance to improve EV. (The quant formalization — `I_t`, micro-price — lives in @concepts/prediction-market-statistical-arbitrage.md.)

**6 — Near-Resolution Bot.** Waits for the final stage, when the underlying already shows the winner but Polymarket still trades the winning side at 0.98–0.99 instead of 1.00. Buys the almost-resolved outcome for the residual yield and waits for redeem. High win rate, low per-trade edge — but **tail-risk exposed**: if the outcome was not truly final or the underlying sharply reverses in the last second, one loss wipes many small wins.

### What all 6 share

The post extracts a common DNA:

1. **Limit orders, always.** In small-edge strategies, market-order slippage destroys the entire edge. Every type enters passively.
2. **Small, repeatable edge.** Not one perfect prediction — hundreds/thousands of small temporary mispricings compounded.
3. **Trade structure, not direction.** The questions are "where is price lagging reality / where is the book weak / which timeframe hasn't repriced / can the position be built below fair value" — never just "up or down."
4. **Exploit lag.** Reality → underlying price → fair probability → Polymarket reprice. The bot acts before the last step.
5. **Manage risk through position structure.** Two-sided builds, one side as hedge, neighboring-timeframe hedges — not naked single-side bets.

Compressed: **limit orders + small repeatable edge + precise execution + hedging + speed.**

### Cemini posture

- This is a **strategy menu**, not an architecture. The engineering substrate for any of these is @concepts/polymarket-bot-architecture.md (clean websocket feeds, sub-ms hot path, fill-realistic backtests).
- Types 1 and 6 are the most latency-relaxed (Type 1 = standing logical arb; Type 6 = a slow residual-yield harvest) and align with @concepts/non-latency-arbitrage-strategies.md — candidates for the Cemini arb scanner that does *not* need co-location.
- Types 3, 4, 5 are latency-sensitive (they race the repricing lag) and need the full low-latency stack.
- **Single-source.** @RetroValix is one creator; the "1,000 bots analyzed with Claude" methodology is unverifiable. But the taxonomy *converges* with @concepts/polymarket-bot-architecture.md and Post 4's stat-arb roadmap (same lag-exploitation thesis from three independent authors) — that triangulation is the signal; treat the 6-way partition as a useful map, specific example wallets/handles as `[TENTATIVE]`.

## Snippets

> "At first glance, it may seem like these bots all do the same thing... But in reality, profitable bots trade market microstructure: repricing delays, order book imbalance, arbitrage between Up and Down, lag between 5 minute and 15 minute contracts, and the final seconds before resolution." [Source: posts-2026-05-18.docx — Post 2, @RetroValix]

> "All strategies are different, but the principle is the same: the bot acts before the market fully corrects the price." [Source: posts-2026-05-18.docx — Post 2, @RetroValix]

## Dead Ends

*(none yet — first synthesis.)*
