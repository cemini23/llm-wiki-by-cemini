---
title: Nash equilibrium solver selection (K136)
type: concept
tags: [concept, game-theory, poker, cfr, k136, reference-only]
keywords: [Nash polytope, maximum-entropy, CFR+, R-NaD, fictitious play, solver interchangeability, Kuhn poker]
related:
  - sources/arxiv-nash-solver-selection-2606.28308-2026-06-30.md
  - sources/arxiv-projected-exploitability-descent-2606.29169-2026-06-30.md
  - concepts/exact-multiplayer-nash-computation.md
  - sources/arxiv-quadratic-programming-nash-2509.25618-2026-07-04.md
  - sources/arxiv-variable-bound-tightening-nash-2606.25997-2026-07-04.md
  - concepts/extensive-form-games-stochastic-action-sets.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/team-zero-sum-games-complexity.md
  - concepts/takeover-auction-diligence-solvers.md
  - sources/arxiv-takeover-auction-diligence-2606.29457-2026-07-01.md
  - concepts/projected-exploitability-descent.md
maturity: draft
created: 2026-06-30
updated: 2026-10-25
---

## Relations

- @sources/arxiv-nash-solver-selection-2606.28308-2026-06-30.md — primary source (Leal, 2606.28308)
- @concepts/exact-multiplayer-nash-computation.md — K143 exact-solver sibling cluster
- @concepts/takeover-auction-diligence-solvers.md — K138 PPO vs exact CFR on deal auctions (2606.29457)
- @concepts/extensive-form-games-stochastic-action-sets.md — CFR theory cluster (K122)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — M₇ strategic-mixing axis

## Raw Concept

What prompted this page: K136 arXiv **2606.28308** shows that when a two-player zero-sum game has a **non-singleton Nash set**, CFR-family and regularized last-iterate solvers **systematically select different equilibria** — not interchangeable at the strategy-profile level even though all achieve \(V^\*\).

## Narrative

### Solver families

| Family | Examples | Deployed strategy | Selection bias (asymmetric Nash sets) |
|--------|----------|-------------------|--------------------------------------|
| Regret averaging | CFR, CFR+, fictitious play | Time average | Lower-entropy face (FP drifts on symmetric games too) |
| Regularized last-iterate | R-NaD, magnetic mirror descent | Final iterate | **Maximum-entropy** ≈ I-projection of uniform reference |

Differences vanish on **symmetric** Nash geometry; emerge on **asymmetric** polytopes. Kuhn poker: max-entropy member is a **better hedge** vs flawed opponents.

### Cemini / poker relevance

- **Chart provenance:** log which solver produced a GTO-ish baseline (CFR+ vs regularized) when equilibrium set may be non-singleton.
- **Axis eval:** M₇ mixing entropy — align with max-entropy selection when using regularized solvers on toy games.
- **Not for NLHE prod:** tabular ground truth infeasible; literacy only.

**Posture:** REFERENCE — brief steal → `agents/devfun-poker-arena/briefs/`.

### K143 extension: exactness vs selected member

K143 shifts the adjacent question from **which equilibrium member** a solver selects to **which solution concept/exactness target** the solver can support in multiplayer imperfect-information games. NCP/QP exact solvers, logit QRE approximations, PED/FP-PED refiners, and CFR/FP baselines should not be treated as interchangeable "Nash-ish" chart generators. For any toy-game chart, record solver family, preprocessing (dominated-action removal), and whether the output is exact Nash, QRE approximation, exploitability descent, or regret-average baseline.

## Snippets

> "R-NaD attains the maximum-entropy member in 100% of converged games [180-game ensemble] while CFR+ sits strictly below it in 94%." [Source: arXiv:2606.28308 abstract (retrieved 2026-06-30)]
