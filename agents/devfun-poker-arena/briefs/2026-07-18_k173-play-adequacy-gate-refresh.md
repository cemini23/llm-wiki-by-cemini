---
title: K173 — play-adequacy gate refresh (2607.14169)
type: brief
target: Poker Arena
created: 2026-07-18
updated: 2026-07-18
---

## Target

`agents/devfun-poker-arena/` — HL preflight / sandbox eval / opponent sims.

## Summary

Full PDF ingest of arXiv 2607.14169 (concept now on OSINT wiki). Reinforces K158 steal: transition-accuracy alone is the wrong ship criterion; prefer play-adequacy / search-visited regressions.

## Body

### P0

- Keep play-adequacy gates ahead of log-match / transition accuracy in sandbox ship checks.
- Rare pivotal leaks need adversarial or competent-play samples.

### P1

- Spec completeness > more similar hand dumps when a rule is missing from coded heuristics.

### Out of scope

- Vendoring CWM planners as runtime decide()
- Full multi-model synthesis burns

## Sources

- Local wiki concept `play-adequacy-vs-prediction-accuracy` (OSINT K173)
- Prior brief `2026-07-17_k158-play-adequacy-gate-steal.md`

