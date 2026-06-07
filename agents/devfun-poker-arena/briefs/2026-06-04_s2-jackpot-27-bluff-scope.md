---
title: S2 jackpot hunt — 2-7 offsuit bluff bot (scope)
type: brief
tags: [brief, poker, devfun, jackpot, playground, satellite-bot]
created: 2026-06-04
target: agents/devfun-poker-arena/examples/jackpot_27_decide.py (planned)
status: P1 IMPLEMENTED — register + deploy when S2 live
---

## Target

**Separate** dev.fun agent + `decide()` module for Playground **S2 jackpot** ($2,500 trigger: **2-7 offsuit bluff**).  
**Do not** modify prod `cemini_decide.py` or `cemini-devfun-poker-lobby.service`.

## Summary

S1 **Royal Flush** jackpot ($2,500) hit — effectively closed for this window. S2 (opens **~Jun 7**) rotates trigger to **27o bluff win** per arena rewards UI. Scope a **satellite bot** that:

1. Runs on its **own agent ID** (unclaimed probe pattern — @LESSONS.md L5).
2. Attempts a **bounded** number of 72o/27o bluff lines per session when fold equity is high.
3. Keeps **qualification bot** (`cemini_wiki_poker`) on survival/accumulation strategy unchanged.

Jackpot EV remains **lottery-tier**; this is optional upside, not a replacement for top-20 → tournament path.

## Jackpot rules (from UI — verify before code)

| Season | Window (UI) | Trigger | Pool |
|--------|-------------|---------|------|
| **S1** | Jun 3–6 | Royal flush | $2,500 (**claimed**) |
| **S2** | Jun 7+ (TBD) | **2-7 offsuit bluff** | $2,500 |
| Rollover | — | Unclaimed → next season | per UI |

**Interpretation (standard 7-2 game — [NEEDS VERIFICATION on dev.fun API/docs]):**

- Hero must hold **7-2 offsuit** specifically (not 72s, not 73o unless rules broaden).
- Hero must **win the pot as a bluff** — villain(s) fold; showing down with a made hand likely **does not** count.
- Likely requires **show** or platform-detected bluff win event (confirm via `recentEvents` / hand export / dev.fun support).

**P0 before any prod run:** fetch official text from `docs.dev.fun`, Playground competition metadata, or hand export where S1 royal was paid — document exact JSON fields.

## Why a separate bot (not prod patch)

| Concern | Qualification bot (`cemini_decide`) | Jackpot bot |
|---------|--------------------------------------|-------------|
| Goal | Top 20 chips, tournament seat | Rare S2 trigger hit |
| 72o default | Hard fold everywhere | **Seek** bluff spots |
| EP VPIP gate | ≤22%, 0 trash opens | Would fail gate by design |
| Rank / stack | #1 @ 900+ hands — protect | Accept bleed; probe volume |
| Claim timing | Already claimed X | Run **unclaimed** until jackpot or abandon |

Per **L5**: register handle, run parallel, claim only if it wins something that matters.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  cemini-prod (unchanged)                                     │
│  cemini-devfun-poker-lobby.service → cemini_decide.py         │
│  agent: cmpy4lcyi001y11vnekn1zlo3 (cemini_wiki_poker)       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  jackpot lane (new — local creds OR second prod unit)        │
│  jackpot-27-lobby.service → jackpot_27_decide.py              │
│  agent: NEW unclaimed handle (e.g. cemini_27_hunter)         │
│  .arena-credentials.jackpot-27 (never rsync over prod)       │
└─────────────────────────────────────────────────────────────┘
         │
         ├─ imports: position_utils, opponent_hud (read-only)
         ├─ fork baseline: fold everything EXCEPT 27o hunt branch
         └─ reasoning YAML tags: jp: "27_bluff_attempt@BTN"
```

**Deploy isolation**

- `scripts/cemini_deploy.sh` — prod only; **exclude** jackpot creds.
- New: `scripts/jackpot_27_deploy.sh` (optional) — separate path, `ARENA_NO_AUTO_REGISTER=0` only on jackpot host.
- Env: `JACKPOT_27_MODE=1`, `COMPETITION_ID=<playground-s2>` when live.

## `jackpot_27_decide.py` — behavior sketch

### Default (99.9% of hands)

Delegate to **minimal fold/check** chart — tighter than `cemini_decide` (no CO steals, no maniac exploits). Goal: **cheap table presence**, not chip accumulation.

### Hunt mode (dealt 72o / 27o only — verify exact classes)

Activate only when **all** gates pass:

| Gate | Rationale |
|------|-----------|
| Hand ∈ `{72o, 27o}` (verify suit order) | Trigger definition |
| Position ∈ `{BTN, CO, SB}` | Fold equity |
| Heads-up or **≤2 villains** in pot | Multiway bluff fails |
| HUD: `rock` or `passive` OR cold-start + late position | Fold equity |
| Effective stack ≥ 15bb | Room to fire 2–3 barrels |
| `attempts_this_session < MAX_ATTEMPTS` (default **3**) | Cap bleed |
| Not in `qualification_protect` / survival stack mode | N/A on this agent |

### Line (when hunting)

1. **Preflop:** open-raise 2.5–3bb from BTN/CO; SB complete only if HU pot.
2. **Flop/Turn:** c-bet ~33–50% on dry boards; barrel once on scare cards (A/K overcard) if villain is capped.
3. **Never:** call a raise, bluff multiway, show down for “value,” slowplay.
4. **Give up:** check-fold if raised or if `attempts` exhausted on same hand.

### Reasoning / observability

- YAML: `jp: "hunt|72o@BTN|rock"` for postmortem grep.
- Log every dealt 27o to `reports/jackpot-27/dealt.jsonl` (local + prod copy).

## Phased delivery

| Phase | Deliverable | Exit criteria |
|-------|-------------|---------------|
| **P0 — Rules** | Wiki stub on `@entities/platforms/devfun-poker-arena.md` § Jackpots; confirm 72o vs 27o, bluff-only, rollover | Official text or paid-hand replay |
| **P1 — Skeleton** | `examples/jackpot_27_decide.py` + `tests/test_jackpot_27_spots.py` (3 spots: fold 72o EP, hunt BTN vs rock, abort vs raise) | pytest green, preflight **not** EP-VPIP gate |
| **P2 — Local sim** | Self-play: measure **attempts/1000**, **success bluff rate**, chip bleed/hr | Report in `reports/jackpot-27/sim.md` |
| **P3 — Register probe** | New handle on official API; `.arena-credentials.jackpot-27`; local lobby loop | 50 hands, ≥1 hunt attempt logged |
| **P4 — Prod satellite** | Optional `jackpot-27-lobby.service` on prod OR laptop LaunchAgent | Runs parallel to main lobby; separate monitor |
| **P5 — S2 go-live** | Point at S2 competition ID Jun 7+ | Monitor for jackpot event in exports |

**Explicit non-goals (v1):** LLM runtime, royal-flush chase, merging into `cemini_decide`, claiming X on jackpot bot unless it hits.

## Test plan

| Test | Type |
|------|------|
| 72o UTG → fold (no hunt) | regression |
| 72o BTN unopened vs rock HUD → bet (hunt) | regression |
| 72o BTN vs 3bet → fold (abort) | regression |
| 72o multiway limped pot → fold | regression |
| Session cap: 4th 72o → fold | unit |
| Prod credential isolation: deploy script skips jackpot creds | shell |

No EP VPIP gate on this agent — use **custom gate**: `attempts_per_500 ≤ 5`, `bb/100 ≥ -80` (informational bleed cap).

## EV sanity (honest)

| Event | Rough order |
|-------|-------------|
| Dealt 72o | ~1 in 330 hands |
| Hunt spot + successful bluff win | Unknown; << 1% of 72o deals |
| S2 pool | $2,500 one-shot |

**Compare:** #1 Playground + tournament path ≈ **much higher** expected value than jackpot hunt. Run jackpot bot as **optional lottery ticket**, not strategy pivot.

## Risks

| Risk | Mitigation |
|------|------------|
| Chip bleed on probe agent | Session attempt cap; tight default fold |
| Accidental prod cred overwrite | Separate cred file; deploy script guard |
| Rules differ (73o, suited, showdown win) | P0 verification; feature flag `JACKPOT_HANDS=72o,27o` |
| Multi-agent ToS / prize eligibility | One claim per operator; confirm dev.fun rules |
| Distraction from qualification | Keep prod bot unchanged; schedule S2 probe after S1a lock |

## Operator decisions (pick before P1)

1. **When to start P3?** After S1a qualification secured (recommended) vs parallel now.
2. **Host:** laptop LaunchAgent vs second systemd unit on `cemini-prod`.
3. **Handle name:** e.g. `cemini_27_hunter` (unclaimed until event).
4. **Max attempts/session:** default 3 — raise only if sim shows low bleed.

## Sources

- Arena rewards UI (S1 royal / S2 27o bluff — user screenshot 2026-06-04)
- @LESSONS.md L5 — multi-agent probe pattern
- @entities/bots/cemini-devfun-poker-agent.md — prod agent (do not merge)
- @concepts/poker-hl-analyst-loop.md — HL loop stays on prod lane only
- [7-2 game side pot tradition](https://www.pokerstrategy.com/news/content/Poker-Basics-The-7-2-Game_118826/) — bluff-show semantics (informal)

## Implementation status

| Field | Value |
|-------|-------|
| Status | **P1 IMPLEMENTED** |
| Next step | P3 — `./scripts/jackpot_27_register.sh` then set `JACKPOT_27_COMPETITION_ID` for S2 |
| Owner | operator + HL analyst |
| Prod impact | **None** until separate creds + service |
