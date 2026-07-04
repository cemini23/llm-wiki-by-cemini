---
title: "Quadratic programming for multiplayer imperfect-information Nash — arXiv 2509.25618"
type: source
tags: [source, arxiv, game-theory, poker, nash, k143]
keywords: [2509.25618, nonlinear complementarity, quadratically constrained program, three-player Kuhn poker, Gambit, logit QRE]
related:
  - concepts/exact-multiplayer-nash-computation.md
  - sources/arxiv-variable-bound-tightening-nash-2606.25997-2026-07-04.md
  - concepts/projected-exploitability-descent.md
  - concepts/nash-equilibrium-solver-selection.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/multi-agent-fictitious-play-llm.md
maturity: draft
read_status: read
created: 2026-07-04
updated: 2026-07-04
clusters: [rl-marl, poker]
---

## Relations

- @concepts/exact-multiplayer-nash-computation.md — K143 synthesis
- @sources/arxiv-variable-bound-tightening-nash-2606.25997-2026-07-04.md — follow-on bound-tightening improvement
- @concepts/projected-exploitability-descent.md — sibling Ganzfried multiplayer solver line
- @concepts/nash-equilibrium-solver-selection.md — solver-family caution; K143 extends from selection to exact computation
- @concepts/kuhn-poker-sft-curriculum-reference.md — Kuhn toy-game curriculum anchor
- @concepts/poker-arena-multi-axis-cognitive-profile.md — Kuhn poker baseline literacy for strategic-mixing axis

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Quadratic Programming Approach for Nash Equilibrium Computation in Multiplayer Imperfect-Information Games |
| **Author** | Sam Ganzfried (Ganzfried Research) |
| **arXiv** | 2509.25618v2 (30 Jun 2026) |
| **sha256** | `85b44f27d63caf8a605ae39c566683ee7583b600a0b7f199a7eec08a2b7581c1` |
| **Repo** | none public |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2509.25618-quadratic-programming-approach-for-nash-equilibr.pdf` |
| **Retrieved** | 2026-07-04 daily digest inbox |
| **Read status** | read (abstract, algorithm framing, §3–5 experiments/conclusion) |

## Narrative

Presents an exact Nash-equilibrium formulation for **multiplayer imperfect-information games** using a sequence-form nonlinear complementarity problem (NCP) modeled as a quadratically constrained feasibility program.

**Benchmark:** reduced three-player Kuhn poker after dominated-action removal. The NCP/Gurobi route solved the reduced game in **2.47 seconds** with deviation gain \(1.4 \times 10^{-17}\), while Gambit's only successful applicable method, logit QRE, took **43–49 seconds** and produced a \(1.667 \times 10^{-5}\) approximate equilibrium.

**Limit:** the same approach did **not** solve full three-player Kuhn poker within 24 hours. Dominated-action preprocessing made the difference between tractable and intractable for this exact solver.

**Cemini posture:** **REFERENCE**. Use for poker/game-theory literacy and offline toy-game baselines only; not a live Arena `decide()` method and not a deployable repo.

## Snippets

> "Our approach was able to solve the game in 2.47 seconds. We verified that no player can gain more than 1.4 × 10−17 by deviating from the computed solution." [Source: arXiv:2509.25618 §4 (retrieved 2026-07-04)]

> "The logit QRE approach took 17.4 times longer to solve the reduced version than our new algorithm, but was successfully able to solve the full version in several minutes while our algorithm was not." [Source: arXiv:2509.25618 §4 (retrieved 2026-07-04)]

## Dead Ends

- Exact NCP/QP is small-game tooling. Full three-player Kuhn already broke the initial formulation; multiplayer NLHE remains far outside scope.
- Requires commercial/nonconvex quadratic solver infrastructure; no public implementation to adopt.
