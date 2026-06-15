---
title: Stronghold 2 Heaven — targeted mechanics scrape (2026-06-13)
type: source
tags: [source, stronghold-2, community, mechanics]
keywords: [popularity, resources, crime, buildings, controls]
related:
  - concepts/stronghold-2-popularity-model.md
  - concepts/stronghold-2-crime-punishment-loop.md
  - concepts/stronghold-2-economy-storage-chains.md
  - concepts/stronghold-2-architect-controls.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - concepts/stronghold-2-systems-inventory.md
read_status: read
source_type: community-wiki
source_url: https://stronghold2.heavengames.com/
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Raw Concept

Second-pass **implementation-focused** scrape while operator plays SH2 in parallel session. Pages fetched 2026-06-13.

## Narrative

### Pages ingested → concept split

| URL | Author | Routed to |
|-----|--------|-----------|
| `/gameinfo/popularity/` | Merepatra | @concepts/stronghold-2-popularity-model.md |
| `/gameinfo/resources/` | Merepatra | @concepts/stronghold-2-economy-storage-chains.md |
| `/faqs/gameplay/` | HeavenGames | popularity + crime + labor caps |
| `/gameinfo/buildings/cservices1/` | — | crime loop § gong, courthouse, falconer |
| `/gameinfo/buildings/cservices2/` | — | guard post, torturer, fire |
| `/gameinfo/buildings/cservices3/` | — | punishment table + honour clock |
| `/gameinfo/buildings/industry1–3/` | — | production graph |
| `/gameinfo/buildings/civilian1–2/` | — | keeps, church, fair, joust, hovel, bedchamber |

### Controls (secondary sources)

| Source | URL | Routed to |
|--------|-----|-----------|
| Stronghold Nation | keyboard shortcuts SH2 | @concepts/stronghold-2-architect-controls.md |
| Stronghold Nation | game views | architect § |
| GameSpy 2004 Bradbury Q&A | (prior ingest) | wall gap / architect intent |

### Fetch failures / 404 (defer)

- `/gameinfo/buildings/farms1/` — 404; farm data from resources + industry pages
- `/gameinfo/buildings/castlestructure1/` — 404; use buildings index
- Dedicated crime page — use FAQ + cservices3

### Walkthrough tactical note [community]

Mission 2 Edwin castle: pause-heavy setup; **one guard post by granary**; crime stack optional but gong + falconer + inn + lord's kitchen fit in expanded layout. See agent-tools walkthrough excerpts in session transcript.

## Snippets

Popularity immigration rule (Heaven):

> 100 is maximum; below 50 people leave and won't return until above 50.

Punishment honour dual-clock (cservices3):

> Honour clock starts when device placed; sentence clock when prisoner arrives — fractional months may gain or lose final +1.

## Dead Ends

- Scraping every military unit stat page — defer to siege phase (Phase D)
