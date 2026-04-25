---
title: "Full grid solution for multi-asset options pricing with tensor networks"
type: source
tags: [pdf, options-derivatives, quant-finance, tensor-networks, pde, black-scholes]
clusters: [options-derivatives, quant-finance]
related: []
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

*(Cross-references will be added in Phase 2.)*

## Raw Concept

- **Original title**: Full grid solution for multi-asset options pricing with tensor networks
- **Author(s)**: Lucas Arenstein, Michael Kastoryano
- **Affiliation**: Department of Computer Science, University of Copenhagen
- **Type**: PDF (arXiv:2601.00009v2, q-fin.CP)
- **Location**: research for cemini/greeks 9 3:29.pdf
- **Length**: 22p
- **Retrieved**: 2026-04-23 (download date, not publication)
- **Publication date**: 2026-02-24
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: options-derivatives, quant-finance

## Narrative

Arenstein & Kastoryano present the first tensor-network (quantized tensor train, QTT) solver that delivers full-grid solutions of the multi-asset Black–Scholes PDE beyond the classical three-asset barrier — running on a laptop. Classical finite-difference/finite-element methods scale as O(N^d), hitting the curse of dimensionality at d=3. Monte Carlo is the usual escape valve but only returns prices at specific initial states (no dense Greeks, no interpolation surface, noisy early-exercise). The authors prove that the d-asset Black–Scholes operator, payoffs, and boundary conditions admit QTT representations whose ranks scale polynomially in d and polylog in grid size N, converting exponential storage into polylog-in-N arithmetic.

Two solvers: (a) time-stepping QTT for European and American options; (b) space-time QTT that treats time as an extra dimension and solves all time layers in one shot (uniquely providing the full temporal surface). Numerical experiments in d=3,4,5 produce correlated basket and max-min option prices + dense Greeks on full grids, validated against high-accuracy references. Claims the approach can be pushed to d=10–15 with more compute.

Relevant to Cemini for options trading workflows that need dense cross-Greeks and instant re-pricing (hedging, intraday risk, calibration of entire vol surfaces) without overnight MC reruns. Honest limit: QTT rank control dominates wall-clock, and the paper does not report production-grade calibration or real market data fits — all benchmarks are on synthetic Black-Scholes baskets.

## Key findings

- First full-grid d>3 multi-asset Black-Scholes PDE solver runnable on a laptop; tested in d=3,4,5.
- QTT ranks of the BS operator bounded polynomially in d (not in grid size N); payoffs/boundary conditions admit low TT-rank at target accuracy.
- Space-time QTT is often faster than time-stepping for d≤3 European options and gives the full temporal surface in one run; for d>3, time-stepping is preferable.
- American options: early-exercise projection adds only modest overhead; QTT rank growth is the dominant cost, not grid size.
- Enables instant re-pricing for new spots via interpolation and dense cross-Greeks consistently over the grid — capabilities MC cannot match.

## Snippets

- **p.1** — "We show that quantized tensor trains (QTT) turn the d-asset Black–Scholes PDE into a tractable high-dimensional problem on a personal computer." — core claim.
- **p.1** — "ranks that scale polynomially in d and polylogarithmically in the grid size" — complexity bound that enables d>3.
- **p.1** — "methods introduced can comfortably be pushed to full-grid solutions on 10−15 underlyings, with further algorithmic optimization and more compute power" — scaling claim (tentative, not empirically shown beyond d=5).
- **p.1** — "A full state–space solution enables… (i) instant re-pricing for new spots within the domain via interpolation, without reruns; and (ii) dense Greeks—including cross-sensitivities—computed consistently over the grid." — value proposition vs MC.
