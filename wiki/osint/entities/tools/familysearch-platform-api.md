---
title: FamilySearch Platform API
type: entity
tags: [tool, genealogy, api, familysearch, draft]
keywords: [FamilySearch, OAuth, GEDCOM, person search, places authority]
related:
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
  - concepts/computational-genealogy-archival-automation.md
maturity: draft
created: 2026-07-09
updated: 2026-07-09
---

## Relations

- @sources/gemini-automated-deep-genealogy-research-2026-07-09.md — REST-over-scrape recommendation
- @concepts/computational-genealogy-archival-automation.md — metadata / tree traversal step

## Raw Concept

Official FamilySearch developer REST API (OAuth 2.0 / PKCE; `unauthenticated_session` for limited harvest). Docs: [developers.familysearch.org](https://developers.familysearch.org/).

## Narrative

| Field | Value |
|-------|-------|
| **Useful endpoints (roadmap)** | person, parents, matches, places search |
| **Why cited** | FamilySearch web UI uses Shadow DOM; scrapers (`BeautifulSoup` / naive Selenium) break; API is the supported path |
| **Verdict** | **Watch** — free developer application; rate-limit aware clients required |
| **Policy** | Stay within FamilySearch terms; no anonymous mass scrape of viewer HTML |

Python `requests`/`httpx` clients are enough; official Python SDK noted as legacy/partial in the Gemini source.

## Snippets

> Use authorization_code + PKCE (or unauthenticated_session for limited reads) rather than Shadow-DOM scraping. [Source: @sources/gemini-automated-deep-genealogy-research-2026-07-09.md]
