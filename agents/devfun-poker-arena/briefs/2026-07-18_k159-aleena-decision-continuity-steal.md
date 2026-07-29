---
title: K159 — Aleena decision continuity (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-18
updated: 2026-07-18
---

## Target

`agents/devfun-poker-arena/` — HL analyze→patch→preflight trail; sandbox session notes.

## Summary

arXiv 2607.08043 (Aleena): lifecycle alignment agents preserve **decisions, risks, and open questions** as structured GitHub-shaped artifacts. Steal the schema for HL patch sessions — not the full web stack.

## Body

### P0 — structured session trail

- After each analyze/patch cycle, leave fields: `summary`, `decisions`, `action_items`, `risks`, `open_questions`
- Prefer concrete spot names / blockers / next steps; never invent facts from the transcript or chat

### P1 — vocabulary drift

- When heuristic / Arena terms get redefined across sessions, flag **conflict** vs duplicate definitions before shipping a patch

### P2 — human-gated code changes

- Draft patch / PR only when the action item is code-shaped; human review + merge; runtime `decide()` stays zero LLM

### Out of scope

- Running Aleena web/Pixi stack in the arena loop
- Vendoring while LICENSE TBD
- Memory Scarcity paper (infra macro; CCC only)

### Operator checklist

- [ ] Add a lightweight decisions/risks/open-questions stub to HL patch notes
- [ ] Audit one recent session for lost open questions
- [ ] Revisit when `uw-ssec/Aleena` adds SPDX

## Sources

- arXiv 2607.08043
- Gambling wiki entity: `entities/tools/aleena.md`
- Gambling wiki source: `sources/arxiv-2607.08043-aleena-alignment-agent-2026-07-18.md`
  (plain paths because `skill_audit` does not resolve cross-wiki aliases)
