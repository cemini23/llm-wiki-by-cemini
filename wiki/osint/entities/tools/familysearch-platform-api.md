---
title: FamilySearch Platform API
type: entity
tags: [tool, genealogy, api, familysearch, draft]
keywords: [FamilySearch, OAuth, GEDCOM, person search, places authority]
related:
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
  - concepts/computational-genealogy-archival-automation.md
  - sources/gemini-sellia-calabria-archive-routing-2026-07-11.md
maturity: draft
created: 2026-07-09
updated: 2026-10-25
---

## Relations
- @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md — K176 GPUOLOGY business DR
- @concepts/gpuology-genealogy-agent-kit.md — product strategy concept

- @sources/gemini-automated-deep-genealogy-research-2026-07-09.md — REST-over-scrape recommendation
- @concepts/computational-genealogy-archival-automation.md — metadata / tree traversal step

## Raw Concept

Official FamilySearch developer REST API (OAuth 2.0 / PKCE; `unauthenticated_session` for limited harvest). Docs: [developers.familysearch.org](https://developers.familysearch.org/).

## Narrative

| Field | Value |
|-------|-------|
| **Useful endpoints (roadmap)** | person, parents, matches, places search |
| **Why cited** | FamilySearch web UI uses Shadow DOM; scrapers (`BeautifulSoup` / naive Selenium) break; API is the supported path |
| **Verdict** | **Watch → commercial CONDITIONAL** — free developer app; production keys need Compatibility Review |
| **Policy** | Stay within FamilySearch terms; no anonymous mass scrape of viewer HTML |
| **K176 (GPUOLOGY)** | **BYO-auth local client only** — apps that “simply copy data out without providing value back” are denied; throttle ~18s work / 1 min → HTTP 429 [Source: @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md] |

Python `requests`/`httpx` clients are enough; official Python SDK noted as legacy/partial in the Gemini source.

Before any product ship: submit Read API framing as **local user-authenticated lookup**, not bulk extract.

## Snippets

> Use authorization_code + PKCE (or unauthenticated_session for limited reads) rather than Shadow-DOM scraping. [Source: @sources/gemini-automated-deep-genealogy-research-2026-07-09.md]

> Compatibility review + anti “copy out without enrich” rule. [Source: @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md]
