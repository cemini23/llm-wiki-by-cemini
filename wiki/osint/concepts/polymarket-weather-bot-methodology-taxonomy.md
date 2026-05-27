---
title: "Polymarket weather-bot methodology taxonomy (five types)"
type: concept
tags: [concept, polymarket, weather-trading, bot-taxonomy, parity, prediction-markets, k70]
keywords: [forecast-driven weather bot, latency arbitrage kalshi, base-rate statistical divergence, copy-trading smart money weather, ai-agent weather bot, parity terminal bot survey]
related:
  - sources/alterego-eth-five-weather-methodologies-2026-05-27.md
  - entities/people/alteregoeth.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/tools/parity-polymarket-analytics.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/nwp-bias-correction-ml-weather-trading.md
  - concepts/nwp-model-stack-polymarket-weather.md
  - concepts/polymarket-bot-architecture.md
  - entities/tools/hermes-agent.md
  - entities/tools/clawdbot.md
  - sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md
maturity: validated
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @sources/alterego-eth-five-weather-methodologies-2026-05-27.md — K70 primary source
- @entities/people/alteregoeth.md — taxonomy author
- @concepts/polymarket-weather-trading-strategy.md — operational weather edge (Gamma, stations, ensembles)
- @entities/tools/parity-polymarket-analytics.md — claimed survey instrument (>30 bots)
- @concepts/polymarket-copy-trading-strategy.md — type 4
- @concepts/nwp-bias-correction-ml-weather-trading.md — ML refinement within type 1
- @concepts/nwp-model-stack-polymarket-weather.md — regional stack within type 1
- @concepts/polymarket-bot-architecture.md — engineering playbook (latency, WS) for types 1–2
- @entities/tools/hermes-agent.md — type 5 runtime example
- @entities/tools/clawdbot.md — type 5 runtime example (ColdMath lineage)
- @sources/alterego-eth-xgboost-nwp-polymarket-models-2026-05-25.md — deep-dive on type-1 ML variant

## Raw Concept

Synthesized from @AlterEgo_eth K70 (2026-05-27): a **strategy-layer** taxonomy for Polymarket **weather** bots, distinct from @concepts/polymarket-updown-bot-taxonomy.md (short-horizon up/down markets) and @concepts/polymarket-bot-architecture.md (implementation layers).

## Narrative

### Type 1 — Forecast-driven / model-based

- **Mechanism:** Independent NWP models (GFS ensemble, ECMWF, HRRR, etc.) converge → confidence → positive EV with filters.
- **Tradeoffs:** Medium complexity; high profit with filters; **high and growing competition**; medium–high stability when consensus is strong.
- **Risks:** Correlated model failure, settlement noise, fees.
- **Cemini:** Default path — @concepts/polymarket-weather-trading-strategy.md, K66 bias-correction stack. ColdMath-style micro-scaling is an execution overlay on type 1 [TENTATIVE].

### Type 2 — Arbitrage / latency

- **Mechanism:** Seconds–minutes: new model runs, Polymarket↔Kalshi price divergence, pure latency.
- **Tradeoffs:** High complexity; very high early profit with **closing windows**; very high competition; low–medium stability.
- **Risks:** Downtime, slippage, execution errors, regulatory exposure [NEEDS VERIFICATION 2026-05-27].
- **Cemini:** Overlaps K67 FOK/copy-latency brief + @concepts/polymarket-bot-architecture.md; often **combined** with type 1 per author.

### Type 3 — Base-rate / statistical divergence

- **Mechanism:** Long-horizon city/season base rates + adjustment for current conditions; fade narrative overreaction.
- **Tradeoffs:** Medium–high complexity (data science); stable long-run profit; **medium competition**; high stability.
- **Risks:** Fat tails, data volume, fewer signals.
- **Cemini:** **Under-documented** in wiki prior to K70 — candidate for dedicated ingest (historical settlement + seasonality datasets).

### Type 4 — Copy-trading / smart-money

- **Mechanism:** Monitor top on-chain wallets (often ex-meteorologists); require **multi-wallet convergence** before mirroring.
- **Tradeoffs:** Low–medium complexity; good profit with selection; rapidly growing competition; medium stability.
- **Risks:** Lag, slippage, wash trading, style drift.
- **Cemini:** @concepts/polymarket-copy-trading-strategy.md, K57 Gustafsson/Polydao threads, @concepts/polymarket-wallet-alpha-pipeline.md.

### Type 5 — Self-learning / AI-agent

- **Mechanism:** Autonomous agents (Claude, Hermes, GPT) compute EV + Kelly, backtest, calibrate, combine strategies.
- **Tradeoffs:** High complexity; potentially highest adaptability; medium–high competition; stability **medium but improving** [TENTATIVE].
- **Risks:** Black box, overfitting, API cost, hallucinations.
- **Cemini:** Treat as **research/experimental** until reproducible eval — aligns with Hermes/Clawdbot entities but not Adopt without license + ops gates.

### Comparison axes (author framing)

Compared across: **probability calibration**, **adaptability**, **infrastructure requirements**. Parity Terminal named as the observability layer for the >30-bot survey [TENTATIVE — sample size and selection bias not disclosed].

### Stacking recommendation (inferred)

Author implies **hybrids**: type 2 + type 1; type 3 as drawdown hedge; type 4 as beginner ramp; type 5 as long-horizon R&D. Cemini prod posture: prioritize types **1 + 2** with measured latency budget; type **3** as research backlog; type **4** only with wallet-alpha hygiene; type **5** sandbox only.

## Snippets

> "From deterministic NWP-based systems to ML-driven bias correction and multi-agent reinforcement learning" [Source: @AlterEgo_eth.docx, 2026-05-27]

> "Verdict: Excellent second layer or replacement for forecast after drawdowns" (type 3) [Source: @AlterEgo_eth.docx, 2026-05-27]
