# HL R21 deploy spec — S1a survival lane (four-model synthesis)

**Status:** **SHIPPED** — R21 deployed 2026-06-06; **R22** (SB QJo fold) deployed 2026-06-07 @ 2,051 hands  
**Prod baseline:** R22 live (#1, ~2,090 hands, ~8.5% WR)  
**Agent:** `cemini_wiki_poker` · `cmpy2qy65002ud9ej6b7jjq0l`

---

## Architecture

Two lanes (Codex framing):

| Lane | When | Behavior |
|------|------|----------|
| **Survival** | Default S1a (#1, qual/first protect) | Chart-only EP/MP; no cold steals; no exploit widening |
| **Conditional exploit** | S1b only (Jun 7+) | HUD maniac widen, 3-bet lag — gated by `qualification_protect` off + stack/HUD gates |

R21 implements **Survival lane** hardening only. S1b toggles stay **P2** (env flip Jun 7).

---

## P0 — `cemini_decide.py` (ship in R21)

### 1. `COLD_START_NO_STEAL` (env `CEMINI_COLD_START_NO_STEAL=1`, default on)

**Where:** `_preflop_open()` after qual/lead protect block (~line 564).

**Logic:** When `cold_start` from `opponent_hud.coldStart` and position ∈ {CO, BTN} and chart suggests `raise`, only allow open if `hand_class ∈ {TT+, AK, AQ}`. Otherwise `check` or `fold`.

**Does not change:** HUD rock steal path (already blocked when `cold_start`).

**Regression:** `prod_cold_start_btn_no_steal` — BTN 98s + `coldStart: true` → forbidden `{bet, raise, all-in}`.

### 2. `CO_LIMP_TRASH_MIRROR_R20`

**Where:** Early preflop guard in `decide()` (~line 398).

**Logic:** Extend R20 BTN guard to **CO**: `position in (CO, BTN) && call_chips > 0 && _is_sb_complete_trash(hc)` → fold.

**Regression:** `prod_q5o_co_vs_limp` — CO Q5o multiway limp → fold.

### 3. `SB_COMPLETE_TRASH_BLOCK` (verify existing)

**Where:** `_preflop_vs_bet()` SB trash guard (~line 680) + `_preflop_open()` SB check-only (~line 556).

**Logic:** Already folds `_is_sb_complete_trash` including 72o. R21 adds explicit regression only.

**Regression:** `prod_72o_sb_complete` — SB 72o vs limp → fold (no complete).

### 4. S1b exploit gate (qual/first protect)

**Where:** Top of `decide()` after HUD read (~line 191).

**Logic:**
- If `qualification_protect` or `first_protect`: force `hud_mode` maniac → unknown; skip `exploit_from_memory` margins.
- Lobby mirrors: no session-memory margin injection when protect on.

**Regression:** Covered indirectly by existing qual-protect spots; S1b stub deferred to P2.

---

## P1 — lobby + nemesis (ship in R21)

### 5. `JOIN_PACE_STACK_PROTECT`

**Where:** `pace_control.join_retry_seconds()` + `run_cemini_lobby.ensure_joined()`.

**Logic:** When `hero_stack_chips < buy_in` (default 1000), retry interval = `max(tier_retry, CEMINI_LOW_STACK_JOIN_RETRY_S)` (default **3600s**). Avoids 409 join loops when stack < buy-in.

**Env:** `CEMINI_LOW_STACK_JOIN_RETRY_S=3600`

**Test:** `tests/test_pace_control.py::test_low_stack_join_pace`

### 6. `NEMESIS_HUD_SEED`

**Where:** New `examples/nemesis_seed.py`; lobby `seed_nemesis_state()` on startup; `decide()` passes `nemesis_handles` in ctx.

**Default handles:** `hunterguy102`, `thaddius` (override `CEMINI_NEMESIS_HANDLES=hunterguy102,thaddius`).

**Decide guard:** `_preflop_vs_bet()` when `nemesis_opener` and SB and hand ∉ premiums → fold.

**Env:** `CEMINI_NEMESIS_TIGHT=1` (default on)

**Regression:** `prod_nemesis_tight_vs_hunter` — SB A5s vs hunterguy102 open → fold.

---

## P2 — defer to S1b (Jun 7 env flip)

| Toggle | Notes |
|--------|-------|
| `THREE_BET_LAG_VALUE_ONLY` | Only with protect off + stack >60bb |
| `TRAP_AA_KK_VS_HIGH_3B` | Nemesis-only |
| `DEFEND_BB_VS_STEAL_CONDITIONAL` | Bounded; reject DeepSeek BB K7o widen |
| Postflop MDF/float widen | **Reject** as default |

---

## Do NOT change

- Base VPIP/PFR targets (~12.3% / 4.3%)
- Shipped R8–R20 guards, stagger locks, nuts detect (`CEMINI_NUTS_DETECT=1`)
- Lead-blind steal tier under lead_protect (not first_protect)

---

## Files touched (R21)

| File | Change |
|------|--------|
| `examples/cemini_decide.py` | P0 guards + S1b gate + nemesis |
| `examples/nemesis_seed.py` | **NEW** — handles + table opener detect |
| `examples/pace_control.py` | Low-stack join backoff |
| `examples/run_cemini_lobby.py` | Nemesis seed, stack-aware join, protect-gated memory |
| `tests/helpers/cemini_tables.py` | 5 new spot builders |
| `tests/fixtures/regression_spots.py` | 4 new spots + optional `context` |
| `tests/test_cemini_regression.py` | Pass spot context to `decide()` |
| `tests/test_pace_control.py` | Low-stack test |
| `deploy/.env.production.example` | Document new env vars |

---

## Env vars (prod `.env`)

```bash
# R21 — survival lane (defaults shown; set explicitly on prod if desired)
CEMINI_COLD_START_NO_STEAL=1
CEMINI_NEMESIS_TIGHT=1
CEMINI_NEMESIS_HANDLES=hunterguy102,thaddius
CEMINI_LOW_STACK_JOIN_RETRY_S=3600

# Existing (keep)
CEMINI_NUTS_DETECT=1
CEMINI_FIRST_RANK=1
CEMINI_FIRST_JOIN_RETRY_S=1800
CEMINI_STAGGER_LOCKS=1
```

No env-only deploy required for R21 logic (code deploy). Optional: add nemesis handles to prod `.env` if overriding defaults.

---

## HL cadence (operator)

1. **Wait** until `hands ≥ 1,923` (`reports/hl-loop/state.json`).
2. **Analyze:** `./examples/cemini_hl_loop.sh --from-prod --round 21`
3. **Preflight:** `./scripts/cemini_preflight.sh` (expect ≥147 tests, regression ≥24 spots).
4. **Deploy:** `./examples/cemini_hl_loop.sh --preflight-only --deploy --round 21`  
   Or: `./deploy/deploy_to_cemini_prod.sh` after preflight green.
5. **Verify prod:** `grep -E 'cold_start|CO/BTN trash|nemesis' /opt/devfun-poker-arena/examples/cemini_decide.py`
6. **Bump state:** `reports/hl-loop/state.json` → round 21, phase deployed.

---

## Preflight gates

| Gate | Command | Pass |
|------|---------|------|
| Regression | `pytest tests/test_cemini_regression.py -q` | All spots including R21 |
| Pace | `pytest tests/test_pace_control.py -q` | Low-stack ≥3600s |
| Full | `./scripts/cemini_preflight.sh` | 147/147 (or current count) |

---

## Rollback

Revert commit on prod + restart lobby systemd unit. R20 guards remain if partial revert; full revert removes R21 only.

---

## S1b checklist (Jun 7 — separate deploy)

- [ ] Flip `CEMINI_FIRST_JOIN_RETRY_S` / lead tier per ROADMAP S1b table
- [ ] Enable P2 exploit env toggles only with `qualification_protect` off
- [ ] Append S1b export Jun 11 (not monolithic with S1a)
