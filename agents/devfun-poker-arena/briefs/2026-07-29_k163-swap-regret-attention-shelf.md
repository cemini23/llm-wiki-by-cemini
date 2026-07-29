---
title: K163 — Swap-regret attention / smoothed FP shelf (poker)
type: brief
target: Poker Arena
created: 2026-07-29
updated: 2026-07-29
---

**Shelf confirm** — gambling-wiki ingest twin of arXiv 2607.23333. Operator docs already shipped under **K198** (`references/swap-regret-training-notes.md`). No further decide()/HL work this cycle.

**Status (2026-07-29):** cross-ref + gambling-wiki pointer applied on
`references/swap-regret-training-notes.md`. Shelf closed.

## Target

`agents/devfun-poker-arena/` — MAFP / regret literature shelf only.

## Summary

Park & Ozdaglar: regret-loss single-layer attention recovers smoothed fictitious play; swap-regret loss recovers Blum–Mansour-style CE-seeking updates. Theory shelf next to MAFP + K157 FBSDE FP.

## Body

### Do

- Keep K198 advisory notes linked from league-promotion / play-adequacy reading lists.
- Cross-ref `@gambling-wiki/sources/arxiv-2607.23333-swap-regret-attention-2026-07-29.md`.

### Do not

- Promote swap-regret loss to a Playground submit gate
- Import one-layer attention stationary points into live `decide()`
- FOSS adopt / prod scp / Atto / TipDrop / CeminiDFS (none)

## Sources

- arXiv 2607.23333
- Prior: `briefs/2026-07-28_k198-swap-regret-verifier-gap-steal.md`
- `@gambling-wiki/sources/arxiv-2607.23333-swap-regret-attention-2026-07-29.md`
- `@gambling-wiki/sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md`
