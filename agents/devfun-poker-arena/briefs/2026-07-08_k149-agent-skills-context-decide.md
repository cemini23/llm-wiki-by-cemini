---
title: K149 — context-engineering skills for cemini_decide
type: brief
target: Poker Arena
created: 2026-07-08
updated: 2026-07-08
---

## Target

dev.fun Poker Arena — `agents/devfun-poker-arena`.

## Summary

Steal K149 **Agent-Skills-for-Context-Engineering** (MIT) patterns for multi-hand `cemini_decide` sessions: scratchpad offload of betting history, latent briefing to worker evaluators — reduce lost-in-the-middle over long HU trajectories.

## Body

### P0

1. Map current trajectory memory vs filesystem scratchpad suggestion.
2. Spike evaluator rubric offload for nine-axis checks without bloating decide() prompt.

### Out of scope

- Managed Anthropic multi-agent rewrite of the sandbox loop

## Sources

- OSINT `@entities/tools/agent-skills-for-context-engineering.md`
- OSINT `@sources/eval-url-revenue-plan-20url-2026-07-08.md`
