# Eval −17 bb/100 vs Playground chip #1 — posture gap (2026-06-08)

## Target

Operator decision before S1b / main KO. **No deploy** until eval direction is agreed.

## Summary

Overnight **Poker Eval S1** (`seed_poker_eval_s1`, 500 hands vs DeepCFR reference panel):

| Metric | Value | Kit baseline |
|--------|-------|--------------|
| `adjustedBbPer100` | **−17.45** | L1 heuristic −15 to −5 |
| `rawBbPer100` | −37.8 | same panel, no adjustment |
| Mid-run peak | **+13 bb/100** @ hand ~390 | — |
| Collapse | **+9.8 → −10.4** between hands 452–454 | ~48-hand tail wipe |

Playground S1a (same `decide()`, different scoring + context):

| Metric | Value |
|--------|-------|
| Chip rank | #1 (139,946 chips, 2,362 hands) |
| UI adjusted bb/100 | +2,820 (chip-proxy field; not API) |
| EV rank (≥400 hands, UI log) | **#3** behind Jeff (+3,670) and Jagoan (+2,828) |
| Runtime posture | **`first_protect ON`** via lobby |

**Verdict:** Playground qualification strategy is working on **today's chip metric**. Eval score says we are **below starter-kit baseline** vs the panel that end-tournament / S1b scoring will resemble (raw bb/100 today; V2 all-in EV + V3 AIVAT later — server-side only, no `decide()` API change).

## Root cause (evidence)

### 1. Metric + context mismatch (not luck alone)

- Playground ranks **`totalChips`** in a persistent pool; nit + `first_protect` + HUD exploit gates maximize survival and big pots.
- Eval resets **100bb/hand** vs fixed DeepCFR panel; chip-hoarding logic does not transfer.
- **`first_protect` is lobby-only** (`run_cemini_lobby.py` → `research_context`). Benchmark/eval path (`agent.py`) does **not** set it — R25/R26 guards tied to `first_protect` **do not run on eval**.

### 2. Structural leak: preflop −100 streaks (eval analyze, last 100 hands)

Prod `analyze.py --match seed_poker_eval_s1`:

- **3W / 75L / 22 push** in sample
- Worst positions: **SB −78**, UTG −63, CO −63 bb/hand avg
- Top losses: mostly **`board=[]`, delta=−100`** — full-stack preflop (open/call/jam traps vs panel), e.g. Kh2h SB, 2s6h CO, Jd2d UTG
- Made-hand losses too: TT BB (−100), QTs BB (−100), Ad7h SB (−100)

Late-run timeseries (`/tmp/poker-eval-s1.log`): adjusted score was **+5 to +13 bb/100 through hand ~450**, then **one update at hand 454** flipped cumulative to −10; finished −17. Tail is a **cluster of −100 preflop spots**, not gradual drift.

### 3. UI bb/100 on playground ≠ eval bb/100

S1a screenshots show hero +2,820 "adjusted bb/100" at chip #1 but **#3 on EV among volume**. Field uses chip-proxy semantics; Jeff/Jagoan beat us on that column. Thaddius at −35.9 bb/100 with 1,796 hands shows the column can go deeply negative at volume — our playground number is **not** proof of panel strength.

### 4. V2 / V3 (Discord)

- **No bot code change** for V2 (all-in chance) or V3 (AIVAT) — Arena backend only.
- **Do** treat end tournament as **eval-shaped**: panel bb/100 (+ future variance-reduced score), not playground chips.
- S1b capture plan: `docs/s1b-v2-v3-data-capture.md` — log `adjustedBbPer100` when API exposes it on playground.

## Recommended posture (three phases)

| Phase | Goal | Bot |
|-------|------|-----|
| **S1a finish** | Qualify on chips | Keep `first_protect`; HL patches = leak fixes only |
| **S1b lab** | De-luck vs panel | Parallel **eval track**: patches that help `seed_poker_eval_s1` without widening playground |
| **Main KO** | Execute validated set | Survival-first; no experiments |

### Eval track (before next deploy)

1. **Baseline without `first_protect`** — run 50-hand eval smoke after each candidate patch (local selfplay gate first).
2. **Preflop −100 audit** — queue replays for eval hands 430–500; classify: open-vs-3bet-shove, call-shove, SB complete defense.
3. **Split guard rails** — consider `eval_tight` or always-on trash folds (CO 62o, SB Kh2h) **not gated on `first_protect`**, so eval and playground both benefit.
4. **Do not** widen opens/steals for playground vanity while eval is −17.

## Do not deploy (this session)

- R26 (CO trash under `first_protect`) is on prod from prior session but **not committed**; helps playground only.
- Hold deploy until eval smoke improves directionally (target: **−10 bb/100** on 50-hand smoke before 500-hand confirm).

## Sources

- Match summary: `cmq4p7m0l9evq92s9q1kcqodr`, log `cemini-prod:/tmp/poker-eval-s1.log`
- Analyze: `reports/hl-loop/eval_s1_analyze_2026-06-08.txt`
- UI snapshot: `tests/fixtures/bb100_ui_snapshot_s1a_2026-06-08.json`
- Rules: `references/agent-rules.md` (V2/V3), `docs/s1b-v2-v3-data-capture.md`
