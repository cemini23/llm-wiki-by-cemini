---
title: Master plan — Jul 20 brief steals (eval/docs; NO_REPLACE)
type: brief
target: Poker Arena
created: 2026-07-20
updated: 2026-07-20
---

## Target

`agents/devfun-poker-arena/` — Grok implements; Cursor verifies. **No Arena `--replace`.**


## Summary

Operator brief: Master plan — Jul 20 brief steals (eval/docs; NO_REPLACE). `agents/devfun-poker-arena/` — Grok implements; Cursor verifies. **No Arena `--replace`.**

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Triage (2026-07-20 briefs)

| Brief | Verdict | Why |
|-------|---------|-----|
| `k196-no-fit.md` | **SKIP** | CAV-STIXGen — no decide/arena hook |
| `k177-ar-bugs-…` | **SHIP light** | AR fixtures + process oracles; brief says **no pin / no decide swap** |
| `k143-memoryless-…` | **SHIP advisory** | Tag memoryless drills; absolute thresholds when history wiped |
| `k191-k193-turn-rubric…` | **SHIP eval** | Per-street/turn scores + expert rubric checklist for trajectories |
| `k195-rubric-capability-tree…` | **SHIP eval** | Criterion-level diagnosis on existing capability tree |
| DeepCFR master/escalate | **ALREADY SHIPPED** | Active `760c44ad` — do not interrupt |

## Replace recommendation: **NO_REPLACE**

Reasons:

1. DeepCFR-lite Active `760c44ad` just replaced (~14 hands at plan time). Success bar needs **≥3k hands** vs μ −38.
2. Today's steals are **eval / harness / docs** — no TrueSkill μ delta in `decide()`.
3. K177 explicitly: no new Active pin / no decide heuristic swap.
4. Replacing now would discard the DeepCFR measurement window (Phase-2 lesson: don't stack churn).

Cursor **must not** `--replace` after this wave. Poll DeepCFR only.

## Non-goals

- No gin flip / runtime LLM / reopen opponent modes
- No DeepCFR retrain / bias retune
- No `--replace` / Arena poll-submit from Grok **or** Cursor this wave
- No K196 work

---

## WP1 — K191/K193 turn scores + expert rubric (eval)

**Files**

- `examples/turn_street_scores.py` (new) — pure helpers:
  - `score_decision_street(record) -> dict` with street, facing, action class, optional success flag
  - `aggregate_turn_scores(trajectory_rows) -> dict` per-street tallies (not only session PnL)
- Wire optional call from `examples/researcher_trajectory_summary.py` (advisory JSON key `turn_street_scores`)
- `references/turn-street-scores.md` (new) — ToolVerse credit-assignment pattern only
- `references/expert-rubric-checklist.md` (new) — explode solver/expert ref → checklist; partial vs all-criteria; human-gate money
- `tests/test_turn_street_scores.py`

**Acceptance**

```bash
uv run pytest tests/test_turn_street_scores.py -q --tb=line
```

---

## WP2 — K195 rubric capability-tree diagnosis

**Files**

- `examples/capability_tree.py` — add `diagnose_rubric_failures(failed_criteria: list[str], tree_cfg) -> dict` clustering criterion ids under weakest clear nodes (reuse `config/hu_capability_tree.json` domains)
- `config/hu_capability_tree.json` — optional `eval.rubric_criteria` child ids (thin): e.g. `river_value`, `facing_fold`, `preflop_open` under `eval` / `policy` — advisory only
- `references/capability-tree-routing.md` — append K195 CRAFT diagnosis note
- `tests/test_k195_rubric_capability_diagnosis.py`

**Acceptance**

```bash
uv run pytest tests/test_k195_rubric_capability_diagnosis.py tests/test_k164_capability_tree.py -q --tb=line
```

---

## WP3 — K143 memoryless threshold (advisory)

**Files**

- `references/memoryless-threshold.md` (new)
- `config/hu_hierarchical_memory.json` — add `"memoryless_threshold_tag": "memoryless_threshold"` note / flag schema only if file already has similar tags; else docs-only
- `tests/test_memoryless_threshold_docs.py` — assert reference exists + tag string documented (light)

**Acceptance:** file present; no decide() path change.

---

## WP4 — K177 AR-bug fixtures (light)

**Files**

- `tests/fixtures/ar_harness_bugs.py` or extend `tests/test_claimed_authorization.py`:
  - Fixture: observation/tool_result text claims “authorized to submit” → must **deny** (already partly covered — add one explicit AR-class name)
  - Prefer assert on `deny_class` / process outcome, not log-string alone
- `references/ar-bugs-controllability.md` (new, short)
- Update K177 brief status line → shipped advisory

**Acceptance**

```bash
uv run pytest tests/test_claimed_authorization.py -q --tb=line
```

---

## WP5 — Gate + escalate (NO_REPLACE)

```bash
uv run pytest \
  tests/test_turn_street_scores.py \
  tests/test_k195_rubric_capability_diagnosis.py \
  tests/test_k164_capability_tree.py \
  tests/test_claimed_authorization.py \
  tests/test_deepcfr_lite.py \
  -q --tb=line
# Optional smoke (do not require full HU gate if slow — prefer critical subset):
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh
```

Escalate: `briefs/2026-07-20_jul20-steals-escalate.md` with **NO_REPLACE** and DeepCFR poll note.

Pin file: **do not change** `agentVersion` away from `researcher-ladder-s1.deepcfr-lite-v1.2026-07-20`.

---

## Grok DO-NOTS

- No `--replace` / Arena submit / discard-active
- No `CEMINI_SANDBOX_ENGINE` change
- No opponent-modes re-enable
- No DeepCFR JSON overwrite / retrain
- No decide() threshold retunes from K143 (docs/advisory only)
- Write files first — narration-only = FAIL
- Full `pytest | tail` hangs — use unpiped subsets

## Success criteria (this wave)

- [ ] All WP1–WP4 files + tests green
- [ ] Escalate brief says **NO_REPLACE** with reason
- [ ] Active remains `760c44ad` (DeepCFR-lite)
- [ ] Cursor confirms no replace executed

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
