# VAKRA eval axes (CCC K275)

**Dual-ID:**
- CCC K275 = VAKRA (2608.12282) ← this ref
- CCC K274 = CDH (2608.12273) → `references/cdh-skill-budget.md`
- CCC K276 = RSM (2608.12311) → `references/rsm-helper-roles.md`
- Cybersec K276 = withhold contract (2608.12292) → `references/withhold-contract.md`
- Cybersec K277 = RSM (same 2608.12311) → `references/rsm-helper-roles.md`

**Code:** `examples/vakra_eval_axes.py`
**Tests:** `tests/test_vakra_eval_axes.py`

## Steal

Eval helper agents on **reasoning depth + NL policy constraints**, not tool
mechanics — VAKRA failures sit at entity disambiguation / cross-source
grounding. A helper-eval claim must state its axes explicitly:

1. `api_paradigm` — `endpoint` vs `compositional`
2. `reasoning_hops` — int 2–5 (out of range → flagged incomplete)
3. `multi_source` — bool
4. `nl_policy_constraint` — bool
5. `reexec_verified` — bool; re-execution evidence, **not self-report**
   (a `"yes"` string is invalid)
6. Policy-constrained / unanswerable queries must be present for a
   "complete" helper-eval claim.

`score_eval(record)` → `{complete, missing, notes}`. Local checklist only —
no network, no HF dataset download.

## Do not

- Clone `IBM/vakra` (CC-BY-NC-SA 4.0) — methodology only.
- Download the VAKRA HF dataset — WATCH only.
- Treat paper metrics as poker chip EV — they are not.
- Accept self-reported re-exec as verification.

## Check

```bash
uv run pytest tests/test_vakra_eval_axes.py -q --tb=short
```
