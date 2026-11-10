---
title: "BOXBOX — recursive harness self-improvement with hot reload"
type: source
related:
  - concepts/recursive-harness-hot-reload.md
  - concepts/meta-harness-continual-improvement.md
  - concepts/benchmark-maintenance-debt.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BOXBOX: Recursive Harness Self-Improvement for Long-Running Performance Optimization |
| Author | Yuhao Tan, Hanyun Jiang, Fangkai Yang, and others (Nanjing University, Zhejiang University, Microsoft) |
| Type | arXiv paper (cs.SE), 2611.09218 |
| Location | `research to be indexed/ccc/arxiv-2611.09218-boxbox-recursive-harness-self-improvement-for-lo.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 47 |
| Read status | read |

## Narrative

Most harness-optimisation work is offline. It learns from reference answers or task feedback, then ships one harness for held-out tasks. The paper argues that this does not fit open-ended, long-running tasks. On their new benchmark, offline **Harness Evolution** performs worse than a frozen harness.

The authors release **PERFRACE**, a benchmark for long-running performance optimisation of real software projects. Tasks come from public projects and need no reference optimisation.

**BOXBOX** changes who controls the loop. The task-solving agent decides when to spend budget on reviving its own harness. When the agent asks, a kernel pauses execution and starts a review session. The reviewer reads the trajectory, diagnoses the difficulty, and revises the full executable harness. After validation, the kernel resumes the task with **preserved execution context** under the new harness. The new harness governs later execution and later reviews, so improvement is recursive.

Results on 50 PERFRACE test tasks with three runs per method:

| Method | Speedup@4h | Model cost |
|--------|-----------|-----------|
| Frozen harness | 1.44x | $23.21 |
| Offline Harness Evolution | 1.28x | $24.56 |
| Harness Scaling (external control) | 1.54x | $12.98 |
| BOXBOX | 1.70x | $16.41 |

BOXBOX beats the strongest baseline on speed and uses less model cost than the frozen and offline arms.

The notable design decision is the split. The agent chooses **when** to revise. A kernel that the agent does not control performs the **hot reload** and protects context. That avoids the failure of agent-authored self-modification with no checkpoint.

## Snippets

> "The kernel pauses task execution and launches an agent review session to diagnose difficulties from the trajectory and revise the harness." [Source: arxiv-2611.09218-boxbox-recursive-harness-self-improvement-for-lo.pdf p.2]

> "BOXBOX achieves a Speedup@4h of 1.70x, compared with 1.44x for Frozen Harness, 1.28x for Harness Evolution, and 1.54x for Harness Scaling." [Source: arxiv-2611.09218-boxbox-recursive-harness-self-improvement-for-lo.pdf p.1]
