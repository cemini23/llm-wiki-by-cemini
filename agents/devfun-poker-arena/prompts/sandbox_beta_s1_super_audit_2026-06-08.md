# dev.fun HU sandbox beta S1 — 5-model super audit (maximize bot before 10k hands)

You are auditor **{{MODEL_SLOT}}** in a **5-model super audit**.

**Mode:** `prod-ship` · **Readonly** — markdown report only; no edits.

---

## Mission (single sharp question)

Given live sandbox PvP is running and submission works (`POST /submissions` bundle), what **P0/P1 code + env + bundle** changes will maximize **TrueSkill + adj BB/100** for the remaining ~9,600 hands — and is the bot **SHIP-ready** to continue without resubmit, or **SHIP-WITH-FIXES** requiring bundle rebuild + `--replace`?

Deliver:

1. **Verdict** PASS/WARN/FAIL on current bot quality vs field
2. **What's working** vs **what isn't** (cite file:line)
3. **Ranked patch backlog** — smallest diffs first; quantify expected lift on maniac/LAG match_win and trajectory axes
4. **Sandbox submit recommendation** — continue current submission | rebuild bundle | replace smoke bot
5. **Arena vs local gap** — why live metrics may diverge from `run_hu_sandbox_gate.sh`

---

## Context

| Layer | State (2026-06-08) |
|-------|-------------------|
| **Comp** | `[poker] heads-up sandbox — beta S1` `cmqqqs05i1u7ppnu7stqbw7d8` — skill `sandbox-pvp.md` |
| **Agent** | `cemini_wiki_poker` — Cemini bundle Active ~386/10k hands, TS **6.08**, adj BB/100 **+59.7** |
| **Smoke** | `always_fold` submission still Active (~353/10k) — dead weight; next submit should `--replace` |
| **Local gate** | 200h HU PASS; **maniac series_win ~20%** (advisory ≥38%); lag 100%; rock 60% |
| **Bundle** | `harness/strategy.py` sets researcher HU env; vendored `assets/_vendor` + `cemini_decide.py` |
| **Prod lobby** | Playground S3 intel only; researcher comp id in env; not driving sandbox via texas/join |
| **Recent fix** | `safest_legal_action` + trajectory test pollution (`9431818`) |

**Code surface:** `examples/cemini_decide.py`, `gin_style.py`, `research_static_chart.py`, `s1b_exploit.py`, `session_memory.py`, `harness/strategy.py`, `examples/submit_sandbox_pvp.py`, `examples/arena_client.py`, selfplay/gate scripts.

**Known weakness:** passivity vs maniac/LAG in homogeneous selfplay — structural not smoke-test artifact.

---

## Regime boundaries

- **Sandbox static PvP** (`choose_action` bundle) ≠ **lobby texas/join** — audit bundle path and env `setdefault` in harness.
- **Playground S3 6-max** ≠ Researcher HU sandbox — do not recommend 6-max chart patches for this comp.
- **Selfplay `bot_maniac`** is caricature — still flag if policy is structurally too passive vs HUD maniac/LAG archetypes.
- **Dual Active submissions** — policy/operator issue; recommend `--replace` not second parallel bot.
- **bb/100 alone** misleading at low sample — prioritize match W/L proxies, maniac exploit, trajectory M₈/M₉.

---

## Data pack files (READ these paths)

```
{pack_index}
```

---

## Prior audit consensus (validate — do not repeat blindly)

- K122 HU fork + trajectory gates aligned; W-PFR shipped.
- Maniac match_win ~29–30% in prior audits — still open.
- Local diagnosis: rank 9 mostly sample size; early adj BB/100 positive on real bundle.
- Trajectory bound fix shipped; bundle QTs call vs nit OK.

---

## Required output format

### Verdict
PASS | WARN | FAIL — one line why

### Findings
| Severity | Finding | Evidence | Fix |
|----------|---------|----------|-----|

### Sandbox deploy recommendation
- **CONTINUE | REBUILD-BUNDLE | REPLACE-SUBMIT | REWORK**
- Env toggles in harness vs missing from bundle
- Metrics to optimize (match_win vs maniac, 3-bet freq, BTN open %)
- Bundle packaging gaps (deps, paths, deadline_s)

### Root cause
One paragraph on dominant limiter to TrueSkill ceiling — or insufficient evidence + next inspect step.

### Ranked patch backlog
| P | Patch | Effort | Expected lift |
|---|-------|--------|---------------|

### Unique angle
One thing other auditors might miss

### Confidence
high | medium | low

---

## Constraints

- Readonly — no edits, no prod SSH
- Cite file paths + line-level behavior
- Distinguish bug vs doctrine vs intentional hold
- Propose **smallest** diffs that move maniac match_win and live PvP

---

## Already ruled out

- Runtime LLM `decide()` for prod Researcher track
- CFR weight training before season end
- Full Jungleman/Dwan style emulation (operator hold until rules)
- Lobby `/texas/join` as sandbox submit path (wrong API)
- `b-arena.dev.fun` base URL (401; fixed to `arena.dev.fun`)
