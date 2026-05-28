---
title: "Perps DEX funding-carry strategy — market-neutral cross-venue hedged funding capture"
type: concept
tags: [concept, perpetual-futures, funding-rate, market-neutral, cross-venue-hedging, dex, basis-trade, carry-trade, k55]
keywords: [perps-funding-carry, market-neutral-funding-bot, cross-venue-hedging, volatility-adjusted-funding-carry, funding-rate-arbitrage, dex-perpetuals, reduce-only-orders, partial-fill-reconciliation, morpphhhaw, semi-automated-allocator]
related:
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - sources/trading-posts-compilation-25-2026-05-27.md
  - concepts/carry-trade.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/polymarket-bot-architecture.md
  - entities/people/morpphhhaw.md
  - entities/tools/hl-funding-sniper.md
  - entities/people/the-smart-ape.md
  - entities/platforms/hyperliquid.md
  - sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md
  - concepts/pnl-attribution-versioning.md
  - concepts/production-trading-blind-spots.md
maturity: validated
created: 2026-05-20
updated: 2026-05-28
clusters: [quant-finance, crypto, market-neutral]
---

## Relations

- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — Post 1 (@morpphhhaw) primary source
- @concepts/carry-trade.md — canonical carry-trade concept; this is the perp-funding instantiation
- @concepts/cross-venue-arbitrage-pattern.md — cross-venue hedge mechanics overlap; the *signal* here is funding spread rather than spot mispricing
- @concepts/polymarket-bot-architecture.md — bot-discipline lessons fully transfer; "infrastructure-first" thesis matches
- @entities/people/morpphhhaw.md — bot author
- @sources/trading-posts-compilation-25-2026-05-27.md — K72 Post 16 (@the_smart_ape)
- @entities/tools/hl-funding-sniper.md — open-source HL funding monitor reference
- @entities/people/the-smart-ape.md
- @concepts/pnl-attribution-versioning.md — partial-fill reconciliation shares failure family with versioned PnL attribution
- @concepts/production-trading-blind-spots.md — row 6 one-leg-open hedge break

## Raw Concept

What prompted this page: K55 Posts.docx Post 1 (@morpphhhaw) — a working operator's first-principles description of how to capture perpetual-futures funding spreads across DEX venues with a delta-neutral hedge. Documents the specific architectural choices that distinguish a viable funding-carry bot from a "complicated way to lose money."

## Narrative

### The mechanism

Perpetual futures pay/receive **funding** between longs and shorts to anchor the perp price to spot/index. When the perp trades above index, longs pay shorts; when below, shorts pay longs. Funding pays on a venue-defined schedule (typically 1h or 8h).

**The structural opportunity**: funding rates differ across venues. If Venue A pays +0.01%/8h to shorts (longs in surplus) while Venue B pays +0.005%/8h to longs (shorts in surplus), a position that is **short on A** + **long on B** earns funding on both sides and is **delta-neutral** to the underlying asset's price.

The bot is **not** trying to predict BTC, ETH, or any altcoin direction. It's hunting funding regimes that pay positive net carry on both legs after costs, with a hedge that cancels the directional exposure.

### Strategy filters — "volatility-adjusted funding carry"

Simply buying the highest funding-paying venue is naïve and gets eaten by:
- Funding rates that flip within minutes after entry.
- Thin order books where spread + slippage destroy the carry.
- Unbalanced hedges where one leg is larger than the other.

Five filters define a usable signal:

1. **Funding spread** — net carry (Venue A funding − Venue B funding) after estimated round-trip costs (open + close + funding-payment friction).
2. **Stability** — penalize opportunities that appear briefly and disappear quickly. The signal must persist long enough that the cycle's cost is amortized over multiple funding payments.
3. **Liquidity + min size** — both venues must absorb the position size without significant slippage; reject if expected edge < spread + slippage.
4. **Position symmetry** — long and short legs must be matched in size. Asymmetric hedge becomes a naked directional position, not funding carry.
5. **Rotation threshold** — only rotate to a different market when the new opportunity is meaningfully better OR the current one breaks the entry filters. Don't churn on small improvements.

Author's framing: the result "behaves less like a high-frequency arb bot and more like a slow allocator between funding regimes." Cycle frequency is **15 minutes**, not seconds. Funding is paid on a schedule and many regimes don't require fast reaction.

### Live-loop logic

```
LOOP every 15 minutes:
  fetch all market/funding data across venues
  rank candidate cross-venue hedged opportunities
  check account balances + risk limits
  if no open position:
    enter best valid regime
  if position open:
    decide hold / exit / rotate
    if rotate: close both legs first, THEN open new pair
  record decision; update local state
```

### Risk architecture — "the most important part of the system"

The author is explicit: entry logic is not the hard part. **What happens when something goes wrong** is the hard part. Eight safety gates fire before any real order:

1. Explicit live-confirmation phrase before real orders (prevents accidental wire-up).
2. **Reduce-only close commands** (closing position cannot accidentally open a new one).
3. Leverage cap.
4. Minimum balance check.
5. Minimum hold period.
6. Local DB of active positions (source-of-truth for reconciliation).
7. Event log per allocator cycle.
8. Emergency manual flatten command.

**The dominant failure mode** for cross-venue market-neutral perps strategies is **one leg opens, the other doesn't**. The moment that happens, the strategy is no longer market-neutral — it's a naked long or short with full directional exposure. The bot treats execution errors as **first-class events** requiring active reconciliation:
- Live position fetch from each venue (not relying on bot-internal state).
- Close partial fills if needed.
- Never assume bot state matches exchange state.

This pattern is identical to the @0x_Punisher / @Gustafssonkotte / @adiix_official Polymarket-bot lessons in `@concepts/polymarket-bot-architecture.md` — "phantom WIN" failures and orphan-order management are the same class of bug. Cross-domain confirmation that **infrastructure > strategy** for any production trading bot.

### Live test results (4 closed positions, ~17.2 position-hours)

```
Closed positions: 4
Net PnL: +0.059237 USDC
Funding PnL: +0.057067 USDC      ← ~96% of net
Price PnL:   +0.002170 USDC
Return on quote size: ~0.0370%
Annualized run-rate (point estimate): ~18.9% APR
```

**The interpretive point**: dollar amount is too small to matter (tiny size; the goal was process verification, not yield). What matters is the **composition of PnL** — funding PnL dominated price PnL ~26:1. Confirms the hedge is doing its job: profit came from carry, not from price luck.

**The annualized number is a point estimate from n=4. Do not treat as expected return.** A more serious evaluation needs:
- Several days of continuous data.
- 10-20 closed positions minimum.
- Sensitivity analysis to funding-rate regime changes (current regimes will disappear).

### Failure modes seen in the live test

- **Positions with positive funding still closed negative** when price/basis movement outweighed funding earned. "Market-neutral" ≠ "risk-free" — different venues mark prices differently; fills happen at slightly different levels; closing both legs introduces friction. Basis risk is real.
- **API session-token expiry mid-loop**: bot couldn't read positions or send orders for an extended window. Session refresh + credential-rotation must be first-class.
- **Position discovery gap**: some on-exchange positions appeared in raw fetch but weren't picked up by the normal close command. Solution was an explicit reduce-only close-by-symbol+size command, bypassing the position-detection layer.

### Why this is in the wiki

This isn't a Polymarket strategy — it's a crypto-perpetuals strategy that **doesn't currently fit Cemini's stack** (no perp DEX adapters today). Recorded because:

1. **The architecture is portable**. Every safety gate, reconciler, and failure-mode lesson maps onto how any Cemini market-neutral strategy should be built — including any future cross-venue strategy on Polymarket+Kalshi or on Polymarket+Hyperliquid.
2. **Funding-carry is a real adjacent yield surface**. If Cemini eventually adds perpetual-DEX adapters (Hyperliquid, dYdX, GMX), this concept page documents a vetted strategy template to build against.
3. **Counterpoint to the LP-rewards-farming concept** (also K55) — both are yield strategies, both are market-neutral-ish, both are "edge in the plumbing not the algorithm," but the source of yield is structurally different (Polymarket-pool subsidy vs cross-venue funding-rate divergence).

### Cemini fit (current)

- **Out of scope today**: no perp-DEX adapters; no cross-venue execution layer beyond Polymarket+Kalshi.
- **In scope as a portable lesson**: the failure-mode taxonomy + reconciliation patterns generalize.
- **Conditional-future Adopt**: if/when a Hyperliquid or GMX adapter is added to the stack, this concept page is the strategy-blueprint.

## Snippets

> "Most traders look at funding as a small operational detail. For automated strategies, though, funding can become the main signal." [Source: Posts.docx — Post 1, @morpphhhaw]

> "A trading bot with a clever strategy and weak execution is just a complicated way to lose money." [Source: Posts.docx — Post 1, @morpphhhaw]

> "The result is a strategy that behaves less like a high-frequency arbitrage bot and more like a slow allocator between funding regimes." [Source: Posts.docx — Post 1, @morpphhhaw]

> "The most important part of the system is not the entry logic. It is what happens when something goes wrong." [Source: Posts.docx — Post 1, @morpphhhaw]

> "Funding PnL was positive and represented almost all of the net result. Price PnL was close to flat. That is exactly what a funding carry strategy wants to see." [Source: Posts.docx — Post 1, @morpphhhaw]
