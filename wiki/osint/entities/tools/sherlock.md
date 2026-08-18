---
title: sherlock — Username social footprinting (Extract → Atto FIND)
type: entity
tags: [tool, atto, osint, k227, mit]
keywords: [sherlock, username enumeration, FIND]
related:
  - entities/tools/tookie-osint.md
  - sources/eval-url-revenue-opportunity-2026-08-08.md
  - sources/substack-rss-secpro-2026-08-07-beyond-threat-hunting.md
  - entities/tools/gosearch.md
  - concepts/cemini-license-posture.md
  - concepts/computational-genealogy-archival-automation.md
  - entities/catalogs/osint4all-people-contact.md
  - sources/eval-multi-wiki-url-revenue-2026-08-18.md
  - entities/tools/mitaka.md
  - entities/tools/bbot.md
  - entities/tools/osint4all.md
maturity: draft
created: 2026-08-08
updated: 2026-08-18
wire_status: policy_wired
wire_target: Atto .cursor/rules/atto-k227-phase1-wires.mdc
wire_note: FIND deep-links Extract; human-gated; ToS/rate limits
---

## Relations
- @entities/tools/tookie-osint.md — K230 FIND sibling

- @sources/eval-url-revenue-opportunity-2026-08-08.md
- @sources/substack-rss-secpro-2026-08-07-beyond-threat-hunting.md
- @entities/tools/gosearch.md
- @concepts/cemini-license-posture.md
- @concepts/computational-genealogy-archival-automation.md
- @entities/catalogs/osint4all-people-contact.md — OSINT4ALL username row (K241)
- @sources/eval-multi-wiki-url-revenue-2026-08-18.md — K241 re-clone
- @entities/tools/mitaka.md — K241 browser OSINT sibling
- @entities/tools/bbot.md — AGPL Extract-only recon sibling
- @entities/tools/osint4all.md — catalog hub

## Raw Concept

K227 Extract. Clone `.local/adopts/sherlock` (~2.5MB).

## Narrative

- **URL:** https://github.com/sherlock-project/sherlock
- **License:** MIT
- **Fit:** username → social accounts for Atto FIND / living-heir discovery — **human-gated**; respect platform ToS; no mass scrape; never Barone PII in fixtures.
- **Combo:** with gosearch (GPL isolate).
- **Verdict:** **GO Extract**.

[Source: URL Revenue Opportunity Analysis.docx URL 7]
