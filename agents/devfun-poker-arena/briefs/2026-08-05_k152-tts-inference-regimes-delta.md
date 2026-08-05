---
title: K152 — TTS inference regimes delta (poker sandbox)
type: brief
target: Poker Arena
created: 2026-08-05
updated: 2026-08-05
---

## Target

`agents/devfun-poker-arena/` — `cemini_decide` / HL analyst loop.

## Summary

Thin steal from **test-time scaling taxonomy** (arXiv 2608.04001): longer CoT, best-of-N + vote/verify, and tree search are **not interchangeable** under one “thinking budget.”

For HU sandbox: when comparing decide() variants, tag the inference regime and report protocol-matched cost (tokens on one trajectory vs N complete candidates vs expanded prefixes).

## Body

### P0 — name the regime

1. Sequential: one evolving thought stream / adaptive stop
2. Leaf + reduce: sample N complete actions, then vote / verifier / MBR
3. Prefix search: expand partial action trees (ToT-style)

### Do not

- Claim “more tokens = TTS win” without saying which regime
- Pull Scorio HF traces onto laptop or prod
- Auto-scp to cemini-prod

## Filed (2026-08-05)

- `references/tts-inference-regimes.md` (K152)
- `examples/inference_regime.py`
- `tests/test_inference_regime.py`
- Regime tag wired into `cemini_decide.retrieve_solver_context` return (fail-open)

## Sources

- https://arxiv.org/abs/2608.04001
- `@seo-wiki/sources/arxiv-hariri-2026-test-time-scaling-reasoning-llms-2608.04001-2026-08-05.md`
