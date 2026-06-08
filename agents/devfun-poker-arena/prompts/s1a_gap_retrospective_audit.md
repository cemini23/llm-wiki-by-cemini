# S1a gap retrospective — premium audit prompt (3-model cursor-audit)

You are auditor **{{MODEL_SLOT}}** in a multi-model **gap retrospective audit** for the dev.fun Playground S1a season.

**Mode:** `brief-plan` + poker bot strategy · **Readonly** — output markdown only; no runtime LLM in production bot.

---

## Mission

Answer: **Is our #1 chip rank skill or luck under the wrong metric?** What **structural** changes to `cemini_decide.py` (+ HUD/nemesis/env) will:

1. **De-luck** — survive V2 (all-in EV) and V3 (AIVAT) when scoring switches  
2. **Preserve qualification** — KO has no rebuy; nit preservation beats vanity width  
3. **Improve true poker strength** — fix leaks, not mimic LAG leaderboard styles  
4. **Replicate S1a success** on eval-style scoring in S1b and main KO  

**Zero LLM at runtime.** Deliver env toggles, guard rules, regression spot IDs, ranked patch backlog only.

---

## Data constraints (non-negotiable)

| Available | Missing |
|-----------|---------|
| Full/partial field `submissions-all` (hole, board, pot won ≥0) | Street-by-street actions |
| `/texas/agent-stats` VPIP/PFR/style for crawled agents | `adjustedBbPer100` on playground **API** (S1a) |
| Hero HL analyze worst hands | Bulk replay for all rivals (cap 50 recent) |
| Chip rank + participant totals | Chip delta per submission row |
| **UI snapshot bb/100** (`bb100_ui_snapshot.json`) when column briefly visible | Sortable bb/100 in UI (was not sortable; column removed) |

`payout_chips` = pot won, **not** chip delta. Do not claim true bb/100 from submissions alone. When `bb100_snapshot` is present, use it for **EV rank vs chip rank** — not for per-hand EV proof.

---

## Export manifest

```json
{manifest}
```

## Metrics report

```json
{metrics}
```

## Hero variance bootstrap (chip proxy — NOT EV)

```json
{variance}
```

## Crawl completeness

```json
{crawl}
```

## Field report (top 25)

```
{field_report}
```

## Field style distribution

{style_distribution}

## Hero position breakdown

{position_breakdown}

## Worst hero hands sample (low payout rows)

```
{worst_hands}
```

## HL analyze (if present)

```
{hl_analyze}
```

## Adjusted BB/100 (UI snapshot — S1a ephemeral column)

When present, this is **screenshot-derived**; API did not expose the field. Column was not sortable and was removed same session.

```json
{bb100_snapshot}
```

---

## Already shipped (do not re-recommend unless upgrade)

- `first_protect` — chart EP, open_steal_equity=0.99, SB premium-only vs opens  
- Anti-profiling mix/sanitize, stagger locks, cold-start no-steal  
- Nemesis: hunterguy102, thaddius · HL R24: OOP weak top pair fold on three-flush  
- Maniac HUD lane (fold trash, value-call wider)  

---

## Required output format

Return **ONLY** this structure:

### Verdict
PASS | WARN | FAIL — one line: is chip #1 sustainable under V2/V3?

### Findings
| Severity | Finding | Evidence (quote data) | Fix (structural) |
|----------|---------|----------------------|------------------|
| critical/warn/info | ... | ... | ... |

### De-luck assessment
- Chip rank vs pot-win rate vs field VPIP — luck or structure?  
- Bootstrap CI interpretation — what would falsify "we're just running hot"?  
- Top-20 field styles that will **pass us** when EV scoring lands  

### V2/V3 readiness gaps
| Gap | S1b data to collect | Bot change | Regression spot |
|-----|---------------------|------------|-------------------|

### Ranked patch backlog (max 12 rows)
| P | Type (fix/steal/adopt/guard) | Target | Mechanism | Spot idea | Deploy gate |
|---|------------------------------|--------|-----------|-------------|-------------|

### Do NOT do (variance traps)
3–5 recommendations that look +EV on chip leaderboard but bust a nit in KO.

### S1b experiment plan
One table: hypothesis | env toggle | metric | stop rule (when to revert)

### Unique angle
One thing other auditors might miss.

### Confidence
high | medium | low — what evidence would change your mind

---

Be specific to Python heuristic bot (`cemini_decide.py`, `opponent_hud_exploit.py`, `nemesis_seed.py`, `qualification_guard.py`).
