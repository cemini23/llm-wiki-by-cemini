---
title: "MARL Trading Architecture — design patterns for Cemini's MAPPO stack"
type: concept
tags: [concept, rl-marl, mappo, marl, trading-architecture, conductor, cemini-internal, k49]
keywords: [mappo, maddpg, masac, iddpg, ctde, hierarchical-marl, time-frame-allocator, volatility-gating, communication-constrained-marl, base-policy-prediction, rl-model-routing, rlae]
related:
  - sources/hi-darts.md
  - sources/3-29-3.md
  - sources/3-29-9.md
  - sources/3-29-18.md
  - concepts/rl-marl-research.md
  - concepts/rl-retrain-pipeline-hardening.md
  - sources/arxiv-rmats-geopolitical-multi-agent-2605.25311.md
maturity: validated
created: 2026-05-16
updated: 2026-05-30
---

## Relations

- @sources/hi-darts.md — hierarchical volatility-gated multi-agent PPO trading system (anchor)
- @sources/3-29-3.md — MAPPO vs MASAC/MADDPG/IDDPG empirical benchmark (anchor)
- @sources/3-29-9.md — communication-constrained cooperative MARL / base policy prediction (anchor)
- @sources/3-29-18.md — RLAE: RL-assisted dynamic ensemble weighting for LLMs (anchor)
- @concepts/rl-marl-research.md — RL/MARL corpus-index hub
- @concepts/rl-retrain-pipeline-hardening.md — sibling Cemini-MARL concept: this page is *architecture*, that one is *retrain process*
- @sources/arxiv-rmats-geopolitical-multi-agent-2605.25311.md — K87: recursive typed-message coordination until weight convergence; contrast with fixed TradingAgents debate rounds

## Raw Concept

Synthesis page assembled 2026-05-16 from four MARL papers deep-read in the K49 cited-unread campaign (batches 3 + 7). The question it answers: **what does the current external MARL literature say about how Cemini's 5-agent MAPPO trading stack and conductor should be architected?** Paired with the `briefs/2026-05-16_marl-architecture-findings.md` deliverable shipped to cemini-prod.

## Narrative

Cemini's trading brain is a 5-agent MAPPO system (MacroForecaster / BullAdvocate / BearAdvocate / RiskAssessor / Trader). Four independent papers, read cold, converge on four architecture-level findings.

### 1. Algorithm choice — MAPPO is validated `[CONFIRMED]`

A 4-algorithm benchmark (`@sources/3-29-3.md`) under the centralized-training–decentralized-execution (CTDE) paradigm, on a competitive multi-seller pricing environment, 10 seeds:

| Algorithm | Profit (norm.) | Behaviour |
|-----------|---------------|-----------|
| **MAPPO** | 0.91 (highest) | +16% vs MADDPG, +47% vs IDDPG; low cross-seed variance |
| MADDPG | lower | fairest outcomes (Jain 0.96) — pick only if equity is the objective |
| IDDPG | — | highest variance — confirms CTDE coordination is load-bearing |
| MASAC | negative | failed to converge — Q-value overestimation + entropy-coefficient sensitivity |

Cemini's MAPPO choice is independently corroborated for continuous-action competitive economic environments. MASAC is a documented cautionary case; MADDPG only where fairness across agents outranks profit.

### 2. Hierarchical volatility-gated execution — a candidate extension

Cemini runs at a fixed decision cadence. **Hi-DARTS** (`@sources/hi-darts.md`) demonstrates a two-layer alternative: a top-layer **Time Frame Allocator** meta-agent reads market state + reward feedback and routes execution to a lower-layer agent specialised at 1-min / 10-min / 1-hour resolution. Reward-shaping pair: log-return `R = ln(V_t/V_{t-1})` for the allocator, `tanh`-bounded normalized profit for sub-agents. Backtest beat buy-and-hold, SPY, and every single-frequency agent standalone; the allocator demonstrably leaned on the fast agent only in the most volatile quartile.

Pattern for Cemini: **gate execution frequency on volatility via a meta-agent.** Worth evaluating if fixed-cadence execution wastes compute in calm regimes or reacts too slowly in volatile ones. Proof-of-concept scale (single stock) — adopt as a design pattern, not a drop-in.

### 3. Communication-constrained coordination — base policy prediction

Cooperative MARL normally assumes cheap frequent access to global information; throttle that synchronization and importance-sampling gradient variance explodes. `@sources/3-29-9.md`'s **base policy prediction** uses old gradients to predict a sequence of upcoming policy updates and collects samples for that whole sequence within one communication round — converging to ε-Nash in O(ε⁻³ᐟ⁴) communication rounds and removing the exponential joint-action-space dependence of earlier work. Validated inside MAPPO. Directly applicable if Cemini's 5 agents ever run with throttled inter-agent synchronization (distributed or rate-limited deployment).

### 4. RL-based model routing for the conductor

`@sources/3-29-18.md` (RLAE) casts multi-LLM ensembling as an MDP — state = prompt + history, action = per-model weight vector, reward = output quality. `RLAE_MAPPO` gives each model its own RL agent + shared centralized critic, so the joint action space decomposes and scales as models are added; +3.3 accuracy points over fixed-weight ensembling, no reward signal needed at inference. The conductor's blend/route-across-models job is exactly this problem — evidence that **dynamic context-conditioned weighting beats static routing rules**.

### Synthesis — the four findings as a Cemini design checklist

1. Keep **MAPPO** as the base algorithm; CTDE coordination is load-bearing; avoid MASAC.
2. Consider a **hierarchical meta-agent gating execution frequency on volatility** (Hi-DARTS pattern).
3. If inter-agent synchronization is ever throttled, apply **base policy prediction** to keep MAPPO stable.
4. For the conductor, prefer **RL-based context-conditioned model weighting** over static routing rules.

`[NEEDS VERIFICATION 2026-05-16]` All four findings are external-paper-derived; none has been tested against Cemini's own instruments or stack. Server-side validation owned by server-Claude — see the cemini-prod brief.

## Snippets

> "MAPPO achieved the highest average profit (0.91), outperforming MADDPG by +16% and IDDPG by +47%." [Source: 3:29 3.pdf — Results, Table II]

> "The top layer — a 'Time Frame Allocator' meta-agent — reads real-time market data plus reward feedback and selects which specialized lower-layer 'Time Frame Agent' should trade." [Source: Hi-DARTS.pdf — architecture]
