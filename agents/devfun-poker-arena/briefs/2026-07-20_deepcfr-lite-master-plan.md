---
title: Master plan — DeepCFR-lite (Phase 3) on HU bucket infosets
type: brief
target: Poker Arena
created: 2026-07-20
updated: 2026-07-20
---

## Target

`agents/devfun-poker-arena/` — Grok implements; Cursor gate + **`--replace`**.

## Summary

Phase 2 (opponent modes + stronger bias) **regressed** ladder μ (−38 → −43 on Active `8d66b6e0` @10.4k). Fable verdict: ship **DeepCFR-lite** on the existing 90-key HU bucket abstraction — not full open_spiel NLHE, not rlcard NFSP.

1. **WP0** — kill opponent-mode stack + roll texas_solver bias to Phase‑1 clamps.
2. **WP1–2** — offline advantage-CFR / ES-MCCFR over bucket infosets → `research/deepcfr_hu_buckets.json`.
3. **WP3** — `CEMINI_DEEPCFR=1` O(1) load + soft-replace `solver_frequencies` postflop.
4. **WP4–5** — gate + Cursor `--replace`.


## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Non-goals

- No gin flip / runtime open_spiel / runtime TexasSolver / runtime LLM / torch in sandbox zip
- No full NLHE DeepCFR train (week+ GPU) — defer
- No rlcard NFSP as primary policy (wrong game / mapping OOS)
- No new river-guard micro-patches as the ship
- No Arena `--replace` from Grok

## Baseline (replace metric)

| | Value |
|--|-------|
| Current Active | `8d66b6e0` (~10.4k, μ≈−43, rank ~183) |
| Prior good Active | `a7a677b7` (~13.7k, μ≈−38, rank ~178) |
| Success | μ **better than −38** over ≥3k hands on new Active |
| Stretch | μ ≤ −30 |
| Fail / rollback | still ≤ −43 @ ≥3k |

## Hardest risk

Stacked-margin OOS (Phase‑2 failure mode). **WP0 must be clean before train/ship.**

---

## WP0 — Unstack Phase 2

**Files**

- `harness/strategy.py` — remove `CEMINI_OPPONENT_MODES` setdefault (or setdefault `"0"`). Modes code may stay; ship pin must not enable it.
- `examples/postflop_buckets.py` — `bias_scale_params` for `texas_solver_v1` → Phase‑1:
  - clamp **0.14**, free_mult **0.15**, fold/call/raise **0.18 / 0.15 / 0.225**
- Do **not** delete opponent_modes module; flag-off must be byte-identical to no-overlay.

**Acceptance**

```bash
uv run pytest tests/test_opponent_modes.py tests/test_postflop_buckets.py -q --tb=line
# assert bias_scale_params('texas_solver_v1')['clamp'] == 0.14
```

---

## WP1 — Offline DeepCFR-lite trainer

**File:** `examples/deepcfr_lite_train.py` (new)

**Algorithm (tabular advantage-CFR on abstract game — "lite"):**

- Infosets = existing keys `{street}|{role}|{texture}|{strength_bin}` (90).
- Actions = `bet, check, call, fold, raise` (same schema as buckets).
- Prior = load `research/postflop_hu_buckets.json` (`texas_solver_v1`).
- Iterate external-sampling / regret-matching self-play with a **simple pot EV model** keyed by strength_bin equity midpoints + SPR/role (no card dealing required).
- Maintain cumulative regret + average strategy per infoset.
- Warm-start regrets from prior freqs so early iters stay near solver.
- CLI: `--iters N` (default ≥50k), `--seed`, `--out research/deepcfr_hu_buckets.json`, `--force`.
- Pure stdlib + existing examples imports. **No torch.** Offline-only (not imported by decide hot path except reading JSON).

**Acceptance**

```bash
uv run python examples/deepcfr_lite_train.py --iters 50000 --seed 7 --force
python -c "import json;d=json.load(open('research/deepcfr_hu_buckets.json'));m=d['meta'];assert m['generator']=='deepcfr_lite_v1';assert len(d['buckets'])>=90"
```

---

## WP2 — Bake artifact schema

`research/deepcfr_hu_buckets.json`:

```json
{
  "meta": {
    "generator": "deepcfr_lite_v1",
    "prior_generator": "texas_solver_v1",
    "iters": 50000,
    "seed": 7,
    "infosets": 90
  },
  "buckets": { "<key>": { "bet": ..., "check": ..., "call": ..., "fold": ..., "raise": ..., "size_pot_frac": ... } }
}
```

Refuse overwrite without `--force`. Keep `postflop_hu_buckets.json` intact (prior / fallback).

---

## WP3 — Hot path wire

**Files**

- `examples/postflop_buckets.py` — when `CEMINI_DEEPCFR=1`, resolve path to `deepcfr_hu_buckets.json` (env `CEMINI_DEEPCFR_PATH` override; bundle-aware like existing). Prefer DeepCFR payload for `get_buckets_payload` / `lookup_freqs` **or** dedicated `get_deepcfr_payload` merged in `build_solver_frequencies_context`. Flag off → identical to today.
- `examples/cemini_decide.py` — no heavy logic; use existing solver_frequencies path once buckets resolve to DeepCFR.
- `harness/strategy.py` — `os.environ.setdefault("CEMINI_DEEPCFR", "1")` for researcher HU; **do not** setdefault opponent modes on.
- Bias: when meta.generator is `deepcfr_lite_v1`, use Phase‑1 solver-scale clamps (0.14 / 0.15 / …) — **not** ±0.16.

**Acceptance**

```bash
CEMINI_DEEPCFR=0 uv run pytest tests/test_postflop_buckets.py -q --tb=line
CEMINI_POSTFLOP_BUCKETS=1 CEMINI_DEEPCFR=1 uv run pytest tests/test_deepcfr_lite.py -q --tb=line
```

---

## WP4 — Tests + gate

**File:** `tests/test_deepcfr_lite.py` (new)

- Flag off: no DeepCFR path required for parity tests.
- Flag on: lookup returns freqs; generator meta `deepcfr_lite_v1`.
- At least one fixture table where DeepCFR freqs differ from texas_solver prior **or** bias deltas differ.
- Train smoke: `--iters 200` writes valid schema (tmpdir).

```bash
uv run pytest tests/test_deepcfr_lite.py tests/test_postflop_buckets.py tests/test_opponent_modes.py -q --tb=line
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh
uv run python examples/submit_sandbox_pvp.py --build-only
```

Escalate: `briefs/2026-07-20_deepcfr-lite-escalate.md`  
Pin: `researcher-ladder-s1.deepcfr-lite-v1.2026-07-20`

---

## WP5 — Cursor ship (not Grok)

```bash
bash scripts/rsync_poker_arena_code.sh
# prod:
cd /opt/devfun-poker-arena && . venv/bin/activate
uv run python examples/submit_sandbox_pvp.py --build --replace \
  --pin researcher-ladder-s1.deepcfr-lite-v1.2026-07-20 \
  --competition-id cmr3n8tft01nilecm1u5jlny7
```

Poll Active continuous; compare μ to −38.

---

## Grok DO-NOTS

- No `--replace` / Arena poll-submit
- No `CEMINI_SANDBOX_ENGINE` change
- No torch / open_spiel in pyproject or sandbox bundle
- No deleting texas_solver bake JSON
- Full pytest pipe-to-tail hangs — use unpiped critical subsets + HU gate

## Sources

- Fable advisor 2026-07-20: verdict C DeepCFR-lite + WP0 first
- Live: `8d66b6e0` μ≈−43 @10.4k; prior `a7a677b7` μ≈−38
- Prior plans: `briefs/2026-07-17_texassolver-bake-master-plan.md`, `briefs/2026-07-19_opponent-modes-deeper-bake-master-plan.md`
