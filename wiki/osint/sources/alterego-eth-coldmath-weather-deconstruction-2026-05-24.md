---
title: "@AlterEgo_eth — ColdMath Polymarket weather deconstruction (narrow bins + micro-scaling)"
type: source
tags: [source, trading-posts, polymarket, weather-trading, coldmath, adversary-model, k61]
keywords: [alteregoeth, coldmath, parity, narrow-bins, micro-scaling, metar, bias-correction, singapore, kuala-lumpur, houston, k61]
related:
  - entities/people/alteregoeth.md
  - entities/people/coldmath-polymarket.md
  - entities/people/polymarketsuccubus.md
  - entities/tools/parity-polymarket-analytics.md
  - entities/tools/clawdbot.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/polymarket-bot-architecture.md
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
maturity: validated
read_status: deep-read
created: 2026-05-24
updated: 2026-05-24
clusters: [polymarket, weather-trading]
---

## Relations

- @entities/people/alteregoeth.md — author (fifth ingested artifact; operator forensics, not API mechanics)
- @entities/people/coldmath-polymarket.md — subject wallet/operator
- @entities/people/polymarketsuccubus.md — K55 Top-7 ranking author (#1 ColdMath)
- @entities/tools/parity-polymarket-analytics.md — claimed data source (1,200+ recent trades)
- @entities/tools/clawdbot.md — K55 framework attribution for ColdMath stack
- @concepts/polymarket-weather-trading-strategy.md — adds micro-scaling + ultra-narrow bin adversary patterns
- @concepts/polymarket-bot-architecture.md — execution discipline corroboration
- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — K55 Top-7 baseline

## Raw Concept

- **Title**: How ColdMath Dominates Polymarket Weather Markets (Narrow 1°C Bins + Aggressive Scaling + Multi-Model Bias Correction)
- **Author**: @AlterEgo_eth (X)
- **Type**: long-form X post / thread export
- **Location**: `research to be indexed/@AlterEgo_eth.docx` → `cemini-librarian:/opt/cemini-bulk/research/@AlterEgo_eth.docx`
- **Retrieved**: 2026-05-24
- **Read status**: deep-read

## Narrative

@AlterEgo_eth reverse-engineered **ColdMath** using **Parity** trade history (>1,200 recent trades). The post argues apparent randomness is a **disciplined automated system** — not raw ECMWF pulls.

### Four observable behaviors

1. **Ultra-narrow bins** — precise 1°C (or tight range) markets, e.g. Singapore 34°C, Kuala Lumpur 29°C, Houston 70–71°F. Profit requires high forecast precision, not broad “warmer than average” bets.

2. **Micro-scaling (scaling in)** — dozens of entries on the **same outcome** at $0.01–$50 (up to $100–200), e.g. 8–10 buys at 7, 10, 16, 46, 115, 290 shares in one day. Goals: limit slippage, average entry, stop adding if forecast shifts.

3. **High automation volume** — tens to hundreds of trades/day → full bot, not discretionary clicks.

4. **Deep OOM / 1¢ Yes-No building** — large size on very cheap contracts after adjusted probability — aligns with K55 Parity profile (entries 0.01–0.02¢, +$124K, ~81.7% WR cited there).

### Inferred stack [TENTATIVE — single-source forensics]

- Multi-model blend (not single ECMWF)
- **City + horizon bias correction**
- **Dynamic model weights** from recent performance
- Real-time obs emphasis (**METAR**, etc.)
- Author claim: ~**63–65% win rate** still “outstanding” because edge is **price + sizing discipline**, not hit-rate alone

### Cemini relevance

- **Adversary model** for weather markets: expect **liquidity consumption via micro-lots** on narrow bins, not one-shot size.
- **Forecast bar** for competing on 1°C bins is higher than coarse threshold markets — ties to ensemble + station-coordinate work on @concepts/polymarket-weather-trading-strategy.md.
- **Parity** (or in-house wallet forensics) as tooling to monitor top weather wallets — second independent use after K55 @polysuccubus rankings.
- Does **not** replace @alteregoeth-ai/weatherbot as open-source reference — this is competitive intelligence, not API docs.
- **Wallet resolved (2026-05-24):** @entities/people/coldmath-polymarket.md → `0x594edb9112f526fa6a80b8f858a6379c8a2c1c11` (`polymarket.com/@coldmath`).

## Snippets

> "Consistently profiting from such narrow outcomes is only possible with very high forecast accuracy." [Source: @AlterEgo_eth.docx, 2026-05-24]

> "Entering the same outcome dozens of times with small amounts ($0.01 to $10–50… minimizing slippage, averaging entry price." [Source: same]

> "ColdMath is not just 'a bot that pulls ECMWF' — multiple forecast sources, bias correction, extremely disciplined position management through micro-scaling." [Source: same]
