# SB TAG Defend — posfix Dig Brief

**Date:** 2026-08-03  
**Agent version:** `playground-s11.qual.2026-08-03.tag-sb-v3.posfix`

## Target

operator / Playground S11 dig archive

## Summary

SB TAG defend was already working; the apparent AQo miss was a mid-hand position flip. `posfix` shipped and lobby restarted. No further TAG/gin/T10 action.

## Dig findings

### SB TAG defend — working

Under `tag-sb-v3`, stable SB `TAG_SB_DEFEND` hands all called: 44, KJo, K9s, AKo. Defend-set SB folds = 0.

### Apparent AQo miss

AQo logged as SB fold shared `tableId`/hole with a prior MP call (`cmsdtdp8bo6wbv70jabqpll2s`). Position flipped after early folds.

**Root cause:** `examples/position_utils.py` — `hero_position_label` used `_active_seat_numbers` (dropped folded seats), rotating UTG/MP/CO/SB mid-hand. Corrupted logs and re-action branches.

### What shipped

- Dealt-in seats for position geometry; tests in `tests/test_position_utils.py`
- Preflop log: `stackChips`, `big_blind`, `call_chips`
- Live: `AGENT_VERSION=playground-s11.qual.2026-08-03.tag-sb-v3.posfix` on competition `cms7hrnjg20czv7oi85cho570`

## Explicit NO further action

- No more TAG/SB widen for this dig
- Do not re-enable gin
- No T10 250 MON rebuy
- VPIP ~8% = selection + nit chart, not broken SB defend

## Sources

- `reports/exports/playground-s11-live/preflop_decisions.jsonl`
- `examples/position_utils.py`, `examples/cemini_decide.py` (`_log_preflop_decision`)
- `scripts/playground_chip_qual_apply_env.py`
