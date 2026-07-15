# Solver-bake escalate — ship brief (2026-07-15)

## Target

CeminiSuite / Arena — Researcher HU ladder S1 (`cmr3n8tft01nilecm1u5jlny7`). **Cursor-owned `--replace` only** after this brief.

## Summary

L3 Option D solver-bake on cemini (not gin, not DeepCFR). Fable wrote [`2026-07-15_solver-bake-master-plan.md`](2026-07-15_solver-bake-master-plan.md); Grok implemented WP0–WP2; Cursor verified WP3 (gate + critical tests) and owns submit.

| Artifact | Result |
|----------|--------|
| MAFP chart | `chart_changes: **197**` (was baseline 0) |
| Postflop buckets | **90** keys, provenance `heuristic_bucket_v1` |
| `CEMINI_MAFP_CHART` | Wired live in `research_static_chart.py` |
| `CEMINI_POSTFLOP_BUCKETS` | setdefault in `harness/strategy.py`; `solver_frequencies` bias in `cemini_decide` |
| Critical pytest | **47 passed** (mafp wire, postflop, HU guards, K155/K163/K164) |
| HU sandbox gate | **GATE PASS** / `GATE_EXIT:0` — bundle `reports/researcher-round/gate-hu-20260715T141740Z` |
| Bundle | `dist/sandbox-pvp-bundle.zip` includes `assets/research/{mafp_hu_chart,postflop_hu_buckets,preflop}.json` |
| `--replace` | **shipped** — Active `daf19c7e-9039-4252-a45d-c00227ae9b97` (replaced `f4de9f5c`) |

### Yardstick numbers (advisory in gate script; plan thresholds)

| Opponent | bb/100 | Plan ≥ | Status |
|----------|-------:|-------:|--------|
| tight | +42.0 | −5 | OK |
| TEN | +32.2 | 0 | OK |
| maniac_shark_lag | **−5.0** | 0 | short of plan (advisory-only in `run_hu_sandbox_gate.sh`) |
| lag series_win | 60% | — | OK |
| rock/maniac/lag selfplay | GATE PASS | — | OK |

WARN: VPIP 43.9% > 42% advisory ceiling (over-loose after MAFP widen).

## Proposed pin

`researcher-ladder-s1.solver-bake.2026-07-15`

Keep cemini engine. Replace Active `f4de9f5c` (or whatever is Active on poll) only on operator GO.

## Success bar (live)

TrueSkill **μ lift** over ≥2k hands vs pre-replace Active — **not** peak adj bb/100. Field context: rank was **231/247**.

## Orchestration notes

- Claude Code OAuth was revoked → Fable plan via Cursor Task `claude-fable-5-thinking-high`
- Grok CLI re-authed (`grok login --device-auth`); WP0+WP1–2 with `--yolo --max-turns`
- Grok hung on `pytest \| tail` full suite; Cursor finished gate + brief
- `NO_REPLACE=confirmed` until Cursor submit step

## Sources

- Arena S1 ladder field posture 2026-07-15; prior K131b/K136/K160 notes in poker briefs
- Internal: mafp_chart_refinement.py, research_static_chart.py, postflop_buckets.py
