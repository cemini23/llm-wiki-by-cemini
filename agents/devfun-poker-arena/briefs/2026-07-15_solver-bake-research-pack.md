---
title: Research pack — S1 solver-bake escalate
type: brief
target: Poker Arena
created: 2026-07-15
updated: 2026-07-15
---

## Target

`agents/devfun-poker-arena/` — Researcher HU ladder S1. Audience: Fable architect → Grok implementer → Cursor `--replace` only.

## Summary

Field posture + closed paths for L3 Option D solver/chart bake into cemini (MAFP chart + postflop buckets). Live Active at pack time was `f4de9f5c`; do not recommend gin flip, DeepCFR, or runtime LLM this wave.

**Competition:** `cmr3n8tft01nilecm1u5jlny7` · Agent `cemini_wiki_poker` · Pin baseline `researcher-ladder-s1.k164-capability.2026-07-14`

---

## Live field posture (2026-07-15 poll)

| Metric | Value |
|--------|-------|
| PvP status | Active |
| Hands | ~1.5k+ |
| Adj bb/100 | ~+78 (inflated vs soft pairings) |
| TrueSkill μ | ~−61 |
| Score μ−3σ | ~−108 |
| **LB rank** | **231 / 247** |

Operator judgment: bottom-decile vs field. +bb/100 ≠ competitive. Escalate away from guard micro-patches.

---

## Closed / failed paths (do not recommend)

| Path | Evidence | Verdict |
|------|----------|---------|
| Live `CEMINI_SANDBOX_ENGINE=gin_hu004` | Brief k139: gin `8545120c` **+7.3 TS @ 5k** vs cemini **+19 TS** — reverted K131b | **NO** |
| Runtime LLM (Level 5) | Paid, deadline risk, Arena static-agent | **NO this wave** |
| DeepCFR / open_spiel train | K136 OOS on Arena clock; K160 information-bound | **DEFER** after bake plateaus |
| More trip-board / river guard patches as primary lever | Soft EV; does not move μ vs strong | **NO as main ship** |

---

## Canon escalate (locked)

**L3 Option D — solver/chart lookup bake into cemini**, O(1) hot path.

Primary docs:
- `docs/strategy.md` — Option D cheapest for one competition
- `references/optimization-levels.md` — TexasSolver bake OR train weights
- `briefs/2026-07-05_s1-ladder-upgrade-implementation-plan.md` — PATCH-AND-REPLACE, keep cemini
- `prompts/s1_ladder_gap_audit.md` — +bb with negative μ; need structural μ lift
- K95: **no solver calls in hot path**

---

## Code reality (critical gaps)

### Chart already drives decide (preflop)

`examples/cemini_decide.py`:
- `retrieve_solver_context` → `preflop_chart.suggested_action`
- HU open/defend/3bet paths consume `suggested` (`_hu_preflop_pfr_open`, `_hu_bb_*`, `_preflop_open`, gin v008 floors)

### Dead flag

`harness/strategy.py` L30: `setdefault("CEMINI_MAFP_CHART", "1")`
**No runtime code reads `CEMINI_MAFP_CHART`.**

Helpers exist only offline in `examples/mafp_chart_refinement.py`:
- `load_mafp_chart_ranges(path)`
- `apply_mafp_overlay_to_static_chart() -> int`

### Baseline chart is a no-op

`research/mafp_hu_chart.json`:
```json
"meta": { "baseline": true, "chart_changes": 0 }
```
Provenance: `solver_family=mafp`, stamped 2026-06-30. Wiring this alone **does not change play**.

Must **regenerate** with `chart_changes > 0` vs yardstick mix before wire is valuable.

### Static chart

`examples/research_static_chart.py` — in-memory `_HU_OPEN_CHART`; postflop returns `{}`.
Export helper for `research/preflop.json` exists; file **missing** from repo.

### Postflop

No `research/postflop_*.json`. No TexasSolver/WASM code.
Reference sizing only: `assets/decide_textured.py` (not sandbox wired).
`retrieve_solver_context` has no `solver_frequencies` yet.

### Bundle

`examples/submit_sandbox_pvp.py` copies `research/` → `assets/research/`.
Must load chart from: `assets/research/mafp_hu_chart.json` (bundle) or repo `research/` (local).
`skills/` omitted by default. Gin vendor omitted when engine=cemini.

### Engine route

`harness/strategy.py`: default `CEMINI_SANDBOX_ENGINE=cemini` → `cemini_decide.decide`.

---

## Yardstick gate (before --replace)

`config/hu_yardstick_pool.json` (`never_train: true`):

| Opponent | min_bb100 |
|----------|-----------|
| ten | ≥ 0 |
| maniac_shark_lag | ≥ 0 |
| tight | ≥ −5 |
| lag | ≥ −10 |

Gate script: `CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh`

Success for live wave: **TrueSkill μ improvement** over ≥2k hands vs current Active — not peak adj bb/100.

---

## Competitor intel (skim)

Wiki: `wiki/concepts/devfun-poker-competitor-github-recon-2026-06.md`
- gin: ranges + profiled counters + Kuhn CFR literacy (not live NLHE solver)
- Top LB handles often closed-source
- Heuristic Learning ceiling vs panel ~+5–10 bb/100; top is solver-lookup / DeepCFR territory

---

## Operator orchestration constraints

1. **Fable** writes the master implementation plan only (architect).
2. **Grok CLI** implements all code/tests/charts (implementer).
3. **Cursor Auto** only: review evidence → HU gate confirm → `submit_sandbox_pvp.py --build --replace` + poll.
4. Do **not** replace while implementing; keep `f4de9f5c` running for intel.
5. No secrets in commits. Stay under `agents/devfun-poker-arena/` (+ brief).

---

## Suggested work packages (architect may reorder)

**WP0 — Regenerate chart:** run `mafp_chart_refinement.py` against ten/maniac_shark_lag/tight until `chart_changes > 0`; overwrite `research/mafp_hu_chart.json`; export `research/preflop.json`.

**WP1 — Wire:** when `CEMINI_MAFP_CHART=1`, load/apply overlay in `research_static_chart` or `retrieve_solver_context`; tests for on/off + one changed cell.

**WP2 — Postflop bake v1:** `research/postflop_hu_buckets.json` (~50–100 keys: street × ip/oop × texture × strength_bin → freqs); return `solver_frequencies` from context; bias existing postflop bet/check/fold — **no new river guards**. Stamp provenance `heuristic_bucket_v1` / mafp. Defer external TexasSolver CLI if not installable.

**WP3 — Tests + gate:** unit tests; HU sandbox gate TEN/maniac green.

**WP4 — Ops artifacts (Grok):** brief `2026-07-15_solver-bake-escalate.md`, pin agentVersion `researcher-ladder-s1.solver-bake.2026-07-15`, note in `references/researcher-track-sandbox.md`. **Do not submit** — leave for Cursor.

---

## Explicit non-goals

- gin_hu004 live engine flip
- DeepCFR training
- Runtime LLM
- Primary ship = more `cemini_decide` leak guards
- Auto-submit / Cursor spending tokens on bulk implement

---

## Key absolute paths

```
/Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena/
  examples/cemini_decide.py
  examples/research_static_chart.py
  examples/mafp_chart_refinement.py
  harness/strategy.py
  research/mafp_hu_chart.json
  config/hu_yardstick_pool.json
  scripts/run_hu_sandbox_gate.sh
  examples/submit_sandbox_pvp.py
  briefs/
```

## Sources

- Arena S1 ladder field posture 2026-07-15; prior K131b/K136/K160 notes in poker briefs
- Internal: mafp_chart_refinement.py, research_static_chart.py, postflop_buckets.py
