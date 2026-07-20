---
title: K177 — AR bugs + behavioral controllability (poker light steal)
type: brief
target: Poker Arena
created: 2026-07-20
updated: 2026-07-20
---

## Target

`agents/devfun-poker-arena/`

## Summary

arXiv 2607.15684 (agent-reactive bugs) + 2607.15715 (behavioral controllability IE): silent model–harness failures and process-trace eval. Light steal for decide()/capability-tree regressions — not a pin change.

## Body

1. Add AR-class fixtures where a pinned model output elicits wrong tool / submit routing without crash.
2. Prefer process-level oracles (tool calls, retries, recovery) over log-match alone when evaluating harness changes.
3. No new Active pin / no decide() heuristic swap from this batch.
4. Continue texassolver / play-adequacy gates from K173.

## Sources

- arXiv 2607.15684
- arXiv 2607.15715
- OSINT concepts/agent-reactive-bugs.md
