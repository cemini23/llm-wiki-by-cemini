---
title: "Scrapling — adaptive scraping (BSD-3); the Cloudflare bypass is an operator decision"
type: entity
tags: [tool, scraping, scraping-risk, collectibles, tos-question]
keywords: [scrapling, stealthyfetcher, adaptive parsing, cloudflare turnstile, comp scraping, robots.txt]
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md, URL 2, **Integrate** tier. Routed to Collectibles comp and population-report ingestion.

The question this page answers: **how do you keep a scraper working when the target page changes, and what does the "stealth" part actually mean?**

## Narrative

### What it is

A Python scraping framework, **BSD-3-Clause**. Four fetchers, escalating:

| Fetcher | What it does |
|---------|--------------|
| `Fetcher` | Plain HTTP. |
| `DynamicFetcher` | Real browser, no evasion. |
| `StealthyFetcher` | Browser plus anti-bot evasion, persistent sessions, proxy rotation, DoH. |
| Spider | Crawler with optional `robots_txt_obey` and AutoThrottle. |

Plus **adaptive parsing**, which is the feature that actually solves the maintenance problem: element selectors that survive layout changes, so a scraper does not break every time a portal redesigns.

### Phase-0, 2026-11-02 — the honest reading

The report's Integrate rests on one line: "StealthyFetcher (automated Cloudflare Turnstile/Interstitial bypass and TLS/HTTP3 fingerprint spoofing)".

What the README actually supports:

- It says it "Can easily bypass all types of Cloudflare's Turnstile/Interstitial with automation."
- **It describes no mechanism.** "With automation" is the whole explanation.
- The project's own disclaimer says the library is **"for educational and research purposes only"**, tells users to **"Always respect the terms of service of websites and robots.txt files"**, and disclaims responsibility for misuse.
- `robots_txt_obey` is **opt-in and off by default**.

So the capability is claimed by its author, unexplained, and disclaimed for exactly the use it is being adopted for.

### The distinction that matters

Split the tool in two.

**Part A — ordinary scraping.** Plain fetching, browser rendering, and adaptive parsing. This is unremarkable. It reads public pages, respects robots.txt if you set the flag, and throttles. It solves the real problem: a comp site changes its markup and your pipeline breaks.

**Part B — the evasion layer.** StealthyFetcher's fingerprint spoofing and challenge circumvention. This defeats an access control the site owner installed deliberately.

Part A needs no approval. Part B is **not a technical decision**. Whether to defeat a specific site's bot protection is a legal and business question about that site's terms, and the operator owns it. This page cannot answer it, and the tool's own author declines to.

### Recommendation

1. **Adopt Part A for Collectibles.** Adaptive parsing is worth the dependency on its own.
2. **Set `robots_txt_obey`.** It is off by default and there is no reason to leave it off.
3. **Treat Part B as a separate decision, per site**, made by the operator with that site's terms in hand. Do not enable it as a default.
4. **Never route any of this to CeminiParlays.** The report imposes a no-scrape contract there and it stands.

### Reliability caveat

An evasion capability that is claimed but not explained is also hard to trust. When it breaks — and protection vendors update constantly — there is no mechanism to reason about, only a symptom. Budget for the pipeline failing with no diagnosis.

## Snippets

> "Can easily bypass all types of Cloudflare's Turnstile/Interstitial with automation." — README [fetched 2026-11-02]

> "This work is licensed under the BSD-3-Clause License." — README [fetched 2026-11-02]

> "Always respect the terms of service of websites and robots.txt files." — README disclaimer [fetched 2026-11-02]

## Dead Ends

- **Reading the Integrate as a blanket approval.** The report rates the tool. It does not, and cannot, rate your standing to use the evasion layer against a named site.
- **Expecting the stealth path to fail loudly.** No mechanism is documented, so a breakage gives a symptom and no explanation.
