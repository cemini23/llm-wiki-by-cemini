---
title: Multi-Agent Fictitious Play (MAFP) for LLM decisions
type: concept
tags: [concept, llm-agents, game-theory, poker, k124]
keywords: [MAFP, fictitious play, stance entanglement, tournament strength, robustness]
related:
  - sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md
  - concepts/garip-running-average-self-play.md
  - sources/arxiv-garip-self-play-2606.22688-2026-06-23.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/team-zero-sum-games-complexity.md
  - concepts/extensive-form-games-stochastic-action-sets.md
  - concepts/projected-exploitability-descent.md
  - sources/arxiv-projected-exploitability-descent-2606.29169-2026-06-30.md
  - concepts/exact-multiplayer-nash-computation.md
  - sources/arxiv-quadratic-programming-nash-2509.25618-2026-07-04.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/projected-exploitability-descent.md
  - sources/arxiv-projected-exploitability-descent-2606.29169-2026-06-30.md
  - sources/arxiv-2608.15258-self-fictitious-play-2026-08-18.md
maturity: draft
created: 2026-06-20
updated: 2026-07-04
---

## Relations

- @sources/arxiv-mafp-fictitious-play-2606.19308-2026-06-20.md — primary source (Shen et al., NUS)
- @concepts/garip-running-average-self-play.md — K127 gradient self-play magnet (orthogonal to MAFP stance play)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — multi-stakeholder poker eval
- @concepts/projected-exploitability-descent.md — K136 FP-PED hybrid for multiplayer toy games
- @concepts/exact-multiplayer-nash-computation.md — K143 exact-solver baseline literacy for small multiplayer imperfect-info games
- @concepts/devfun-researcher-track-readiness-2026-06.md — Researcher Round target

## Raw Concept

Prompted by arXiv **2606.19308** (K124). **Stance entanglement** — mutually dependent stakeholder decisions — breaks divide-and-conquer MAS. **MAFP** applies fictitious play: each stance-agent best-responds to the empirical mixture of others' prior policies.

## Narrative

**Operators:**
1. **Aggregation** — build empirical mixture over past language policies
2. **Best-response** — generate utility-maximizing policy against mixture

**Metrics:** tournament strength + robustness (vs adaptive exploiters) — complementary to Raeth **axis profile** (how) vs chips (how much).

**Poker steal (offline):**
- Stance agents = villain archetypes (rock / lag / maniac) + hero seat constraints
- Iterative best-response refines preflop charts before locking Researcher submit
- Pairs with K122 axis gates — fictitious play reduces **exploitability** axis hole

**Not in scope:** runtime multi-LLM call chain on Arena action deadline — offline chart synthesis only unless latency spike passes dry-run.

**Posture:** **REFERENCE** — brief to poker-arena; no prod scp.

**K143 note:** exact NCP/QP solvers are complementary to MAFP rather than replacements. MAFP is a language-policy/stance iteration pattern; K143 exact solvers are small-game ground-truth tools that can sanity-check toy abstractions before any chart logic graduates into Arena-facing heuristics.

## Snippets

> "A good decision maximizes payoff while exhibiting no exploitable weaknesses … lies in an equilibrium." [Source: arXiv:2606.19308 §1 (retrieved 2026-06-20)]

## Dead Ends

- 13-scenario eval uses open language policies — PokerKit requires discrete {fold,call,raise} mapping layer.
