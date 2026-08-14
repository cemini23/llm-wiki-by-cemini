---
title: "A DEX Implied Volatility Proxy — Uniswap v3 fee-IV (arXiv 2608.13340)"
type: source
tags: [arxiv, defi, volatility, amm, uniswap, xsp, pm, k237]
keywords: [fee-IV, fee implied volatility, Uniswap v3, LVR, loss-versus-rebalancing, Panoptic, DEX, sigma_fee, realized volatility]
related:
  - concepts/dex-fee-implied-volatility.md
  - concepts/cl-amm-dynamic-fees-lvr.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/kalshi-retail-lp.md
  - concepts/polymarket-bot-architecture.md
  - sources/eval-url-revenue-opportunity-2026-08-14.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
read_status: read
---

## Relations

- @concepts/dex-fee-implied-volatility.md — the σ_fee proxy + non-identification result
- @concepts/cl-amm-dynamic-fees-lvr.md — K128 LVR / dynamic-fee sibling
- @concepts/xsp-lane-trading-framework.md — cross-venue signal routing
- @concepts/pm-canary-kalshi-poly.md — prediction-market IV cross-check
- @sources/eval-url-revenue-opportunity-2026-08-14.md — K237 eval batch companion

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.13340, "A DEX Implied Volatility Proxy" |
| Author | Amy Oumayma Khaldoun (sqv3.com) |
| Retrieved | 2026-08-14 |
| File | `arxiv-2608.13340-fee-implied-volatility-on-uniswap-v3-a-dex-nativ.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |
| Type | q-fin.MF preprint, 20pp, single author |

## Narrative

Derives an **oracle-free, on-chain observable "fee implied volatility proxy"** for Uniswap v3/v4 and Panoptic:

**σ_fee = 2·feeRate·√(Volume / L_tick)**

Best interpreted as a **fee-based activity index**, NOT a Black–Scholes-consistent structural IV. Proves (Prop. 2) the structural volatility is **not identified** from pool observables alone: fee income captures only the compensation leg of a narrow-range LP position; the hedging-cost leg (predictable loss / **LVR = σ²/8**) is unobserved.

### Key results

- Empirical ETH/USDC 30bps pool vs ETH-spot realized vol, daily Jan 2023–Jul 2026 (N=1276): Corr(IV, RV) = **0.87**; mean IV−RV spread 3.53 pp; IV>RV on 68.26% of days; mean α̂_RV = (IV/RV)² = 1.33 (median 1.18, IQR [0.92, 1.53], max 11.33).
- Fee tiers {0.0005, 0.0030, 0.01} ↔ tick spacings {10, 60, 200}; minimal percent widths ≈ 0.10% / 0.60% / 2.02%; **tS ≈ 2·10⁴·feeRate**.
- Windowed estimator: σ_fee,[t0,t1] = 2·feeRate·√(Volume[t0,t1] / L̄_tick,[t0,t1]) — Volume summed over swap events, L̄_tick time-averaged active liquidity.
- Tick-level attribution hard (Uniswap doesn't store per-tick cumulative volume → pool-state reconstruction); **pool-level proxy is feasible**.
- Structural non-identification (Prop. 2): α (fee-capture share of full short-option cost) depends on external price process, arbitrage speed, informed-vs-uninformed flow mix, sampling scale. Correction path: estimate arbitrage flow share + α̂, then σ̂_* = σ_fee/√α̂.

### Use as a signal

Concrete implementable DEX-side volatility/flow regime indicator for cross-venue PM×Kalshi×DEX frameworks: compare DEX σ_fee against Polymarket/Kalshi implied vol or realized vol; α̂ ratio is a DEX-side variance-risk-premium gauge. Treat as activity/flow signal, not calibrated IV — do not price off it directly without a microstructure filter. Pool choice matters (fee tier is in the formula → normalize or fix tier when comparing).

**Brief:** `briefs/pm-k237-uniswap-fee-iv.md` → cemini-prod (scp'd). Tier: `[TENTATIVE]` — single-author preprint, single empirical pool; math self-contained and citable.
