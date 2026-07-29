## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-17_texassolver-bake-grok-prompt.md).

# Grok task — TexasSolver bake Phase 1

ROLE: Implementer. Cursor wrote the plan; you write ALL bake code, JSON, bias scale, tests, escalate brief. You do NOT Arena `--replace`.

CWD: `/Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena`

READ FIRST (in order):
1. `briefs/2026-07-17_texassolver-bake-master-plan.md`
2. `research/texassolver_spot_grid.json` (already written — use it)
3. `examples/postflop_buckets.py`
4. AGENTS.md Hard NEVERs

SOLVER (installed, smoke OK):
`.local/texassolver/TexasSolver-v0.2.0-MacOs/console_solver`

Strategy JSON shape (from smoke):
```
root = { actions, childrens, node_type, player, strategy }
strategy = { actions: ["CHECK","BET …"], strategy: { "AhKd": [p_check, p_bet], … } }
```
Player 1 at root is typically OOP. After CHECK child, IP acts. Aggregate both roles.


## Summary

Operator brief: 2026-07-17 texassolver-bake-grok-prompt. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-17_texassolver-bake-grok-prompt.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Tasks (in order)

### WP1 — grid
Keep/adjust `research/texassolver_spot_grid.json` if needed (already has 18 flop + 6 turn + 6 river).

### WP2 — bake script
Create `examples/bake_texassolver_buckets.py`:
- Resolve bin via `CEMINI_TEXASSOLVER_BIN` or default path above
- For each spot: write temp input txt (pot/stack/board/ranges/bet sizes from grid defaults), run console_solver, parse dump
- Aggregate into existing schema keys `{street}|{role}|{texture}|{strength_bin}`
- Strength bin: reuse `postflop_buckets.strength_bin` with a cheap equity estimate vs random/board (MC ok offline) OR hand-category heuristic; document choice
- Atomic overwrite `research/postflop_hu_buckets.json` with `meta.generator = "texas_solver_v1"`
- List `streets_solved` / `streets_extrapolated` honestly
- If a spot fails, log and continue; require ≥12 successful flop spots
- Cache dumps under `.local/texassolver/dumps/` (gitignored) so re-runs are fast

Protect heuristic path: `python examples/postflop_buckets.py` must NOT overwrite texas_solver_v1 unless `--force-heuristic`.

### WP3 — bias scale
In `bias_thresholds_from_freqs` (or caller): if loaded meta generator is `texas_solver_v1`, use clamp ±0.14 and ~1.5× multipliers vs heuristic. Flag off = unchanged.

### WP4 — verify
```bash
uv run python examples/bake_texassolver_buckets.py
uv run pytest tests/test_postflop_buckets.py -q --tb=line
uv run pytest tests/ -q --tb=line
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh
uv run python examples/submit_sandbox_pvp.py --build
```
Write `briefs/2026-07-17_texassolver-bake-escalate.md` with gate numbers + pin `researcher-ladder-s1.texassolver-v1.2026-07-17`.
Append one line to `references/researcher-track-sandbox.md`.

## Hard DO-NOTS
- No `--replace`, no Arena poll
- No `CEMINI_SANDBOX_ENGINE` change
- No runtime solver in decide()
- Do not commit `.local/texassolver/`
- No new river-guard branches
- Do not pipe pytest to `tail` (hangs)

DONE WHEN: `meta.generator==texas_solver_v1`, ≥90 bucket keys, tests+gate green, escalate brief filled. Print gate summary verbatim at end.

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
