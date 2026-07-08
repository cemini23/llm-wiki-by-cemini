## Target

`agents/devfun-poker-arena/` — ladder S1 opponent modeling (`cmr3n8tft01nilecm1u5jlny7`).

## Summary

K150 ladder nemesis update: **TEN** is our primary scheduler pairing (95/100 recent tables) and crushes us H2H (−218 bb/100) despite ranking 135/174 overall. Arena stats → **`wide_passive`** (51.6% VPIP, 86% WTSD), not linear_aggro. Fix is **nemesis handle seed + wide-passive exploit path**, not a new decide() rewrite.

**Shipped (2026-07-08):** `research/opponents/ten-ladder-s1-profile.json`, `scripts/profile_opponent_style.py`, `ten` added to `nemesis_seed._DEFAULT`. Prod export: `reports/exports/ten-nemesis-20260708/`. **No deploy/resubmit** — let `dcad875c` accumulate a clean season first.

## Body

### Investigation recap

| Signal | Ladder (`19fdf72b`) | Sandbox stray (`b31e5947`) |
|--------|---------------------|----------------------------|
| TrueSkill μ | −53.5 | +54.7 |
| Adj bb/100 | −11.2 | +208.8 |
| Primary opponent | **TEN** (95%) | plutus (100%) |
| Interpretation | Hard nemesis pairing | Soft draw — not ladder proxy |

### TEN style profile (Arena export 2026-07-08)

| Metric | Value |
|--------|------:|
| VPIP | 51.6% |
| PFR | 0.0% (API quirk — treat as limp/call line) |
| WTSD | 86.2% |
| WSD | 50.7% |
| Archetype | **wide_passive** |
| H2H bb/100 (recent 100) | **−218** |
| Uncontested villain wins | 53 / 95 tables |

**Exploit path:** `table_nemesis_pressure` → `wide_passive` branch (`CEMINI_NEMESIS_WIDE_PASSIVE=1`) + `try_iso_vs_wide_passive_limp` in `s1b_exploit.py`. **Do not** add TEN to `_LINEAR_AGGRO_NEMESIS`.

### Nemesis seed change

```python
# nemesis_seed._DEFAULT — add:
"ten",  # K150 ladder S1 export 2026-07-08
```

### Next (not this brief)

1. **Regression spot** — HU BB defend vs wide-passive min-steal / limp line (TEN-shaped).
2. **Selfplay villain** — `finale` or custom bot from TEN replay export (`ten-archive/replays.jsonl`, 50 hands).
3. **Watchlist** (no seed until H2H evidence): `pokaH01`, `reaper`, `quantarmy-7`.
4. **Deploy gate** — only after HU gate + new spot green; single `--replace` on ladder comp.

### Validation

```bash
uv run pytest tests/test_k150_ten_nemesis.py -q
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 200
uv run python scripts/profile_opponent_style.py \
  --agents reports/exports/ten-nemesis-20260708/ladder-snapshot/agents.jsonl \
  --tables reports/exports/ten-nemesis-20260708/ladder-snapshot/tables.jsonl \
  --handle TEN
python3 scripts/skill_audit.py briefs/2026-07-08_k150-ten-nemesis-update.md
```

### Prod posture

- Auto-submit timer: **DISABLED** (see `LESSONS.md` 2026-07-07).
- Live bot: `dcad875c` on ladder S1 — **do not replace** until ≥2k hands or explicit strategy patch.

## Sources

- [Source: Arena export cmr3n8tft01nilecm1u5jlny7, retrieved 2026-07-08]
- `research/opponents/ten-ladder-s1-profile.json`
- @agents/devfun-poker-arena/references/researcher-track-sandbox.md
