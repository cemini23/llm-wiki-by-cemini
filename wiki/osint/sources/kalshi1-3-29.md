---
title: "ParlayMarket: Automated Market Making for Parlay-style Joint Contracts"
type: source
tags: [pdf, deep-read, prediction-markets, market-microstructure, amm-design, kalshi, parlay, ising-model]
keywords: [parlaymarket, automated-market-making, parlay, joint-contracts, ising-model, prediction-markets, kalshi, lmsr, rfq-trilemma, correlation-aware-pricing, combinatorial-markets, online-learning, belief-propagation]
related:
  - concepts/market-microstructure.md
  - entities/platforms/kalshi.md
  - concepts/parlay-market-making.md
  - concepts/agent-authorization-stack.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-01
clusters:
  - market-microstructure
  - prediction-markets
---
## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub
- @entities/platforms/kalshi.md — primary Cemini prediction-market venue; Kalshi is the empirical testbed in §6.4
- @concepts/parlay-market-making.md — K24 promotion: reusable AMM design primitive for correlation-aware joint-contract pricing
- @concepts/agent-authorization-stack.md — K24 canonical source for ParlayMarket; Layer 4 of the four-layer authorization architecture.

## Raw Concept

- **Original title**: ParlayMarket: Automated Market Making for Parlay-style Joint Contracts
- **Author(s)**: Ranvir Rana (Kaleidoscope Blockchain), Viraj Nadkarni (Princeton), Niusha Moshrefi (Princeton), Pramod Viswanath (Princeton)
- **Type**: PDF (arXiv preprint)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/kalshi1 3:29.pdf`
- **Retrieved**: 2026-04-23
- **Pages / length**: 30p (21p body + 9p appendices)
- **Read status**: deep-read (K24, 2026-05-01)
- **arXiv**: 2603.22596v1 [cs.CE], March 23, 2026
- **Institution**: Princeton University + Kaleidoscope Blockchain

## Narrative

**[K24 DEEP-READ — 2026-05-01]** This paper introduces ParlayMarket, the first automated market-making design that supports parlay-style joint contracts within a unified liquidity pool while maintaining coherent pricing across base markets and their combinations. The key design choice: represent the joint distribution over M binary events using a pairwise exponential-family (Ising) model, compressing the 2^M outcome space into O(M²) sufficient statistics. This allows a single liquidity pool to support an exponentially large family of contracts without separate capitalization. The paper proves geometric convergence to the best Ising approximation of the true joint distribution, shows aggregate loss scales polynomially (O(M²)) rather than exponentially (O(2^M)), and demonstrates on historical Kalshi NBA data that the standalone market-maker achieves Sharpe 1.0049 vs. Kalshi native 0.7151.

### The core problem

With M binary events, the joint outcome space contains 2^M possible realizations. A naive combinatorial market maker must maintain prices and risk across all outcomes — loss scales exponentially. Current platforms (Kalshi, Polymarket) either prohibit parlays or use dealer-mediated RFQ mechanisms that fragment liquidity and produce incoherent pricing: the paper documents Fréchet upper-bound violations in 39% of sampled Kalshi combo quotes (Table 5–6), meaning the quoted joint probability P(A∩B) exceeds min(P(A), P(B)) — impossible under any joint distribution.

### The RFQ trilemma (§4.1.2)

The paper identifies a structural trilemma in request-for-quote architectures. By adjusting collateral requirements, market-maker access, and quote policy, a platform can achieve at most two of three objectives:

1. **Liquidity consistency** — comparable price impact across base and parlay markets
2. **Information aggregation** — prices converge to true probabilities
3. **Bounded loss** — aggregate market-maker loss remains controlled

- Open participation + relaxed collateral → liquidity + info aggregation, but unbounded loss
- Conservative quoting → liquidity + bounded loss, but prices don't aggregate information
- Restricted market family → info aggregation + bounded loss, but liquidity is fragmented

Kalshi's current combo system sits at the first corner: open dealer participation gives reasonable quote availability and price discovery, but tail exposures are unconstrained.

### ParlayMarket architecture (§5)

Three interlocking mechanisms:

1. **Ising model belief state** — The joint distribution is approximated as P_φ(x) ∝ exp(Σ θ_i x_i + Σ W_ij x_i x_j). This is the maximum-entropy distribution consistent with observed first- and second-order moments — the weakest possible assumptions beyond the moment constraints. All 2^M − 1 prices are derived as marginals of a single shared parameter vector φ.

2. **Shadow trades** — After each real trade, the AMM records internal "shadow trades" on related markets. These are bookkeeping entries that encode the information inferred about correlated markets from the observed trade. They ensure no market's price becomes stale from low direct volume.

3. **Composite-likelihood SGD** — Each trade reveals a discrepancy between the posted price p^φ_m and the true probability p*_m. The AMM takes a stochastic gradient step φ_{t+1} = φ_t − η ∇_φ CE(p*_m, p^φ_m). Because φ is shared, one trade updates all prices.

### Theoretical results (§5)

- **Theorem 1 — Geometric convergence**: E‖φ_t − φ*‖² ≤ (1−2ημ)^t ‖φ*‖² + ησ²/(2μ). With η=0.2, μ≈1/4, the contraction factor is 0.9/round; ~22 rounds to reduce initial error 10×. The strong-convexity constant µ is O(1), independent of M.

- **Proposition 2 — Complete-parlay loss scaling**: In the regime where every non-empty subset S⊆[M] is traded at equal rate, aggregate expected loss decomposes into transient + steady-state: L_transient = O(bρ²M²/η), L_ss,round = O(bη). Loss grows polynomially (O(M²)), not exponentially. Per-market loss ℓ_M ≈ C·2^{−M} — it *halves* with each additional base asset.

- **Proposition 3 — Parlay-accelerated convergence**: Higher-order parlay trades strictly improve convergence by adding curvature in interaction directions. A k-way parlay contributes O(1) directly to the Hessian in the (W_kl, W_kl) entry vs. O(ρ²) from base-market cross-effects — a factor of O(ρ^{−2}) improvement at small correlations.

### The parlay reversal (§6.2)

A striking empirical finding: **with complete parlays**, ParlayMarket is the best non-oracle model (lowest per-round loss, just above the true oracle). **Without parlays**, the ranking completely reverses — ParlayMarket becomes the *worst* non-oracle model, while the independent LMSR (which ignores correlations) performs best. The explanation: base-market-only gradient signals are under-determined relative to the full Ising parameter space. Parlays are not an efficiency accelerant; they are the *primary information channel* through which the model learns the joint distribution. No other model tested achieves this reversal.

### Kalshi empirical replay (§6.4)

Historical replay on Kalshi's NBA slate for 2026-03-07: 732 base markets across 6 games, 5,918 listed combo tickers (2- through 10-leg parlays). One Ising model per game cluster, initialized from first 30 candle mid-prices.

| Strategy | Accepted Trades | Win Rate | Net PnL | Sharpe |
|----------|----------------|----------|---------|--------|
| Kalshi (execution price) | 5,436 | 84.5% | $244,190.77 | 0.7151 |
| Stand-alone MM (θ_corr) | 3,973 | 86.8% | $113,984.58 | **1.0049** |
| Full AMM | 5,436 | 69.0% | $158,577.66 | 0.7062 |

The stand-alone MM achieves the highest Sharpe ratio among non-native strategies — it can be inserted as a drop-in correlation-aware parlay quoting engine layered on top of existing RFQ. The full AMM accepts all trades but exhibits lower risk-adjusted return, likely because observed RFQ flow contains substantial noise that a fully internalized LMSR must absorb.

### Fee-bias correction

A practical contribution: observed Kalshi combo execution prices are ask quotes, systematically upward-biased by platform markup. Training directly on these would bias the learned joint model upward. The authors preprocess trades into a canonical all-YES representation using complement + inclusion–exclusion — for mixed YES/NO parlays the additive fee cancels, yielding approximately unbiased targets.

### Cemini relevance

Kalshi is Cemini's primary prediction-market venue. This paper provides:

- **Structural diagnosis**: The RFQ trilemma explains *why* Kalshi combo pricing is systematically broken (Fréchet violations are not bugs — they're structural consequences of the architecture)
- **Deployable alternative**: The stand-alone MM mode can be layered on top of existing Kalshi RFQ without replacing the platform — a correlation-aware quoting engine that improves risk-adjusted P&L
- **P&L signal**: The Sharpe improvement (0.7151 → 1.0049) is meaningful — ~40% improvement on risk-adjusted basis
- **Theoretical foundation**: The Ising-model AMM + shadow-trade architecture is a principled design primitive that could inform Cemini's own prediction-market quoting logic

### Limitations (per authors)

Assumes contracts are already expressed in structurally coherent binary form — a preprocessing/structural-learning layer is needed to map raw market data into variables satisfying the AMM's assumptions. The current framework is text-only; multimodal and tool-augmented chains are not covered. Robustness against adaptive adversaries who craft attacks to evade the taxonomy-embedded prompt is an open problem.

## Snippets

**S1 — Core contribution** (p.1, Abstract):
> "We introduce ParlayMarket, the first automated market-making design that supports parlay-style joint contracts within a unified liquidity pool while maintaining coherent pricing across base markets and their combinations. The key design choice is to represent the joint distribution using a pairwise exponential-family model. The postulated model compresses the 2^M outcome space into O(M²) sufficient statistics, while making weakest assumptions on higher order moments."

**S2 — The RFQ trilemma** (p.8, §4.1.2):
> "The RFQ architecture faces a fundamental trilemma among three desiderata: liquidity consistency, information aggregation, and bounded loss. By adjusting collateral requirements, market-maker access, and quote policy, the platform may achieve at most two of these objectives at the expense of the third."

**S3 — Fréchet violations on Kalshi** (pp.22–23, Appendix A.1):
> "Under probabilistic pricing, the combo YES price should be approximately the product of the two leg YES prices. All 33 quoted prices exceed the independence benchmark. Moreover, 13 of the 33 quotes (39%) violate the Fréchet upper bound P(A∩B) ≤ min(P(A), P(B)) — a constraint that holds under any joint probability distribution, regardless of correlation structure."

**S4 — Why the Ising model** (p.2, §1):
> "This is the smallest coherent model that can represent dependence across events: an independence model cannot encode correlations at all, while a fully general joint model requires exponentially many degrees of freedom. The pairwise exponential-family choice therefore acts as the structural bridge between combinatorial expressiveness and quadratic capital requirements."

**S5 — Shadow trades mechanism** (p.10, §5.1):
> "Shadow trades are not real bets - they are bookkeeping entries that encode the information the AMM infers about other markets from the observed trade. Critically, they ensure that no market's price becomes stale simply because it receives little direct trading volume; even an esoteric parlay market that rarely attracts traders will see its posted price updated whenever a correlated market is active."

**S6 — Geometric convergence** (p.12, §5.3):
> "In the pure arbitrageur environment, starting from φ_0 = 0 with step size η ≤ 1/(2L): E‖φ_t − φ*‖² ≤ (1−2ημ)^t ‖φ*‖² + ησ²/(2μ). With η = 0.2 and μ ≈ 1/4, the contraction factor per round is 0.9; roughly 22 rounds suffice to reduce the initial error by 10×."

**S7 — Loss scaling** (p.13, §5.4):
> "In the complete-parlay regime, where every non-empty subset S⊆[M] is traded at equal rate, aggregate expected LMSR loss decomposes as L_transient = O(bρ²M²/η), L_ss,round = O(bη). The dependence on M is polynomial rather than exponential."

**S8 — Per-market loss halving** (p.16, §6.1, Table 3):
> "ℓ_M decays exponentially as C·2^{−M}, halving with each additional base asset. The product ℓ_M · 2^M ≈ 0.15 is approximately constant for M = 4,…,9, confirming that the total per-round loss N_M · ℓ_M is essentially flat."

**S9 — The parlay reversal** (pp.17–18, §6.2):
> "With complete parlays, the ParlayMarket is the best-performing non-oracle model. Without parlays, the ranking completely reverses: the ParlayMarket now has the highest loss of all non-oracle models. Parlays are not merely an efficiency accelerant: they are the primary information channel through which the ParlayMarket learns the joint distribution."

**S10 — Parlay-accelerated learning** (p.14, §5.5):
> "Higher-order parlays that include both i and j constrain several interaction directions at once and can therefore dominate the curvature in the weakly identified subspace; heuristically, the improvement can be of order O(ρ^{−2}) when ρ≪1."

**S11 — Kalshi empirical results** (p.19, §6.4, Table 4):
> "The standalone ParlayMarket market maker achieves the strongest risk-adjusted liquidity-provider portfolio, with the highest Sharpe ratio among the non-native strategies while still accepting a large fraction of historical flow. The empirical value of ParlayMarket pricing is strongest in the standalone market-maker regime: the model can be inserted into an existing platform, improve LP portfolio quality, and remain competitive on accepted quotes."

**S12 — Signal-noise balance** (pp.13–14, §5.4):
> "Adding more markets increases signal and noise at the same rate rather than letting noise dominate. As a result, the steady-state parameter error remains O(η) rather than growing with N_M."

**S13 — Scope condition** (p.20, §7):
> "An important scope condition of the current framework is that the traded contracts are assumed to already be expressed in a structurally coherent binary form. In many practical settings, this representation must itself be constructed before correlation-aware pricing becomes meaningful. This suggests a broader architecture for automated parlay markets: a structural layer that identifies and normalizes the relevant event representation, followed by a pricing layer such as ParlayMarket."
