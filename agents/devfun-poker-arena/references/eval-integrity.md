# Eval integrity (CCC K277 + light K280 + light K281)

**Dual-ID:**
- CCC K277 = Labels ≠ endpoints / measurement integrity (2608.12880) ← this ref
- CCC K278 = InterSAGE (2608.13030) — SKIP poker
- CCC K279 = MARC-v1 (2608.13476) — SKIP poker (clinical OOD)
- CCC K280 = Vero (2608.13522) ← light joint outcome+verification
- CCC K281 = AutoDesign (2608.13560) ← light external/HITL pass criteria
- Cybersec K277 = RSM (2608.12311) → `references/rsm-helper-roles.md` (already wired)
- Cybersec K278 = ATOBench (2608.12996) → `references/atobench-verification-chain.md`

**Code:** `examples/eval_integrity.py`
**Tests:** `tests/test_eval_integrity.py`

## Steal

Keep arena/scoring honest — **eval integrity, not EV**:

1. **Treatment-blind grading** — `strip_treatment(record)` removes
   `treatment` / `arm` / `is_treatment` / … before a grader assigns a class;
   relabeling `arm` on otherwise identical `executed_behavior` must not
   change the grader view.
2. **Labels ≠ endpoints** — a label ("win", "attack", "qualified") is not a
   behavioral endpoint. `bind_endpoint(record)` binds the five Integrity
   Chain links (`treatment_bytes`, `executed_behavior`, `authorization`,
   `outcome_rule`, `analysis_unit`) before interpreting a label; a
   label-only record fails-closed.
3. **Joint outcome + verification** (K280 light) — `joint_score(outcome,
   verification)` is ok only when both are truthy **and** verification is not
   self-report (`"yes"` / `"self-report"` / same object as `self_report`).
   Outcome-only and verification-only are both not ok.
4. **External / HITL pass criteria** (K281 light) — `assert_external_pass_criteria`
   requires `owner ∈ {hitl, external}`; rejects `harness` / `self` /
   `optimizer` (`closed_loop`), a missing owner (`missing_owner`), and a
   scorer rewriting its own pass bar (`mutated_by == scorer_id` →
   `self_rewrite`).

Scope honesty: campaign counts are not population EV / model-ranking claims.
All functions are pure and never raise — return `{ok, ...}` dicts.

## Do not

- Clone Vero, MARC-v1, AutoDesign, or InterSAGE — pattern only.
- Hook these into live `decide()` — offline eval helpers only.
- Treat paper numbers as poker chip EV — they are not.
- Let the harness rewrite its own scoring rubric (closed loop).

## Check

```bash
uv run pytest tests/test_eval_integrity.py -q --tb=short
```
