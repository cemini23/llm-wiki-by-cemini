---
title: "Continual Harness — online reset-free harness self-improvement"
type: concept
tags: [concept, agent-harness, self-improvement, online-learning, embodied-agents]
keywords: [continual-harness, reset-free-adaptation, harness-refiner, process-reward-co-learning, gemini-plays-pokemon]
related:
  - sources/arxiv-continual-harness-self-improving-agents-2605.09998.md
  - sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md
  - concepts/code-as-agent-harness.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/llm-agent-systems.md
  - sources/agentic-harness-engineering.md
cross-wiki:
  - ccc-wiki/concepts/continual-harness-online-self-improvement.md
maturity: validated
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @sources/arxiv-continual-harness-self-improving-agents-2605.09998.md — primary source
- @sources/arxiv-veritas-visual-verification-2606.18247-2026-06-18.md — external verifier vs harness-edit (K123)
- @concepts/generator-verifier-inference-time-steering.md
- @concepts/code-as-agent-harness.md — static / human-curated harness design space
- @concepts/llm-agent-systems.md — parent
- @sources/agentic-harness-engineering.md — observability-driven harness evolution (complementary)

## Raw Concept

Synthesized from arXiv:2605.09998 (K72) — formalizes **online harness refinement** without episode resets, motivated by Gemini Plays Pokémon human-in-the-loop success.

## Narrative

### Problem

Prompt-optimization and many RL harness pipelines assume **reset between episodes**. Long-horizon embodied (and many production research) tasks are **single continuous trajectories** — resets destroy the realism of adaptation.

### Mechanism (three-panel mental model)

1. **Human-in-the-loop** — human refiner updates harness from trajectories (GPP).
2. **Self-improving harness** — refiner is automated; agent refines prompt, sub-agents, skills, memory from past trajectories.
3. **Model + harness co-learning** — open agent rollouts + frontier teacher process rewards → weight updates without env reset between iterations.

### Cemini mapping [TENTATIVE]

| Paper element | Cemini analogue |
|---------------|-----------------|
| Minimal env interface | Raw MCP + market APIs without hand-built strategy scaffolding |
| Harness refiner | Server-Claude / conductor reviewer loops, skill_audit feedback |
| Trajectory memory | stash episodic + wiki log + hot.md |
| Co-learning | Not deployed — would pair prod rollouts with teacher relabeling |

**Not a prod adoption** — no Pokémon stack on cemini-prod. **CCC relevance:** pairs with K72 Posts on agent memory (mem0, Hermes, Obsidian); see @ccc-wiki/concepts/claude-code-finance-research-setup.md and @ccc-wiki/concepts/continual-harness-online-self-improvement.md

## Snippets

> "Prompt-optimization methods require episode resets; Continual Harness adapts online within a single run." [Source: 2605.09998v1.pdf p.1]
