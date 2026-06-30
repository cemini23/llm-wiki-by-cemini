---
title: Extensive-form games with stochastic action sets (EFGSAS)
type: concept
tags: [concept, game-theory, poker, cfr, k122]
keywords: [EFGSAS, SI-CFR, extensive-form, Nash equilibrium, stochastic actions, sleeping regret]
related:
  - sources/arxiv-equilibrium-efgsas-2606.13093-2026-06-18.md
  - concepts/strategic-resource-acquisition-game-theory.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/team-zero-sum-games-complexity.md
  - sources/arxiv-team-zero-sum-games-2606.16139-2026-06-20.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/nash-equilibrium-solver-selection.md
  - concepts/projected-exploitability-descent.md
  - sources/arxiv-nash-solver-selection-2606.28308-2026-06-30.md
  - sources/arxiv-projected-exploitability-descent-2606.29169-2026-06-30.md
maturity: draft
created: 2026-06-18
updated: 2026-06-30
---

## Relations

- @sources/arxiv-equilibrium-efgsas-2606.13093-2026-06-18.md — primary source (Schwarz, Sim, Ling)
- @concepts/strategic-resource-acquisition-game-theory.md — competitive resource games under constraints
- @concepts/poker-arena-multi-axis-cognitive-profile.md — strategic mixing axis uses GTO/CFR baselines
- @concepts/team-zero-sum-games-complexity.md — team zero-sum PPAD hardness (K124)
- @concepts/nash-equilibrium-solver-selection.md — K136: CFR vs regularized equilibrium member selection on Nash polytopes
- @sources/arxiv-nash-solver-selection-2606.28308-2026-06-30.md — K136 source (Kuhn poker testbed)

## Raw Concept

Prompted by arXiv **2606.13093** (daily digest K122). Extends classical extensive-form game theory when the **action menu itself** is stochastically restricted — closer to real venues (partial liquidity, rule noise) than static EFG trees.

## Narrative

**Problem:** Standard EFGs assume full action sets at every node. **EFGSAS** models exogenous stochastic restriction of available actions from a base game. Naïve expansion can blow up strategy space exponentially; under independence, compact polynomial representations exist.

**SI-CFR:** sleeping-internal-regret variant of counterfactual regret minimization; converges to Nash in **two-player zero-sum** EFGSAS with high probability. Stochastic approximation compresses iterates into compact equilibrium strategies.

**Cemini relevance:**
- **Poker eval literacy** — Raeth Poker Arena (2606.13815) references CFR/equilibrium baselines for strategic-mixing and positional axes; EFGSAS is upstream theory, not LLM inference.
- **Execution games** — stochastic action sets mirror venues where order types or size buckets appear/disappear (latency, halts) — conceptual link to `@concepts/strategic-resource-acquisition-game-theory.md`, not a deployed primitive.

**Posture:** **REFERENCE** — no code repo; do not brief prod.

## Snippets

> "SI-CFR … converging to Nash equilibria with high probability in two-player zero-sum EFGSAS." [Source: arXiv:2606.13093 abstract (retrieved 2026-06-18)]

## Dead Ends

- Multi-player NLHE tournament dynamics ≠ two-player zero-sum EFGSAS — do not claim direct equilibrium computation for dev.fun 6-max.
