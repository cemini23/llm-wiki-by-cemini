---
title: "Application-level optimisation eval — a correct patch is not a speedup"
type: concept
related:
  - sources/arxiv-accelerate-bench-application-level-optimization-2611.20882.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/eval-integrity-minimum-standards.md
  - concepts/harness-as-eval-artifact.md
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Question this page answers: how do you score an agent that must make a whole program faster, not fix one bug?

Synthesised from one source: `@sources/arxiv-accelerate-bench-application-level-optimization-2611.20882.md` (Accelerate Bench, 2611.20882).

## Narrative

Accelerate Bench holds 32 CPU optimisation tasks from scientific applications and supercomputing competitions. Each task gives a working program, a workload, correctness requirements, timing boundaries and permitted edits. The agent chooses where to optimise.

On version 1.1, 16 agents score 25.5%–67.4% Score@1. Most programs are correct; speedup size separates them. The two leaders reach at least 2× on 22 or more of the 32 tasks. The other fourteen reach 2× on 8 to 17, and leave 125 of 412 correct outcomes below 1.25×.

### The controlled replay

The most useful result is a stress test of measurement. Identical source code runs between **0.29× and 2.12×** depending only on build and runtime settings. One code change is worth 1.01× or 6.4× depending on another change.

So the environment and the configuration set the outcome as much as the patch. A local change that looks fast can be invisible or harmful end to end.

### Operating rules

1. **Score end-to-end, under a stated configuration.**
2. **Report the configuration with the number.**
3. **Test interactions.** One change at a time can mislead.

This is the same warning as `@concepts/benchmark-maintenance-debt.md`, applied to performance instead of accuracy: the measurement setup is part of the result. Cemini backtests have identical exposure — a parameter change is scored against one data and execution configuration. [TENTATIVE]

## Snippets

> "Identical source code runs between 0.29× and 2.12× depending only on build and runtime settings, and one code change is worth 1.01× or 6.4× depending on another." [Source: arxiv-2611.20882-accelerate-bench-evaluating-agents-for-applicati.pdf p.1]
