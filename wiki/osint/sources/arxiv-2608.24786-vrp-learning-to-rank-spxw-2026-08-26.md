---
title: "VRP learning-to-rank on SPXW — Wysocki (arXiv 2608.24786)"
type: source
tags: [arxiv, options, vol, k247]
keywords: [VRP, SPXW, LightGBM, LambdaRank, zero-DTE, vol-risk-premium]
related:
  - concepts/k247-vol-options-wave.md
  - sources/arxiv-2608.22478-arbitrage-aware-iv-surfaces.md
  - sources/arxiv-2608.22620-wsvi-implied-vol-shape.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
read_status: read
---

## Relations

- @concepts/k247-vol-options-wave.md — K247 vol cluster hub
- @sources/arxiv-2608.22478-arbitrage-aware-iv-surfaces.md — sibling K246 vol surface paper
- @sources/arxiv-2608.22620-wsvi-implied-vol-shape.md — sibling K246 WSVI paper

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.24786, "Harvesting the Volatility Risk Premium: A Learning-to-Rank Approach" |
| Author | Maciej Wysocki (University of Warsaw, Quantitative Finance Research Group) |
| Retrieved | 2026-08-26 |
| File | `arxiv-2608.24786-harvesting-the-volatility-risk-premium-a-learnin.pdf` |
| sha256 | `7ddf3853c5757f2273c40ed3c24b10aad048b4e9cf13b51b627790e8c480bd08` |
| Dual-ID | **OSINT K247**. **Wiki-only** — no xsp scp. |

## Narrative

First end-to-end cross-sectional **learning-to-rank** application to S&P 500 weekly (SPXW) zero-DTE options surface. LightGBM LambdaRank scores a daily nine-strategy cross-section (eight delta-targeted short-put legs + SKIP) against a path-aware Sortino-on-bars label at one-minute resolution. Framework includes margin-aware sizing, uncertainty-driven abstention, and strict out-of-time integrity check.

Reported 2025 held-out slice: annualized Sharpe 4.31–5.76 across seven sizing methods; headline Probabilistic Sharpe Ratio 0.964; max drawdown −2.28%. Wiki-only vol research — pairs K246 IV surface papers; **no prod brief scp**.

## Snippets

> "A LightGBM LambdaRank ranker scores a daily nine-strategy cross-section … trained against a path-aware Sortino-on-bars label computed at one-minute resolution." [Source: arxiv-2608.24786-harvesting-the-volatility-risk-premium-a-learnin.pdf abstract]
