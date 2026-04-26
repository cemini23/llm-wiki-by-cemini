---
title: Market-Adaptive Ratio for Portfolio Management
type: source
tags: [pdf, portfolio-strategy, risk-adjusted-returns, sharpe, sortino, bull-bear, risk-metric]
clusters: [portfolio-strategy]
related:
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- **Original title**: Market-Adaptive Ratio for Portfolio Management
- **Author(s)**: Ju-Hong Lee, Bayartsetseg Kalina, Kwang-Tek Na
- **Affiliation**: Unspecified in metadata captured
- **Type**: PDF
- **Length**: 13p
- **Location**: research for cemini/sortino 3 4:3.pdf
- **Retrieved**: 2026-04-23
- **Read status**: read-skim (preview + title only)
- **Primary cluster**: portfolio-strategy
- **All clusters**: portfolio-strategy

## Narrative

Short academic paper proposing a new risk-adjusted return ratio ("Market-Adaptive Ratio") that explicitly accounts for bull/bear regime differences. Preview critique is standard: Treynor/Sharpe/Sortino/Information ratios treat all market states uniformly and miss the distinct behavior of bull vs bear regimes, leading to sub-optimal allocation. The proposed ratio adapts to the market state — mechanism unspecified in the preview.

Honest assessment: 13 pages is short for a methodology paper, appropriate for a single-ratio proposal. The literature on regime-aware risk metrics is crowded, and the usual risk is that a "market-adaptive" ratio fits noise in the regime-classification step. The method's practical value depends entirely on how robust the regime classification is OOS — this is the typical failure mode.

Relevance to Cemini: potentially useful as a candidate evaluation metric for regime-aware strategies. Cemini's watchlist spans equities (regime-sensitive) and crypto (regime-distinct from equities), so a single scalar that collapses bull/bear behavior is worth considering. Should be tested against standard Sharpe/Sortino in walk-forward before adoption.

## Key findings

- Proposes a single risk-adjusted ratio that varies with bull/bear regime.
- Critique of standard ratios (Sharpe/Sortino/Treynor/Information): regime-blind.
- Short methodology paper (13p).
- Authors Korean/Mongolian affiliation suggested by author names; full affiliation not captured.

## Snippets

- **p.1** — "Traditional risk-adjusted returns, such as the Treynor, Sharpe, Sortino, and Information ratios, have been pivotal in portfolio asset allocation, focusing on minimizing risk while maximizing profit. Nevertheless, these metrics often fail to account for the distinct characteristics of bull and bear markets, leading to sub-optimal investment decisions." — Motivates the regime-aware framing.
