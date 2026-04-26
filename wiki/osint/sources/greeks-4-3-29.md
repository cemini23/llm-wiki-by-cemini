---
title: "Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps"
type: source
tags: [pdf, options-derivatives, ml-methods, 0dte, dml, bates-model, pide, stochastic-volatility, jump-diffusion, greeks, autodiff, heston, merton]
clusters: [options-derivatives, ml-methods]
related:
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- **Original title**: Differential Machine Learning for 0DTE Options with Stochastic Volatility and Jumps
- **Author(s)**: Takayuki Sakuma (Faculty of Economics, Soka University)
- **Type**: PDF (arXiv:2603.07600v1 [q-fin.CP])
- **Location**: research for cemini/greeks 4 3:29.pdf
- **Length**: 15p
- **Retrieved**: 2026-04-23
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: options-derivatives, ml-methods

## Narrative

Differential Machine Learning (DML) [Huge & Savine 2020] adapted to the hardest regime for option pricing: **0DTE options under the Bates stochastic-volatility jump-diffusion (SVJD) model**. 0DTE options now account for a large fraction of index options volume, and recent empirical work (Bandi et al. 2023; Dim et al. 2024) documents elevated intraday jump activity and enormous ATM gamma — exactly where standard numerics explode.

**Three design choices.**

1. **DML with AD-computed Greeks in the loss.** Single price network; Greeks obtained via `torch.autograd`-style automatic differentiation of the network output w.r.t. inputs, then included *directly in the training loss*. Once trained, prices AND Greeks are obtained from a single forward pass — critical for intraday rebalancing of 0DTE books.

2. **Maturity-gated variance correction in BS form.** Rather than predicting raw prices (a near-singular mapping as τ→0), the network learns a correction to an underlying Black-Scholes formula, scaled by a deterministic function that *mathematically forces the correction to vanish as τ→0*. Terminal payoff is enforced structurally, not learned. Standard trick in volatility-surface learning [Liu et al. 2019, Ackerer et al. 2020].

3. **Separate jump-operator network.** The paper's key methodological contribution. When a PIDE-residual penalty is the *only* identification for the jump term, the optimizer can trade off errors between diffusion and jump terms while keeping total residual small. A small residual does not imply correct jump-integral recovery. Sakuma introduces a second network dedicated to the compensated jump operator, trained via a **three-stage procedure** that sequentially identifies the diffusion, then the jump, then jointly refines.

**Model:** Bates = Heston variance process + Merton lognormal jumps, correlated Brownian motions (ρ), Poisson jumps with intensity λ, i.i.d. Gaussian log-jump sizes Y ~ N(μ_J, σ²_J).

**Numerical results:** in Bates simulations, the three-stage twin-network scheme (a) improves jump-term approximation vs one-stage baselines, (b) keeps price errors close to one-stage, (c) improves Greek accuracy, (d) produces stable one-day delta hedges, and (e) is substantially faster than a Fourier-based pricing benchmark.

Relevant to Cemini because (a) Cemini targets SPY/QQQ-style 0DTE plays for the options feature layer per `3-19-trading-options-data-research.md`; (b) the maturity-gating trick is specifically recommended for adoption in `3-29-research-5.md` as a Cemini-portable pattern to stabilize pricing near expiry; (c) the compensated-jump-term numerical proxy is an engineered Polars feature target in the same audit. This paper IS the primary source underneath those prescriptions. Honest limits: (1) all quantitative results are on *simulated* data, not live 0DTE market data — real-microstructure slippage not tested; (2) training cost of the full three-stage twin-network is heavy (the Cemini audit explicitly calls it "too heavy for current deployment" — Cemini adopts only the feature-engineering idea, not the trained model); (3) 15p paper — tight, but numerical results section is brief and hyperparameter-sensitivity is not exhaustively reported.

## Key findings

- DML with AD-computed Greeks in the training loss → single forward pass returns both price and Greeks (critical for 0DTE rebalancing).
- **Maturity-gating trick**: network learns a BS-form variance correction, deterministically scaled to vanish as τ→0. Terminal payoff is structurally enforced, not learned.
- **Twin-network architecture**: separate jump-operator network with three-stage training prevents the optimizer from cancelling diffusion/jump errors against each other — required for identifiable jump-integral recovery.
- Bates model: Heston variance + Merton lognormal jumps; correlated Brownian motions.
- Results vs Fourier benchmark: substantially faster, comparable or better accuracy, stable 1-day delta hedge.
- Improves Greek accuracy vs one-stage DML; keeps price errors close.
- All results on simulated data — no live-market validation.
- Directly prescriptive source for `3-29-research-5.md`'s Cemini recommendations (maturity-gating in PyTorch, compensated-jump as Polars feature).

## Snippets

- **Abstract** — "We present a differential machine learning method for zero-days-to-expiry (0DTE) options under a stochastic-volatility jump-diffusion model that computes prices and Greeks in a single network evaluation."
- **Abstract** — "we represent the price in Black–Scholes form with a maturity-gated variance correction, and combine supervision on prices and Greeks with a PIDE-residual penalty. To make the jump contribution identifiable, we introduce a separate jump-operator network and train it with a three-stage procedure."
- **§1 (point 2)** — "the network learns a variance correction in a Black–Scholes formula, scaled so that the correction vanishes as τ→0. This ensures the correct short-maturity limit (payoff) and reduces the approximation difficulty faced by the network in the near-singular regime."
- **§1 (point 3)** — "When the jump component is identified only through a PIDE-residual penalty, the optimizer can trade off errors between the diffusion and jump terms while keeping the overall residual small. As a result, a small residual does not imply that the learned jump operator matches the model-implied jump integral."
