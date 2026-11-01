---
title: "Marginal composite likelihood for Bergomi models from option prices"
type: source
tags: [source, arxiv, rough-volatility, bergomi, options]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Marginal Composite Likelihood Estimation of Bergomi Models from High-Frequency Option Prices |
| Authors | Haruki Tomita, Graduate School of Engineering Science, The University of Osaka |
| arXiv | 2610.40425 |
| File | `arxiv-2610.40425-marginal-composite-likelihood-estimation-of-berg.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.40425 |
| Read status | skimmed (abstract + intro) |

## Narrative

The paper builds a parametric inference theory for Bergomi-type models. The unknown object is a positive forward-variance kernel. The kernel may be singular at the origin. The data are high-frequency observations across time and maturity. The paper title names the method as marginal composite likelihood estimation. The introduction states the aim as joint estimation of the kernel parameters. This is a single source (arXiv:2610.40425v1, 29 Oct 2026, math.ST).

Rough volatility models describe volatility with low local regularity. The text ties that roughness to a Hurst parameter below one half, and to the short-maturity implied-volatility skew. In the forward variance framework, the rough Bergomi model encodes the irregularity with a singular power-law kernel. The principal example is \(k_\theta(x) = \eta x^{H-1/2}\), with \(\theta = (\eta, H)\), \(\eta > 0\), and \(0 < H \leq 1/2\). For \(H < 1/2\), the variance dynamics match the rough Bergomi model. \(H\) sets the singularity at the origin and the local regularity of volatility. The kernel sets how one common shock moves variance across maturities. The theory also covers regular positive kernels.

The model runs under a martingale measure equivalent to the physical measure, on the interval from 0 to 1. One Brownian motion drives the state. Spot variance is the exponential of the kernel integral against that Brownian motion, with a negative quadratic compensator. The initial variance curve is positive and deterministic. The normalization makes expected spot variance equal to that curve. Forward variance \(V^u_t\) then satisfies \(dV^u_t / V^u_t = k_\theta(u-t)\, dW_t\) for \(t < u\). The forward variance curve is an infinite-dimensional state driven by that single Brownian motion.

The forward variance curve is not observed. The paper uses cumulative forward variance from \(t\) to a horizon \(T\). Under standard integrability conditions, that integral equals two strike integrals of put and call prices, each weighted by \(2/K^2\). The asset price is a strictly positive continuous martingale with spot variance \(V_t\). The paper excludes asset-price jumps. It sets interest rates and dividends to zero.

The only numeric bounds in this text are the kernel restrictions \(\eta > 0\) and \(0 < H \leq 1/2\). They are model assumptions in this single source, not estimated values. The text quotes no sample size, rate, standard error, or fitted \(H\). The introduction says that option-based study of rough volatility remains limited relative to work that uses returns and realized variance. For a quant-finance reader, the claim is a pricing-measure map from a high-frequency option panel to the kernel that links maturity slices of forward variance. No macro series appears in this text.

## Snippets

> "Motivated by this model, we develop a parametric inference theory for Bergomi-type models with a general class of positive kernels that may be singular at the origin. Our focus is the joint estimation of parameters governing a positive, potentially singular forward variance kernel from high-frequency observations across time and maturity." [Source: `arxiv-2610.40425-marginal-composite-likelihood-estimation-of-berg.pdf` p.1 (arXiv 2610.40425), retrieved 2026-11-01]
