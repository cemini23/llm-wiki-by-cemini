---

title: undetected-chromedriver — Selenium stealth patch (GPL isolate)
type: entity
tags: [entity, tool, anti-bot, k202, integrate, gpl]
keywords: [undetected-chromedriver, GPL-3.0, Cloudflare, Selenium]
related:
  - sources/eval-github-revenue-browser-automation-2026-07-28.md
  - entities/tools/flaresolverr.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-28
updated: 2026-07-31
harness_verb: FILE
---

## Relations

- @sources/eval-github-revenue-browser-automation-2026-07-28.md — K202 Integrate (isolate)
- @entities/tools/flaresolverr.md — CF challenge companion
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

K202 Phase-0 on [ultrafunkamsterdam/undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `ultrafunkamsterdam/undetected-chromedriver` |
| **License** | **GPL-3.0** (`gh api` 2026-07-28) |
| **Stars / push** | ~12.7k★ · pushed 2025-07-05 |
| **Verdict** | **Integrate server-side only** — never ship inside Atto kit binaries |
| **Clone** | `.local/adopts/undetected-chromedriver` (~388K) |
| **Routing** | GuruWatcher · TipDrop · prod scrapers |

## Snippets

> Patches Chromedriver to strip automation markers. GPL → no Atto kit distribution. [Source: @sources/eval-github-revenue-browser-automation-2026-07-28.md]
