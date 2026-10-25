---
title: "mvanhorn/last30days-skill — Multi-Source Recent Research Skill (Python, MIT, 24.3k★)"
type: source
tags: [github, claude-code-skill, multi-source-research, recency-analysis, social-media-scraping, polymarket, hacker-news, reddit, mit-license, ip-sale-clean, gemini-dr-wave4, dual-adopt]
keywords: [last30days-skill, mvanhorn, recency-research, reddit-scraping, x-twitter-scraping, youtube-transcripts, hackernews, polymarket-odds-aggregation, tiktok-instagram-bluesky-truthsocial, claude-code-skill, openclaw-claud-installation, scrapecreators-api, yt-dlp, bird-twitter-client, alternative-sentiment-alpha]
clusters: [llm-agents, dev-tooling, alt-data]
related:
  - entities/tools/last30days-skill.md
  - sources/eval-github-revenue-opportunity-repository-2026-08-02.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/polymarket-informed-minority-gomezcram-2026.md
  - sources/polymarket-predictions-mcp.md
  - entities/platforms/polymarket.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - concepts/mcp-tool-marketplace.md
  - concepts/k254-eval-github-wave.md
  - entities/tools/repo-bootcamp.md
  - sources/eval-github-repo-multi-wiki-copilot-2026-07-06.md
maturity: validated
read_status: read-skim
created: 2026-04-30
updated: 2026-10-25
---

## Relations

- @entities/tools/last30days-skill.md — K218 Phase-0 entity + clone
- @sources/eval-github-revenue-opportunity-repository-2026-08-02.md — K218 refresh
- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A URL 16 Adopt; promoted to dedicated source 2026-04-30
- @sources/polymarket-informed-minority-gomezcram-2026.md — last30days-skill **already extracts Polymarket odds** as one of its data sources; provides a third-Cemini-touchpoint for Polymarket data alongside `@sources/polymarket-predictions-mcp.md` (live odds via MCP) and the LBS/Yale paper's informed-flow analyst proposal
- @sources/polymarket-predictions-mcp.md — sibling Polymarket data layer; this skill is broader (multi-source incl. Polymarket) while polymarket-mcp is narrower (Polymarket-only). For Cemini, polymarket-mcp is preferred for production Polymarket access; last30days is a Workflow tool for ad-hoc research synthesis across many sources.
- @entities/platforms/polymarket.md — Polymarket is one of last30days' data sources
- @concepts/wiki-tooling-evaluation.md — Wave 4 evaluation parent
- @concepts/ip-sale-readiness.md — MIT clean; "no tracking, no analytics, your research stays on your machine" per README
- @concepts/high-signal-paper-patterns.md — rubric: 24,344 stars + 30 contributors + 12 releases + 1,012 tests = high-quality maturity signals across the board. Strongest Wave 4 Adopt by quality-and-popularity combined.

## Raw Concept

- **URL**: https://github.com/mvanhorn/last30days-skill
- **Type**: Open-source Python skill (Claude Code, claude.ai, OpenClaw, Gemini CLI compatible)
- **License**: MIT (Exa-verified 2026-04-30; SKILL.md frontmatter explicit)
- **Stars / Forks**: 24,344 ★ / 2,030 forks
- **Stack**: Python 98.8% / Shell 1.2%
- **Org**: mvanhorn (30 contributors)
- **Created**: 2026-01-23; **Last push**: 2026-04-26 (very active)
- **Releases**: 12 published; latest v3.1.0 2026-04-23
- **Tests**: 1,012 (per README)
- **Required env**: SCRAPECREATORS_API_KEY (primary); optional OPENAI/XAI/OPENROUTER/PARALLEL/BRAVE/APIFY/AUTH_TOKEN/CT0/BSKY/TRUTHSOCIAL keys for additional sources
- **Required bins**: node, python3
- **Discovered via**: Gemini DR Wave 4A 2026-04-29 (URL 16); promoted 2026-04-30

## Narrative

### What it is

An **AI-agent skill** that researches any topic across **Reddit, X (Twitter), YouTube transcripts, Hacker News, Polymarket prediction odds, TikTok, Instagram, Bluesky, TruthSocial, GitHub, and the web** — then synthesizes a grounded summary with citations.

Designed to bypass traditional SEO-driven web search in favor of **real-time social relevancy** signals: upvotes, retweets, financial stakes (Polymarket bets). Cross-platform data aggregation on a single skill invocation.

Surfaces:
- **claude.ai** — upload `last30days.skill` via Settings > Capabilities > Skills
- **Claude Code** — `/plugin marketplace add mvanhorn/last30days-skill`
- **OpenClaw** — `clawhub install last30days-official`
- **Gemini CLI** — clone + `gemini extensions install ./last30days-skill`

### Why Cemini-relevant — dual-adopt structure

**This is the unusual case where Gemini brief recommended adoption on TWO Cemini surfaces simultaneously**:

1. **Workflow Adopt** (laptop) — invoke `last30days <topic>` before drafting wiki pages or briefs to ground them in current sentiment rather than outdated documentation. Direct quality improvement on the user's research process.

2. **Cemini production stack — Steal-from extraction** — the Polymarket + Hacker News fetching modules can be **stripped from the skill and migrated into Cemini's existing 24/7 Python ingest layer** alongside GDELT and Open-Meteo polling. Provides "alternative sentiment alpha" — non-financial-market sentiment signals that may inform ticker research.

### Concrete extraction targets for Cemini

The Cemini production angle is the more interesting one. Specifically:

- **`last30days/sources/polymarket.py`** — the Polymarket odds-fetching logic. Cemini can use this in `services/ingest/polymarket_ingestor.py` (alongside the planned `polymarket-predictions-mcp` integration). Two complementary access patterns: this scraping-style ingest for time-series odds; the MCP for on-demand agent queries.
- **`last30days/sources/hackernews.py`** — HN engagement-weighted scraping. Cemini's analyst orchestrator can consult HN for technical-narrative sentiment around specific tickers (e.g. AVGO + chip-design narratives, AAPL + developer-tooling reactions).
- **`last30days/sources/reddit.py`** — Reddit subreddit-targeted scraping. Highest-fragility module (see Risks).

### Risks & open questions

1. **API fragility on walled gardens** (the dominant risk per Gemini brief) — Tools that scrape X (Twitter), Reddit, etc. via undocumented endpoints "are notoriously susceptible to catastrophic failure when platforms inevitably alter their unauthenticated web endpoints or implement draconian rate limits." For Cemini production: if the upstream walled-garden modifies its anti-scraping defenses, the corresponding ingest module fails silently or noisily. **Mitigation**: per-source health monitoring + fallback patterns + alerting on multi-day-zero-content from any source.

2. **Vendored Node.js Twitter client ("Bird")** — bypasses Twitter API rate limits via headless-browser scraping. Complicates Cemini's pure-Python container deployment philosophy. **For Cemini production extraction**: skip the Twitter module unless paid Twitter API access is provisioned; or accept a Node.js sidecar in the container.

3. **API key sprawl** — primary env: `SCRAPECREATORS_API_KEY`. Optional but recommended: 7+ additional API keys for full multi-source coverage. Cemini's secrets-management layer must accommodate this.

4. **yt-dlp dependency** — for YouTube transcript extraction. Adds an external binary to the deployment; YouTube actively breaks yt-dlp periodically.

5. **Polymarket scraping vs paid Polymarket-MCP**: this skill scrapes Polymarket odds; `@sources/polymarket-predictions-mcp.md` provides MCP-mediated access. **Decision matrix**: scraping is free + fragile; MCP is faster + more reliable but requires its own integration. For Cemini: probably use BOTH — scraping for batch-historical-odds time series; MCP for live agent queries during analysis.

### Cemini-side adoption assessment

**Decision: Dual-Adopt** (Workflow now; Cemini-stack-extraction in a follow-on brief). Concrete next-steps:

**Workflow path** (immediate):
1. License audit ✅ done
2. `/plugin marketplace add mvanhorn/last30days-skill` in Claude Code on the laptop ~5 min
3. Test against a current ticker research topic ("last30days NVDA earnings reaction"); compare against existing research approach
4. Configure with SCRAPECREATORS_API_KEY ~5 min
5. If output quality is high: integrate into wiki-curation workflow as the "current-sentiment ground" step before drafting

**Cemini-stack extraction path** (follow-on):
1. Clone `last30days-skill`
2. Identify the standalone Polymarket + HackerNews modules
3. **Brief to cemini-prod**: `briefs/<date>_last30days-extraction-polymarket-hn.md` proposing the migration pattern (extract → adapt to FastAPI → wire into existing ingest pipeline)
4. Pre-condition: the brief should reference both `@sources/polymarket-predictions-mcp.md` and this page so the cemini-prod-side session can choose which Polymarket access pattern fits production needs

### Citation

> mvanhorn. (2026). *last30days-skill: AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web*. https://github.com/mvanhorn/last30days-skill (MIT License; v3.1.0 latest 2026-04-23; 24.3k stars)

## Snippets

> **Project description (from SKILL.md frontmatter)**:
>
> "Research what people actually say about any topic in the last 30 days. Pulls posts and engagement from Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub, and the web." [Source: https://github.com/mvanhorn/last30days-skill/blob/main/SKILL.md, retrieved 2026-04-30 via Exa]

> **Privacy posture**:
>
> "MIT license. No tracking. No analytics. Your research stays on your machine. 1,012 tests." [Source: https://github.com/mvanhorn/last30days-skill README, retrieved 2026-04-30]

> **Cross-platform reach (per the SKILL.md tags list)**:
>
> "research, deep-research, reddit, x, twitter, youtube, tiktok, instagram, hackernews, polymarket, bluesky, truthsocial, trends, recency, news, citations, multi-source, social-media, analysis, web-search, ai-skill, clawhub" [Source: https://github.com/mvanhorn/last30days-skill SKILL.md frontmatter]
