---
title: Master plan — S1 solver-bake escalate
type: brief
target: Poker Arena
created: 2026-07-15
updated: 2026-07-15
---

## Target

`agents/devfun-poker-arena/` — Fable architect plan for Grok implementer; Cursor owns Arena `--replace` after gate green.

## Summary

Bake solver/chart lookups into cemini (MAFP preflop overlay + postflop frequency buckets) to lift TrueSkill μ vs the strong half of S1. No gin flip, no DeepCFR, no runtime LLM. Input: research pack; Active at plan time `f4de9f5c` (keep until Cursor replace).

---

## 1. Goal

Lift TrueSkill μ vs the strong half of the S1 heads-up ladder field (current LB rank 231/247, μ ≈ −61) by baking solver/chart lookups into the existing cemini engine with an O(1) hot path:

1. **Preflop** — regenerate the MAFP HU chart until `meta.chart_changes > 0` (the checked-in file is a baseline no-op), then make the already-defaulted-but-dead `CEMINI_MAFP_CHART=1` flag actually load and apply the overlay at runtime.
2. **Postflop** — ship a v1 bucketed frequency table (`research/postflop_hu_buckets.json`, ~50–100 keys) surfaced as `solver_frequencies` in `retrieve_solver_context`, biasing the existing postflop bet/check/call/fold paths.
3. **Gate** — prove no regression on the frozen HU yardstick pool locally; leave the live `--replace` decision and execution to Cursor.

Success for the wave = TrueSkill μ improvement over ≥2k hands vs the current Active version — **not** peak adjusted bb/100 (already inflated at ~+78 vs soft pairings).

## 2. Non-goals

- **No engine swap** — `CEMINI_SANDBOX_ENGINE=cemini` stays; `gin_hu004` live flip is closed (K131b revert, gin +7.3 TS vs cemini +19 TS).
- **No DeepCFR / open_spiel training** (K136 OOS on Arena clock; K160 information-bound). Deferred until bake plateaus.
- **No runtime LLM** (Level 5) — paid, deadline risk, Arena static-agent.
- **No new trip-board / river-guard micro-patches as the primary ship.** Existing guards stay untouched; WP2 must not add new river guard branches.
- **No Arena submission or `--replace` from the implementer.** No `submit_sandbox_pvp.py --build --replace`, no polling. Cursor owns that step.
- **No runtime solver calls in the hot path** (K95). Everything ships as pre-baked JSON + O(1) dict lookups.
- **No external TexasSolver/WASM dependency for v1.** If a CLI solver is not trivially installable, WP2 buckets are derived from existing equity heuristics and stamped `heuristic_bucket_v1` — honesty in provenance over fake solver claims.
- No edits outside `agents/devfun-poker-arena/` (plus these briefs). No secrets in commits. No pushes to GitHub.

## 3. Work packages

All paths relative to `agents/devfun-poker-arena/` unless absolute.

### WP0 — Regenerate MAFP chart until `chart_changes > 0`

The checked-in `research/mafp_hu_chart.json` has `"meta": {"baseline": true, "chart_changes": 0}` — wiring it as-is changes nothing. Regenerate first.

**Files**
- `research/mafp_hu_chart.json` (overwrite via `write_mafp_chart`)
- `research/preflop.json` (export via `research_static_chart._export_preflop_json` — file currently missing from repo)
- Possibly `examples/mafp_chart_refinement.py` (only if parameter sweep needs a small CLI knob; keep diffs minimal)

**How**
- Run `uv run python examples/mafp_chart_refinement.py` with default params. If round 1 converges with 0 changes (the failure mode that produced the baseline), sweep: lower `--ev-threshold` (0.04 → 0.02 → 0.01), raise `--aggregate-hands` (80 → 160), vary `--seed`. The best-response loop in `best_response_chart_update` only flips cells when EV clears the threshold, so the threshold is the primary lever.
- After a run with changes, verify the written file: `meta.changes >= 1` (note: regenerated meta uses key `changes`; accept either `changes` or `chart_changes` > 0 in the check below and normalize the meta to include `chart_changes` for downstream consistency).
- Run with `--robustness --hands 150` once and record `robustness_gap` in the WP4 brief (informational, not a gate).
- Export `research/preflop.json` (6-max chart; harmless, closes the "export helper exists / file missing" gap).

**Acceptance**
```bash
uv run python -c "
import json; d=json.load(open('research/mafp_hu_chart.json')); m=d['meta']
n=m.get('chart_changes', m.get('changes', 0)); assert n>0, m; print('chart_changes:', n)"
test -f research/preflop.json && echo preflop.json OK
```

**Artifacts:** regenerated chart JSON (provenance stamp `solver_family=mafp` preserved), `research/preflop.json`, deploy-registry rows (script writes them by default).

### WP1 — Wire `CEMINI_MAFP_CHART` at runtime

`harness/strategy.py` L30 sets `CEMINI_MAFP_CHART=1` but nothing reads it. Make it real.

**Files**
- `examples/research_static_chart.py` — add a runtime loader + overlay applier
- `tests/test_mafp_chart_wire.py` (new)

**Design constraints**
- Do **not** import `examples/mafp_chart_refinement.py` at runtime — it imports `agent`, `selfplay`, `deploy_registry` (heavy, offline-only). Replicate the ~30-line load/overlay logic (`load_mafp_chart_ranges` + `apply_mafp_overlay_to_static_chart` semantics) inside `research_static_chart.py`, applied to `_HU_OPEN_CHART`.
- **Bundle-aware path resolution**, in order: (1) `assets/research/mafp_hu_chart.json` relative to the bundle root (submit copies `research/` → `assets/research/`), (2) repo `research/mafp_hu_chart.json` relative to the module, (3) `CEMINI_MAFP_CHART_PATH` env override for tests. Missing/unparseable file → silently keep the static chart (fail-open, never crash decide()).
- Apply overlay **once** (module-level guard or `functools.lru_cache`), only when `CEMINI_MAFP_CHART` is truthy (`1/true/yes/on`), before `research_static_chart()` consults `_HU_OPEN_CHART`. HU only — 6-max `_OPEN_CHART` untouched.

**Acceptance**
```bash
uv run pytest tests/test_mafp_chart_wire.py -q
```
Tests must cover: flag off → static chart answer unchanged; flag on + temp chart file flipping one known cell (e.g. a BTN hand raise→fold) → `research_static_chart` output changes for that cell only; missing file → no exception, static behavior; loader is idempotent across repeated calls.

**Artifacts:** wired loader, new test file.

### WP2 — Postflop bake v1: O(1) bucket JSON + `solver_frequencies`

**Files**
- `research/postflop_hu_buckets.json` (new)
- `examples/postflop_buckets.py` (new — classifier + O(1) lookup; keep helpers in this one file per repo convention)
- `examples/cemini_decide.py` — `retrieve_solver_context` returns `ctx["solver_frequencies"]`; postflop action paths (`_postflop_free`, `_postflop_facing_bet`, and the mix path via `_postflop_mix_allowed`) consume it
- `harness/strategy.py` — add `os.environ.setdefault("CEMINI_POSTFLOP_BUCKETS", "1")` in the cemini block (keep `CEMINI_SANDBOX_ENGINE` default `cemini` untouched)
- `tests/test_postflop_buckets.py` (new)

**Bucket schema (~50–100 keys)**
Key: `"{street}|{role}|{texture}|{strength_bin}"` where street ∈ {flop, turn, river}, role ∈ {ip, oop}, texture ∈ {dry, wet, paired} (implement a small board classifier in `postflop_buckets.py`; `cemini_decide.py` has no texture helper today — `_scenario_label`'s 2-suit check is too coarse; reference `assets/decide_textured.py` for sizing/texture conventions, but do not wire it), strength_bin ∈ {air, weak, medium, strong, nuts} binned from the MC equity decide() already computes (e.g. <0.35 / 0.35–0.5 / 0.5–0.65 / 0.65–0.85 / >0.85).
Value: `{"bet": f, "check": f, "call": f, "fold": f, "raise": f, "size_pot_frac": s}` (frequencies sum ≈1 per decision type; generator normalizes).

**Generation:** offline script section (`python -m` guard) in `postflop_buckets.py` that derives frequencies from equity-vs-pot-odds heuristics consistent with current decide() behavior, nudged toward standard HU solver tendencies (more IP flop stabs on dry boards, fewer OOP river bluffs, etc.). Stamp `solver_provenance("heuristic_bucket_v1", notes="derived from mafp-informed equity heuristics; not a tabular solver export")` via the existing `solver_provenance` helper. Atomic write like `write_mafp_chart`.

**Runtime wiring**
- `retrieve_solver_context`: when street != preflop and `CEMINI_POSTFLOP_BUCKETS` truthy, classify (street, ip/oop from `hero_is_in_position`-equivalent info in table, texture, coarse strength) and set `ctx["solver_frequencies"] = {bucket_key, freqs}`. Pure dict lookup, no simulation — the fine equity bin can be re-resolved inside decide() where equity is already computed; in that case context carries the table slice for the (street, role, texture) triple and decide() picks the bin. Choose one home for bin selection and test it; do not compute equity twice.
- decide() postflop paths: use frequencies to **bias**, not replace, existing logic — e.g. shift bet/check thresholds by bounded deltas derived from bucket freqs, use `size_pot_frac` as sizing hint where a size is chosen. Bounded influence (clamp threshold shifts) so a bad bucket can't produce absurd actions. **No new river-guard branches.** Flag off → byte-identical behavior to today (assert in tests).
- Bundle-aware load same as WP1 (assets/research → repo research → env override), fail-open.

**Acceptance**
```bash
uv run python examples/postflop_buckets.py            # regenerate + self-check
uv run pytest tests/test_postflop_buckets.py -q
uv run pytest tests/ -q                               # full suite still green
```
Tests: JSON schema + key-count 50–100 + provenance present; classifier unit cases (dry/wet/paired, ip/oop); flag off → identical action on fixture tables; flag on → at least one fixture where the biased path changes bet/check choice; O(1) — no network, no subprocess, loader cached.

**Artifacts:** bucket JSON with provenance, lookup module, wired context + decide paths, tests.

### WP3 — Full test suite + local HU sandbox gate

**Files:** none new beyond fixing anything WP0–WP2 broke.

**Acceptance**
```bash
uv run pytest tests/ -q                                   # all green
uv run python -m py_compile examples/cemini_decide.py examples/research_static_chart.py examples/postflop_buckets.py harness/strategy.py
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh   # yardstick gate
```
Yardstick thresholds (`config/hu_yardstick_pool.json`, `never_train: true` — grade only, never tune against these handles): ten ≥ 0, maniac_shark_lag ≥ 0, tight ≥ −5, lag ≥ −10 bb/100.

**Artifacts:** gate output captured (copy the summary block into the WP4 brief).

### WP4 — Ops artifacts (no submit)

**Files**
- `briefs/2026-07-15_solver-bake-escalate.md` (new) — what changed, chart_changes count, bucket key count, gate numbers, robustness_gap, proposed pin `researcher-ladder-s1.solver-bake.2026-07-15`
- `references/researcher-track-sandbox.md` — append a dated note (MAFP wired, postflop buckets v1, gate result)

**Acceptance:** brief exists with all gate numbers filled in; **no** call to `submit_sandbox_pvp.py`; Active `f4de9f5c` untouched.

**Artifacts:** escalate brief + reference note, ready for Cursor's review→replace decision.

## 4. Verification

**Local gate (implementer-owned, blocking):**

1. `uv run pytest tests/ -q` — zero failures.
2. `CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh` — all four yardstick thresholds met.
3. Flag-off parity: with `CEMINI_MAFP_CHART=0 CEMINI_POSTFLOP_BUCKETS=0`, fixture actions identical to pre-change baseline (test-enforced).
4. Chart sanity: `research/mafp_hu_chart.json` has changes > 0 and mafp provenance; `research/postflop_hu_buckets.json` has 50–100 keys and `heuristic_bucket_v1` provenance.
5. Bundle sanity: `uv run python examples/submit_sandbox_pvp.py --build` (build **only**, no `--replace`) and confirm `assets/research/mafp_hu_chart.json` + `assets/research/postflop_hu_buckets.json` land in the bundle and the loader resolves them.

**Live replace (Cursor-owned, later — out of scope here):** Cursor reviews evidence in the WP4 brief, re-runs the gate if needed, then `submit_sandbox_pvp.py --build --replace` with pin `researcher-ladder-s1.solver-bake.2026-07-15`, and polls TrueSkill μ over ≥2k hands vs the current Active. μ lift — not adj bb/100 — is the success metric.

## 5. Grok implementer brief (paste-ready)

```
ROLE: You are the implementer for the S1 solver-bake escalate. Fable wrote the plan; you write ALL code, tests, and charts. You do NOT submit to Arena.

CWD: /Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena

READ FIRST:
- briefs/2026-07-15_solver-bake-master-plan.md   (this plan — WP0..WP4 are your task list, in order)
- briefs/2026-07-15_solver-bake-research-pack.md (code-reality context)
- AGENTS.md Hard NEVERs

FILES YOU MAY TOUCH:
- research/mafp_hu_chart.json (regenerate), research/preflop.json (export), research/postflop_hu_buckets.json (new)
- examples/research_static_chart.py, examples/cemini_decide.py, examples/postflop_buckets.py (new)
- examples/mafp_chart_refinement.py (minimal, only if a sweep knob is needed)
- harness/strategy.py (ONLY to add CEMINI_POSTFLOP_BUCKETS setdefault)
- tests/test_mafp_chart_wire.py (new), tests/test_postflop_buckets.py (new), existing tests only to fix breakage you caused
- briefs/2026-07-15_solver-bake-escalate.md (new), references/researcher-track-sandbox.md (append note)

COMMANDS (in order):
1. uv run python examples/mafp_chart_refinement.py            # sweep --ev-threshold 0.04/0.02/0.01, --aggregate-hands 80/160, --seed until chart changes > 0
2. uv run python -c "import json; d=json.load(open('research/mafp_hu_chart.json')); m=d['meta']; n=m.get('chart_changes', m.get('changes',0)); assert n>0, m"
3. uv run python examples/research_static_chart.py            # exports research/preflop.json
4. <implement WP1 loader + tests>  uv run pytest tests/test_mafp_chart_wire.py -q
5. <implement WP2 buckets + wiring> uv run python examples/postflop_buckets.py && uv run pytest tests/test_postflop_buckets.py -q
6. uv run pytest tests/ -q                                    # full suite green
7. CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh    # ten>=0, maniac_shark_lag>=0, tight>=-5, lag>=-10
8. uv run python examples/submit_sandbox_pvp.py --build       # BUILD ONLY — verify assets/research/*.json in bundle
9. Write briefs/2026-07-15_solver-bake-escalate.md with gate numbers; append note to references/researcher-track-sandbox.md

DO-NOTS (hard):
- Do NOT run submit_sandbox_pvp.py with --replace, or any Arena submission/poll. Cursor does that.
- Do NOT change CEMINI_SANDBOX_ENGINE default from "cemini"; no gin_hu004 flip.
- Do NOT add DeepCFR/open_spiel training, runtime LLM calls, or any network/solver call in the decide() hot path (K95: O(1) lookups only).
- Do NOT add new trip-board/river-guard branches; buckets bias existing postflop paths only.
- Do NOT import mafp_chart_refinement.py at runtime (it pulls agent/selfplay); replicate the small loader in research_static_chart.py.
- Do NOT tune decide() against the yardstick handles (never_train: true) — they grade, they do not train.
- Do NOT wire research/mafp_hu_chart.json while meta shows chart_changes/changes == 0 — regenerate first (WP0 gates WP1).
- Do NOT edit outside agents/devfun-poker-arena/; no new deps without asking; no secrets in commits; no git push.

DONE WHEN: steps 2, 4, 5, 6, 7 all pass, bundle check (8) shows both research JSONs, and the WP4 brief exists with real gate numbers. Report the gate summary block verbatim.
```

## Sources

- Arena S1 ladder field posture 2026-07-15; prior K131b/K136/K160 notes in poker briefs
- Internal: mafp_chart_refinement.py, research_static_chart.py, postflop_buckets.py
