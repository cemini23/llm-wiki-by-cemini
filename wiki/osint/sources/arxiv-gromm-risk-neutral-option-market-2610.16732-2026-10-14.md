---
title: "GROMM — Generative Risk-neutral Option Market Models"
type: source
tags: [arxiv, options, volatility, arbitrage, quant-finance]
keywords: [option market model, local volatility, arbitrage-free, SANOS, S&P index options, BHW test]
related:
  - concepts/k291-osint-wave.md
  - concepts/fomc-iv-surface-dynamics.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-osint-wave.md — K291 osint wave hub
- @concepts/fomc-iv-surface-dynamics.md — an option-surface model whose state is directly observable

## Raw Concept

Title: GROMM — Generative Risk-neutral Option Market Models
Authors: Magnus Wiese, Hans Buehler, Blanka Horvath (Oxford Mathematical Institute; Oxford-Man Institute)
Type: arXiv preprint (2610.16732)
Location: `research to be indexed/osint/arxiv-2610.16732-gromm-generative-risk-neutral-option-market-mode.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**A statically and dynamically arbitrage-free European option market model** with smooth interpolation between option prices, built on the SANOS framework, with a proof that its dynamics admit a **unique strong solution**. It sits inside the **stochastic local volatility** family.

The framing matters more than the construction:

> It is a stochastic model for local volatility **when the latter is used as a representation of a European option price surface, not as a pricing model.**

That is, the option surface is treated as the **state variable** to be modelled and interpolated, rather than as an output of an underlying price process.

### Evidence

| Claim | Value |
|---|---|
| Initial state fits inside bid/ask | **>95%** of relevant market option prices |
| Data | S&P Index options, January 2022 – August 2025 |
| Training | Under both **P** and **Q** |
| Arbitrage | Statically and dynamically free, verified after training |
| New tooling | A range of **BHW tests** for absence of arbitrage |

### Why it is filed here

**Surface-first modelling is the contrast to this wiki's usual treatment.** Most option material here starts from a price process and derives a surface. GROMM inverts that: the surface is observable, so it is the state. The >95% bid/ask fit is a strong practical result for anyone marking or interpolating an index surface.

**Status: desk-relevant, no trade, no wire.** No Cemini implementation.

## Snippets

> "We present a statically and dynamically arbitrage-free European option market model with smooth interpolation between option prices ... and prove that its dynamics admit a unique strong solution." [Source: arxiv-2610.16732 p.1]

> "In spirit, it is a stochastic model for local volatility when the latter is used as a representation of a European option price surface, not as a pricing model." [Source: arxiv-2610.16732 p.1]

> "We show that the model's initial state fits within bid/ask for more than 95% of relevant market option prices." [Source: arxiv-2610.16732 p.1]

## Dead Ends

- Reading GROMM as a directional signal. It is a surface representation and interpolation model; it makes no claim about future returns.
