---
title: ColdMath — Polymarket weather trader (#1 ranked, micro-scaling)
type: entity
tags: [entity, person, polymarket, weather-trading, adversary, k55, k61]
keywords: [coldmath, polymarket-weather, clawdbot, micro-scaling, narrow-bins, parity, pilot-aviation]
related:
  - sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - entities/tools/clawdbot.md
  - entities/tools/parity-polymarket-analytics.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/people/polymarketsuccubus.md
  - entities/people/alteregoeth.md
  - concepts/polymarket-bot-architecture.md
maturity: draft
created: 2026-05-24
updated: 2026-05-24
---

## Relations

- @sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md — K61 @AlterEgo_eth forensics (>1,200 trades via Parity)
- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — K55 @polysuccubus Top-7 #1 (+$124,896, 81.7% WR)
- @entities/tools/clawdbot.md — attributed automation framework [NEEDS VERIFICATION 2026-05-20]
- @entities/tools/parity-polymarket-analytics.md — trade-history aggregation surface
- @concepts/polymarket-weather-trading-strategy.md — operational patterns (narrow bins, micro-scaling)
- @entities/people/alteregoeth.md — K61 analyst (not the operator)
- @concepts/polymarket-bot-architecture.md — micro-scaling adversary execution pattern

## Raw Concept

Polymarket weather-market operator ranked **#1** in K55 Top-7 (@polysuccubus). K61 adds @AlterEgo_eth trade-level deconstruction via Parity.

## Narrative

### Reported stats [TENTATIVE — promotional / aggregated sources]

| Source | PnL | Win rate | Notes |
|--------|-----|----------|-------|
| K55 @polysuccubus | +$124,896 | 81.7% | 6,575 predictions; entries 0.01–0.02¢; Clawdbot + pilot aviation feeds |
| K61 @AlterEgo_eth | — | ~63–65% | Outstanding results despite “average” WR — edge = narrow bins + sizing |

Discrepancy may be sample window, market subset, or marketing vs forensics — treat both as **[TENTATIVE]** until wallet-level Cemini replay.

### K61 operational fingerprint (@AlterEgo_eth)

- **Ultra-narrow bins** (1°C / tight ranges) — SG, KL, Houston examples
- **Micro-scaling** — many small buys same outcome ($0.01–$200)
- **High frequency** — full automation
- **1¢ tail building** after bias-corrected probability
- Inferred: multi-model + city/horizon bias correction + dynamic weights + METAR

### Cemini posture

- **Primary adversary reference** for weather PM execution design (liquidity, bin selection, forecast precision).
- **Do not Adopt** Clawdbot on K55 mention alone — see @entities/tools/clawdbot.md Phase-0 backlog.
- Wallet address not in ingested docx — resolve via Parity or on-chain index for backtests.

## Snippets

> "He made 8–10 separate buys in the same market at 7, 10, 16, 46, 115, and 290 shares." [Source: @AlterEgo_eth.docx via @sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md]
