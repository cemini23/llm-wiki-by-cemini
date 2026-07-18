---
title: Play-Adequacy vs Prediction-Accuracy
type: concept
tags: [concept, poker, eval, k173]
keywords: [play-adequacy, transition-accuracy, CWM, sandbox-gates]
related:
  - sources/arxiv-2607.14169-play-adequacy-vs-prediction-accuracy.md
  - concepts/belief-conditioned-agent-audit-hidden-info.md
maturity: draft
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- @sources/arxiv-2607.14169-play-adequacy-vs-prediction-accuracy.md
- @concepts/belief-conditioned-agent-audit-hidden-info.md

## Raw Concept

Acceptance criteria for simulators / coded world models / poker sandbox gates: high transition accuracy on sampled trajectories ≠ adequacy for planning or competitive play.

## Narrative

Rare omitted rules can have near-zero mass under random rollouts yet dominate under competent search. Ship checks should sample **search-visited / adversarial** distributions and prefer head-to-head play metrics. Completing the specification beats flooding more similar examples when the rule is missing from the coded heuristic.
