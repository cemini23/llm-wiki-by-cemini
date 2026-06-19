---
title: SH2 Kingmaker YouTube watchlist ingest — 2026-06-19
type: source
tags: [source, stronghold-2, youtube, kingmaker, playtest]
keywords: [kingmaker, youtube, estate, honour, transcript, story-033]
related:
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/operator-vision-sh2-personal-clone.md
  - sources/sh2-youtube-parity-watchlist-2026-06-17.md
  - sources/sh2-heaven-kingmaker-strategy-2026-06-17.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - sources/stronghold-franchise-research-pass2-2026-06-18.md
  - entities/projects/castle-sim.md
read_status: read
source_type: youtube-transcript
maturity: validated
created: 2026-06-19
updated: 2026-06-19
---

## Raw Concept

Seven **Kingmaker-specific** YouTube videos from story-033. Transcripts fetched via `youtube-transcript-api` (2026-06-19). Extends story-030 parity path into skirmish/economy/estates. Operator checklist: `briefs/research/sh2-playsession-checklist-kingmaker.md` (appended to castle-sim master checklist).

## Narrative

### Videos processed

| ID | Title | Transcript | Checklist focus |
|----|-------|------------|-----------------|
| MD8MfO3BuZw | Kingmaker Freeman→King, Three Bridges | ✅ | PvE riding archers, estate raids, promotions |
| vy4546WfkCg | Steam Edition Tutorial | ✅ | Honour, treasury, >50 pop gate, estate buy |
| fJ8wjeMdz9k | Kingmaker Part 2 | ✅ | Guard/fair conflict, crossbows, siege UX |
| 2xcDg5RscRc | Kingmaker mode overview | ✅ | Lobby UX, skirmish location, rank picker |
| P0SrfrucRTo | Multiplayer versus | ✅ | MP estates, Freeman start, tax/honour loop |
| 1NDb5LxGY1I | Beginners Guide — strong economy | ❌ private | `[UNKNOWN]` — use Matt Logan Heaven |
| DBD-20osfiA | Kingmaker India map | ❌ no subs | `[UNKNOWN]` — metadata only |

Transcript archive (local session): `/tmp/sh2-kingmaker-yt-transcripts.json`

### Key `[OBSERVED-YT]` findings (Kingmaker-only)

**Mode UX:** Kingmaker labeled as **skirmish**; not under Multiplayer menu (*2xcDg5RscRc*). Starting ranks include Freeman through Duke.

**Honour / ranks:** Tutorial links honour to promotions, estates, knights (*vy4546WfkCg*). Voice lines on promotion (*MD8MfO3BuZw*). **Enemy lord promoted** announced during PvE (*MD8MfO3BuZw*).

**Estates:** Flag capture for neutral/village estates (*2xcDg5RscRc*, *P0SrfrucRTo*). Distinct **estate attack** advisor line (*MD8MfO3BuZw*). Lost estate = zero estate income (*P0SrfrucRTo*). Carter post **first-use tutorial** (*MD8MfO3BuZw*).

**Economy automation:** Double rations + tax/popularity advisor loop (*MD8MfO3BuZw*, *P0SrfrucRTo*) — **confirms** Matt Logan cheat sheet. Treasury required before tax (*vy4546WfkCg*, *P0SrfrucRTo*). Honour from granary variety (*P0SrfrucRTo*).

**Military:** Three Bridges PvE emphasizes **horse / riding archer** lines (*MD8MfO3BuZw*) — retail merc meta; castle-sim uses **BO2 capped emergency levy** instead. Freeman cannot field troops until promoted (*P0SrfrucRTo*).

**Crime / services:** Guard post **deprioritized** when traveling fair runs (*fJ8wjeMdz9k*). Crime can **jail fletchers**, halting bow production (*P0SrfrucRTo*).

### Matt Logan cross-check

| Heaven guide claim | YouTube confirmation |
|--------------------|----------------------|
| Double rations + cruel tax net >50 | ✅ *MD8MfO3BuZw*, *P0SrfrucRTo* |
| Treasury before tax | ✅ *vy4546WfkCg* |
| Buy/skip full weapon chain (PvE) | `[INFERRED]` fletchers still built when gold-tight |
| 50+ merc horse archers | ✅ riding archer PvE — **defer for clone (BO2)** |
| Carter manual luxury routing | Partial — carter tutorial + manual cancel shown |
| Stocks over executioner | `[OBSERVED-YT]` crime/stocks in MP; executioner not favored |

### Kingmaker gap rank (story-033)

1. Rank-gated build menu + rival promotion callouts  
2. Estate capture + estate raid events  
3. Popularity automation preset  
4. Carter tutorial + multi-estate routing  
5. Fair pulls guards — crime coverage hole  

### Limits

| Topic | Status |
|-------|--------|
| India map choke | `[UNKNOWN]` — no captions |
| Beginners economy build order video | `[UNKNOWN]` — private |
| Exact merc post UI / horse archer count | `[INFERRED]` from PvE voice lines |

## Snippets

```
Enemy estate raid: "Our enemies are attacking one of our estates my lord" — MD8MfO3BuZw
Fair vs guard: "if the guard keeps going to the traveling fair no one is protecting the city" — fJ8wjeMdz9k
```

## Dead Ends

- Replacing Matt Logan guide with private 1NDb5LxGY1I — Heaven scrape remains canonical build order
