---
title: K156 — AgentTexasPoker risk spectrum (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-15
updated: 2026-07-15
---

## Target

`agents/devfun-poker-arena/` — Researcher Round HU / Playground HL loop / AI-opponent panels.

## Summary

arXiv 2607.10251 + AgentTexasPoker: frontier LLMs show **stable VPIP/PFR risk spectra** and **heterogeneous plasticity** when blinds or stacks change. Steal for opponent tagging and pressure-aware gates — not for copying GPT aggression into `decide()`.

## Body

### P0 — risk-spectrum tags for AI / sandbox foes

Map opponents on:

- **Participation (VPIP)** — willingness to enter uncertain pots
- **Proactiveness (PFR)** — preflop escalation

Expect extremes to diverge further in mixed pools (conservatives tighten harder; aggressors take volume). Homogeneous self-play WRs look similar while strategies differ — don't rank agents by self-play alone.

### P1 — pressure-band gates

When BB burns stack (or short-stack focal):

- Retest open/3-bet gates under high-pressure bands
- Separate **entry** contraction from **raise** contraction (selective de-escalation pattern)
- Near-invariant opponents won't self-correct — exploit stuck ranges

### P2 — decide() JSON hygiene

Paper prompt/parser: strict JSON → recover embedded JSON → retry with audit. Mirror in arena logs: parse failure ≠ fold; log retries separately from behavioural actions.

### Out of scope

- Shipping AgentTexasPoker engine into Arena (incompatible protocol)
- Full multi-frontier API tournament burns
- HF dataset bulk download without size check
- Vendoring code while LICENSE TBD

### Operator checklist

- [ ] Add Participation/Proactiveness labels to nemesis / sandbox opponent cards
- [ ] One high-blind gate re-check next HL round
- [ ] Confirm decide() parse/retry counters in monitor

## Sources

- arXiv 2607.10251 (risk-sensitive LLM poker)
- Gambling wiki entity: entities/tools/agent-texas-poker.md
- Gambling wiki source: sources/arxiv-2607.10251-risk-sensitive-llm-poker-2026-07-15.md
  (plain paths — skill_audit does not resolve `@gambling-wiki/` aliases)
