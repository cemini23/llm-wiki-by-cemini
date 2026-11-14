---
title: "On agentic manipulation policies — AMP1 beats specialist robot policies"
type: source
related:
  - concepts/agentic-robotics-harness.md
  - concepts/model-harness-six-responsibilities.md
  - concepts/subagent-orchestration.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | On Agentic Manipulation Policies |
| Author | Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, and others (Apple) |
| Type | Research article (arXiv cs.RO), 2611.09892 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.09892-on-agentic-manipulation-policies.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 31 |
| Read status | read |

## Narrative

An **agentic manipulation policy (AMP)** lets a generalist model command a robot directly and adapt as the task unfolds. Two prior designs are compared. Skill orchestration limits the model to choosing provided skills. Offline program synthesis writes one control program before execution and leaves the model out of the loop.

**AMP1** is the reference harness. It runs unchanged across single-arm, bimanual, and mobile robots.

Zero-shot results:

- RoboLab-120: 85.6% success, against 49.2% for the best vision-language-action model (VLA) and 42.9% for the best world-action model (WAM).
- Real world: 104 of 108 trials succeeded, across twelve tasks and three robot instances. That is a 20x and 15x reduction in failure rate against strong VLA and WAM baselines.

The base harness supplies no grasping, pushing, or placing skills. The agent develops its own strategies: searching for hidden objects, using objects as tools, calibrating its cameras.

A persistent memory variant learns across episodes. On RoboDojo bimanual tasks it lowers the failure rate 4.6x against zero-shot. Practice raises success on unseen layouts from 26.4% to 84.1%. One pass through tasks in sequence more than doubles success to 57.6%. Memory also cuts model calls by about 35%.

The controlled experiments are the transferable result:

- **Model choice dominates.** RoboLab-120 success was 82.8% with Opus 5.5, 51.6% with Haiku 5.5, and 35.2% with Opus 4.5.
- **More reasoning helps every model.**
- **Harness help is model-dependent.** Assistive grasping and placing routines help weak models and hurt strong ones.
- **Strong models absorb missing sensors.** Opus 5.5 falls from 82.8% to 75.8% without depth and camera calibration, at a cost of more model calls. Haiku 5.5 collapses from 51.6% to 10.7%.
- **Replacing images with text descriptions is sharply harmful** — 82.8% to 36.8% on Opus 5.5.

That last point contradicts prior guidance, and it is a useful reminder that one term should mean one thing: perception is not a summary of perception.

## Snippets

> "The choice of model has the largest effect." [Source: arxiv-2611.09892-on-agentic-manipulation-policies.pdf p.3]

> "Weaker models are helped by assistive grasping and placing routines, while stronger models perform best without these routines." [Source: arxiv-2611.09892-on-agentic-manipulation-policies.pdf p.3]
