---
title: "Stochastic-calculus foundations — Itô, Girsanov, martingales, Black-Scholes"
type: concept
tags: [concept, stochastic-calculus, derivative-pricing, ito-calculus, girsanov, martingale, brownian-motion, black-scholes, quant-finance, foundations, k55]
keywords: [ito-calculus, brownian-motion, martingale, risk-neutral-measure, radon-nikodym, cameron-martin-girsanov, change-of-measure, binomial-tree, black-scholes, self-financing-hedging, path-integral, heat-kernel, european-options]
related:
  - sources/phynance-kakushadze-1405-1948v2-stochastic-calculus-2014.md
  - concepts/quant-finance.md
  - concepts/time-series-arima-garch-framework.md
  - concepts/markov-regime-switching-models.md
  - entities/people/zura-kakushadze.md
  - concepts/partial-observation-stochastic-control.md
  - concepts/time-inconsistent-stochastic-control.md
  - sources/arxiv-particle-methods-partial-observation-2606.09055-2026-06-15.md
  - sources/arxiv-dpg-time-inconsistent-equilibrium-2606.11798-2026-06-16.md
maturity: validated
created: 2026-05-20
updated: 2026-06-16
clusters: [quant-finance, foundations, education]
---

## Relations

- @sources/phynance-kakushadze-1405-1948v2-stochastic-calculus-2014.md — primary reference (Kakushadze "Phynance" lecture notes, 111p)
- @concepts/quant-finance.md — corpus-index home
- @concepts/time-series-arima-garch-framework.md — empirical-modeling complement (Phynance gives the theoretical underpinnings, ARIMA/GARCH gives the practical implementation)
- @concepts/markov-regime-switching-models.md — Markov property is invoked in the binomial-tree and risk-neutral-measure chapters
- @concepts/partial-observation-stochastic-control.md — K117: filtering distribution as infinite-dimensional control state; particle finite-dimensional surrogate
- @concepts/time-inconsistent-stochastic-control.md — K118: equilibrium via extended HJB + DPG two-stage reformulation
- @sources/arxiv-dpg-time-inconsistent-equilibrium-2606.11798-2026-06-16.md — K118 source

## Raw Concept

What this page is for: a synthesized in-wiki reference for stochastic-calculus results that other wiki pages cite without a primary-source pointer (Itô's lemma, Cameron-Martin-Girsanov, martingale representation theorem, Black-Scholes derivation). The Kakushadze "Phynance" lecture notes (`@sources/phynance-kakushadze-1405-1948v2-stochastic-calculus-2014.md`) are the canonical reference; this page is the topic-organized index into them, plus the operational summary of what each result is used for in trading-system contexts.

## Narrative

This is a **reference** page, not a strategy page. It documents the mathematical machinery underneath options pricing, risk-neutral valuation, and continuous-time hedging — the same machinery that underlies any structured-product, options-trading, or volatility-strategy work that may live in or connect to the Cemini stack.

### The hierarchy of objects

```
discrete time, binary outcomes:    binomial tree
                                         ↓ (let Δt → 0)
continuous time, Gaussian noise:    Brownian motion (Wiener process)
                                         ↓ (build calculus on top)
Itô calculus:                       dX = μ dt + σ dW   (Itô SDE)
                                         ↓ (apply f(X) ↦ Itô's lemma)
                                    df = (∂f/∂t + μ ∂f/∂x + ½σ² ∂²f/∂x²) dt + σ ∂f/∂x dW
                                         ↓ (change of probability measure)
Girsanov / Radon-Nikodym:           change drift, keep volatility — produces risk-neutral measure
                                         ↓
Self-financing hedging:             portfolio replicates derivative payoff
                                         ↓
Black-Scholes:                      no-arbitrage price as expected payoff under risk-neutral measure
```

### Binomial tree (the discrete-time scaffold)

The simplest viable derivative-pricing model. At each step, asset price goes up by factor `u` with risk-neutral probability `q*` or down by factor `d` with probability `1 − q*`. Risk-neutral probability:

```
q* = (e^(rΔt) − d) / (u − d)
```

The price of any derivative is the expected payoff under `q*`, discounted at the risk-free rate `r`. **Note**: `q*` is *not* the real-world probability of an up-move; it's the probability that makes the *discounted* asset price a martingale.

Worked example in Kakushadze: pricing a bet on the **Baseball World Series**. Useful — same mechanics apply to Polymarket Bo-7 series markets (NBA Finals, Stanley Cup, MLB World Series). The binomial tree is the right pricing model for those markets; the Polymarket-displayed odds can be checked against the tree's risk-neutral probability.

### Martingales (the core abstraction)

A martingale is a stochastic process whose conditional expectation, given history up to time `t`, equals its current value:
```
E[X_{t+1} | X_1, ..., X_t] = X_t
```

**Tower Law**: `E[E[X | F_t] | F_s] = E[X | F_s]` for `s ≤ t`. Conditioning on a finer information set then a coarser one is the same as conditioning on the coarser one directly.

**Martingale measure** (risk-neutral measure `Q`): the measure under which the *discounted* asset price is a martingale. The price of any derivative under `Q` is its expected discounted payoff.

**Binomial Representation Theorem**: in a binomial tree, every martingale can be written as a discrete stochastic integral against the underlying — gives the explicit *replicating portfolio* (which is what you trade to hedge).

**Self-financing hedging**: a portfolio whose value changes only because of price movements, never from external cash inflows/outflows. The self-financing condition is the equation that ties the replication strategy to the derivative's payoff.

→ Used in Cemini context for understanding when a hedge actually self-finances vs requires ongoing cash injection. See `@concepts/perps-dex-funding-carry-strategy.md`: a cross-venue funding carry that requires periodic rebalancing is **not** self-financing; treat as a strategy with ongoing cost, not a free hedge.

### Itô calculus (continuous time)

**Brownian motion** `W_t` is a continuous-time Gaussian process with `E[W_t] = 0`, `Var(W_t) = t`, independent increments. The continuous-time analogue of the discrete-time random walk.

**Itô's stochastic differential equation**:
```
dX_t = μ(X_t, t) dt + σ(X_t, t) dW_t
```
where `μ` is the drift and `σ` is the diffusion (volatility).

**Itô's Lemma** (the chain rule of stochastic calculus). For `f = f(X_t, t)`:
```
df = (∂f/∂t + μ ∂f/∂x + ½σ² ∂²f/∂x²) dt + σ ∂f/∂x dW
```
The `½σ² ∂²f/∂x²` term is the "extra" piece compared to ordinary calculus — it's where the volatility-of-volatility effects come in. Foundational for option-pricing PDEs.

### Radon-Nikodym + Cameron-Martin-Girsanov (the change-of-measure machinery)

**Radon-Nikodym derivative** `dQ/dP`: a function that converts between probability measures `P` (real-world) and `Q` (risk-neutral). For any random variable `X`, `E_Q[X] = E_P[X · dQ/dP]`.

**Cameron-Martin-Girsanov Theorem**: gives the explicit form of the Radon-Nikodym derivative for changing the drift of a Brownian motion. Under measure `Q`, the process `dX̃_t = (μ − γσ) dt + σ dW̃_t` has a new drift, but **the volatility is unchanged**. Asset volatility is the same under `P` and `Q`; only the drift changes.

This is **why options can be priced uniquely**: the risk-neutral drift is forced (it must equal the risk-free rate for the discounted price to be a martingale), so the only free parameter that matters for pricing is volatility. All the empirical/historical effort goes into estimating σ.

**Path-integral formulation** (the "Phynance" angle): the Radon-Nikodym derivative can be written as a Boltzmann-like exponential of the path action. Useful for path-dependent payoffs (Asian, lookback, barrier options) — the option price becomes a path integral with the payoff as the observable.

### Black-Scholes (the canonical result)

Combining everything above: under the risk-neutral measure `Q`, the European call option price is:
```
C(S_t, t) = E_Q[e^{-r(T-t)} max(S_T − K, 0) | F_t]
```
Closed-form via the lognormal distribution of `S_T`:
```
C = S_t · N(d₁) − K · e^{-r(T-t)} · N(d₂)
d₁ = [ln(S_t/K) + (r + σ²/2)(T-t)] / (σ √(T-t))
d₂ = d₁ − σ √(T-t)
```
`N(·)` is the standard normal CDF. Implied volatility σ_IV is the σ that makes this equal the observed market price. The volatility-surface (σ_IV across strike + expiry) is a primary trading observable for options strategies.

### Binary / digital options

European binary call: payoff `1` if `S_T > K`, else `0`. Closed-form under Black-Scholes:
```
C_binary = e^{-r(T-t)} · N(d₂)
```
**Why this matters for Polymarket**: Polymarket contracts are conceptually European binary options. The Kakushadze formula gives a continuous-time fair price for a Polymarket binary if the underlying has lognormal dynamics — useful as a pricing baseline against which the actual Polymarket market price can be compared.

For prediction-market contexts the underlying is often not a price (e.g. election outcomes don't have continuous dynamics), so Black-Scholes binaries don't directly apply. But for any Polymarket market on a tradeable financial asset (BTC > X, S&P 500 > Y), the binary-option pricing formula is the canonical theoretical reference.

### Exotic options (covered in later chapters, not transcribed here)

- **American options**: early-exercise feature; pricing via the *optimal stopping problem*; closed-form not generally available; numerical methods required (PDE, lattice, Monte Carlo).
- **Asian options**: payoff depends on average price over the path; path-integral formulation natural.
- **Lookback options**: payoff on max or min over the path.
- **Barrier options**: payoff modified by whether the price hit a barrier.

All have closed-form or semi-closed-form solutions under Black-Scholes assumptions. → Phynance Chapter 11+ has the derivations.

### Practical relevance to Cemini

This material isn't currently load-bearing on any Cemini strategy. Recorded as **reference + readiness**:

1. **Resolves `[NEEDS VERIFICATION]` tags** that cite Itô's lemma or Girsanov on other wiki pages — those can now point here.
2. **Baseline for Polymarket binary pricing**: any future Polymarket-tradeable-asset market (BTC > X by date Y) can be pre-priced against a Black-Scholes binary as a sanity check.
3. **Foundation for any options/structured-product workstream** — if Cemini extends into Deribit, dYdX options, or any other options venue, the wiki should not be starting from zero.
4. **Hiring/intellectual orientation marker**: matches the Simons interview (also K55) — the kind of material expected of a quant hire.

## Dead Ends

- **Trying to apply Black-Scholes binary pricing directly to election / sports / weather Polymarket markets**: the underlying does not have lognormal dynamics. Election outcomes are discrete events with no continuous trading process; Black-Scholes assumptions don't hold. Use the binomial-tree-style approach with explicit risk-neutral probabilities derived from the event structure instead.

## Snippets

> "[Phynance] primarily focused on an introduction to stochastic calculus and derivative pricing with various stochastic computations recast in the language of path integral, which is used in theoretical physics, hence 'Phynance'." [Source: 1405.1948v2.pdf p.1, Kakushadze]

> Table of Contents: Binomial Tree Model (Risk-neutral Measure; Baseball World Series) · Martingales (Tower Law; Martingale Measure; Binomial Representation; Self-financing Hedging) · Stochastic Calculus (Itô; Radon-Nikodym; Path Integral; Cameron-Martin-Girsanov) · Continuous Hedging (Heat Kernel Method) · European Options (Call, Put, Binary). [Source: 1405.1948v2.pdf pp.2-3]
