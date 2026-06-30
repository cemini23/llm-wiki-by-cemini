---
title: "Which Nash Equilibrium? Solver-Dependent Selection — arXiv 2606.28308"
type: source
tags: [source, arxiv, game-theory, poker, cfr, k136]
keywords: [2606.28308, Nash polytope, maximum-entropy equilibrium, CFR, CFR+, fictitious play, R-NaD, Kuhn poker, exploitability]
related:
  - concepts/nash-equilibrium-solver-selection.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
  - concepts/extensive-form-games-stochastic-action-sets.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/multi-agent-fictitious-play-llm.md
  - sources/arxiv-projected-exploitability-descent-2606.29169-2026-06-30.md
maturity: draft
read_status: read
created: 2026-06-30
updated: 2026-06-30
clusters: [rl-marl]
---

## Relations

- @concepts/nash-equilibrium-solver-selection.md — K136 synthesis
- @concepts/kuhn-poker-sft-curriculum-reference.md — Kuhn poker testbed in paper
- @concepts/extensive-form-games-stochastic-action-sets.md — CFR family sibling theory
- @concepts/poker-arena-multi-axis-cognitive-profile.md — strategic-mixing axis uses equilibrium baselines

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Which Nash Equilibrium? Solver-Dependent Selection on Zero-Sum Nash Polytopes |
| **Authors** | Luis Leal |
| **arXiv** | 2606.28308 (26 Jun 2026) |
| **sha256** | `633bdb24ec4db7ac1958efaf0b5294f4182890b73332a49dc439fdb76ad6d529` |
| **Repo** | none public |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.28308-which-nash-equilibrium-solver-dependent-selectio.pdf` |
| **Retrieved** | 2026-06-30 (inbox) |
| **Read status** | read (abstract + §1–2 + Kuhn results) |

## Narrative

Two-player zero-sum games often have a **convex Nash polytope** — all profiles achieve minimax value \(V^\*\) but differ in off-path behaviour, support, and robustness to suboptimal opponents. This paper asks whether standard solvers **select different equilibria systematically** (algorithm, not seed).

**Testbed:** tabular extensive-form engine with exact counterfactual values; six games with analytic Nash sets including **Kuhn poker** and a 2-D Nash polytope.

**Findings [CONFIRMED] on testbed:**
1. Selection is **algorithmic** and **geometry-gated** — large splits on asymmetric Nash sets, vanish on symmetric controls.
2. **Regularized last-iterate** methods (R-NaD, magnetic mirror descent) pick the **maximum-entropy** member ≈ I-projection of uniform reference onto \(\mathcal{N}(G)\) — exact on 2-D polytope, 99.7% max entropy in Kuhn; **CFR/CFR+/FP** drift to lower-entropy faces on asymmetric games.
3. Against flawed opponents, selected member matters most in **sequential/hidden-info** games (Kuhn); matrix games show smaller bounded gaps.
4. **Negative results:** CFR's \(\max(R,0)\) projection is not the cause of boundary drift; R-NaD selection is **anchor-following** (not init-independent).

**Cemini posture:** **REFERENCE** — no code artifact. Informs poker baseline literacy: do not treat CFR+ and R-NaD outputs as interchangeable when the equilibrium set is non-singleton; prefer documenting which solver family produced a chart.

## Snippets

> "When the equilibrium set is not a singleton, a solver does not merely find an equilibrium; it selects one." [Source: arXiv:2606.28308 §1 (retrieved 2026-06-30)]

> "In Kuhn the max-entropy member is a strictly better hedge against flawed opponents." [Source: arXiv:2606.28308 abstract (retrieved 2026-06-30)]

## Dead Ends

- NLHE has enormous imperfect-info trees — tabular ground-truth Nash sets infeasible; steal is **solver-family awareness**, not direct replication.
- No public implementation — Phase-0 finds no adoptable repo.
