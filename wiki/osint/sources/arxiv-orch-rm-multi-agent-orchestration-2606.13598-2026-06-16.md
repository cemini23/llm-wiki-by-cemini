---
title: "Reward Modeling for Multi-Agent Orchestration — Orch-RM (arXiv 2606.13598)"
type: source
tags: [source, arxiv, llm-agents, multi-agent, reward-modeling, orchestration, k118]
keywords: [2606.13598, orch-rm, bradley-terry, mas-orchestra, test-time-scaling, best-of-n]
related:
  - concepts/orchestration-reward-modeling-orch-rm.md
  - concepts/conductor-orchestrator.md
  - concepts/llm-agent-systems.md
  - entities/tools/orchrm.md
  - concepts/llm-listwise-alignment.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-06-16
clusters: [llm-agents, rl-marl, ml-methods]
---

## Relations

- @concepts/orchestration-reward-modeling-orch-rm.md — Orch-RM framework summary
- @concepts/conductor-orchestrator.md — orchestrator training / BoN selection target
- @concepts/llm-agent-systems.md — MAS cluster hub
- @entities/tools/orchrm.md — repo stub (not yet published)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Reward Modeling for Multi-Agent Orchestration |
| **Authors** | Tsang, Zhao, Venkataramani, Shi, Ke, Yavuz, Joty, Wang (Rutgers + Salesforce AI Research) |
| **arXiv** | 2606.13598 |
| **sha256** | `18b7455f2d190967187c8c5034c54f9f6fe07ceb3cbf79b9caea1660515936ad` |
| **Repo (claimed)** | https://github.com/Wang-ML-Lab/OrchRM — **404 as of 2026-06-16** [OPEN QUESTION 2026-06-16] |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.13598-2606-13598v1-reward-modeling-for-multi-agent-orc.pdf` |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (abstract + §1–3 methodology overview) |

## Narrative

**Orch-RM (Orchestration Reward Modeling)** — self-supervised reward model for **orchestration quality** without human preference labels.

**Mechanism:** harvest intermediate artifacts (checkpoints, trajectories) from **MAS-Orchestra** training; multi-faceted grouping builds win-lose orchestration pairs; train **Bradley-Terry** scalar reward model that scores **plans** without full sub-agent rollouts.

**Headline gains (paper claims):**

| Use | Result |
|-----|--------|
| Test-time scaling (BoN) | ~**8%** accuracy lift vs baselines |
| Continued orchestrator training | Consistent gains vs MAS-Orchestra checkpoint |
| Token efficiency | ~**10×** fewer tokens vs rollout-heavy judges |

**Domains tested:** math reasoning, web QA, multi-hop reasoning.

**Why it matters for Cemini:** existing RMs / LLM-as-judge fail on **orchestration-level** credit assignment (trajectory shape varies by role/turn). Orch-RM operates at the **plan** layer — aligns with Conductor's multi-model fan-out without 1B-token GRPO budgets.

**Cemini posture:** **REFERENCE** — repo not published; steal **orchestration-level BoN** + **checkpoint-derived preference pairs** as design pattern for conductor eval. Phase-0: `adopt_k118_phase0.sh` (smoke only when repo lands).

## Snippets

> "Orch-RM operates directly at the orchestration level, enabling efficient and high-performing reward-guided orchestrator training and MAS test-time scaling." [Source: arxiv-2606.13598-2606-13598v1-reward-modeling-for-multi-agent-orc.pdf abstract]

> "Orch-RM improves training efficiency by up to 10× in token usage while improving MAS test-time scaling performance by up to 8% in accuracy." [Source: arxiv-2606.13598-2606-13598v1-reward-modeling-for-multi-agent-orc.pdf abstract]

> "Traditional scalar and process reward models… struggle to reliably evaluate the out-of-distribution, conversational dynamics inherent to multi-agent orchestration." [Source: arxiv-2606.13598-2606-13598v1-reward-modeling-for-multi-agent-orc.pdf §2, citing MAS-ProVe]
