---
title: GEO ICE turnkey acquisition thesis — investigative OSINT synthesis
type: concept
tags: [concept, osint, geo-group, ice, event-study]
keywords: [turnkey, 8-K, McFarland, DRI, bridge contract, annex consolidation, EJM55, N5000P, aviation]
related:
  - entities/companies/geo-group.md
  - entities/tickers/geo.md
  - entities/companies/corecivic.md
  - entities/tickers/cxw.md
  - entities/facilities/california-city-detention-facility.md
  - entities/facilities/florence-az-detention-cluster.md
  - concepts/cxw-california-city-ice-turnkey-research-2026-06-29.md
  - concepts/ice-turnkey-research-backlog-2026-06-30.md
  - meta/ice-facility-jobs-cadence.md
  - sources/geo-group-ice-turnkey-investigation-2026-04-09.md
maturity: draft
created: 2026-06-13
updated: 2026-07-04
---

## Relations

- @entities/companies/geo-group.md
- @entities/tickers/geo.md
- @entities/companies/corecivic.md — peer operator in ~10-facility turnkey talks
- @entities/tickers/cxw.md
- @entities/facilities/california-city-detention-facility.md — messiest CXW CA node (June 2026 research)
- @entities/facilities/florence-az-detention-cluster.md — SPC vs CAFCC disambiguation (Jul 2026)
- @concepts/cxw-california-city-ice-turnkey-research-2026-06-29.md — CXW/CA legal + bull/bear synthesis
- @concepts/ice-turnkey-research-backlog-2026-06-30.md — Tier 0 site ranking (Montgomery #1, Tacoma strategic #4); no 8-K confirm
- @meta/ice-facility-jobs-cadence.md — recurring jobs anomaly monitor for GEO/CXW target clusters
- @sources/geo-group-ice-turnkey-investigation-2026-04-09.md

## Raw Concept

Synthesis of April 2026 operator investigative briefs on a hypothesized GEO/ICE turnkey portfolio transaction. Distinct from the retracted 2026-04-23 schema-level "DRI thesis" — this page cites only the K114 source cluster.

## Narrative

### Indicator classes (from briefs) `[TENTATIVE]`

| Class | Claimed signal |
|-------|----------------|
| Procurement | Bridge contract expiry; anomalous modification spikes on existing ICE vehicles |
| Corporate | CFO equity tied to ROCE; revolver draw vs burn-rate cliff |
| Physical | Facility activation hiring patterns; annex legal consolidation |
| Aviation | Executive jet movements + BARR privacy |
| Political | Congressional inquiry timing vs voluntary disclosure delay |
| Legal | California AB 1801 friction on McFarland cluster |

### Disclosure timing model

Briefs model **SEC 4-business-day** 8-K obligation from signature date — used to align options expiry with expected press release **`[NEEDS VERIFICATION 2026-06-13]`**. As of ingest date (2026-06-13), the April 2026 window is **historical**; use page for tradecraft reference (OSINT + event-study framing), not active positioning.

### Verification pass (Exa/press, 2026-06-13)

| Claim | Tag | Notes |
|-------|-----|-------|
| ICE discussing **purchase of GEO turnkey facilities** | `[CONFIRMED]` | Zoley on Q1 2026 earnings call; Axios May 2026; ~10 processing centers discussed |
| **McFarland / Central Valley Annex** activation | `[CONFIRMED]` | CalMatters / LA Times Apr 28 2026 — ~700 beds, detainee transfers underway |
| **$300–400M** portfolio size | `[TENTATIVE]` | Brief assertion; no SEC filing match in quick pass |
| **April 16–17 2026 8-K** / Apr-17 options catalyst | `[RETRACTED]` | Window passed without verified 8-K; Zoley cited Q2–Q3 2026 for potential sales |
| **$100M revolver draw** liquidity cliff | `[RETRACTED partial]` | Jan 2026: revolver **expanded** $450M→$550M (8-K Jan 20–22) — not same as draw thesis |
| Rivers **$619K bridge** / **EJM55** OPSEC | `[CONFIRMED]` | **EJM55 = callsign for N5000P** (Geo Leasing LLC); Apr brief misread as tail. ADS-B history LADD/paywall-blocked on public trackers 2026-06-29 |
| **GEO corporate jet — consecutive DC weekends (Jun 2026)** | `[CONFIRMED reg / TENTATIVE routing]` | **N5000P** (Bombardier Global 5000, hex **A63C56**); operator-reported: wk1 **DC → NJ**; wk2 (**~Jun 28–29**) **DC only** |

Report: `.local/reports/k114-local-eval-2026-06-13.md`

### Aviation signal — N5000P / EJM55 (GEO corporate jet)

**Aircraft identity** `[CONFIRMED]`

| Field | Value |
|-------|-------|
| **Registration** | **N5000P** |
| **Type** | Bombardier Global 5000 (GL5T), msn 9655, built 2014 |
| **ICAO hex** | A63C56 |
| **FAA owner** | **Geo Leasing LLC** — 4955 Technology Way, Boca Raton FL 33431 (GEO Group HQ) |
| **Officer** | **George C. Zoley**, Manager (FL Sunbiz / commerceflorida) |
| **Operator (Part 135)** | Executive Jet Management — callsign **EJM55** |
| **Apr 2026 brief "EJM55"** | Was **callsign**, not a separate tail — same airframe |

**Jun 2026 weekend pattern** `[CONFIRMED reg; TENTATIVE routing — ADS-B transponder observation]`

Observed via **free ADS-B transponder tracking** (friend's live track; exact timestamps/airports not yet archived). Commercial trackers (FlightAware/FR24) often hide **N5000P** under LADD; **ADS-B Exchange**-class receivers still pick up Mode S.

| Trip | Routing (reported) | Plausible read |
|------|-------------------|----------------|
| Weekend 1 (~Jun 21–22) | Boca area → **DC** → **NJ** | DHS/ICE/Congress + **Delaney Hall / Newark** (GEO ~1,000-bed NJ ICE contract) or TEB/EWR |
| Weekend 2 (~Jun 28–29) | Boca area → **DC** → return | Continued federal-side talks (turnkey, Venturella/Schroyer transition, Warren ethics) |

Typical routing: depart **PBI/FXE/FLL** → **DCA/IAD/BWI**; NJ leg likely **TEB/EWR**.

**Archive backlog:** Friend to export legs when convenient — need **dep/arr ICAO + UTC times** for Jun 21–22 and Jun 28–29 to upgrade routing to `[CONFIRMED]`.

**Thesis read:** Resolves K114 backlog — GEO jet = **Zoley-controlled Geo Leasing LLC**. Back-to-back DC weekends = **weak accelerant** (talks live), not an **8-K** substitute.

**Tracking note:** N5000P is a good case study for **LADD vs ADS-B Exchange** — FR24 showed no free history (2026-06-29) while transponder receivers still capture **EJM55** / hex **A63C56**.

**Counter-read:** Mullin warehouse retreat + no GEO sale 8-K — jet reflects **ongoing negotiation**, not imminent close.

### Verification backlog

- USAspending / FPDS contract award for McFarland / Rivers
- GEO 8-K and 10-Q liquidity discussion (Q1 2026)
- California AB 1801 legislative status
- ADS-B/BARR flight logs — **N5000P / EJM55 resolved**; Jun 2026 DC weekend legs need ADS-B Exchange premium export

### CoreCivic parallel (June 2026) `[CONFIRMED partial]`

WaPo draft (Dec 2025) lists **2 CoreCivic + 6 GEO** facilities on ICE acquisition shortlist. June 2026 OSINT pass on **California City** (2,560 beds) finds federal purchase **legally viable during local appeal** but CA City likely **tranche 2** due to **Gomez Ruiz** PI (Feb 2026) + external monitor — not municipal veto. Full scorecard: @concepts/cxw-california-city-ice-turnkey-research-2026-06-29.md.

**Florence AZ cluster (Jul 2026):** J&A-26-0143 ($240k First American title/escrow) names Florence with Krome FL and Batavia NY — **federal SPC expansion** pattern, **not** a named CoreCivic seller. CAFCC (1155 N. Pinal) is **multi-customer** (Idaho DOC actively filling dedicated unit Mar 2026); Pinal recorder sweep **no** 2026 U.S. grantee deed. Detail: @entities/facilities/florence-az-detention-cluster.md.

**Cemini posture:** wiki-only; no prod brief unless operator reopens GEO/CXW workstream.

## Snippets

> "EJM55" in the April 2026 investigative brief = **callsign** for **N5000P** (Geo Leasing LLC), not a separate tail number.
> — [Source: FAA registry via aircraftdata.org; flightdb.net; operator tail ID 2026-06-29]
