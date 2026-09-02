---
title: "mitaka — browser OSINT (Extract)"
type: entity
tags: [tool, osint, k241, mit, extract]
keywords: [mitaka, ninoseki, browser-osint]
related:
  - sources/eval-multi-wiki-url-revenue-2026-08-18.md
  - entities/tools/sherlock.md
  - entities/tools/osint4all.md
  - concepts/cemini-license-posture.md
  - concepts/osint4all-catalog.md
  - entities/catalogs/osint4all-people-contact.md
  - entities/catalogs/osint4all-search-domain.md
  - entities/tools/bbot.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
harness_verb: FILE
---

## Relations

- @sources/eval-multi-wiki-url-revenue-2026-08-18.md — K241 URL eval
- @entities/tools/sherlock.md — username sibling
- @entities/tools/osint4all.md — catalog hub
- @concepts/cemini-license-posture.md
- @concepts/osint4all-catalog.md
- @entities/catalogs/osint4all-people-contact.md
- @entities/catalogs/osint4all-search-domain.md
- @entities/tools/bbot.md — AGPL recon sibling

## Raw Concept

K241 Phase-0 Extract. Clone `.local/adopts/mitaka` (2.1MB). MIT confirmed via `gh api` 2026-08-18.

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/ninoseki/mitaka |
| License | **MIT** [CONFIRMED gh 2026-08-18] |
| Local | `.local/adopts/mitaka` (2.1MB) |
| Verdict | **GO Extract** — browser OSINT context-menu |
| wire_status | `policy_wired` |

Browser extension that sends selected IoCs to public OSINT engines. Human-gated; respect site ToS; no Barone PII fixtures; authorized-target only.

## Snippets

> Verdict: GO Extract (MIT). [Source: `.local/reports/license-k241-2026-08-18.md`]
