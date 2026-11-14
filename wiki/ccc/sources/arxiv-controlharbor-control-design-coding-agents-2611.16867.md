---
title: "ControlHarbor — 44 control-design tasks for coding agents, graded like control engineers"
type: source
related:
  - concepts/generation-verification-gap-agent-artifacts.md
  - entities/tools/harbor.md
  - concepts/harness-as-eval-artifact.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ControlHarbor: A Benchmark for Control Design by Coding Agents |
| Author | Jieqiang Wei (EQT), Fahad Ali (Redpine), Jonny Reichwald (EQT), Silun Zhang (KTH) |
| Type | arXiv preprint (math.DS), 2611.16867v1; dated 2026-11-12 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.16867-controlharbor-a-benchmark-for-control-design-by.pdf` |
| Retrieved | 2026-11-14 |
| Pages | 21 |
| Read status | read |

## Narrative

ControlHarbor asks whether a coding agent can design a controller. The task is a **single Python file** that maps measurements to actions. The file is the whole artifact. It cannot hold trained weights, call outside services, or use gradient-based learning.

The grader treats the file as a control engineer would. Each plant has an ordered ladder of requirement rungs, for example alive, forward, brisk, fast. A chance constraint must hold on each member of a perturbation suite at confidence 1 − δ. Some tasks also demand a structural certificate and at least 90% of a reference RL policy's return.

Scope: 44 tasks over 13 plants. Plants include network consensus, vehicle platooning, and the MuJoCo hopper, walker, and humanoid. Tasks use the **Harbor** format, so any harness can run them. The same environments also grade RL.

Protocol: three frontier models run as coding agents through the Claude Code harness at highest effort. Opus 5.5 and Fable 5.1 run all 44 tasks; Sonnet 5.5 runs the 22 MuJoCo tasks. Each session gets one hour, two cores, and 2 GB, with no network. Three sessions per task and model give 330 sessions.

Findings:

- Designed controllers reach the RL return on **every** parity task, but only in a minority of sessions, one to three of nine per task.
- Controllers certified for return alone usually fail under perturbation.
- On the humanoid, a structured design meets the robust requirement at RL return; domain-randomised RL does not.
- Under a 75 N push, domain-randomised RL succeeds and no designed controller does.
- Sonnet uses almost the full hour at the median (52 minutes). Opus and Fable use about half.

The statistical detail matters for any eval Cemini runs. With 40 held-out seeds, the one-sided Clopper-Pearson bound gives a 0.072 failure probability at δ = 0.05. With the five visible seeds the agent can test, the same bound gives 0.45. A visible-seed pass is weak evidence.

## Snippets

> "a controller designed for speed alone falls under those perturbations" [Source: arxiv-2611.16867-controlharbor-a-benchmark-for-control-design-by.pdf p.7]

> "the one-sided Clopper–Pearson bound gives, with confidence 1 − δ, a failure probability of at most 1 − δ^(1/n): 0.072 for n = 40 and δ = 0.05, but 0.45 for the five visible seeds the agent evaluates on." [Source: arxiv-2611.16867-controlharbor-a-benchmark-for-control-design-by.pdf p.5]
