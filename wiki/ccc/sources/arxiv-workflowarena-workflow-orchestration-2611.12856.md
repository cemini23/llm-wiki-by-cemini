---
title: "WorkflowArena — workflow orchestration as a measured capability"
type: source
related:
  - concepts/workflow-orchestration-as-capability.md
  - concepts/subagent-orchestration.md
  - concepts/benchmark-maintenance-debt.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems |
| Author | Zheng Jiang, Fang Niu, Bo Peng, and others (Navers Lab, Einsia.AI, Tsinghua University) |
| Type | arXiv paper (cs.CL), 2611.12856 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.12856-workflowarena-benchmarking-executable-workflow-o.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 22 |
| Read status | read |

## Narrative

Modern harnesses let the model write the workflow that coordinates its workers. The structure of a multi-agent system is therefore a model output, not a developer decision. The authors call this capability **workflow orchestration** and measure it directly.

**WorkflowArena** has 145 long-horizon tasks across 8 domains and 17 task forms: software engineering, formal mathematics, legal analysis, 3D production, and others. Each task gives an initial workspace and a deliverable with interdependent parts. A hidden verifier scores the deliverable, including checks that individually correct but unreconciled parts cannot pass.

The protocol has two properties that make it more than another task set:

- Delegation is optional. The agent decides whether to delegate at all.
- Time spent organising the work is charged against the same budget as the work.

Every delegation passes a recorded interface, so the workflow can be read next to the outcome.

Results across 25 configurations of nine models in Claude Code or Codex:

- The strongest configuration, Claude Opus 5.5 with Claude Code at max effort, resolved 36.95% of tasks on average.
- No configuration was best in every domain.
- Delegation styles differ. At high effort, Claude models in Claude Code launch fewer workflows with larger worker groups. GPT models in Codex delegate more often in smaller units.

A fixed-executor transfer test separates orchestration from raw capability. A source model writes the workflow and does not edit the workspace; every worker is a weaker model. On a hard subset, workflows authored by Opus 5.5 raised all four execution models by 6.41 points on average in static mode. Workflows from Astra helped far less and lowered two of them.

So orchestration quality is a measurable source of performance, distinct from solo task ability. For Cemini that supports the existing rule: the architect session should write the plan, and the implementer lane should do the typing.

## Snippets

> "workflows authored by Claude Opus 5.5 substantially improve weaker executors, indicating that workflow organization is itself a measurable determinant of task performance." [Source: arxiv-2611.12856-workflowarena-benchmarking-executable-workflow-o.pdf p.1]

> "at high effort, Claude models in Claude Code invoke workflows less frequently but with larger worker groups, whereas GPT models in Codex delegate more frequently in smaller units." [Source: arxiv-2611.12856-workflowarena-benchmarking-executable-workflow-o.pdf p.1]
