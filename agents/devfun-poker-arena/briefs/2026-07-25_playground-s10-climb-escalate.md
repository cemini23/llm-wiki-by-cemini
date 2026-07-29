---
title: Playground S10 climb escalate — selective BTN/CO steal + maniac value calls
type: brief
tags: [brief, poker, playground, s10, climb, hl-loop, chip-qual, cemini-decide]
created: 2026-07-25
target: examples/cemini_decide.py
---

## Target

`agents/devfun-poker-arena/examples/cemini_decide.py` — **6-max Playground S10 chip climb** (lobby live decide).

- Competition: `cms0bwufmf3n8kyykdpxi6d2i`
- Snapshot (task): **#48 @ 988 chips / 359 hands / 31 won** (~8.6% win) — ~flat vs 1000 start
- #20 floor ≈ **1662** · gap **+674**
- Objective: **totalChips / top-20**, not TrueSkill or Eval bb/100
- Posture: gin / ladder / eval / MAFP / solver V3 **OFF**. No Tournament buy. No Arena `--replace`.

## Summary

S9→S10 survival folds already shipped (SB/BB trash + CO/BTN cold-call trash). S10 is **chip-flat** — climb missing. This escalate adds **selective pot capture** only:

1. **BTN/CO open-steal vs confirmed loose-passive HUD** (legacy `tight` + `open_steal_equity` &lt; 0.50 / rock_steal_eq path). **No** global VPIP widen. **No** gin.
2. **Maniac / VPIP≫45% value call-downs** on **6-max + HU** (fold trash preflop still).
3. **No additional SB leak patch** — S10 analyze does **not** evidence SB float/call-trash (only small blind-tax deltas).

### Deploy recommendation — **DEPLOY lobby (rsync + restart), NO Arena `--replace`**

| Action | Verdict | Why |
|--------|---------|-----|
| **Lobby rsync + `systemctl restart cemini-devfun-poker-lobby`** | **YES — deploy** | Lobby loads `cemini_decide` live. Steals + maniac call-downs only take effect after code lands on prod + lobby restart. |
| Arena `--replace` / sandbox submit / Eval profile | **NO_REPLACE** | Wrong surface. Chip qual is playground lobby. |
| Flip `CEMINI_GIN_*` / MAFP / solver V3 / researcher HU | **NO** | Width without HUD gate re-bleeds stack. |
| Touch prod `.env` | **NO** (Cursor owns enter) | Chip-qual posture already on S10. |

**Cursor one-liner after apply on laptop:**

```bash
# from agents/devfun-poker-arena
bash scripts/rsync_poker_arena_code.sh
ssh cemini-prod 'systemctl restart cemini-devfun-poker-lobby.service && sleep 2 && systemctl is-active cemini-devfun-poker-lobby.service'
./scripts/cemini_playground_status.sh --competition cms0bwufmf3n8kyykdpxi6d2i
```

Do **not** run `./examples/cemini_hl_loop.sh --deploy` unless Cursor wants full preflight again — rsync+restart is enough once unit gates pass.

## Body

### S10 HL evidence (`python3 examples/analyze.py --match cms0bwufmf3n8kyykdpxi6d2i --limit 100 --top 15`)

API returned **50 hands** (cap). Snapshot saved as `reports/hl-loop/latest_analyze_s10.txt`.

| Source | Finding |
|--------|---------|
| Position avg Δ | **SB −1** (worst), BB/UTG/CO ~0, MP/BTN ~0 — blind-tax scale, not bust lines |
| Worst 15 | Tiny −1/−2 deltas; many empty boards (blind folds). Named: 79s SB −2, JTs SB −2 (3c3dQd), J9o BB −2, T5o BB −2, KJs SB −1 |
| Best | KK BB +3; small MP scrapes +1 |
| Preflop log S10 | **0 rows** in local `preflop_decisions.jsonl` (no SB call-trash evidence like S9 Q5s/KTs/22) |
| Climb gap | Flat ~988 vs #20 ~1662 — need **selective pot capture**, not more EP nit |

### SB leak decision — **NO patch this wave**

| Criterion | Result |
|-----------|--------|
| Explicit SB float/call-trash in HH | **Not evidenced** in 50-hand analyze |
| S9-style nonfolds (Q5s/Q6s/KTs/22 SB) | Already guarded; S10 log empty |
| Action | **Do not expand SB fold sets** without new evidence |

If later HL shows SB completes/calls of dominated suits, reopen SB set — not this escalate.

### Leak table → patch

| Pri | Finding | Patch |
|-----|---------|--------|
| P0 | wide_passive → legacy `tight` **never stole** (rock-only gate) | `_allows_selective_btn_co_steal` — rock **or** tight/passive + `open_steal_equity` &lt; 0.50 |
| P0 | Chart + equity steal paths hard-coded `hud_mode == "rock"` | Gate both BTN/CO paths through helper |
| P1 | Maniac value call boost **HU-only** | `_maniac_value_call_margin_boost` — 6-max + HU; VPIP≥0.45 or maniac/lag mode |
| — | SB bleed | **No change** (insufficient evidence) |
| — | Global VPIP / gin / EP | **Not touched** |

**Not patched (by design):** EP trash opens, maniac preflop steal widen, SB complete width, gin/MAFP/solver.

### Files touched

| File | Change |
|------|--------|
| `examples/cemini_decide.py` | Selective BTN/CO steal helper + gates; 6-max maniac value-call boost |
| `tests/test_cemini_preflop_guards.py` | 6 new S10 climb unit tests |
| `reports/hl-loop/latest_analyze_s10.txt` | Prod analyze snapshot |
| `briefs/2026-07-25_playground-s10-climb-escalate.md` | This escalate |

### Gate commands + numbers

```bash
cd agents/devfun-poker-arena
uv run pytest tests/test_cemini_preflop_guards.py tests/test_cold_start_hud.py -q --tb=line
# → 29 passed in ~0.1s (was 23; +6 S10 climb)
```

| Gate | Result |
|------|--------|
| `test_cemini_preflop_guards` + `test_cold_start_hud` | **29 passed** |
| Gin / MAFP / solver flags | Unchanged (OFF) |
| Arena replace / Eval | Not run |
| SB new guards | **None** (no evidence) |

### Chip-climb rationale (why deploy now)

1. **Survival already on; accumulation missing.** #48 @ ~988 with 359 hands — blind tax + zero steal vs call stations.
2. **Field intel (S1 canon) still holds:** loose-passive seats are steal fuel via `rock_steal_eq` / low `open_steal_equity` — but decide only stole when `hud_mode == "rock"`. wide_passive maps to **`tight`**, so steals never fired.
3. **Maniacs (Grok cluster VPIP≫45%):** slightly wider call-downs capture value without preflop trash defense.
4. **HUD-gated only** — unknown cold-start / maniac mode keep high steal bar; trash (`J2o`) still blocked.

### Do not

- Arena `--replace` / sandbox submit / Eval profile
- Enable `CEMINI_GIN_*`, MAFP, solver V3, researcher HU
- Global steal widen without HUD gate
- Extra SB folds without hand-history evidence
- Edit prod `.env` from this escalate

### Follow-up (after ≥80–100 more S10 hands post-deploy)

```bash
python3 examples/analyze.py --match cms0bwufmf3n8kyykdpxi6d2i --limit 100 --top 15
./scripts/cemini_playground_status.sh --competition cms0bwufmf3n8kyykdpxi6d2i
```

Watch: rank vs #20 floor, BTN/CO pot share, SB avg Δ. Reopen SB only if nonfold trash appears in preflop log.

## Sources

- Prod analyze: `reports/hl-loop/latest_analyze_s10.txt` (comp `cms0bwufmf3n8kyykdpxi6d2i`)
- Prior: `briefs/2026-07-25_playground-s10-hl-escalate.md` (S9 survival)
- Canon: `briefs/2026-06-04_playground-s1-competition-intel.md` (S1b rock_steal_eq vs LP)
- Task: `briefs/2026-07-25_playground-s10-climb-grok-prompt.md`

## Implementation status

| Field | Value |
|-------|-------|
| Status | **READY TO DEPLOY** after apply to WORKDIR — lobby rsync+restart; **NO_REPLACE** Arena/Eval |
| Proof | 29 unit gates green (2026-07-25); smoke A9s BTN bet vs LP, J2o fold, maniac no steal |
| Apply note | Grok sandbox could not write OSINT WORKDIR; package under tipdrop handoffs — run `APPLY.sh` |
| Owner next | Operator/Cursor: `APPLY.sh` → rsync + restart lobby; monitor S10 chips/rank |
