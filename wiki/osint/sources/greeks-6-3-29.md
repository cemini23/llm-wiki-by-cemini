---
title: Application of Quasi Monte Carlo and Global Sensitivity Analysis to Option Pricing and Greeks
type: source
tags: [pdf, options-derivatives, qmc, sobol, gsa, greeks, brownian-bridge, aad, finite-differences, pca, monte-carlo]
related:
  - concepts/options-derivatives.md
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
clusters:
  - options-derivatives
---

## Relations

- @concepts/options-derivatives.md — Options & Derivatives corpus-index hub (Q 2026-04-27)
- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- **Original title**: Application of Quasi Monte Carlo and Global Sensitivity Analysis to Option Pricing and Greeks
- **Author(s)**: Stefano Scoleri (Iason Ltd), Marco Bianchetti (Intesa Sanpaolo Market Risk + U. Bologna), Sergei Kucherenko (Imperial College London)
- **Type**: PDF (arXiv:2602.14354v1 [q-fin.CP]; also published in Wilmott vol 2021 issue 116 pp. 66-83)
- **Location**: research for cemini/greeks 6 3:29.pdf
- **Length**: 46p
- **Retrieved**: 2026-04-23
- **Read status**: read-skim
- **Primary cluster**: options-derivatives
- **All clusters**: options-derivatives

## Narrative

Comprehensive practitioner study of Quasi-Monte Carlo (QMC) with Sobol' low-discrepancy sequences vs standard pseudorandom Monte Carlo (MC) for option pricing AND Greeks, including rigorous Global Sensitivity Analysis (GSA) to explain WHY QMC wins when it wins. Representative payoff set runs from vanilla European through Asian, barrier knock-outs, and cliquet structures. Published in Wilmott (2021) with this arXiv v1 release in Feb 2026.

**Core empirical claims:**
- QMC + Sobol' outperforms standard MC for pricing in most cases, *including* high-dimensional problems, with faster AND more stable convergence.
- **For Greeks with a small number of sensitivities, QMC + finite differences (FD) matches Adjoint Algorithmic Differentiation (AAD) accuracy** — at a fraction of the implementation cost. This is the paper's most practitioner-consumable finding: a solo dev gets AAD-grade Greeks without building the AAD tape-recording machinery.
- GSA using Sobol' indices diagnoses *why*: effective dimension reduction via **Brownian-bridge discretization** or **PCA path construction** concentrates most variance into the first few QMC coordinates, where Sobol' sequences have the strongest uniformity. In edge cases (specific barrier structures) this does not hold — GSA identifies those.

**Methodology:** tests pricing and Greek convergence across Asian, barrier, cliquet payoffs. Speed-up analysis shows ~10× accuracy improvements at fixed sample size vs PRN MC. Stability analysis explicitly demonstrates lower variance in the Sobol'+bridge construction.

Relevant to Cemini because: (1) the Cemini stack is CPU-only and needs CPU-efficient Greeks for the options feature layer; (2) `3-29-research-5.md` explicitly prescribes `scipy.stats.qmc.Sobol` based on THIS paper's findings — it is the primary source for the "QMC+FD = AAD at lower code cost" recommendation; (3) GSA Sobol indices give free interpretability on which market factors drive portfolio risk — aligns with the Analytics-Agent FastMCP tool pattern. Honest limits: (a) 2017/2021 paper; the QMC+Sobol' literature has matured further; (b) payoffs tested are European/Asian/barrier/cliquet, not crypto perpetuals or prediction-market binaries — the effective-dimension argument requires re-verification for those; (c) AAD vs QMC+FD trade-off flips when Greeks count is large (basket options with many underlyings) — not Cemini-relevant today but worth noting.

## Key findings

- QMC + Sobol' > PRN MC in pricing, including high-D, with faster and more stable convergence.
- **QMC + FD matches AAD accuracy for small number of Greeks** — huge implementation-effort saving for solo dev.
- GSA Sobol indices explain when QMC wins: Brownian bridge or PCA path construction reduces effective dimension, concentrating variance in first Sobol' coordinates.
- Tested payoffs: European vanilla, Asian, barrier knock-outs, cliquet.
- ~10× accuracy speed-up at fixed sample size vs PRN MC.
- GSA Sobol indices double as a risk-driver explainability tool.
- Directly sourced by Cemini's prescription in `3-29-research-5.md` to use `scipy.stats.qmc.Sobol` + central FD.
- Caveat: specific barrier structures can have effective dimensions that resist reduction — GSA identifies them.

## Snippets

- **Abstract** — "QMC outperforms MC in most cases, including the highest-dimensional simulations, showing faster and more stable convergence."
- **Abstract** — "when the number of greeks is small, the FD approach combined with QMC can lead to the same accuracy as AAD, thanks to increased convergence rate and stability, thus saving a lot of implementation effort while keeping low computational cost."
- **Abstract** — "Using GSA, we are able to fully explain our findings in terms of reduced effective dimension of QMC simulation, allowed in most cases, but not always, by Brownian bridge discretization or PCA construction."
- **§1** — "LDS are designed in such a way that the integration domain is covered as uniformly as possible, while PRN are known to statistically form clusters and holes of points."
