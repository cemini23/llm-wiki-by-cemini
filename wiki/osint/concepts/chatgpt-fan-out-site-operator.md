---
title: "ChatGPT fan-out and the site: quality prior"
type: concept
tags: [concept, seo, geo, chatgpt, k241]
keywords: [fan-out, site-operator, retrieved, cited, ChatGPT-5.6]
related:
  - sources/substack-rss-lily-ray-2026-08-17-chatgpt-fan-out.md
  - sources/newsletter-rss-sparktoro-2026-08-18-persona-tool.md
  - sources/newsletter-rss-sparktoro-2026-08-14-zero-click.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @sources/substack-rss-lily-ray-2026-08-17-chatgpt-fan-out.md — primary (Ray + Peec/Nectiv/Resoneo/Suganthan)
- @sources/newsletter-rss-sparktoro-2026-08-18-persona-tool.md — persona tool live (SEO cluster)
- @sources/newsletter-rss-sparktoro-2026-08-14-zero-click.md — website as permanent home

## Raw Concept

What this page answers: why ChatGPT 5.6 retrieves more pages and cites fewer domains, and what an operator should do about `site:`. Synthesized from Lily Ray (2026-08-17) plus the studies she attributes. SEO steal; OSINT awareness.

## Narrative

Fan-out queries are the background searches ChatGPT fires when a prompt needs the live web. They are not the user query. They are the model's guess about *where* a trustworthy answer lives. Two words that the industry keeps collapsing: **retrieved** means a URL the model fetched; **cited** means a URL that survived into the visible answer. After 5.6 they move opposite ways. Retrieval counts roughly doubled (Peec: ~12 → 24). Unique cited domains per response fell (Resoneo: 19 → 15 after 5.3). More pages are considered; fewer get credit.

The `site:` operator is the quality prior. Peec saw it jump from ~0.3% of fan-outs to ~23% the day 5.6 became default; Long's API sample put `site:` in 64% of Sol queries. Opinions go to Reddit and named subreddits. YMYL goes to `.gov`. Specs and pricing go to the brand, including brands the user never typed (Suganthan: 21 of 27 first queries injected brand names; those brands were cited 68.9% of the time vs 2.1% for fetch-only pages). Listicles — the format GEO spam industrialized — lost retrieval share to product pages.

Operator steal, not a ranking hack: (1) always measure retrieved vs cited separately; (2) being named in the *first* fan-out beats being one of 24 retrieved URLs; (3) official pages, `.gov`/`.org` where the query is YMYL, and first-party product URLs are the `site:` targets; (4) listicle farms are the wrong object to optimize. SparkToro's new persona tool is the audience-side complement — know who you are supposed to be the official source *for*. OSINT takeaway is smaller: when an agent cites a page, ask whether it was retrieved or cited, and treat `site:` as a prior, not a dork.

Numbers above are `[TENTATIVE]` (single-newsletter synthesis of third-party studies). SEO brief carries the action list; this page stays the concept.

## Snippets

> "retrieved means a page ChatGPT fetched while running its fan-out queries. Cited means a page that made it into the visible answer as a link." [Source: https://lilyraynyc.substack.com/p/what-we-can-learn-from-evolving-chatgpt (retrieved 2026-08-17)]
