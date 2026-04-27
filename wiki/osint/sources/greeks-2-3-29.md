---
title: 'Curved Greeks: A Geometric Layer for Option P&L Adjustments'
type: source
tags: [pdf, options-derivatives, portfolio-strategy, greeks, vanna-volga, covariant-hessian, riemannian, fx-barriers, execution-cost]
related:
  - concepts/options-derivatives.md
  - concepts/portfolio-strategy.md
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
clusters:
  - portfolio-strategy
  - options-derivatives
---

## Relations

- @concepts/options-derivatives.md — Options & Derivatives corpus-index hub (Q 2026-04-27)
- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub (Q 2026-04-27)
- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- **Original title**: Curved Greeks: A Geometric Layer for Option P&L Adjustments
- **Author(s)**: Pedro Pablo Pérez Velasco (ICADE Comillas + Santander Model Risk), Mengjue Lu (ICAE Complutense), Daniel Arrieta (ICADE Comillas + Santander)
- **Type**: PDF (arXiv:2603.14438v1 [q-fin.MF])
- **Location**: research for cemini/greeks 2 3:29.pdf
- **Length**: 34p
- **Retrieved**: 2026-04-23
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: portfolio-strategy, options-derivatives

## Narrative

Practitioner-grade quant paper from Santander Model Risk + Comillas that addresses the coordinate-invariance problem in short-horizon option P&L. Standard second-order Taylor expansions in (S, σ) vs (F, σ) vs (log F, σ) give *different* quadratic P&L predictions, which matters for (a) comparing desks on different parameterizations, (b) aggregating second-order effects across portfolios, and (c) doing rigorous P&L attribution. The paper replaces the raw Hessian H_ij = ∂_i∂_j V with a **covariant Hessian** Ĥ_ij = ∂_i∂_j V − Γᵏ_ij ∂_k V defined via an affine connection Γ, yielding a quadratic term ½Ĥ_ij δxⁱδxʲ that IS invariant under factor reparameterization.

The connection Γ is not postulated — it's **calibrated to match a desk-target quadratic P&L** (typically Vanna–Volga smile correction, or a local regression on realized P&L if available), while first-order Greeks (Δ, Vega) are left untouched. Calibration reduces to small linear systems with identifiability conditions (requires instruments whose (Δ, Vega) gradients span the factor directions — e.g. two vanillas with linearly independent sensitivities).

**Execution frictions** are folded into the same geometric picture: a quadratic trade-cost surrogate L(δq) = ½δq⊤Λδq on instruments, combined with the local hedge map x ↦ q(x), induces a quadratic penalty g_ℓ(x) = M⊤ΛM on factor moves — which can be interpreted as a (second, liquidity-aware) Riemannian metric on factor space. Least-cost rebalancing then becomes geodesic computation in this metric. Two FX-barrier case studies: EURUSD and USDTRY. Briefly sketches extensions to risk normalization, scenario/gap terms, and xVA/capital add-ons.

Relevant to Cemini only tangentially — Cemini is not running a multi-desk bank options book, so the coordinate-invariance use case is muted. The *execution-cost-as-metric* idea is more portable: it's a geometrically clean way to fold liquidity into hedge-rebalance scheduling, which could be adopted in the Cemini Order Router if options execution ever moves beyond single-venue CLOB. Honest limits: (1) local-only framework — no global guarantees outside the Taylor neighborhood; (2) "model-agnostic" holds for the quadratic term but requires a desk target (V-V, realized P&L) that IS model-dependent; (3) case studies are illustrative, not benchmark-grade; (4) ill-conditioning discussion is thin — real desk P&L is noisy.

## Key findings

- Core construction: replace raw Hessian with covariant Hessian Ĥ_ij = ∂_i∂_j V − Γᵏ_ij ∂_k V; quadratic P&L term becomes reparameterization-invariant.
- Connection Γ calibrated to match desk target (Vanna–Volga or realized P&L regression); first-order Greeks preserved.
- Calibration = small linear systems; identifiability needs instruments spanning (Δ, Vega) directions.
- Execution cost surrogate L(δq) = ½δq⊤Λδq induces Riemannian metric g_ℓ = M⊤ΛM on factor space → cost-aware least-cost rebalancing = geodesic.
- BS quadratic predictor recovered when smile is locally flat — backward compatibility.
- Two FX-barrier case studies: EURUSD, USDTRY.
- Direct Cemini portability is limited; execution-cost-as-Riemannian-metric is the most transferable idea.

## Snippets

- **Abstract** — "The usual Hessian is replaced by a covariant Hessian defined by an affine connection, yielding an invariant quadratic predictor. The connection is calibrated to match a desk target for quadratic P&L—Vanna–Volga for smile effects or, in principle, a local fit to realized P&L—while leaving first-order hedge Greeks unchanged."
- **§1** — "The first-order term is already invariant (it is the directional derivative of the value along the factor move), but the usual Hessian of a scalar price is not: its coefficients do not transform tensorially under a change of variables."
- **§1** — "Combining this trade-cost model with a local hedge map x ↦ q(x) yields an induced quadratic penalty on factor moves, δx⊤g_ℓ(x) δx, g_ℓ(x) = M(x)⊤Λ M(x)."
- **Keywords** — "Curved Greeks; Covariant Hessian; Affine connection; Coordinate invariance; Vanna–Volga; Riemannian metric; Geodesic hedging."
