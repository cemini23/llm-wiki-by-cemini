---
title: "Benchmark maintenance debt — the score drifts away from the capability"
type: concept
related:
  - sources/arxiv-benchmarks-as-software-terminal-bench-2611.08417.md
  - sources/arxiv-task-efficient-agent-eval-cached-traces-2611.06803.md
  - sources/arxiv-workflowarena-workflow-orchestration-2611.12856.md
  - sources/arxiv-vabar-variational-automation-benchmark-2611.06881.md
  - concepts/harness-as-eval-artifact.md
  - concepts/baseline-and-metric-calibration.md
  - concepts/terminal-state-eval-discovery-reliability-gap.md
  - concepts/expert-data-rl-environments.md
  - concepts/agentic-robotics-harness.md
  - concepts/workflow-orchestration-as-capability.md
  - concepts/frontier-model-release-cadence.md
  - sources/arxiv-boxbox-recursive-harness-2611.09218.md
  - concepts/task-efficient-eval-cached-traces.md
  - concepts/eval-integrity-minimum-standards.md
updated: 2026-11-14
---

## Raw Concept

Question this page answers: what makes an agent benchmark stop measuring what it claims, and what does a repair cost?

Synthesised from Terminal-Bench 2.1, trubric, WorkflowArena, and VABAR.

## Narrative

**Benchmark maintenance debt** is the backlog of task defects that decouples a score from the capability it is meant to measure. Three failure classes recur:

| Class | What breaks |
|-------|-------------|
| Instruction-verification mismatch | A valid solution fails, or a shortcut passes the tests |
| Environment issue | Isolation fails, packages change, or external state moves |
| Task drift | A dependency or website changes after release |

Terminal-Bench 2.0 had passed human review, LM-assisted audit, and exploit testing before release. Within months it had more than 50 open defect reports. An audit found issues in roughly 30% of tasks. [TENTATIVE: single source]

### What the repair changed

- Accuracy rose more than 10 percentage points.
- Leaderboard positions moved by up to three ranks.
- Overall ranking stayed highly correlated (Spearman rho = 0.958).

Read that carefully. The **ordering** was robust; the **numbers** were not. A claim of the form "system A scores 71%" is fragile. A claim of the form "A ranks above B" survived.

### Resource budgets are part of the specification

Fixed wall-clock and token limits changed conclusions. Extending a time limit closed a 20 point harness gap on one model and cut a 30 point gap to 5 points. More than half of failed trials were timeouts, and up to about 68% for some harnesses.

So a harness gap measured under one budget is not a harness property. The budget belongs next to the score, in the same tuple.

### Countermeasures

- **Continuous validation** — collect community reports, traces, and oracle checks, then gate repairs on human review.
- **Task-efficient estimation** — use cached traces to cut the cost of re-running the whole set; see `@concepts/task-efficient-eval-cached-traces.md`.
- **Design against saturation** — VABAR lists saturation resistance as a first-class criterion.
- **Charge orchestration cost to the task** — WorkflowArena makes delegation draw from the same budget.

### Cemini application

`run_*_backtest.sh` reports are benchmark artifacts. Record the resource budget (time window, token cap, model id, effort) with every result. When a sweep cites a harness gap, state the budget that produced it.

## Snippets

> "Benchmark maintenance is therefore not only about repairing task artifacts: resource budgets are part of the measurement specification and must be validated alongside the tasks themselves." [Source: arxiv-2611.08417-benchmarks-as-software-terminal-bench-and-the-ca.pdf p.1]
