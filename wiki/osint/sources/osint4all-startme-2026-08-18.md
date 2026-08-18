---
title: "OSINT4ALL start.me catalog (L1rEYQ, K241)"
type: source
tags: [osint, catalog, startme, k241, socmint]
keywords: [OSINT4ALL, start.me, L1rEYQ, socmint, geoint]
related:
  - entities/tools/osint4all.md
  - concepts/osint4all-catalog.md
  - entities/catalogs/osint4all-geoint.md
  - entities/catalogs/osint4all-records-gov.md
  - entities/catalogs/osint4all-productivity.md
  - entities/catalogs/osint4all-people-contact.md
  - entities/catalogs/osint4all-identity-anon.md
  - entities/catalogs/osint4all-cyber-caution.md
  - entities/catalogs/osint4all-search-domain.md
  - entities/catalogs/osint4all-socmint.md
  - entities/catalogs/osint4all-media.md
  - sources/eval-multi-wiki-revenue-plan-2026-08-18.md
  - sources/eval-multi-wiki-url-revenue-2026-08-18.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
read_status: read
---

## Relations

- @entities/tools/osint4all.md — hub entity
- @concepts/osint4all-catalog.md — how Cemini files public OSINT directories
- @entities/catalogs/osint4all-geoint.md — GEOINT section table
- @entities/catalogs/osint4all-records-gov.md — records / government section table
- @entities/catalogs/osint4all-productivity.md — productivity / toolset section table
- @entities/catalogs/osint4all-people-contact.md — people / contact section table
- @entities/catalogs/osint4all-identity-anon.md — identity / anonymity section table
- @entities/catalogs/osint4all-cyber-caution.md — cyber / high-caution section table
- @entities/catalogs/osint4all-search-domain.md — search / dorking / domain section table
- @entities/catalogs/osint4all-socmint.md — SOCMINT section table
- @entities/catalogs/osint4all-media.md — reverse-image / EXIF / podcast section table
- @sources/eval-multi-wiki-revenue-plan-2026-08-18.md — K241 GitHub eval
- @sources/eval-multi-wiki-url-revenue-2026-08-18.md — K241 URL eval (nested SOCMINT/GEOINT)

## Raw Concept

| Field | Value |
|-------|--------|
| Title | OSINT4ALL |
| Author | Socmint (start.me board) |
| Type | public bookmark dashboard |
| URL | https://start.me/p/L1rEYQ/osint4all |
| Mirror | https://github.com/osint4all/osint4all.github.io (README sha `02877d90`) |
| retrieved | 2026-08-18 |
| Counts | 78 sections, 1454 mirrored links; nine catalogs now cover all 1454 (media heading was the missing 40) |
| Nested hubs | SOCMINT `https://start.me/p/Wp1kpe/socmint`; GEOINT `https://start.me/p/W1kDAj/geoint` |

## Narrative

OSINT4ALL is a large public start.me toolkit (people search, maps, archives, username/email/phone, privacy). Cemini files it as a **catalog**, not a stub farm: section tables live under `@entities/catalogs/osint4all-*.md`. Leak dumps, darknet markets, ransomware directories, unauthorized webcams, and malware-sample repos are **CONTEXT / CAUTION** rows — listed, not visited, no payloads. Authorized OSINT companies may keep public-tool locators; scraping remains authorized-target-only.

Live start.me is Cloudflare-gated from curl; Playwright loaded the first page. The GitHub README is the complete section dump used for ingest.

## Snippets

> "OSINT4ALL aims to provide practical & easy OSINT toolkit for researchers of all level to use." [Source: https://start.me/p/L1rEYQ/osint4all (retrieved 2026-08-18)]
