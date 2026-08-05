# Test-time scaling inference regimes (K152)

Name the regime before comparing decide() variants. Longer CoT, best-of-N +
vote/verify, and tree search are **not interchangeable** under one "thinking
budget" — report protocol-matched cost, not a single token number.

## Regimes

1. **sequential** — one evolving thought stream / adaptive stop.
2. **leaf_reduce** — sample N complete actions, then vote / verifier / MBR.
   `CEMINI_VERIFIER_BON` is this regime.
3. **prefix_search** — ToT-style partial action trees.

## Steal

1. Tag `retrieve_solver_context` output with the active regime so HU sandbox
   compares can read it and report protocol-matched cost (tokens on one
   trajectory vs N complete candidates vs expanded prefixes).
2. Default label is `sequential` unless `CEMINI_VERIFIER_BON` is truthy
   (`leaf_reduce`); only label `prefix_search` when an existing tree/ToT flag
   is already on — do not invent new solver trees.

## Do not

- Claim "more tokens = TTS win" without naming the regime
- Pull Scorio HF traces onto laptop or prod
- Auto-scp to cemini-prod

## Sources

- arXiv 2608.04001 (test-time scaling taxonomy)
- `briefs/2026-08-05_k152-tts-inference-regimes-delta.md`
- `examples/inference_regime.py`
