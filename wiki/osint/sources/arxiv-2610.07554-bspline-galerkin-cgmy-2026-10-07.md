---
title: "A B-Spline Galerkin Method for Option Pricing under the CGMY Process (arXiv 2610.07554)"
type: source
tags: [source, k284, arxiv, options, volatility, quant, pde]
keywords: [cgmy, tempered-stable, b-spline, galerkin, fractional-pde, american-options, calibration, toeplitz]
related:
  - concepts/k284-arxiv-wave.md
  - concepts/xsp-vol-regime-gates.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-arxiv-wave.md
- @concepts/xsp-vol-regime-gates.md

## Raw Concept

| Title | A B-Spline Galerkin Method for Option Pricing under the CGMY Tempered Stable Process |
| Author | Davood Damircheli (Louisiana State University, Dept. of Mathematics) |
| Type | arXiv preprint (math.NA) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.07554-a-b-spline-galerkin-method-for-option-pricing-un.pdf` |
| Retrieved | 2026-10-07 |
| arXiv | 2610.07554v1 |
| read-status | read |

## Narrative

A **deterministic, high-order solver** for European and American option prices under the **CGMY tempered-stable Lévy process** — a jump model that captures both small and large price jumps.

### Method

Backward fractional PDE (FPDE): ∂τV + AV = 0 with the generator

    Au = −(r − ωS)uₓ − CΓ(−Y)D⁺_M u − CΓ(−Y)D⁻_G u + λ₀u

The idea: **cardinal B-spline scaling functions as a Galerkin basis.** Corrected Fourier-symbol connection-coefficient matrices have **exactly Toeplitz interior blocks**, so a matvec is **O(N log N) via FFT**. Proofs: Gårding inequalities; spatial rate **O(h^{p−Y/2})**. Crank–Nicolson in time; a projected-SOR LCP for American puts. Martingale correction:

    ωS = CΓ(−Y)[(M−1)^Y − M^Y + (G+1)^Y − G^Y]

### Results

- **Calibration to S&P 500 surfaces: IV RMSE 2.47 vp and 1.97 vp** on well-identified surfaces; **7.19 vp** on a crisis date.
- European B-spline price converges to the COS reference **6.8276**.
- Beats a stabilized Grünwald–Letnikov baseline **only at tight tolerances**.

### Why it matters here

An **alternative to Monte-Carlo / COS for jump-diffusion pricing** with a fast structured solve. Relevant to the vol lane when the model needs fat tails (CGMY) and a deterministic price. **No license stated; no code.** Awareness for `xsp-vol-regime-gates`; **no trade, no scp.**

## Snippets

> "Corrected Fourier-symbol connection-coefficient matrices have exactly Toeplitz interior blocks, giving O(N log N) matvec via FFT." [Source: arxiv-2610.07554-a-b-spline-galerkin-method-for-option-pricing-un.pdf]

> "Calibration to S&P 500 surfaces attains IV RMSEs of 2.47 vp and 1.97 vp; crisis date 7.19 vp." [Source: arxiv-2610.07554-a-b-spline-galerkin-method-for-option-pricing-un.pdf]
