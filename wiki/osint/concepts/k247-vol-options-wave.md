---
title: K247 vol options wave (Aug 2026)
type: concept
tags: [options, vol, k247]
keywords: [VRP, SPXW, LambdaRank, zero-DTE]
related:
  - sources/arxiv-2608.24786-vrp-learning-to-rank-spxw-2026-08-26.md
  - sources/arxiv-2608.22478-arbitrage-aware-iv-surfaces.md
  - sources/arxiv-2608.22620-wsvi-implied-vol-shape.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
wire_status: wont_wire
wire_target: wiki-only
---

## Relations

- @sources/arxiv-2608.24786-vrp-learning-to-rank-spxw-2026-08-26.md — LightGBM LambdaRank SPXW VRP
- @sources/arxiv-2608.22478-arbitrage-aware-iv-surfaces.md — K246 arbitrage-aware IV
- @sources/arxiv-2608.22620-wsvi-implied-vol-shape.md — K246 WSVI family

## Raw Concept

K247 vol cluster — cross-sectional learning-to-rank for SPXW zero-DTE VRP harvest.

## Narrative

Wysocki (2608.24786) applies LambdaRank to daily SPXW short-put cross-sections with margin-aware sizing, uncertainty abstention, and strict 2025 out-of-time holdout. Sits alongside K246 IV surface papers (arbitrage-aware latent diffusion, WSVI W-shapes). **Wiki-only** — no xsp-killer scp without operator HITL.

## Snippets

> "Seven sizing methods produce out-of-time annualized Sharpe ratios between 4.31 and 5.76." [Source: @sources/arxiv-2608.24786-vrp-learning-to-rank-spxw-2026-08-26.md]
