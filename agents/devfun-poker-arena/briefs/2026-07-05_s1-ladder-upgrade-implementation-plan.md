# S1 ladder upgrade — implementation plan (premium audit synthesis)

## Target

Operator — `cemini_wiki_poker` heads-up ladder S1 (`cmr3n8tft01nilecm1u5jlny7`)

## Verdict

**PATCH-AND-REPLACE** (3/3 auditors) — keep `CEMINI_SANDBOX_ENGINE=cemini`; no gin hu004 swap.

## Premium audit sources

- `reports/gap-audit/premium/claude-opus_20260705T1319Z.md` (primary)
- `reports/gap-audit/premium/deepseek-reasoner_20260705T1319Z.md`
- `reports/gap-audit/premium/grok-4.3_20260705T1319Z.md`

## Root cause (consensus)

1. **6-max brain in HU body** — VPIP ~27% vs optimal HU ~75%+
2. **SB OOP postflop overcommit** — −84 avg chip delta; catastrophic −1000 stackoffs
3. **Set/overpair blind spot** — no fold on 4-straight / 4-flush completing boards

## Shipped P0 (this session)

| # | Patch | File |
|---|-------|------|
| 1 | `_hu_wide_open_hand` + SB/BTN open rescue | `cemini_decide.py` |
| 2 | `_hu_ladder_bb_defend` + HU call margins | `cemini_decide.py` |
| 3 | `_hero_set_vulnerable_on_four_straight` stack-off fold | `cemini_decide.py` |
| 4 | `_board_four_to_flush` OOP fold without flush | `cemini_decide.py` |
| 5 | `_board_four_in_straight_window` OOP river fold | `cemini_decide.py` |

## Validation

```bash
uv run pytest tests/test_cemini_hu_ladder_guards.py tests/test_cemini_preflop_guards.py -q
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 200
```

## Deploy

```bash
bash scripts/rsync_poker_arena_code.sh
ssh cemini-prod 'cd /opt/devfun-poker-arena && ./venv/bin/python examples/submit_sandbox_pvp.py --build --replace --competition-id cmr3n8tft01nilecm1u5jlny7'
```

## Regression spots (must pass mentally)

| id | hole | board | action |
|----|------|-------|--------|
| R3 | JcJs | 9sJd5dTs8c | fold stack-off (set vs straight) |
| R6 | AsJc | QdTd7d6c9d | fold (4-flush, no diamond) |
| R1 | 6hQc | 9s7c8dJc3c | fold river (weak on 4-straight) |

## Do-not-ship (Opus DNs)

- Do not tighten HU VPIP further
- Do not remove `_preflop_pot_committed_should_call`
- Do not blanket fold river all-ins
