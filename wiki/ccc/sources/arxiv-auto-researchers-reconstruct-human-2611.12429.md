---
title: "Can frontier auto researchers reconstruct human research decisions?"
type: source
related:
  - concepts/auto-researcher-human-similarity.md
  - concepts/ordinal-peer-prediction.md
  - concepts/baseline-and-metric-calibration.md
  - concepts/claim-drift-automated-research.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Can Frontier Auto Researchers Reconstruct Human Research Decisions in AI? |
| Author | Shengyun Si, Junjie Chu, Ye Leng, Yang Zhang (CISPA Helmholtz Center for Information Security) |
| Type | arXiv paper (cs.AI), 2611.12429 |
| Location | `research to be indexed/ccc/arxiv-2611.12429-can-frontier-auto-researchers-reconstruct-human.pdf` |
| Retrieved | 2026-11-10 |
| Pages | 14 |
| Read status | read |

## Narrative

The paper defines an **Auto Researcher** as a harness-based system that runs several stages of the research process itself. It asks a measurable question: given the same research context, how close are the agent's decisions to those of human researchers?

They build **AutoHRS**, a stage-wise evaluation framework with three tasks:

1. Literature-grounded idea generation.
2. Idea-grounded experiment design.
3. Findings-grounded paper synthesis.

The corpus is 152 ICLR oral papers, from which they derive 456 research trajectories. Each stage is scored by a checklist derived from the human reference output and verified by human annotators. The checklist correlates better with human judgement than free-form scoring.

Scores on a 0 to 1 normalised scale, for the best-scoring idea per paper:

| Stage | Score |
|-------|-------|
| Idea generation | 0.29 |
| Experiment design | 0.36 |
| Paper synthesis | 0.65 |

Auto researchers are much better at writing up findings than at choosing problems or designing experiments. The authors also find that the input granularity and the research type change the reconstruction score.

The method is reusable. **Evaluate an agent against a decision trace, not only against an output.** The checklist is derived from the reference and then human-filtered, which is a cheap way to keep automated grading honest.

## Snippets

> "current Auto Researchers frequently fail to recover key research decisions and their resulting artifacts across multiple stages of the research process." [Source: arxiv-2611.12429-can-frontier-auto-researchers-reconstruct-human.pdf p.1]

> "auto researchers achieve a score of 0.29 for the best-scoring idea per paper in idea generation, 0.36 on experiment design, and 0.65 on paper synthesis." [Source: arxiv-2611.12429-can-frontier-auto-researchers-reconstruct-human.pdf p.2]
