---
title: "MMGRPO: Multi-Module GRPO — Composing Policy Gradients and Prompt Optimization for Language Model Programs"
type: source
tags: [source, llm-agents, grpo, policy-optimization, prompt-optimization, multi-module, training-method, conductor-relevant]
keywords: [mmgrpo, multi-module-grpo, policy-gradient, prompt-optimization, compound-ai, module-level-rl, iclr-2026]
related:
  - concepts/llm-agent-systems.md
  - concepts/conductor-orchestrator.md
  - sources/toolorchestra-2511.21689.md
  - sources/training-free-grpo-iclr-2026.md
  - sources/gigpo-neurips-2025.md
  - sources/deep-graphrag-2601-11144.md
  - sources/rl-overview-murphy-2412-05265.md
maturity: validated
created: 2026-05-01
updated: 2026-05-11
read_status: deep-read
---

## Relations

- @concepts/llm-agent-systems.md — MMGRPO is the optimization method for training compound AI systems that LLM-agent-systems describes.
- @sources/toolorchestra-2511.21689.md — ToolOrchestra's RL training loop can use MMGRPO as the optimization algorithm for multi-module orchestrators.
- @sources/training-free-grpo-iclr-2026.md — Training-Free GRPO achieves similar effects without parameter updates; MMGRPO is the full-training alternative.
- @concepts/conductor-orchestrator.md — Conductor is the synthesis concept; MMGRPO is Optimization Method A (full training path).
- @sources/gigpo-neurips-2025.md — GiGPO provides the multi-turn credit assignment MMGRPO needs for agent trajectories.

## Raw Concept

- Original title: Multi-Module GRPO: Composing Policy Gradients and Prompt Optimization for Language Model Programs
- Author(s): Anonymous (ICLR 2026 double-blind under review)
- Type: ICLR 2026 under review
- Location: https://openreview.net/forum?id=dbce6b069b4bef59cad397841c1fefa057862f6a
- Retrieved: 2026-05-01 (K25 Conductor sweep)
- Read status: deep-read

## Narrative

MMGRPO generalizes Group Relative Policy Optimization (GRPO) to compound AI systems — modular programs where multiple LM calls with distinct prompt templates and tools are composed together. Standard GRPO assumes a single model with a single output distribution; MMGRPO groups LM calls by module across rollouts and handles variable-length and interrupted trajectories.

### Key contributions

1. **Multi-module grouping**: GRPO's group-relative advantage estimation applied per-module. Each module (prompt template, tool call, sub-agent) gets its own advantage estimate based on rollouts where that module was active.
2. **Variable-length trajectory handling**: Handles trajectories where different modules activate different numbers of times (interrupted rollouts, early exits).
3. **Composition with automatic prompt optimization**: MMGRPO + prompt optimization outperforms either alone.

### Results

- **11% average accuracy improvement** across classification, many-hop search, and privacy-preserving delegation tasks vs. post-trained LM
- **5% improvement** over prompt optimization alone
- Open source: "released as an open-source optimizer for compound AI systems"

### Why this matters for Conductor

MMGRPO provides the optimization algorithm for training Conductor as a compound AI system. Conductor isn't a single LLM call — it's a multi-module program (classifier → router → LLM selector → response aggregator). MMGRPO can optimize all modules jointly:

1. **Module-level GRPO** — each Conductor component (taxonomy classifier, model selector, confidence judge) gets per-module advantage estimates
2. **Cross-module composition** — improvements to the classifier propagate to better routing decisions downstream
3. **Open source** — directly usable

The 5% gain over prompt optimization alone is the key stat: MMGRPO improves the system beyond what prompt engineering can achieve.

## Snippets

**S1 — Core problem**:
> "AI systems are increasingly expressed as modular programs that mix together multiple LM calls with distinct prompt templates and other tools, and it is not clear how best to leverage GRPO to improve these systems."

**S2 — MMGRPO definition**:
> "A simple multi-module generalization of GRPO that groups LM calls by module across rollouts and handles variable-length and interrupted trajectories."

**S3 — Results**:
> "mmGRPO, composed with automatic prompt optimization, improves accuracy by 11% on average across classification, many-hop search, and privacy-preserving delegation tasks against the post-trained LM — and by 5% against prompt optimization on its own."

**S4 — Release**:
> "MMGRPO is released as an open-source optimizer for compound AI systems."
