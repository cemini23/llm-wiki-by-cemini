---
title: "Feynman-Kac Derivatives Pricing on the Full Forward Curve"
type: source
tags: [pdf, options-derivatives, ml-methods, hjm, feynman-kac, pinn, interest-rates, caplets]
clusters: [options-derivatives, ml-methods]
related: []
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

*(Cross-references will be added in Phase 2.)*

## Raw Concept

- **Original title**: Feynman-Kac Derivatives Pricing on the Full Forward Curve
- **Author(s)**: Kevin Mott
- **Affiliation**: Rotman School of Management, University of Toronto
- **Type**: PDF (arXiv:2603.12375v1, q-fin.CP) — chapter of doctoral dissertation
- **Location**: research for cemini/greeks 3 3:29.pdf
- **Length**: 37p
- **Retrieved**: 2026-04-23
- **Publication date**: 2026-03-12
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: options-derivatives, ml-methods

## Narrative

Mott introduces Finance-Informed Neural Networks (FINNs) — a physics-informed-neural-network adaptation for interest-rate derivative pricing under the full Heath-Jarrow-Morton (HJM) framework. Standard HJM yields arbitrage-free prices but is infinite-dimensional, forcing reliance on Monte Carlo simulation with a speed-accuracy trade-off. By applying the Feynman-Kac theorem, the stochastic pricing expectation is recast as a deterministic PDE, and a neural network is trained to minimize PDE residual + boundary-condition violations via automatic differentiation.

The paper's headline: once trained, FINNs price caplets in microseconds, achieving pricing accuracy of 0.04-0.07 cents per dollar of contract value vs Monte Carlo benchmarks, with speedups of 300,000× to 4.5M× as forward-curve state-space discretization grows from 10 to 150 nodes. Critically, theta and curve deltas (the major Greeks) are computed for free via autodiff during PDE evaluation — Monte Carlo requires full re-simulation per sensitivity. The framework generalizes beyond caplets to caps, swaptions, and callable bonds via boundary-condition modifications with the same core PDE structure.

Relevant to Cemini for any interest-rate derivatives exposure, and more broadly as a pattern for amortized-inference pricing: train once, price repeatedly at near-zero marginal cost including Greeks — a significant architectural win on CPU-only infrastructure once the one-time training is amortized. Honest limits: accuracy claimed against MC benchmarks, not against closed-form solutions where they exist; the paper does not report generalization across contract parameters outside the training range (standard PINN weakness); no adversarial stress against volatile rate regimes; single-author dissertation chapter.

## Key findings

- FINNs: PINN-style neural network solves the Feynman-Kac PDE for HJM interest-rate derivatives, eliminating Monte Carlo.
- Pricing accuracy within 0.04-0.07 cents per dollar of contract value vs MC benchmarks.
- Speedup: 300,000× → 4.5M× over MC as forward-curve grid scales from 10 → 150 nodes; inference in microseconds regardless of dimension.
- Greeks (theta, curve deltas) come for free via autodiff — no re-simulation per sensitivity.
- Generalizes to caps, swaptions, callable bonds by changing boundary conditions; PDE structure unchanged.
- Produces a reusable pricing surface across contract features (strike, maturity) — no re-simulation on counterparty term changes.
- Pattern broadly applicable: amortized-inference pricing is a strong CPU-only architectural fit once training is done.

## Snippets

- **p.1 (abstract)** — "FINNs achieve pricing accuracy within 0.04 to 0.07 cents per dollar of contract value compared to Monte Carlo benchmarks. Once trained, FINNs price caplets in a few microseconds regardless of dimension, delivering speedups ranging from 300,000 to 4.5 million times faster than Monte Carlo simulation as the state space discretization of the forward curve grows from 10 to 150 nodes."
- **p.1** — "The major Greeks—theta and curve deltas—come for free, computed automatically during PDE evaluation at zero marginal cost, whereas Monte Carlo requires complete re-simulation for each sensitivity."
- **p.2** — "the Feynman-Kac transformation eliminates Monte Carlo simulation by replacing the stochastic pricing problem with a PDE characterization; second, neural networks trained via automatic differentiation solve high-dimensional PDEs efficiently"
- **p.2** — "If the counterparty changes the terms—even marginally adjusting strike, maturity, or other contract terms—you must resimulate entirely from scratch" — pain point motivating the amortized-inference design.
