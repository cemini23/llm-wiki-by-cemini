---

title: FlareSolverr — Cloudflare / DDoS-GUARD challenge proxy
type: entity
tags: [entity, tool, anti-bot, k202, integrate]
keywords: [FlareSolverr, Cloudflare, IUAM, MIT, Selenium]
related:
  - sources/eval-github-revenue-browser-automation-2026-07-28.md
  - entities/tools/undetected-chromedriver.md
  - entities/tools/puppeteer.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-28
updated: 2026-07-31
harness_verb: FILE
---

## Relations

- @sources/eval-github-revenue-browser-automation-2026-07-28.md — K202 Integrate
- @entities/tools/undetected-chromedriver.md — Python stealth companion
- @entities/tools/puppeteer.md
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

K202 Phase-0 on [FlareSolverr/FlareSolverr](https://github.com/FlareSolverr/FlareSolverr).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `FlareSolverr/FlareSolverr` |
| **License** | **MIT** (`gh api` 2026-07-28) |
| **Stars / push** | ~15k★ · pushed 2026-07-16 |
| **Verdict** | **Integrate** — GuruWatcher Priority #2 polling through CF |
| **Clone** | `.local/adopts/flaresolverr` (~608K shallow) |
| **Ops** | Local/auth-only; never expose unauthenticated public proxy |
| **Routing** | GuruWatcher · TipDrop · XSP ingest · Atto archives |

## Snippets

> Proxy to bypass Cloudflare IUAM / DDoS-GUARD for claim polling. [Source: @sources/eval-github-revenue-browser-automation-2026-07-28.md]
