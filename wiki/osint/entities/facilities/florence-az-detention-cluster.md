---
title: Florence AZ detention cluster (ICE SPC vs CoreCivic CAFCC)
type: entity
tags: [entity, facility, ice, detention, arizona, pinal-county, corecivic]
keywords: [Florence, Arizona, SPC, CAFCC, Pinal Parkway, CoreCivic, Idaho DOC, USMS, J&A-26-0143, turnkey]
related:
  - entities/companies/corecivic.md
  - entities/tickers/cxw.md
  - concepts/geo-ice-turnkey-acquisition-thesis.md
  - entities/facilities/california-city-detention-facility.md
  - sources/ice-ja-26-0143-first-american-escrow-2026.md
  - meta/ice-detention-stats-cadence.md
maturity: draft
created: 2026-07-02
updated: 2026-07-02
---

## Relations

- @entities/companies/corecivic.md — CAFCC owner / operator
- @entities/tickers/cxw.md — listed parent equity
- @concepts/geo-ice-turnkey-acquisition-thesis.md — federal turnkey + OAFM real-property frame
- @entities/facilities/california-city-detention-facility.md — peer CXW ICE site (different legal stack)
- @sources/ice-ja-26-0143-first-american-escrow-2026.md — First American J&A primary source (archived)
- @meta/ice-detention-stats-cadence.md — facility ADP vs guaranteed-min screen

## Raw Concept

Entity stub from July 2026 OSINT disambiguating **three distinct facilities** on the Florence, AZ (Pinal County) corridor — federal **Florence Service Processing Center** vs private **Central Arizona Florence Correctional Complex** vs **EOIR immigration court** — and correcting media conflation with ICE turnkey / First American J&A-26-0143 (`70CMSW26P00000027`).

## Narrative

Florence is **not** a single plant. OSINT and press often collapse “ICE in Florence” into “CoreCivic Florence,” which misreads federal real-property activity.

### Site map (do not merge)

| Facility | Address | Owner | Operator / mgmt | Beds (approx.) | ICE relationship |
|----------|---------|-------|-----------------|----------------|------------------|
| **Florence Service Processing Center (SPC)** | **3250 N. Pinal Pkwy** | **U.S. Government / ICE** | **ICE** | **392** | Federal SPC — direct `[CONFIRMED]` |
| **Florence Immigration Court (EOIR)** | **3260 N. Pinal Pkwy** | DHS campus | DOJ court in **DHS-controlled** facility | — | Adjacent to SPC `[CONFIRMED]` |
| **Central Arizona Florence Correctional Complex (CAFCC)** | **1155 N. Pinal Pkwy** (+ 1100 Bowling Rd) | **CoreCivic** | CoreCivic | ~5,000 | **ICE detainees under ops contract** (subset); not fee-simple federal ownership `[CONFIRMED]` |

**GDP (Florence SPC):** management ICE; owner Government/ICE; capacity 392; 3250 N. Pinal Parkway `[CONFIRMED]`. **EOIR:** court “located in a Department of Homeland Security controlled detention facility” — link to SPC website `[CONFIRMED]`.

### CAFCC — mixed-customer private complex (not USMS-only)

CoreCivic facility page customer base `[CONFIRMED]`:

| Customer | Notes |
|----------|--------|
| City of Coolidge | Municipal |
| City of Mesa | Municipal jail contract |
| Pascua Yaqui Tribe of Arizona | Tribal |
| **Idaho Department of Corrections** | **Dedicated unit** — out-of-state overflow |
| Montana Department of Corrections | State contract |
| U.S. Marshals Service | Federal pre-trial (subset) |

**Idaho DOC (Mar 2026):** transferred **120** residents to CAFCC with **~200 more planned** due to Idaho capacity shortfall (~10k population vs ~8.2k beds); **IDOC staff on-site** for contract oversight `[CONFIRMED]`. Opposite of an empty-the-building federal buy signal.

**ICE ops contract (FPDS):** `70CDCR25FR0000041` (~$25M) — detention services at CAFCC; continues **bed-day ops** distinct from fee-simple acquisition `[CONFIRMED]` USAspending.

### First American J&A-26-0143 (Jun 2 award / Jul 1 post)

| Field | Detail |
|-------|--------|
| Award | `70CMSW26P00000027` — First American title/escrow/settlement |
| Value | $240k ($60k base + $180k option) |
| Sites named | **Florence AZ · Krome FL · Batavia NY** |
| Stated purpose | Expand **existing processing centers** — admin, medical, training, detention space |

**Default read for Florence:** **federal SPC / DHS campus expansion** (3250/3260) — **same class as Krome and Batavia** (already ICE-owned federal SPCs). **Not** stated: seller = CoreCivic, parcel at 1155 N. Pinal, or turnkey buy of CAFCC.

**Weak read for CXW turnkey:** multi-tenant CAFCC + active Idaho/Montana/state contracts + no Pinal grantee deed (recorder sweep through 2026-07-02) + no CXW 8-K `[INFERENCE]`.

### Pinal County recorder watch (2026-07-02)

- Grantee `UNITED STATES` (Mar–Jul 2026): **no index hits**
- Grantor `CORRECTIONS CORP`: only **1990s** land-stack DEEDs (Eloy/Florence assembly) — not 2026 sale signals
- Prod timer: `cemini-ice-recorder-watch.timer` (4h) — @briefs/2026-07-02_ice-turnkey-recorder-watch-24x7-cemini-prod.md

### Turnkey thesis posture

| Hypothesis | Assessment |
|------------|------------|
| ICE expands **federal SPC** (3250/3260) | **Likely** — matches J&A + GDP + Krome/Batavia pattern |
| ICE buys **adjacent private land** only | **Possible** — urgency “seller” = landowner |
| ICE **turnkey-buys entire CAFCC** from CoreCivic | **Low** — mixed customers, Idaho actively filling beds, no deed/8-K |

CAFCC may remain on a **long-dated** WaPo-style shortlist as a **messy tranche-2** node; **J&A-26-0143 alone is weak evidence** for that leg.

## Snippets

> This immigration court is located in a Department of Homeland Security controlled detention facility.
> — [Source: DOJ EOIR Florence Immigration Court (retrieved 2026-07-02)](https://www.justice.gov/eoir/florence-immigration-court)

> Customer base: City of Coolidge, City of Mesa, Pascua Yaqui Tribe of Arizona, Idaho Department of Corrections, Montana Department of Corrections, U.S. Marshals Service — Facility Type: Multi-Level Security, Owned since 1994
> — [Source: CoreCivic CAFCC facility page (retrieved 2026-07-02)](https://www.corecivic.com/facilities/central-arizona-florence-correctional-complex)

> Residents from the Idaho Department of Correction (IDOC) are housed together within a dedicated unit at the facility.
> — [Source: Idaho DOC CAFCC page (retrieved 2026-07-02)](https://www.idoc.idaho.gov/content/locations/prisons/cafcc)

> The scope of this acquisition is to provide real estate title abstract, escrow and settlement services of properties in Florence, AZ, Krome, FL, and Batavia, NY. These properties are required to meet operational requirements for modernizing and enhancing immigration detention and enforcement capabilities for ICE. The existing processing centers in these locations will be expanded…
> — [Source: SAM.gov J&A-26-0143 / Project Salt Box summary (retrieved 2026-07-02)](https://www.projectsaltbox.com/p/ice-awards-240000-sole-source-contract)

## Dead Ends

- **Saltbox / press default = CoreCivic buy** — anchored on CAFCC conditions litigation (e.g. Emmanuel Damas) without seller/parcel in J&A; conflates **ICE detainees at CAFCC** with **ICE buying CAFCC deed**.
- **USMS-only framing for Florence** — CAFCC is **multi-jurisdiction**; weak analog to Cal City Bonta USMS application-swap narrative.
