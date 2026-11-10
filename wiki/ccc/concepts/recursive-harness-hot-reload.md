---
title: "Recursive harness self-improvement with kernel-managed hot reload"
type: concept
related:
  - sources/arxiv-boxbox-recursive-harness-2611.09218.md
  - concepts/meta-harness-continual-improvement.md
  - concepts/harness-as-eval-artifact.md
  - concepts/context-engineering.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: can an agent improve its own harness during a long run without losing its place?

Synthesised from `@sources/arxiv-boxbox-recursive-harness-2611.09218.md`.

## Narrative

Offline harness optimisation learns from reference answers or task feedback, then ships one harness for held-out tasks. BOXBOX tests that approach on open-ended, long-running work and finds it **worse than a frozen harness** (1.28x against 1.44x speedup at four hours).

The design that wins splits authority:

- **The task-solving agent decides when** to spend budget on a harness revision. It is the only party that knows the run is stuck.
- **A kernel the agent does not control performs the swap.** It pauses execution, validates the new harness, then resumes with the execution context preserved.

Because the revised harness also governs later reviews, improvement is recursive.

| Method | Speedup@4h | Cost |
|--------|-----------|------|
| Frozen | 1.44x | $23.21 |
| Offline evolution | 1.28x | $24.56 |
| External Harness Scaling | 1.54x | $12.98 |
| BOXBOX | 1.70x | $16.41 |

[TENTATIVE: single source, self-reported; 50 tasks, three runs each]

### Why the split matters

An agent that can rewrite its own harness with no external checkpoint is an unguarded loop. BOXBOX keeps agent judgement and removes agent control of the switch. That is the same shape as the wiki rule that the implementer does not merge its own work.

### Cemini fit

The workspace already separates architect and implementer lanes. The closest analogue is a long `/route` run that may request a harness change between phases. The BOXBOX lesson is that the **request** should come from the working agent and the **swap** should come from a supervisor that preserves state. [OPEN QUESTION 2026-11-10] No such supervisor exists in the current `/route` implementation.

## Snippets

> "Existing offline methods use reference answers to optimize harnesses for reuse on held-out tasks. However, many real-world tasks are open-ended, while long runs expose new difficulties that offline-optimized harnesses may not address." [Source: arxiv-2611.09218-boxbox-recursive-harness-self-improvement-for-lo.pdf p.1]

> "When requested, the kernel pauses task execution and launches an agent review session... After validation, it resumes the task with preserved execution context under the revised harness." [Source: arxiv-2611.09218-boxbox-recursive-harness-self-improvement-for-lo.pdf p.2]
