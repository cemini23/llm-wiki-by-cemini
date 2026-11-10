---
title: "Workflow orchestration is a measurable capability, separate from solo task skill"
type: concept
related:
  - sources/arxiv-workflowarena-workflow-orchestration-2611.12856.md
  - concepts/subagent-orchestration.md
  - concepts/perspectivegap-orchestration-prompting.md
  - concepts/benchmark-maintenance-debt.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: when the model writes its own multi-agent workflow, how good are those workflows, and can that be measured apart from model capability?

Synthesised from `@sources/arxiv-workflowarena-workflow-orchestration-2611.12856.md`.

## Narrative

Modern harnesses let the model instantiate workers and author the executable workflow that coordinates them. The system structure therefore becomes a model output. The authors call this **workflow orchestration** and build a benchmark for it.

**WorkflowArena**: 145 long-horizon tasks, 8 domains, 17 task forms. Each task has a workspace and a deliverable with interdependent parts, scored by a hidden verifier. Two protocol choices make it distinct:

- Delegation is optional. The agent decides whether to delegate at all.
- Organisation time is charged against the same budget as the work.

### Results

Twenty-five configurations of nine models in Claude Code or Codex:

- The best configuration resolved 36.95% of tasks on average.
- No configuration won every domain.
- Delegation style differs by family. At high effort, Claude models in Claude Code launch **fewer workflows with more workers**. GPT models in Codex delegate **more often in smaller units**.

### The fixed-executor test

The important experiment holds the worker fixed. A source model writes and revises the workflow without editing the workspace. Every worker is a weaker model.

On a hard subset, workflows from Opus 5.5 raised all four execution models by 6.41 points on average in static mode. Workflows from a stronger model, Astra, helped far less and lowered two of them.

That isolates orchestration quality from solo capability. A workflow is not good because its author is strong; it is good when it decomposes and integrates well.

### Cemini application

This is direct evidence for the workspace's architect/implementer split:

- The architect session writes the plan and the spec. It does not type the code.
- The implementer lane executes. Its model may be weaker.
- Record the workflow next to the result. A good outcome from a weak executor says something about the plan.

It also predicts a specific failure to watch: a delegation that looks efficient — many small parallel calls — may be worse than fewer, larger calls with an integration step.

## Snippets

> "workflows authored by Claude Opus 5.5 substantially improve weaker executors, indicating that workflow organization is itself a measurable determinant of task performance." [Source: arxiv-2611.12856-workflowarena-benchmarking-executable-workflow-o.pdf p.1]

> "The strongest configuration, Claude Opus 5.5 with Claude Code at max effort, resolves only 36.95% of tasks on average across domains, and no configuration performs best in every domain." [Source: arxiv-2611.12856-workflowarena-benchmarking-executable-workflow-o.pdf p.3]
