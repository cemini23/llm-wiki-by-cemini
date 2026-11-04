---
title: "Nonparametric GARCH — an iterated neural estimator with minimax rates"
type: source
tags: [source, arxiv, garch, volatility, neural-estimation, statistics]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-04
updated: 2026-11-04
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Nonparametric GARCH: An Iterated Neural Estimator |
| Authors | Ruizhi Deng, Guohao Shen (Hong Kong Polytechnic University), Ngai Hang Chan (City University of Hong Kong) |
| arXiv | 2611.04157 [stat.ML] |
| Pages | 69 |
| Read status | skimmed (abstract and title page) |

## Narrative

GARCH assumes the conditional variance is a known parametric function of the past. This paper drops that assumption and estimates the **recursion map itself** nonparametrically with a neural network.

### The estimator

An **iterated** scheme that alternates between two steps:

1. Estimate the recursion map.
2. Update the unobserved conditional variances.

The unknown variances are latent, so neither step can be solved alone. Alternating is the standard answer to that circularity, and the paper's contribution is the rate analysis rather than the loop.

### The results that matter

Under mild conditions they establish **finite-sample bounds** for the time-averaged in-sample variance-path error, and show the estimator is **minimax rate-optimal up to logarithmic factors**. Under stationarity and mixing they get the same rate for the recursion map, plus finite-sample bounds for out-of-sample variance forecasts and **expected excess QLIKE loss**.

**The practically useful finding is about misspecification:** the convergence rates depend on the true lag orders and **remain unchanged when the fitted orders are overspecified**.

That is a reassuring property. In applied work the lag order is a guess; a method whose rate degrades when you over-guess is fragile, and this one does not. It says you can err large on the order and pay little.

### Why it is filed here

Volatility modelling underpins the options and risk side of this workspace — the crypto surface repair paper from the 2026-11-03 batch is the same problem from the pricing end, and regime watches are the same problem from the signal end.

The abstract also notes the method "can incorporate option-price and high-frequency information", which is the bridge from a pure price-series GARCH to a surface-aware variance model.

**Caveat.** Abstract only. No empirical comparison, no simulation magnitude, and no statement of computational cost is reproduced here.

## Snippets

> "We propose an iterated neural estimator that alternates between estimating the recursion map and updating the unobserved conditional variances." [Source: arxiv-2611.04157 p.1]

> "The convergence rates depend on the true lag orders and remain unchanged when the fitted orders are overspecified." [Source: arxiv-2611.04157 p.1]

## Dead Ends

- **Citing an empirical improvement.** Abstract only.
- **Assuming it beats parametric GARCH out of sample.** The abstract says "competitive", which is not the same claim.
