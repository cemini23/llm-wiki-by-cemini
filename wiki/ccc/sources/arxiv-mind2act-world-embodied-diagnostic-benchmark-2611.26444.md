---
title: "Mind2Act-World — separating mind, action and their composition in robotic manipulation"
type: source
related:
  - concepts/mind-act-composition-diagnosis.md
  - concepts/harness-attribution-multimodal-eval.md
  - concepts/agentic-robotics-harness.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|------|
| Title | Mind2Act-World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation |
| Author | Yuzhi Huang, Jie Wu, Fanding Huang et al. (THU, Cambridge, Oxford, Stanford, CMU and others) |
| Type | arXiv benchmark paper, 2611.26444 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.26444-mind2act-world-a-diagnostic-benchmark-for-embodi.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 58 |
| Read status | read |

## Narrative

Mind2Act-World separates three views of the same robot task: **Mind** (memory, goal selection, planning), **Act** (timely, precise, stable execution), and **Mind2Act** (the composition of the two). It has 30 tasks across three levels, 12 capability categories, and 180 configurations in Isaac Sim.

The headline result is the composition gap. A strong Mind score and a strong Act score do not produce a strong Mind2Act score. The paper reports 52.7% on Mind and 39.0% on Act against 12.0% on Mind2Act. The benchmark also reports a first-failure trace per run, so a failure is attributed to a stage and a failure code rather than a single number.

This is a moderate fit for CCC. It is a robotics benchmark, but the design idea transfers: score the sub-capabilities separately from the composition, and record where the first failure occurred. A single end-to-end score hides which layer broke. Cemini's harness work has the same problem when a task fails — model, harness or environment. [TENTATIVE] single source.

## Snippets

> "Strong Mind 52.7% + strong Act 39.0% ≠ Mind2Act 12.0%." [Source: arxiv-2611.26444-mind2act-world-a-diagnostic-benchmark-for-embodi.pdf p.1]
