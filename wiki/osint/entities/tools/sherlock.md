---
title: sherlock — Username social footprinting (Extract → Atto FIND)
type: entity
tags: [tool, atto, osint, k227, mit]
keywords: [sherlock, username enumeration, FIND]
related:
  - sources/eval-url-revenue-opportunity-2026-08-08.md
  - sources/substack-rss-secpro-2026-08-07-beyond-threat-hunting.md
  - entities/tools/gosearch.md
  - concepts/cemini-license-posture.md
  - concepts/computational-genealogy-archival-automation.md
maturity: draft
created: 2026-08-08
updated: 2026-08-08
wire_status: policy_wired
wire_target: Atto .cursor/rules/atto-k227-phase1-wires.mdc
wire_note: FIND deep-links Extract; human-gated; ToS/rate limits
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-08.md
- @sources/substack-rss-secpro-2026-08-07-beyond-threat-hunting.md
- @entities/tools/gosearch.md
- @concepts/cemini-license-posture.md
- @concepts/computational-genealogy-archival-automation.md

## Raw Concept

K227 Extract. Clone `.local/adopts/sherlock` (~2.5MB).

## Narrative

- **URL:** https://github.com/sherlock-project/sherlock
- **License:** MIT
- **Fit:** username → social accounts for Atto FIND / living-heir discovery — **human-gated**; respect platform ToS; no mass scrape; never Barone PII in fixtures.
- **Combo:** with gosearch (GPL isolate).
- **Verdict:** **GO Extract**.

[Source: URL Revenue Opportunity Analysis.docx URL 7]
