---
title: "Concentrated liquidity AMM dynamic fees vs LVR — agent-based model (arXiv 2606.23070)"
type: source
tags: [source, arxiv, defi, amm, market-making, k128]
keywords: [2606.23070, Uniswap v3, concentrated liquidity, LVR, loss-versus-rebalancing, dynamic fees, adverse selection]
related:
  - concepts/cl-amm-dynamic-fees-lvr.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-lp-rewards-farming.md
  - sources/arxiv-prfs-counterfactual-dex-2606.08228-2026-06-16.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
clusters: [market-microstructure, crypto, prediction-markets]
---

## Relations

- @concepts/cl-amm-dynamic-fees-lvr.md — K128 synthesis
- @concepts/polymarket-bot-architecture.md — LP adverse-selection steal for PM retail bot
- @concepts/polymarket-lp-rewards-farming.md — maker-side yield complement

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Mitigating Adverse Selection in Concentrated Liquidity AMMs with Dynamic Fees: An Agent-Based Model Approach |
| **Authors** | Daniele Maria Di Nosse, Fabrizio Lillo (Scuola Normale Superiore, Pisa) |
| **arXiv** | 2606.23070v1 (Jun 2026) |
| **sha256** | `6954b322cda7ce317a87667f9c3f7e62bbaffbc941093ffb7a42a4cb2c737c8f` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.23070-2606.23070v1-mitigating-adverse-selection-in-con.pdf` |
| **Retrieved** | 2026-06-24 (inbox) |
| **Read status** | read (abstract + intro + headline finding) |

## Narrative

Agent-based model of **Uniswap v3** concentrated-liquidity pool vs Heston-vol reference market. Incorporates block propagation, mempool latency, arbitrageurs, smart routers, MEV searchers, and active LPs vs frictionless rebalance benchmark.

**LVR (loss-versus-rebalancing):** delta-hedged LP PnL = fees − LVR; LVR captures adverse selection from stale AMM prices vs informed flow [TENTATIVE — formal defs in paper §1].

**Dynamic fee schedules:** volatility + order-flow toxicity proxies. Finding: dynamic fees improve **hedged LP profitability mainly by raising fee income in stale-price states** — compensates LVR more directly than reducing realized LVR [TENTATIVE — aggregate sim result].

**Cemini steal:** PM/Kalshi **retail LP** should treat spread/rebate as **state-dependent compensation for toxic flow**, not static tier — maps to `@concepts/polymarket-lp-rewards-farming.md` and pm-kalshi brief.

## Snippets

> "Dynamic fee adjustments can improve hedged LP profitability mainly by increasing fee income in states associated with stale-price risk." [Source: arXiv:2606.23070 abstract (retrieved 2026-06-24)]

> "LVR is the loss an LP suffers due to adverse selection: because AMMs execute trades at stale prices, informed arbitrageurs extract value when prices move." [Source: arXiv:2606.23070 §intro (retrieved 2026-06-24)]

## Dead Ends

- DeFi on-chain sim ≠ Polymarket CLOB fee model — steal is **economic framing**, not parameter transplant without backtest.
