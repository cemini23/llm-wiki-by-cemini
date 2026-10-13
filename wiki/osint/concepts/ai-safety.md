---
title: AI safety — alignment, misalignment, and safety post-training
type: concept
tags: [concept, ai-safety, alignment, misalignment, safety-post-training]
keywords: [ai safety, alignment, misalignment, emergent misalignment, conditional misalignment, RLHF, safety post-training]
related:
  - concepts/emergent-misalignment.md
  - sources/qwen-scope.md
  - concepts/mechanistic-interpretability.md
  - sources/arxiv-2610.12758-distressbench-2026-10-13.md
  - concepts/k290-arxiv-wave.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@concepts/emergent-misalignment.md` — specific failure mode covered under the AI-safety umbrella
- `@sources/qwen-scope.md` — Qwen SAE-Scope work touching safety post-training + alignment-relevant steering
- @sources/arxiv-2610.12758-distressbench-2026-10-13.md
- @concepts/k290-arxiv-wave.md

## Raw Concept

What prompted this page: emergent-misalignment concept page flagged a gap for an upstream AI-safety hub. This is the parent topic — alignment objectives, misalignment failure modes, and safety post-training methods.

## Narrative

AI safety, in the Cemini-relevant slice: making LLMs reliable when used inside agentic financial-research pipelines. Two angles matter here:

1. **Alignment-with-intent** — does the model do what the operator asked, not what it inferred from training-data drift? Conditional and emergent misalignment (see `@concepts/emergent-misalignment.md`) are the headline failure modes.
2. **Safety post-training** — RLHF, constitutional AI, and SAE-based steering (cf. `@sources/qwen-scope.md`) are the toolkit operators have to push a model away from undesired behaviors after pretraining.

For Cemini specifically: a misaligned agent in a trading loop is a money-leaking failure. Safety here is not abstract — it's pre-commit gates, audit trails, and bounded-budget loops. See `@concepts/ralph-autonomous-agent-pattern.md` for the budget-bounded pattern and `@entities/tools/anthropic-harness-design.md` for the Planner/Generator/Evaluator pattern that operationalizes oversight.

This is a stub. Real content accumulates as misalignment incidents get logged and the safety toolchain matures.
