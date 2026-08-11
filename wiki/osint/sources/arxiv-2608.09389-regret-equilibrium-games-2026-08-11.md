---
title: "Regret, Equilibrium, and Learning in Games — A Guided Tour"
type: source
tags: [arxiv, k232, poker]
keywords: [2608.09389, regret, fictitious-play, ftrl, exp3, nash-equilibrium, learning-in-games]
related:
  - concepts/swap-regret-attention-fictitious-play.md
  - concepts/devfun-poker-agent-challenge-2026.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
read_status: skimmed
---

## Relations

- @concepts/swap-regret-attention-fictitious-play.md
- @concepts/devfun-poker-agent-challenge-2026.md

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.09389 |
| sha256 | `dd95ed9cd9c61d4de04ba622470e4d3e1b14233ceb755464e88a4527d6d78673` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.09389-regret-equilibrium-and-learning-in-games-a-guide.pdf` |
| retrieved | 2026-08-11 |

## Narrative

Mertikopoulos (Univ. Grenoble Alpes / Inria, 44 pp) — an entry-point guided tour of **learning in games**. Two complementary viewpoints: (1) the **single-agent/unilateral** setting — a learner playing against Nature in an unknown, non-stationary, possibly adversarial environment, minimizing regret (basis of the adversarial multi-armed bandit problem, AdvMAB); (2) the **multi-agent/game-theoretic** setting — several myopic agents in a repeated game who adjust to each other's play on the fly, with the central question of whether learning converges to Nash equilibrium.

Unified framework: **regularized learning** — best-respond to the history of play up to a regularization penalty that encourages exploration and prevents over-commitment. Covers fictitious play (FP), follow-the-regularized-leader (FTRL), EXP3, Tsallis-INF, and both oracle (full payoff-vector) and bandit (payoff-only) feedback. Includes an ergodic equilibrium convergence result for zero-sum games in the spirit of fictitious play, and a "folk theorem" linking Nash equilibria to attracting points of regularized learning. Notes PPAD-completeness of NE computation and Hart & Mas-Colell's no-uncoupled-dynamics impossibility; EXP3 dynamics avoid mixed NE and are attracted only by strict NE.

**Routing:** poker Arena researcher-track reference — regret/equilibrium framing for opponent modeling and tournament strategy; concept-only, no live betting.

[Source: arXiv:2608.09389]
