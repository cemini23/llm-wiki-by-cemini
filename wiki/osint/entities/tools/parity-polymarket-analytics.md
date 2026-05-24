---
title: "Parity — Polymarket counterparty-intel + analytics platform"
type: entity
tags: [entity, tool, polymarket, analytics-platform, counterparty-intel, orderbook-insights, k55]
keywords: [parity, parity-polymarket, counterparty-intelligence, orderbook-insights, trader-profile-analytics, real-time-analytics-polymarket, polymarket-with-parity, polymarketsuccubus-affiliate]
related:
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/platforms/polymarket.md
  - entities/people/polymarketsuccubus.md
  - sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md
  - entities/people/coldmath-polymarket.md
maturity: draft
created: 2026-05-20
updated: 2026-05-24
---

## Relations

- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — K55 Posts.docx Post 5 prominently uses Parity for trader profiles
- @concepts/polymarket-weather-trading-strategy.md — trader-profile data referenced in concept page
- @entities/platforms/polymarket.md — venue
- @entities/people/polymarketsuccubus.md — primary creator using the platform's affiliate funnel
- @sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md — K61: >1,200 ColdMath trades analyzed via Parity
- @entities/people/coldmath-polymarket.md — subject wallet profile

## Raw Concept

Third-party analytics platform for Polymarket traders providing counterparty intelligence (who you're trading against), trader-profile aggregation (PnL, win rate, trade history per wallet), and orderbook flow insights. Referenced extensively in the @polysuccubus K55 ingest as the data source behind the Top-7 weather-trader rankings.

## Narrative

### Pitched feature surface (from @polysuccubus Post 5 footers)

> "*Polymarket with Parity exists to give you real edge in prediction markets. Our platform shows you who you're trading against, where top wallets are positioning, and how smart money is flowing. In the world of prediction markets, every dollar counts. Parity gives you counterparty intelligence and orderbook insights that no one else offers.*"

### Surface area

- **Trader profiles**: PnL, total gains, total losses, win rate, biggest single win, total predictions per wallet.
- **Trade history**: per-trader, per-market — invested amount → payout → profit/percent-return for individual positions.
- **Counterparty intel**: "who you're trading against."
- **Orderbook insights**: flow + positioning analytics.
- **Real-time analytics** with "Sign Up with email or wallet for full access" gating.

### Access model [NEEDS VERIFICATION 2026-05-20]

- Sign-up required for "full access to real-time analytics."
- Freemium suggested by the framing (some data public, more behind login).
- Pricing structure not disclosed in the K55 ingest source — likely tiered.

### Cemini relevance

- **Read-only intel layer**, not an execution surface.
- **Worth Phase-0 audit** as a complement to existing Polymarket data sources (Gamma API + CLOB + Bridge + LB) if it offers material counterparty-intel data the public APIs don't.
- **Affiliate funnel concern**: @polysuccubus actively promotes Parity in posts; the Top-7 rankings themselves are observable on-chain, but the *aggregation + presentation* is Parity-fronted.

### Open questions

1. Is Parity public-data aggregation only, or does it have data sources (e.g. dealer-side orderbook insights) the public APIs lack?
2. What's the pricing structure?
3. Is there a programmatic API, or is it UI-only?
4. Is the same intelligence buildable from Cemini's existing Polymarket data adapters + ArcticDB?

### Cemini fit

- **Defer**. Recorded as a known third-party analytics surface to evaluate later if Cemini's internal counterparty-intel needs cannot be met from existing data sources.

### Caveats

- "No one else offers" is marketing language — most of what Parity presents (trader profiles, PnL, trade history) is on-chain-derivable via Polygon blockchain queries. The value Parity adds is presentation + aggregation, not (necessarily) proprietary data.
- @polysuccubus affiliate relationship means his content is a biased information source about Parity's actual capabilities.
