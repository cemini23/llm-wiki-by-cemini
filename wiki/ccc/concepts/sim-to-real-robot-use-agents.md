---
title: Robot-use agents trained in simulation
type: concept
maturity: draft
related:
  - sources/arxiv-simulation-reasoning-real-robots-2611.18562.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: can a small open model trained in simulation control a real robot better than a large general model?

From arXiv 2611.18562 (MIT, UC Berkeley, UCSD, NVIDIA, Inco AI).

## Narrative

The agent shape matches a computer-use agent: observe the scene, reason in a chain of thought, emit an action. Here the action is an end-effector pose rather than a click. Training happens entirely in simulation with RL; deployment is on a real robot.

The headline number is the comparison against generalists. A trained Qwen3.8-27B reaches 74.4% on LIBERO against 48.1% for its base and 49.3% for a frontier model at medium effort.

Transfer is where the paper is most useful. On unseen tasks 39.0% against 10.7% for a prior trained policy; on a new robot 60.0% against 0.0%; on a robustness variant 96.9%. General benchmarks show no regression before and after RL.

The pattern that generalises: training on a narrow interaction contract in a simulator can beat a far larger general model on that contract, and the specialist keeps its general capability. This is the strongest case yet in this wiki for "train the narrow contract, do not rely on the big model's zero-shot skill".

[TENTATIVE] One paper's abstract and overview figure. Real-robot and transfer results were not independently reproduced.

## Snippets

> "strong performance has so far been achieved only by frontier proprietary models … whereas open-weight models remain substantially less capable" — the gap the paper claims to close.
