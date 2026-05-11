---
title: "GiGPO: Group-in-Group Policy Optimization for LLM Agent Training"
type: source
tags: [source, llm-agents, grpo, multi-turn-rl, credit-assignment, agent-training, neurips-2025, conductor-relevant]
keywords: [gigpo, group-in-group, policy-optimization, multi-turn-agent, credit-assignment, grpo, neurips-2025, ntu-skywork]
related:
  - concepts/llm-agent-systems.md
  - concepts/conductor-orchestrator.md
  - sources/mmgrpo-iclr-2026.md
  - sources/toolorchestra-2511.21689.md
  - sources/training-free-grpo-iclr-2026.md
  - sources/deep-graphrag-2601-11144.md
  - sources/rl-overview-murphy-2412-05265.md
maturity: validated
created: 2026-05-01
updated: 2026-05-11
read_status: deep-read
---

## Relations

- @concepts/llm-agent-systems.md — GiGPO solves the multi-turn credit assignment problem for LLM agent training that single-turn GRPO can't handle.
- @concepts/conductor-orchestrator.md — Conductor is the synthesis concept; GiGPO provides the multi-turn credit assignment for Conductor's routing trajectories.
- @sources/mmgrpo-iclr-2026.md — MMGRPO handles multi-module; GiGPO handles multi-turn. Together they cover both dimensions of Conductor optimization.
- @sources/toolorchestra-2511.21689.md — ToolOrchestra's orchestrator trajectories need multi-turn credit assignment; GiGPO provides it.
- @sources/training-free-grpo-iclr-2026.md — GiGPO needs parameter access (full RL); Training-Free GRPO is the API-only alternative.

## Raw Concept

- Original title: Group-in-Group Policy Optimization for LLM Agent Training
- Author(s): Lang Feng, Zhenghai Xue, Tingcong Liu, Bo An (NTU + Skywork AI)
- Type: NeurIPS 2025
- Location: https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf
- Retrieved: 2026-05-01 (K25 Conductor sweep)
- Read status: deep-read

## Narrative

GiGPO addresses the core limitation of GRPO for agent training: GRPO works well for single-turn tasks (math, code) but struggles with multi-turn agent trajectories where rewards are sparse/delayed and credit assignment across steps is ambiguous.

### Key innovation: two-level advantage estimation

Standard GRPO compares a rollout against a group baseline at the episode level. GiGPO introduces a nested structure:

1. **Episode-level**: compare full trajectory outcomes across a group of rollouts (standard GRPO)
2. **Step-level**: within each episode, compare individual steps against a step-group baseline

This two-level structure enables fine-grained credit assignment: a step that contributed to a successful episode gets positive advantage even if other steps in the same episode were neutral. Conversely, a poor step in a successful episode gets penalized.

### Properties

- **Critic-free** — no value function needed (inherits GRPO's simplicity)
- **Low memory** — group-based comparisons, no replay buffer
- **Stable convergence** — two-level grouping reduces variance
- **Multi-turn agent benchmarks** — tested on ALFWorld and other interactive environments

### Author credibility

Bo An (NTU) is a major figure in multi-agent RL. Skywork AI is the AI arm of Kunlun Tech. NeurIPS 2025 acceptance signals strong peer review.

### Why this matters for Conductor

Conductor operates over multi-turn agent trajectories (classify → route → execute → evaluate → possibly re-route). Standard GRPO can't credit-assign whether the routing decision or the tool execution was responsible for the outcome. GiGPO's two-level structure solves this:

1. **Episode-level**: did this full Conductor trajectory succeed?
2. **Step-level**: was the routing decision good? Was the model selection correct? Was the tool execution accurate?

This is the fine-grained optimization signal Conductor needs to improve its routing decisions over time.

## Snippets

**S1 — Core problem**:
> "Unlike static tasks, agent-environment interactions unfold over many steps and often yield sparse or delayed rewards, making credit assignment across individual steps significantly more challenging."

**S2 — GiGPO structure**:
> "GiGPO introduces a two-level structure for estimating relative advantage: (i) At the episode-level, comparing trajectories across groups; (ii) At the step-level, comparing individual actions within an episode."

**S3 — Properties preserved**:
> "Critic-free, low memory, and stable convergence."

**S4 — Baseline comparison**:
> "PPO improves average ALFWorld performance substantially; GiGPO further improves upon PPO through fine-grained credit assignment."
