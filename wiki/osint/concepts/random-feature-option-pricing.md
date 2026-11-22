---
title: Random-feature solvers for option pricing and calibration
type: concept
maturity: draft
related:
  - sources/arxiv-pirannn-random-feature-pricing-2611.19792.md
  - concepts/options-derivatives.md
  - concepts/local-stochastic-volatility-calibration.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: when does a training-free random-feature solver beat a neural pricing network, and where does it still lose to finite differences?

Built from one paper, Bansal, Iyer and Jain (arXiv 2611.19792, 2026-11-15).

## Narrative

**The construction.** Fix the inner weights of a one-hidden-layer network at random, use a probit activation, and fit the output weights by regularised least squares. The fit targets the pricing equation, the payoff and the boundary conditions at once. There is no gradient training. Because the problem is linear in the output weights, one factorisation gives prices at every state and time, the Greeks, and the exact parameter derivatives.

**Where it helps.** Repeated valuation. Calibration needs the price and its parameter derivatives at many trial parameter vectors. A single least-squares factorisation supplies both. For Merton and Kou jump models, each feature has an explicit jump integral, so no quadrature is needed.

**Accuracy.** The method roughly matches a Crank-Nicolson finite-difference scheme at equal run time. A finite-difference scheme that also subtracts the Black-Scholes price is about two orders of magnitude more accurate. So the fair claim is speed and convenience, not accuracy.

**The calibration lesson, which generalises beyond this method.** Fitting the quotes does not prove the parameters are right. If the pricing error is large relative to the sensitivity of price to the parameter, the optimiser finds a wrong parameter set that still fits. In the paper, jump parameters miss by up to 50% without Black-Scholes subtraction and land within 3% with it. Any calibrator, neural or not, needs a pricing-error check against parameter sensitivity.

**Benchmark result.** On the test problems of a physics-informed neural network study, the method matched that network's accuracy in seconds rather than about half an hour.

**Limits.** It is a European-option study with known reference prices. Heston and SABR are an applicability check with a 1% pricing error and about 15% parameter error. Continuously monitored barriers and path-dependent products are named as future work, not shown.
