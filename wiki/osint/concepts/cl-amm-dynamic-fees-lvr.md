---
title: Concentrated liquidity AMM dynamic fees and LVR compensation
type: concept
tags: [concept, defi, amm, market-making, lp, k128]
keywords: [LVR, loss-versus-rebalancing, concentrated liquidity, dynamic fees, adverse selection, Uniswap v3, hedged PnL]
related:
  - sources/arxiv-cl-amm-dynamic-fees-lvr-2606.23070-2026-06-24.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/active-project-research-routing.md
  - concepts/cl-amm-dynamic-fees-lvr.md
  - sources/arxiv-prfs-counterfactual-dex-2606.08228-2026-06-16.md
  - sources/arxiv-2608.13340-uniswap-fee-iv-2026-08-14.md
  - concepts/dex-fee-implied-volatility.md
maturity: draft
created: 2026-06-24
updated: 2026-08-14
---

## Relations

- @sources/arxiv-cl-amm-dynamic-fees-lvr-2606.23070-2026-06-24.md — K128 primary source
- @concepts/polymarket-bot-architecture.md — retail CLOB bot LP steal
- @concepts/polymarket-lp-rewards-farming.md — maker rebate context

## Raw Concept

Prompted by arXiv **2606.23070** (K128). How should liquidity providers price **adverse selection** when flow is informed and quotes are stale?

## Narrative

**LVR framing:** LP hedged PnL ≈ fees − **loss-versus-rebalancing** — the cost of providing liquidity at prices that lag the reference market when arbitrageurs trade against stale quotes.

**Dynamic fee hypothesis (Di Nosse & Lillo, 2026):** fee schedules tied to **volatility** and **order-flow toxicity** can restore positive hedged PnL primarily by **increasing fee income in high stale-price-risk states**, not necessarily by reducing realized LVR.

### PM/Kalshi translation [TENTATIVE]

| DeFi AMM concept | PM retail LP analog |
|------------------|---------------------|
| Stale pool price vs external ref | CLOB mid vs external oracle / cross-venue fair |
| LVR | Toxic taker flow on one-sided books |
| Dynamic fee bump | Widen spread / reduce size when vol or flow imbalance spikes |
| Hedged LP PnL | Maker rebate − inventory risk − resolution jump risk |

**Steal for pm-kalshi-bot:** treat static spread tiers as **insufficient** — gate quote width on vol + recent fill toxicity (see K128 brief).

## Snippets

> "Dynamic fee adjustments can improve hedged LP profitability mainly by increasing fee income in states associated with stale-price risk." [Source: arXiv:2606.23070 abstract (retrieved 2026-06-24)]

## Dead Ends

- Uniswap v3 agent-based parameters do not calibrate directly to Polymarket tick size — require `run_pm_lp_backtest.sh` tier refresh before prod.
