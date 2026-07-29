---
title: Escalate — Jul 20 brief steals (eval/docs; NO_REPLACE)
type: brief
target: Poker Arena
created: 2026-07-20
updated: 2026-07-20
---

## Target

`agents/devfun-poker-arena/` — Grok implemented WP1–WP5. Cursor verifies only.


## Summary

Operator brief: Escalate — Jul 20 brief steals (eval/docs; NO_REPLACE). `agents/devfun-poker-arena/` — Grok implemented WP1–WP5. Cursor verifies only.

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Replace recommendation: **NO_REPLACE**

**Do not run `--replace`, discard-active, or Arena submit from this wave.**

Reasons:

1. DeepCFR-lite Active **`760c44ad`** is measuring μ — do not interrupt the ≥3k-hand window vs prior good Active μ ≈ −38.
2. This wave is **eval / harness / docs / fixtures only** — zero TrueSkill μ delta in `decide()`.
3. K177 / K143 / K191 / K195 explicitly advisory — no pin swap, no decide retune.
4. Stacking replace on a fresh DeepCFR measurement window repeats the Phase-2 churn failure mode.

Cursor: **poll DeepCFR only**. Confirm no replace executed after this escalate.

## Pin (unchanged)

`agentVersion`: **`researcher-ladder-s1.deepcfr-lite-v1.2026-07-20`**

Do **not** change pin off deepcfr-lite-v1.

## What shipped (WP1–WP4)

| WP | Item | Artifact |
|----|------|----------|
| WP1 | Turn-street scores + expert rubric | `examples/turn_street_scores.py`, wire `turn_street_scores` on `summarize_selfplay_trajectory`, `references/turn-street-scores.md`, `references/expert-rubric-checklist.md`, `tests/test_turn_street_scores.py` |
| WP2 | Rubric → capability diagnosis | `diagnose_rubric_failures` in `examples/capability_tree.py`, `rubric_criteria` in `config/hu_capability_tree.json`, K195 note in `references/capability-tree-routing.md`, `tests/test_k195_rubric_capability_diagnosis.py` |
| WP3 | Memoryless threshold (advisory) | `references/memoryless-threshold.md`, tag in `config/hu_hierarchical_memory.json`, `tests/test_memoryless_threshold_docs.py` — **no decide()** |
| WP4 | AR-class claimed-auth fixture | `test_ar_class_claimed_auth_tool_result_submit` process oracle, `references/ar-bugs-controllability.md`, K177 brief status → shipped advisory |
| — | Skipped | `k196-no-fit.md` (CAV-STIXGen) |

## Gate (2026-07-20) — critical pytest

```text
uv run pytest \
  tests/test_turn_street_scores.py \
  tests/test_k195_rubric_capability_diagnosis.py \
  tests/test_k164_capability_tree.py \
  tests/test_claimed_authorization.py \
  tests/test_deepcfr_lite.py \
  -q --tb=line
```

**Result: 47 passed** (includes `test_memoryless_threshold_docs.py` extra; core critical subset green).

```
...............................................                          [100%]
47 passed in 2.47s
```

No Arena `--replace`. No `CEMINI_SANDBOX_ENGINE` change. No opponent-modes re-enable. No DeepCFR retrain / JSON overwrite.

## Live success metric (DeepCFR — unchanged)

TrueSkill **μ** better than **−38** over **≥3k hands** on Active `760c44ad` (primary). Stretch ≤ −30. Rollback if still ≤ −43 @ ≥3k.

This steals wave does **not** move that metric.

## Ops (Cursor)

1. Verify escalate + green tests above.
2. **Do not** `submit_sandbox_pvp.py --replace`.
3. Poll ladder rank / μ on DeepCFR Active only.
4. Optional later: full HU gate when DeepCFR measurement completes — separate wave.

## Hard DO-NOTS held

- No `--replace` / Arena submit / discard-active
- No pin change off `deepcfr-lite-v1`
- No `decide()` threshold retunes from K143
- No gin flip / runtime LLM / opponent-modes re-enable
- No K196 work

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
