---
title: "camofox-browser — anti-detection browser server for agents"
type: entity
tags: [entity, tool, osint, scraping, playwright, anti-bot, adopt, k71]
keywords: [camofox, camoufox, jo-inc, playwright replacement, cloudflare bypass, rest api, npm]
related:
  - sources/multi-wiki-tool-eval-27url-2026-05-27.md
  - concepts/cemini-license-posture.md
  - entities/infrastructure/cemini-egress-fi.md
maturity: validated
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @sources/multi-wiki-tool-eval-27url-2026-05-27.md — K71 URL 18 Adopt
- @concepts/cemini-license-posture.md — MIT confirmed; not AGPL
- @entities/infrastructure/cemini-egress-fi.md — optional fetch adjunct (laptop); not default prod path

## Raw Concept

K71 eval + GitHub verify: [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) — MIT, ~5.9k★. Camoufox-based **REST browser server** for agents (accessibility snapshots, element refs), not a PyPI drop-in.

## Narrative

### Phase-0 [CONFIRMED 2026-05-27]

| Check | Result |
|-------|--------|
| License | **MIT** (`gh api`) |
| Deploy | `npm install -g camofox-browser` → `npm start` → `http://localhost:9377` |
| vs eval text | Eval said "Playwright replacement" — actually **HTTP API** wrapping Camoufox Firefox fork |
| Prod / librarian | **Laptop adopt only** (2026-05-27 npm global install). Librarian/egress: no daemon deployed — operator-gated if ingest fetch needs it |

### Use in Cemini

- Harden **Exa/fetch gaps** and paywalled pages during ingest — pair with redaction discipline
- Do **not** route prod trading or kb-server RAG through Google/external browser farms

### Guardrails

- Session isolation per target; no prod credentials in cookie import files
- AGPL **bbot** remains separate reject — do not conflate with camofox

## Snippets

> "Anti-detection browser server for AI agents — bypass Cloudflare, bot detection, and anti-scraping." [Source: GitHub jo-inc/camofox-browser README, 2026-05-27]
