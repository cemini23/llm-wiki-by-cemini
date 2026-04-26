---
title: Federal Register API
type: entity
tags: [data-source, regulatory-primary-source, government, news]
keywords: [federal-register, anprm, nprm, final-rule, agency-notice, rin, fr-doc]
related:
  - sources/cftc-anprm-prediction-markets-2026-03-16.md
maturity: draft
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @sources/cftc-anprm-prediction-markets-2026-03-16.md — first concrete use case in this wiki: the CFTC ANPRM (RIN 3038-AF65 / FR Doc 2026-05105 / 91 FR 12516) was retrieved as the canonical primary source via this API; future regulatory ingests should follow the same pattern

## Raw Concept

Added 2026-04-25 from the [public-apis](https://github.com/public-apis/public-apis) curated list during a librarian-hygiene pass. Promoted to a dedicated entity page after the 2026-04-25 post-Kalshi regulatory ingest demonstrated the value of routing regulatory queries through the canonical FR docket rather than secondary aggregators.

## Narrative

The Federal Register REST API exposes the Daily Journal of the United
States Government — proposed rules, final rules, notices, presidential
documents — in JSON form. For Cemini's regulatory tracking thread
(CFTC ANPRMs, DCM Core Principle changes, related agency actions),
this is the single canonical entry point.

**Key endpoints**:

1. **Document search** — `federalregister.gov/api/v1/documents.json`
   with filters by `agencies[]`, `regulation_id_number`, `date.publication_date`,
   `type` (`PRORULE`, `RULE`, `NOTICE`). Returns paginated metadata
   including FR Doc number, full-text URL, RIN, comment-period dates.
2. **Document by FR Doc** — `federalregister.gov/api/v1/documents/
   2026-05105.json` returns the full document record.
3. **Public inspection** — same-day pre-publication notices, useful
   for monitoring regulatory signals before official FR publication.

**Authentication**: none. No rate limit published (be polite — keep
under 1000 req/hour per IP).

**License**: works of the US Government, public domain. No commercial
restrictions.

**Why it matters**: regulatory threads are load-bearing for the
IP-sale-readiness story (Cemini's compliance-leverage thesis depends
on Kalshi's CFTC-DCM status surviving the AZ/CT/IL preemption fight —
see `@concepts/dcm-state-preemption.md`). Citing FR docs by FR Doc
number gives every downstream synthesis a verifiable primary-source
anchor.

## Snippets

- API root: https://www.federalregister.gov/reader-aids/developer-resources/rest-api
- Example: https://www.federalregister.gov/api/v1/documents/2026-05105.json (CFTC ANPRM RIN 3038-AF65)
- Full document: https://www.federalregister.gov/documents/2026/03/16/2026-05105/
