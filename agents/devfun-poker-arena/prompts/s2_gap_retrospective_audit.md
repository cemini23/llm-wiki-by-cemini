# S2 gap retrospective — premium audit prompt (3-model cursor-audit)

You are auditor **{{MODEL_SLOT}}** in a multi-model **gap retrospective audit** for the dev.fun Playground **S2** season (`cmq57o53r0bhw18g23qkydb08`).

**Mode:** `brief-plan` + poker bot strategy · **Readonly** — output markdown only; no runtime LLM in production bot.

---

## Mission

Answer: **Can we re-qualify top 20 for Tournament S2 on true skill, not chip-variance?** What **structural** changes to `cemini_decide.py` (+ HUD/nemesis/env) will:

1. **De-luck** — survive V2 (all-in EV) and V3 (AIVAT) when scoring switches  
2. **Preserve qualification** — rebuy allowed on playground but KO has no rebuy; nit preservation beats vanity width  
3. **Improve true poker strength** — fix leaks, not mimic LAG leaderboard styles  
4. **Exploit / neutralize** rivals with **≥200 hands** of export data (full showdown samples in pack)  

**Zero LLM at runtime.** Deliver env toggles, guard rules, regression spot IDs, ranked patch backlog only.

---

## Data constraints (non-negotiable)

| Available | Missing |
|-----------|---------|
| Full field `submissions-all` (hole, board, pot won ≥0) — **138k+ rows** | Street-by-street actions |
| `/texas/agent-stats` VPIP/PFR/style for crawled agents | Per-hand chip delta in export rows |
| Hero HL analyze worst hands | Bulk replay for all rivals |
| **Rival profiles** for agents with **≥200 hands** (showdown samples + stats) | `adjustedBbPer100` on playground API (often null) |
| Chip rank + participant totals | True bb/100 from submissions alone |

`payout_chips` = pot won, **not** chip delta. Do not claim true bb/100 from submissions alone.

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

## Field report (top 30)

```
{field_report}
```

## Rivals with ≥200 hands (leaderboard)

{rivals_200plus}

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

## Adjusted BB/100 (UI snapshot if present)

```json
{bb100_snapshot}
```

---

## Already shipped (do not re-recommend unless upgrade)

- `first_protect` — chart EP, open_steal_equity=0.99, SB premium-only vs opens  
- Anti-profiling mix/sanitize, stagger locks, cold-start no-steal  
- Nemesis exploit: hunterguy102, thaddius, v_16, 0xJeff_ai (`CEMINI_NEMESIS_EXPLOIT=1`)  
- HL R1–R5 patches (preflop trash, paired rivers, stack-off guards)  
- Jackpot lanes on main bot (royal showdown + 27o hunt)  
- Deploy grace for auto-analyst kill switch  

---

## Required output format

Return **ONLY** this structure:

### Verdict
PASS | WARN | FAIL — one line: is current qual trajectory sustainable under V2/V3?

### Findings
| Severity | Finding | Evidence (quote data) | Fix (structural) |
|----------|---------|----------------------|------------------|
| critical/warn/info | ... | ... | ... |

### Rival steal/adopt matrix (≥200h agents only)
| Rival | Style/VPIP | Pattern to steal | Pattern to deny | Nemesis? |
|-------|------------|------------------|-----------------|----------|

### De-luck assessment
- Chip rank vs pot-win rate vs field VPIP — luck or structure?  
- Bootstrap CI interpretation — what would falsify "we're just running hot"?  
- Top-20 field styles that will **pass us** when EV scoring lands  

### V2/V3 readiness gaps
| Gap | S2 data to collect | Bot change | Regression spot |
|-----|--------------------|------------|-------------------|

### Ranked patch backlog (max 12 rows)
| P | Type (fix/steal/adopt/guard) | Target | Mechanism | Spot idea | Deploy gate |
|---|------------------------------|--------|-----------|-------------|-------------|

### Do NOT do (variance traps)
3–5 recommendations that look +EV on chip leaderboard but bust a nit in KO.

### S2 experiment plan
One table: hypothesis | env toggle | metric | stop rule (when to revert)

### Unique angle
One thing other auditors might miss.

### Confidence
high | medium | low — what evidence would change your mind

---

Be specific to Python heuristic bot (`cemini_decide.py`, `opponent_hud_exploit.py`, `nemesis_seed.py`, `qualification_guard.py`).
