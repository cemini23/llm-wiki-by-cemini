# K170 + timeout harden v2 — escalate brief (2026-07-16)

## Target

CeminiSuite / Arena — Researcher HU ladder S1. **Cursor-owned `--replace` only** after review. Grok implementer: **no `--replace`**.

## Summary

Timeout harden v2 (wider tight band, lower sim caps, earlier SIGALRM, 5s default deadline, import-time cache warm) + K170 MAFP theory shelf cite (arXiv 2607.08861). Engine stays **cemini**. No FBSDE in `decide()`, no gin flip, no runtime LLM.

| Artifact | Result |
|----------|--------|
| Timeout v2 | `deadline_s < 5` tight; sims `>5→250`, `≥3→150`, `<3→40`; guard `min(d-0.5, 4.5, 0.6d)`; default deadline **5.0**; warm MAFP+buckets at harness import |
| K170 cite | `references/mafp-fbsde-theory-shelf.md` + `research/mafp_hu_chart.json` notes contain `2607.08861` |
| Critical pytest | **47 passed** (deadline, wall-clock, mafp wire+K170, postflop, HU ladder guards) |
| HU sandbox gate | **GATE_EXIT:1** — hard fail: `series_win_rate vs lag 40.0% < 45.0%` (same residual as evening-steals; seed=42) |
| Trajectory/axis | **PASS** (M8=0, hierarchical memory ok) |
| tight selfplay | **+42.0** bb/100 (200h) |
| TEN advisory | **+34.2** bb/100 |
| maniac_shark advisory | **+60.8** bb/100 |
| maniac series | **+51.0** bb/100 series_win 60% |
| lag series | **−1.5** bb/100 series_win **40%** (fail gate) |
| Bundle | `dist/sandbox-pvp-bundle.zip` build-only OK (~864 KB) |
| `--replace` | **not run** — `NO_REPLACE=confirmed` |

## Timeout v2 deltas

| Knob | Before (evening WP0) | After (v2) |
|------|----------------------|------------|
| Tight band | `deadline_s < 3` | `deadline_s < 5` |
| Skip under tight | HL / chat / jackpot | + **PokerSkill** |
| Sims `>5s` | 500 | **250** (`CEMINI_LOOSE_DEADLINE_SIMS`) |
| Sims `≥3s` | 350 | **150** (`CEMINI_MEDIUM_DEADLINE_SIMS`) |
| Sims `<3s` | 80 default | **40** (`CEMINI_TIGHT_DEADLINE_SIMS`) |
| SIGALRM guard | `min(d-0.35, 7.5)` floor 0.5 | `min(d-0.5, 4.5, 0.6*d)` floor 0.35 |
| Missing Arena deadline | `CEMINI_DECIDE_DEADLINE_S` default **8.0** | default **5.0** |
| Cache warm | first `decide()` only | harness import: `_hu_chart_for_lookup` + `get_buckets_payload` |

**Files:** `examples/cemini_decide.py`, `harness/strategy.py`, `tests/test_sandbox_deadline_guard.py`, `tests/test_strategy_wall_clock_guard.py`.

## K170 cite path

| Item | Path |
|------|------|
| Theory shelf | `references/mafp-fbsde-theory-shelf.md` |
| Chart provenance | `research/mafp_hu_chart.json` → `solver_provenance.notes` includes `2607.08861` |
| Brief cross-link | `briefs/2026-07-16_k170-fictitious-play-fbsde-theory.md` → shelf done |
| Test | `tests/test_mafp_chart_wire.py::test_k170_mafp_provenance_cites_fbsde_theory_shelf` |

**Hard:** no FBSDE numerics on Arena clock / `decide()` hot path.

## Gate detail

Bundle dir: `reports/researcher-round/gate-hu-20260716T121704Z`

| Check | Status |
|-------|--------|
| HU regression pytest | PASS (2) |
| Substrate K146/K148 | PASS |
| Trajectory `--gate` | PASS |
| tight 200h | +42.0 bb/100 |
| TEN advisory | +34.2 (≥0) |
| maniac_shark advisory | +60.8 (≥0) |
| maniac/lag series audit | **FAIL** lag series_win 40% &lt; 45% |
| yardstick pool | 3/3 pass advisory |
| build-only zip | PASS |

**Note:** Same lag series residual as `briefs/2026-07-15_evening-steals-timeout-escalate.md` under seed=42. Timeout v2 intentionally lowers default deadline budget for missing Arena clocks; do **not** micro-patch river guards to chase 45%. Cursor: re-run gate once before `--replace` if desired; lag fail alone is not a new regression class.

## Proposed pin

`researcher-ladder-s1.timeout-v2-k170.2026-07-16`

## Live posture (pre-replace)

| Field | Value |
|-------|-------|
| Current pin (pre) | `researcher-ladder-s1.evening-steals.2026-07-15` |
| Submission | `18b2ee80-508f-43c9-93cb-a0771b9dbbde` |
| PvP | **Failed** @ **991** hands |
| Error | `422: static submission timed out` |
| Adj bb/100 before fail | ~+16.4 |

## Cursor later

1. Review this escalate + timeout deltas.
2. rsync / package as usual.
3. `--build --replace` only after GO.
4. Poll: no 422 in first **1000+** hands.

## Hard do-nots (honored)

- `NO_REPLACE=confirmed`
- No FBSDE in `decide()`
- No gin flip
- No runtime LLM

## Sources

- Internal Researcher HU ladder timeout telemetry, 2026-07-16
- K170 fictitious-play FBSDE theory brief
