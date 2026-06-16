---
title: TT-DAC-PS optimal trade execution (arXiv 2606.08379)
type: source
tags: [source, arxiv, quant-finance, reinforcement-learning, optimal-execution, market-microstructure]
keywords: [2606.08379, TT-DAC-PS, implementation-shortfall, actor-critic, TD3, Almgren-Chriss, LOB]
related:
  - concepts/sequential-optimal-execution-quoting.md
  - concepts/strategic-resource-acquisition-game-theory.md
  - concepts/regime-conditioned-evaluation.md
  - sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md
  - sources/arxiv-particle-methods-partial-observation-2606.09055-2026-06-15.md
  - concepts/partial-observation-stochastic-control.md
  - sources/arxiv-dpg-time-inconsistent-equilibrium-2606.11798-2026-06-16.md
  - concepts/time-inconsistent-stochastic-control.md
maturity: validated
read_status: deep-read
created: 2026-06-10
updated: 2026-06-16
---

## Relations

- @concepts/sequential-optimal-execution-quoting.md — LOB execution theory cluster
- @concepts/strategic-resource-acquisition-game-theory.md — Almgren–Chriss solo-execution vs multi-agent
- @concepts/regime-conditioned-evaluation.md — IS% benchmarking discipline
- @sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md — LOB / MM microstructure sibling
- @sources/arxiv-particle-methods-partial-observation-2606.09055-2026-06-15.md — K117 partial-observation contrast (latent drift vs fully observed state)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | TT-DAC-PS: Twin-Target Deterministic Actor-Critic with Policy Smoothing for Optimal Trade Execution |
| **Authors** | Ilia Zaznov, Atta Badii (Reading); Julian Kunkel (Göttingen); Alfonso Dufour (ICMA Centre) |
| **arXiv** | 2606.08379 (cs.AI) |
| **Pages** | 21 |
| **sha256** | `699fc66380b278e3ed6e53bb6189f3422035d6e3cb4ae807533c2f357652a163` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.08379-pdf-tt-dac-ps-twin-target-deterministic-actor-cr.pdf` |
| **Retrieved** | 2026-06-10 |
| **Read status** | deep-read — abstract, Table 2–3 results, ablations, conclusions |

## Narrative

RL framework for **large sell-program execution** minimizing **implementation shortfall (IS)** on real LOB data for ten U.S. equities. Environment combines **Almgren–Chriss** permanent impact with LOB prices/volumes, per-step participation caps, and utility-based rewards.

**TT-DAC-PS architecture:**

- Twin EMA critic targets with **pessimistic min backup** (TD3-style)
- Target policy smoothing + delayed actor updates
- Conservative Q regularisation against overestimation
- Hybrid OU exploration: episode decay + variance-guided adjustment + SAC-style learned temperature

**Baselines:** PPO, SAC, A2C, TWAP, VWAP, Almgren–Chriss.

**Headline results (IS% mean, selected):**

| Instrument | Vol regime | TT-DAC-PS | Best classical | Worst on-policy |
|------------|------------|-----------|----------------|-----------------|
| INTC | low (0.12%) | **0.03%** | AC 0.04% | PPO 0.11% |
| AMD | high (0.37%) | **−0.02%** | AC 0.01% | PPO 0.14% |
| AVGO | high (0.53%) | **0.12%** | AC 0.13% | PPO 0.65% |
| ADBE | med (0.27%) | **0.01%** | AC 0.02% | PPO 0.46% |

Off-policy actor–critics (TT-DAC-PS, SAC) beat on-policy (PPO, A2C) on most names. VWAP/TWAP competitive in **liquid low-vol** names; fail in **high-impact** regimes (AVGO, ADBE).

**Ablations:** Removing twin-target pessimistic backup or adaptive exploration degrades IS most on AVGO/ADBE — stabilisation matters in hard liquidity/volatility regimes `[CONFIRMED — Table 3, single source]`.

**Cemini implications:**

| Takeaway | Action |
|----------|--------|
| Adaptive exploration > fixed noise in non-stationary LOB | PM/Kalshi size-in over event windows may need regime-conditioned aggression, not static TWAP-like schedules |
| Classical schedules viable in calm books | Don't over-engineer RL execution for deep PM markets with tight spreads |
| IS% + CI reporting | Adopt for any future equity/PM execution backtests in `@concepts/regime-conditioned-evaluation.md` |

**Posture:** REFERENCE for execution-module design — not PM-validated (equity LOB only). No prod brief unless CeminiSuite adds equity execution path.

## Snippets

> "The proposed model consistently reduces mean implementation shortfall percentage with competitive variance, outperforming classical baselines and standard reinforcement learning benchmark models."

> — [Source: arxiv-2606.08379-pdf-tt-dac-ps-twin-target-deterministic-actor-cr.pdf Abstract, retrieved 2026-06-10]

> "While classical strategies such as VWAP remain viable in highly liquid, low-volatility regimes, they fail to protect against implementation shortfall in complex, high-impact scenarios where adaptive control is paramount."

> — [Source: arxiv-2606.08379 p.15, retrieved 2026-06-10]

> "Removing the second target critic and pessimistic minimum backup worsens execution performance on several instruments, particularly AVGO and ADBE."

> — [Source: arxiv-2606.08379 §6.1, retrieved 2026-06-10]
