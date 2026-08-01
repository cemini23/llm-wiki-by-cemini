# CoGate — confidence-gate side advisors (K231)

Steal from arXiv 2607.28529 / CCC Phase-1 policy. Applies when a **side model**
(security, verifier, LLM coach) can veto or steer `decide()`.

## Rule

1. Require a confidence threshold before advisor veto/steer.
2. Low confidence → log + pass through primary policy (do not force "secure"/coach override).
3. Eval advisors on OOD spots, not only familiar patterns.

## Arena status (2026-08-01)

- Primary `cemini_decide` is heuristic (no LLM system prompt path).
- No live security-advisor side model in the lobby loop.
- If a coach/verifier is added later: gate influence on confidence; keep frozen control arm.

## Sources

- `briefs/2026-07-31_k231-secure-codegen-confidence-steal.md`
- CCC `.cursor/rules/cemini-phase1-policy-wires.mdc` (K231)
