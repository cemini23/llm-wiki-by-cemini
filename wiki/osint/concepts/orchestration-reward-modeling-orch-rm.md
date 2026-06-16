---
title: Orchestration reward modeling (Orch-RM)
type: concept
tags: [concept, llm-agents, multi-agent, reward-modeling, orchestration, conductor, k118]
keywords: [orch-rm, bradley-terry, mas-orchestra, best-of-n, test-time-scaling, plan-level-reward]
related:
  - sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598-2026-06-16.md
  - concepts/conductor-orchestrator.md
  - concepts/llm-listwise-alignment.md
  - concepts/llm-agent-systems.md
  - entities/tools/orchrm.md
maturity: draft
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- @sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598-2026-06-16.md — K118 primary source
- @concepts/conductor-orchestrator.md — orchestrator BoN + continued-training target
- @concepts/llm-listwise-alignment.md — listwise / preference modeling cluster
- @concepts/llm-agent-systems.md — MAS hub
- @entities/tools/orchrm.md — upstream repo stub

## Raw Concept

K118 arXiv 2606.13598 — **orchestration-level** reward models score multi-agent **plans** without executing full sub-agent rollouts. Self-supervised pairs from MAS-Orchestra training checkpoints.

## Narrative

### Credit-assignment gap

Single-agent RLHF RMs and LLM-as-judge on full rollouts break when:

- Conversation topology varies by role and turn
- Sub-agent execution is expensive (MAS-Orchestra: >1B tokens / 100 GRPO steps)

Orch-RM trains on **win-lose orchestration trajectories** (specialized-over-base, correct-over-incorrect groupings) with Bradley-Terry objective.

### Deployment modes

| Mode | Mechanism | Claimed benefit |
|------|-----------|-----------------|
| Test-time scaling | BoN plan selection | Beats majority vote; ~8% acc lift |
| Continued training | Reward-guided fine-tune on orchestrator | Beats MAS-Orchestra checkpoint; ~10× token savings vs rollout judges |

### Cemini mapping

| Orch-RM idea | Conductor analog |
|--------------|------------------|
| Plan-level scalar reward | Score fan-out topology before worker calls |
| Checkpoint-derived pairs | Mine conductor session logs for preference pairs |
| BoN at orchestration layer | Cheap test-time scaling without full venue execution |

**Verdict:** **REFERENCE** until `Wang-ML-Lab/OrchRM` publishes (404 2026-06-16). Prod brief stages design pattern for server-Claude eval pass.

## Snippets

> "We operate directly at the orchestration level of MAS." [Source: arxiv-2606.13598-2606-13598v1-reward-modeling-for-multi-agent-orc.pdf Fig. 1 caption]
