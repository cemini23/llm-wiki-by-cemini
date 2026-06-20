---
title: Team zero-sum games — PPAD complexity
type: concept
tags: [concept, game-theory, poker, marl, k124]
keywords: [team zero-sum, PPAD, Nash, polymatrix, equilibrium hardness]
related:
  - sources/arxiv-team-zero-sum-games-2606.16139-2026-06-20.md
  - concepts/extensive-form-games-stochastic-action-sets.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/multi-agent-fictitious-play-llm.md
  - sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @sources/arxiv-team-zero-sum-games-2606.16139-2026-06-20.md — primary source (Anagnostides et al.)
- @concepts/extensive-form-games-stochastic-action-sets.md — EFG equilibrium computation (K122)
- @concepts/multi-agent-fictitious-play-llm.md — iterative equilibrium seeking for LLMs (K124)

## Raw Concept

Prompted by arXiv **2606.16139** (daily digest K124). When each side of a zero-sum game has **multiple non-coordinating agents**, Nash equilibrium computation jumps from tractable (2-player zero-sum → P) to **PPAD-complete** (2 vs 2 teams).

## Narrative

**Model:** team zero-sum games generalize two-player zero-sum and potential games. Each team shares a payoff but members choose actions independently — communication may be costly (bridge, firm teams, multi-agent RL).

**Result:** ε-Nash in 2×2 team polymatrix games is PPAD-complete at inverse-polynomial precision — **as hard as general-sum**, despite adversarial team structure. Min-max first-order stationary points for quadratic objectives share the same barrier.

**Poker relevance:**
- Heads-up NLHE retains two-player zero-sum tractability for **full coordination** models; multi-way pots introduce **team-like partial coordination** (implicit collusion impossible but correlated unilateral errors persist).
- Explains why multi-agent poker eval (Raeth 7-max) cannot lean on closed-form minimax — aligns with `@concepts/poker-arena-multi-axis-cognitive-profile.md` axis-over-chip thesis.

**Posture:** **REFERENCE** — wiki literacy only; no prod brief.

## Snippets

> "Team zero-sum games are as hard as general-sum games." [Source: arXiv:2606.16139 (retrieved 2026-06-20)]

## Dead Ends

- Paper does not implement poker solvers — do not cite for HU exploit frequencies.
