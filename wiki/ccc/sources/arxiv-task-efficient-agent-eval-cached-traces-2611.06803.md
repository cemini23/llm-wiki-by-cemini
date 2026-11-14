---
title: "Task-efficient agent evaluation using cached traces (trubric)"
type: source
related:
  - concepts/task-efficient-eval-cached-traces.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/baseline-and-metric-calibration.md
  - concepts/headless-claude-code-controlled-eval-lane.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Task-Efficient Agent Evaluation Using Cached Traces |
| Author | Ben Johnson (Jataware), Hayden Helm (Helivan) |
| Type | arXiv paper (cs.AI), 2611.06803 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.06803-task-efficient-agent-evaluation-using-cached-tra.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 22 |
| Read status | read |

## Narrative

A full agent benchmark run is expensive. The paper states that one full evaluation can exceed $2,000. Efficient benchmarking tries to estimate a full score from a few executed tasks. Prior methods use only the binary correctness of reference systems.

An agent run also leaves a **trace**: file diffs, tool calls, plans, and errors. The authors ask how to turn a trace into a useful vector. Raw trace embeddings mostly encode **system identity**, **model family**, and **harness** instead of task behaviour.

Their answer is **trubric** (trace rubric). An LLM writes a task-specific structured summary of each trace. A standard text encoder embeds the summary. The authors test seven encoders and report that trubric keeps task and correctness signal, and suppresses system, model-family, and harness signal.

They then build low-dimensional representations of all reference systems. A regressor predicts the score of a new system from its geometric position among the references.

Results on SWE-bench Verified (n=107) and Terminal-Bench 2.0 (n=65):

- With one random task, the hybrid of item-response theory (IRT) and trubric cuts mean absolute error from 0.13 to 0.08 on SWE-bench Verified (Wilcoxon p < 10^-4).
- On Terminal-Bench 2.0 the same hybrid cuts error from 0.14 to 0.12 (p < 10^-3).
- The hybrid beats every baseline at every task budget tested.

The practical lesson for Cemini is narrow and useful. **A trace is a measurement of behaviour, not only a log.** A rubric summary of a trajectory carries more signal per dollar than one more full benchmark run. The harness signal is explicitly treated as noise here, which is the opposite goal of harness evaluation — the two uses must not be confused.

## Snippets

> "These representations preserve correctness- and task-related signal while minimizing the presence of system identity-, model family-, and harness-related signals that dominate raw trace embeddings." [Source: arxiv-2611.06803-task-efficient-agent-evaluation-using-cached-tra.pdf p.1]

> "Full evaluation on a benchmark can regularly exceed $2,000." [Source: arxiv-2611.06803-task-efficient-agent-evaluation-using-cached-tra.pdf p.1]
