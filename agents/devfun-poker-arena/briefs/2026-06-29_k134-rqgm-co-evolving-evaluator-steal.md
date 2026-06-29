## Target

`agents/devfun-poker-arena/` — Researcher Round verifier / sandbox tri-verifier stack.

## Summary

K134 **RQGM** (2606.26294): steal **controlled utility evolution** — versioned rubric epochs, GT-gated evaluator promotion, selective erasure of stale trajectory scores — for sandbox regression without full Gödel tree search.

## Body

### P0 — rubric versioning (schema only)

1. Add `rubric_epoch` + `evaluator_id` fields to `sandbox_tri_verifier_schema.json` reports.
2. **Frozen epoch:** tri-verifier weights fixed for one submit generation batch.
3. **Promotion gate:** new challenger weights ship only if hold-out spot suite pass rate ↑ vs incumbent on PokerKit oracle (ε-best-belief style threshold — advisory first).

### P1 — selective erasure

- When `rubric_epoch` bumps, mark prior sandbox LB rows `superseded_by_epoch` (do not delete raw trajectories).
- Align with K132 tri-verifier + K131 Relaxed NFL DecideTrace deferred work.

### P2 — adversarial epoch (optional)

- If LLM judge over-accepts reasoning YAML vs harness legality, run debiasing epoch (RQGM §5.4 pattern) — log only initially.

### Out of scope

- Full Thompson-sampling archive tree (RQGM §3.1)
- Scientific-paper reviewing domain experiments

## Sources

- @wiki/sources/arxiv-red-queen-godel-machine-2606.26294-2026-06-29.md
- @wiki/concepts/red-queen-controlled-utility-evolution.md
- @wiki/concepts/generator-verifier-inference-time-steering.md
- [Source: https://arxiv.org/abs/2606.26294 (retrieved 2026-06-29)]
