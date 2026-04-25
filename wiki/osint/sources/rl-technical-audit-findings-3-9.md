---
title: "Technical Research Audit: Reinforcement Learning and Self-Learning Architecture for the Cemini Financial Suite"
type: source
tags: [docx, rl-marl, portfolio-strategy, ml-methods, crypto, prediction-markets, cemini-internal, mappo, torchrl, action-masking, mars]
clusters: [rl-marl, portfolio-strategy, ml-methods, crypto, prediction-markets, cemini-internal]
related: []
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

*(Cross-references will be added in Phase 2.)*

## Raw Concept

- **Original title**: Technical Research Audit: Reinforcement Learning and Self-Learning Architecture for the Cemini Financial Suite
- **Author(s)**: Cemini internal audit (no attributed author)
- **Type**: DOCX (internal audit)
- **Location**: research for cemini/RL Technical Audit Findings 3_9.docx
- **Length**: ~4264 words, 161 paragraphs
- **Retrieved**: 2026-04-23 (filename date 2026-03-09)
- **Read status**: read-skim
- **Primary cluster**: ml-methods
- **All clusters**: rl-marl, portfolio-strategy, ml-methods, crypto, prediction-markets, cemini-internal

## Narrative

Gap-analysis / audit of the Cemini RL architecture, structured as a severity-rated list of findings with "Good enough" vs "Gold standard" vs effort estimates for each. The four headline gaps:

**Gap 1 (HIGH): DSR → DSoR.** Differential Sharpe penalizes upside volatility — destructive for positively-skewed Kalshi / crypto. Migrate to Differential Sortino (2 dev-days). Gold standard is a Composite Risk-Aware Reward combining annualized return + downside risk + Treynor ratio.

**Gap 2 (CRITICAL): Catastrophic forgetting.** Single-weight MAPPO across regimes catastrophically forgets prior regimes during fine-tune. "Good enough" = context windowing (regime one-hot in observation, 1 dev-day). "Gold standard" = MARS (Meta-controlled Agents for a Risk-aware System) — frozen specialist agents (bull, mean-reversion) + Meta-Adaptive Controller dynamically shifting allocation without updating weights (8 dev-days).

**Gap 3 (CRITICAL): Safety boundaries.** Rejects Constrained MDPs (Lagrangian primal-dual) as unstable and non-zero-violation during learning. Prescribes deterministic Action Masking / Projection at the broker-API layer — severed from the learning algorithm (3 dev-days with TorchRL ActionDiscretizer + MaskedCategorical wrapper in the LangGraph EMS router).

**Gap 4 (HIGH): Opacity hurts IP valuation.** Execute SILVER-style episodic Shapley values over observation features as a human-readable JSON attribution artifact (4 dev-days). Concept Bottleneck Models rejected as compute-prohibitive for solo dev.

Then tool evaluations: TorchRL (ADOPT with strict Parallel-API constraint), PettingZoo, etc. Concrete TorchRL code snippet showing a 25K-parameter-per-agent MultiAgentMLP (depth=2, num_cells=64, share_params=False, tanh, centralised_info=True) calibrated for 5 heterogeneous agents on CPU.

Relevant to Cemini as the primary RL audit of record — explicitly IP-sale-oriented, CPU-only, solo-dev. Honest limits: "X developer-days" estimates are ungrounded in prior ticket data; MARS framework cited but not benchmarked; "gold standard" framing is rhetorically persuasive but evidence-light.

## Key findings

- DSR → DSoR migration prescribed (Sharpe symmetrical-vol penalization harms Kalshi/crypto positively-skewed regimes).
- Catastrophic forgetting flagged CRITICAL — prescribed solution is MARS-style frozen-weights ensemble + Meta-Adaptive Controller (dynamic agent weighting, no fine-tuning).
- Context windowing (regime one-hot in obs) is the "good enough" fallback (1 dev-day).
- CMDPs (Lagrangian primal-dual) explicitly rejected as unstable and non-zero-violation-guaranteeing.
- Deterministic Action Masking at broker-API layer is the safety primitive — severed from learning algorithm; 3 dev-days.
- SILVER-style episodic Shapley over obs features is the prescribed interpretability artifact — 4 dev-days; CBMs rejected.
- TorchRL 25K-params-per-agent concrete config: `MultiAgentMLP(n_agents=5, centralised_info=True, share_params=False, depth=2, num_cells=64, activation_class=Tanh)`.
- Strict TorchRL Parallel-API (not AEC) to avoid turn-based tensor stacking bugs.

## Snippets

- **Gap 2** — "The 'gold standard' is an Ensemble Switching architecture, such as the Meta-controlled Agents for a Risk-aware System (MARS) framework… distinct, specialized agents (e.g., a bull expert, a mean-reversion expert) maintain frozen weights. A higher-level Meta-Adaptive Controller (MAC) observes the current regime and dynamically shifts the execution weight allocation among these specialized agents without altering their internal neural network parameters."
- **Gap 3** — "Lagrangian methods are notoriously difficult to tune, exhibit unstable training dynamics, and critically, do not guarantee zero constraint violations during the learning phase. For a solo developer managing a production system, deterministic Action Masking is vastly superior to CMDPs."
- **Executive Summary** — "The immediate priority for the development cycle is the implementation of a hardcoded, deterministic Action Masking overlay within the existing QuantOS and Kalshi execution routing logic before initiating any TorchRL model training."
- **TorchRL snippet** — `n_agents=5, centralised_info=True, share_params=False, depth=2, num_cells=64, activation_class=torch.nn.Tanh` — "25K parameter initialization per agent optimized for CPU".
