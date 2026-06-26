## Target

`agents/devfun-poker-arena/` — K131b HU sandbox tune wave. Follow-up to K131 (`2026-06-26_k131-sandbox-improvement-plan.md`). **Two parallel implementation tracks (A/B)**, each scoped to a separate agent with no file collisions on the hot path. Distribution target: local dev loop → Researcher HU sandbox submission (next after the last K131 commit).

## Summary

K131 widened the HU BTN/SB steal and wired the LAG-series gate (`--min-match-win-lag 0.45`, `HU_MIN_VPIP_FLOOR=0.26`). The 400-hand post-K131 audit shows the widen overshot on BTN and **did not touch the two real leaks**:

| Metric | Post-K131 (400h) | Target |
|---|---|---|
| VPIP (all) | **40.8%** | **30–38%** |
| VPIP BTN (= SB seat) | 54.5% | trim → low-50s/high-40s |
| VPIP BB | **18.5%** | **materially up (≈30–38%)** |
| LAG series win rate | **40%** (gate FAIL, needs ≥45%) | **≥45%** |

Diagnosis:

1. **BB defends far too tight (18.5%).** In HU, hero is BB half the time facing a single opener and should defend ~55–70% vs a min-raise. The `_WEAK_FACING_RAISE` BB fold-guard in `cemini_decide.py` (line 2319–2322) fires **in HU too** — it has no `hu_bb_exploit` guard (unlike the `_BB_BROADWAY_FOLD` guard at line 2332). It folds all A2o–A9o, K/Q/J/T-x offsuit, and most offsuit connectors *before* the HU BB defend block (line 2338+) ever runs. The downstream defend set `_BB_DEFEND_VS_STEAL` (s1b_exploit.py line 28–33) is also only ~40% wide and lacks offsuit broadways/connectors.
2. **vs-LAG postflop over-folds.** The selfplay LAG bot (`selfplay.py` `bot_balanced_lag`, line 170–194) c-bets 58% when checked to, raises 32% facing a bet, and is **bluff-heavy**. Hero's `_postflop_facing_bet` only nudges `raise_bar -= 0.05` for `lag_like` (line 4234–4235) but never **calls down wider** against LAG's frequent bets. Hero folds too many marginal-but-ahead hands to LAG bluffs → series < 45%.

**The fix is a rebalance, not a further widen.** BB openness goes up; BTN comes down a touch so total VPIP lands back in [30%, 38%]; postflop hero stops over-folding to LAG. This is fully consistent with the K131b instruction "BB defend + vs-LAG postflop **without** further BTN widen" — Track A trims BTN (it does not widen it).

- **Track A — BB preflop defend + BTN rebalance.** Gate the HU BB over-fold guard, widen the HU BB defend range, trim the loosest BTN opens so VPIP re-centers.
- **Track B — vs-LAG postflop discipline.** LAG-aware call-down (defend wider vs LAG c-bets) + LAG-aware thin value, to push LAG series ≥45%.

**Hard invariant for both tracks:** 6-max behavior and the M8/M9 trajectory gates must not regress. Everything new is HU-gated (`_is_hu_table(table)` / `resolve_table_format(table) == "hu"`) or LAG-archetype-gated; nothing changes the 6-max `_OPEN_CHART`, 6-max BB guards, or the rock/nit postflop lines.

---

## Phased tasks — exact files, functions, constants

### Track A — BB preflop defend + BTN rebalance

**Owner files (exclusive):** `examples/research_static_chart.py`, `examples/s1b_exploit.py`, `examples/cemini_decide.py` **(preflop BB region only, ~line 2310–2410)**, `tests/fixtures/hu_regression_spots.py` (append only), new `tests/test_hu_bb_defend.py`.

**A1 — Gate the HU BB over-fold guard so HU BB reaches the defend block.**
File: `examples/cemini_decide.py`, function `_preflop_vs_bet`.
The `hu_bb_exploit` flag is computed at line 2326–2331. The `_WEAK_FACING_RAISE` BB fold at line 2319–2322 fires before the HU defend block (2338+) and has **no** HU guard. Change it to skip in HU (mirror the `not hu_bb_exploit` pattern already used at line 2332–2335):

```python
# BB: never defend chart-trash vs raises (Q6o BB −100 — IP preflop pricing leak).
# HU: skip — HU BB defends wider via try_defend_bb_vs_steal below (K131b A1).
if (position == "BB" and call_chips > 0 and hc in _WEAK_FACING_RAISE
        and hc not in {"AA", "KK", "QQ", "JJ", "TT", "AKs", "AKo", "AQs", "AQo"}
        and not hu_bb_exploit
        and "fold" in available):
    return "fold", None
```

**Important ordering bug:** `hu_bb_exploit` is currently defined at line 2326, *after* the 2319 guard. Move the `hu_bb_exploit = (...)` assignment (lines 2326–2331) **up above** the 2314 "downgrade spurious raise" block (i.e. just after `bb_chase_steal` is computed at line 2311) so it is in scope for the 2319 guard. No other behavior change — it is a pure read of `_is_hu_table`, `s1b_exploit_enabled`, `position`, `call_chips`.

Also confirm the two other HU-reachable BB fold-guards do **not** strip legitimate defends:
- `_is_bb_suited_trash` (line 2472–2474) — keep as-is; it only folds genuine low suited junk (T2s/93s-class). Acceptable.
- `_marginal_ace_kicker` is **SB-only** (line 2468) — not BB; no change.

**A2 — Widen the HU BB defend range (HU-gated, 6-max untouched).**
File: `examples/s1b_exploit.py`.
Add an HU-specific defend set next to `_BB_DEFEND_VS_STEAL` (line 28–33). Do **not** widen `_BB_DEFEND_VS_STEAL` itself — it is also used by the 6-max `placement_chase` path (`cemini_decide.py` line 2298), so widening it would regress 6-max.

```python
# HU BB closes the action vs a single opener at a great price — defend ~60%.
# Adds offsuit broadways + offsuit connectors + suited fill-ins on top of
# the 6-max top-40% set. Trash (72o/83o/T3o/Q5o/J6o-class) stays OUT.
_HU_BB_DEFEND_VS_STEAL = _BB_DEFEND_VS_STEAL | frozenset({
    # offsuit broadways / aces
    "AJo", "ATo", "A9o", "A8o", "A7o", "A6o", "A5o", "A4o", "A3o", "A2o",
    "KQo", "KJo", "KTo", "K9o", "QJo", "QTo", "Q9o", "JTo", "J9o", "T9o", "T8o", "98o",
    # suited fill-ins not already in the steal set
    "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s",
    "Q9s", "Q8s", "Q7s", "Q6s", "Q5s", "J9s", "J8s", "T8s", "T7s", "97s", "86s", "75s", "64s", "53s",
})
```

Thread an `hu` flag into `try_defend_bb_vs_steal` (line 315–338) and pick the set + relax the price margin for HU (BB closing vs a min-raise is getting 2:1+):

```python
def try_defend_bb_vs_steal(
    *,
    hand_class: str,
    position: str,
    call_chips: int,
    pot_odds: float,
    equity: float,
    available: list,
    hero_stack_chips: int,
    hu: bool = False,
) -> tuple[str, int | None] | None:
    """Bounded BB defend vs steal — top-40% (6-max) / ~60% (HU), max 30% stack."""
    if position != "BB":
        return None
    defend_set = _HU_BB_DEFEND_VS_STEAL if hu else _BB_DEFEND_VS_STEAL
    if hand_class not in defend_set:
        return None
    if call_chips <= 0:
        return None
    if call_chips > hero_stack_chips * _max_call_frac_stack():
        return None
    # HU BB closes a single opener cheaply — looser equity margin than 6-max.
    margin = 0.0 if hu else 0.02
    if equity < pot_odds + margin:
        return None
    if "call" in available:
        return "call", None
    return None
```

Pass `hu=_is_hu_table(table or {})` at **both** `try_defend_bb_vs_steal` call sites in `cemini_decide.py` (the `placement_chase` path ~line 2298, and the `hu_bb_exploit` path ~line 2377). The first site is 6-max-reachable, so it must pass `hu=False` there unless HU — `_is_hu_table` already resolves that correctly.

**A3 — Trim the loosest HU BTN opens (rebalance VPIP, do NOT widen).**
File: `examples/research_static_chart.py`, `_HU_OPEN_CHART["BTN"]["raise"]` (line 30–38).
K131 pushed this to ≈82–84%. Drop the loosest ~10 combos to bring BTN VPIP from 54.5% toward ~48% so total VPIP re-centers when BB rises. **Remove** (and only these): `K2s`, `K3s`, `Q4s`, `Q5s`, `J7s`, `85s`, `75s`, `64s`, `53s`, `43s`, `A4o`, `A5o`.
**Must NOT remove** (each backs a `hu_sb_*_open` regression spot that requires `raise`/`bet`): `KTo`, `Q7s`, `J9o`, `76s`, `98s`, `JTs`, `QJs`, `QJo`, `ATo`, `A9o`, and all premium pairs/broadways.

Mirror the BB chart for consistency: add the A2 offsuit broadways/connectors to `_HU_OPEN_CHART["BB"]["call"]` (line 47–54) so `research_static_chart` reports `call` (not `fold`) for the hands the defend set now defends. (Cosmetic for telemetry/`suggested` — the gating path is A1+A2; keep them in sync to avoid confusing `analyze` output.)

**A4 — VPIP advisory alignment.**
File: `examples/gin_style.py` — constants `HU_TARGET_VPIP_MIN = 0.28` / `HU_TARGET_VPIP_MAX = 0.38` already exist (line 76–77). No change. Track A's job is to land VPIP in [30%, 38%] **and** lift BB VPIP materially in `cemini_selfplay_audit.py` HU runs. The audit's `HU_MAX_VPIP_ADVISORY = 0.42` (line 140) will now warn if BTN trim is insufficient — use it as the upper-bound signal.

**A5 — Tests.**
New file `tests/test_hu_bb_defend.py` (use `hu_bb_vs_minraise` from `tests/helpers/cemini_tables.py` + `_gin_v008_ctx()` + `CEMINI_S1B_EXPLOIT=1`):
- `test_hu_bb_defends_KTo` — `hu_bb_vs_minraise(["Kd","Th"])` → action in `{"call","raise"}` (was fold).
- `test_hu_bb_defends_QJo` — `hu_bb_vs_minraise(["Qs","Jc"])` → `{"call","raise"}`.
- `test_hu_bb_defends_A8o` — `hu_bb_vs_minraise(["Ah","8c"])` → `{"call","raise"}`.
- `test_hu_bb_defends_J9o` — `hu_bb_vs_minraise(["Jh","9c"])` → `{"call","raise"}`.
- `test_hu_bb_still_folds_72o` — `hu_bb_vs_minraise(["7h","2c"])` → `fold` (lower bound; backs `hu_bb_72o_vs_minraise`).
- `test_hu_bb_still_folds_Q5o` — `hu_bb_vs_minraise(["Qs","5c"])` → `fold` (backs `hu_bb_q5o_vs_minraise`).
- `test_hu_bb_still_folds_T3o` — `hu_bb_vs_minraise(["Tc","3h"])` → `fold`.
Append to `tests/fixtures/hu_regression_spots.py` (after line 216, in the BB DEFEND block) 3–4 new **defend** spots mirroring the above (KTo/QJo/A8o defend) so `test_hu_regression_count` grows and `test_hu_regression_spots` enforces them. Use `context=_gin_v008_ctx()` plus `"CEMINI_S1B_EXPLOIT": "1"`. **Keep every existing `*_vs_minraise` fold spot unchanged** (72o/83o/T3o/Q5o must still fold).
6-max guard: add/confirm `tests/test_cemini_regression.py` stays green — a 6-max BB-vs-open fold spot (e.g. Q6o/A6o BB) must still fold (proves `_HU_BB_DEFEND_VS_STEAL` did not leak into 6-max).

---

### Track B — vs-LAG postflop discipline

**Owner files (exclusive):** `examples/cemini_decide.py` **(postflop `_postflop_facing_bet`, ~line 4213–4250)**, `examples/gin_v2_exploits.py` (`villain_pressure_summary` priors + thin-value floor only), `tests/test_gin_v2_exploits.py` (append), new `tests/test_lag_postflop.py`.
**No collision with Track A:** A edits the preflop BB region (~2310–2410); B edits the postflop facing-bet region (~4213–4250) — non-adjacent. If both must land in `cemini_decide.py`, serialize the merge (A first, then B rebases).

**B1 — LAG-aware call-down (defend wider vs LAG's high c-bet frequency).**
File: `examples/cemini_decide.py`, `_postflop_facing_bet`.
Today `lag_like` (line 4229–4231) only adjusts `raise_bar`. Add a **call-down** adjustment in the marginal band so hero stops folding ahead-but-marginal hands to LAG bluffs. After the `lag_like` block (around line 4235, before the `raise_bar` raise check at 4236), insert:

```python
# vs LAG: defend wider — LAG c-bets ~58% and is bluff-heavy. Lower the fold
# line / call line so marginal-but-ahead hands call instead of folding.
# Bounded so it never turns a clear fold (equity << price) into a call.
if lag_like:
    fold_slack += LAG_FOLD_SLACK_BONUS      # push fold_line lower
    call_margin = max(0.0, call_margin - LAG_CALL_MARGIN_RELIEF)
```

New module constants near the top of `cemini_decide.py` (next to other postflop tunables; keep names greppable):

```python
LAG_FOLD_SLACK_BONUS = 0.05      # widen call vs LAG bluffs (fold_line down 5%)
LAG_CALL_MARGIN_RELIEF = 0.03    # lower call_line so marginal hands call
```

Bounds / don't-break:
- This runs **only** when `lag_like` is true (`arch == "linear_aggro" or hud_mode == "lag" or (maniac and not hyper_maniac)`), so rock/nit/hyper-maniac lines are untouched.
- It applies on top of `fold_slack`/`call_margin` after all the **made-hand fold guards** (paired-board, three-flush, weak-ace, overcommit at line 4190–4221) — so it never widens calls with literal air; those guards still fold first.
- `call_margin` is floored at 0.0; `fold_slack` total stays < ~0.12 so `fold_line = pot_odds − fold_slack` cannot go negative for realistic prices. Verify against `fold_probability_marginal` (`action_mix.py` line 34–50): lower `fold_line` + lower `call_line` ⇒ higher call frequency, exactly the intent.

**B2 — LAG-aware thin value (LAG calls ~62% — value-bet one pair thinner).**
File: `examples/gin_v2_exploits.py`.
The `lag` opponent maps to archetype `linear_aggro` (`opponent_hud_stub.py` line 142–143). `villain_pressure_summary` (line 81–124) gives `linear_aggro` a `call_freq` prior of **0.45** (line 106), below the thin-value floor `THIN_VALUE_CALL_FREQ_MIN = 0.70` (line 35) — so `try_high_wtsd_thin_value_bet` never fires vs LAG even though the bot calls 62%. Two bounded edits:
1. Raise the `linear_aggro` `call_freq` prior to **0.58** (line 106) to reflect the real LAG call frequency. Leave `wide_passive` (0.75) and `premium_nit` (0.30) unchanged.
2. Add a LAG-specific thin-value floor so one-pair value bets fire vs LAG without lowering the bar for genuine stations:

```python
THIN_VALUE_CALL_FREQ_MIN = 0.70
THIN_VALUE_CALL_FREQ_MIN_LAG = 0.55   # linear_aggro calls wide enough to value-bet thin
```

In `try_high_wtsd_thin_value_bet` (line 230–259), choose the floor by archetype:

```python
summary = villain_pressure_summary(hud)
floor = (
    THIN_VALUE_CALL_FREQ_MIN_LAG
    if summary["archetype"] == "linear_aggro"
    else THIN_VALUE_CALL_FREQ_MIN
)
if summary["confidence"] < THIN_VALUE_MIN_CONFIDENCE:
    return None
if summary["call_freq"] < floor:
    return None
# fold_to_bet check unchanged (line 255-256)
```

Bounds: still gated on `_is_hu_solo`, `made_hand_rank == 1`, and `confidence >= THIN_VALUE_MIN_CONFIDENCE` — cold-start (confidence 0) still does not fire, so this only activates once the LAG sample is real.

**B3 — Tests.**
New file `tests/test_lag_postflop.py`:
- `test_lag_calls_down_marginal` — construct an OOP facing-bet HU table vs LAG (`villain_archetype="linear_aggro"` / `hud_mode="lag"`) where `equity` sits just below `pot_odds` (e.g. equity 0.30, pot_odds 0.33) → `_postflop_facing_bet(...)` returns `call` (would be `fold` without B1). Add the mirror `test_nonlag_still_folds_marginal` with `hud_mode="rock"` same equity/price → `fold` (proves B1 is LAG-gated).
- Bound test `test_lag_calldown_still_folds_air` — equity far below price (0.12 vs 0.40) vs LAG → still `fold` (B1 never calls pure air).
Append to `tests/test_gin_v2_exploits.py`:
- `test_thin_value_fires_vs_lag` — hud `linear_aggro`, `call_freq 0.60`, sample ≥ `PROFILE_CONF_SAMPLE_FULL`, one-pair HU solo, dry-ish board → `try_high_wtsd_thin_value_bet(...)` returns `("bet", _)`.
- `test_thin_value_skips_lag_low_callfreq` — same but `call_freq 0.50` (< LAG floor) → `None`.
- `test_thin_value_station_floor_unchanged` — `wide_passive`, `call_freq 0.68` (< 0.70) → `None` (non-LAG floor not lowered).

**B4 — Do not commit until green.** Run `uv run pytest tests/test_lag_postflop.py tests/test_gin_v2_exploits.py tests/test_hu_regression.py tests/test_cemini_regression.py -q` → all green. Commit Track B as one logical "vs-LAG postflop discipline" commit (user-gated — do not push).

---

## Test commands per track

**Track A**
```bash
cd "agents/devfun-poker-arena"
uv run pytest tests/test_hu_bb_defend.py tests/test_hu_regression.py tests/test_cemini_regression.py -q
# BB-VPIP / total-VPIP rebalance check (BB up, total in [30%,38%]):
CEMINI_TABLE_FORMAT=hu CEMINI_GIN_STYLE=1 CEMINI_GIN_V008=1 CEMINI_S1B_EXPLOIT=1 \
  uv run python examples/cemini_selfplay_audit.py --players 2 --hands 400 --seed 42
```

**Track B**
```bash
cd "agents/devfun-poker-arena"
uv run pytest tests/test_lag_postflop.py tests/test_gin_v2_exploits.py -q
uv run pytest tests/ -q                       # full suite green before commit
git diff --stat examples/cemini_decide.py examples/gin_v2_exploits.py
```

**Integration (after both tracks merge):**
```bash
cd "agents/devfun-poker-arena"
CEMINI_TABLE_FORMAT=hu CEMINI_GIN_STYLE=1 CEMINI_GIN_V008=1 \
  CEMINI_S1B_EXPLOIT=1 CEMINI_GIN_V2_EXPLOITS=1 CEMINI_RESEARCHER_MODE=1 \
  ./scripts/run_hu_sandbox_gate.sh --hands 200
uv run pytest tests/ -q
```

---

## Acceptance criteria (metrics)

| # | Metric | Source | Post-K131 | Target |
|---|--------|--------|-----------|--------|
| AC1 | HU BB VPIP | `cemini_selfplay_audit.py` VPIP-by-seat BB row | 18.5% | **materially up (≈30–38%)** |
| AC2 | HU VPIP (all) | audit `--players 2` | 40.8% | **30–38%** |
| AC3 | HU BTN VPIP | audit, BTN/SB seat row | 54.5% | trimmed (≈46–50%), still ≥ BB |
| AC4 | LAG series win rate | gate `series_win_rate (lag)` | 40% (FAIL) | **≥ 45%** (gated) |
| AC5 | rock series win rate | gate | ≥ 0.55 | ≥ 55% (unchanged gate) |
| AC6 | maniac series | gate (advisory) | — | no regression vs K131 |
| AC7 | HU PFR / VPIP−PFR gap | audit | — | gap ≤ 10% (unchanged HU gate) |
| AC8 | Full HU gate | `run_hu_sandbox_gate.sh` | FAIL (LAG) | **PASS** |
| AC9 | Tests | `pytest tests/ -q` | green | green (all new tests added) |
| AC10 | 6-max untouched | `test_cemini_regression.py` + 6-max `mixed` audit | green | green, 0 EP trash opens |

A submission is **GO** only when AC1–AC5, AC8, AC9 all pass on a 200-hand gate (advisory: 400-hand audit for AC1/AC2/AC3 stability).

---

## Risks / don't-break

1. **VPIP overshoot the other way.** If the BTN trim (A3) over-corrects and total VPIP drops below 30% (or HU PFR < 0.12 floor), restore the suited fill-ins first (`Q5s`, `J7s`) before any offsuit ace. If BB widen (A2) pushes total > 38%, trim 2–3 more of the loosest BTN suited combos (`Q4s`-class) rather than narrowing BB — BB defend is the explicit goal.
2. **6-max must be untouched.** Track A's `_HU_BB_DEFEND_VS_STEAL` is HU-gated via the `hu=` flag; `_BB_DEFEND_VS_STEAL` (6-max) is unchanged. The A1 guard change adds `and not hu_bb_exploit`, which is False in 6-max, so the 6-max BB fold path is byte-identical. Verify `test_cemini_regression.py` + a 6-max BB-vs-open fold spot stay green.
3. **B1 must not turn air into calls.** The LAG call-down runs **after** the paired-board / three-flush / weak-ace / overcommit fold guards (line 4190–4221) and only widens the *marginal* band. `test_lag_calldown_still_folds_air` proves it. Keep `call_margin` floored at 0.0 and total `fold_slack` < ~0.12.
4. **B1/B2 LAG-gating.** Both fire only when `lag_like` / `archetype == "linear_aggro"`. Confirm `hud_mode`/`villain_archetype` actually reach `_postflop_facing_bet` in the audit (they are passed at `cemini_decide.py` line 1858–1859 from `villain_archetype` set at line 854). `test_nonlag_still_folds_marginal` guards against accidental application to rock.
5. **Thin-value cold-start.** B2 lowers only the *LAG* call_freq floor and keeps the `confidence >= THIN_VALUE_MIN_CONFIDENCE` gate — so it never fires on a zero-sample read. The `wide_passive`/`premium_nit` priors are unchanged.
6. **M8/M9 trajectory gates** run at the end of `run_hu_sandbox_gate.sh` (line 171–172, `researcher_trajectory_summary.py`). Wider BB defend + wider LAG call-down raises variance; if an axis gate trips, narrow A2 (drop the loosest offsuit aces `A2o`–`A4o` and suited `53s`/`64s` from `_HU_BB_DEFEND_VS_STEAL`) before touching B1. Re-run the full gate before claiming done.
7. **Reasoning YAML ≤150 chars** (AGENTS.md hard rule #3). New hooks return `(action, amount)` and reuse `_message()` — no new YAML strings. Keep it that way.
8. **No file collisions.** Track A owns `research_static_chart.py` + `s1b_exploit.py` + the preflop BB region of `cemini_decide.py`; Track B owns `gin_v2_exploits.py` + the postflop region of `cemini_decide.py`. The two `cemini_decide.py` edits are non-adjacent (~2310–2410 vs ~4213–4250). If both land in the same branch, serialize (A first, B rebases).
9. **Don't push.** All commits user-gated; no `git push`, no Arena `pokerkit run` without per-action confirmation (AGENTS.md first-turn handshake).

## Sources

- Post-K131 400h HU audit (VPIP 40.8% / BTN 54.5% / BB 18.5%; LAG series 40% FAIL)
- K131 plan `briefs/2026-06-26_k131-sandbox-improvement-plan.md`
- `examples/cemini_decide.py` — `_preflop_vs_bet` BB region (lines 2184–2410, esp. `_WEAK_FACING_RAISE` guard 2319, `hu_bb_exploit` 2326–2331, defend block 2338–2387); `_postflop_facing_bet` LAG block (lines 4225–4250); `villain_archetype`/`villain_vpip` wiring (lines 854, 1858–1859); BB guard sets (`_WEAK_FACING_RAISE` 425, `_BB_BROADWAY_FOLD` 445)
- `examples/s1b_exploit.py` — `_BB_DEFEND_VS_STEAL` (28–33), `try_defend_bb_vs_steal` (315–338), `exploit_lane_active` HU-always (105–112)
- `examples/research_static_chart.py` — `_HU_OPEN_CHART` BTN (30–38) + BB (41–55), SB→BTN map (153–154)
- `examples/gin_v2_exploits.py` — `villain_pressure_summary` priors (95, 106), `try_high_wtsd_thin_value_bet` (230–259), thin-value constants (35–37)
- `examples/action_mix.py` — `fold_probability_marginal` (34–50), `resolve_postflop_call_fold` (53–85)
- `examples/selfplay.py` — `bot_balanced_lag` (170–194: 58% c-bet, 32% raise, 62% call)
- `examples/cemini_selfplay_audit.py` — LAG profile (200), LAG gate (338–345), `HU_MIN_VPIP_FLOOR`/`HU_MAX_VPIP_ADVISORY` (139–140), `min_vpip` (406–412)
- `scripts/run_hu_sandbox_gate.sh` — HU case + LAG advisory (131–153), trajectory gate (171–172)
- `tests/fixtures/hu_regression_spots.py` (BB defend + trash-fold spots 158–216), `tests/helpers/cemini_tables.py` (`hu_bb_vs_minraise` 245–266)
