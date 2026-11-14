---
title: "Benchmarks as software — Terminal-Bench 2.1 and benchmark maintenance debt"
type: source
related:
  - concepts/benchmark-maintenance-debt.md
  - concepts/task-efficient-eval-cached-traces.md
  - concepts/harness-as-eval-artifact.md
  - concepts/terminal-state-eval-discovery-reliability-gap.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks |
| Author | E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman, Christopher Re (Stanford, Cornell) |
| Type | arXiv paper (cs.AI), 2611.08417 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.08417-benchmarks-as-software-terminal-bench-and-the-ca.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 24 |
| Read status | read |

## Narrative

The paper defines **benchmark maintenance debt**: the growing backlog of task defects that makes a score stop measuring the capability it claims to measure.

Three failure classes appear along the task lifecycle:

- **Instruction-verification mismatch** — the task text and the tests disagree, so a valid solution fails, or a shortcut passes.
- **Environment issue** — resource isolation, missing packages, or changed external state.
- **Task drift** — an external dependency changes after release.

Terminal-Bench 2.0 had passed human review, LM-assisted auditing, and exploit testing before release. Within months its issue trackers held more than 50 open defect reports. The audit here found issues in roughly 30% of the benchmark and released repairs as **Terminal-Bench 2.1**.

Effect of the repairs:

- Accuracy rose by more than 10 percentage points.
- Leaderboard positions moved by up to three ranks.
- Overall ranking stayed highly correlated (Spearman rho = 0.958).

The second result is the operational one. **Resource budgets are part of the measurement.** Fixed wall-clock and output-token limits changed conclusions. Extending the time limit closed a 20 point harness gap on GPT 5.4 and shrank a 30 point gap on GPT 5.4 mini to 5 points. More than 50% of failed trials were timeouts, and up to about 68% for some harnesses.

The workflow also matters: evidence collection, agent-assisted audit, oracle rebuild, human-gated repair, then release. Repairs that only patched a symptom were rejected in favour of repairs that fixed the validity failure.

For Cemini this is a direct warning about `run_*_backtest.sh` and sweep comparisons. A harness gap measured under one time budget may be a budget artifact. The budget belongs next to the score.

## Snippets

> "We call the resulting accumulation of defects benchmark maintenance debt: a growing gap between benchmark scores and the capabilities they are intended to measure." [Source: arxiv-2611.08417-benchmarks-as-software-terminal-bench-and-the-ca.pdf p.1]

> "Benchmark maintenance is therefore not only about repairing task artifacts: resource budgets are part of the measurement specification and must be validated alongside the tasks themselves." [Source: arxiv-2611.08417-benchmarks-as-software-terminal-bench-and-the-ca.pdf p.1]
