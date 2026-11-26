---
title: "FanDuel Thanksgiving player list — NFL Week 12, 26 November 2026"
type: source
related:
  - concepts/operator-nfl-slate-packet-workflow.md
  - sources/operator-dfs-slate-thanksgiving-2026-11-26.md
  - entities/platforms/fanduel.md
updated: 2026-11-26
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | thanksgivingplayerscsv.csv — FanDuel player list |
| Author | FanDuel contest export, no named author |
| Type | Operator working file, .csv |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/thanksgivingplayerscsv.csv` |
| Retrieved | 2026-11-26 (file timestamp 2026-11-25 17:40) |
| Pages | 153 data rows, 17 columns |
| Read status | read (structure, counts and injury column) |

## Narrative

### What it is

The FanDuel player pool for the Thanksgiving slate. One row per player, with salary, average fantasy points per game, team, opponent and an injury indicator. [Source: thanksgivingplayerscsv.csv]

### Structure

Columns: `Id`, `Position`, `First Name`, `Nickname`, `Last Name`, `FPPG`, `Played`, `Salary`, `Game`, `Team`, `Opponent`, `Injury Indicator`, `Injury Details`, `Tier`, one empty column, `Roster Position`.

The empty column is a real artefact of the export and should be dropped on ingest, not renamed.

### Contents

| Measure | Value |
|---|---|
| Data rows | 153 |
| Rows per game | 51, in each of the three games |
| Games | CHI@DET, KC@BUF, PHI@DAL |
| Positions | WR 57, TE 37, RB 34, QB 19, D 6 |
| Salary range | 3,400 to 11,600 |
| Roster slots | QB, RB/FLEX, WR/FLEX, TE |

The even 51/51/51 split across the three games confirms the export is a Thursday-only slate. It does not contain the Wednesday GB at LAR or the Friday DEN at PIT games.

### Injury column

28 of 153 rows carry an injury indicator. Three are Out and two are Questionable:

| Player | Position | Indicator |
|---|---|---|
| Kenneth Walker III | RB | O |
| Jake Ferguson | TE | O |
| Roschon Johnson | RB | O |
| Dalton Kincaid | TE | Q |
| Noah Gray | TE | Q |

The remainder are IR. Jalen Hurts is on IR, which matches the depth-chart finding in the slate packet.

Under the desk rule, Out and IR are hard excludes and Questionable stays in. So five rows drop on this file and five stay flagged.

### Why this file matters for the record

The slate packet, compiled 24 November, reports that the FanDuel salary CSV was not found anywhere on the box, and marks contest inclusion UNVERIFIED for every game.

This file has a timestamp of 25 November, 17:40. So the gap closed after the packet was written. Both statements are true, in order. The lesson is procedural: a packet should record the file timestamp it searched for, so a later arrival does not look like an error.

This file also resolves contest inclusion. The three games in the export are exactly the three Thursday games. The adjacent Wednesday and Friday games are not on this slate.

### Honest limits

`FPPG` and `Played` are FanDuel's own averages over a partial season, not a projection. `Salary` is the FanDuel price at export time and moves until lock. No projections, ownership or contest size is in the file.

### Read

A clean salary export, and the missing input that closed the one open item in the Week 12 packet.
