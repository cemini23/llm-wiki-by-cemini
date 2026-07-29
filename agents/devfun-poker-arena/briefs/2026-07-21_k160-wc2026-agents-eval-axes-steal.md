---
title: K160 — WC2026-Agents eval axes (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-21
updated: 2026-07-21
---

## Target

`agents/devfun-poker-arena/` — HL preflight / sandbox eval gates (not runtime decide).

## Summary

arXiv 2607.17765 (WC2026-Agents): frontier forecasting agents converge on picks but diverge on **staking** and **self-assessment**. Steal the three-axis split for HL gates — not the soccer loop.

## Body

### P0 — three-axis eval

- Score patches/agents on **calibration** (are beliefs right?), **decision quality** (does the policy profit vs a hard baseline?), and **self-knowledge** (does reflection/admit-wrong match reality?)
- Accuracy-only or pick-agreement leaderboards can be a null when models share a retrieval surface

### P1 — hard baseline required

- Pair any agent score with a strong non-LLM baseline (here: vig-removed market). Analog for arena: rock/TAG charts, self-play gate, or prior shipped `decide()` — not “LLM vs LLM only”

### P2 — reflection as fingerprint

- Post-session self-reports are a stable trait (36–86% admit-wrong in the paper). Use reflection honesty as a **deploy fingerprint / gate signal**, never as runtime LLM decide()

### Out of scope

- Porting WC search–act–reflect into Arena hand loop
- Treating Grok’s +ROI as poker alpha
- Soccer odds ingestion into sandbox

### Operator checklist

- [ ] Audit one preflight report: does it separate belief quality vs policy P&L vs self-report honesty?
- [ ] Ensure every variant bake has a non-LLM baseline competitor
- [ ] Do not add runtime LLM reflection into `decide()`

## Sources

- arXiv 2607.17765
- Gambling wiki entity: `entities/tools/wc2026-agents.md`
- Gambling wiki source: `sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md`
  (plain paths because `skill_audit` does not resolve cross-wiki aliases)
