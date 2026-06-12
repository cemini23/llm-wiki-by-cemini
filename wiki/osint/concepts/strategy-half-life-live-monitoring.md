---
title: Strategy half-life — live decay monitoring for quant desks
type: concept
tags: [concept, quant-finance, strategy-ops, decay, backtest, k112]
keywords: [strategy-half-life, edge-decay, post-publication, live-monitoring, horizon-trade]
related:
  - sources/trading-posts-compilation-9-2026-06-12.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/instrumental-probability-learnable-alpha.md
maturity: draft
created: 2026-06-12
updated: 2026-06-12
---

## Relations

- @sources/trading-posts-compilation-9-2026-06-12.md — @horizon_trade_x Post 2
- @concepts/regime-conditioned-evaluation.md — regime shift vs strategy decay
- @concepts/monte-carlo-permutation-test-mcpt.md — promotion gate before live capital

## Raw Concept

K112 Posts.docx — operational framework for detecting strategy death before drawdown realizes.

## Narrative

Empirical anchor: **97 published strategies** averaged **−58% edge** after publication (2016 finance professors study) `[TENTATIVE — cited via @horizon_trade_x; primary paper not ingested]`.

Desk practice: weekly tracking of four metrics separating **routine variance** from **structural decay**; three kill forces (only one survivable via re-tune). Horizon.trade markets plain-English strategy → backtest → live deploy (closed beta) `[REFERENCE — not evaluated]`.

**Cemini mapping:** Pair with quarterly backtest cadences (PM LP, equity signal) — add **live half-life review** ritual before promoting new conviction or LP tiers. No code adoption in K112.

## Snippets

> "Every strategy has a half-life."

> — [Source: trading-posts-compilation-9-2026-06-12.docx Post 2 @horizon_trade_x, retrieved 2026-06-12]
