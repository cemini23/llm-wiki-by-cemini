---
title: "CeminiParlays Sunday slate packet — NFL Week 10, 2026-11-15"
type: source
related:
  - concepts/operator-nfl-slate-packet-workflow.md
  - sources/operator-parlays-slate-2026-11-22.md
  - sources/operator-parlays-recap-week9-2026-11-08.md
updated: 2026-11-25
read_status: skimmed
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | CeminiParlays Sunday slate packet 2026-11-15 |
| Author | Operator working file (CeminiParlays desk) |
| Type | Operator document, .docx, packet bundle |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/laysslate.docx` |
| Retrieved | 2026-11-25 |
| Slate date | 2026-11-15 |
| Read status | skimmed (opening sections and tables) |

## Narrative

### What it is

The Week 10 CeminiParlays packet, for Sunday 15 November 2026. Same eleven-file bundle as the Week 11 packet. No book opened, no slip placed. [Source: laysslate.docx]

### Slate

Eleven games including the Munich international game at 9:30 AM ET: one at 9:30 AM, seven at 1:00 PM, two at 4:05 PM, one at 4:25 PM. 22 team rows in `environment.csv`. Munich is a neutral site and is not in the `stadiums.py` table, which the packet notes.

### Weather notes worth keeping

Two live forecast disagreements are recorded rather than resolved:

- San Francisco at Dallas: the NWS hourly period shows 17% precipitation probability at kickoff, while the NWS Sunday day text says rain showers with a 100% chance and 0.75 to 1 inch. Both readings are listed. A roof-closed call at AT&T Stadium would remove the weather; none was found at build time.
- Houston at Cleveland: 39% hourly probability at kickoff against a day text of "rain likely, 60%". Open-air lakefront site.

That is the useful pattern: when two products from the same provider disagree, show both and do not pick one.

### Reuse value

Medium. The Week 11 packet supersedes the structure. This file is worth keeping for the weather-disagreement handling and for the neutral-site gap in the stadium table. The leans themselves expire.

The companion recap for the preceding week is `operator-parlays-recap-week9-2026-11-08.md`.
