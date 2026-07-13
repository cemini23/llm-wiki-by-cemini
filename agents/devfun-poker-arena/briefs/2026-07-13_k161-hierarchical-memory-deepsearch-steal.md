---
title: K161 — hierarchical memory + DeepSearch trajectory filter (poker sandbox)
type: brief
target: Poker Arena
created: 2026-07-13
updated: 2026-07-13
---

## Target

`agents/devfun-poker-arena/` — Researcher Round HU sandbox / HL analyst loop.

## Summary

Two steals: (1) **Ensemble QSP hierarchical memory** (2607.07666) — capped mid-term project-state + eviction so session context stays ~O(1) tokens; (2) **DeepSearch-Evolve** (2607.07820) — generate→filter→mix trajectories in a verifiable env without teacher distillation.

## Body

### P0 — hierarchical session memory

- Keep **short-term**: last N hands + scratchpad facts (stack, HUD tags).
- Keep **mid-term**: capped session JSON (active goals, last 3 session summaries, recent jobs) — **evict** completed drills.
- Keep **long-term**: strategy handbook / yardstick docs (already in `references/`).
- **Do not** dump full Arena trajectories into `decide()` or HL prompts.

### P1 — trajectory filter/mix (DeepSearch analogy)

- When mining sandbox failures: require **progress verification + grounded reflection + failure recovery** tags before mixing into training/eval sets.
- Drop ungrounded reflection / teacher-imitation-only traces.
- DeepSearch code release is **Watch** — steal the loop shape only until env lands.

### Out of scope

- Quantile DRL theory (2607.08444) — shelf
- Psychological competence (coach UX) — TipDrop/David lane

## Sources

- @wiki/sources/arxiv-hierarchical-memory-ensemble-qsp-2607.07666-2026-07-13.md
- @wiki/sources/arxiv-deepsearch-world-2607.07820-2026-07-13.md
- @wiki/concepts/hierarchical-bounded-agent-memory.md
- @wiki/concepts/deepsearch-world-self-evolution.md
