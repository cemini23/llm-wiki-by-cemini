---
title: "Generalizing Manipulation Skills with a Local Coding Agent"
type: source
tags: [arxiv, source, k270, robotics, harness]
keywords: [k270, VLM, UR3e, coding-agent, generalization]
related:
  - concepts/k270-harness-evolution-wave.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
read_status: skimmed
---

## Relations

- @concepts/k270-harness-evolution-wave.md

## Raw Concept

| Paper | arXiv:2609.26499 |
| File | `arxiv-2609.26499-generalizing-manipulation-skills-with-a-local-co.pdf` |
| Location | `local inbox (archive blocked 2026-09-23): research to be indexed/arxiv-2609.26499-generalizing-manipulation-skills-with-a-local-co.pdf` |
| Authors | Raman Talwar, Elias Nijs, Andreas Verleysen, Francis wyffels |
| Retrieved | 2026-09-23 |
| Pages | 8 |
| Dual-ID | **OSINT K270** |
| sha256 | `6145b7cb5f34689a67cd260f9e4e4add7d388e2751b266a1c8d1bc4a9cfea6cb` |

## Narrative

Most language-driven robots give the model a fixed action interface or a trained policy. Generalizing to a new task then needs more engineering effort or more data collection. This paper tests whether a **local open-weight vision-language model** can control a robot and one-shot generalize to new task variations, with no new human programming and no training.

**Setup.** A local open-weight VLM, **Qwen3.8-27B**, drives a **UR3e** robotic arm from a coding-agent harness. The agent writes and runs its own code above a service. That service implements kinematics, safety limits, and classic computer vision techniques.

**Generalization test.** Nine tasks built from children's toys probe generalization across object color, size, shape, and task variation. Five trials per task. The system generalizes in **30 of 45 trials**. Durations range from **3.4 to 67.5 minutes**, depending on task complexity.

**Self-improvement test.** When the agent is asked to redo a task after successful completion, duration drops by **50%**. The paper reads this as self-improvement over time.

**Limitations.** The paper exposes limitations of a local coding agent. It argues that solving those limitations, combined with further study of self-improvement over time, points at a path toward real-world deployment.

**Cemini relevance:** local open-weight coding-agent harness pattern only. **Robotics `wont_wire`. FILE only. 0 product Integrate GO. Never `npx github:`.**
