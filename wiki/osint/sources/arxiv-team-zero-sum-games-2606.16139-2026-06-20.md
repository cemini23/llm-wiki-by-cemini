---
title: "Team zero-sum games — PPAD complexity — arXiv 2606.16139"
type: source
tags: [source, arxiv, game-theory, poker, k124]
keywords: [2606.16139, team zero-sum, PPAD, Nash equilibrium, polymatrix, min-max]
related:
  - concepts/team-zero-sum-games-complexity.md
  - concepts/extensive-form-games-stochastic-action-sets.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
maturity: draft
read_status: read
created: 2026-06-20
updated: 2026-06-20
clusters: [rl-marl]
---

## Relations

- @concepts/team-zero-sum-games-complexity.md — K124 synthesis
- @concepts/extensive-form-games-stochastic-action-sets.md — equilibrium computation sibling (K122)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — poker eval uses equilibrium baselines

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Computational Complexity of Team Zero-Sum Games |
| **Authors** | Ioannis Anagnostides, Ioannis Panageas, Tuomas Sandholm, Jingming Yan |
| **arXiv** | 2606.16139 (16 Jun 2026) |
| **sha256** | `72032a165ae1d52189abac9fff54fc1d55ebec1ff0f4ee6e6150f29c1d8b522b` |
| **Repo** | none public |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.16139-2606-16139v1-the-computational-complexity-of-tea.pdf` |
| **Retrieved** | 2026-06-20 (daily digest inbox) |
| **Read status** | read (abstract + §1 + complexity table) |

## Narrative

Settles complexity of **team zero-sum games**: multiple agents per side share a team objective but cannot perfectly coordinate. Computing an ε-approximate Nash equilibrium is **PPAD-complete** even for **2 vs 2** teams, inverse-polynomial precision, and **polymatrix** structure — as hard as general-sum games despite global adversarial structure.

**Prior landscape:** two-player zero-sum → **P** (minimax); n vs 1 adversarial team → **CLS-complete**; n vs m (both ≥2) → open until this paper.

**Also:** first-order stationary points in min-max optimization with **quadratic multilinear objectives** are PPAD-complete.

**Cemini posture:** **REFERENCE** — pure game-theory literacy for poker/MARL; no code install. Informs why multi-agent poker teams (implicit collusion models) don't inherit tractable two-player zero-sum solvers.

## Snippets

> "Computing an ϵ-approximate Nash equilibrium in 2 vs. 2 team zero-sum games is PPAD-complete even when ϵ is inversely polynomial in the size of the input." [Source: arXiv:2606.16139 Theorem 1.1 (retrieved 2026-06-20)]

> "Team zero-sum games generalize both two-player zero-sum games and potential games." [Source: arXiv:2606.16139 §1 (retrieved 2026-06-20)]

## Dead Ends

- No implementation artifact — theory-only; do not brief prod.
- Bridge/card-game examples are illustrative, not poker solver code.
