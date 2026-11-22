---
title: "Mind–Act composition — score sub-capabilities apart from the whole"
type: concept
related:
  - sources/arxiv-mind2act-world-embodied-diagnostic-benchmark-2611.26444.md
  - concepts/harness-attribution-multimodal-eval.md
  - concepts/agentic-robotics-harness.md
  - concepts/execution-contract-failure-attribution.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: when an embodied agent fails, which layer broke?

Synthesised from one source: `@sources/arxiv-mind2act-world-embodied-diagnostic-benchmark-2611.26444.md` (Mind2Act-World, 2611.26444).

## Narrative

Mind2Act-World splits a robot task into three views:

- **Mind** — memory, goal selection, planning.
- **Act** — timely, precise, stable execution.
- **Mind2Act** — the composition of the two.

The benchmark has 30 tasks, three difficulty levels, 12 capability categories and 180 simulator configurations.

The headline is the composition gap. Strong sub-scores do not compose: 52.7% on Mind and 39.0% on Act yield 12.0% on Mind2Act. The benchmark also records a **first-failure trace** per run, with a failure stage and code.

### Why it transfers

An end-to-end score hides which layer broke. Three rules follow:

1. **Score layers separately.**
2. **Score the composition too** — the whole can be far below the parts.
3. **Record the first failure,** not only the last.

Cemini agent tasks have the same structure: model capability, harness behaviour, and environment. A failed task that reports only "failed" cannot be fixed.

Caveat: robotics benchmark, one source. The design pattern transfers; the numbers do not. [TENTATIVE]

## Snippets

> "Strong Mind 52.7% + strong Act 39.0% ≠ Mind2Act 12.0%." [Source: arxiv-2611.26444-mind2act-world-a-diagnostic-benchmark-for-embodi.pdf p.1]
