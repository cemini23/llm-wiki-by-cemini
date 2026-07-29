---
title: Tournament S10 go-live — prep pack (no lobby swap yet)
type: brief
tags: [brief, poker, tournament, s10, ko, readiness]
created: 2026-07-28
target: agents/devfun-poker-arena
---

## Target

Playground S10 → **free Tournament S10** when season pairs. Stay on Playground until T10 is Active.

## Summary

Readiness pack is staged: apply script (CONFIRM-gated), wait-and-apply poller, lobby `s10_tournament` posture wiring, nemesis intel from live Tournament S9 + Playground S10 leaders. **Do not** run apply until T10 opens.

## Status at prep (2026-07-28)

| Track | Snapshot |
|-------|----------|
| Playground S10 | **#14 @ ~9898** — IN ZONE (top 20) |
| Tournament S10 | **not listed** yet |
| Tournament S9 | Live (we are **not** entered — no free seat) |

## Go-live checklist

### Now (done / keep)

- [x] Stay on `s10_playground` / `cms0bwufmf3n8kyykdpxi6d2i`
- [x] `scripts/s10_tournament_prod_apply.sh` (requires `CONFIRM=1` + comp id)
- [x] `scripts/wait_tournament_s10_and_apply.sh`
- [x] `scripts/tournament_s10_readiness_check.sh`
- [x] Lobby posture branch for `s10_tournament` in `run_cemini_lobby.py`
- [x] Optional intel (below) baked into nemesis handles/prefixes
- [ ] Optional: eval smoke + `pick_deploy_for_tournament.py --lock` when you want a frozen commit (candidate stub notes playground climb2)

### When Tournament S10 appears Active

1. Confirm free entry / our agent on T10 participant list.
2. Either:
   - `CONFIRM=1 ./scripts/s10_tournament_prod_apply.sh <t10-comp-id>`
   - or `./scripts/wait_tournament_s10_and_apply.sh` (auto when Active)
3. Verify journal: `role=s10_tournament label=Tournament S10`
4. Status: `./scripts/cemini_playground_status.sh --competition <t10-id>`
5. Hour-one: KO survival ON (60h / 600 stack) — do not chase early.

### Do not

- Swap lobby before T10 Active
- Buy Tournament S9 with ~1.4 MON
- Leave Playground gin OFF into KO — apply script now keeps gin OFF (revisit only after KO analyze)

## Optional intel (2026-07-28)

### Tournament S9 top 25 (KO field — not us)

`batu_karang`, `alnitak`, `okonkwo`, `halloran`, `page`, `StartupBros`, `blacksite`, `kuma_zero`, `ronin`, `clurit`, `godam`, `reaper`, `royal_79f44c`, `vigilate`, `suzybaaaee`, `slowroll_sue`, `chad_bets`, `paron`, `whalealert`, `cipher`, …

**Overlap with Playground S10 top 20:** `StartupBros`, `blacksite`, `kuma_zero`, `batu_karang` (+ `batu_*` cluster). Expect these handles again in T10.

### Playground S10 top 20 (our board)

`reichelligahh`, `sky_top`, `flintlock`, `alex_nft`, `nightshift`, `cosmometrics`, `mako_shark`, `creed_thorn`, `flattened_v2`, `si_nekat`, … **#14 `cemini_wiki_poker`**.

### Nemesis bake (in apply script)

```
CEMINI_NEMESIS_HANDLES=batu_karang,StartupBros,blacksite,kuma_zero,page,okonkwo,halloran,reichelligahh,sky_top,flintlock,ronin,clurit
CEMINI_NEMESIS_PREFIXES=batu_,kuma_,royal_,phoenix-,holonomic-,v12_,grok,si_,mako_
```

## KO posture deltas vs Playground

| Knob | Playground S10 | Tournament S10 apply |
|------|----------------|----------------------|
| Objective | totalChips / top 20 | placement / survive |
| `CEMINI_TOURNAMENT_MODE` | 0 | 1 |
| Gin | OFF | **OFF** (keep qual style; widen only if KO analyze says too nitty) |
| KO survival | 200h / 2000 | **60h / 600** |
| Qual buffer | 1000/3000 | 999999 (disabled) |
| Prize/qual ranks | 20/20 | **10 / 25** |
| Pace | volume 12/25/15 | join 25 / queue 60 |

## Commands

```bash
# anytime — confirm still Playground
./scripts/tournament_s10_readiness_check.sh

# when you want auto-swap at open (leaves poll running)
./scripts/wait_tournament_s10_and_apply.sh

# manual at open
./scripts/list_arena_competitions.sh   # copy Tournament S10 id
CONFIRM=1 ./scripts/s10_tournament_prod_apply.sh <comp-id>
```

## Artifacts

| Path | Role |
|------|------|
| `scripts/s10_tournament_prod_apply.sh` | CONFIRM-gated enter |
| `scripts/wait_tournament_s10_and_apply.sh` | Poll → apply |
| `scripts/tournament_s10_readiness_check.sh` | Preflight (no swap) |
| `reports/hl-loop/tournament_s10_candidate.json` | Lock stub |
| `examples/run_cemini_lobby.py` | `s10_tournament` posture |

## Sources

- Internal Arena ops / prior escalate briefs in this directory.
