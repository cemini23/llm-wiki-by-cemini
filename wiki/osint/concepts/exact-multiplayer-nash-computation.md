---
title: Exact multiplayer imperfect-information Nash computation
type: concept
tags: [concept, game-theory, poker, nash, optimization, k143]
keywords: [multiplayer imperfect-information games, nonlinear complementarity, sequence form, quadratic programming, Kuhn poker, variable bound tightening]
related:
  - sources/arxiv-diffnash-diffusion-equilibrium-2610.15932-2026-10-14.md
  - sources/arxiv-quadratic-programming-nash-2509.25618-2026-07-04.md
  - sources/arxiv-variable-bound-tightening-nash-2606.25997-2026-07-04.md
  - concepts/projected-exploitability-descent.md
  - concepts/nash-equilibrium-solver-selection.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
maturity: draft
created: 2026-07-04
updated: 2026-07-04
---

## Relations

- @sources/arxiv-quadratic-programming-nash-2509.25618-2026-07-04.md — initial NCP/QP exact-solver formulation
- @sources/arxiv-variable-bound-tightening-nash-2606.25997-2026-07-04.md — slack-bound tightening that solves full 3-player Kuhn
- @concepts/projected-exploitability-descent.md — approximate/refinement sibling in the Ganzfried solver line
- @concepts/nash-equilibrium-solver-selection.md — broader warning that solver choice changes the equilibrium member or solution concept

## Raw Concept

Prompted by K143 daily digest papers from Sam Ganzfried: arXiv **2509.25618** and **2606.25997**. Together they form an exact-solver micro-cluster for multiplayer imperfect-information games: sequence-form NCP → quadratically constrained feasibility program → branch-and-bound performance governed by dominated-action preprocessing and variable-domain tightening.

## Narrative

### What changed

The first paper shows that a sequence-form NCP/QP can compute an essentially exact Nash equilibrium for **reduced three-player Kuhn poker** in seconds, beating Gambit's logit QRE approximation on that reduced instance.

The second paper shows the same formulation was not fundamentally stuck on full three-player Kuhn: unbounded slack/multiplier variables were weakening the nonconvex solver. Bounding slack variables via best-response duality moved full-game solve time from **>24 hours** to **1.160 seconds**.

### Solver ladder

| Use case | Practical posture |
|----------|-------------------|
| Small toy game, exact equilibrium needed | NCP/QP with dominated-action removal and slack-bound tightening |
| Larger toy game, approximate baseline acceptable | Gambit logit QRE or PED/FP-PED |
| Arena/NLHE-scale policy work | CFR/FP-style offline approximations, verifier/axis metrics, exploitability literacy only |

### Poker relevance

This is not a live `decide()` path. It is useful for **baseline literacy**:

- Kuhn and related toy games are still rich enough to exhibit bluffing, trapping, off-path equilibrium differences, and solver-selection effects.
- Exact baselines need provenance: solver family, dominated-action preprocessing, and domain-bound choices all matter.
- Strategic-mixing axis work should not collapse "Nash-like" outputs into one interchangeable chart.

## Snippets

> "The full game has 48 total information sets ... and 601 total nodes." [Source: arXiv:2606.25997 §3 (retrieved 2026-07-04)]

> "Slack Bounds: Yes; Multiplier Bounds: No; Solve Time: 1.160 seconds." [Source: arXiv:2606.25997 Table 1 (retrieved 2026-07-04)]

## Dead Ends

- Do not promote this to Poker Arena implementation work. The research gives exact-solver discipline for toy baselines, not tractable NLHE policy search.
