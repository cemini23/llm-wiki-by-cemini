---
title: "Firecrawl — JS-rendering scraper for LLM agents"
type: entity
tags: [entity, tool, web-scraping, llm-agent-tooling, javascript-rendering, sports-consensus-agent, k55]
keywords: [firecrawl, web-scraping, js-rendering, llm-friendly-scraper, search-with-url-filter, sports-analytics-scraper]
related:
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - concepts/sports-prediction-consensus-agent.md
  - entities/people/stacyonchain.md
maturity: draft
created: 2026-05-20
updated: 2026-05-20
---

## Relations

- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — K55 Posts.docx Post 4 explicitly cites Firecrawl as the scraping layer
- @concepts/sports-prediction-consensus-agent.md — the synthesized concept uses Firecrawl in its data-layer stage
- @entities/people/stacyonchain.md — referencing author

## Raw Concept

Web scraping platform with built-in JavaScript rendering, optimized for LLM consumption (returns clean Markdown / structured text suitable for prompt injection). Cited as the scraping layer in @stacyonchain's sports-prediction consensus agent (K55 Posts.docx Post 4).

## Narrative

### What it is

A web-scraping API designed for LLM agents. Key features (per the K55 source code samples):
- **JS rendering** for SPA-heavy sites (sports-analytics platforms, finance sites) where basic scrapers fail.
- **Search-with-URL-filter** — given a query + `url_filter` (domain restriction), returns matching articles + their content.
- **Async Python client** (`firecrawl.FirecrawlApp`) used in the @stacyonchain code samples.
- **Trim-to-N-chars** content output — caller chooses byte limits per article for token-budget control.

### Cited usage in K55

```python
from firecrawl import FirecrawlApp
firecrawl = FirecrawlApp(api_key=FIRECRAWL_KEY)

response = await firecrawl.search(
    query=f"{team_a} vs {team_b} prediction analysis preview",
    url_filter=source["domain"],
    max_results=2
)

for article in response.results:
    results.append({
        "source": source["name"],
        "content": article.content[:2000],  # trim for token efficiency
        "url": article.url
    })
```

### Cemini relevance

- **Adopt-candidate** as a generic scraping primitive for any LLM-driven Cemini research workflow.
- **Direct use cases** in the existing stack:
  - Sports-consensus agent (`@concepts/sports-prediction-consensus-agent.md`) — primary use case from K55.
  - LP-rewards-page scraper for Polymarket reward-pool monitoring (`docs.polymarket.com` Rewards page is partially JS-rendered).
  - News-feed scraping for any future Cemini sentiment / event-detection workstream.
  - Phase-0 source audits (already done manually with `git clone` + grep; Firecrawl could scrape repo READMEs + LICENSE pages programmatically).

### Open questions [NEEDS VERIFICATION 2026-05-20]

1. **License + pricing**: paid SaaS; what are the tiers? Is there a usable free tier?
2. **Self-host alternative?** Is there an open-source self-hostable version, or is it cloud-only?
3. **Rate limits + reliability** for production use?
4. **Comparison vs alternatives**: Bytez (also K55 eval URL 12), Browserbase (already in wiki), pure Playwright (already on the laptop) — does Firecrawl offer enough above these alternatives to justify a paid dependency?

### Cemini fit

- **Defer pending Phase-0**. Sports-consensus agent is the cleanest justification; if Cemini decides to build that workstream, Firecrawl is the natural adoption candidate.
- If not, existing Browserbase / Playwright stack is probably sufficient.

### Connections to other wiki entities

- @entities/tools/browserbase-skills.md — cloud-hosted browser-automation skill set; partial overlap.
- Bytez (K55 eval URL 12 — model-API-bundling SaaS, no entity page created in this batch but flagged as adjacent positioning if a future Cemini decision compares scraping/inference SaaS tools side-by-side).
