---
title: "LLM List-wise Alignment — Beyond Token-Level Loss for Ranked Outputs"
type: concept
tags: [concept, llm-training, alignment, recommendation, ranking, grpo, list-wise, bayesian, applied-during-ingest]
keywords: [list-wise-alignment, BoN-alignment, best-of-N, NDCG, fairness, diversity, GRPO, indiscriminate-supervision, gradient-decay, policy-distillation, dynamic-target, ticker-ranking, news-relevance-ranking, conductor-routing]
related:
  - sources/blade-bayesian-listwise-alignment.md
  - concepts/conductor-orchestrator.md
  - concepts/deepseek-models.md
  - concepts/policy-distillation.md
  - concepts/portfolio-strategy.md
  - concepts/llm-agent-systems.md
  - concepts/regime-conditioned-evaluation.md
  - entities/tools/blade-github.md
  - concepts/orchestration-reward-modeling-orch-rm.md
  - sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598-2026-06-16.md
maturity: draft
created: 2026-05-07
updated: 2026-06-16
---

## Relations

- @sources/blade-bayesian-listwise-alignment.md — K33 anchor source; introduces Bayesian dynamic-target alignment as the fix to static BoN failure modes.
- @concepts/conductor-orchestrator.md — Conductor's routing decisions are list-wise (rank candidate model+tool bundles); same alignment problem applies.
- @concepts/deepseek-models.md — GRPO is DeepSeek-R1's training algo and the BLADE optimization backbone.
- @concepts/policy-distillation.md — BoN Alignment is a distillation pattern (compress N-sample inference into single-pass model).
- @concepts/portfolio-strategy.md — ticker-watchlist ranking is the most direct Cemini application surface.
- @concepts/llm-agent-systems.md — agent-system landing area where BLADE-pattern application would land.
- @concepts/regime-conditioned-evaluation.md — sibling K33 concept; both are about evaluation/optimization rigor.
- @entities/tools/blade-github.md — STUDY-METHODOLOGY-only verdict on the unlicensed `RegionCh/BLADE` companion repo; reimplement from CC BY 4.0 paper.

## Raw Concept

K33 ingest of @sources/blade-bayesian-listwise-alignment.md (SIGIR '26) crystallized a pattern that applies to **any LLM-based ranking task**: the standard training pipeline (SFT + DPO) optimizes token-level or pair-level objectives, but downstream success is measured by list-level non-differentiable rewards (NDCG, fairness, diversity, downstream PnL). This page is the concept hub for the mismatch and the BLADE-style fix.

## Narrative

### The problem in one sentence

LLM rankers are trained against token likelihoods or pairwise preferences but evaluated against list-level rewards — a structural mismatch that leaves ranking quality on the table.

### Why standard alignment falls short

- **SFT** (Supervised Fine-Tuning) — maximizes token likelihood under reference outputs. The list ordering is implicit in the token sequence but never directly optimized; small re-rankings change list-level NDCG dramatically while barely shifting token loss.
- **DPO** (Direct Preference Optimization) — pair-wise preference. Two lists $A$ and $B$ get ranked; the model is pushed toward the preferred one. But list-level reward is a function of all $K$ items jointly; pair-wise comparison loses that structure.
- **PPO with reward model** — list-level reward can be computed by a critic. But trains a separate critic network (memory + instability), and the reward model itself has the same offline-distribution problem.

### Best-of-N (BoN) as the inference-time fix

Sample $N$ candidate lists from $\pi_\theta$, pick the one with highest list-wise reward $R(y)$. Bypasses the differentiability constraint entirely. Empirically very effective: NDCG@5 climbs monotonically with $N$ on the BLADE benchmark.

**Cost**: latency scales linearly in $N$. Real-time deployment cap is roughly $N \leq 4$ before SLA breaks. So the question is: can we **internalize** BoN's selection capability into the model weights?

### BoN Alignment

The variational BoN (vBoN) reformulation gives a tractable objective:

$$\mathcal{J}_{\text{BoN}}(\theta) = \mathbb{E}_{y\sim\pi_\theta}\bigl[(N-1)\log F_{\text{ref}}(R(y)) - \log(\pi_\theta(y)/\pi_{\text{ref}}(y))\bigr]$$

The first term is a **quantile reward** — high reward relative to the reference distribution. The second term is **KL regularization** — stay anchored to a sane base.

In practice, $F_{\text{ref}}(\cdot)$ is estimated as the empirical CDF over a fixed set of reference samples. This is the **static-reference formulation** BLADE diagnoses.

### Two failure modes of static BoN Alignment (BLADE diagnostic)

1. **Indiscriminate Supervision** — once the policy generates candidates exceeding the reference's empirical reward range, $F_{\text{ref}}(R(y)) = 1$ for **all** such candidates. The objective stops distinguishing between them. Ranking guidance disappears in exactly the high-reward regime where ranking matters most.

2. **Gradient Decay** — as $\pi_\theta$ outpaces $\pi_{\text{ref}}$, the proportion of reference samples that still provide informative comparison shrinks. The supervision signal vanishes, optimization stalls early.

### The BLADE fix: Bayesian dynamic target

Replace the fixed empirical CDF with a **Bayesian fusion** of (a) static reference prior + (b) dynamic evidence from the model's current rollouts. Each step updates the target distribution to track the policy's evolving capability.

The mathematical machinery is straightforward (conjugate-prior update over reward distribution), but the operational point is: **the alignment target itself is no longer fixed.** The model is chased by a moving frontier rather than anchored to a stale snapshot.

Optimization uses **GRPO** (Group Relative Policy Optimization, the algo behind DeepSeek-R1):

- Sample $G$ candidates per context.
- Compute advantage $A_i = (R(y_i) - \mu_G) / \sigma_G$ — group-relative reward.
- Apply clipped policy update with KL anchor.
- No critic network needed (memory + stability win over PPO).

GRPO is already Cemini's intended training-side algo via the Conductor pipeline (@concepts/conductor-orchestrator.md). The BLADE pattern is a downstream application of the same optimizer to a different objective surface.

### Cemini application surfaces

Each of these is today either (a) prompt-engineered with no learned ranking, or (b) trained with token-level or pair-level loss that suffers BLADE's failure modes. All are candidates for BLADE-style retrofit.

| Surface | What's being ranked | Reward signal | Why list-wise matters |
|---|---|---|---|
| **Ticker watchlist scoring** | Candidate tickers given portfolio context | Portfolio-Sharpe / drawdown / alpha-correlation | Top-K interactions are non-decomposable (covariance, sector concentration) |
| **News-relevance ranking** | Headlines given regime + held positions | Downstream trade-PnL or analyst-judged usefulness | Diversity within the top-K matters as much as point relevance |
| **Conductor query routing** | (model, tool) bundles given query | End-to-end success rate | Routing involves backup/fallback ordering — list-wise structure |
| **Brief-candidate screening** | Paper-ingest candidates for next-week roadmap | Downstream brief-shipping rate | Topic diversity across the top-K matters |
| **Strategy ensemble selection** | Trading-strategy slate for a regime | Aggregate ensemble Sharpe | Strategy-correlation in the slate is non-decomposable |

### Minimum operational pattern (when adopting BLADE-style training)

Per @sources/blade-bayesian-listwise-alignment.md and Cemini's existing training discipline:

1. **Define the list-wise reward** — must be computable from the generated list and ground-truth labels. NDCG@K, downstream PnL, ensemble Sharpe.
2. **Establish a static reference** — typically the SFT model. Compute its reward distribution over a held-out validation set. This is the seed prior $F_{\text{ref}}$.
3. **Bayesian update on rollouts** — at each training step, treat the current group of $G$ rollouts as evidence, update the posterior over reward CDF.
4. **GRPO on quantile reward** — group-relative advantage of each candidate's quantile under the **dynamic** posterior CDF, not the frozen static CDF.
5. **Monitor the gradient-decay diagnostic** — fraction of reference samples with informative comparison. If it falls below ~20%, the dynamic update is the load-bearing component (validates BLADE over static BoN).
6. **Regime-disclosure on evaluation** — per @concepts/regime-conditioned-evaluation.md, any benchmarking of the trained ranker against alternatives must report regime variables (budget, action-space size, prior quality, metric type). Otherwise the ranking is a CATE in disguise.

### Open question: BLADE without DeepSeek-R1-class compute

BLADE's GRPO backbone assumes the ranker is a fine-tunable LLM. Cemini's intended brain is DeepSeek API (no fine-tuning access). For the application surfaces above, the practical path is one of:

- **(a)** Train a small open-weights ranker (Qwen-2-7B or smaller) with BLADE on Cemini's task data; deploy alongside the DeepSeek API for ranking-specific calls.
- **(b)** Use BLADE conceptually for **prompt-time** list-wise feedback: generate $G$ candidates with DeepSeek API per query, score them with a list-wise reward, pick the top one (this is just inference-time BoN — defeats the BLADE-internalization goal but is the no-fine-tuning fallback).
- **(c)** Defer until Cemini's compute posture changes (budget for self-hosted GRPO training run).

This is a brief-level decision, not a wiki-level one. Logged in ROADMAP as research question.

## Snippets

- "Existing LLM4Rec methods primarily rely on token-level objectives, making it difficult to optimize list-level and non-differentiable metrics (e.g., NDCG, fairness) that define actual recommendation quality." [Source: BLADE p.1]
- "While Best-of-N (BoN) directly optimizes these metrics during inference, its high computational cost hinders real-world deployment." [Source: BLADE p.1]
- BLADE NDCG@5 = 0.0410, time = 44.56 s, inference cost 1× — vs static BoN Alignment 0.0333 at same cost; vs inference-time BoN N=4 0.0470 at 4× cost. [Source: BLADE p.3 Table 1]
