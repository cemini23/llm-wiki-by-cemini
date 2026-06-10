---
title: Sequential optimal execution quoting (signal-adaptive LOB)
type: concept
tags: [concept, quant-finance, market-microstructure, execution]
keywords: [optimal quoting, limit order book, inventory risk, CARA, metaorder]
related:
  - sources/arxiv-signal-adaptive-execution-2605-24242-2026-06-01.md
  - sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md
  - concepts/market-microstructure.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/polymarket-microstructure-findings.md
maturity: draft
created: 2026-06-01
updated: 2026-06-10
---

## Relations

- @sources/arxiv-signal-adaptive-execution-2605-24242-2026-06-01.md — K92 ingest
- @sources/arxiv-tt-dac-ps-optimal-execution-2606.08379-2026-06-10.md — K110 RL execution (TT-DAC-PS, IS% benchmarks vs TWAP/VWAP/AC)

## Raw Concept

K92 arXiv 2605.24242 — explicit LOB quoting theory bridging scheduling and placement.

## Narrative

Integrates **metaorder horizon** with **per-child limit-order quotes** under signal-dependent drift, price impact, inventory penalty, and fill risk (Poisson intensities tied to quotes). Yu (2026) gives **closed-form** solutions across four objective classes — useful reference when tuning PM/Kalshi quoters (inventory skew vs signal, aggression vs fill rate).

Cross-link gambling/OSINT bot quoter steal-from: @gambling-wiki/entities/bots/wagerbrain.md (eval K92) and world-cup-bot conviction/quoter modules on @osint-wiki.

K110 adds **empirical RL execution** (TT-DAC-PS): twin-target TD3-style critic + adaptive OU exploration on equity LOB; beats PPO/A2C and classical schedules in high-vol names (AVGO, ADBE). Steal **IS% + CI reporting** and **regime-conditioned aggression** insight — not the equity-specific env without PM validation.

## Snippets

> "Explicit formulas reveal … signal-dependent drift can substantially affect optimal execution." [Source: arxiv-2605.24242, Abstract]
