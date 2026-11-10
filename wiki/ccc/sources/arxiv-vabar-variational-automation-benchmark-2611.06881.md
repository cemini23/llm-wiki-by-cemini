---
title: "VABAR — a Variational Automation benchmark for agentic robotics"
type: source
related:
  - concepts/agentic-robotics-harness.md
  - concepts/benchmark-maintenance-debt.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | VABAR: A Variational Automation Benchmark for Agentic Robotics |
| Author | Shuangyu Xie, Kaiyuan Chen, Uksang Yoo, and others (UC Berkeley, NVIDIA, Siemens) |
| Type | arXiv paper (cs.RO), 2611.06881 |
| Location | `research to be indexed/ccc/arxiv-2611.06881-vabar-a-variational-automation-benchmark-for-age.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 9 |
| Read status | read |

## Narrative

The paper defines **Variational Automation (VA)**: a robot repeats one operational objective across a controlled distribution of object shapes, poses, layouts, and execution conditions. VA sits between fixed automation and open-ended generalist robotics.

The authors argue that current manipulation benchmarks are mostly household pick-and-place tasks, and many are saturated. They propose seven design criteria for an agentic-robotics benchmark:

1. Relevance to agentic robotics (the agent writes, tests, and revises robot programs).
2. Application relevance.
3. Accessibility and clarity.
4. Controlled diversity with explicit variation axes.
5. Repeatability through seeds and fixed success criteria.
6. Computational efficiency.
7. Resistance to saturation.

VABAR instantiates these in six task classes: tool sorting, tool hanging, gear meshing, syringe packing, cable insertion, and cable routing. It supports single-arm Franka and bimanual YAM robots. It ships 33 generalisable skills, human-authored reference solutions, and runs on the Newton physics engine and Isaac Lab Arena.

Baselines use Graph-as-Policy (GaP), an open agentic manipulation harness.

The criteria are the reusable part. Cemini has no robots, but the same checklist applies to any internal eval. **Controlled diversity plus repeatability plus saturation resistance** is a fair description of what `run_*_backtest.sh` and the wiki sweeps try to do.

## Snippets

> "We call this Variational Automation (VA) to differentiate these settings from fixed automation." [Source: arxiv-2611.06881-vabar-a-variational-automation-benchmark-for-age.pdf p.1]

> "VABAR evaluates externally measurable task objectives and structured variation distributions rather than prescribing a particular agent architecture." [Source: arxiv-2611.06881-vabar-a-variational-automation-benchmark-for-age.pdf p.3]
