---
title: Variance option short-maturity asymptotics under rough volatility
type: concept
maturity: draft
related:
  - sources/arxiv-large-deviations-integrated-exponentials-volterra-2611.34567.md
  - concepts/rough-log-normal-volatility.md
  - concepts/local-stochastic-volatility-calibration.md
updated: 2026-11-26
---

## Raw Concept

Question this page answers: how fast do options on realised variance decay near expiry in a rough volatility model, and why does the Hurst exponent set the rate?

From Jacquier, Oumgari, Pirjol and Zhu, "Large deviations for integrated exponentials of Gaussian Volterra processes" (arXiv:2611.34567, 2026-11-25).

## Narrative

### The setup

A variance option pays on realised variance. In a rough volatility model the instantaneous volatility is `σ_t = σ(Y_t)` with `Y` a fractional or Volterra Gaussian process. Realised variance is then the time average of `exp(2Y)`, that is, the integral of an exponential of a Gaussian process divided by `T`.

Pricing a short-dated variance option means knowing how that average behaves as `T` goes to zero. The exponent is Gaussian, so the average sits between two limits: typical paths keep it near its mean, and rare paths dominate the tail.

### The decay rate

The main result of the paper is a large deviation principle for the normalised integral, plus a central limit theorem and a moderate deviation principle. The practical consequence is a rate: **at-the-money variance options decay like `T^H`**, where `H` is the Hurst exponent of the volatility process.

The comparison that makes this useful:

| Instrument | At-the-money decay |
|---|---|
| European option on the asset | `√T` |
| Variance option, rough volatility | `T^H` |

With equity-index `H` near 0.1, `T^H` decays far more slowly than `√T` for small `T`. That is the mathematical reason short-dated variance can stay expensive while short-dated vanilla options cheapen fast.

### Why the kernel matters

The constant in front of `T^H` is not universal. The two common rough-volatility kernels, Molchan-Golosov and Riemann-Liouville, give constants that differ by a factor of `√(8H)/(2H+1)`, which is one only at `H = 1/2`. So a practitioner who takes a constant from one kernel and applies it to the other gets a wrong price. This is the most transferable warning on the page.

### What it does not give

- It is asymptotic in `T`. It is not a finite-maturity pricing formula.
- The validation is numerical, in the rough Bergomi model. It is not a market calibration and not a test of fit to option data.
- The rate function is fully explicit only at `H = 1/2` and in a few special cases.

### Where it sits

This is the variance-option counterpart to the short-maturity smile literature for European options (Forde and Zhang, Fukasawa, Friz-Gassiat-Pigato). A related workspace paper, @concepts/rough-log-normal-volatility.md, handles a different problem: keeping a rough model arbitrage-free under positive spot-volatility correlation. Together they cover the two questions that decide whether a rough model is usable — does it price the tail, and is it a martingale.

### Read

Reference only. No Cemini project prices variance options. Keep the `T^H` rate and the kernel-constant warning; those transfer to any rough-volatility work in this wiki.
