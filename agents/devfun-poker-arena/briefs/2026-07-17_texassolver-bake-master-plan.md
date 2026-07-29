---
title: Master plan — TexasSolver postflop bake (Phase 1 μ climb)
type: brief
target: Poker Arena
created: 2026-07-17
updated: 2026-07-17
---

## Target

`agents/devfun-poker-arena/` — Cursor architect plan; **Grok implements**; Cursor owns gate re-check + Arena `--replace`.

## Summary

Replace `heuristic_bucket_v1` frequencies in `research/postflop_hu_buckets.json` with **aggregated TexasSolver console exports** (`texas_solver_v1`), keep O(1) hot path, strengthen bias when provenance is real solver. Goal: TrueSkill **μ** lift vs strong half of S1 (baseline at plan time: rank ~190/259, μ≈−45, Active `bf7679bd`). No gin flip, no DeepCFR, no runtime solver/LLM.

TexasSolver macOS binary already downloaded to (gitignored):

`.local/texassolver/TexasSolver-v0.2.0-MacOs/console_solver`

Smoke OK 2026-07-17 (sample → `/tmp/ts_smoke_out.json`, schema `actions/childrens/strategy`).

---

## 1. Goal

1. Offline-solve a fixed HU spot grid with TexasSolver `console_solver`.
2. Aggregate root (+ optional facing-bet) strategies into the existing bucket schema:
   `{street}|{role}|{texture}|{strength_bin}` → `{bet,check,call,fold,raise,size_pot_frac}`.
3. Stamp provenance `texas_solver_v1` (not heuristic).
4. Raise bias authority for solver provenance (still clamped; no river-guard branches).
5. Pass frozen HU yardstick gate; Cursor `--replace` after green.

Success metric (live): μ improvement over ≥3k hands vs pre-replace Active — **not** peak adj bb/100.

## 2. Non-goals

- No engine swap (`CEMINI_SANDBOX_ENGINE=cemini`).
- No DeepCFR / open_spiel training (Phase 3 later).
- No runtime TexasSolver / network / LLM in `decide()` (K95).
- No Arena `--replace` from Grok.
- No AGPL TexasSolver binary in the Arena zip — bake JSON only; binary stays under `.local/`.
- No Phase-2 opponent-mode switch in this wave (follow-on).

## 3. Work packages

### WP0 — Solver path + smoke (done on architect machine; re-verify)

```bash
TS=".local/texassolver/TexasSolver-v0.2.0-MacOs"
chmod +x "$TS/console_solver"
"$TS/console_solver" -i "$TS/resources/text/commandline_sample_input.txt"
# expect output_result.json or configured dump
```

Env override: `CEMINI_TEXASSOLVER_BIN` → absolute path to `console_solver`.

### WP1 — Spot grid (checked-in)

**File:** `research/texassolver_spot_grid.json`

Minimum v1 grid (~18 flop boards × 1 SPR):

| texture | boards (examples) |
|---------|-------------------|
| dry | `Kd7c2s`, `Ah9d3c`, `Qs5h2d`, `Jc8d3s`, `Td6c2h`, `9h4d2c` |
| wet | `JhTh2h`, `9s8s7c`, `QdJd3d`, `Ts9h8d`, `AhKh5h`, `7h6h2c` |
| paired | `KK7c`→`KsKd7c`, `AhAd5s`, `QcQd2h`, `JhJd8c`, `TsTd4h`, `9c9d3s` |

Defaults per spot:

- `pot=20`, `effective_stack=100` (SPR 5 — typical SRP mid)
- Ranges: use TexasSolver sample-style wide HU continue ranges (BTN open / BB defend) — put full range strings in the grid file
- Bet sizes: 50% pot bet, 60% raise, allin threshold 0.67 (match sample)
- `set_accuracy 1.0`, `set_max_iteration 120`, `set_dump_rounds 1` for flop-root aggregation speed
- `set_thread_num` = min(8, cpu_count)

Turn/river fill strategy for v1:

- Prefer: solve **6 turn** + **6 river** boards (2 per texture) with shorter trees if flop-only aggregation leaves turn/river as heuristic blend
- Acceptable fallback: copy flop-aggregated freqs to turn/river with documented street size_pot_frac nudges, but **meta must list which streets are `solved` vs `extrapolated`**

### WP2 — Bake pipeline

**Files**

- `examples/bake_texassolver_buckets.py` (new) — offline only
- `research/postflop_hu_buckets.json` (overwrite)
- Keep `examples/postflop_buckets.py` runtime loader; extend generator path so heuristic regen does not silently overwrite solver bake unless `--heuristic`

**Pipeline**

1. For each spot in grid: write temp command file → run `console_solver` → parse dump JSON.
2. At root decision node for OOP (and IP if tree exposes IP root after check): for each hand in `strategy`, map action probs:
   - CHECK / BET x → check/bet
   - CALL / FOLD / RAISE x → call/fold/raise when facing
3. Strength bin: coarse hand-vs-board equity heuristic already used by decide (`strength_bin`) OR equity from solver if present; must be deterministic and tested.
4. Aggregate weight = range weight × strategy mass into bucket accumulators per `(street, role, texture, strength_bin)`.
5. Normalize freqs; set `size_pot_frac` from modal bet size / pot.
6. Atomic write JSON with:

```json
"meta": {
  "generator": "texas_solver_v1",
  "solver": "bupticybee/TexasSolver@v0.2.0",
  "spots_solved": <int>,
  "streets_solved": ["flop", ...],
  "streets_extrapolated": [...],
  "key_count": 90,
  "baked_at": "YYYY-MM-DD"
}
```

Also call existing `solver_provenance(...)` if present.

**Acceptance**

```bash
uv run python examples/bake_texassolver_buckets.py --grid research/texassolver_spot_grid.json
python -c "import json;d=json.load(open('research/postflop_hu_buckets.json'));assert d['meta']['generator']=='texas_solver_v1';assert len(d['buckets'])>=90"
```

### WP3 — Stronger bias for solver provenance

**Files:** `examples/postflop_buckets.py` (`bias_thresholds_from_freqs`)

When loaded meta `generator == texas_solver_v1` (or env `CEMINI_POSTFLOP_BIAS_SCALE`):

- Raise clamp from `±0.08` → `±0.14`
- Raise free-spot multiplier `0.10` → `0.18`
- Facing multipliers similarly (+~50%)

Flag off (`CEMINI_POSTFLOP_BUCKETS=0`) still byte-identical. No new river guards.

**Tests:** extend `tests/test_postflop_buckets.py` — provenance-aware scale; flag-off parity.

### WP4 — Gate + ops brief (no submit)

```bash
uv run pytest tests/test_postflop_buckets.py tests/test_mafp_chart_wire.py -q --tb=line
uv run pytest tests/ -q --tb=line   # unpiped
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh
uv run python examples/submit_sandbox_pvp.py --build   # BUILD ONLY
```

Write `briefs/2026-07-17_texassolver-bake-escalate.md` with gate numbers + proposed pin:

`researcher-ladder-s1.texassolver-v1.2026-07-17`

## 4. Verification (Cursor after Grok)

1. Meta generator is `texas_solver_v1`, key_count ≥ 90
2. Pytest green; HU gate thresholds held
3. Bundle contains updated `assets/research/postflop_hu_buckets.json`
4. `--build --replace` + poll μ (≥3k hands)

## 5. Grok implementer brief (paste-ready)

```
ROLE: Implementer for TexasSolver postflop bake Phase 1. Cursor wrote the plan; you write ALL bake code, grid, JSON, bias scale, tests, escalate brief. You do NOT Arena --replace.

CWD: /Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena

READ FIRST:
- briefs/2026-07-17_texassolver-bake-master-plan.md
- examples/postflop_buckets.py
- AGENTS.md Hard NEVERs

SOLVER BIN (already installed):
.local/texassolver/TexasSolver-v0.2.0-MacOs/console_solver
(or CEMINI_TEXASSOLVER_BIN)

FILES YOU MAY TOUCH:
- research/texassolver_spot_grid.json (new)
- research/postflop_hu_buckets.json (overwrite with texas_solver_v1)
- examples/bake_texassolver_buckets.py (new)
- examples/postflop_buckets.py (bias scale + protect heuristic overwrite)
- tests/test_postflop_buckets.py (extend)
- briefs/2026-07-17_texassolver-bake-escalate.md (new)
- references/researcher-track-sandbox.md (append one note)

DO-NOTS:
- No --replace / no Arena poll
- No CEMINI_SANDBOX_ENGINE change
- No runtime solver in decide()
- Do not commit .local/texassolver binary
- Do not add new river-guard branches
- Full pytest: unpiped `uv run pytest tests/ -q --tb=line` (piped tail hangs)

DONE WHEN: bake produces texas_solver_v1 JSON, tests+gate green, escalate brief has real numbers.
```

## 6. Follow-on (not this wave)

- **Phase 2:** opponent-conditioned modes (nit/LAG/wide-passive) using K156 risk tags + HUD — switch preflop/postflop modes.
- **Phase 3:** DeepCFR only if Phase 1 plateaus after ≥5k hands.

## Sources

- Field: rank ~190/259, μ≈−45 (2026-07-17 poll)
- Prior: `briefs/2026-07-15_solver-bake-master-plan.md` (heuristic v1 — superseded for postflop freqs)
- TexasSolver: https://github.com/bupticybee/TexasSolver (AGPL-3.0; binary not redistributed)
