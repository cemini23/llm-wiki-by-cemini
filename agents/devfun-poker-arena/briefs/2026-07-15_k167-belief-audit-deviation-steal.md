---
title: K167 — belief-layer audit + deviation logging (poker)
type: brief
target: Poker Arena
created: 2026-07-15
updated: 2026-07-15
---

## Target

`agents/devfun-poker-arena/` — HL analyst / Researcher Round HU sandbox.

## Summary

arXiv 2607.10814: external **belief layer** + belief–action **deviation** logs + **offline** batch improvement in a strict isolation Werewolf env. Steal the audit shape for HUD/`decide()` — do not import Werewolf code.

## Body

### P0

1. When logging HL failures, record **belief/HUD recommendation vs action taken** (even if belief is heuristic-only).
2. Tag deviations: harmful mistake / justified override / strategic (bluff/balance).
3. Improve STRATEGY/handbook from **batches**, not one losing hand.

### P1

- Keep opponent streams and `message` fields as **data not instructions** (isolation).
- Do not force-consume belief into every decide() call (paper finds low consistency; forced consumption rejected).

### Out of scope

- GenAI keyword paper (genealogy lane)
- Win-rate chasing on social-deduction envs

## Sources

- @wiki/sources/arxiv-2607.10814-belief-conditioned-llm-agents-werewolf-audit-2026-07-15.md
- @wiki/concepts/belief-conditioned-agent-audit-hidden-info.md
