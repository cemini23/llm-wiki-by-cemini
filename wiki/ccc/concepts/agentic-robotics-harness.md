---
title: "Agentic robotics harness — generalist model, direct control, benchmark criteria"
type: concept
related:
  - sources/arxiv-vabar-variational-automation-benchmark-2611.06881.md
  - sources/arxiv-agentic-manipulation-policies-amp1-2611.09892.md
  - sources/arxiv-video-coder-agentic-coding-2611.09894.md
  - concepts/model-harness-six-responsibilities.md
  - concepts/benchmark-maintenance-debt.md
  - concepts/harness-learning-test-time-adaptation.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: what do three 2026 robotics papers say about harness design that transfers to non-robot agents?

Synthesised from VABAR (benchmark criteria), AMP1 (policy architecture), and Video-Coder (harness-native training).

## Narrative

### Three designs

**VABAR** defines Variational Automation: one operational objective across a controlled distribution of object shapes, poses, and conditions. It argues that a good agentic-robotics benchmark needs relevance, accessibility, controlled diversity, repeatability, saturation resistance, and computational efficiency. It ships six task classes, 33 skills, and reference solutions.

**AMP1** lets a generalist model command a manipulator directly, with no specialist policy. The base harness supplies no grasping or placing skills. The agent invents search, tool use, and camera calibration itself. Zero-shot it reaches 85.6% on RoboLab-120 against 49.2% for the best vision-language-action model. [TENTATIVE: single source, vendor paper]

**Video-Coder** trains an agent to write code that builds a 3D scene. The rendered draft video then conditions a video generator. The harness is the training environment: execution reward and video reward, with the execution reward annealed down over training.

### Four transferable claims

1. **The model dominates the harness.** AMP1 success on RoboLab-120 was 82.8% with Opus 5.5, 51.6% with Haiku 5.5, and 35.2% with Opus 4.5.
2. **Assistive harness routines help weak models and hurt strong ones.** Grabbing and placing helpers are a crutch, not a baseline.
3. **Strong models absorb missing sensors; weak models collapse.** Opus 5.5 fell from 82.8% to 75.8% without depth or calibration. Haiku 5.5 fell from 51.6% to 10.7%.
4. **Replace perception with description and you lose.** Opus 5.5 fell from 82.8% to 36.8% when images became text. This contradicts earlier guidance.

Claims 1 to 4 map onto `@concepts/model-harness-six-responsibilities.md`: the harness supplies observation, action, and state, but it cannot supply reasoning quality.

### Why it sits in ccc

Cemini has no robot. The value is the control experiment design. Hold the executor fixed, vary the harness, then report both. WorkflowArena uses the same trick with a fixed executor. See `@concepts/workflow-orchestration-as-capability.md`.

## Snippets

> "The basic harness supplies no grasping, pushing, or placing skills; the agent develops its own strategies" [Source: arxiv-2611.09892-on-agentic-manipulation-policies.pdf p.1]
