---
title: "Term structure of implied fee rates in AMM liquidity pools"
type: source
tags: [source, arxiv, defi, amm, implied-fees]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Term Structure of Implied Fee Rates in Liquidity Pools |
| Authors | Diogo Duarte et al., Florida International University |
| arXiv | 2610.36392 |
| File | `arxiv-2610.36392-the-term-structure-of-implied-fee-rates-in-liqui.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.36392 |
| Read status | skimmed (abstract + intro) |

## Narrative

Automated market makers pay liquidity providers (LPs) with swap fees. The paper says this compensation is hard to measure before the LP withdraws. Market prices do not show a forward-looking fee return. The LP payoff is nonlinear. It depends on the asset price and on the liquidity range.

The authors build a no-arbitrage framework. They recover implied fee rates from option-implied information. Expected accumulated fees equal the current pool value minus the risk-neutral value of the terminal payoff. Forward-looking LP compensation then reduces to pricing the LP payoff. Under a risk-neutral measure, expected accumulated fees equal the current value of the LP position minus the risk-neutral value of its payoff at the horizon.

They apply the framework to Uniswap v2 and Uniswap v3 ETH–USDC pools. The pricing model is a stochastic-volatility jump-diffusion model. They calibrate it to Deribit options. Uniswap v2 uses an infinite range. Uniswap v3 uses a finite range. The object they recover is the implied total fee return over a horizon for a chosen range.

The abstract states four properties of implied fee rates. The rates are positive. They vary over time. They slope downward in maturity. They are highly sensitive to range design. Tighter near-the-money ranges earn larger implied returns. The abstract quotes no numeric fee rate. These claims come from this paper alone.

A quant-finance reader can treat LP fee compensation as the price of the LP payoff, taken from the options market. A macro reader gets a maturity slope for ETH–USDC pool compensation, plus a range-design effect. The paper reports both results for Uniswap v2 and Uniswap v3.

## Snippets

> "We apply the framework to Uniswap v2 and Uniswap v3 ETH–USDC pools using a stochastic-volatility jump-diffusion model calibrated to Deribit options. Implied fee rates are positive, time varying, downward sloping in maturity, and highly sensitive to range design, with tighter near-the-money ranges earning larger implied returns." [Source: `arxiv-2610.36392-the-term-structure-of-implied-fee-rates-in-liqui.pdf` p.1 (arXiv 2610.36392), retrieved 2026-11-01]
