---
title: Tournament stack repair — freeze climb, stop HU bleed, return to P13 grind
type: brief
tags: [brief, poker, tournament, repair, playground-s13]
created: 2026-08-10
---

## Target

`agents/devfun-poker-arena/` — repair KO posture; grind Playground S13 for next free tournament ticket

## Summary

Dual audit ([GPT-SOL](37d29e7e-f99f-471a-8de9-c0a95ec30b88) / [Cursor Grok](e9a677c2-bfb5-4617-9379-de354492a752)): tournament stack is **structurally bust-biased**. All of S1/S2/S3/S10/S12 ended at **0 chips**. Freeze climb aggression, force `6max` (no mid-hand HU chart bleed), clear leftover `TAG_WIDEN` in tournament posture. Hold the next tournament seat until this repair ships and soaks. Meanwhile re-enter **Playground S13** (#30 @ ~3918, #20 cut ~5257) for free T13 ticket.

## Regime disclosure

**Single-regime** Arena chip-score only. Repair targets KO absorbing-zero policy under `MAX_REBUYS=0`, not cash EV. Per-regime: playground TAG widen stays for chip-qual; tournament posture must not inherit it.

## Root causes (audit consensus)

1. `CEMINI_TAG_WIDEN=1` leftover in prod during tournament (posture never cleared it)
2. `CEMINI_TABLE_FORMAT=auto` → mid-hand HU → BB 86s/87s 3bet/4bet/fold
3. Permanent `placement_chase` under prize top-3 + climb pack (polar/flat/3bet)
4. Postflop check/fold conversion (out of scope for this repair slice — telemetry stays)
5. Mid-run version thrash with rebuy=0

## Repair (implement now)

### R1 — Tournament posture freeze (`run_cemini_lobby._apply_competition_posture` s12 block)

| Key | Value |
|---|---|
| `CEMINI_TABLE_FORMAT` | `6max` |
| `CEMINI_TAG_WIDEN` | `0` |
| `CEMINI_TAG_BLIND_DEFEND` | `0` |
| `CEMINI_TOURNAMENT_3BET` | `0` |
| `CEMINI_TOURNAMENT_3BET_POLAR` | `0` |
| `CEMINI_FLAT_DOMINATE` | `0` |
| `CEMINI_PLACEMENT_CHASE` | `0` |
| `CEMINI_NEMESIS_TIGHT` | `1` |
| `CEMINI_SHORT_STACK_BB` | `20` |
| `CEMINI_KO_SURVIVAL_HANDS` | `60` |
| `CEMINI_GIN_KILL` | `1` (unchanged) |
| `CEMINI_MAX_REBUYS` | `0` (unchanged) |

Placement protect cushion pct may remain for when naturally in money; do not force chase.

### R2 — HU BB chart raise hard gate (`cemini_decide._hu_bb_chart_raise_vs_open`)

Even if format flips to HU: **no chart 3bet/4bet from BB** when `CEMINI_TOURNAMENT_MODE=1`, or when `call_chips > 3 * big_blind` (already facing a re-raise). Premium-only exception optional; default = refuse raise path in tournament.

### R3 — Tests

Update `tests/test_t12_posture.py` for freeze knobs. Add test that HU BB raise helper returns None in tournament mode.

### R4 — Return to Playground S13 grind

Apply chip-qual env for S13 (`cmsg35zvs001hbagh1wdjc1me`), `PRIMARY_TRACK=playground`, restart lobby. Goal: top-20 → free Tournament S13 entry. Do **not** enter another paid tournament until repair validated offline.

## Do not

- Re-enable gin
- Pay MON for another tournament seat this cycle
- Mid-event agent_version thrash once P13 grind is stable
- Claim repair fixes postflop conversion (still open)

## Success criteria

- [x] s12 tournament posture forces TAG_WIDEN=0 and TABLE_FORMAT=6max
- [x] HU BB chart raise disabled under tournament mode
- [x] Tests green (`test_t12_posture` + `test_hu_bb_chart_raise_tournament_freeze` — 5 passed)
- [x] Lobby on Playground S13, at table (rank≈30, buffer≈−1339 vs #20)
- [ ] No tournament entry until operator GO after freeze soak

## Sources

- Dual audit 2026-08-10 (GPT-SOL + Cursor Grok)
- `briefs/2026-08-09_p13-postmortem-t12-number-one-plan.md`
- Prod export `reports/exports/s12-tournament-live/`
