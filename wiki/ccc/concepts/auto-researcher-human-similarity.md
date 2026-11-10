---
title: "Auto-researcher–human similarity — score the decisions, not only the paper"
type: concept
related:
  - sources/arxiv-auto-researchers-reconstruct-human-2611.12429.md
  - sources/arxiv-information-elicitation-ordinal-agreement-2611.08366.md
  - sources/newsletter-rss-latent-space-2026-11-06-controlling-biology---fabian-theis-helmholtz-mun.md
  - concepts/baseline-and-metric-calibration.md
  - concepts/claim-drift-automated-research.md
  - concepts/ordinal-peer-prediction.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: how do you tell whether an autonomous research harness makes decisions like a competent researcher?

Synthesised from AutoHRS, plus the Theis interview and the ordinal-agreement mechanism as supporting context.

## Narrative

An **Auto Researcher** is a harness-based system that runs several stages of research itself. Judging its output on novelty or breakthrough value is not tractable. Judging whether it reconstructs human decisions is.

**AutoHRS** defines three stage-wise tasks and scores each against a human reference:

1. Literature-grounded idea generation.
2. Idea-grounded experiment design.
3. Findings-grounded paper synthesis.

Each stage is graded by a checklist derived from the reference output and filtered by a human annotator. The paper reports that the checklist correlates better with human judgement than free-form scoring.

Corpus: 152 ICLR oral papers, 456 trajectories. Normalised scores, best idea per paper:

| Stage | Score |
|-------|-------|
| Idea generation | 0.29 |
| Experiment design | 0.36 |
| Paper synthesis | 0.65 |

Current auto researchers write well and choose badly. They are far better at synthesising findings than at selecting a problem or designing the experiment that tests it. [TENTATIVE: single source]

### The method is the reusable part

- **Decompose the workflow into stages** and score each stage separately. Stage independence avoids error propagation and localises the failure.
- **Derive the rubric from the reference, then human-filter it.** Automated rubric generation alone produced generic questions.
- **Score decisions, not prose.** A good abstract over a weak experiment still scores low.

### Why it sits next to the eval-integrity cluster

The 0.29 and 0.36 scores are only meaningful if the checklist is calibrated. The Theis interview gives the counter-example: on Virtual Cell perturbation prediction, uninformative constant baselines beat complex models because the metric rewarded the mean. A checklist that a constant output can satisfy would show the same defect.

### Cemini application

The wiki already produces research artifacts (sources, concepts, briefs). A stage-wise check on an ingest is feasible without new tooling: did the source identify a gap, propose a test, and report a result? That is a short checklist per brief, and it separates "wrote a good page" from "did the work".

## Snippets

> "auto researchers achieve a score of 0.29 for the best-scoring idea per paper in idea generation, 0.36 on experiment design, and 0.65 on paper synthesis." [Source: arxiv-2611.12429-can-frontier-auto-researchers-reconstruct-human.pdf p.2]
