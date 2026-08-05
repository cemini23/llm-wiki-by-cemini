## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-31_k230-k233-model-when-radio-steal.md).

# CCC→Poker K230/K231/K232 — memory reconstruct + when-to-model + multi-agent radio

**From:** CCC ingest 2607.28272 / 2607.28287 / 2607.28430

## Summary

Past-hand snippets need state-conditioned rewrite; don't auto-build solvers/sims on every miss; parallel agents need mid-hand awareness.

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.

## Steal

1. Session memory / prior-hand notes: reconstruct for current street/stack — don't verbatim-replay unrelated spots (K230).
2. Solver/world-model use: actor-requested or advantage-gated build/repair/bypass — sim match ≠ EV-useful (K231 / Tycho).
3. Multi-agent Arena helpers: non-blocking inbox so mid-task findings can correct peers (K232).
4. EV/numbers still solver-grounded (K199).

## Sources

- Internal Arena ops briefs under `agents/devfun-poker-arena/briefs/`

## Phase-1

CCC wired these as always-on policy in `.cursor/rules/cemini-phase1-policy-wires.mdc`. Arena operators: apply the Steal bullets above in session prompts; no Harbor/Modal AgentRadio runtime.
