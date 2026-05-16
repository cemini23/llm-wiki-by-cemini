---
title: The Three-Dimensional Decomposition of Volatility Memory (Wang, Trindade & Rachev 2025)
type: source
tags: [pdf, options-derivatives, volatility, garch, time-series]
keywords: [volatility memory, level shape tempo, GARCH, FIGARCH, regime switching, business time, RSM, G-FIGARCH, G-Clock, TG-Vol, QMLE, Whittle, VaR, SPY, EURUSD]
related:
  - concepts/options-derivatives.md
  - concepts/quant-finance.md
  - entities/tickers/spy.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/options-derivatives.md — Options & Derivatives corpus-index hub (Q 2026-04-27)
- @concepts/quant-finance.md — volatility forecasting / regime detection / VaR-CVaR risk measures cluster; this paper is core volatility-modeling material
- @entities/tickers/spy.md — SPY is one of the two empirical testbeds (2005-2024); regime + tempo gates dominate equity tail-risk timing

## Raw Concept

- **Original title**: The Three-Dimensional Decomposition of Volatility Memory
- **Author(s)**: Ziyao Wang, A. Alexandre Trindade, Svetlozar T. Rachev (Texas Tech University)
- **Type**: PDF (arXiv:2512.02166v1 [q-fin.MF], 1 Dec 2025)
- **Location**: research for cemini/The Three-Dimensional Decomposition of Volatility Memory.pdf
- **Retrieved**: 2026-04-27
- **Length**: 55p
- **Read status**: deep-read
- **Cluster**: options-derivatives

## Narrative

This paper develops a **canonical decomposition of volatility memory** into three orthogonal components — **level (M)**, **tempo (µ)**, and **shape (g)** — and proves that every admissible volatility memory kernel factorizes uniquely as `f(u) = M·µ⁻¹·g(u/µ)`. The decomposition unifies three previously disjoint literatures: regime-switching / smooth-transition GARCH (level), fractional integration / FIGARCH long memory (shape), and business-time / stochastic-clock models (tempo).

**Theory.** The authors establish existence, uniqueness, and a frequency-domain orthogonality result: level rescales the spectrum vertically, tempo dilates the frequency axis, and the low-frequency slope (long-memory strength) depends *only* on the shape. They prove the framework is a **universal envelope** — all GARCH-family models (GARCH(1,1), IGARCH, FIGARCH, HYGARCH, GJR-GARCH, MS-GARCH) arise as restrictions on (M, µ, g). Three observable-gated models operationalize each dimension: **RSM** (logistic gate on persistence level), **G-FIGARCH** (state-dependent fractional order), and **G-Clock** (business-time deformation), with a fully unified **TG-Vol** tri-gate model. Positivity, finite-moment, and geometric-ergodicity conditions are proven; QMLE is consistent and asymptotically normal, with Whittle-regularization for the fractional component.

**Empirical findings.** Tested on SPY and EUR/USD daily data (2005-2024) against GARCH/EGARCH/GJR baselines: volatility memory is **state-dependent and market-specific**. On EUR/USD the long-memory shape gate (G-FIGARCH) dominates variance forecasting (lowest QLIKE/RMSE, DM p=0.004). On SPY the regime and tempo gates (RSM, G-Clock) deliver superior tail-risk timing — G-Clock posts the best FZ(5%) score — while G-FIGARCH is numerically fragile at the daily horizon due to lack of intraday realized variance. Crises raise persistence and fractional-memory gates while compressing business-time speed.

**Relevance to Cemini.** Gives a rigorous, interpretable volatility-regime model whose gates are observable features (realized variance, VIX, volume, |return|) — directly compatible with an RL state vector and with regime-conditioned position sizing. The proposed "memory-thickening index" (E[M+d]) is pitched as an early-warning systemic-stress indicator complementary to financial-conditions indices.

## Snippets

> "This paper develops a three-dimensional decomposition of volatility memory into orthogonal components of level, shape, and tempo... We establish conditions for existence, uniqueness, and ergodicity of this decomposition and show that all GARCH-type processes arise as special cases."
> [Source: The Three-Dimensional Decomposition of Volatility Memory.pdf p.1]

> "Sf(λ) = M² Sg(µλ) ... 1. Level M produces a pure vertical rescaling of the spectrum; 2. Tempo µ dilates the frequency axis (horizontal rescaling); 3. ... the low-frequency slope is a shape property only."
> [Source: The Three-Dimensional Decomposition of Volatility Memory.pdf p.7]

> "On EURUSD, the long-memory gate (G-FIGARCH) dominates variance forecasting, while on SPY the regime and clock gates (RSM, G-Clock) deliver superior tail-risk timing. Across markets, crises raise the persistence and fractional-memory gates while compressing the business-time speed—consistent with faster information flow during stress."
> [Source: The Three-Dimensional Decomposition of Volatility Memory.pdf p.2]
