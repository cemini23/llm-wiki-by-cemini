# dev.fun Researcher Track HU — 7-model super audit (style / rules cross-ref)

You are auditor **{{MODEL_SLOT}}** in a **7-model super audit** (5 Cursor + 2 API).

**Mode:** `prod-ship` · **Readonly** — markdown report only; no edits.

---

## Mission (single sharp question)

Will the **currently deployed** Cemini HU Researcher-primary bot (`researcher-hu.*` on cemini-prod) perform poorly on **Researcher track evals** (TrueSkill match wins, style rep, trajectory M₁–M₉) given gambling-wiki + dev.fun rules research — and what **P0 fixes** are required before Jun 21 beta / first sandbox submit?

Deliver:

1. **Verdict** PASS/WARN/FAIL on deploy posture vs Researcher doctrine
2. **Cross-ref table**: research claim → code/env evidence → gap severity
3. **Ranked patch backlog** (P0 before Jun 21, P1 after) — smallest diffs first
4. **Play-style flaws** — HU-specific (not 6-max bleed), Jungleman-band vs actual policy
5. **Eval failure modes** — TrueSkill proxy, maniac match_win, trajectory gates, style rep lane

---

## Context

| Layer | State (2026-06-19) |
|-------|-------------------|
| **Prod** | `CEMINI_PRIMARY_TRACK=researcher`, `CEMINI_TABLE_FORMAT=hu`, `CEMINI_LOBBY_ROLE=researcher_primary`, Playground S3 slow intel only, HL auto off, `CEMINI_S1B_EXPLOIT=1` |
| **Comp** | No Researcher HU `competitionId` on arena yet — Playground S3, Tournament S2, Eval only |
| **Doctrine** | TrueSkill **match W/L** > bb/100; HU fork not 6-max tweak; F6 memory not runtime LLM; fix PFR before style emulation |
| **Selfplay gate** | 500h HU gate PASS; PFR ~20.5%, VPIP−PFR ~6.1%; rock match_win ~61%; **maniac match_win ~29.4%** (advisory, target ≥38%) |
| **Hold** | `CEMINI_RESEARCHER_STYLE_TARGET`, Kaggle path, Jungleman/Dwan code until Jun 21 rules |

**Research sources (in pack):** K122 plan, heads-up arena strategy, OSINT readiness hub, pro-style targets, starter-kit diff.

**Code surface (read paths in index):** `cemini_decide.py`, `gin_style.py`, `research_static_chart.py`, `s1b_exploit.py`, `session_memory.py`, selfplay audit/gate scripts.

---

## Regime boundaries

- **Playground S3 6-max** analyze / HL patches ≠ Researcher HU sandbox — do not recommend Playground-cadence HL or 6-max chart logic for HU eval.
- **Selfplay `bot_maniac`** is a random LAG caricature — not TrueSkill pool; flag proxy limits but still critique structural passivity vs LAG.
- **Style rep (Dwan/Jungleman)** — profiles exist in wiki; **code emulation on hold** until rules — WARN if missing code is expected pre-Jun 21; FAIL only if deploy contradicts stated hold.
- **bb/100 vs maniac** gate at −40 is weak for TrueSkill — prioritize match_win and axis narrative.

---

## Data pack files (READ these paths)

```
{pack_index}
```

---

## Prior audit consensus (validate — do not repeat blindly)

- K122 validation TRUE: pure-code HU fork, offline HL, trajectory gates aligned with research.
- W-PFR shipped: chart-first HU opens; passive limp gap fixed in audit.
- W-MATCH shipped: `match_win_rate` reported but not HL training target.
- Maniac match_win still ~29% — structural vs LAG remains open.

---

## Required output format

### Verdict
PASS | WARN | FAIL — one line why

### Findings
| Severity | Finding | Evidence | Fix |
|----------|---------|----------|-----|

### Researcher deploy recommendation
- **SHIP | SHIP-WITH-FIXES | HOLD | REWORK** for first Researcher sandbox submit
- Env toggles to flip when `competitionId` lands
- Metrics to **stop** optimizing (bb/100, Playground chips)
- Metrics to **start** gating (match W/L, style rep if rubric requires)

### Root cause
One paragraph on the dominant failure mode for eval performance — or "insufficient evidence" + what to inspect next. Do not transcribe internal reasoning.

### Ranked patch backlog
| P | Patch | Effort | Expected lift |
|---|-------|--------|---------------|

### Unique angle
One thing other auditors might miss

### Confidence
high | medium | low

---

## Constraints

- Readonly — no code edits, no prod SSH changes
- Cite file paths + line-level behavior where possible
- Distinguish **bug** vs **doctrine mismatch** vs **intentional hold**

---

## Already ruled out

- Runtime LLM `decide()` for prod Researcher (starter-kit L2 dead-end for this track)
- CFR weight training before Jun 25 deadline
- Full Jungleman/Dwan style code before rules email (operator hold)
