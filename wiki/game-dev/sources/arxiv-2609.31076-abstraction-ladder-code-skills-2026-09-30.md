---
title: Abstraction ladder — code-based skills for language agents (2026-09-30)
type: source
tags: [source, arxiv, harness, agents, skills]
keywords: [codehack, code-skills, primitives, nethack, abstraction-ladder]
related:
  - concepts/agent-harness-castle-project.md
  - concepts/ai-assisted-game-dev-workflows.md
  - sources/arxiv-2609.34214-glyphbench-rl-playground-2026-09-30.md
  - sources/inbox-arxiv-reject-batch-2026-09-30.md
  - entities/tools/codehack.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2609.31076
maturity: validated
created: 2026-09-30
updated: 2026-09-30
---

## Raw Concept

**arXiv:2609.31076** — "Up and Down the Abstraction Ladder: Code-Based Skills for Language Agents". The paper studies how code-based action abstraction changes language-agent performance, inference cost, and learning.

Language agents struggle with long sequences of low-level actions. [CONFIRMED] Code-based abstractions let an agent invoke reusable skills instead of choosing every primitive action. [CONFIRMED] The code handles recurring local decisions; the LLM decides which skills to use and how to combine them. [CONFIRMED] Abstractions leak, so a way back down to primitives matters. [CONFIRMED]

The study environment is NetHack, with CodeHack, the authors' library of code-based skills carrying natural-language descriptions. [CONFIRMED] The authors compare primitives-only, skills-only, and skills-plus-primitives agents in zero-shot prompting, supervised fine-tuning, and RL. [CONFIRMED]

Headline results: skills nearly triple game progression versus primitives and cut inference cost per episode by 86%. [CONFIRMED] Skills-plus-primitives keeps most of the benefit and preserves a path back to low-level actions. [CONFIRMED] In RL, skill-based agents learn faster, with a 7.2x larger average gain in dungeon level over the same training budget. [CONFIRMED] The authors release CodeHack plus training and evaluation code. [CONFIRMED] Project page: bartekcupial.github.io/abstraction-ladder/.

## Narrative

### castle-sim harness relevance [CONFIRMED]

The argument maps to the agent harness in @concepts/agent-harness-castle-project.md. Give agents named high-level operations (build wall segment, place granary, run smoke scene) instead of raw editor calls. Keep primitive fallback when a skill does not fit. The same case applies to the castle-sim Codex swarm and to Godot editor automation. [CONFIRMED]

The 86% lower inference cost is the concrete reason to prefer skills in a token-budgeted hobby workflow. [CONFIRMED]

### Caveat [TENTATIVE]

The evidence is from NetHack with a supplied skill library. Transfer to a Godot or castle-sim tool surface is unproven.

## Dead Ends

- Skills-only agents with no primitive fallback.
- Expecting a skill library to fix a badly specified task.
