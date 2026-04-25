---
title: "Hedging of exotic options in Hawkes jump-diffusion models by Malliavin calculus"
type: source
tags: [pdf, options-derivatives, market-microstructure, malliavin, hawkes, jump-diffusion, greeks]
clusters: [options-derivatives, market-microstructure]
related: []
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

*(Cross-references will be added in Phase 2.)*

## Raw Concept

- **Original title**: Hedging of exotic options in Hawkes jump-diffusion models by Malliavin calculus
- **Author(s)**: Ayub Ahmadi, Mahdieh Tahmasebi
- **Affiliation**: Tarbiat Modares University, Tehran
- **Type**: PDF (arXiv:2510.05689v1, math.PR)
- **Location**: research for cemini/greeks1 3:29.pdf
- **Length**: 37p
- **Retrieved**: 2026-04-23 (download date, not publication)
- **Publication date**: 2025-10-08
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: options-derivatives, market-microstructure

## Narrative

Ahmadi & Tahmasebi derive the first Malliavin-calculus hedging framework (delta computation) for exotic options under Hawkes jump-diffusion dynamics with stochastic self-exciting jump intensity. The motivation: Hawkes processes capture jump clustering observed in asset prices (pronounced since the 2008 crisis) — the exponential-kernel model λ_t = λ_0 + α Σ e^{-β(t-T_i)} has tractable Markov structure but the stochastic intensity materially changes the delta representation vs classical Poisson jump-diffusion.

Core technical move: replace the stochastic integral against the point process with an integral against a Lévy process whose Lévy measure absorbs the stochastic intensity. This lets the authors express Hawkes SDE solutions in exponential form and compute explicit Malliavin derivatives — at the cost that Malliavin derivatives of the intensity itself enter the formula, complicating the moment-boundedness proofs for the inverse (needed for the Skorokhod integral domain condition). Section 4 delivers delta formulas for European and Asian options via innovation quadratures; Section 5 proves convergence of a discretized path-by-path simulation scheme; Section 6 provides numerical verification.

Relevant to Cemini for equity/FX derivative desks running clustered-jump volatility regimes (earnings drift, energy/FX crisis regimes). Honest limit: purely theoretical paper — no market calibration, no benchmark against Heston/Bates. Computational cost of the Malliavin weight scheme vs finite-difference Monte Carlo isn't quantified. Production use requires downstream calibration and performance work.

## Key findings

- First hedging (delta) strategy for exotic options in Hawkes jump-diffusion models via Malliavin calculus.
- Novel reformulation: Hawkes SDEs → Lévy SDEs with intensity-embedded Lévy measure, permitting exponential-form solutions.
- Explicit delta Malliavin-weight formulas for European and Asian options (Lemmas 4.2, 4.4).
- Numerical convergence theorem for the discretized simulation scheme (Section 5).
- Hawkes framework produces heavier tails / higher peaks than Poisson jump-diffusion → higher deep-OTM option prices — matches empirical post-2008 jump clustering.

## Snippets

- **p.1 (abstract)** — "we employ Malliavin calculus to determine the delta of European and Asian options, where the underlying asset evolves according to a Hawkes jump-diffusion process. A central feature is that the Hawkes jump intensity is stochastic, which substantially affects the delta representation."
- **p.2** — exponential Hawkes: "λt = λ_0 + α Σ_{Ti<t} e^{-β(t-Ti)}" — core self-exciting intensity, Markov tractable.
- **p.2** — "Hawkes jump–diffusion models produce heavier-tailed distributions with higher peaks than Poisson jump-diffusion models, which leads to higher option prices under the Hawkes framework for deep out-of-the-money options."
- **p.3** — "To the best of our knowledge, this is the first paper to propose a hedging strategy for exotic options in Hawkes models."
