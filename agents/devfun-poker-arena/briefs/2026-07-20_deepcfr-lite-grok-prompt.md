## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-20_deepcfr-lite-grok-prompt.md).

# Grok task — DeepCFR-lite Phase 3

ROLE: Implementer. Cursor wrote the plan; you write ALL code, JSON bake, tests, escalate brief. You do NOT Arena `--replace`.

CWD: `/Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena`

READ FIRST (in order):
1. `briefs/2026-07-20_deepcfr-lite-master-plan.md` — full WP0–WP5
2. `examples/postflop_buckets.py`
3. `harness/strategy.py`
4. AGENTS.md Hard NEVERs

CONTEXT:
- Phase 2 opponent modes + ±0.16 bias REGRESSED ladder μ (−38→−43).
- Ship DeepCFR-lite on existing 90 bucket infosets. Pure Python CFR. No torch/open_spiel.
- Keep `CEMINI_SANDBOX_ENGINE=cemini`.

DO ALL WPs 0–4 now (WP5 is Cursor):

### WP0
- `harness/strategy.py`: remove `CEMINI_OPPONENT_MODES` setdefault (modes stay flag-gated off by default).
- `bias_scale_params` for `texas_solver_v1`: clamp 0.14, free_mult 0.15, fold/call/raise 0.18/0.15/0.225.
- For `deepcfr_lite_v1` generator: same Phase-1 solver-scale (0.14/0.15/…).

### WP1–2
- New `examples/deepcfr_lite_train.py` — tabular regret-matching / ES-style CFR over bucket keys; prior from `research/postflop_hu_buckets.json`.
- Write `research/deepcfr_hu_buckets.json` with meta.generator=`deepcfr_lite_v1`, ≥90 keys, `--force` required to overwrite.
- Run train ≥50k iters seed 7.

### WP3
- Wire `CEMINI_DEEPCFR=1` so bucket lookup uses deepcfr JSON (path resolve like postflop; `CEMINI_DEEPCFR_PATH` override).
- `harness/strategy.py` setdefault `CEMINI_DEEPCFR=1` for researcher path.
- Flag off = identical behavior to pre-DeepCFR (with WP0 bias).

### WP4
- `tests/test_deepcfr_lite.py`
- Run critical pytest + `CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh`
- `--build-only` (NOT `--replace`)
- Write `briefs/2026-07-20_deepcfr-lite-escalate.md` with real gate numbers
- Update `config/researcher_sandbox_submit.pin.json` pin string to `researcher-ladder-s1.deepcfr-lite-v1.2026-07-20` with replace:false (Cursor flips replace)

DONE WHEN:
```
uv run python examples/deepcfr_lite_train.py --iters 50000 --seed 7 --force
python -c "import json;d=json.load(open('research/deepcfr_hu_buckets.json'));assert d['meta']['generator']=='deepcfr_lite_v1';assert len(d['buckets'])>=90"
uv run pytest tests/test_deepcfr_lite.py tests/test_postflop_buckets.py tests/test_opponent_modes.py -q --tb=line
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh
uv run python examples/submit_sandbox_pvp.py --build-only
```
Escalate brief has GATE PASS numbers. No `--replace`.

HARD FAIL if you stop after narration without writing files.

## Summary

Operator brief: 2026-07-20 deepcfr-lite-grok-prompt. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-20_deepcfr-lite-grok-prompt.md).


## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
