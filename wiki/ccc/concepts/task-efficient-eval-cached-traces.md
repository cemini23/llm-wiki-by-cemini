---
title: "Task-efficient agent evaluation from cached traces"
type: concept
related:
  - sources/arxiv-task-efficient-agent-eval-cached-traces-2611.06803.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/harness-as-eval-artifact.md
  - concepts/headless-claude-code-controlled-eval-lane.md
  - concepts/baseline-and-metric-calibration.md
  - sources/arxiv-benchmarks-as-software-terminal-bench-2611.08417.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: can a full agent benchmark score be estimated from a few executed tasks and the traces those runs leave behind?

Synthesised from `@sources/arxiv-task-efficient-agent-eval-cached-traces-2611.06803.md`.

## Narrative

A full agent benchmark run is expensive. The paper reports that one full evaluation can exceed $2,000. Efficient benchmarking tries to estimate a full score from a small number of executed tasks.

Two families exist. Score-based methods use item-level correctness from reference systems, usually through item-response theory (IRT). Artifact-based methods compare the artifacts systems produce. Artifact methods worked for plain language models but fail for agents when the embedding captures system, model-family, and harness identity instead of task behaviour.

**trubric** fixes the representation. An LLM writes a task-specific structured summary of each trace. A standard text encoder embeds that summary. The summary keeps task and correctness signal and suppresses identity signal.

Given embeddings for reference systems, the method builds low-dimensional system representations and predicts the target score from geometric position. Combined with IRT, it cut mean absolute error from 0.13 to 0.08 on SWE-bench Verified and from 0.14 to 0.12 on Terminal-Bench 2.0 at a budget of one random task. [TENTATIVE: single source, self-reported]

### When to use this

Use it when the question is "roughly how good is this system" and the budget is small. Do not use it when the question is "which harness is better", because the method deliberately removes harness signal. That removal is the point: the vector is a behaviour fingerprint, not a harness fingerprint.

### Cemini fit

The wiki already keeps trajectories in run folders and briefs. A rubric summary over a `_route_runs` trajectory is cheap. It would let `compare_strategies`-style questions be answered from a handful of new runs plus the existing archive. [OPEN QUESTION 2026-11-10] No implementation exists, and the encoder cost is untested here.

## Snippets

> "reduces mean absolute error from 0.13 to 0.08 (Wilcoxon p < 10^-4) and from 0.14 to 0.12 (Wilcoxon p < 10^-3)" [Source: arxiv-2611.06803-task-efficient-agent-evaluation-using-cached-tra.pdf p.1]
