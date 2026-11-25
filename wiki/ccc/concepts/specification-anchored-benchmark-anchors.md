---
title: "Field criterion and two anchors — how to score a task with no answer key"
type: concept
related:
  - sources/arxiv-stembench-postdoc-level-science-2611.24321.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/eval-integrity-minimum-standards.md
  - concepts/harness-as-eval-artifact.md
  - concepts/baseline-and-metric-calibration.md
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Question this page answers: how do you score a research task when no answer key exists?

Synthesised from one source: `@sources/arxiv-stembench-postdoc-level-science-2611.24321.md` (STEMBench, 2611.24321).

## Narrative

Existing benchmarks handle open tasks by substituting an easier criterion: a reference answer, a unit-test suite, a rubric, or a competition rank. STEMBench argues none of these is how a field decides that one published method beats another.

Its design has two parts.

1. **Score by the field's own figure of merit.** Twelve problems in high-energy physics, astrophysics and neuroscience are each scored the way that community compares published methods — background rejection at fixed signal efficiency, coverage-penalised interval width, and so on.
2. **Ship two measured anchors.** A floor comes from a submission that uses no domain knowledge. A ceiling comes from an expert reference that reproduces a published method. Both come from code shipped with the benchmark.

The score is then read against the interval between the anchors. That interval states how much of the problem needs insight rather than engineering.

### Why anchors matter

A bare score hides difficulty. 40% on an easy task and 40% on a hard task look identical. With a floor and a ceiling, the reader sees position in a meaningful range. Anchors also catch drift: if the floor rises, the task got easier.

### Result worth noting

Task-level wins and domain-level leadership dissociate. A model that won five of twelve tasks led no domain mean. Aggregate rankings therefore hide domain structure.

Cemini's own comparisons should carry a floor and a ceiling. A backtest with no benchmark floor has no scale. [TENTATIVE]

## Snippets

> "Each of its twelve research problems is scored by its own field's figure of merit, and each comes with two measured anchors: a submission that uses no domain knowledge, and an expert reference reproducing a published method." [Source: arxiv-2611.24321-benchmarking-llm-abilities-on-postdoc-level-natu.pdf p.1]

> "The interval between them states how much of a problem is crossed by scientific insight rather than by engineering." [Source: arxiv-2611.24321-benchmarking-llm-abilities-on-postdoc-level-natu.pdf p.1]
