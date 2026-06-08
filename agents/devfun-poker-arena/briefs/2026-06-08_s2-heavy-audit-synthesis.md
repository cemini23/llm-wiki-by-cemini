---
title: S2 heavy gap audit — 3-model synthesis (287k row scan)
type: brief
created: 2026-06-08
updated: 2026-06-08
pack: reports/gap-audit/pack-s2-heavy
models: [claude-opus-4-8-thinking-high, gpt-5.3-codex, kimi-k2.5]
status: ACTIVE — S2 qual secured, jackpot lanes on main bot
---

## Target

CeminiSuite / operator — **S2 playground qual in progress** (`cmq57o53r0bhw18g23qkydb08` → Tournament S2 ticket). S1 qual already secures Tournament S1. Single agent `cemini_wiki_poker`, no separate 27o probe.

## Summary

**Verdict: WARN (3/3).** Full export scan (**287,857** submission rows, **2,363** hero rows) confirms chip #1 is qualification-durable on **chip accumulation** but **EV-fragile** (UI adj bb/100 **#3** behind Jeff **3670** / jagoan **2828**). Hero payout shape: **91.75%** zero-payout rows, **8.25%** pot-win rate, **37** wins ≥500 chips — barbell nit + tail, not LAG volume.

**Jackpot (API 2026-06-08):** Both lanes live on S2 via **main bot** — no satellite agent.
- **Royal flush:** 5× slots @ 13,600 MON each (`Available`). Fires at **showdown** with hand unfolded → bot uses check/call/small-bet line (`JACKPOT_ROYAL_SHOWDOWN=1`).
- **7-2 offsuit bluff:** 10× slots @ 4,500 MON each (`Available`). Uncontested pot (everyone folds) → `JACKPOT_27_HUNT_ENABLED=1` on qual bot.

**Shipped from synthesis:** `CEMINI_NEMESIS_EXPLOIT=1` — s1b value-3bet/trap/BB-defend vs nemesis openers even under `first_protect`; nemesis list adds `0xJeff_ai`.

## Body

### What the heavy pack actually scanned

| Layer | Prior skim audit | Heavy pack |
|-------|------------------|------------|
| Submission rows | 50 worst hero | **287,857** aggregated |
| Rivals | Field VPIP only | **10** rival profiles (25 rows each) |
| Hero hands | 50 | **80** worst + payout histogram |
| Manifest | 1,200 agent IDs bloating prompt | Trimmed summary |
| Prompt size | ~145KB | **~69KB** |

Built by: `scripts/build_heavy_audit_pack.py`

### Three-model consensus

| Theme | Opus | Codex | Kimi | Decision |
|-------|------|-------|------|----------|
| Verdict | WARN | WARN | WARN | **WARN** |
| Don't widen to 40% VPIP | ✓ | ✓ | ✓ | **LOCK** |
| Chip #1 ≠ EV #1 | ✓ | ✓ | ✓ | **CONFIRMED** |
| Blind bleed (SB/BB) | implied | pos2/4 weak | **critical** | Monitor HL; guards shipped R21-R27 |
| Nemesis exploit gap | s1b gated off under protect | predator deny | **unique angle** | **SHIP nemesis exploit bypass** |
| Bounded TAG / micro-steal | value-press IP | LP TAG overlay | selective 3-bet | **Defer** — experiment toggles only |
| Instrument chipDelta | P1 | implied | gap table | **SHIPPED** `playground_timeseries.py` |
| 27o jackpot | PASS | no satellite | deferred | **ON main bot** (operator override) |

### Rejected (all models)

- Global VPIP widen toward field LAG (~38%)
- Separate 27o probe agent / `jackpot-27-lobby.service`
- Copy Grok 65–77% VPIP lanes
- Remove `first_protect` / stagger locks for EV vanity

### Ranked patch backlog (merged, top 8)

| P | Patch | Status |
|---|-------|--------|
| 1 | Nemesis-gated `s1b_exploit` (`CEMINI_NEMESIS_EXPLOIT`) | **SHIPPED** |
| 2 | Nemesis handles + Jeff (`0xJeff_ai`) | **SHIPPED** |
| 3 | chipDelta timeseries for S2 (true bb/100) | **SHIPPED** |
| 4 | Royal showdown jackpot line (`jackpot_rules.py`) | **SHIPPED** |
| 5 | 27o hunt on qual bot (`maybe_hunt_action`) | **SHIPPED** |
| 6 | `CEMINI_VALUE_PRESS` IP thin value (bet_bar tweak) | BACKLOG — gated experiment |
| 7 | `S2_TAG_LP_OVERLAY` bounded steals CO/BTN | BACKLOG — A/B only |
| 8 | Broaden s1b HUD trigger LAG not just maniac | BACKLOG |

### S2 experiment plan

| Hypothesis | Toggle | Metric | Stop |
|------------|--------|--------|------|
| Nemesis exploit cuts hunter/Jeff pots | `CEMINI_NEMESIS_EXPLOIT=1` | pots lost vs hunter/Jeff per shared table | Revert if rank >20 |
| Value press lifts bb/100 without bust | `CEMINI_VALUE_PRESS=1` | chipDelta over 300h | Revert if qual buffer lost |
| Micro-steal LP overlay | `S2_TAG_LP_OVERLAY=1` | adj bb/100 + bust rate | Revert if VPIP >18% |
| Royal / 27 jackpot EV | `JACKPOT_*` | inbox payout + slot status | Cap hunt attempts (5/session) |

## Sources

- `reports/gap-audit/pack-s2-heavy/`
- Cursor audit subagents 2026-06-08 (Opus, Codex, Kimi)
- `GET /texas/jackpots?competitionId=cmq57o53r0bhw18g23qkydb08` (2026-06-08)
- dev.fun homepage — $5K playground royal + 2-7 bluff copy
