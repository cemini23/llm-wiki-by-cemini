## Target

`agents/devfun-poker-arena/` — Researcher Round verifier stack.

## Summary

K131 **Relaxed NFL** (2606.24443) + K129 **ForEx** cluster: steal a **two-stage trajectory formalization** — permissive `DecideTrace` JSON → PokerKit elaboration → harness + axis rubric verification — before sandbox submit claims.

## Body

### P0 — schema (no new deps)

1. Define **Relaxed DecideTrace** fields: `{street, action_class, sizing_intent?, rationale?}` — allow omitted chip counts.
2. **Elaboration pass** fills pot/stack via existing PokerKit adapter (deterministic, logged).
3. **Verification kernel**: existing harness tests + hand legality; add fail-closed gate on elaboration mismatch.

### P1 — tie to ForEx pattern

- Read `@wiki/sources/arxiv-forex-lean4-fallacy-detection-2606.21867-2026-06-25.md` — explanation text checked against formal trace (fallacy = axis penalty, not ship blocker initially).
- Optional: log verifier pass rate alongside `match_win_rate` in gate reports (advisory).

### P2 — RLVF (offline only)

- If offline self-play resumes: use harness legality bit as **RLVF-style reward** complement to win/loss — see `@wiki/concepts/rlvf-verifier-feedback-training.md`.
- **Out of scope:** Lean4 / theorem prover integration.

### Out of scope

- Legal-AI domain (2606.23913) — pattern reference only
- ToolBench-X — CCC harness brief

## Sources

- @wiki/sources/arxiv-relaxed-nfl-auto-formalization-2606.24443-2026-06-26.md
- @wiki/sources/arxiv-forex-lean4-fallacy-detection-2606.21867-2026-06-25.md
- @wiki/concepts/relaxed-nfl-auto-formalization.md
- [Source: https://arxiv.org/abs/2606.24443 (retrieved 2026-06-26)]
