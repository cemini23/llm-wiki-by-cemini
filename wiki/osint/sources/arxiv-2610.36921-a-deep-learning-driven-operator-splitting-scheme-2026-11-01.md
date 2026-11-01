---
title: "Deep learning operator splitting for American options in incomplete markets"
type: source
tags: [source, arxiv, american-options, operator-splitting, incomplete-markets]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Deep Learning-Driven Operator Splitting Scheme for Free Boundary Problems: An Application to American Option Pricing in Incomplete Markets |
| Authors | Dong Yan et al., University of International Business and Economics and Southwestern University of Finance and Economics |
| arXiv | 2610.36921 |
| File | `arxiv-2610.36921-a-deep-learning-driven-operator-splitting-scheme.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.36921 |
| Read status | skimmed (abstract + intro) |

## Narrative

The paper proposes a deep learning operator-splitting scheme for high-dimensional free-boundary problems. American option pricing is the application.

The market has proportional transaction costs, stochastic liquidity risk, and two-factor stochastic volatility. The liquidity risk uses a nonlinear drift. The authors say S&P 500 data validate that drift. They state that the price is a five-dimensional highly nonlinear variational inequality. That dimension count is a single-source claim from this abstract.

At each time layer the scheme splits the variational inequality. A physics-informed neural network approximates an elliptic continuation equation. A closed-form projection step enforces the early-exercise constraint. The authors derive a conditional ℓ∞ stability bound under stated resolvent and Lipschitz assumptions.

The authors compare the scheme with finite-difference solutions and least-squares Monte Carlo solutions. They state that option prices and the learned exercise boundary show close agreement with those reference solutions. The abstract states no error size. "Close agreement" is a single-source claim. The authors also report sensitivity analyses for the key model parameters.

A quant-finance and macro reader can use the paper for American prices when transaction costs, liquidity risk, and two-factor volatility sit in one model. The abstract ties the liquidity drift to S&P 500 data. The scheme returns a price and an exercise boundary for the stated five-dimensional problem. The stability result holds only under the stated assumptions.

## Snippets

> "In a market with proportional transaction costs, a stochastic liquidity risk with an empirically validated nonlinear drift based on S&P 500 data, and two-factor stochastic volatility, the pricing problem takes the form of a five-dimensional highly nonlinear variational inequality. The proposed scheme decomposes this variational inequality at each time layer into an elliptic continuation equation approximated by a physics-informed neural network and a closed-form projection step enforcing the early-exercise constraint." [Source: `arxiv-2610.36921-a-deep-learning-driven-operator-splitting-scheme.pdf` p.1 (arXiv 2610.36921), retrieved 2026-11-01]
