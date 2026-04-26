---
title: "Differentiating Through Stochastic Differential Equations: A Primer"
type: source
tags: [pdf, options-derivatives, sde, adjoints, ito, stratonovich, autodiff, greeks, tutorial]
clusters: [options-derivatives]
related:
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- **Original title**: Differentiating Through Stochastic Differential Equations: A Primer
- **Author(s)**: Rishi Leburu, Levon Nurbekyan, Lars Ruthotto
- **Affiliation**: Emory University (Math + CS)
- **Type**: PDF (arXiv:2601.08594v1, math.NA) — tutorial/primer, NSF DMS 2038118
- **Location**: research for cemini/greeks 8 3:29.pdf
- **Length**: 20p
- **Retrieved**: 2026-04-23 (download date, not publication)
- **Publication date**: 2026-01-13
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: options-derivatives

## Narrative

A graduate-level pedagogical primer on numerically differentiating through stochastic differential equations, framed explicitly around three motivating use cases: financial Greeks (Black-Scholes sensitivities to σ, r, T, S), neural ODE/SDE training, and physical parameter tuning (Lorenz-63). The authors observe that while differentiation of deterministic ODEs is standard material in optimal control courses and textbooks, SDE differentiation is underserved — and the subtleties of noise type (Itô vs Stratonovich) × discretization choice are commonly mishandled.

Structured as "two tales." Tale 1 — discretize-optimize (DO): differentiate through a numerical scheme (Euler-Maruyama, Milstein, etc.) as if it were a deterministic computational graph; works reliably for both Itô and Stratonovich calculi. Tale 2 — optimize-discretize (OD): derive the adjoint/backward equation in continuous time first, then discretize; examines when DO and OD converge to the same gradient in the continuous limit and when they diverge. The presentation adapts Kidger's rough-path framework into a simplified small-dimensional treatment with numerical validations.

Relevant to Cemini for any Monte-Carlo-based Greek computation pipeline or trainable SDE/neural-SDE models (deep hedging). Honest limits: explicitly a tutorial, not a survey of state-of-the-art — no new algorithms or convergence theorems; instructors are the target audience; no benchmarks vs Malliavin pathwise or adjoint methods implemented in JAX/Diffrax.

## Key findings

- Discretize-optimize (DO) differentiation through SDEs is reliable for both Itô and Stratonovich calculi when paired with the correct numerical scheme.
- Optimize-discretize (OD) via continuous-time adjoints can diverge from DO depending on discretization — gives explicit criteria for when they agree.
- Unified treatment of ODEs, SDEs, and neural-SDE training (shared DO/OD machinery) drawing on Kidger's rough-path framework.
- Greek computation is explicitly listed as a primary motivating application — Black-Scholes sensitivity examples appear throughout.
- Pedagogical intent, small-dim examples, informal presentation — good onboarding for teams moving into deep hedging / differentiable SDE Monte Carlo.

## Snippets

- **p.1 (abstract)** — "Tale 1 demonstrates differentiating through discretized SDEs, known [as] the discretize-optimize approach, is reliable for both Itô and Stratonovich calculus. Tale 2 examines the optimize-discretize approach, investigating the continuous limit of backward equations from Tale 1 corresponding to the desired gradients."
- **p.1** — "For Black–Scholes models, one computes sensitivities to market parameters such as volatility, interest rate, and maturity, as well as the sensitivity of the future stock price with respect to the current price; quantities collectively known as Greeks."
- **p.2** — "standard textbooks on stochastic differential equations or stochastic optimal control do not include discussions of sensitivities akin to those in ODEs" — motivation for the tutorial.
- **p.2** — "Our presentation draws substantially from the comprehensive treatment in Kidger [16], which provides an elegant and abstract framework using rough path theory and controlled differential equations to unify the treatment of ODEs and SDEs."
