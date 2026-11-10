---
title: VIX term structure with fractional memory — the RISVIX model
type: concept
related:
  - concepts/k296-feeds-wave.md
  - sources/arxiv-risvix-vix-term-structure-2611.07120.md
  - concepts/vix-first-joint-spx-vix-calibration.md
  - concepts/xsp-vol-regime-gates.md
  - concepts/market-memory-hurst-regime.md
updated: 2026-11-10
---

## Raw Concept

How much memory does a volatility shock leave in the VIX curve, and does that memory buy better option prices? Prompted by arXiv 2611.07120.

## Narrative

### The model shape

The standard ISVIX model averages a mean-reverting variance process under the risk-neutral measure. The conditional mean is exponential: `E[V_s] = θ + (V_0 - θ) e^(-κs)`.

RISVIX replaces the exponential with a **Mittag–Leffler function** by putting a fractional Volterra kernel in front of the dynamics:

```
V_t = V_0 + ∫ K(t-s){κ(θ_s - V_s) ds + σ_V √V_s dB_1 + dJ_s}
K(t) = t^(α-1)/Γ(α)
```

`α = 1` gives the Markovian model back. `α < 1` gives slower decay and a fatter memory. [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.6]

### The term structure

At the valuation origin, squared VIX is a two-point mixture:

```
VIX²(τ) = V_0 w(τ) + θ_0 (1 - w(τ))
w(τ) = E_{α,2}(-κτ^α)
```

`w(τ)` falls from one to zero as `τ` rises. So the curve moves monotonically from the spot level to the long-run level. It is upward sloping when `V_0 < θ_0`, downward sloping when `V_0 > θ_0`, and flat when they match. [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.7]

Only four parameters set the curve: `α`, `κ`, `V_0`, `θ_0`. The diffusive and jump parameters do not enter it.

### Why the separation matters

The separation is what makes the calibration two-step and cheap:

1. Fit `(α, κ)` and the daily states `(V_0, θ_0)` to the VIX term-structure indices.
2. Fit `(σ_V, σ_θ, λ_y, μ_y)` to VIX call prices.

Step 1 has a closed form. Step 2 needs one Volterra equation and one scalar Riccati ODE per transform argument, then one numerical integral for the price. [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf pp.8-9]

### The empirical claim

Data 2018-01 to 2025-06, daily VIX term-structure indices and VIX option quotes.

- Term-structure fit improves over the Markovian benchmark. The gain is larger for slope and curvature, and larger in elevated-volatility periods.
- Out-of-sample option pricing improves. MSE −**13.06%**, MAE −**6.33%**. The gain is larger at short maturities and in high-VIX states.

[Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.1]

The regime dependence is the substance. A fractional-memory model adds most when volatility is high, and little when it is calm. That is consistent with the general rough-volatility finding: roughness is a tail phenomenon.

### How to use it

- **As a curve descriptor.** A fitted `α` below 1 is evidence that a shock decays more slowly than exponential. That is a directly reportable number, and it is more informative than a single slope.
- **Not as a joint SPX model.** The model has no SPX dynamics. It cannot price SPX options or hedge equity exposure. Use @concepts/vix-first-joint-spx-vix-calibration.md for SPX work.
- **Not as a standalone signal.** The paper does not test `α` as a predictor of future volatility.

## Snippets

> "The time-zero squared VIX curve moves monotonically from V0 towards θ0: it is upward sloping when V0 < θ0, downward sloping when V0 > θ0, and flat when the two levels coincide." [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.7]

> "The gains from fractional memory vary substantially with market conditions." [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.2]

## Dead Ends

- **Using the model for SPX options.** No spot dynamics.
- **Expecting a gain in calm markets.** The reported gain concentrates in high-VIX states and short maturities.
