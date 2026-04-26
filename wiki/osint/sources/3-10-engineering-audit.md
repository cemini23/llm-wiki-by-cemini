---
title: "Technical Research Audit: Data Pipeline and Feature Engineering Optimization for Cemini Financial Suite"
type: source
tags: [docx, rl-marl, portfolio-strategy, market-microstructure, ml-methods, cemini-internal, polars, timescaledb, continuous-aggregates, normalization, multi-timeframe, orjson, pandas]
clusters: [rl-marl, portfolio-strategy, market-microstructure, ml-methods, cemini-internal]
related:
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Technical Research Audit: Data Pipeline and Feature Engineering Optimization for Cemini Financial Suite
- **Author(s)**: Cemini internal audit (no attributed author)
- **Type**: DOCX (internal engineering audit)
- **Location**: research for cemini/3_10 Engineering Audit.docx
- **Length**: ~4214 words, 146 paragraphs
- **Retrieved**: 2026-04-23 (filename date 2026-03-10)
- **Read status**: read-skim
- **Primary cluster**: cemini-internal
- **All clusters**: rl-marl, portfolio-strategy, market-microstructure, ml-methods, cemini-internal

## Narrative

Structured six-gap engineering audit of the Cemini data pipeline and feature engineering layer, in the "Severity / Current State / Good Enough vs Gold Standard / Effort" format consistent with `rl-technical-audit-findings-3-9.md`.

**Gap 1 (CRITICAL): Memory-bound eager Pandas.** Pandas eager materialization + single-threaded GIL-bound execution will OOM-kill the container as data scales. Cited benchmark: 9GB dataset → 10+GB RAM in Pandas vs <1GB in modern columnar engines. Good enough = Polars lazy-API migration on the hottest feature-engineering functions (4–6 dev-days). Gold standard = full Arrow-native zero-copy pipeline from TimescaleDB through FastAPI response.

**Gap 2 (HIGH): Feature-space dimensionality.** Rejects learned embeddings (FinBERT vectors) and PCA compression. Cites a study (2.79M observations across thousands of equities) where a parsimonious linear model on engineered domain features achieved **Sharpe 1.30**, while an ICA + Wavelet Coherence + LSTM pipeline *collapsed to predicting the unconditional mean with negative returns*. Good enough = deterministic observation vector with technical indicators + bounded sentiment scalars + categorical regime flags. Gold standard = offline SRL with dynamic feature weighting (rejected as solo-dev-unsuitable). 2 dev-days.

**Gap 3 (CRITICAL): TimescaleDB continuous-aggregate silent-invalidation bug.** When refresh policies are set with **NULL end_offset**, the materialization watermark is pushed into the future; live queries cease including recent time buckets → stale data feeding the Kalshi Autopilot. Also flags OHLCV aggregation function not natively handling volume summation without explicit casting. Fix: `DROP` + recreate CAGGs with `WITH NO DATA` and explicit positive `start_offset` / `end_offset`. 1 dev-day via dbmate migration.

**Gap 4 (MEDIUM): Single-timeframe exploitation.** Playbook uses only EMA21 + SMA50 on one timeframe → RL agent over-fits micro-trends and gets wiped by macro regime shifts. Good enough = hierarchical 1h / 15m / 5m observation stack for macro-bias / tactical / execution-trigger. Gold standard = dynamically-adjusted horizons via Hurst exponent (rejected for complexity). 3 dev-days.

**Gap 5 (HIGH): Magnitude bias in heterogeneous observation space.** Raw prices ($400), sentiment (0.5), F&G index (85), volume (2.5M) — PPO/actor-critic will be dominated by price+volume magnitudes, preventing learning from bounded indicators. Good enough = log-returns for prices + min-max for oscillators. Gold standard = Z-score with 3σ clipping for fat-tailed distributions. 2 dev-days.

**Gap 6 (LOW): JSON serialization overhead.** Default FastAPI `jsonable_encoder` + stdlib `json` causes double-serialization on large backtesting payloads. Fix = `orjson` (C-based) as custom response class — bigger payloads get 2–3× faster serialization.

Relevant to Cemini as the canonical engineering-level gap analysis — very concrete, with specific SQL patterns, specific benchmarks cited, specific effort estimates. This is the "what to fix first" companion to the RL-algorithmic-audit in `rl-technical-audit-findings-3-9.md` and the scalability-roadmap in `cemini-suites-technical-analysis.md` (the latter conflicts with this doc's Hetzner CPU-only invariant). Honest limits: (1) dev-day estimates ungrounded; (2) the "ICA+Wavelet+LSTM collapsed to unconditional mean" citation is load-bearing for Gap 2 but the primary-source citation is thin; (3) the "Gap 3 NULL-end-offset bug" is a real documented TimescaleDB footgun but the severity framing is rhetorical — some data pipelines tolerate minutes of staleness; (4) Gap 6 is listed as LOW severity but labelled "severe latency" in the body — mixed signals about urgency; (5) no benchmarks on the Cemini-specific dataset to validate Polars vs Pandas projection.

## Key findings

- **Gap 1 CRITICAL**: Pandas eager evaluation → OOM at scale; migrate hot-path to Polars lazy API (4–6 dev-days).
- **Gap 2 HIGH**: Prefer engineered domain features + bounded scalar sentiment over learned embeddings / PCA; cited study: parsimonious linear Sharpe 1.30 beats ICA+Wavelet+LSTM which collapses to unconditional mean.
- **Gap 3 CRITICAL**: TimescaleDB CAGG with NULL end_offset pushes materialization watermark into future → silent-stale-data failure. Fix via DROP + explicit start/end offsets + WITH NO DATA (1 dev-day).
- **Gap 4 MEDIUM**: Hierarchical multi-timeframe observation stack: 1h macro bias + 15m tactical setup + 5m execution trigger (3 dev-days).
- **Gap 5 HIGH**: Magnitude-bias normalization: log-returns on prices, min-max on oscillators, Z-score with 3σ clip on fat-tailed volume (2 dev-days).
- **Gap 6 LOW**: Replace FastAPI default serializer with `orjson` for 2–3× serialization speedup on large payloads.
- Reinforces CPU-only Hetzner architectural invariant — conflicts with scale-up roadmap in `cemini-suites-technical-analysis.md`.
- Reinforces "deterministic, normalized, bounded, interpretable features" principle across the stack.

## Snippets

- **Gap 1** — "Benchmarks demonstrate that a 9-gigabyte dataset can consume over 10 gigabytes of RAM merely for loading and simple filtering in Pandas, whereas modern columnar engines can process the same data using under 1 gigabyte of memory."
- **Gap 2** — "A comprehensive study analyzing 2.79 million observations across thousands of equities demonstrated that a parsimonious linear model utilizing carefully engineered, normalized domain features achieved a Sharpe ratio of 1.30, whereas a complex pipeline utilizing Independent Component Analysis (ICA), Wavelet Coherence, and Long Short-Term Memory (LSTM) networks collapsed, predicting the unconditional mean and yielding a negative return."
- **Gap 3** — "a documented architectural flaw occurs when refresh policies are configured with a NULL end offset. This pushes the materialization watermark into the future, causing a silent failure where real-time queries cease to include the most recent time buckets, rendering the live trading signals stale."
- **Gap 4** — "Relying on a narrow timeframe causes RL algorithms to suffer from 'single-time-frame exploitation,' where an agent perfectly optimizes for local micro-trends but is repeatedly destroyed by broader macro regime shifts."
- **Gap 5** — "If this raw matrix is fed into an actor-critic network, the neural network weights will be overwhelmingly dominated by the features with the largest numerical magnitudes (volume and price)."
