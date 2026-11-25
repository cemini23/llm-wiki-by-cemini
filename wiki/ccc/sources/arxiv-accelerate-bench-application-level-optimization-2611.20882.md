---
title: "Accelerate Bench — application-level program optimization by coding agents"
type: source
related:
  - concepts/application-level-optimization-eval.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/eval-integrity-minimum-standards.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Accelerate Bench: Evaluating Agents for Application-Level Program Optimization |
| Author | Bowen Liu, Yuhan Li, Nuo Chen et al. (Tencent Hy Team, HKUST, Tsinghua, PKU) |
| Type | arXiv paper (cs.SE), 2611.20882 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.20882-accelerate-bench-evaluating-agents-for-applicati.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 49 |
| Read status | read |

## Narrative

Accelerate Bench holds 32 CPU optimisation tasks adapted from scientific applications and supercomputing competitions. Each task gives a working program plus a workload, correctness requirements, timing boundaries and permitted edits. The agent chooses where and how to optimise.

On version 1.1, 16 coding agents (model plus harness) score between 25.5% and 67.4% Score@1. Most programs are correct; speedup size separates the agents. The two leaders reach at least 2× on 22 or more of the 32 tasks. The other fourteen reach 2× on 8 to 17 tasks, and leave 125 of their 412 correct outcomes below 1.25×.

The most interesting result is a controlled replay. The same source code runs between 0.29× and 2.12× depending only on build and runtime settings. One code change is worth 1.01× or 6.4× depending on another change.

That result is a general warning about code-editing benchmarks. Correctness and a local patch do not imply end-to-end gain. Interactions between changes dominate. Cemini's own backtests have the same structure: a parameter change can look good or bad depending on the surrounding configuration.

The benchmark pairs executable workloads with agent programs and trajectories, so it scores both the gain and the process. [TENTATIVE] single source.

## Snippets

> "Identical source code runs between 0.29× and 2.12× depending only on build and runtime settings, and one code change is worth 1.01× or 6.4× depending on another." [Source: arxiv-2611.20882-accelerate-bench-evaluating-agents-for-applicati.pdf p.1]
