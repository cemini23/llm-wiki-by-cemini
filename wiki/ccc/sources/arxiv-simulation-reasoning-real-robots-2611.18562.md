---
title: "Training Reasoning Models in Simulation to Natively Use Real Robots (2611.18562)"
type: source
maturity: draft
related:
  - concepts/sim-to-real-robot-use-agents.md
updated: 2026-11-16
---

## Raw Concept

- **Title:** Training Reasoning Models in Simulation to Natively Use Real Robots
- **Authors:** Jiaming Tang, Zhuoyang Zhang, Junxian Guo et al. (MIT, UC Berkeley, UCSD, NVIDIA, Inco AI)
- **Type:** arXiv preprint
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.18562-training-reasoning-models-in-simulation-to-nativ.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18562
- **Read status:** full — 21 pages extracted 2026-11-16

## Narrative

A robot-use agent observes camera frames and arm state, reasons in a chain of thought, and emits an end-effector pose, in the same shape as a computer-use agent. It is trained with reinforcement learning entirely in simulation and then deployed on a real robot.

The reported result is that a trained open-weight model (Qwen3.8-27B, trained in LIBERO and RoboDojo) beats much larger frontier models on the same task family. On LIBERO the trained model reaches 74.4% against 48.1% for a base model and 49.3% for one frontier model at medium effort.

The transfer claims are the interesting part: 39.0% on unseen tasks against 10.7% for a prior trained policy, 60.0% on a new robot against 0.0%, and 96.9% on a robustness variant. General capability benchmarks show no regression before and after RL.

The framing that transfers beyond robotics: an agent trained in simulation on a narrow interaction contract can exceed a much larger general model on that contract, without a harness.

[Source: arxiv-2611.18562-training-reasoning-models-in-simulation-to-nativ.pdf]

## Snippets

> "It is trained with reinforcement learning entirely in simulation and deployed on a real robot."

## Dead Ends

- **Full-read note (2026-11-16):** Stated limitation, verbatim: "We have not been able to scale up our training." [Source: arxiv-simulation-reasoning-real-robots-2611.18562.md full text, 21pp]
