---
title: Playground S10 HL escalate — S9 chip-survival leak patches
type: brief
tags: [brief, poker, playground, s10, hl-loop, chip-qual, cemini-decide]
created: 2026-07-25
target: examples/cemini_decide.py
---

## Target

`agents/devfun-poker-arena/examples/cemini_decide.py` — **6-max Playground S10 chip-qual** (lobby live decide).

- Competition: `cms0bwufmf3n8kyykdpxi6d2i` (fresh 1000-chip runway)
- Objective: **totalChips / top-20**, not TrueSkill or Eval bb/100
- Posture: gin / ladder / eval / MAFP / solver V3 **OFF** (Cursor already applied chip-qual env)

## Summary

Playground **S9 closed** ~2026-07-25 13:05 UTC at **#51 @ 3721 chips / 607 hands / 53 won** (win≈8.7%). #20 floor ≈9505 — **missed Tournament S9 free entry**.

This escalate ships **Playground-safe decide() leak patches** from S9 preflop decision log (244 rows, comp `cmrt1wzu40jm911suskj9qebe`) + last-50-hand analyze (API replay cap). Focus: SB/BB defend trash + CO/BTN cold-call trash + EP underpair postflop. No gin widen, no HU ladder, no eval crush.

### Deploy recommendation — **DEPLOY lobby (rsync + restart), NO Arena `--replace`**

| Action | Verdict | Why |
|--------|---------|-----|
| **Lobby rsync + `systemctl restart cemini-devfun-poker-lobby`** | **YES — deploy** | Lobby loads `cemini_decide` live. Patches only take effect after code lands on prod and lobby restarts. S10 is early runway (1000 chips) — survival folds pay immediately. |
| Arena `--replace` / sandbox submit / Eval profile | **NO_REPLACE** | Wrong product surface. Chip qual is playground lobby, not Eval bb/100. |
| Flip `CEMINI_GIN_*` / MAFP / solver V3 / researcher HU | **NO** | S9 already showed volume without top-20; width without leak control re-bleeds stack. |
| Buy Tournament S9 | **NO** | Did not qualify top-20. |
| Touch prod `.env` | **NO** (Cursor owns enter scripts) | Chip-qual posture already on S10. |

**Cursor one-liner after merge/pull on laptop:**

```bash
# from agents/devfun-poker-arena
bash scripts/rsync_poker_arena_code.sh
ssh cemini-prod 'systemctl restart cemini-devfun-poker-lobby.service && sleep 2 && systemctl is-active cemini-devfun-poker-lobby.service'
./scripts/cemini_playground_status.sh --competition cms0bwufmf3n8kyykdpxi6d2i
```

Do **not** run `./examples/cemini_hl_loop.sh --deploy` unless Cursor wants the full preflight gate again — rsync+restart is enough once unit gates pass.

## Body

### S9 evidence

| Source | Finding |
|--------|---------|
| Final LB | #51 / 3721 chips / 607 hands / 53 won (~8.7% win) — #20 ≈9505 |
| Preflop log | 244 decisions on `cmrt1wzu40jm911suskj9qebe` |
| Analyze (API cap 50) | Worst: **22 MP −9** on `6c5sTdQh6d`; position sample noisy (many ±1 blind folds) |
| Preflop nonfolds | SB: Q6s/Q5s/KTs/22/44/77 calls; BB: **75o×2**, 76o, J7s, K9s; BTN/CO: Q5s, J8s, A6s, KQo flats |

Chip death mode for S9 was not EP trash opens (EP nonfolds were AA/KK/QQ/AKo). Bleed was **OOP/IP flats that become postflop overcommits** plus BB connector floats — classic chip-qual stack tax at 6-max.

### Leak table → patch

| Pri | Leak (S9) | Patch |
|-----|-----------|--------|
| P0 | SB Q5s/Q6s/KTs call vs open | Expand `_SB_WEAK_SUITED_VS_OPEN` (Q7s–Q2s, KTs, J7s, …) |
| P0 | SB 22/44/77 set-mine OOP | 6-max SB: fold `_LOW_PAIRS_PROTECT` vs raise (not HU) |
| P0 | BB 75o/76o float | Add `75o/76o/65o/86o/85o` to `_WEAK_FACING_RAISE` |
| P0 | BB J7s/K9s float | Expand `_is_bb_suited_trash` |
| P1 | BTN KQo / Q5s cold-call | Broadway fold → CO+**BTN**; new `_CO_BTN_WEAK_SUITED_VS_OPEN` |
| P1 | CO J8s / A6s cold-call | Same CO/BTN weak-suited set |
| P1 | 22 MP under overcards | EP/MP OOP pocket-under-overcards from flop (0.18 pot) |

**Not patched (by design):** K9s BTN open, 55/33 BTN open, A2s–A3s BTN open — keep modest TAG steal width (~10–16% VPIP early). Premium SB/BB defends (TT+, KQs) still live.

### Files touched

| File | Change |
|------|--------|
| `examples/cemini_decide.py` | Guard sets + SB/BB/CO/BTN preflop folds + EP underpair postflop (primary + secondary path) |
| `tests/test_cemini_preflop_guards.py` | 14 new S9→S10 unit guards |
| `reports/hl-loop/latest_analyze_s9.txt` | Prod analyze snapshot (evidence) |
| `briefs/2026-07-25_playground-s10-hl-escalate.md` | This escalate |

### Gate commands + numbers

```bash
cd agents/devfun-poker-arena

# Required gate (task Done-when)
uv run pytest tests/test_cemini_preflop_guards.py tests/test_cold_start_hud.py -q --tb=line
# → 23 passed in ~0.5s

# Extra safety (ran this escalate)
uv run pytest tests/test_cemini_regression.py tests/test_cemini_preflop_guards.py tests/test_cold_start_hud.py -q --tb=line
# → 25 passed in ~243s
```

| Gate | Result |
|------|--------|
| `test_cemini_preflop_guards` + `test_cold_start_hud` | **23 passed** |
| + `test_cemini_regression` | **25 passed** |
| Gin / MAFP / solver flags | Unchanged (OFF) |
| Arena replace / Eval | Not run |

### Chip-survival rationale (why deploy now)

1. **S10 runway is 1000 chips.** One BB float chain or SB set-mine bust line costs a season; these folds are near-free EV saves.
2. **S9 already proved tight-passive EP is fine** — EP opens were premiums. The gap was **defending too wide OOP** and **cold-calling dominated suits IP**.
3. **Patches are Playground-local.** No HU ladder widen, no gin VPIP spike that fights the chip-qual posture Cursor set.
4. **Lobby decides live.** Code on laptop without rsync leaves S10 on the pre-patch decide that just finished #51.

### Do not

- Arena `--replace` / sandbox submit / Eval profile
- Enable `CEMINI_GIN_*`, MAFP, solver V3, researcher HU for this season
- Buy Tournament S9
- Edit prod `.env` from this escalate (Cursor owns enter scripts)
- Optimize self-play bb/100 as success metric — watch **rank vs #20 floor** via `cemini_playground_status.sh`

### Follow-up (after ≥80–100 S10 hands)

```bash
./examples/cemini_hl_loop.sh --from-prod --match cms0bwufmf3n8kyykdpxi6d2i
./scripts/cemini_playground_status.sh --competition cms0bwufmf3n8kyykdpxi6d2i
```

If still outside top-30 after volume with tight defense, next HL round considers **selective late-position open width only** (BTN/CO chart steals) — not SB/BB float expansion.

## Sources

- Prod analyze: `reports/hl-loop/latest_analyze_s9.txt` (comp `cmrt1wzu40jm911suskj9qebe`)
- Prod preflop log: `reports/analyze/preflop_decisions.jsonl` (S9 rows)
- Canon: `briefs/2026-06-03_playground-top20-qualification.md`, `docs/TESTING-CEMINI.md`
- S10 enter: `scripts/playground_chip_qual_enter.sh` (default season 10)

## Implementation status

| Field | Value |
|-------|-------|
| Status | **READY TO DEPLOY** — lobby rsync+restart; **NO_REPLACE** for Arena/Eval |
| Proof | 23 unit guards + 25 with regression green (2026-07-25) |
| Owner next | Cursor: rsync + restart lobby; monitor S10 chips/rank |
