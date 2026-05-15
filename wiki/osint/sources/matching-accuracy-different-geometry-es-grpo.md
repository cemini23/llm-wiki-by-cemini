---
title: "Matching Accuracy, Different Geometry — ES vs GRPO Catastrophic Forgetting (Academic Paper, 2026)"
type: source
tags: [paper, rl-marl, evolution-strategies, grpo, catastrophic-forgetting, kl-divergence, continual-learning, cemini-internal-evaluation]
keywords: [es-vs-grpo, evolution-strategies, group-relative-policy-optimization, off-manifold-random-walks, catastrophic-forgetting, kl-divergence-tracking, sequential-continual-learning, mappo, parameter-space-geometry, cross-asset-training]
related:
  - sources/4-3-link-research.md
  - sources/sakana-trinity-llm-coordinator.md
  - sources/sakana-conductor-rl-orchestration.md
  - concepts/rl-marl-research.md
  - concepts/scatter-gather-topology.md
  - entities/frameworks/langgraph.md
  - sources/refinerl-self-refinement-rl.md
  - sources/eggro-evolution-strategies-hyperscale-2026.md
maturity: validated
read_status: deep-read
created: 2026-05-01
updated: 2026-05-15
clusters: [rl-marl, cemini-internal]
---

## Relations

- @sources/4-3-link-research.md — parent K13 source; this paper is Promotion #1 from the 18-section link-eval
- @sources/sakana-trinity-llm-coordinator.md — Trinity uses sep-CMA-ES (an Evolution Strategies variant); this paper's finding that ES causes catastrophic forgetting weighs against Trinity for continual-learning deployments
- @sources/sakana-conductor-rl-orchestration.md — Conductor uses GRPO; this paper's finding that GRPO maintains policy stability across sequential tasks supports Conductor over Trinity
- @sources/eggro-evolution-strategies-hyperscale-2026.md — EGGROLL provides the scalable ES implementation; this paper's catastrophic forgetting finding makes the ES-vs-GRPO trade-off actionable
- @concepts/rl-marl-research.md — corpus hub; first paper in the corpus providing mathematical comparison of ES vs GRPO training geometry
- @concepts/scatter-gather-topology.md — cross-asset KL divergence tracking directly informs multi-asset orchestrator routing stability
- @entities/frameworks/langgraph.md — the sequential checkpointing evaluation pattern maps to LangGraph's typed state graph across BTC/SPY asset boundaries
- @sources/refinerl-self-refinement-rl.md — sibling promotion from K13; RefineRL's GRPO implementation excludes KL-regularization, which this paper identifies as the primary defense against catastrophic forgetting — the two papers form a paired read on GRPO best practices

## Raw Concept

- **Original title**: Matching Accuracy, Different Geometry (full title not captured in Cemini evaluation; the evaluation refers to it as analyzing "geometric differences in parameter space when training models using Evolution Strategies versus Group Relative Policy Optimization")
- **Author(s)**: Unknown (paper not directly accessed; evaluated via Cemini-internal link-eval audit)
- **Type**: Academic paper (conference/journal, 2026)
- **Location**: Original paper URL not captured in the Cemini evaluation; the evaluation is in cemini-librarian:/opt/cemini-bulk/research/4_3 link research.docx (ES vs GRPO section)
- **Retrieved**: 2026-04-03 (Cemini evaluation date)
- **Read status**: deep-read (2026-05-01, via K13 Cemini-internal evaluation)

## Narrative

### What the paper shows

The paper analyzes geometric differences in parameter space between Evolution Strategies (ES) and Group Relative Policy Optimization (GRPO). The core finding: **while both methods achieve similar task accuracy, ES accumulates massive off-manifold random walks resulting in weight updates up to 100× larger than GRPO**, which leads to severe catastrophic forgetting in sequential continual learning environments [Source: 4_3 link research.docx, ES vs GRPO section].

This finding has direct architectural implications for the Cemini stack's RL training path — and for the unresolved Trinity-vs-Conductor decision in ROADMAP.

### Cemini relevance — three axes

**1. Trinity-vs-Conductor decision impact.** Trinity (sep-CMA-ES) is an Evolution Strategies variant; Conductor (GRPO) is GRPO-based. This paper provides the first mathematical evidence in the corpus that ES-based training is structurally vulnerable to catastrophic forgetting across sequential tasks — exactly the cross-asset scenario Cemini faces (BTC-USD → SPY → multi-asset). This tilts the conductor decision toward Conductor/Fugu on a *training-stability* dimension that was previously absent from the comparison. The ROADMAP comparison table currently weighs parameter budget (Trinity = 0.6B SLM + 10K head; Conductor = 7B LLM) and implementation complexity (Trinity = ES-only, simpler; Conductor = GRPO/RL, richer). The catastrophic-forgetting finding adds a third dimension: **training stability under continual cross-asset learning**.

**2. Cross-asset KL divergence tracking.** The paper's technique of tracking incremental KL divergence per training step to measure off-target drift is computationally trivial on CPU and provides a mathematically rigorous metric to ensure the 62K-parameter MAPPO models remain stable across asset-class boundaries [Source: 4_3 link research.docx, ES vs GRPO section, ¶3]. The evaluation recommends implementing automated KL divergence logging between BTC and SPY policy updates during the retrain window.

**3. Validation of gradient-based PPO over gradient-free ES.** The paper's finding that "the variance of the off-manifold drift scales linearly with the parameter dimension" for ES means that for any realistic parameter count, gradient-free methods are provably worse. This mathematically validates Cemini's existing MAPPO (gradient-based PPO) architecture choice over ES alternatives [Source: 4_3 link research.docx, ES vs GRPO section, ¶5].

### Solo-dev assessment (from Cemini evaluation)

| Component | Rating | Justification |
|---|---|---|
| KL Divergence Tracking | 🟢 LOW | Standard mathematical divergence tracking; minimal Python scripting, zero new services |
| Sequential Checkpointing | 🟢 LOW | Evaluate models sequentially across distinct tasks; existing PyTorch checkpointing suffices |
| Linear Interpolation Testing | 🟢 LOW | Verify loss basin stability between checkpoints; standard PyTorch evaluation |

All three recommendations are 🟢 LOW effort — implementable within the existing PyTorch MAPPO training loop without new dependencies.

### Stale-snapshot note

The evaluation references the "April 14-17 retrain window" as the target for implementing KL divergence tracking. Per K8/K11 findings, that window was a logic-audit-and-bugfix period, not an RL retrain. The KL divergence tracking recommendation remains valid but its scheduling anchor is stale.

## Snippets

> "This published academic paper analyzes the geometric differences in parameter space when training models using Evolution Strategies (ES) versus Group Relative Policy Optimization (GRPO). It demonstrates mathematically and empirically that while both methods can achieve similar task accuracy, Evolution Strategies accumulate massive off-manifold random walks—resulting in weight updates up to 100x larger than GRPO—which leads to severe catastrophic forgetting in sequential continual learning environments." [Source: 4_3 link research.docx, ES vs GRPO section, ¶1]

> "The Sequential Continual Learning Checkpointing pattern is highly relevant. The researchers evaluate models sequentially across distinct, isolated tasks, measuring degradation at each boundary. This evaluation pattern must be adapted into the Cemini stack. The system should implement a similar checkpointing and linear interpolation evaluation between the BTC-USD and SPY datasets to ensure the PyTorch MAPPO agents are not suffering from catastrophic forgetting when context switching across different asset classes within the multi-broker EMS." [Source: 4_3 link research.docx, ES vs GRPO section, ¶2]

> "The technique of tracking incremental Kullback-Leibler (KL) Divergence per training step to measure off-target drift is highly valuable. Calculating KL divergence between policy updates is computationally trivial on the CPU and provides a mathematically rigorous metric to ensure the 62K parameter models remain stable." [Source: 4_3 link research.docx, ES vs GRPO section, ¶3]

> "The researchers continue to evaluate Evolution Strategies for massive parameter spaces despite acknowledging the fundamental theoretical limitations where the variance of the off-manifold drift scales linearly with the parameter dimension. For a solo developer managing a latency-sensitive trading system, dedicating compute resources to gradient-free Evolution Strategies is a profound waste of time and processing power compared to efficient gradient-based Reinforcement Learning." [Source: 4_3 link research.docx, ES vs GRPO section, ¶5]

> "The findings in this paper mathematically validate the architectural choice of utilizing MAPPO—a gradient-based Proximal Policy Optimization variant—over gradient-free methods. A thorough technical due diligence audit will highly value the documented, mathematically sound justification for avoiding Evolution Strategies to prevent catastrophic forgetting across the varying data distributions of cryptocurrency and traditional equity markets." [Source: 4_3 link research.docx, ES vs GRPO section, ¶6 — IP-sale relevance]
