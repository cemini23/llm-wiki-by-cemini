---
title: "Two Sigma Street View — A Machine Learning Approach to Regime Modeling (2021)"
type: source
tags: [source, two-sigma, regime-modeling, gmm, factor-lens, allocator, street-view, k58]
keywords: [gaussian-mixture-model, unsupervised-learning, factor-lens, crisis, steady-state, inflation, walking-on-ice, stress-test, cross-validation]
related:
  - concepts/gmm-factor-lens-regime-modeling.md
  - concepts/markov-regime-switching-models.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/quant-finance.md
  - concepts/hedge-fund-open-source-tooling.md
  - concepts/macro-weather-regime.md
  - sources/lob-regime-detection-hiremath-2026.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
read_status: read
---

## Relations

- @concepts/gmm-factor-lens-regime-modeling.md — primary synthesis
- @concepts/markov-regime-switching-models.md — sibling: Markov/HMM is temporal transition-based; this source is cross-sectional GMM clustering
- @concepts/regime-conditioned-evaluation.md — use GMM cluster distributions for scenario/stress sampling per regime-conditioned discipline
- @concepts/quant-finance.md — parent cluster
- @concepts/hedge-fund-open-source-tooling.md — Two Sigma institutional context
- @concepts/macro-weather-regime.md — prod macro regime sibling (not auto-wired)
- @sources/lob-regime-detection-hiremath-2026.md — LOB microstructure regimes (orthogonal)

## Raw Concept

- **Title**: A Machine Learning Approach to Regime Modeling
- **Author**: Alex Botte and Doris Bao (Two Sigma Investments, LP)
- **Type**: Street View (investor education / research note)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/two-sigma-gmm-regime-modeling-2021.pdf`
- **Retrieved**: 2026-05-23
- **Pages**: 9
- **Read status**: read

## Narrative

Two Sigma applies an **unsupervised Gaussian Mixture Model (GMM)** to daily returns of **17 factors** in the U.S. **Two Sigma Factor Lens** (1971–late 2020 training window; Crowding style factor excluded for data limits). The GMM fits a **joint multivariate Gaussian** per cluster — not a single-asset return distribution — so each cluster is a 17-dimensional state with its own means, volatilities, and correlations.

**Cluster count:** only hyperparameter; selected via cross-validation (log-likelihood primary; AIC and McAssey 2013 goodness-of-fit test gave similar results). **Four clusters** emerged, later labeled by interpreting factor behavior:

| Label | Intuition (from factor means/vols) | Historical share (highest-prob days, 1971–2020) |
|-------|-------------------------------------|------------------------------------------------|
| **Crisis** | Global Equity & Credit negative; EM underperforms; Local Equity positive (U.S. outperforms); Equity Short Vol negative; Rates & Low Risk/Quality positive; Trend Following strong; factor correlations spike (still low by construction) | ~17% |
| **Steady State** | Healthy “normal” — broad equity/style strength, flat Local vs EM, mild inflation-hedge benefit | ~47% |
| **Inflation** | Dominant 1970s–80s; absent in last decade of sample | ~20% |
| **Walking on Ice (WOI)** | Risk-on fragility / bubble formation — high style vols (Value/Momentum/Low Risk), Momentum weak; tech bubble + post-GFC/COVID rebound fragility | ~16% |

**Regime assignment mechanics:** for each period the model outputs **probabilities** across four conditions; Exhibit-style charts use the **argmax** label. Periods are treated **i.i.d.** — the GMM does **not** condition on past/future labels when scoring a day. Regimes in the narrative sense = **persistence of the same label over time**, but switches can be abrupt (e.g. COVID crash then rebound).

**2020–Jul 2021 snapshot (dated):** Crisis in Feb–Mar 2020 → WOI → H2 2020 Steady State → 2021 shift toward WOI with sporadic Crisis days. **Inflation cluster probability ~0** over 2020–2021 despite CPI fears — Local Inflation and Foreign Currency (inflation winners in-sample) were negative; authors note current inflation may differ from 1970s training draw. Model is **not predictive**.

**Allocator use cases:** (1) **Risk management** — sample from cluster return distributions for stress tests; (2) **Asset allocation** — long-horizon forecasts harder when conditions flip quickly; design portfolios robust to condition volatility, allow tactical shorter-horizon tilts.

**Limitations for Cemini:** proprietary Factor Lens; labels are post-hoc; i.i.d. scoring ignores transition dynamics that @concepts/markov-regime-switching-models.md covers; 2021 “today” section is stale for 2026 ops.

## Snippets

> "An alternative, more data-driven approach is letting historical data on assets and/or market risks delineate the regimes for you. A specific example of this approach is a Gaussian Mixture Model (GMM), which is a type of unsupervised learning method." [Source: two-sigma-gmm-regime-modeling-2021.pdf p.2]

> "The result of the GMM using the Two Sigma Factor Lens factor data was four different clusters, or what we think may correspond to four different types of market conditions." [Source: two-sigma-gmm-regime-modeling-2021.pdf p.3]

> "This model is not predictive, so we are not able to say whether Inflation will be increasingly important later in 2021 or the years ahead." [Source: two-sigma-gmm-regime-modeling-2021.pdf p.6]

> "Allocators can enhance their scenario analysis by sampling from the distributions of these market conditions to stress test their portfolios." [Source: two-sigma-gmm-regime-modeling-2021.pdf p.7]
