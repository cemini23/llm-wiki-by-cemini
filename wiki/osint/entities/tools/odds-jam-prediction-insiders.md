---
title: Odds Jam — Prediction Insiders (Polymarket copy alerts)
type: entity
tags: [entity, tool, polymarket, copy-trading, odds-jam, k80]
keywords: [odds-jam, prediction-insiders, alex-monahan, copy-alerts, smart-money]
related:
  - sources/youtube-polymarket-bots-batch-2026-05-29.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/polymarket-wallet-alpha-pipeline.md
  - entities/people/alex-monahan.md
  - concepts/gambling-wiki-federation.md
maturity: draft
created: 2026-05-29
updated: 2026-05-31
---

## Relations

- @sources/youtube-polymarket-bots-batch-2026-05-29.md — Financial Wolf 30-day experiment (2026-05-19)
- @concepts/polymarket-copy-trading-strategy.md — copy-trading discipline + latency arms race
- @concepts/polymarket-wallet-alpha-pipeline.md — wallet signal ingestion patterns

## Raw Concept

What prompted this page: YouTube *I Used a Polymarket Insider Trading Bot for 30 Days* (Financial Wolf, 2026-05-19) — **Prediction Insiders** product inside Odds Jam surfacing trades from high-ROI Polymarket wallets with one-click copy sizing.

## Narrative

**Prediction Insiders** (Odds Jam) [TENTATIVE]: alert feed of profitable Polymarket bettors; bankroll-aware sizing suggestions; marketing claims ~481% / 30-day product stats.

### Financial Wolf 30-day experiment ($1,000 start) [TENTATIVE]

| Phase | Observation |
|-------|-------------|
| Week 1 | ~13% portfolio gain; heavy trade count |
| Mid-challenge | Drawdown to ~$740; **54% win rate** vs marketed ~65% |
| Day 30 | ~**$224 profit** on ~$7.5K wagered vs ~$187 expected loss at 2.5% fee drag; total bankroll ~$1,698 including **+$474** from casino bonuses / +EV arb (non-PM) |
| Filter tweak | Later trades ranked >80 confidence only |

**Takeaway for Cemini:** modest edge possible vs random after fees, but **underperforms marketed bot stats**; variance + over-trading risk. Complements @concepts/polymarket-copy-trading-strategy.md hedge-leg and 3-month track-record rules.

Founder context: Alex Monahan (Stanford, ex-quant, sold Odds Jam ~$160M cited in video).

### Cemini relevance

- **Reference / competitive intel** — not prod adoption; use experiment as calibration for copy-trading ROI expectations.
- Contrast with on-chain wallet pipeline (@concepts/polymarket-wallet-alpha-pipeline.md) for lower-latency DIY path.

## Snippets

> "375 trades placed so far, our win rate is only 54%." [Source: https://www.youtube.com/watch?v=gSGI82Ej76M (retrieved 2026-05-29)]

> "We profited $224.10 … marking a 22% gain versus an 18.7% expected loss if we just randomly place bets." [Source: https://www.youtube.com/watch?v=gSGI82Ej76M (retrieved 2026-05-29)]
