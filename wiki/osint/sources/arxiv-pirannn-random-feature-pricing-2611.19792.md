---
title: "PIRanNN — random-feature pricing and calibration under jump-diffusion and stochastic volatility"
type: source
maturity: draft
related:
  - concepts/random-feature-option-pricing.md
  - concepts/options-derivatives.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | PIRanNN: Random-Feature Pricing and Calibration under Jump-Diffusion and Stochastic-Volatility Models |
| Author | Saurabh Bansal, Srikanth K. Iyer, Shashi Jain |
| Type | arXiv preprint, q-fin.CP |
| Location | `research to be indexed/osint/arxiv-2611.19792-pirannn-random-feature-pricing-and-calibration-u.pdf` |
| Retrieved | 2026-11-22 |
| arXiv | 2611.19792v1, 15 Nov 2026 |
| Pages | 29 |
| Read status | read |

## Narrative

The paper prices and calibrates European options under four models: Merton and Kou jump-diffusion, and Heston and SABR stochastic volatility. The price function is approximated by a one-hidden-layer network with fixed random inner weights and a probit activation. Training is replaced by one regularised least-squares fit to the pricing equation, the payoff and the boundary conditions. There is no iterative training. [Source: arxiv-2611.19792-pirannn-random-feature-pricing-and-calibration-u.pdf p.1]

For Merton and Kou, each feature has an explicit jump integral, so the solver needs no quadrature. One factorisation of the least-squares matrix returns the price at every state and time, the Greeks, and the exact parameter derivatives. Those derivatives feed Gauss-Newton or Levenberg-Marquardt calibration.

The main practical result is about calibration, not pricing. A solver can fit the quotes and still return wrong parameters when the pricing error is not small compared with the parameter effect. Without subtracting the Black-Scholes price, the fitted jump parameters miss by up to 50%. With the subtraction, they land within 3%. [Source: arxiv-2611.19792-pirannn-random-feature-pricing-and-calibration-u.pdf p.1]

On speed and accuracy, the method roughly matches a Crank-Nicolson finite-difference scheme at the same run time. A finite-difference scheme that also subtracts Black-Scholes is about two orders of magnitude more accurate. Against a recent physics-informed neural network benchmark, the method matches that network's accuracy in seconds instead of about half an hour.

For Heston and SABR the study is an applicability check with boundary conditions that need no reference prices. Pricing error is about 1%, and calibrated parameters land within about 15% of the true values.

The honest read: this is a fast, training-free solver with a real calibration-error lesson. It does not beat a well-built finite-difference scheme on accuracy. The value is speed for many repeated valuations, and the parameter-recovery diagnostic.

## Snippets

> "The calibration experiments show that a solver can fit the quotes and still return wrong parameters when its pricing error is not small compared with the effect of the parameters on the prices." [Source: arxiv-2611.19792-pirannn-random-feature-pricing-and-calibration-u.pdf p.1]
