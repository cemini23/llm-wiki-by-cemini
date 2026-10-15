---
title: "Finite-Sample Guarantees for Fully Discrete Conditional Diffusion Models"
type: source
tags: [arxiv, diffusion, theory, sample-complexity]
keywords: [finite-sample guarantee, discretisation, KL divergence, total variation, score evaluation]
related:
  - concepts/k291-image-gen-wave.md
maturity: draft
read_status: skimmed
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-image-gen-wave.md — K291 image-gen wave hub

## Raw Concept

Title: Finite-Sample Guarantees for Fully Discrete Conditional Diffusion Models
Author: Qiuyun Zhu (University of Iowa)
Type: arXiv preprint (2610.13851)
Location: `research to be indexed/image-gen/arxiv-2610.13851-finite-sample-guarantees-for-fully-discrete-cond.pdf`
Retrieved: 2026-10-14
Read status: skimmed

## Narrative

**The methodological move:** align the **score-training objective with the sampling grid**, so **statistical estimation error and numerical discretisation error are analysed together** rather than separately. Conditional diffusion guarantees usually handle one and assume away the other.

**Under a smooth conditional density model**, for every smoothness index β > 0, a suitable grid yields:

| Quantity | Bound |
|---|---|
| Averaged conditional KL | $\tilde O_p(n^{-2\beta/(d_x+d_y+2\beta)})$ |
| Average target TV error | $\tilde O_p(n^{-\beta/(d_x+d_y+2\beta)})$ |

Here *n* is sample size and $d_x, d_y$ the data and conditioning dimensions, with errors averaged over the conditioning variable. Holds **with or without early stopping**. The TV rate **matches existing conditional distribution-estimation theory up to logarithmic factors**.

**Why it is filed here:** it quantifies **how many score evaluations a given accuracy requires** — a budget question for anyone sizing a diffusion sampler — and it is the theory counterpart to the wave's practical papers.

## Snippets

> "Our approach aligns the score-training objective with the sampling grid, allowing statistical estimation and numerical discretization errors to be analyzed together." [Source: arxiv-2610.13851 p.1]

> "Both the full and early-stopped samplers attain average target total-variation (TV) error $\tilde O_p(n^{-\beta/(d_x+d_y+2\beta)})$." [Source: arxiv-2610.13851 p.1]

## Dead Ends

- Reading the bounds as tight. They match existing rates **up to logarithmic factors**, and the constants are not the point.
