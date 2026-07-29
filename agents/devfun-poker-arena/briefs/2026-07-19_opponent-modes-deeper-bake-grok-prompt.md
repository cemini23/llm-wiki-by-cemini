## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-19_opponent-modes-deeper-bake-grok-prompt.md).

# Grok task — opponent modes + deeper TexasSolver bake

ROLE: Implementer. Cursor wrote the plan. You implement WP1+WP2+gate+escalate brief. You do NOT `--replace` / Arena poll-submit.

CWD: `/Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena`

READ FIRST:
1. `briefs/2026-07-19_opponent-modes-deeper-bake-master-plan.md`
2. `examples/risk_spectrum.py`, `examples/postflop_buckets.py`, `examples/bake_texassolver_buckets.py`
3. `examples/cemini_decide.py` (HUD enrich + margins usage ~L950–1020)
4. `briefs/2026-07-19_k174-no-fit.md` (ignore for ship)

SOLVER BIN: `.local/texassolver/TexasSolver-v0.2.0-MacOs/console_solver`  
DUMP DIR: `/tmp/cemini-texassolver-dumps` (space-free — required)


## Summary

Operator brief: 2026-07-19 opponent-modes-deeper-bake-grok-prompt. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-19_opponent-modes-deeper-bake-grok-prompt.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## WP1 — opponent_modes
- New `examples/opponent_modes.py` + `tests/test_opponent_modes.py` + `references/opponent-modes.md`
- Map risk_spectrum → nit|lag|wide_passive|balanced; bounded ±0.06 deltas
- Wire in `cemini_decide.py` after HUD enrich; `CEMINI_OPPONENT_MODES=1` in harness
- Flag off = identical behavior
- Update `references/risk-spectrum-tags.md` one paragraph: best-response modes OK

## WP2 — deeper bake
- Expand `research/texassolver_spot_grid.json` to ≥42 spots (add flop/turn/river boards)
- Bump texas_solver bias scale (clamp ±0.16, free_mult 0.18, facing ~1.2×)
- `uv run python examples/bake_texassolver_buckets.py --timeout 180`
- Assert meta.spots_solved≥42, generator texas_solver_v1

## WP3
```bash
uv run pytest tests/test_opponent_modes.py tests/test_postflop_buckets.py -q --tb=line
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh
uv run python examples/submit_sandbox_pvp.py --build-only
```
Write `briefs/2026-07-19_opponent-modes-deeper-bake-escalate.md` with gate numbers + pin `researcher-ladder-s1.opp-modes-bake-v2.2026-07-19`.

## Hard DO-NOTS
- No `--replace`
- No CEMINI_SANDBOX_ENGINE change / no gin
- No runtime solver in decide()
- No dump paths with spaces
- Unpiped pytest only

DONE WHEN: tests+gate green, bake ≥42 spots, escalate brief filled. Print gate summary verbatim.

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
