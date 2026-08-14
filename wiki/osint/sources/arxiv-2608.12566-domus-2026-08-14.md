---
title: "Domus — An Open-Data Web Platform for House History Research (arXiv 2608.12566)"
type: source
tags: [arxiv, genealogy, house-history, wikidata, openhistoricalmap, atto, k237]
keywords: [Domus, Wikidata, OpenHistoricalMap, house history, temporal qualifiers, P580, P1319, OHM, Overpass, genealogy]
related:
  - concepts/atto-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
  - entities/tools/ente.md
  - sources/eval-url-revenue-opportunity-2026-08-14.md
  - concepts/e2ee-vault-share.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
read_status: read

---

## Relations

- @concepts/atto-genealogy-agent-kit.md — house-history data model feeds Atto genealogy methodology
- @concepts/computational-genealogy-archival-automation.md — open-records sourcing + temporal property modeling
- @entities/tools/ente.md — house-history + archival images → E2EE vault delivery combo
- @sources/eval-url-revenue-opportunity-2026-08-14.md — K237 eval batch companion

## Raw Concept

| Field | Value |
|-------|--------|
| Paper | arXiv:2608.12566, "Domus: An Open-Data Web Platform for House History Research" |
| Author | David M. Straub (Munich University of Applied Sciences HM) |
| Retrieved | 2026-08-14 |
| File | `arxiv-2608.12566-domus-an-open-data-web-platform-for-house-histor.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/` |
| Type | cs.DL preprint, 7pp, not peer-reviewed |

## Narrative

Map-based, **frontend-only** web platform for crowdsourced house-history research (who lived in a building, ownership, address changes over time). Treats **Wikidata** (linked-data statements with temporal qualifiers, CC0) and **OpenHistoricalMap** (temporal building footprints) as the authoritative data layer; all reads/writes go through public browser-side APIs. MIT-licensed, deployed at domus.genealogy.net. Built substantially with Claude-assisted development.

### Why it matters for Atto

The house-history **record data model is directly portable** to Atto's genealogy agent kit:

- **Temporal property model** (Table 1): address history as free-text string with P580/P582 start/end qualifiers (handles pre-grid village house numbers + administrative reorganizations); occupants/owners as linked person items with date ranges; P571/P576 construction/demolition; **P1319/P1326 earliest/latest-date brackets for archival date-uncertainty** ("before 1409"); P167/P1398 succession across rebuilds.
- **Mandatory sourcing + 3 source types**: online URL / archival document (archive item + call number + page) / book. Form submission hard-blocked without a source — a strong provenance pattern for any genealogy agent.
- **Calendar model**: proleptic Julian before 1583, Gregorian after; date precision down to decade/century accepted.
- **Spatial discovery**: bounding-box SPARQL at zoom ≥14 (1,000–3,000 entities per urban viewport in 700–800 ms); precomputed building-type P279 subclass-hierarchy asset (<200 KB, <1 ms/entity membership) avoids server-side SPARQL property-path timeouts.
- **OHM integration**: Overpass footprint fetch by Wikidata QID + `wikidata=*` tag writeback; time slider through successive footprints.
- **Historical raster overlays**: LGL-BW / swisstopo / Staatsbibliothek zu Berlin cadastral + topographic surveys via a small self-contained layer registry (openly licensed only) — the closest thing to IIIF/archive-image integration; worth checking whether those archives expose IIIF manifests for an Atto image layer.
- **Frontend architecture**: dual OAuth 2.0 PKCE (Wikimedia + OHM), JSON Patch incremental editing (no overwrites), CORS as hard requirement, replication-lag staleness/refetch (5–60 s handled client-side).

### Dead ends / limits

Frontend-only design fully dependent on public endpoint rate limits (no caching layer); uneven Wikidata building coverage by region; GOV (P2503) integration sparse; a connection to CompGen's digitized historical city directories (occupants-per-address-per-year) is a natural fit but unexplored.

**Brief:** `../atto/briefs/2026-08-14_k237-ente-e2ee-vault.md` (Domus section). Tier: `[TENTATIVE]` — single non-peer-reviewed source.
