---
title: Polymarket Tracker Ecosystem — predictparity / Parity / PredictFolio / PolyWallet
type: entity
tags: [tool, prediction-market, polymarket, wallet-tracker, leaderboard, alpha-source, saas, candidate-data-source]
keywords: [predictparity, parity, predictfolio, polywallet, polymarket-pnl-tracker, wallet-leaderboard, smart-money-following, prediction-market-analytics]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/prediction-market-historical-analysis.md
  - entities/tools/polymarket-agents.md
  - entities/tools/polymarket-python-order-utils.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 13 (`predictparity.com/traders/p/@amisrael123`), originally marked **UNAVAILABLE** at eval time, Exa-resolved 2026-05-06 with the broader Polymarket-tracker landscape
- @concepts/prediction-market-historical-analysis.md — Polymarket tracker SaaS fits the broad prediction-market scope (per memory `prediction_market_scope.md`); these trackers complement historical-analysis with live wallet-flow data
- @entities/tools/polymarket-agents.md — Cemini's existing Polymarket agent stack; trackers are candidate **data sources** for "follow the smart wallets" alpha overlay
- @entities/tools/polymarket-python-order-utils.md — companion Polymarket SDK already adopted

## Raw Concept

Three SaaS products surfaced via Exa-rescue of K32 URL 13 (`predictparity.com`). All three monitor Polymarket trader P&L, leaderboards, and wallet flows — operationally distinct from the SDK/agent stack Cemini deploys.

These are **candidate data feeds**, not adoption candidates (Cemini does not run third-party SaaS in production). Documented for the Polymarket alpha-overlay design space.

## Narrative

### Three products in the ecosystem

| Product | URL | Verified | Notes |
|---------|-----|----------|-------|
| **Parity** (predictparity) | `https://predictparity.com/` | ✓ Exa 2026-05-06 (login wall) | Original DR-flagged URL `predictparity.com/traders/p/@amisrael123` requires auth. The site is rebranded "Parity" |
| **PredictFolio** | `https://predictfolio.com/` | ✓ Exa 2026-05-06 | Public leaderboard, search, community PnL. Reports $5B traded volume across 2.4M traders, 210k markets. "Poly Alpha Discord" community angle |
| **PolyWallet** | `https://polywallet.app/` | ✓ Exa 2026-05-06 | Wallet-tracker w/ live PnL, 30s refresh on Premium / 5min Free. Free tier: 5 wallets. Premium tier: 500 wallets, CSV export, live PnL tracking |

### What they offer (consolidated feature set)

- **Wallet tracking**: monitor any Polymarket wallet's positions, trades, balances
- **PnL analytics**: daily/weekly/monthly breakdowns; calendar heatmaps; realized vs unrealized
- **Leaderboard / Market Scout**: discover top-performing wallets by PnL/win-rate
- **Trade history export**: CSV (PolyWallet Premium)
- **Live price refresh**: 30-second refresh interval on premium tier; real-time PnL on open positions
- **Community signals**: PredictFolio integrates a Discord-driven "Poly Alpha" community for trader discovery

### Why interesting for Cemini

If Cemini runs Polymarket-side strategies (per active K30 brief `cemini-prod:/opt/cemini/briefs/2026-05-05_polymarket-stack-adoption.md`), there are two distinct alpha-overlay angles:

**Angle 1: "Follow the smart wallets"** — track top-PnL wallets identified by these services, mirror their position changes (on a delay or with risk filters). Strategy is well-known in crypto markets ("alpha follow"); applicability to prediction markets depends on how many of those wallets persist edge across markets vs ride one big bet to glory.

**Angle 2: "Avoid the dumb wallets"** — per the MEXC News summary cited in DR (`https://www.mexc.com/news/1012457` retrieved indirectly), 69% of historical Polymarket traders are unprofitable. Identifying chronic-loser wallets and **fading their positions** could be a contrarian alpha source.

Both angles require **wallet-state data**, which is on-chain and accessible via Polymarket's public APIs directly — these SaaS services are convenient front-ends but not strictly necessary. Cemini could replicate the analytical layer in-house.

### Why they're not adoption candidates (yet)

- **SaaS, not libraries**: cannot embed in `cemini-prod` stack
- **Free tier limits**: PolyWallet free is 5 wallets / 5min refresh — too narrow for systematic strategy backtest
- **Premium pricing not surfaced**: would require user signup to evaluate cost vs value
- **License posture irrelevant**: these are services, not code we'd deploy
- **Vendor risk**: small SaaS, single-maintainer plausible — cannot bet production strategy on uptime

### What Cemini could build instead

If a "follow smart wallets" strategy crystallizes from research, build the wallet-tracker layer in-house:

1. Pull Polymarket on-chain transaction history for top-N wallets (identified externally, e.g., via PredictFolio's free leaderboard scraped manually)
2. Stream new positions / liquidations / closes via Polymarket subgraph or `py-clob-client` (already in K30 brief)
3. Apply alpha-follow logic in `cemini-prod` orchestrator: when wallet X opens position Y above threshold T, trigger Cemini's mirror trade with sized-down exposure
4. Use PredictFolio/PolyWallet only for **manual research** (find top wallets to track) — not as a runtime dependency

### Open questions

- ⚠ How does PredictFolio's leaderboard rank wallets? (return-based? Sharpe? consistency?)
- ⚠ Does PolyWallet expose an API tier above its UI?
- ⚠ Does Parity (rebranded predictparity) have a public leaderboard or is everything behind login?
- ⚠ What's the regulatory frame for "follow the smart wallets" on Polymarket from a US-resident perspective?

### Adoption status — NOT ADOPTED

These are SaaS services, NOT libraries. Cemini does not adopt them. Documented as candidate **research-time data sources** for designing Polymarket alpha overlays.

## Snippets

### PredictFolio scope claim

> "Polymarket Analytics by PredictFolio. Discover traders, analyze Polymarket data, compare strategies, and research markets. Traders 2,413,137 / Markets 210,860 / Volume $5B." [Source: https://predictfolio.com/ (retrieved 2026-05-06)]

### PolyWallet feature framing

> "PolyWallet is a portfolio tracker for Polymarket — the leading prediction market. You can track any wallet address, view PnL analytics, and scout top traders. ... Real-time unrealized PnL updates using live market prices. Watch your open positions move tick by tick." [Source: https://polywallet.app/ (retrieved 2026-05-06)]

### Polymarket trader profitability (DR-cited statistic)

> "Contextual research indicates that PredictParity is an analytics platform dedicated to tracking historical profit and loss (P&L) distributions on prediction markets like Polymarket, revealing that **69% of historical traders are unprofitable**." [Source: 5_6 links.docx URL 13 citing https://www.mexc.com/news/1012457 (retrieved 2026-05-06)]

This statistic, if accurate, frames the alpha-overlay design space: a coin-flip distribution would put unprofitability at 50%; 69% suggests a meaningful structural edge for systematic players (and a contrarian opportunity for fading the chronic losers).
