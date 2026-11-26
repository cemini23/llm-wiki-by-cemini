---
title: "Operator DFS slate packet — Thanksgiving 2026, NFL Week 12"
type: source
related:
  - concepts/operator-nfl-slate-packet-workflow.md
  - sources/operator-fanduel-thanksgiving-players-2026-11-26.md
  - entities/platforms/fanduel.md
updated: 2026-11-26
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | FanDuel Thanksgiving packet: NFL 2026 Week 12, Thursday Nov 26, 2026 (all three Thursday windows) |
| Author | Cemini23 |
| Type | Operator document, .docx, read-only slate packet |
| Location | `research to be indexed/osint/dfsslatethanksgiving.docx` |
| Retrieved | 2026-11-26 |
| Pages | 153 blocks, 10 tables |
| Read status | read |

## Narrative

### What it is

A read-only injury, reserve and weather packet for the three Thanksgiving games, plus a T-90 checklist. It contains no lineups, no projections, no ownership, no salaries and no bets. [Source: dfsslatethanksgiving.docx]

Packet compiled Tuesday 24 November 2026, 18:10 to 18:20 ET.

### The slate

| Away | Home | Kick (ET) | Venue | Roof |
|---|---|---|---|---|
| CHI | DET | 1:00 PM | Ford Field | Fixed dome |
| PHI | DAL | 4:30 PM | AT&T Stadium | Retractable, call unknown |
| KC | BUF | 8:20 PM | Highmark Stadium | Open air |

Six clubs, three windows. Both schedule sources agree on every kick time.

### Conflict 1 — a task parameter was wrong

The task text named a 12:30 PM ET early window. NFL.com and ESPN both show 1:00 PM ET. No 12:30 game exists in either source. The packet uses the real kicks and logs the difference rather than guessing. The true T-90 is therefore 11:30 AM, not the 11:00 AM the task named.

This is the correct handling: the source of truth is the schedule API, and a wrong instruction is recorded, not silently obeyed.

### Conflict 2 — no Week 12 injury hub

`nfl.com/injuries/league/2026/reg12` returned HTTP 302 to the Week 11 page. The page title confirmed Week 11. The packet therefore used zero NFL.com hub data and fell back to the six club pages, each requested on the explicit `/week/REG-12` path and each verified to show Week 12.

The trap here is real: the default club URLs still serve Week 11 and still display stale OUT rows, for example KC Kenneth Walker III and DAL Jake Ferguson. A reader who takes the default page gets last week's status.

### Status counts

All 62 Week 12 club rows read UNSPECIFIED. The clubs have posted no game status, so there is no club-page Out and no mismatch trigger.

ESPN shows three Out and one Doubtful:

- CHI Elijah Hicks (S), Out — non-skill
- DET Skyler Gill-Howard (DT), Out — non-skill
- DAL Tyler Booker (G), Out — non-skill
- DAL Jake Ferguson (TE), Doubtful — skill, hard-excluded on the ESPN read

The packet keeps both readings and labels the disagreement. It does not average them.

### Reserve and IR

23 skill players sit on club Reserve/Injured across the six clubs: 5 + 3 + 5 + 3 + 6 + 1. That matches the tool's 23 hard excludes. No PUP, suspended or NFI skill players were found.

### Quarterback gate

`qb_starters.py` returned 6 clubs with CONFIRMED 0 and CLAIMED 6. The tool did not force any starter to confirmed. A manual read of each club depth chart agrees with ESPN on all six.

Two caveats the packet records. Several club depth charts are labelled "Unofficial" or carry an old date. And Philadelphia's listed starter is Joe Milton, because Jalen Hurts is on the club Reserve/Injured list.

The packet proposes a second-source file to promote the six to confirmed, and deliberately does not write it, because that cache is shared between two desks. It leaves the write to the owner. This is the right call: a shared cache is a coordination surface, not a private scratch file.

### Weather

Buffalo is the only open-air night game and the one to watch. NWS shows rain at 100 percent, 38 °F, and 10–13 mph north-east wind from 19:00 to 23:00 ET, four days out. Dallas is mild and dry at 54 °F with no precipitation. Wind gusts are absent from the hourly feed and are marked Unavailable, not estimated.

### What failed

- The elevation check failed with HTTP 404 on all six game-roster endpoints. All 23 practice-squad players were excluded with `elevation=NO_EVIDENCE`. This is expected before game day; the packet says to re-run on Thursday.
- The FanDuel salary CSV was not found anywhere on the box. Contest inclusion is therefore UNVERIFIED for every game, including the adjacent Wednesday GB at LAR and Friday DEN at PIT games.

### Honest limits

Every injury status is Tuesday-only. The Wednesday afternoon refresh is required, not optional. The packet says so in its first lines and again in the checklist.

### Read

A clean example of a gate document. Three properties are worth copying: it records a wrong input instead of following it, it keeps the strictest source and labels the conflict, and it never invents a missing value.
