---
title: "SMB Capital YouTube — week of 2026-05-22 (3 videos)"
type: source
tags: [source, youtube, smb-capital, tape-reading, options, market-wizards, k79]
keywords: [smbcapital, ugro-tape-read, broken-wing-butterfly, jack-schwager-next-generation, kenny-sharkness]
related:
  - sources/smb-capital-youtube-week-2026-04-14.md
  - sources/smb-capital-youtube-week-2026-05-05.md
  - sources/insights-from-a-gemini.md
  - entities/organizations/smb-capital.md
  - meta/smb-capital-youtube-ingest-cadence.md
  - concepts/tape-reading-order-flow-day-trading.md
  - concepts/broken-wing-butterfly-options.md
  - entities/people/jack-schwager.md
  - sources/insights-from-a-gemini.md
maturity: validated
read_status: deep-read
created: 2026-05-29
updated: 2026-05-29
clusters: [trading-education, order-flow, options, trading-psychology]
---

## Relations

- @entities/organizations/smb-capital.md — channel publisher
- @meta/smb-capital-youtube-ingest-cadence.md — backfill checkpoint
- @concepts/tape-reading-order-flow-day-trading.md — video 1 synthesis
- @concepts/broken-wing-butterfly-options.md — video 3 synthesis
- @entities/people/jack-schwager.md — video 2 guest
- @sources/insights-from-a-gemini.md — prior SMB PlayBook mention

## Raw Concept

| Field | Value |
|-------|-------|
| Channel | [SMB Capital (@smbcapital)](https://www.youtube.com/@smbcapital) |
| Batch window | 2026-05-22 → 2026-05-29 (calendar week) |
| Videos | 3 (channel publishes ~1–2/week; sparse week) |
| Transcripts | yt-dlp auto-captions (en VTT → text) |
| Location | `.local/smb-capital-youtube/2026-05-22-week/` → `cemini-librarian:/opt/cemini-bulk/research/smb-capital-youtube-week-2026-05-22-transcripts.md` |
| Read | 2026-05-29 deep-read (transcript) |

## Narrative

First **K79** batch of SMB Capital YouTube backfill (newest-first). High signal density on **tape reading**, **SPX broken wing butterflies**, and **Market Wizards: The Next Generation** (June 9 release).

### Video index

| # | Date | ID | Title | Route |
|---|------|-----|-------|-------|
| 1 | 2026-05-23 | [AZy-LET8THE](https://www.youtube.com/watch?v=AZy-LET8THE) | The Skill That Separates $50K from $500K Traders | @concepts/tape-reading-order-flow-day-trading.md |
| 2 | 2026-05-21 | [34TnfjFWbj8](https://www.youtube.com/watch?v=34TnfjFWbj8) | How To Become A Market Wizard with Jack Schwager (and George Coyle) | @entities/people/jack-schwager.md |
| 3 | 2026-05-19 | [FDGN3sMF8AY](https://www.youtube.com/watch?v=FDGN3sMF8AY) | How to Trade Broken Wing Butterflies Like a Pro | @concepts/broken-wing-butterfly-options.md |

### Video 1 — tape reading (UGRO)

Jeff Holden walks **four tape moments** on ticker **UGRO**: (a) hidden seller above PM resistance ~$4.15 with fading buyer urgency; (b) post-failure held offer that refreshes ~1h then lifts → sweep/aggression; (c–d) additional intraday transitions. Delivers **30/60/90-day learning protocol** and **four-signal** framework (offer thinning, sweeps, bid stack, print acceleration).

### Video 2 — Schwager / Coyle podcast (~71 min)

- *Market Wizards: The Next Generation* — release **2026-06-09**; **Kenny Sharkness** (SMB) profiled.
- Schwager: books = idea mines; start **small capital**; stop trading when wrong; not a full-time trader himself.
- George Coyle: temperament/strategy fit; Wizard series as style catalog.
- Strategy **decay** discussion (trend-following still trends but choppier; edges compress as crowded).
- SMB desk color on Shark (multi-position bandwidth, calm after stopouts).

### Video 3 — broken wing butterfly (SPX classroom)

- Index options primer (cash settlement, $100/pt, daily SPX expiries).
- **Directional** BWB examples (RSI 30 bullish put side; bearish call side after extended selloff/rally).
- **Non-directional** dual BWB — iron-condor cousin; 10-delta shorts; example +$1,400 on ~$8,600 capital.
- Emphasis: **backtest triggers**, stops, targets; time decay can hide spot risk until late DTE.

### Cemini relevance

1. **Tape reading** — execution confirmation layer for intraday equity stack; L2 vendor required (Bookmap/TC2000/DAS — standard category) **`[TENTATIVE 2026-05-29]`** — methodology from SMB; prod L2 integration = internal gate.
2. **BWB / SPX structures** — options research catalog; prod blocked without backtest kit.
3. **Schwager / Shark** — process psychology reference; book ingest when published June 2026.

### Next batch

Resume at **2026-05-12** video `YqNXTEEn1HQ` — see @meta/smb-capital-youtube-ingest-cadence.md.

## Snippets

> "The tape quite literally tells the story of how other players, how big players are playing the game right now." [Source: https://www.youtube.com/watch?v=AZy-LET8THE (retrieved 2026-05-29)]

> "Our very own SMB heavy hitter, Kenny Sharkness, is one of the Market Wizards in the new book." [Source: https://www.youtube.com/watch?v=34TnfjFWbj8 (retrieved 2026-05-29)]

> "The broken wing butterfly can therefore be directional and it can be non-directional." [Source: https://www.youtube.com/watch?v=FDGN3sMF8AY (retrieved 2026-05-29)]
