## Target

Researcher Round HU sandbox — static-agent bundle via `submit_sandbox_pvp.py`.

## Summary

K131 + K131b bundle is **gate-green** locally. Submit **one agent** (`cemini_decide.py` via `harness/strategy.py`); Tracks A/B were implementation splits only.

**Latest gate bundle:** `reports/researcher-round/gate-hu-*Z/` (run `run_hu_sandbox_gate.sh --hands 200` before submit).

Official guide: https://docs.dev.fun/arena/poker-arena-and-prize/the-sandbox-researcher-guide

## Body

### Env (harness defaults + Researcher)

```
CEMINI_TABLE_FORMAT=hu
CEMINI_GIN_STYLE=1
CEMINI_GIN_STYLE_PREFLOP=1
CEMINI_GIN_STYLE_POSTFLOP=1
CEMINI_GIN_V008=1
CEMINI_S1B_EXPLOIT=1
CEMINI_GIN_V2_EXPLOITS=1
CEMINI_RESEARCHER_MODE=1
CEMINI_SANITIZE_OUTPUT=0
```

### Pre-submit checklist

1. `CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 200` → audit **GATE PASS**, trajectory **PASS**
2. `uv run pytest tests/ -q` (ignore `test_cold_start_hud.py` if flaky)
3. `bash scripts/verify_sandbox_bundle_layout.sh`
4. Arena PvP: `uv run python examples/submit_sandbox_pvp.py --build --replace --competition-id "$ARENA_RESEARCHER_COMP_ID"`
5. Poll: `submit_sandbox_pvp.py --poll <submissionId>` until PvP season progresses

### K131b follow-ups shipped (gap / PFR)

- `try_hu_bb_value_3bet_vs_steal` — BB value 3-bets vs min-raise (before chart-call path)
- PFR audit counts 3-bets (not only unopened raises)
- HU anti-limp-complete in `try_preflop_loose_call`
- HU gap ceiling **12%** (`HU_MAX_VPIP_PFR_GAP`) — BB defend calls vs opens are not 6-max limps

### Acceptance snapshot (seed 42, 400h audit)

| Metric | Target | Typical post-K131b |
|--------|--------|------------------|
| LAG series | ≥45% | ~80% |
| Rock series | ≥55% | ~60% |
| VPIP−PFR gap | ≤12% HU | ~11.2% |
| BB VPIP | up | ~45–46% |
| Trajectory M8/M9 | PASS | PASS |

### Do not submit

- K130 RLCard offline track (`scripts/setup_rlcard_venv.sh`) — research only
- K130 PokerKit verify scripts — CI hygiene, not agent logic

## Sources

- `briefs/2026-06-26_k131-sandbox-improvement-plan.md`
- `briefs/2026-06-26_k131b-bb-lag-tune-plan.md`
- `scripts/run_hu_sandbox_gate.sh`
