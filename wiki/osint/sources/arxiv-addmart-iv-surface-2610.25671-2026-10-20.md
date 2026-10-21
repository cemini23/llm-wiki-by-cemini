---
title: "ADDMART — arbitrage-free implied-volatility surface reconstruction"
type: source
related:
  - concepts/k293-osint-wave.md
  - concepts/fomc-iv-surface-dynamics.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: Arbitrage-Free Implied Volatility Surface Reconstruction via Additive Martingales
Authors: Haochen Luo, Sifan Lin, Xiaolong Luo, An Binh Minh, Yuan Zhang, Chen Liu (City University of Hong Kong; Shanghai University of Finance and Economics)
Type: arXiv preprint (2610.25671)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.25671-arbitrage-free-implied-volatility-surface-recons.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract and introduction)

## Narrative

Desks need a continuous implied-volatility surface. The market quotes a sparse grid. Learning methods such as HyperIV fit that grid in one forward pass, but they enforce butterfly and calendar constraints with penalties on a finite grid. Those penalties trade accuracy against regularity, and a direct IV prediction can imply a negative risk-neutral density.

ADDMART does not predict IVs. It maps a few quotes to non-negative increment densities of an exponential additive martingale, then recovers call prices and IVs. Static no-arbitrage holds by the martingale construction, so training does not add an arbitrage penalty. The marginals support option-implied VaR, CVaR, and crash probabilities without a Breeden-Litzenberger derivative.

On ten real-option datasets, five seeds, and **2,500 audited model-date surfaces over a 16-month test**, the authors report competitive reconstruction accuracy and **no material butterfly or calendar violations**, with no per-surface optimisation at inference.

This sits next to GROMM (@sources/arxiv-gromm-risk-neutral-option-market-2610.16732-2026-10-14.md). GROMM models the surface as a state. ADDMART rebuilds a sparse surface so the density stays valid. **No trade. No wire.**

## Snippets

> "By incorporating the no-arbitrage structure directly into its architecture, rather than enforcing it through regularization in the learning objective, ADDMART produces IV surfaces that satisfy static no-arbitrage conditions throughout the domain." [Source: arxiv-2610.25671 p.1]
