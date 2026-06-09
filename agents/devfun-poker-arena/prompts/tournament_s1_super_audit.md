# Tournament S1 SUPER AUDIT — multi-model cursor-audit (5 auditors)

You are auditor **{{MODEL_SLOT}}** in a **5-model super audit** before **Tournament S1** (~9 AM EST).

**Mode:** `brief-plan` + poker bot architecture · **Readonly** — markdown report only.

---

## Mission (single sharp question)

Given everything we know from **S1 playground success** vs **S2 playground struggle**, what should `cemini_wiki_poker` **ship for Tournament S1** (equal stacks, **5 rebuys**, prize-pool focus, jackpots irrelevant)?

Deliver:

1. **Verdict** PASS/WARN/FAIL on current prod posture (`ca5845f` decide + survival env)
2. **What's working** vs **what isn't** (code, env, data pipeline, version tracking)
3. **Ranked patch backlog** (P0 before 9 AM, P1 post-bracket) — smallest diffs, no runtime LLM
4. **Versioning scheme** — how to label each deploy (`AGENT_VERSION` / git SHA / HL round) so we can tell if we're improving
5. **Data capture gaps** — what we must log going forward (correct metrics, not misleading proxies)
6. **Regime discipline** — separate Playground S1 / S2 / Eval panel / Tournament S1; no cross-pool claims

---

## Context — S1 playground win (official recap PDF)

| Fact | Value |
|------|-------|
| Competition | `cmpy2qy65002ud9ej6b7jjq0l` |
| Hero | cemini — **10.3% VPIP**, 2,361 hands, **never busted** |
| Comeback | 432 chips → **+138,946** (324×) |
| Opponents beaten | 276 distinct; **56.5%** showdown win |
| Style label | "the rock" — tight nits (cemini, uday, fefou ~10–11% VPIP) **and** maniacs both won |
| Field meta | 71.5% hands no showdown; 46.9% preflop death; median pot 16 vs mean 728 (jam/fold meta) |
| Chip #1 vs rate | Chip leader but **adj bb/100 #3** behind 0xJeff, jagoan among volume players |

---

## Context — S2 playground struggle

| Fact | Value |
|------|-------|
| Competition | `cmq57o53r0bhw18g23qkydb08` |
| Recent rank | ~#160, ~1.8k chips / 584 hands (reset 1000 stack) |
| Field | Harder early tier; leaders posting +500–+2300 adj bb/100 |
| Hypothesis (operator) | Optimized too long for **#1 chip lead** (`lead_protect`, stagger locks, volume pace) — wrong when behind |

---

## Context — Tournament S1 today

- Everyone starts **equal chips** — no inherited lead
- **5 rebuys** (S1 playground win perk) — not no-rebuy KO
- **Prize pool / placement** matters; jackpots irrelevant
- Tournament comp ID **not yet in list-active** — will swap `ARENA_LOBBY_COMPETITION_ID` at bracket open
- Prod env (applied): `CEMINI_EVAL_PANEL_GATE=0`, `CEMINI_PACE_PHASE=survival`, `CEMINI_KO_SURVIVAL=1`, `JACKPOT_27_HUNT_ENABLED=0`

---

## Code / version state

| Artifact | Value |
|----------|-------|
| Prod decide commit (last deploy) | `ca5845f` (HL R10) |
| Best eval-panel candidate | `70f2527` at **−17.45** bb/100 (500h live eval) |
| Current local panel gate | **−26.67** bb/100 (150h, `eval_panel_mode`) — fails floor |
| Regression spots | 80+ frozen leaks in `tests/fixtures/regression_spots.py` |
| Runtime LLM | **None** in prod decide; HL auto-analyst JSON guards sparse on prod |

**HL R8–R10 theme:** always-on EP trash / weak suited ace / low suited paired folds — tightened for eval panel & analyze windows; may hurt vs maniac field when not leading.

---

## Protect lanes (read `run_cemini_lobby.py` + `qualification_guard.py`)

- `qualification_protect`, `lead_protect`, `first_protect` — tiered when ranked high
- `ko_survival_lane` — first N hands / min stack
- `eval_panel_mode` — only in self-play gate & `agent.py` dry-run, **not** prod lobby path
- `CEMINI_S1B_EXPLOIT`, nemesis archetypes, seat matrix v2 — env toggles

**Key tension:** S1 win = patient nit + survival; S2 patches = fold-heavy; lead mode = defend buffer not accumulate.

---

## Data pack files (READ these paths in workspace)

```
{pack_index}
```

---

## Prior audit consensus (S2 heavy v2 — do not repeat blindly; validate for Tournament)

- **Do NOT** widen to field LAG (~36% VPIP)
- Blind/EP preflop −100 cluster is real — but distinguish **historical analyze window** vs **already-patched** spots
- Nemesis/HUD should be **archetype** not name-only (101 rivals ≥200h in S2 export)
- `payout_chips` in export ≠ chip delta — do not claim bb/100 from submissions alone
- Eval panel gate is **deploy widen blocker**, not playground rank predictor

---

## Required output format

### Verdict
PASS | WARN | FAIL — one line why

### Findings
| Severity | Finding | Evidence | Fix |
|----------|---------|----------|-----|

### Tournament S1 deploy recommendation
- **Git commit** to deploy (or revert target): `???`
- **Env toggles** (explicit list ON/OFF)
- **Expected VPIP/PFR band** for tournament (numeric target)
- **Rebuy strategy** (when to rebuy vs sit out)

### Version & telemetry plan
- Proposed `AGENT_VERSION` string for today's ship
- What to append to `deploys.jsonl` / `eval_timeseries.jsonl` / `playground_timeseries.jsonl` each deploy
- Metrics that are **wrong** to optimize (list)

### Root cause (S2 underperformance vs S1)
One paragraph

### Ranked patch backlog
| P | Patch | Effort | Expected lift |
|---|-------|--------|---------------|

### Unique angle
One thing other auditors might miss

### Confidence
high | medium | low

---

## Constraints

- Zero runtime LLM in bot
- Smallest diff wins before 9 AM
- Do not recommend "play looser" without field evidence and eval gate pass
- Tournament ≠ S2 playground qual — separate recommendations
