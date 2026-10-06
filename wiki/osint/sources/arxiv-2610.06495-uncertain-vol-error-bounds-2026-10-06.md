---
title: "A posteriori error bounds for the Uncertain Volatility Model (arXiv 2610.06495)"
type: source
tags: [source, k283, arxiv, volatility, options, robust, quant]
keywords: [uncertain-volatility-model, uvm, black-scholes-barenblatt, pinn, robust-hedging, dual-bound]
related:
  - concepts/k283-arxiv-wave.md
  - concepts/xsp-vol-regime-gates.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
read_status: read
---

## Relations

- @concepts/k283-arxiv-wave.md
- @concepts/xsp-vol-regime-gates.md

## Raw Concept

| Title | A posteriori error bounds for the Uncertain Volatility Model |
| Authors | Abbas-Turki (Sorbonne), Chassagneux (ENSAE-CREST), Lemor, Loeper, Sananes (BNP Paribas Global Markets) |
| Type | arXiv preprint (math.OC) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.06495-a-posteriori-error-bounds-for-the-uncertain-vola.pdf` |
| Retrieved | 2026-10-06 |
| arXiv | 2610.06495v1 |
| read-status | read |

## Narrative

In the **Uncertain Volatility Model (UVM)** you do not know σ; you only know σ ∈ [σ⁻, σ⁺]. The price is then a *range*, not a number. This paper gives **computable two-sided bounds** that bracket the true price from one smooth candidate value function.

### Method

Define the matrix-valued **cash-gamma** field:

    Γ_v(t,x) = ½ · diag(x) · ∇²v · diag(x)

and the Hamiltonian H★[γ] = sup_{a∈A} Tr[γaaᵀ]. The dual representation V = D(Γ_V) = inf_Γ D(Γ). For a candidate v, the dual bound is D(Γ_v) = v + ε(v), where ε(v) uses the **Black–Scholes–Barenblatt (BSB) residual**:

    R(v) = ∂_t v + r(xᵀ∇v − v) + H★[Γ_v]

The primal lower bound comes from the maximiser control a_v. Discrete-time versions give errors O((T/N)^{1/4}) and O((T/N)^{1/2}). **Second-order Sobolev training** improves neural critics.

### Results

- 5-D geometric call-spread (reference 9.70): PINN dual Û_D = 9.7143, Û_ε = 9.7248; the martingale dual gives Û_M = 10.0785.
- 2-D outperformer (reference 12.83): finite-difference candidate Û_D = 12.8291.
- Ordering: FD < PINN < Sobolev-2 < Sobolev-1 < standard.
- **Hessian-based duals are tighter than the martingale dual.** Second-order supervision makes them tighter still.

### Why it matters here

A practical way to bound a robust option price when the vol surface is uncertain — the "how wrong can my price be" question. Complements the K237 `dex-fee-implied-volatility` work and the vol-regime gate family. The technique (cash-gamma dual, BSB residual) is the reusable part.

**No license stated; no code.** ANR / France-2030 funding.

## Snippets

> "Hessian-based duals are tighter than the martingale dual; second-order supervision improves them." [Source: arxiv-2610.06495-a-posteriori-error-bounds-for-the-uncertain-vola.pdf]

> "R(v) = ∂_t v + r(xᵀ∇v − v) + H★[Γ_v]" [Source: arxiv-2610.06495-a-posteriori-error-bounds-for-the-uncertain-vola.pdf]
