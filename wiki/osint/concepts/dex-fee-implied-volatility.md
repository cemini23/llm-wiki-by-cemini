---

title: "DEX fee-implied volatility — oracle-free volatility/flow proxy (σ_fee = 2·feeRate·√(V/L))"
type: concept
tags: [concept, defi, volatility, uniswap, amm, xsp, pm, k237]
keywords: [fee-IV, fee implied volatility, sigma_fee, Uniswap v3, LVR, Panoptic, oracle-free, flow-intensity, variance-risk-premium]
related:
  - sources/arxiv-2608.13340-uniswap-fee-iv-2026-08-14.md
  - concepts/cl-amm-dynamic-fees-lvr.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/kalshi-retail-lp.md
  - concepts/polymarket-bot-architecture.md
  - sources/eval-url-revenue-opportunity-2026-08-14.md
  - concepts/pm-canary-kalshi-poly.md
maturity: draft
created: 2026-08-14
updated: 2026-10-25
---

## Relations

- @sources/arxiv-2608.13340-uniswap-fee-iv-2026-08-14.md — primary source
- @concepts/cl-amm-dynamic-fees-lvr.md — K128 LVR/dynamic-fee sibling
- @concepts/xsp-lane-trading-framework.md — cross-venue signal routing
- @concepts/pm-canary-kalshi-poly.md — PM implied-vol cross-check

## Raw Concept

What this page answers: can we get an implied-volatility proxy for a DEX pool from on-chain observables alone, without an oracle? Synthesized from "A DEX Implied Volatility Proxy" (arXiv 2608.13340).

## Narrative

**σ_fee = 2·feeRate·√(Volume / L_tick)** — a closed-form, oracle-free proxy from pool observables (fee rate, swap volume, active liquidity at current tick). Interpretation: a **fee-based activity index** — how intense is fee-generating trading flow relative to the liquidity absorbing it.

### Why it's not structural IV (Prop. 2)

A narrow-range Uniswap v3 position ≈ a short-dated option: short-option PnL = **Fees + HedgingCost**, and the hedging cost leg is **LVR = σ²/8**. Fee income captures only the compensation leg; the omitted leg depends on the external price process, arbitrage timing/speed, informed-vs-uninformed flow mix — so structural volatility is **not identified** from feeRate/Volume/L_tick alone. Raising the fee tier raises σ_fee with an unchanged price process; retail/inventory flow can raise volume with flat price.

### Empirical anchor

ETH/USDC 30bps pool, daily Jan 2023–Jul 2026 (N=1276): Corr(σ_fee, realized vol) = **0.87**; IV>RV on 68.26% of days; mean α̂ = (IV/RV)² = 1.33 — a DEX-side **variance-risk-premium gauge**.

### Use as a cross-venue signal (xsp/pm)

Concrete implementable signal for the cross-venue PM×Kalshi×DEX framework:

- Windowed estimator: σ_fee,[t0,t1] = 2·feeRate·√(Volume[t0,t1] / L̄_tick,[t0,t1]) — Volume summed over swap events, L̄_tick time-averaged active liquidity; **pool-level feasible** (tick-level requires pool-state reconstruction).
- Compare DEX σ_fee vs Polymarket/Kalshi implied vol or realized vol → regime/flow divergence readout; α̂ ratio as variance-risk-premium gauge.
- **Treat as activity/flow signal, not calibrated IV** — do not price off it directly without a microstructure filter. Fix or normalize the fee tier when comparing pools.

**Brief:** `briefs/pm-k237-uniswap-fee-iv.md` → cemini-prod (scp'd). Tier: `[TENTATIVE]` (single-author preprint, single pool) — math self-contained.
