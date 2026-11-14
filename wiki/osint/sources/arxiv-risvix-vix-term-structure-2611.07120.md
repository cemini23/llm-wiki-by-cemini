---
title: "Rough instantaneous squared VIX (RISVIX) — term structure and VIX option pricing"
type: source
related:
  - concepts/k296-feeds-wave.md
  - concepts/vix-term-structure-fractional-memory.md
  - concepts/vix-first-joint-spx-vix-calibration.md
  - concepts/xsp-vol-regime-gates.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | A Rough Instantaneous Squared VIX Model for Term Structure and Option Pricing |
| Author | Tianfeng Yang, Wen Su, Blanka Horvath |
| Type | arXiv preprint, q-fin.PR |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf` |
| Retrieved | 2026-11-10 |
| File | arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf (33 pages) |
| Read status | read |

## Narrative

The paper adds fractional memory to the instantaneous squared VIX (ISVIX) framework of Luo and Zhang (2012) and Luo et al. (2019). The result is RISVIX. A fractional Volterra kernel `K(t) = t^(α-1)/Γ(α)` replaces the constant kernel of the Markovian model. Setting α = 1 recovers the Markovian benchmark.

Three results carry the paper.

1. **A closed-form VIX term structure.** The time-zero squared VIX curve is a weighted average of the spot level `V0` and the long-run level `θ0`. The weight `w(τ) = E_{α,2}(-κτ^α)` is a Mittag-Leffler function, not a pure exponential. The curve moves monotonically from `V0` to `θ0`, and its slope sign is set by the gap between the two levels. Only four parameters enter the time-zero curve: `(α, κ, V0, θ0)`. [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.7]
2. **A semi-closed VIX option formula.** An affine Fourier–Laplace transform gives the call price through a one-dimensional numerical integral. Each transform argument needs one nonlinear Volterra equation for `ψ1` and one scalar Riccati ODE for `ψ2`. [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.8]
3. **A two-step calibration.** Step 1 fits `(α, κ)` and the date-specific states `(V0, θ0)` to VIX term-structure indices. Step 2 fits the four distributional parameters `(σV, σθ, λy, μy)` to VIX call mid prices. The separation is clean because the diffusion and jump terms do not enter the time-zero term structure. [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.9]

The model includes a jump component with exponentially distributed sizes and a stochastic mean level `θ` with its own square-root diffusion.

### Empirical results

Data: daily VIX term-structure indices and VIX option quotes from **January 2018 to June 2025**.

- RISVIX fits the VIX term structure better than the Markovian benchmark. The gain is larger for slope and curvature, and larger in elevated-volatility periods. [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.1]
- Out-of-sample option pricing improves. MSE falls **13.06%** and MAE falls **6.33%**. The gain is larger at short maturities and in high-VIX states. [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.1]

The second point is the useful one for a trading desk. The model earns its memory term when volatility is high. It adds little when volatility is calm.

### Why it matters here

The paper is a **direct VIX model**, not a joint SPX–VIX model. It does not impose a structural link between the equity market and the volatility market. That makes it cheap to fit and useful for VIX futures and VIX options only. It does not replace the VIX-first joint calibration pattern in @concepts/vix-first-joint-spx-vix-calibration.md for SPX work.

The term-structure reading is compatible with @concepts/xsp-vol-regime-gates.md. A Mittag-Leffler decay is a one-parameter family between exponential decay and slow power-law decay. The fitted α is therefore a direct measure of how slowly a volatility shock decays along the curve.

## Snippets

> "RISVIX also improves out-of-sample option pricing, reducing MSE and MAE by 13.06% and 6.33%, respectively, with larger gains at shorter maturities and in high-VIX states." [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.1]

> "The time-zero term structure depends only on (α, κ, V0, θ0). The diffusion and jump parameters do not enter this curve." [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.7]

> "Formally setting α = 1 gives K ≡ 1 and a Markovian jump-diffusion." [Source: arxiv-2611.07120-a-rough-instantaneous-squared-vix-model-for-term.pdf p.6]

## Dead Ends

- **Using RISVIX as a joint SPX–VIX model.** The model has no SPX spot dynamics. It cannot price SPX options and cannot hedge SPX exposure.
- **Reading α as a tradable signal on its own.** α is a calibration output on a term-structure snapshot. The paper does not test α as a predictor of future volatility.
