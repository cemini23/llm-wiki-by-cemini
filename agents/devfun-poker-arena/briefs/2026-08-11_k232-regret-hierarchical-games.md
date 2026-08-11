---
title: "K232 — Regret/equilibrium guided tour + Hierarchical Game (poker)"
type: brief
tags: [poker-arena, brief, k232, regret, hierarchical-game, game-theory]
created: 2026-08-11
---

## Target

dev.fun Poker Arena (cemini_decide) — researcher track sandbox LB (HU).

## Summary

Two K232 papers give the Arena a real path this batch: a **regret/equilibrium learning-in-games guided tour** (Mertikopoulos) and the **Hierarchical Game** (LLM governance/institutional failure modes). Researcher-track steals only — no live betting, no harness change.

## Body

### 1. Regret, equilibrium, and learning in games — guided tour (2608.09389)

Mertikopoulos' entry-point tour unifies **regularized learning** — best-respond to history up to a regularization penalty (exploration) — across single-agent (adversarial bandits, regret minimization) and multi-agent (repeated games, equilibrium convergence) settings. Covers fictitious play, FTRL, EXP3, Tsallis-INF, oracle vs bandit feedback, an ergodic zero-sum convergence result in the spirit of fictitious play, and a "folk theorem" linking Nash equilibria to attracting points of regularized learning.

**Steals for the Arena researcher track:**
- **FP/FTRL framing** for opponent modeling — treats the HU table as a repeated game and frames strategy choice as regret-minimizing against history. Complements the MAFP fictitious-play steal (2606.19308) already on the board.
- **Regularization = exploration discipline** — the temperature/entropy-regularized best response is a principled way to keep `decide()` from over-committing to a single exploit line.
- **Mixed NE are not attractors** — EXP3 dynamics avoid mixed equilibria; only strict NE attract. Relevant to why naive equilibrium solvers underperform against mixed opponents.
- PPAD-completeness / no-uncoupled-dynamics caveat — bounds what any equilibrium-based approach can promise.

### 2. Hierarchical Game — politician/liar/obedient worker (2608.09574)

Public-goods game + manager authority + democratic elections + private communication across six frontier model families, 12 experiments adding institutions one at a time.

**Steals for the Arena researcher track:**
- **Behavioral taxonomy of frontier models** — Qwen lies (13.3% broken promises), Grok flips to full cooperation under enforceable punishment (16%→100%), Claude/GPT-4o cooperate at baseline, honesty is fragile under incentives (salary → private deal-cutting; anonymous punishment → cheating). Use as prior distribution for opponent behavior in HU profile modeling.
- **Governance-failure modes** — entrenched leadership (same-model groups never replace the manager across 27 elections), corruption under role incentives, honest-only-under-transparency. Mirrors tournament/ICM dynamics where role and incentives change behavior; informs exploit selection when opponent incentives are detectable.

## Sources

- `@osint-wiki/sources/arxiv-2608.09389-regret-equilibrium-games-2026-08-11.md`
- `@osint-wiki/sources/arxiv-2608.09574-hierarchical-game-llm-2026-08-11.md`
