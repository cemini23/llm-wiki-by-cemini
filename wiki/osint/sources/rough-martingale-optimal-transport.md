---
title: 'Rough Martingale Optimal Transport: Theory, Implementation, and Regulatory Applications for NMRF'
type: source
tags: [pdf, options-derivatives, k49]
keywords: [Rough, Martingale, Optimal, Transport, RMOT, FRTB, NMRF, rough-volatility, Hurst, capital-relief, identifiability]
clusters: [options-derivatives]
related:
  - concepts/options-derivatives.md
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/options-derivatives.md — Options & Derivatives cluster hub (covers rough volatility, fractional models, FRTB-audit)

## Raw Concept

- **Original title**: Rough Martingale Optimal Transport: Theory, Implementation, and Regulatory Applications for Non-Modelable Risk Factors
- **Author(s)**: Sri Sairam Gautam B. (Jawaharlal Nehru University), Isha (Jawaharlal Nehru University)
- **Type**: PDF (arXiv 2602.00097)
- **Location**: research for cemini/Rough Martingale Optimal Transport.pdf
- **Retrieved**: 2026-04-27
- **Length**: 15p
- **Read status**: deep-read
- **Cluster**: options-derivatives

## Narrative

The Fundamental Review of the Trading Book (FRTB) imposes punitive capital treatment on Non-Modelable Risk Factors (NMRF) — risk factors with insufficient market data to satisfy supervisors. For exotic derivatives referencing NMRFs, classical Martingale Optimal Transport (MOT) — which prices payoffs by finding the most/least favorable martingale measure consistent with observed option marginals — produces *infinite* audit bounds when data are sparse, forcing banks into prohibitively expensive "stress scenario" pricing. This paper proposes Rough Martingale Optimal Transport (RMOT), which regularizes the MOT transport plan with a rough-volatility prior (a Rough Heston measure), yielding finite, explicit, and asymptotically rate-optimal extrapolation bounds.

Key theoretical results: (1) a single-asset identifiability theorem — the effective parameter dimension grows only logarithmically with the number of strikes (`d_eff ≤ min{5, ⌊log₂ m⌋ + 2}`), and a Cramér-Rao bound `Std(Ĥ) ≥ C·m^(-1/2)` shows ~50 strikes suffice to estimate the Hurst exponent to ±0.05; (2) an explicit deep-OTM extrapolation error bound that decays as a stretched exponential `exp(−k^(1−H))`, matching the intrinsic large-deviations rate of rough volatility (so the bound is rate-optimal); (3) a counter-intuitive multi-asset result — correlation matrices are locally identifiable from marginal option surfaces *provided assets have distinct Hurst exponents*, with Tikhonov regularization toward historical correlation needed when roughness is too similar; (4) a block-sparse Newton calibration algorithm with `O(N²M²)` complexity, scaling to N=30 assets in ~3 minutes on an Apple M4.

Empirically, the authors calibrate on SPY/QQQ/IWM/GLD options (2019–2024, CBOE via yfinance), recovering very rough Hurst exponents (H ≈ 0.08–0.14) and confirming the SPY-QQQ correlation (`ρ̂ = 0.85 ± 0.02` vs historical 0.83). Deep-OTM extrapolation error stays under 5.7% where Black-Scholes exceeds 50%. The headline regulatory claim: on a $1B exotic basket-options book, RMOT cuts the capital charge from $1B (classical MOT) to $120M — ~$880M of capital relief — while a 100-seed cross-validation (4.2% error) and a pilot traffic-light backtest (1 exception, Green Zone) support coverage. The authors are careful to frame RMOT as an FRTB *stress-calibration tool* (a generator of "least plausible" prices), not a replacement for the regulatory aggregation formula, and label the capital figures as illustrative.

**Cemini relevance**: RMOT is a rough-volatility / derivative-bound framework with a direct FRTB non-modelable-risk-factor audit application — relevant to Cemini's options/derivatives work and to any audit or capital-charge analysis where sparse-data exotic pricing must produce explicit, defensible bounds rather than the trivial bounds classical MOT yields.

## Snippets

> "We propose a unified Rough Martingale Optimal Transport (RMOT) framework that regularizes the transport plan with a rough volatility prior, yielding finite, explicit, and asymptotically tight extrapolation bounds." [Source: Rough Martingale Optimal Transport.pdf p.1]

> "Empirical results show that RMOT provides approximately $880M in capital relief per $1B exotic book compared to classical methods, while maintaining conservative coverage confirmed by 100-seed cross-validation." [Source: Rough Martingale Optimal Transport.pdf p.1]

> "We prove that correlation matrices are uniquely identifiable from marginal surfaces provided the assets have distinct Hurst exponents (Hi ≠ Hj)... This result is counter-intuitive: 'roughness separation' aids in identifying correlation structures from marginals." [Source: Rough Martingale Optimal Transport.pdf p.2, p.5]
