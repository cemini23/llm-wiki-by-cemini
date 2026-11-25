---
title: "Parlays recap, Week 9 paper tickets — graded 2026-11-10"
type: source
related:
  - concepts/operator-nfl-slate-packet-workflow.md
  - sources/operator-parlays-slate-2026-11-15.md
  - concepts/parlay-market-making.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Parlays recap, Week 9 Sunday 2026-11-08 (paper / unstaked) |
| Author | Operator working file (CeminiParlays desk) |
| Type | Operator document, .docx, graded ticket recap |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/week10recapparlays.docx` |
| Retrieved | 2026-11-25 |
| Slate date | 2026-11-08 |
| Read status | read |

## Narrative

The filename says week 10, but the content is the Week 9 recap for Sunday 8 November 2026. Note the mismatch; the file title is authoritative.

### Status

Six tickets, paper only. Stake is zero on every ticket and no book was opened. The operator pasted the six tickets on 10 November 2026 and said they were not played for money. Settlement and bonus are UNCONFIRMED because no settled sportsbook screenshot exists. [Source: week10recapparlays.docx]

Grading used the official ESPN boxes for full-game markets and ESPN play-by-play for fourth-quarter markets. All five games used were final at retrieval.

### Integrity checks

- Every ticket matches a card leg on player, market, side and line, so `off_card` is false.
- No leg player was out, IR, inactive, doubtful, NFI, PUP or suspended on the official inactive list.
- Two grading discrepancies are recorded and do not change any grade: Nabers receiving yards 43 box against 44 play-by-play, and Milton passing yards 169 against 170.

### Outcomes

Eight unique legs, four hit and four miss. Ticket-weighted legs: 14, with eight hits and six misses, because several legs appear on more than one ticket.

- Two tickets won on paper: the Herbert interception over and the Milton passing-yards under.
- Three tickets lost on Kenneth Walker III's fourth-quarter rushing yards: 12 actual against 14.5 needed.
- The McCaffrey fourth-quarter rushing over missed at 5 yards against 14.5.

Brier score on the joint model probability: 0.30 over all six settled tickets. Book price at placement is `NO_EVIDENCE`, so skill against the market cannot be measured.

### Reuse value

Medium-high. This page is the grading reference for the CeminiParlays offline grader: leg-level citations, hard-exclude checks, and the split between cash P&L and model-fair units. The outcomes themselves are a single slate and prove nothing about the process.

The cash P&L is zero on every ticket, by construction. Do not read the paper win/loss as a track record.
