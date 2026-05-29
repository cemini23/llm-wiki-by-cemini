---
title: "SMB Capital YouTube — week of 2026-05-05 (2 videos)"
type: source
tags: [source, youtube, smb-capital, execution-discipline, prop-desk, k79]
keywords: [five-day-trading-mistakes, prop-desk-structure, jeff-holden, team-trading, pre-market-volume]
related:
  - entities/organizations/smb-capital.md
  - meta/smb-capital-youtube-ingest-cadence.md
  - sources/smb-capital-youtube-week-2026-04-14.md
  - sources/smb-capital-youtube-week-2026-05-22.md
  - concepts/day-trading-execution-mistakes-smb.md
  - concepts/prop-desk-team-trading-collaboration.md
  - concepts/tape-reading-order-flow-day-trading.md
maturity: validated
read_status: deep-read
created: 2026-05-29
updated: 2026-05-29
clusters: [trading-education, execution, prop-trading]
---

## Relations

- @entities/organizations/smb-capital.md — channel publisher
- @meta/smb-capital-youtube-ingest-cadence.md — batch 2 checkpoint
- @sources/smb-capital-youtube-week-2026-05-22.md — prior batch (tape reading, Schwager, BWB)
- @concepts/day-trading-execution-mistakes-smb.md — video 1 synthesis
- @concepts/prop-desk-team-trading-collaboration.md — video 2 synthesis
- @concepts/tape-reading-order-flow-day-trading.md — cross-link mistake #3 + follow-up video reference

## Raw Concept

| Field | Value |
|-------|-------|
| Channel | [SMB Capital (@smbcapital)](https://www.youtube.com/@smbcapital) |
| Batch window | 2026-05-05 → 2026-05-18 (gap before batch 1) |
| Videos | 2 |
| Location | `.local/smb-capital-youtube/2026-05-05-week/` → `cemini-librarian:/opt/cemini-bulk/research/smb-capital-youtube-week-2026-05-05-transcripts.md` |
| Read | 2026-05-29 deep-read |

## Narrative

**K79 batch 2** — execution mistakes + prop desk collaboration.

### Video index

| # | Date | ID | Title | Route |
|---|------|-----|-------|-------|
| 1 | 2026-05-12 | [YqNXTEEn1HQ](https://www.youtube.com/watch?v=YqNXTEEn1HQ) | The 5 Day Trading Mistakes Robbing Your Account ($10k+ per month) | @concepts/day-trading-execution-mistakes-smb.md |
| 2 | 2026-05-05 | [R04-2QQXkYc](https://www.youtube.com/watch?v=R04-2QQXkYc) | The Secret Structure of 8-Figure Prop Desks | @concepts/prop-desk-team-trading-collaboration.md |

### Video 1 highlights

Jeff Holden (head of trader development): Marcos case study — +$400 morning → −$570 by noon via five recurring mistakes. SMB 20-trader intervention: fix execution errors 60 days → 16/20 back on track. Five mistakes enumerated in closing; resistance partial-profit stats (68% first-test hold).

### Video 2 highlights

Desk talk on **team trading** vs lone-wolf myth; shared workspace with ticker-attached catalyst notes + **theme tracker**; pre-market **>20% ADV** alert threshold; Fastly 200% ADV earnings inflection example with specialist “pounding the table.”

### Next batch

Resume **2026-04-18** — `mssPkDuQnmY` and `45eaVU5NVi8` (Claude AI trading assistant pair). See @meta/smb-capital-youtube-ingest-cadence.md.

## Snippets

> "Eliminating execution errors, that is the golden ticket to so much growth in trading." [Source: https://www.youtube.com/watch?v=YqNXTEEn1HQ (retrieved 2026-05-29)]

> "When Fastly was doing 200% of its average daily volume… I knew immediately… I needed to share this with my team." [Source: https://www.youtube.com/watch?v=R04-2QQXkYc (retrieved 2026-05-29)]
