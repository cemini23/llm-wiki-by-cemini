---
title: Harbor — task format and rollout runner for coding-agent benchmarks
type: entity
related:
  - sources/arxiv-controlharbor-control-design-coding-agents-2611.16867.md
  - sources/arxiv-metal-sandbox-gpu-coding-agents-apple-silicon-2611.17294.md
  - sources/newsletter-rss-latent-space-2026-11-12-ainews-d-day-decision-models-day.md
  - concepts/generation-verification-gap-agent-artifacts.md
  - concepts/harness-as-eval-artifact.md
  - entities/tools/metal-sandbox.md
updated: 2026-11-14
---

## Raw Concept

What prompted this page: three sources in the 2026-11-14 batch use Harbor as the common task container and rollout runner. Before this page the wiki had no page for it, only mentions inside benchmark papers.

## Narrative

Harbor is the packaging and orchestration layer that runs an agent against a benchmark task. The sources show three uses.

| Use | Reported detail |
|-----|-----------------|
| Task packaging | ControlHarbor packs 44 control-design tasks in the Harbor format, "so that any agent harness can be run against them" |
| Session launch | ControlHarbor sessions run in one container, with one instruction, one hour, one graded file, launched by Harbor |
| Rollout orchestration | Metal Sandbox integrates with Harbor for task execution, automatic verification, and rollout collection; Harbor and the cluster controller share one node |
| Teaching | Stanford CS329Z assignment 2 has students write Terminal-Bench-style tasks with Harbor |

The common shape: a task is a container plus a verifier plus a budget. The harness calls the model in a loop, records actions, and cannot see the test. ControlHarbor states this directly: the harness is "the program that calls the model in a loop, gives it tools and records its actions."

Two consequences follow for Cemini.

1. **The task format is portable across harnesses.** The same task can grade Claude Code, Codex, and a local harness. A comparison between lanes can hold the task fixed and vary only the harness.
2. **Infrastructure is separable from the task.** Metal Sandbox adds command scheduling and migration underneath Harbor, without changing the task definition. That is the correct boundary for an eval runner.

Open facts to confirm before any adoption:

- License and repository for Harbor itself. [NEEDS VERIFICATION 2026-11-14]
- Whether the Metal Sandbox fork differs from upstream Harbor. The paper links `github.com/WangHaoZhe/harbor`. [NEEDS VERIFICATION 2026-11-14]

This page records the pattern. It is not a Phase-0 audit.

## Snippets

> "The tasks are packaged in the Harbor format, so that any agent harness can be run against them" [Source: arxiv-2611.16867-controlharbor-a-benchmark-for-control-design-by.pdf p.1]

> "Integration with Harbor supports task execution, automatic verification, and rollout collection through a common workflow." [Source: arxiv-2611.17294-metal-sandbox-isolated-execution-and-command-sch.pdf p.1]
