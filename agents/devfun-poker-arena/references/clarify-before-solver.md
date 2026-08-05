# Clarify-before-solver (K244)

Ask / require street + stack + inference regime **before** launching solver
or helper fan-out. A solver run against an incomplete observation produces a
compare artifact, not a decision.

## Steal

1. `solver_inputs_ready(table)` returns the list of missing inputs (street,
   stack/chips, inference_regime or table format). When non-empty,
   `retrieve_solver_context` returns a small skip dict
   (`{"solver_preflight": "skip", "missing": [...]}`) instead of launching
   heavy solver helpers. Fail-open: any preflight weirdness keeps the normal
   path.
2. Final numeric claims must align with solver/tool output — reuse
   `solver_context_prune.assert_solver_grounded` (K199) for the
   narrate-only contract; do not duplicate it here.

## Do not

- Treat a skipped solver context as an EV claim — the skip dict is a signal
  for the compare harness, not a decision
- Dump more MCP/tools onto instruction-only helpers expecting uplift (K245)

## Sources

- arXiv 2608.03018 (K244)
- `examples/solver_preflight.py`
- `examples/solver_context_prune.py` (K199/K201)
- `briefs/2026-08-05_k244-k245-steal.md`
