---
title: "BeTINN — structured conditional neural solvers for Heston pricing (arXiv 2610.19254)"
type: source
tags: [quant, volatility, neural-pde, heston, source, k292]
keywords: [BeTINN, TINN, PINN, DeepONet, Heston, greeks, delta, gamma, derivative-aware eval]
related:
  - concepts/k292-osint-wave.md
  - concepts/xsp-lane-trading-framework.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @concepts/k292-osint-wave.md — K292 osint wave hub
- @concepts/xsp-lane-trading-framework.md

## Raw Concept

Title: Beyond Time Induction: Structured Conditional Neural Solvers for Parametric Stochastic-Volatility Pricing
Authors: Jose Miguel Lara Rangel (UCL), Mixtli Vazquez Mendoza (Aicraft, Mexico)
Type: arXiv 2610.19254v1 [cs.LG], 30 pages, 13 Oct 2026
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.19254-beyond-time-induction-structured-conditional-neu.pdf`
Retrieved: 2026-10-16
Code: none printed
Read status: read

## Narrative

A physics-informed neural surrogate for the **Heston pricing map**, and — more useful to us — a **measurement argument**: an accurate price does not imply accurate greeks.

**Architecture.** BeTINN extends TINN (time-induced neural networks). Backbone weights are modulated jointly on time **and** the PDE parameters along *q* learned adaptation directions: `Θ_g(c) = B_g + Σ_{k=1..q} A_g,k · φ_g,k(c)`, with a small conditioning net on `(τ, µ)`. A lightweight **joint residual pathway** runs in parallel on the raw `(τ, x, v, µ)` input; the surrogate is the sum. TINN is the restricted case (q=1, fixed µ, no residual path). Sensitivities come free by autodiff from the same surrogate — no second model.

**Conditioning space:** `c = (τ, r, ρ, κ, θ, σ)`, backbone `ζ = (x, v, µ)`. Ranges: τ∈[0,5], x∈[−2,2], v∈[0.1,1], r∈[0,0.2], ρ∈[−0.9,0.1], κ∈[0.5,3], θ∈[0.01,1], σ∈[0.1,1]. Training is **label-free**: Heston PDE residual plus payoff initial condition and two log-moneyness boundary conditions, each its own mean-squared block. 15,000 interior points, 100,000 per boundary constraint, two frozen 10,000-point eval panels, q=4, Levenberg–Marquardt ≤3,000 steps at 64-bit, patience 250.

**Results** (Table 1, mean ± std over 6 seeds; MAE on the **normalized value u = C/K**, not absolute price; lower is better; baselines capacity-matched within 2.4% of BeTINN's parameters):

| Method | Params | Price MAE | Δ MAE | KΓ MAE | u_v MAE |
|---|---|---|---|---|---|
| TINN | 3,663 | 0.00910 | 0.0197 | 0.158 | 0.00853 |
| PINN | 3,631 | 0.00857 | 0.0188 | 0.149 | 0.00800 |
| PI-DeepONet | 3,511 | 0.00974 | 0.0232 | 0.199 | 0.0109 |
| **BeTINN** | **3,595** | **0.00746** | **0.0180** | **0.143** | **0.00712** |

Versus the best baseline (PINN): price MAE **−13%**, `u_v` **−11%**, Δ −4%, KΓ −4%. An external reference, **DeepSVM-adapted** (33,920 params, a re-implementation of Malandain et al. 2025), scored price MAE **0.1258** — roughly **10× worse** — with errors localizing at the money; the authors attribute that to the `max(e^x−1,0)` kink propagating a payoff-derivative discontinuity.

**The finding worth keeping.** **Validation physics loss is informative but does not determine differential fidelity** (Spearman ρ between held-out physics loss and MAE: 0.578 price, 0.682 Δ, 0.617 KΓ, 0.698 `u_v` — correlated, but the rankings reorder). **Accurate solution values coexist with localized derivative errors.** Errors concentrate near maturity at the sharp KΓ peak and at low moneyness, amplified by the `e^{−x}` / `e^{−2x}` coordinate factors.

**Limitations (stated).** Only the Heston family is fully validated; capacity matching leaves function class, optimization geometry and compute uncontrolled; **no formal monotonicity, convexity or arbitrage-freeness guarantees**; semi-analytic Heston made evaluation easy here and may not transfer.

### Why it matters here

**Read-and-cite, not adopt.** No code or data was released, and it is an architecture paper using finance as a benchmark rather than a finance method. Three things carry:

1. **The caveat.** Any neural pricer or greeks surrogate we evaluate must be validated on **Δ/Γ**, not on price alone. This is the same shape as the K290 DistressBench lesson — score the thing that matters, not the convenient proxy.
2. **Reference bars.** PINN at 3.6k parameters reaching 0.00857 normalized price MAE, DeepONet 0.00974, DeepSVM-adapted 0.1258 — cheap comparison points.
3. **Where the errors live:** near maturity at the KΓ peak and at low moneyness.

**No trade. No scp.**

## Snippets

> We further find that validation physics loss is informative but does not fully determine differential fidelity, and that accurate solution values can coexist with localized derivative errors. [Source: arXiv 2610.19254, abstract]

> These results support structured conditional adaptation and motivate derivative-aware evaluation when sensitivities are downstream quantities of interest. [Source: arXiv 2610.19254, abstract]
