---
title: Calibrating local stochastic volatility by fixed-point iteration
type: concept
maturity: draft
related:
  - sources/arxiv-quantum-local-vol-calibration-2611.25344.md
  - concepts/quantum-local-vol-calibration.md
  - concepts/random-feature-option-pricing.md
  - sources/arxiv-local-stochastic-volatility-2611.18214.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: how do you fit a local stochastic volatility model to a live option surface without a large parameter search?

From Bayer, Belomestny, Hager and Schoenmakers (arXiv 2611.18214).

## Narrative

The structure. An LSV model multiplies a stochastic variance process by a local leverage factor. Gyöngy's Markovian projection gives the calibration identity: the leverage factor times the square root of the conditional expectation of variance given spot must equal Dupire local volatility. That produces a McKean-Vlasov equation of a singular kind, whose general existence and uniqueness remain open.

The practical method. Iterate: simulate with the current leverage factor, regress to approximate the conditional expectation of variance given spot (one regression over time and state, quasi-likelihood loss for positive responses), and update the factor. The output is smooth in time and spot with few coefficients.

Why compactness matters. The factor can be refined directly against option quotes. In the paper's test, holding a two-factor Bergomi calibration from four weeks earlier, five iterations with 63 and 143 coefficients reproduced the surface within a few basis points across quoted strikes — the smaller one except in the left wing. A few regularised Gauss-Newton steps then put 87% and 95% of liquid quotes inside their bid-ask intervals.

The transferable idea is the split: a small global object fitted by iteration, then a local quote-level correction. It avoids re-fitting the stochastic-volatility parameters on every recalibration.

[OPEN QUESTION 2026-11-16] Existence and uniqueness of the underlying equation are open in general; the method is validated numerically, not proved.

## Snippets

> "Each iteration simulates the model with the current leverage factor and approximates the conditional expectation of the stochastic variance given the spot by a single regression in time and state."
