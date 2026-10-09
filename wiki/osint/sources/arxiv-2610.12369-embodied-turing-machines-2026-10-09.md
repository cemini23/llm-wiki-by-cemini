---
title: "Embodied Turing Machines (arXiv 2610.12369)"
type: source
tags: [source, k287, arxiv, robotics, code-policy]
keywords: [embodied-turing-machine, coap, robodojo, k287]
related:
  - concepts/k287-arxiv-wave.md
maturity: draft
created: 2026-10-09
updated: 2026-10-09
read_status: read
---

## Relations

- @concepts/k287-arxiv-wave.md

## Raw Concept

| Title | Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement |
| Authors | Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu |
| Type | arXiv preprint |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.12369-embodied-turing-machines-stateful-code-for-robot.pdf` |
| Retrieved | 2026-10-09 |
| arXiv | 2610.12369v1 |
| Licence | arXiv non-exclusive distribution 1.0 |
| read-status | read |

## Narrative

The paper treats the robot and the scene as a tape, and the policy as code. Code-Only-as-Policy keeps perception and decisions in code. It does not keep a vision-language model in the control loop.

The figure reports 70.24 percent success for that code policy on RoboDojo, against 33.95 percent for a vision-language-action baseline and 27.96 percent for an agent harness.

**No training wire.** Do not start a recursive self-improvement job from this paper. FILE only.

## Snippets

> "If this state can be represented accurately, the decision making can be written entirely in code." [Source: arxiv-2610.12369 PDF, abstract]
