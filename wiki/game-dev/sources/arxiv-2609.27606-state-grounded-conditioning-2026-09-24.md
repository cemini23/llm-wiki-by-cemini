---
title: State-Grounded Conditioning — user-facing LLM agents (2026-09-24)
type: source
tags: [source, arxiv, npc, guardrails, harness, llm]
keywords: [sgc, direction-drift, rule-kernels, perception-grounding-interaction]
related:
  - concepts/agentic-npc-design-guardrails.md
  - sources/arxiv-2609.18935-long-lived-characters-local-inference-2026-09-19.md
  - concepts/agent-harness-castle-project.md
  - sources/inbox-arxiv-reject-batch-2026-09-24.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.27606
maturity: validated
created: 2026-09-24
updated: 2026-09-24
---

## Raw Concept

**arXiv:2609.27606** — **State-Grounded Conditioning (SGC)** for user-facing LLM agents that must follow **live game/session state**. Targets **direction drift**: responses that complete the task but pick the wrong action for current state. Uses rule kernels + Perception / Grounding / Interaction wrappers over structured state slices.

## Narrative

### castle-sim relevance [CONFIRMED]

Pairs with @sources/arxiv-2609.18935-long-lived-characters-local-inference-2026-09-19.md (memory KV) and guardrails **hard walls**:

- Godot holds authoritative granary/crime/honour state
- LLM proposes player-facing direction (advisor, lord message)
- SGC-style wrappers block drift before state mutation

### Phase-1

**policy_wired** in @concepts/agentic-npc-design-guardrails.md — “direction drift” term + rule-kernel pattern (Tier 3+).

## Dead Ends

- Letting LLM agents write economy flags directly without grounding wrapper
