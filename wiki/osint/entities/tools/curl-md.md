---
title: curl.md — URL-to-Markdown CLI for AI Agents
type: entity
tags: [tool, ingest-pipeline, llm-context, mit-license, candidate-adopt, laptop-only]
keywords: [curl-md, url-to-markdown, ingest-cli, exa-crawling-alternative, token-optimized-output]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - entities/tools/sift-kg.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 10, originally marked **UNAVAILABLE** at eval time (DR couldn't reach `curl.md/playground` specifically), Exa-resolved 2026-05-06 with full landing-page metadata
- @concepts/cemini-license-posture.md — MIT-licensed, fully clean; no IP-sale concerns
- @entities/tools/sift-kg.md — companion 2026-05-06 K32 Exa-rescued tool; both are candidate ingest-pipeline upgrades

## Raw Concept

CLI tool that turns any URL into LLM-context-optimized markdown. Open source, MIT-licensed. Two usage modes:

1. CLI install: `curl -fsSL https://curl.md/install.sh | bash`, then `curl-md <URL>`
2. Prefix any URL with `curl.md/` (e.g., `curl https://curl.md/<original-url>`) — works as a server-side rewrite proxy

Originally marked **UNAVAILABLE** in K32 Gemini DR eval. Exa-rescued 2026-05-06.

## Narrative

- **URL**: `http://curl.md` ✓ verified via Exa 2026-05-06
- **License**: MIT (per upstream landing page; "fully open source. The source code is public on GitHub under the MIT License")
- **Repo URL**: not directly surfaced in the landing page; need a follow-up Exa or GitHub search to find canonical source
- **Maturity**: not surfaced (no commit count / star count from landing page)
- **Stack**: undisclosed at landing-page level; install method (`bash` from `curl.md/install.sh`) suggests a binary distribution

### Why interesting for Cemini

The current ingest pipeline uses `mcp__exa__crawling_exa` for URL→clean-markdown extraction in the `## Snippets` section of source pages and entity pages. Exa is a paid API; per `CLAUDE.md` the workspace exercises cost discipline (`numResults: 3-5` default, `deep_researcher` reserved).

`curl.md` is a potential **free alternative** for the URL→markdown step specifically. Use cases:

1. **Source-page Snippets** — when a source cites a URL with primary content, extracting that URL's markdown via `curl.md/<URL>` gives Cemini a verbatim quote without burning Exa credits.
2. **Entity-page upstream-README extraction** — for tool entity pages (like this one), extracting the GitHub README via curl.md is cheaper than Exa-crawling.
3. **Brief content-grounding** — when staging briefs for distribution, citing primary URLs with curl.md-extracted markdown avoids re-fetching content during brief revisions.

### Phase-0 audit checklist

1. ⚠ Find canonical GitHub repo (landing page hides the URL)
2. ⚠ Verify MIT license claim against the actual `LICENSE` file
3. ⚠ Verify maturity (commits, last push, star count)
4. **Audit failure mode for ingest-pipeline tool class**: does it work without an API key? Does it have rate limits? Does it work with bot-defense pages (Cloudflare, anti-scraping)?
5. Test against representative Cemini ingest URLs: GitHub README, arXiv paper, Anthropic docs, Polygon API docs
6. Compare: same URL via `mcp__exa__crawling_exa` vs `curl.md/<URL>` — quality, completeness, token count, latency
7. Decide GO / CONDITIONAL-GO / NO-GO

### Adoption stance

**CONDITIONAL CANDIDATE** — Phase-0 audit pending. If MIT license verified and quality is comparable to Exa for our use cases, this becomes a cheap workflow upgrade for laptop-side ingest. Not blocking; do when convenient.

If quality is meaningfully worse than Exa (e.g., misses code blocks, misses tables, misses footnotes), keep Exa as primary and skip adoption.

### Open questions

- ⚠ Canonical GitHub URL (not surfaced in landing page)
- ⚠ Rate limits / SLA / privacy posture (do they log/store URLs sent to the proxy form?)
- ⚠ Output quality vs Exa on representative Cemini-ingest URL classes
- ⚠ Can it be self-hosted? (relevant if revenue-generation downstream means we want to avoid a vendor dependency on yet another small SaaS)

### Adoption status — NOT YET ADOPTED

Phase-0 audit deferred until next ingest cycle or when ingest-cost discipline becomes a bottleneck.

## Snippets

### curl.md core value proposition

> "URL to markdown for agents. Turn websites into optimized, low token output to supercharge your context. Works with every agent." [Source: http://curl.md (retrieved 2026-05-06)]

### License + open-source claim

> "Yes, curl.md is fully open source. The source code is public on GitHub under the MIT License, meaning anyone can use, modify, or contribute to its development. Anyone from the community can file issues, submit pull requests, and extend functionality." [Source: http://curl.md (retrieved 2026-05-06)]
