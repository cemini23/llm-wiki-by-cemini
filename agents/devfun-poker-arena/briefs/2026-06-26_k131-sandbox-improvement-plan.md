## Target

`agents/devfun-poker-arena/` — K131 HU sandbox improvement wave. Three parallel implementation tracks (A/B/C), each scoped to a separate agent with no file collisions on the hot path. Distribution target: local dev loop → Researcher HU sandbox submission (next after `a0e7bff8`).

## Summary

Yesterday's HU submission (`a0e7bff8`, 10k PvP) finished +25 adj BB/100, TrueSkill ~20.9, rank #17/25. The tail 50-hand failure report names two dominant leaks:

1. **SB −10 uncontested folds** — hero open-folds the SB (= BTN seat in HU) too often, bleeding 10 chips/hand without contest. The field is loose-LAG (e.g. #1 `cosmometrics` VPIP 32%); our `cemini_wiki_poker` VPIP was 22.9% — too tight for this pool.
2. **Weak top-pair stack-offs** — big single-hand loss on `Ac3d` weak top pair (thin kicker called down / committed).

K131 does three things in parallel:

- **Track A** — widen HU preflop (SB defend, BTN steal, VPIP toward ~30–35%) so the SB −10 bleed stops and PFR/VPIP match the LAG field.
- **Track B** — postflop discipline (bluff guard vs stations, weak-TP downgrade) **and** finalize/commit the K130 `gin_v2_exploits.py` work that exists but is uncommitted.
- **Track C** — gate calibration (LAG series thresholds in `run_hu_sandbox_gate.sh` + audit), prod-harvest `uv`→`venv` fix, regression tests.

**Hard invariant for all tracks:** 6-max behavior and the M8/M9 trajectory gates must not regress. Everything new is HU-gated (`resolve_table_format(table) == "hu"`) or behind an env flag that defaults off outside HU.

---

## Phased tasks — exact files, functions, constants

### Track A — Preflop HU widen (SB defend, BTN steal, VPIP)

**Owner files (exclusive):** `examples/research_static_chart.py`, `examples/gin_style.py`, `tests/fixtures/hu_regression_spots.py` (append only), new `tests/test_hu_preflop_widen.py`.

**A1 — Widen the HU BTN/SB open chart.**
File: `examples/research_static_chart.py`, dict `_HU_OPEN_CHART["BTN"]["raise"]` (≈ line 30–38).
HU SB maps to BTN chart via `research_static_chart()` line 153–154 (`if fmt == "hu" and pos == "SB": pos = "BTN"`), so this set *is* the SB open range.
Current range ≈ 62% of combos. Target ≈ **78–84%** (a standard HU BTN open is ~80–90%; cap at 84% to keep the worst trash folding).
Add these hand classes to the `raise` set (do **not** add 72o-class trash — keep regression folds intact):
- Offsuit broadways/aces: `KTo`, `QTo`, `QJo`(already), `JTo`, `ATo`(already), `A9o`, `A8o`, `A7o`, `A5o`, `A4o`, `KJo`(already), `K9o`, `Q9o`, `J9o`, `T9o`.
- Suited fill-ins: `K4s`, `K3s`, `K2s`, `Q7s`, `Q6s`, `Q5s`, `Q4s`, `J7s`, `T7s`, `96s`, `85s`, `75s`, `64s`, `53s`, `43s`.
- Keep explicit folds: `72o`,`73o`,`82o`,`83o`,`92o`,`93o`,`T4o`,`Q2o`,`J6o` (these back the existing `hu_sb_*_fold` regression spots — **must still fold**).

**A2 — Lower gin gate-open thresholds for HU SB/BTN.**
File: `examples/gin_style.py`, function `_gin_preflop_thresholds()` (line 82–107), the `if _gin_style_gate_open():` branch (line 88–92).
Current gate-open tuple: `play=34, bet_open=46, raise=58(ip)/64(oop), premium_ip=82, premium_oop=88`.
Add an HU-aware floor. Introduce module constant near line 73:
```
HU_SB_STEAL_BET_OPEN = 40   # gin-score floor for HU SB/BTN first-in open
HU_SB_STEAL_RAISE = 40      # HU collapses raise→bet_open anyway (try_preflop line 378)
```
In `try_preflop()` (line 352), in the HU open branch (after line 376 `hu = resolve_table_format(...)`), when `hu and open_spot and position in ("SB","BTN")`, clamp `bet_open_threshold = min(bet_open_threshold, HU_SB_STEAL_BET_OPEN)`. Bound: never below 38 (keeps 72o/82o/92o which score ≤ ~30 folding; a hand needs score ≥ 38 to open).

**A3 — SB never-fold-uncontested floor (kill the −10 bleed).**
File: `examples/gin_style.py`, new helper `try_preflop_sb_steal_floor(table, allowed, available, hole, position)`.
Logic: HU only, `open_spot` true, `position in ("SB","BTN")`, `preflop_score(hole) >= HU_SB_STEAL_BET_OPEN`, and `"raise"`/`"bet"` in available → return the open wager (reuse `_value_bet_amount` / `_raise_amount`). This is the explicit anti-leak: with a min-openable hand the SB should open rather than fold and surrender 10.
Wire in `examples/cemini_decide.py` `_apply_v008_preflop_rescue()` (line 589–619): the existing block (line 603–612) already converts chart-fold→open when `chart_suggested == "raise"`. Extend the guard so it also fires when `chart_suggested in ("raise","call")` OR `preflop_score >= HU_SB_STEAL_BET_OPEN` for `position in ("SB","BTN")` in HU. Keep `lane_tight` and KO-survival short-circuits intact.

**A4 — VPIP target bump in the audit (Track A owns the constant; Track C owns wiring it into the gate).**
File: `examples/gin_style.py` — add documented constant `HU_TARGET_VPIP_MIN = 0.28`, `HU_TARGET_VPIP_MAX = 0.38` for reference by Track C.
No behavior change here beyond A1–A3; the chart+threshold widen is what moves VPIP. Track A’s job is to land VPIP in [28%, 38%] in `cemini_selfplay_audit.py` HU runs.

**A5 — Tests.**
New file `tests/test_hu_preflop_widen.py`:
- `test_hu_sb_steal_opens_KTo` — `hu_sb_unopened(["Kd","Th"])` → action in `{"raise","bet"}` (was fold).
- `test_hu_sb_steal_opens_Q7s` — `hu_sb_unopened(["Qs","7s"])` → `{"raise","bet"}`.
- `test_hu_sb_steal_opens_J9o` — `hu_sb_unopened(["Jh","9c"])` → `{"raise","bet"}`.
- `test_hu_sb_still_folds_72o` — `hu_sb_unopened(["7h","2c"])` → `fold` (guard the lower bound).
- `test_hu_sb_still_folds_T4o` — `hu_sb_unopened(["Td","4s"])` → `fold`.
Append to `tests/fixtures/hu_regression_spots.py` (after line 89) 3–4 new steal spots mirroring the above so `test_hu_regression_count` (≥20) grows and `test_hu_regression_spots` enforces them. Use `_gin_v008_ctx()` for context. Keep all existing `*_fold` spots unchanged.

---

### Track B — Postflop discipline + K130 finalize

**Owner files (exclusive):** `examples/gin_v2_exploits.py`, `tests/test_gin_v2_exploits.py`, plus the **commit** of the already-staged K130 set. Postflop facing-bet downgrade lives in a new helper in `gin_v2_exploits.py` (do **not** edit `gin_style.py` — that is Track A’s file).

**B1 — Bluff guard vs stations (don’t barrel into a caller).**
File: `examples/gin_v2_exploits.py`, function `try_ip_dry_board_cbet()` (line 189–219).
Problem: IP dry c-bet fires purely on `fold_to_bet >= 0.65`; against a station the same HUD can show high ftb on a stale sample while `call_freq` is high. Add a guard.
New constant near line 31: `IP_DRY_CBET_MAX_CALL_FREQ = 0.62`.
After the `fold_to_bet` check (line 215–216), add:
```
if summary["call_freq"] >= IP_DRY_CBET_MAX_CALL_FREQ:
    return None
```
This routes station spots away from a pure-air bluff c-bet and into the thin-value path instead. Bound: only suppress when confidence ≥ `IP_DRY_CBET_MIN_CONFIDENCE` (already gated at line 213) — cold-start (`confidence==0`) does not over-fold because `fold_to_bet`/`call_freq` use archetype priors only when sample present.

**B2 — Weak top-pair downgrade (the `Ac3d` loss).**
File: `examples/gin_v2_exploits.py`, new function `try_weak_top_pair_pot_control(table, allowed, available, hole, board, *, proposed_action, call_chips, pot, effective_stack)`.
Purpose: when facing a bet, hero holds **top pair with a weak kicker** (kicker rank ≤ 9, e.g. A3 on A-high), and the price/stack-off is large, downgrade `call`/`raise`→`call`-capped or `fold` rather than stacking off.
New constants near line 34:
```
WEAK_TP_KICKER_MAX = 9          # kicker rank ≤ 9 = "weak"
WEAK_TP_FOLD_PRICE = 0.42       # fold weak TP when call price > 42% pot
WEAK_TP_MAX_SPR_COMMIT = 1.5    # below this SPR, allow call (committed); above, fold to big bet
```
Logic (HU solo only, `len(board) >= 3`, `made_hand_rank == 1` and top pair true via a small local kicker check; reuse `made_hand_rank`/`has_top_pair_or_better` imported from `gin_style`):
- Compute `required = call_chips/(pot+call_chips)`.
- If kicker ≤ `WEAK_TP_KICKER_MAX` and `required > WEAK_TP_FOLD_PRICE` and SPR `> WEAK_TP_MAX_SPR_COMMIT` and `"fold" in available` → return `("fold", None)`.
- Else if `"call" in available` and price ≤ `WEAK_TP_FOLD_PRICE` → return `("call", call_chips)` (call down small, no raise).
- Else return `None` (defer).
**Interaction with SPR lock:** this guard must run **only for `made_hand_rank == 1`**; `try_spr_commitment_lock` only fires for `made_hand_rank >= 2` (two-pair+), so there is no overlap — weak TP is never force-committed by the SPR lock.
Wire in `examples/cemini_decide.py` at line 1846–1855 (the `if action_name == "fold" and street != "Preflop":` block): run `try_weak_top_pair_pot_control` **before** the existing fold path too — i.e. when `_postflop_facing_bet` returns `call`/`raise` with weak TP, allow the downgrade to fold/cap. Add it as a second hook right after `_postflop_facing_bet` returns (around line 1845), gated `if gin_v2_exploits_enabled() and action_name in ("call","raise","all-in") and street != "Preflop":`.

**B3 — Finalize + commit K130.**
The K130 work is on disk but uncommitted (`git status`): `examples/gin_v2_exploits.py` (new), `tests/test_gin_v2_exploits.py` (new), `examples/cemini_decide.py` (modified — gin v2 hooks at lines 24–36, 1807–1855), `harness/strategy.py` (modified), `briefs/2026-06-25_k130-...md` (new).
Steps:
1. Run `uv run pytest tests/test_gin_v2_exploits.py -q` → must be green.
2. Run full suite `uv run pytest tests/ -q` → green (esp. `test_hu_regression.py`, `test_cemini_regression.py`).
3. Verify `harness/strategy.py` diff only adds the v2-exploits env-flag wiring (no 6-max behavior change) — `git diff harness/strategy.py`.
4. Commit K130 + B1/B2 together as one logical postflop-discipline commit (user-gated — do not push).

**B4 — Tests (append to `tests/test_gin_v2_exploits.py`).**
- `test_ip_dry_cbet_skips_station` — hud `wide_passive` w/ `call_freq 0.75`, sample 30, dry board → `try_ip_dry_board_cbet(...) is None` (guard B1).
- `test_ip_dry_cbet_still_fires_vs_nit` — existing `test_ip_dry_cbet_fires_vs_folder` keeps passing (premium_nit, low call_freq).
- `test_weak_tp_folds_big_bet` — `Ac3d` on `Ah 9c 2s`, `pot=300 call_chips=180 hero_stack=400` → `try_weak_top_pair_pot_control` returns `("fold", None)`.
- `test_weak_tp_calls_small` — same hand, `call_chips=40 pot=300` → `("call", 40)`.
- `test_weak_tp_skips_strong_kicker` — `AcKd` on `Ah 9c 2s` (kicker K > 9) → `None` (don’t downgrade real TP).
- `test_weak_tp_skips_two_pair` — `Ac9d` on `Ah 9c 2s` (two pair, rank ≥ 2) → `None` (SPR lock’s job).

---

### Track C — Gates + tooling

**Owner files (exclusive):** `scripts/run_hu_sandbox_gate.sh`, `scripts/run_sandbox_season_harvest.sh`, `examples/cemini_selfplay_audit.py` (LAG-gate wiring only — coordinate the one constant name with Track A), new `tests/test_harvest_venv.py` (smoke).

**C1 — Wire the LAG series into the HU gate.**
File: `scripts/run_hu_sandbox_gate.sh`, the `hu)` case (line 131–149).
The audit already runs a `lag` profile in HU mode (`cemini_selfplay_audit.py` line 196 `profiles = ("rock","maniac","lag")`) but the gate invocation (line 137–143) passes only `--min-match-win-rate 0.55` and `--min-match-win-maniac 0`. Add:
```
--min-match-win-lag 0.45 \
```
to the `cemini_selfplay_audit.py` call (line 139–143). Rationale: the field is loose-LAG; LAG series win rate is now a *gated* metric (target ≥ 45%), maniac stays advisory. Print an advisory line for `series_win_rate (lag):` mirroring the maniac block (line 144–147).

**C2 — VPIP floor in HU gate.**
File: `examples/cemini_selfplay_audit.py`, `main()` line 395–397.
Currently `min_vpip = 0.18` when `CEMINI_GIN_STYLE` on. Raise the HU floor to match Track A’s target: when `hu_mode`, set `min_vpip = max(min_vpip, 0.26)` (lower bound of the [28%,38%] target minus tolerance). Add CLI override `--min-vpip` (default None → 0.26 HU / 0.18 6-max). Do **not** change 6-max default.
Also add an **upper** VPIP advisory: if `vpip_rate > 0.42` print a warning (over-loose) but do not gate-fail — avoids overcorrection.

**C3 — Prod harvest `uv`→`venv` fix.**
File: `scripts/run_sandbox_season_harvest.sh`, lines 45 and 119 use `uv run python` which fails on prod (no `uv`). Adopt the venv-aware pattern already used by `scripts/run_export_harvest_worker.sh` (line 27–30):
```
PY="$(cd "$(dirname "$0")/.." && pwd)/venv/bin/python"
if [[ ! -x "${PY}" ]]; then PY="$(command -v uv) run python"; fi   # local fallback
```
Then replace `uv run python` (line 119) with `"${PY}"` and the heredoc invocation (line 45 `uv run python - <<'PY'`) with `"${PY}" - <<'PY'`. Keep `python3 -c` one-liners (lines 97, 142) as-is — they need no venv. Verify both code paths: prod (`venv/bin/python` exists) and laptop (`uv run python`).

**C4 — Regression / smoke tests.**
- New `tests/test_harvest_venv.py`: assert `scripts/run_sandbox_season_harvest.sh` contains no bare `uv run python` (regex) and references `venv/bin/python` — guards the prod fix from regressing.
- Add a CI-cheap shellcheck note (optional): `bash -n scripts/run_sandbox_season_harvest.sh` parses clean.
- Confirm `scripts/run_hu_sandbox_gate.sh` still parses: `bash -n scripts/run_hu_sandbox_gate.sh`.

---

## Test commands per track

**Track A**
```bash
cd agents/devfun-poker-arena
uv run pytest tests/test_hu_preflop_widen.py tests/test_hu_regression.py -q
# VPIP / SB-fold check (must land VPIP in [28%,38%], SB fold-rate down):
CEMINI_TABLE_FORMAT=hu CEMINI_GIN_STYLE=1 CEMINI_GIN_V008=1 \
  uv run python examples/cemini_selfplay_audit.py --players 2 --hands 400 --seed 42
```

**Track B**
```bash
cd agents/devfun-poker-arena
uv run pytest tests/test_gin_v2_exploits.py -q
uv run pytest tests/ -q                       # full suite green before commit
git diff --stat harness/strategy.py examples/cemini_decide.py
```

**Track C**
```bash
cd agents/devfun-poker-arena
bash -n scripts/run_sandbox_season_harvest.sh
bash -n scripts/run_hu_sandbox_gate.sh
uv run pytest tests/test_harvest_venv.py -q
# Full HU gate with new LAG threshold (slow, ~5-8 min):
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 200
```

**Integration (after all three merge):**
```bash
CEMINI_TABLE_FORMAT=hu CEMINI_GIN_STYLE=1 CEMINI_GIN_V008=1 CEMINI_GIN_V2_EXPLOITS=1 \
  ./scripts/run_hu_sandbox_gate.sh --hands 200
uv run pytest tests/ -q
```

---

## Acceptance criteria (metrics)

| # | Metric | Source | Pre-K131 | Target |
|---|--------|--------|----------|--------|
| AC1 | HU SB open-fold rate (uncontested −10) | `cemini_selfplay_audit.py` VPIP-by-seat SB row | high (VPIP 22.9% live) | SB VPIP up; fold-uncontested ↓ materially |
| AC2 | HU VPIP (all) | audit, `--players 2` | 22.9% | **28–38%** |
| AC3 | HU PFR | audit | 19.4% | ≥ 20%, VPIP−PFR gap ≤ 10% |
| AC4 | LAG series win rate | gate `series_win_rate (lag)` | n/a (ungated) | **≥ 45%** (gated) |
| AC5 | rock series win rate | gate | ~0.55 floor | ≥ 55% (unchanged gate) |
| AC6 | WSD proxy / showdown discipline | `try_weak_top_pair_pot_control` unit tests + no thin-value regression | — | B4 tests green; thin-value still fires vs station |
| AC7 | Bluff-into-station rate | B1 guard | fires on stale ftb | 0 IP dry c-bets when `call_freq ≥ 0.62` |
| AC8 | Full gate | `run_hu_sandbox_gate.sh` | PASS | **PASS** with LAG gate on |
| AC9 | Tests | `pytest tests/ -q` | green | green (all new tests added) |
| AC10 | Prod harvest | `run_sandbox_season_harvest.sh` on prod | breaks (no `uv`) | runs via `venv/bin/python` |

A submission is **GO** only when AC2–AC5, AC8, AC9 all pass on a 200-hand gate (advisory: 400-hand audit for AC2/AC3 stability).

---

## Risks / don't-break

1. **M8/M9 trajectory gates** — `researcher_trajectory_summary.py --gate` runs at the end of `run_hu_sandbox_gate.sh` (line 166–167). Widening VPIP raises variance; if M8/M9 axis gates trip, **narrow the A1 chart additions** (drop the loosest suited fill-ins `85s/53s/43s` and offsuit `A4o/A5o` first) rather than disabling the steal floor. Re-run the full gate before claiming done.
2. **6-max must be untouched.** Track A edits only `_HU_OPEN_CHART` (HU dict) and HU-gated branches in `gin_style.try_preflop` (guard with `if hu and position in ("SB","BTN")`). Do **not** touch `_OPEN_CHART` (6-max) or the non-`_gin_style_gate_open()` thresholds. Track C’s `min_vpip` change is `hu_mode`-only. Verify `tests/test_cemini_regression.py` stays green.
3. **EP trash-open gate** (`max_ep_trash_raises=0`, `cemini_selfplay_audit.py` line 98–100, 288) — UTG/MP only, so HU widen can’t trip it; but the 6-max `mixed` audit must still show 0 EP trash opens. Re-run 6-max audit if any shared file changed.
4. **SPR-lock / weak-TP overlap** — B2 must guard `made_hand_rank == 1` exactly; `try_spr_commitment_lock` is `>= 2`. Test `test_weak_tp_skips_two_pair` proves no double-handling.
5. **HUD cold-start** — B1 station guard must not fire at `confidence == 0` (no sample) or it suppresses legitimate cold c-bets. The `confidence < IP_DRY_CBET_MIN_CONFIDENCE` early-return (line 213) already protects this; keep the new guard *after* it.
6. **Reasoning YAML ≤150 chars** (AGENTS.md hard rule #3) — any new message string in `cemini_decide.py` hooks must respect the cap. New hooks here return `(action, amount)` and reuse `_message()`, so no new YAML — keep it that way.
7. **No file collisions** — Track A owns `gin_style.py` + `research_static_chart.py`; Track B owns `gin_v2_exploits.py`. Both wire into `cemini_decide.py` at **different, non-adjacent** line ranges (A: `_apply_v008_preflop_rescue` ~589–619; B: postflop hook ~1845–1855). If both must edit `cemini_decide.py`, serialize the merge (A first, then B rebases) to avoid a hot-path conflict. Track C touches no shared Python except the audit constant — coordinate the `min_vpip`/`HU_TARGET_VPIP_MIN` name with Track A once.
8. **Don't push.** All commits are user-gated; no `git push`, no Arena `pokerkit run` without per-action confirmation (AGENTS.md first-turn handshake).

## Sources

- HU submission `a0e7bff8` tail 50-hand failure report (2026-06-25)
- `examples/gin_style.py`, `examples/gin_v2_exploits.py`, `examples/cemini_decide.py` (gin hooks lines 24–36, 589–619, 1807–1855)
- `examples/research_static_chart.py` `_HU_OPEN_CHART` (lines 27–56)
- `examples/cemini_selfplay_audit.py` (LAG profile line 196, gate thresholds 124–136, `min_vpip` 395)
- `scripts/run_hu_sandbox_gate.sh` (HU case 131–149), `scripts/run_export_harvest_worker.sh` (venv pattern 27–30), `scripts/run_sandbox_season_harvest.sh` (`uv run` lines 45, 119)
- `tests/test_hu_regression.py`, `tests/fixtures/hu_regression_spots.py`, `tests/test_gin_v2_exploits.py`
- K130 brief `briefs/2026-06-25_k130-gin-v2-exploits-implementation.md`
