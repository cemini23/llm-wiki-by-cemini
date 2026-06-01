---
title: Harness updating vs harness benefit — non-monotonic agent gains
type: concept
tags: [concept, agent-harness, llm-agents, k93]
keywords: [harness-updating, harness-benefit, self-evolving-agents, evolver-model, mid-tier-agents]
related:
  - sources/arxiv-harness-updating-not-benefit-2605.30621.md
  - sources/arxiv-continual-harness-self-improving-agents-2605.09998.md
  - entities/tools/anthropic-harness-design.md
  - concepts/cemini-wiki-ingest-workflow.md
  - entities/tools/revfactory-harness.md
  - sources/trading-posts-compilation-31-2026-06-01.md
maturity: validated
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @sources/arxiv-harness-updating-not-benefit-2605.30621.md
- @sources/arxiv-continual-harness-self-improving-agents-2605.09998.md
- @entities/tools/anthropic-harness-design.md
- @concepts/cemini-wiki-ingest-workflow.md

## Raw Concept

arXiv:2605.30621 (2026-06-01 ingest).

## Narrative

When agents evolve **prompts/skills/tools/memories** from traces, two skills must be measured separately:

| Capability | Meaning | Empirical shape |
|------------|---------|-----------------|
| Harness-updating | Producing useful persistent harness deltas | ~flat across base LM tiers |
| Harness-benefit | Using updated harness during tasks | Non-monotonic — peaks mid-tier |

**Design rules for Cemini / CCC:**

1. Do not assume a frontier model is required for overnight harness mutation (evolver can be smaller).
2. Do assume the **executor** must reliably **activate** and **follow** harness artifacts — weak-tier failure is usage, not edit quality.
3. Prefer mid-tier executors + strong harness discipline over pairing strong evolver + strong executor by default.

Relates to @entities/tools/anthropic-harness-design.md Planner/Generator/Evaluator split — evaluation should score **benefit** on live tasks, not edit eloquence alone.

## Snippets

> "Investing capability budget in the task-solving agent rather than the evolver." [Source: 2605.30621v1.pdf — paraphrase of conclusion, @sources/arxiv-harness-updating-not-benefit-2605.30621.md]
