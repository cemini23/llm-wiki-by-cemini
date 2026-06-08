---
title: Playground qualification — top 20 to tournament
type: brief
tags: [brief, poker, devfun, playground, tournament, qualification]
created: 2026-06-03
target: agents/devfun-poker-arena/examples/cemini_decide.py
---

## Target

dev.fun **Playground S1** → tournament knockout (Jun 2026). One claimed agent: `cemini_wiki_poker`.

## Summary

Qualification is **top 20 agents by chip score** per **playground season** (**not** top 25%). **Season pairing (Discord 2026-06-08):** Playground **S*N*** top 20 → **free entry** to Tournament **S*N***. Qualifying on Playground S1 does **not** carry to Tournament S2 — each playground season is a fresh bankroll and a separate tournament ticket.

**S1 (closed):** qualification **secured** — **rank #1 @ ~140k chips** at S1 close → **Tournament S1** seat when that bracket opens.

**S2 (active):** fresh 1000-chip runway on `cmq57o53r0bhw18g23qkydb08` — must re-qualify top 20 for **Tournament S2**. Early snapshot 2026-06-08: rank ~51 @ 999 chips (field still forming).

## Body

### Qualification ladder (dev.fun) — paired seasons

| Playground season | Competition ID | Advance |
|-------------------|----------------|---------|
| **S1** (closed) | `cmpy2qy65002ud9ej6b7jjq0l` | Top **20** → **Tournament S1** (free entry) |
| **S2** (active) | `cmq57o53r0bhw18g23qkydb08` | Top **20** → **Tournament S2** (free entry) |
| **Tournament S*N*** KO | TBA per season | Top **25** within that bracket |
| Researcher / finale | TBA | separate tracks |

**Operator posture (Jun 8):** S1 ticket **in hand**; prod lobby on **S2 playground** until S2 top-20 secured. Swap `ARENA_LOBBY_COMPETITION_ID` only when intentionally changing season target.

**S2 phase plan:** Days 1–2 — `JACKPOT_27_PHASE=early` (more 72o hunt volume; rebuy runway). Stay near qual zone, chase royal/27 slots. Days 3+ — `JACKPOT_27_PHASE=climb` + `AGGRESSIVE=0` to push top-20 rank.

Leaderboard metric: **`totalScore`** (season chips). ~258 agents in field; rank **#20 ≈ 1607 chips** (moving target).

### Cemini status (2026-06-07 UTC)

| Field | Value |
|-------|-------|
| Claimed handle | `cemini_wiki_poker` |
| Agent ID | `cmpy4lcyi001y11vnekn1zlo3` |
| Rank | **#1** |
| Chips | **138,758** |
| Hands | 2,090 (~177 won, **~8.5%** win rate) |
| Net / hand | **~+65.9 chips** (~+330 bb/100 at 20-chip BB) |
| **bestRank** | **1** |
| #20 floor | ~34,503 chips |
| Buy-in | **1000** chips (`initialChips`) |
| HL state | **Round 22 deployed** — rerun at **≥ 2,101** hands |

**Resolved (Jun 3–7):** credential split, sub-buy-in stack, rebuy 403 — prod creds restored; HL R8–22 patches (SB/UTG/BTN bleed, survival lane, nuts detect).

**Active (S1a tail / S1b prep):** first-protect join pace; KO survival hooks for next comp reset; S1b exploit flip when protect off.

### Hand-history scan (2026-06-03 ~18:30 UTC)

100-hand prod analyze after latest deploy. **Still bleeding; SB dominates worst hands.**

| Priority | Pattern | Examples from worst 15 |
|----------|---------|------------------------|
| P0 | SB bust lines | `22`, `79`, `96`, `88`, `JJ` paired, `A8`/`K6` SB |
| P1 | Weak ace postflop | `A6` BB on 999, `A7` CO paired, `A9` BTN preflop |
| P2 | BTN overcall scary boards | `QAh` on 55776, `AT` monotone |
| OK | Value hands | `TT` +396, `77` +284, `AK` +122 |

**Status:** rank **230**, **782 chips**, gap to #20 **+1193**. Buy-in **1000** → 409 when between tables. Patches (JJ SB, 83o, KQo MP, survival mode) need post-deploy sample before next HL round.

See `LESSONS.md` L6.

1. **Survival first** — one bust from 1000 ≈ season over (no rebuy). HL patches (SB trash, JJ paired river, KQ OOP) reduce bleed.
2. **Volume when +EV** — leaders run **50–100+ hands**; chip edge compounds (e.g. #1: 6810 / 102 hands).
3. **HL loop cadence** — `./examples/cemini_hl_loop.sh --from-prod` → patch → preflight → deploy **without** `CEMINI_FORCE_CREDS=1`.
4. **Monitor cutoff** — `./scripts/cemini_playground_status.sh` (rank vs #20 floor).
5. **Stage 2 (Jun 7–11)** — treat as fresh 1000-chip runway if S1a ends busted; same bot, zero duplicate agents.

### Do not

- Auto-register new handles on prod (`ARENA_NO_AUTO_REGISTER=1` in prod `.env` recommended).
- Deploy with `CEMINI_FORCE_CREDS=1` unless intentionally rotating keys.
- Optimize self-play bb/100 — optimize **live chip survival + accumulation**.

## Sources

- https://dev.fun/ (playground top 20 / KO top 25)
- `agents/devfun-poker-arena/README-CEMINI.md` — season pairing + qual guards
- Discord dev.fun team (2026-06-08) — Playground S*N* → Tournament S*N*

## Implementation status

| Field | Value |
|-------|-------|
| Status | **S1a QUALIFIED** — #1 in zone; S1b Jun 7–11; protect stack + HL R23 at 2,101 hands |
| Proof | `scripts/cemini_playground_status.sh` 2026-06-07 |
| Follow-up | S1b (Jun 7–11): multi-agent probe (L5); S2 jackpot bot P3 when S2 live |

## Next playground — multi-agent funnel (L5)

Observed meta: many entrants run **multiple unclaimed agents**, tune in secret, **claim only when rank/chips look good**.

| Phase | Action |
|-------|--------|
| Pre-window | Register 5–10 official agents; store `credentials/agent-{1..N}.json` |
| Days 1–2 | Parallel lobby/self-play; branch `cemini_decide` or train profiles per agent |
| Gate | `cemini_playground_status.sh` per agent; pick top 1–2 by rank + chip runway |
| Claim | X-verify **winners only**; point prod lobby at winner creds |
| Retire | Abandon or archive losers; never deploy stale beta keys |

We did the opposite: one claimed agent, early public lock-in, single-strategy bleed. Correct for brand visibility; wrong for qualification EV.
