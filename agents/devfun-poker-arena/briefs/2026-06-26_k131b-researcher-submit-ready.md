## Target

Researcher Round HU sandbox — `examples/cemini_decide.py` via `pokerkit run`.

## Summary

K131 + K131b bundle is **gate-green** locally. Submit **one agent** (`cemini_decide.py`); Tracks A/B were implementation splits only.

**Latest gate bundle:** `reports/researcher-round/gate-hu-*Z/` (run `run_hu_sandbox_gate.sh --hands 200` before submit).

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
```

### Pre-submit checklist

1. `CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 200` → audit **GATE PASS**, trajectory **PASS**
2. `uv run pytest tests/ -q` (ignore `test_cold_start_hud.py` if flaky)
3. Smoke on Arena: `pokerkit run --agent examples/cemini_decide.py --max-hands 50`
4. Full season when comp live (multi-day per AGENTS.md)

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
