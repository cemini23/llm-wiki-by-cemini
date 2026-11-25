---
title: "CeminiParlays Sunday slate packet — NFL Week 11, 2026-11-22"
type: source
related:
  - concepts/operator-nfl-slate-packet-workflow.md
  - sources/operator-dfs-slate-2026-11-22.md
  - sources/operator-parlays-slate-2026-11-15.md
  - concepts/parlay-market-making.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | CeminiParlays Sunday slate packet 2026-11-22 |
| Author | Operator working file (CeminiParlays desk) |
| Type | Operator document, .docx, packet bundle |
| Location | `research to be indexed/osint/11.21parlays.docx` |
| Retrieved | 2026-11-25 |
| Slate date | 2026-11-22 |
| Read status | skimmed (packet, scheme, T-90 checklist) |

## Narrative

### What it is

The CeminiParlays weekly packet for Sunday 22 November 2026, NFL Week 11. The document bundles eleven files: `packet.md`, `scheme.md`, `scratches.md`, and environment, odds, inactives, leg-alerts, Q4 RB checkdown, QB starters and quarter-script files. [Source: 11.21parlays.docx]

No book was opened and no slip was placed. Every hard-exclude rule fires before a leg is allowed onto a slip.

### Slate and sources

Ten games: seven at 1:00 PM ET, one at 4:05 PM ET, two at 4:25 PM ET. Kicks come from the ESPN scoreboard API as primary and NFL.com Week 11 as second source. All 13 week-11 kick instants agreed. The NFL.com rendered text lacks per-row times for the late windows, so the times were taken from the page's embedded `gameTime` JSON.

Weather uses NWS `api.weather.gov` for the kickoff hour, with Open-Meteo as a second read. Roof values come from the CeminiDFS `stadiums.py` table: open and retractable are weather-exposed, dome and semi-open are not. NYJ at LAC is at SoFi and is skipped; TB at DET is indoors.

### Status and scratch rules

The NFL.com designation is primary. Where the ESPN feed is stricter, the row keeps the NFL.com token and is labelled CONFLICT, with both readings shown. A Questionable player stays on the board and is flagged. Token counts: 1 DNP, 5 Doubtful, 19 IR, 4 Limited, 41 Out, 56 Questionable. 65 rows are hard-excluded.

Starting-QB confirmation for the parlay packet is stronger than for the DFS packet: 19 of 20 CONFIRMED from two sources, 1 CONFIRMED_CLUB_NEWS, 0 CLAIMED. Every backup is a hard exclude.

### Scheme and Q4 leans

The packet ranks running backs by fourth-quarter receptions per game, and clubs by quarter script, over 151 final 2026 games. The leans are marked `[TENTATIVE]` and are derived per run, not stored as picks. Game-script priors map spread to COMPETITIVE_LEAD, BENCH_BLOWOUT_RISK, TRAIL_BLOWOUT or NEUTRAL. On a TRAIL_BLOWOUT script the packet ranks `receptions_q4` over 0.5 ahead of `rec_yds_q4` over.

### T-90 checklist

Per-window check times: 11:30 AM ET for the 1:00 PM games, 2:35 PM for 4:05, 2:55 PM for 4:25. The checklist names the players to never enter, the CONFLICT rows to recheck, and the rule that a backup QB removes the slip. Wind at or above 10 mph adds a review note but the leg stays.

### Reuse value

High. This packet is the clearest statement of the CeminiParlays validation gates: dual-source starts, hard-exclude tokens, conflict labelling, and the inactives diff loop. Those rules transfer to any NFL market set. The individual leans expire with the slate.
