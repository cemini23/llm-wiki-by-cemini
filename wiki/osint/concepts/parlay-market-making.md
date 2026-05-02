---
title: Parlay Market Making — Correlation-Aware AMM for Joint-Contract Pricing
type: concept
tags: [concept, parlay-market-making, amm-design, prediction-markets, kalshi, ising-model, correlation-aware-pricing, rfq-trilemma]
keywords: [parlaymarket, ising-model, parlay, joint-contracts, shadow-trades, composite-likelihood, rfq-trilemma, automated-market-making, prediction-markets, kalshi-combos, correlation-aware, frechet-bound]
related:
  - sources/kalshi1-3-29.md
  - entities/platforms/kalshi.md
  - concepts/market-microstructure.md
  - concepts/agent-authorization-stack.md
maturity: validated
created: 2026-05-01
updated: 2026-05-01
---

## Relations

- @sources/kalshi1-3-29.md — K24 deep-read; primary source. Rana, Nadkarni, Moshrefi, Viswanath (Princeton, Mar 2026). ParlayMarket: first AMM for parlay-style joint contracts.
- @entities/platforms/kalshi.md — primary Cemini venue; the RFQ trilemma and Fréchet violations directly characterize Kalshi's current combo pricing
- @concepts/market-microstructure.md — cluster hub; parlay market making is the prediction-market dimension of market microstructure
- @concepts/agent-authorization-stack.md — K19+K22+K23+K24 cross-cluster synthesis; Layer 4 (market-design constraints) of the four-layer authorization architecture.

## Raw Concept

Promoted from K24 deep-read of @sources/kalshi1-3-29.md (arXiv:2603.22596v1). The paper introduces the first automated market maker capable of pricing parlay-style joint contracts from a shared liquidity pool — a problem previously thought to require exponential (2^M) capital. The architecture is general: Ising-model belief state + shadow trades + composite-likelihood SGD. This concept page extracts the reusable design primitives and maps them to Cemini's Kalshi trading.

## Narrative

### The problem

Prediction markets with M binary events have a 2^M joint outcome space. Pricing all possible parlays naively requires maintaining prices and risk across all outcomes — exponential capital. Existing platforms (Kalshi, Polymarket) use dealer-mediated RFQ mechanisms that fragment liquidity and violate basic probability constraints. ParlayMarket shows this exponential dependence is not fundamental.

### The RFQ trilemma

Three objectives for parlay-capable market makers:

| Objective | Definition |
|-----------|-----------|
| **Liquidity consistency** | Price impact comparable across base and parlay markets |
| **Information aggregation** | Prices converge to true probabilities as trades accumulate |
| **Bounded loss** | Aggregate market-maker loss remains controlled, scaling subexponentially in M |

An RFQ architecture can satisfy at most two simultaneously. Deployed systems (Kalshi) typically achieve liquidity + information aggregation at the cost of unbounded tail risk. The trilemma is structural, not an implementation defect — it arises from the absence of a shared probabilistic model.

### ParlayMarket architecture — three reusable primitives

**1. Ising-model belief state.** The joint distribution over M binary events is approximated as a pairwise exponential-family (Ising) model: P_φ(x) ∝ exp(Σ θ_i x_i + Σ W_ij x_i x_j). This is the maximum-entropy distribution consistent with observed first- and second-order moments — the weakest assumptions beyond moment constraints. State complexity: O(M²) instead of O(2^M). All 2^M − 1 prices (base + all parlay combinations) are derived as marginals of a single shared parameter vector φ, guaranteeing global probabilistic coherence.

**2. Shadow trades.** After each real trade, the AMM records internal "shadow trades" on correlated markets. These are bookkeeping entries, not real bets — they encode the information the AMM infers about other markets from the observed trade. They ensure no market's price becomes stale from low direct volume and are what make the signal-noise balance work: each real trade contributes one gradient update, but shadow trades spread that update's effect across all related markets.

**3. Composite-likelihood SGD.** Each trade reveals a discrepancy between posted price p^φ_m and true probability p*_m. The AMM minimizes composite pseudo-likelihood (sum of cross-entropy terms over all markets) via stochastic gradient: φ_{t+1} = φ_t − η ∇_φ CE(p*_m, p^φ_m). Because φ is shared, one trade updates all prices. The loss is strongly convex with μ = O(1) independent of M, giving geometric convergence.

### Key theoretical results

- **Geometric convergence**: E‖φ_t − φ*‖² ≤ (1−2ημ)^t ‖φ*‖² + ησ²/(2μ). ~22 rounds to reduce error 10×.
- **Polynomial loss scaling**: Aggregate loss = O(bρ²M²/η) transient + O(bη) steady-state. Per-market loss *halves* with each additional base asset (ℓ_M ≈ C·2^{−M}).
- **Parlay-accelerated learning**: Higher-order parlay trades add curvature in interaction directions, improving the contraction factor. A k-way parlay contributes O(1) directly vs. O(ρ²) from base-market cross-effects — O(ρ^{−2}) improvement at small correlations.

### The parlay reversal

A striking empirical result: with complete parlays, the Ising AMM is the best non-oracle model. Without parlays, the ranking completely reverses — the Ising AMM becomes the *worst*. Base-market-only gradient signals are under-determined for the full Ising parameter space. Parlays are not an efficiency accelerant; they are the *primary information channel* for learning the joint distribution. No other model tested achieves this reversal.

### Cemini application — Kalshi standalone market maker

Kalshi's current combo RFQ pricing exhibits **Fréchet upper-bound violations**: 39% of sampled two-leg quotes have P(A∩B) > min(P(A), P(B)), which is impossible under any joint distribution. Combo spreads are >2× wider than base-market spreads (11.89 vs. 5.12 cents).

The ParlayMarket can be deployed in **standalone market-maker mode**: layered on top of existing Kalshi RFQ without replacing the platform. It acts as a correlation-aware quoting engine for combos only, while base markets remain external LMSRs. On Kalshi's 2026-03-07 NBA slate (732 base markets, 5,918 combos), the standalone MM achieves:

| Metric | Kalshi native | Standalone Parlay MM |
|--------|--------------|---------------------|
| Win rate | 84.5% | 86.8% |
| Sharpe | 0.7151 | **1.0049** |

The ~40% risk-adjusted improvement comes from correlation-aware pricing — the model doesn't quote combos at independence-product prices when the underlying events are correlated.

### Practical considerations

- **Fee-bias correction**: Kalshi combo execution prices are ask quotes, upward-biased by platform markup. Training directly on them biases the joint model. The correction: preprocess into canonical all-YES representation using complement + inclusion–exclusion; for mixed YES/NO parlays the additive fee cancels.
- **Scope condition**: Contracts must be expressed in structurally coherent binary form. A preprocessing layer is needed to map raw market data into variables satisfying the AMM's assumptions before correlation-aware pricing becomes meaningful.
- **Cluster-based scaling**: For large event universes, train one Ising model per correlated cluster (e.g., per-game for sports) rather than one global model.

## Snippets

> "We introduce ParlayMarket, the first automated market-making design that supports parlay-style joint contracts within a unified liquidity pool while maintaining coherent pricing across base markets and their combinations." [Source: kalshi1 3:29.pdf p.1]

> "The pairwise exponential-family choice acts as the structural bridge between combinatorial expressiveness and quadratic capital requirements. It is also principled statistically: among all distributions matching the learned marginals and pairwise moments, it is the maximum-entropy distribution." [Source: kalshi1 3:29.pdf p.2]

> "The RFQ architecture faces a fundamental trilemma among three desiderata: liquidity consistency, information aggregation, and bounded loss. By adjusting collateral requirements, market-maker access, and quote policy, the platform may achieve at most two of these objectives at the expense of the third." [Source: kalshi1 3:29.pdf p.8]

> "Parlays are not merely an efficiency accelerant: they are the primary information channel through which the ParlayMarket learns the joint distribution. Without them, the Ising model is the worst non-oracle performer; with them, it is the best." [Source: kalshi1 3:29.pdf pp.17–18]
