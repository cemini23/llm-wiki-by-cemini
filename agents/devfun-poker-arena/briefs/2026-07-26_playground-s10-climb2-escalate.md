---
title: Playground S10 climb2 escalate — CO/MP overcommit folds
type: brief
tags: [brief, poker, playground, s10, climb, hl-loop, chip-qual, cemini-decide]
created: 2026-07-26
target: examples/cemini_decide.py
---

## Target

`agents/devfun-poker-arena/examples/cemini_decide.py` — **6-max Playground S10 chip climb** (lobby live decide).

- Competition: `cms0bwufmf3n8kyykdpxi6d2i`
- Status at patch: **#50 @ ~1498 / 922h** — climb1 helped chips; #20 floor ~2809 (gap +1311)
- Implemented in **Cursor** (Grok CLI unavailable)

## Summary

Post-climb1 analyze: **BTN prints** (+34 avg, AKo +310); **CO/MP tax** the stack. Worst hands: **K9s CO −11** king-high air on `43JTx`, **55 MP −5** underpair on `K74`.

### Deploy recommendation — **DEPLOY lobby (rsync + restart), NO Arena `--replace`**

| Action | Verdict |
|--------|---------|
| Lobby rsync + restart | **YES** |
| Arena `--replace` / gin / Tournament buy | **NO** |
| Touch prod `.env` | **NO** |

```bash
bash scripts/rsync_poker_arena_code.sh
ssh cemini-prod 'systemctl restart cemini-devfun-poker-lobby.service'
./scripts/cemini_playground_status.sh --competition cms0bwufmf3n8kyykdpxi6d2i
```

## Patches

| Pri | Leak | Patch |
|-----|------|--------|
| P0 | K9s CO king-high air (−11) | `_hero_weak_king_high_air` → fold CO/BTN K9–K2 no pair vs ≥15% pot |
| P0 | 55 MP under K-high flop (−5) | EP/MP underpair-under-overcards: IP+OOP; small-pair bar **0.12** |
| P1 | IP small-pair peels | CO/BTN under-overcards from **flop** for small pairs @ 0.15 |

**Not touched:** BTN selective steals / maniac value (climb1); gin; global VPIP widen.

## Files

- `examples/cemini_decide.py`
- `tests/helpers/cemini_tables.py` — `mp_55_under_king_flop_s10`, `co_k9s_king_high_air_s10`
- `tests/test_cemini_preflop_guards.py` — 3 climb2 tests
- `reports/hl-loop/latest_analyze_s10_climb2.txt`

## Gate

```bash
uv run pytest tests/test_cemini_preflop_guards.py tests/test_cold_start_hud.py -q --tb=line
# → 32 passed
```

## Chip rationale

Climb1 raised chips/hand (~0.9/h) but #20 runs ~2+/h. Cutting CO/MP overcommits protects the BTN edge instead of giving it back mid-hand.

## Sources

- Internal Arena ops / prior escalate briefs in this directory.
