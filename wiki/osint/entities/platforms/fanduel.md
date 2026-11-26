---
title: FanDuel — daily fantasy contest platform and salary source
type: entity
maturity: draft
related:
  - concepts/operator-nfl-slate-packet-workflow.md
  - sources/operator-dfs-slate-thanksgiving-2026-11-26.md
  - sources/operator-fanduel-thanksgiving-players-2026-11-26.md
  - entities/companies/draftkings.md
updated: 2026-11-26
---

## Raw Concept

What prompted this page: every CeminiDFS slate packet starts from a FanDuel contest export. The platform is the upstream data source, so its file shape and quirks belong on a page rather than in each packet.

Synthesised from four operator working files: two salary exports (Weeks 10 and 11) and two Week 12 Thanksgiving files.

## Narrative

### What it is

FanDuel is a US daily-fantasy-sports operator. The desk uses it as a read-only data source: a contest export gives the player pool, the salary, and an injury indicator. The desk never places a contest entry from an automated step.

### The export

The player list downloads as a CSV from a contest page. Columns seen in the Week 12 export:

| Column | Use |
|---|---|
| `Id` | Stable player key, formatted as `contest-player` |
| `Position` | QB, RB, WR, TE, D |
| `First Name`, `Nickname`, `Last Name` | Name parts; `Nickname` often repeats the first name |
| `FPPG`, `Played` | Season average and games played, platform-computed |
| `Salary` | Price at export time |
| `Game`, `Team`, `Opponent` | Slate membership, in `AWAY@HOME` form |
| `Injury Indicator`, `Injury Details` | `O`, `Q`, `IR` and free text |
| `Tier` | Often empty |
| `Roster Position` | Slot eligibility, e.g. `RB/FLEX` |

Two quirks matter. The export carries one unnamed empty column, which should be dropped on ingest. And `FPPG` is a backward-looking average, not a projection.

### Why the slate split is useful

The Week 12 export held exactly 51 rows in each of three games. An even per-game split is a quick check that the file belongs to the single slate you think it does. A file with a fourth game is a different contest.

### Injury indicator versus a status feed

The FanDuel indicator is a third read, not a primary source. In Week 12 it agreed with ESPN on the notable cases (Jalen Hurts on IR, Jake Ferguson out) and disagreed with the club pages, which showed UNSPECIFIED for all 62 rows. The desk rule holds: use the platform token for what the platform prices, and keep the primary source for game status.

### Read

The platform page for salary and pool questions. For injury truth, use the club pages.
