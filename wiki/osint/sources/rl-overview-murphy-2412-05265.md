---
title: "Reinforcement Learning: An Overview (Murphy, arXiv 2412.05265, v5)"
type: source
tags: [reinforcement-learning, methodology-reference, textbook, conductor-relevant, mappo-relevant]
keywords: [rl-overview, kevin-murphy, value-based-rl, policy-gradient, actor-critic, model-based-rl, multi-agent-rl, marl, grpo-context]
related:
  - concepts/conductor-orchestrator.md
  - concepts/mappo.md
  - concepts/autoresearch-loop-pattern.md
  - sources/training-free-grpo-iclr-2026.md
  - sources/mmgrpo-iclr-2026.md
  - sources/gigpo-neurips-2025.md
  - sources/deep-graphrag-2601-11144.md
maturity: validated
read_status: skimmed
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @concepts/conductor-orchestrator.md — Conductor uses GRPO variants (Path A trained orchestrator, Path B token-prior); Murphy's overview provides the canonical RL textbook reference for the underlying methods
- @concepts/mappo.md — MAPPO is one specific multi-agent RL algorithm; Murphy §5 (Multi-agent RL) is the canonical reference
- @concepts/autoresearch-loop-pattern.md — RL is the meta-framework underlying autoresearch loops (proposal × objective × mutation = exploration × reward × policy update)
- @sources/training-free-grpo-iclr-2026.md, @sources/mmgrpo-iclr-2026.md, @sources/gigpo-neurips-2025.md — K25 Conductor-sweep GRPO papers; Murphy provides §3.5 (Gradient-free policy optimization) and §3.1 (Policy gradient methods) as the foundational reference
- @sources/deep-graphrag-2601-11144.md — companion 2026-05-05 ingest; DW-GRPO is one of many RL-applied-to-LLM techniques covered in spirit by Murphy

## Raw Concept

- Original title: Reinforcement Learning: An Overview
- Author: Kevin P. Murphy (Google Research; author of *Machine Learning: A Probabilistic Perspective*, *Probabilistic Machine Learning*)
- Type: arXiv preprint (textbook-length survey)
- arXiv ID: 2412.05265
- Version: v5 (1 December 2025)
- Pages: 253 (substantial — textbook scope)
- Location: cemini-librarian:/opt/cemini-bulk/research/Reinforcement Learning- An Overview.pdf
- Retrieved: 2026-05-05
- Read status: **skimmed** (TOC + intro). Deep-read deferred — this is reference material, not a single-thesis paper.

## Narrative

Kevin Murphy's 253-page survey of modern RL. Comprehensive coverage from basic Bellman-equation foundations through value-based methods, policy gradients, model-based RL, and multi-agent RL. Functions as **the canonical RL textbook reference** for any time Cemini's research touches RL methods.

### Section structure (TOC sample)

| Chapter | Topic | Cemini relevance |
|---------|-------|-------------------|
| 1 | Introduction (sequential decision making, canonical models) | Background |
| 2 | Value-based RL (Q-learning, SARSA, TD methods) | Background |
| 3 | Policy-based RL (gradient methods, actor-critic, **§3.5 Gradient-free policy optimization**) | **Direct relevance to Conductor's GRPO variants** |
| 3.6 | RL as inference | Bayesian-RL framing; relevant to Cemini's confidence-aware decisions |
| 4 | Model-based RL (decision-time planning, world models) | Future relevance for backtest-driven trade decisions |
| 5 | Multi-agent RL (games, solution concepts, ...) | **Direct relevance to MAPPO** + atlas-gic 25-agent debate pattern |

### Why this matters for Cemini

This is **reference material**, not a single-finding paper. Use it as the canonical RL citation when:

1. Discussing GRPO / training-free GRPO / MMGRPO / DW-GRPO (K25 Conductor sweep + K30 Deep GraphRAG) — Murphy §3.1 + §3.5 are the textbook foundation
2. Discussing MAPPO / multi-agent debate / atlas-gic 25-agent autoresearch — Murphy §5 (Multi-agent RL) is the textbook foundation
3. Discussing model-based RL / world models — Murphy §4
4. Authoring any concept page that needs a "see Murphy ch. N" pointer for foundational RL concepts

### Why this isn't a deep-read priority

It's a 253-page reference. Deep-reading the whole thing is a multi-week effort with diminishing marginal value vs targeted chapter reads as concepts surface. **Deep-read individual chapters when their topics become operationally relevant**, not preemptively. The skim above is sufficient to locate the right chapter when needed.

### Status: cited but unread

Per the workspace's "cited but unread" lint convention: this stub is intentionally created as a reference shell. If a future ingest cites Murphy ch. 5 (Multi-agent RL), promote that chapter to deep-read status; the rest stays at skim.

## Snippets

- **Title-page metadata** (p.1): "Reinforcement Learning: An Overview. Kevin P. Murphy. December 3, 2025. arXiv:2412.05265v5 [cs.AI] 1 Dec 2025." [Source: arXiv:2412.05265v5 p.1]

- **Section 3.5 — Gradient-free policy optimization** is the textbook foundation for GRPO-family methods. Direct cross-link to `@sources/training-free-grpo-iclr-2026.md` and Conductor's Path B token-prior approach. [Source: arXiv:2412.05265v5 §3.5]

- **Section 5 — Multi-agent RL** covers games + solution concepts; foundational reference for MAPPO + atlas-gic-style multi-agent debate. [Source: arXiv:2412.05265v5 §5]

## Dead Ends

*(none yet — reference material; deep-read deferred until specific chapter relevance surfaces.)*
