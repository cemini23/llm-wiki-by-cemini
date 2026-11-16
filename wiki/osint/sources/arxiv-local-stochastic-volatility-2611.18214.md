---
title: "Local Stochastic Volatility Iterations (2611.18214)"
type: source
maturity: draft
related:
  - concepts/local-stochastic-volatility-calibration.md
updated: 2026-11-16
---

## Raw Concept

- **Title:** Local Stochastic Volatility Iterations
- **Authors:** Christian Bayer, Denis Belomestny, Paul P. Hager, John Schoenmakers
- **Type:** arXiv preprint, mathematical finance
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2611.18214-local-stochastic-volatility-iterations.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18214
- **Read status:** skimmed (abstract + introduction)

## Narrative

A calibration method for local stochastic volatility models. The leverage factor is found by fixed-point iteration: simulate with the current factor, then approximate the conditional expectation of stochastic variance given spot with a single regression over time and state, using a quasi-likelihood loss for positive responses.

The output is deliberately small. The leverage factor is a smooth function of time and spot with relatively few coefficients, which can then be refined directly against option quotes.

The test is a recalibration to S&P 500 index options on a rate-announcement day, holding the parameters of a two-factor Bergomi model that was calibrated four weeks earlier. After five iterations, leverage factors with 63 and 143 coefficients reproduce the fitted implied-volatility surface within a few basis points across quoted strikes — the smaller one except in the left wing. A few regularised Gauss-Newton steps then place 87% and 95% of liquid quotes inside their bid-ask intervals.

Relevance: a recalibration routine that needs only a handful of iterations and a compact representation, and that is evaluated on the surface shape rather than on a single loss number.

[Source: arxiv-2611.18214-local-stochastic-volatility-iterations.pdf]

## Snippets

> "After five iterations, leverage factors with 63 and 143 coefficients reproduce the implied volatility surface fitted to the quotes within a few basis points."

> "A few regularized Gauss–Newton steps against the quotes then bring 87% and 95% of the liquid quotes inside their bid–ask intervals."
