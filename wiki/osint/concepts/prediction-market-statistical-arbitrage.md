---
title: Cross-Market Statistical Arbitrage on Prediction Markets
type: concept
tags: [concept, quant-finance, statistical-arbitrage, prediction-markets, polymarket, kalshi, cointegration, microstructure, k52]
keywords: [statistical-arbitrage, cointegration, augmented-dickey-fuller, johansen-test, ornstein-uhlenbeck, mean-reversion, maximum-likelihood-estimation, order-book-imbalance, micro-price, optimal-stopping, l2-order-book, markov-transition-matrix]
related:
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/non-latency-arbitrage-strategies.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/markov-regime-switching-models.md
  - concepts/market-microstructure.md
  - entities/tools/prediction-market-analysis.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — Post 4 (@ridark_eth), the source roadmap this page synthesizes
- @concepts/cross-venue-arbitrage-pattern.md — the *execution-loop* reference (poll → detect → execute → reconcile); this page is the *signal-generation* math layer that decides when to fire it
- @concepts/non-latency-arbitrage-strategies.md — the model-free cousin: standing logical arb. Stat-arb here is *not* riskless — it is a probabilistic mean-reversion bet
- @concepts/polymarket-updown-bot-taxonomy.md — Types 3 (fair-value/repricing) and 5 (imbalance) are the bot-strategy expression of this page's micro-price / OBI math
- @concepts/markov-regime-switching-models.md — the cross-venue predictive signal (Method 2 Phase 3) uses a rolling Markov transition matrix
- @concepts/market-microstructure.md — order-book mechanics (depth, spread, micro-price) backdrop
- @entities/tools/prediction-market-analysis.md — the repo Post 4 advertised; verified 2026-05-18 as real + MIT, but a trades/markets dataset, **not** the L2 order-book dataset the post claimed

## Raw Concept

What prompted this page: K52 ingest of @ridark_eth's "Cross-Market Statistical Arbitrage" roadmap. The post lays out the *quantitative* layer that @concepts/cross-venue-arbitrage-pattern.md deliberately left abstract — how a desk decides the spread between the same event on two venues is *tradeable*, and how it generates a millisecond-horizon directional signal from order-book structure. This page captures the two methodologies; the execution loop stays on the cross-venue page.

**Important framing.** @concepts/non-latency-arbitrage-strategies.md and the pure cross-venue loop describe edges that are *logically riskless* (a YES+NO that must sum to \$1). Statistical arbitrage is **not** riskless — it is a probabilistic bet that a historically mean-reverting spread will revert again. The "arb" label is the industry's; the risk is real (the relationship can break).

## Narrative

### The setup

When the *same* real-world outcome is listed on both Polymarket and Kalshi, both contracts must converge to the identical terminal value (\$1.00 or \$0.00) at resolution. Local liquidity shocks — a whale dumping size on one venue — push the two prices temporarily apart. Stat-arb trades that temporary divergence and delta-hedges venue inventory toward zero, so the position is agnostic to *who actually wins the event*.

The post claims a public repo + L2 order-book dataset as the backtest sandbox — see the verification caveat below.

### Method 1 — Cointegration + Ornstein-Uhlenbeck mean reversion

The slower, position-level methodology.

**Phase 1 — test for cointegration.** With `P_P,t` the Polymarket mid-price and `P_K,t` the Kalshi mid-price, construct the spread

```
S_t = P_P,t − β·P_K,t − μ
```

where β is the cointegration coefficient and μ a constant. Run the **Augmented Dickey-Fuller (ADF)** test or the **Johansen** test on historical data to confirm `S_t` is stationary, I(0) — i.e. it reliably reverts to its mean rather than wandering.

**Phase 2 — model the spread as an OU process.** Once cointegration holds, model the continuous-time spread as an Ornstein-Uhlenbeck process:

```
dS_t = θ(μ − S_t) dt + σ dW_t
```

- θ — rate of mean reversion (how fast the gap closes)
- μ — long-term mean of the spread
- σ — volatility of the spread
- dW_t — Brownian increment (noise)

**Phase 3 — calibrate by MLE.** Apply Euler–Maruyama discretization over interval Δt to turn the SDE into a discrete AR(1)-form regression:

```
S_{t_i} = S_{t_{i-1}}·e^(−θΔt) + μ·(1 − e^(−θΔt)) + ε_t
```

Maximum-Likelihood Estimation on the historical series extracts θ (hence μ, σ). The **tradeability gate**: the mean-reversion half-life `τ = 1/θ` must be *faster than execution latency* — if the spread closes faster than you can act, the edge is unreachable.

**Phase 4 — optimal entry/exit thresholds.** An amateur enters the moment any gap appears; a desk solves an **optimal-stopping problem**. Using the calibrated OU parameters, derive entry threshold `x_open` and exit `x_close` to maximize expected return *per unit time*, net of cost `c` (transaction fees + slippage across both venues). Conceptually: short the spread near `+x_open`, go long near `−x_open`, unwind toward μ.

```
        S_t
         ^   ······ short entry (+x_open)
         |  /\
  ───────┼─/──\────────── long-term mean (μ)
         |/    \    /
         |      \__/  ···· long entry (−x_open)
         +──────────────────────> t
```

### Method 2 — Order-Book Imbalance + micro-price

The faster, millisecond-horizon methodology — at HFT horizons the Method-1 cointegration model is too slow.

**Phase 1 — imbalance.** The plain mid-price ignores the *volume* at the inside market. Level-1 Order-Book Imbalance:

```
I_t = (V_b − V_a) / (V_b + V_a),   I_t ∈ [−1, 1]
```

with `V_b` the volume at the best bid, `V_a` at the best ask. If the best bid holds 100k contracts and the ask only 1k, price is structurally pressured upward.

**Phase 2 — micro-price.** The volume-weighted "true" instantaneous value, weighting each side's price by the *opposite* side's volume:

```
P_micro = (V_b·P_a + V_a·P_b) / (V_b + V_a)
```

Substituting the imbalance definition gives the clean linear form:

```
P_micro = P_mid + I_t·(spread/2)
```

— the micro-price is the mid-price nudged toward the heavier side of the book.

**Phase 3 — cross-venue predictive signaling.** Because Polymarket (on-chain / hybrid) and Kalshi (centralized clearinghouse) process order flow at different velocities, an imbalance on the faster venue *leads* the slower one:

```
ΔP_Kalshi(t+δ) = f( I_Polymarket(t), P_micro,Poly(t) − P_micro,Kalshi(t) )
```

Compute a rolling **Markov transition matrix** over historical L2 data: measure the probability that a large imbalance shift (`I > 0.8`) on venue A predicts the ask book clearing on venue B within δ ≈ 200ms. If that probability exceeds a threshold, the execution system crosses the spread on the lagging venue before retail order routers register the move. (The Markov-matrix mechanics are the same family as @concepts/markov-regime-switching-models.md.)

### Process over prediction

The post's core takeaway: institutional desks are *agnostic to the actual event* — no polling data, no macro opinion. The edge is operational/structural: (1) calibrate positions via empirical OU parameters rather than nominal spreads; (2) exploit the micro-price↔imbalance relationship across venues; (3) act on cross-platform signals before the UI refreshes.

### Cemini posture

- **This is the signal layer; the loop is the cross-venue page.** Method 1 outputs *when a spread is worth trading and at what threshold*; @concepts/cross-venue-arbitrage-pattern.md is the poll→execute→reconcile machinery that acts on it.
- **Method 1 is the realistic Cemini target.** ADF/Johansen/OU calibration runs offline on `cemini-prod`; the resulting thresholds drive a relaxed-cadence scanner — no co-location. statsmodels covers ADF/Johansen; OU-MLE is a short fit.
- **Method 2 is aspirational.** A 200ms cross-venue predictive edge needs co-located low-latency infra Cemini does not have; record it as a reference, do not scope it.
- **Not riskless — size with discipline.** Cointegration can break (the relationship was historical, not guaranteed). Treat stat-arb as a probabilistic strategy under @concepts/kelly-sizing-quarter.md sizing, not as the locked-payoff arb of @concepts/non-latency-arbitrage-strategies.md.
- **Repo/dataset — verified 2026-05-18.** The advertised repo `github.com/Jon-Becker/prediction-market-analysis` **is real**: MIT-licensed, ~3,378★, actively maintained — see @entities/tools/prediction-market-analysis.md. But Post 4 **misrepresents what it contains.** The real dataset is **trades + market metadata** (36 GiB compressed), *not* the "L2 order-book snapshots, 20 levels deep, 100ms, 850M state updates" the post described — there is no order-book depth data in it, and every setup command in the post is wrong (`cd prediction-market-arbitrage` 404s; `make download-ob` / `orderbooks_l2.tar.zst` / `data/snapshots/` do not exist). **Consequence for this page: Method 1 is backtestable** from the real dataset (cointegration / OU calibration on trade or mid prices, plus the repo's own cross-venue `comparison/` analyses). **Method 2 is not** — order-book imbalance and micro-price need L2 data this dataset does not have. To do Method-2 work, Cemini must record its own L2 snapshots (see the @0x_Punisher 6-layer websocket playbook in @concepts/polymarket-bot-architecture.md). The OBI/micro-price *math* in Method 2 remains textbook-correct; only the post's claimed *data source* for it is fictional.

## Snippets

> "When two distinct platforms host markets on the exact same real-world outcome, their long-term prices must converge to identical terminal values (\$1.00 or \$0.00). However, local liquidity shocks ... cause temporary divergence." [Source: posts-2026-05-18.docx — Post 4, @ridark_eth]

> "If θ implies a mean-reversion time τ = 1/θ faster than the platform's execution latency, the asset is deemed highly tradeable." [Source: posts-2026-05-18.docx — Post 4, @ridark_eth]

> "They measure the probability that a significant imbalance shift (I > 0.8) on Platform A predicts a clearing of the ask book on Platform B within a δ = 200ms window." [Source: posts-2026-05-18.docx — Post 4, @ridark_eth]

## Dead Ends

- **Method 2 (OBI / micro-price) cannot be backtested from the @ridark_eth-advertised dataset.** Post 4 claimed `Jon-Becker/prediction-market-analysis` ships L2 order-book snapshots; verification (2026-05-18) showed it ships *trades + market metadata* only. Do not re-attempt to source Method-2 L2 data from that repo — it is not there. Method-2 work requires Cemini recording its own L2 snapshots. Recorded so the dead end is not re-walked.
