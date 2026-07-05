---
title: Substack RSS ingest cadence
type: concept
tags: [meta, automation, substack, rss, ingest, phase-2]
keywords: [substack, rss, finance, macro, prediction-markets, inbox, cross-wiki]
related:
  - meta/macro-charts-email-ingest-cadence.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/macro-charts-regime-signals.md
maturity: validated
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @meta/macro-charts-email-ingest-cadence.md — paid Macro Charts lane (Gmail)
- @concepts/cemini-wiki-ingest-workflow.md — Phase 2 inbox extension

## Raw Concept

2026-07-05: curated RSS auto-drop for finance/trading Substacks **plus** cross-wiki newsletters (gambling, cyber, SEO/GEO, CCC). Drops land in OSINT `research to be indexed/` with `cross_wiki:` frontmatter; sibling wiki ingest via `cross_wiki_route.py` at K-batch time.

## Narrative

### OSINT-primary (macro / quant)

| Feed id | Publication | Inbox prefix |
|---------|-------------|--------------|
| `macrocharts` | Macro Charts | `macro-charts-rss-*` |
| `moontower` | Moontower Meta | `substack-rss-moontower-*` |
| `last-bear-standing` | The Last Bear Standing | `substack-rss-last-bear-*` |
| `capital-flows` | Capital Flows | `substack-rss-capital-flows-*` |
| `apricitas` | Apricitas Economics | `substack-rss-apricitas-*` |
| `kyla` | Kyla's Newsletter | `substack-rss-kyla-*` |
| `wublock` | Wu Blockchain | `substack-rss-wublock-*` |

### Cross-wiki routes

| Target wiki | Feeds | Route at ingest |
|-------------|-------|-----------------|
| **gambling-wiki** | `outlier-weekly`, `klement`, `event-horizon`, `the-closing-line` | PM retail + sports-betting industry; OSINT keeps bot/CeminiSuite overlap |
| **cybersecurity-wiki** | `tldrsec` (Beehiiv), `secpro`, `seceng-weekly` | Offensive/defensive tooling + agent-security adjacency |
| **seo-wiki** | `lily-ray`, `sparktoro`, `sterling-sky` | GEO/AEO + local SEO; SparkToro/Sterling are WordPress RSS |
| **ccc-wiki** | `pragmatic-engineer`, `latent-space`, `addy-osmani` | Eng leadership, AI eng, Cursor/agent tooling |

**Config:** `config/substack-rss-ingest.yaml`  
**Poller:** `scripts/substack_rss_poller.py` — LaunchAgent `com.cemini.substack-rss-poller` (30 min)  
**State:** `.local/state/substack-rss-posts.json`

**Dedup:** URL registry shared with Macro Charts Gmail poller — paid `macro-charts-paid-forward-*` wins over RSS.

**Skipped after RSS audit:**

| Candidate | Why skip |
|-----------|----------|
| `tldrsec.com/feed` | HTML landing page; real feed is Beehiiv XML |
| `predictionmarketspicks.com` | Near-empty feed |
| `contextwindowsec` | Low cadence; add if it picks up |
| Trail of Bits / Huntress blogs | High signal but not Substack — separate blog-RSS lane if needed |
| Lenny's Newsletter | Product/growth; thin CCC fit |
| Search Engine Journal / Moz / Ahrefs | Noisy trade press; Lily Ray + SparkToro + Sterling Sky cover SEO/GEO better |

**Ingest:** Check `cross_wiki:` in inbox stub → run `python3 scripts/route_newsletter_inbox_cross_wiki.py` (batch) or `cross_wiki_route.py` (single). OSINT keeps trading-stack overlap only.

**2026-07-05 batch:** 28 newsletter RSS drops routed — 7 gambling, 18 ccc, 2 cyber, 1 seo source pages + OSINT pointer stubs.
