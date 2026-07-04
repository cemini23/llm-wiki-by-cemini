---
title: "Variable-bound tightening for multiplayer imperfect-information Nash — arXiv 2606.25997"
type: source
tags: [source, arxiv, game-theory, poker, nash, optimization, k143]
keywords: [2606.25997, variable bound tightening, slack bounds, multiplier bounds, branch-and-bound, three-player Kuhn poker]
related:
  - concepts/exact-multiplayer-nash-computation.md
  - sources/arxiv-quadratic-programming-nash-2509.25618-2026-07-04.md
  - concepts/projected-exploitability-descent.md
  - concepts/nash-equilibrium-solver-selection.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
maturity: draft
read_status: read
created: 2026-07-04
updated: 2026-07-04
clusters: [rl-marl, poker]
---

## Relations

- @concepts/exact-multiplayer-nash-computation.md — K143 synthesis
- @sources/arxiv-quadratic-programming-nash-2509.25618-2026-07-04.md — prior NCP/QP formulation improved by this paper
- @concepts/projected-exploitability-descent.md — sibling exact/approximate multiplayer solver line
- @concepts/nash-equilibrium-solver-selection.md — solver-family caution
- @concepts/kuhn-poker-sft-curriculum-reference.md — Kuhn toy-game curriculum anchor

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Variable Bound Tightening for Nash Equilibrium Computation in Multiplayer Imperfect-Information Games |
| **Author** | Sam Ganzfried (Ganzfried Research, Cornell University) |
| **arXiv** | 2606.25997v2 (30 Jun 2026) |
| **sha256** | `1f125dbb11e9bc7cbc16fa2cc9a269b58b0db3c9ffd8fba67f49430474a58eb9` |
| **Repo** | none public |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.25997-variable-bound-tightening-for-nash-equilibrium-c.pdf` |
| **Retrieved** | 2026-07-04 daily digest inbox |
| **Read status** | read (abstract, bound derivations, §4 experiments/conclusion) |

## Narrative

Improves the NCP/QP exact-solver line from `@sources/arxiv-quadratic-programming-nash-2509.25618-2026-07-04.md` by deriving finite bounds for slack and multiplier variables from the best-response LP dual structure.

**Key result:** the full three-player Kuhn poker game, previously unsolved by the NCP approach after **24 hours**, solved in **1.160 seconds** when applying slack-variable bounds only. Multiplier bounds helped when used alone but slowed the best configuration when combined with slack bounds.

**Operational intuition:** slack variables appear in the quadratic constraints, so tightening their domains materially strengthens spatial branch-and-bound relaxations. The bound used in the experiment was 0.25, while the largest optimal slack value was 0.167.

**Cemini posture:** **REFERENCE**. Strong theoretical/poker-literacy result; no code artifact, no live Arena route. Steal the preprocessing lesson: exact toy-game baselines can hinge on dominated-action removal and solver-domain tightening, not just the high-level equilibrium algorithm.

## Snippets

> "Overall, our improvements enabled us to solve a problem that was previously intractable (could not be solved in 24 hours) in just 1.160 seconds." [Source: arXiv:2606.25997 §4 (retrieved 2026-07-04)]

> "The bounds for the slack variables are particularly valuable since they appear in quadratic constraints." [Source: arXiv:2606.25997 §5 (retrieved 2026-07-04)]

## Dead Ends

- Exact solver speedups on full three-player Kuhn do not imply tractability for NLHE-scale games.
- No public implementation; treat as solver-design reference rather than adoption candidate.
