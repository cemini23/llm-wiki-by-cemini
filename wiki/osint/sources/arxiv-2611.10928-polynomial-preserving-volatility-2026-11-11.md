---
title: "Polynomial-preserving processes — exact moments for discrete-time volatility models"
type: source
tags: [source, arxiv, volatility, discrete-time, moments, derivative-pricing]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Polynomial-Preserving Processes and Volatility Modelling in Discrete Time |
| Authors | Maciej Augustyniak, Alexandru Badescu, Zekun Zhang |
| arXiv | 2611.10928 |
| Pages | 91 |
| Read status | skimmed (abstract) |

## Narrative

A discrete-time framework for volatility modelling and derivative pricing built on **polynomial preservation**.

The property: **exact moments of arbitrary order, and serial cross-moments of variance and return processes, over any finite horizon** — through finite-dimensional matrix representations.

That is unusual. Most discrete-time volatility models either give you moments by simulation or give you closed forms only for low orders. Exact moments at arbitrary order make certain calculations — tail-sensitive risk measures, high-order hedging — analytically available rather than estimated.

And the tractability is maintained while **accommodating flexible leverage and variance-of-variance dynamics and non-Gaussian innovations** — the three features usually traded away to get closed forms.

### The convergence result

Under two scaling regimes, they establish **weak convergence to polynomial diffusions and jump-diffusions**, and convergence of polynomial moments — linking discrete-time moment recursions to continuous-time matrix-exponential formulas.

So the discrete model is not a separate world: it converges to the continuous one it approximates. That is what makes a discrete-time model defensible for pricing rather than only for filtering.

**Caveat.** Abstract only; 91 pages, title and abstract read. No numerical result reproduced.

## Snippets

> "The framework provides exact moments of arbitrary order and serial cross-moments of variance and return processes over any finite horizon through finite-dimensional matrix representations." [Source: arxiv-2611.10928 p.1]

## Dead Ends

- **Citing a model fit.** Abstract only.
