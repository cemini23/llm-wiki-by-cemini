## Target

`agents/devfun-poker-arena/` — ladder S1 opponent modeling (`cmr3n8tft01nilecm1u5jlny7`).

## Summary

K151 ladder nemesis update: **maniac_shark_lite_2** locked 100% pairing after ~1k K150 hands and drove adj bb/100 from −28.9 → −74.5 over 1.8k hands. Arena stats → **`linear_aggro`** LAG (30.6% VPIP, 15.1% PFR, 22% 3-bet), **not** TEN-style wide_passive. Fix is **nemesis handle + linear_aggro exploit + S1B BB defend spots**, not TEN iso path.

**Shipped (2026-07-09):** `research/opponents/maniac-shark-ladder-s1-profile.json`, `maniac_shark_lite_2` in `nemesis_seed._DEFAULT` + `_LINEAR_AGGRO_NEMESIS`, **8 HU regression spots**, `bot_maniac_shark_lag` selfplay villain + HU gate advisory. **Deployed** ladder S1 replace → `bb2a7e5e` (bench Succeeded). Let season accumulate — no further replaces.

## Body

### Investigation recap (2026-07-09)

| Signal | K150 @ 1k hands | K150 @ 1.8k hands |
|--------|-----------------|-------------------|
| Adj bb/100 | −28.9 | **−74.5** |
| Recent pairing | Blitz Kanzaki (healthy) | **maniac_shark_lite_2 100%** |
| TEN pairing | 0% | 0% |

### maniac_shark_lite_2 style profile

| Metric | Value |
|--------|------:|
| VPIP | 30.6% |
| PFR | 15.1% |
| 3-bet | 22.1% |
| WTSD | 22.2% |
| AF | 2.58 |
| Archetype | **linear_aggro** |
| H2H bb/100 (last 50 replays) | **−890** |
| Loss modes | 27× small steal (−10), 2× stack-off (−1000) |

**Exploit path:** `table_nemesis_pressure` → `linear_aggro` branch (`CEMINI_NEMESIS_LINEAR_AGGRO=1`) + S1B `try_defend_bb_vs_steal` / `try_hu_three_bet_vs_aggro`. **Do not** use wide_passive iso path.

### Nemesis seed change

```python
# nemesis_seed._DEFAULT — add:
"maniac_shark_lite_2",  # K151 ladder S1 export 2026-07-09

# _LINEAR_AGGRO_NEMESIS — add:
"maniac_shark_lite_2",
```

### Validation

```bash
uv run pytest tests/test_k151_maniac_shark_nemesis.py \
  tests/test_k151_maniac_shark_selfplay_villain.py \
  tests/test_k151_maniac_shark_hu_spots.py -q
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 200
uv run python scripts/profile_opponent_style.py \
  --agents reports/exports/maniac-shark-audit-20260709/recent/agents.jsonl \
  --tables reports/exports/maniac-shark-audit-20260709/recent/tables.jsonl \
  --handle maniac_shark_lite_2
python3 scripts/skill_audit.py briefs/2026-07-09_k151-maniac-shark-nemesis-update.md
```

### Prod posture

- Auto-submit timer: **DISABLED**
- Live bot: `bb2a7e5e` (K151) — **do not replace** until ≥2k hands or explicit strategy patch.

## Sources

- [Source: Arena export cmr3n8tft01nilecm1u5jlny7, retrieved 2026-07-09]
- `research/opponents/maniac-shark-ladder-s1-profile.json`
- `reports/exports/maniac-shark-audit-20260709/` (prod)
