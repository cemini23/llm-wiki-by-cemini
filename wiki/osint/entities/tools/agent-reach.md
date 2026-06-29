---
title: Panniantong/Agent-Reach — CLI social read layer for agents
type: entity
tags: [entity, tool, osint, scraping, k134]
keywords: [agent-reach, yt-dlp, twitter-cli, reddit, cookie-auth, mit]
related:
  - sources/eval-github-repos-plan-multi-wiki-2026-06-29.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/polymarket-bot-architecture.md
maturity: draft
created: 2026-06-29
updated: 2026-06-29
---

## Relations

- @sources/eval-github-repos-plan-multi-wiki-2026-06-29.md — K134 URL 7
- @concepts/polymarket-bot-architecture.md — PM/Kalshi sentiment ingest steal

## Raw Concept

K134 eval Adopt row for [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) — unified CLI over yt-dlp, twitter-cli, rdt-cli using browser session cookies.

## Narrative

Orchestrates read/search on Twitter/X, Reddit, YouTube, Bilibili without paid API keys by reusing authenticated browser cookies.

**Phase-0 (2026-06-29):** **CONDITIONAL-GO (wiki-only)** — MIT; 45k★; active. **Failure modes:** platform ToS on automated cookie reuse; account ban risk; injection via scraped content. Do not wire to cemini-prod or TipDrop without operator legal review.

**Steal:** CLI composition pattern for daily digest social pass (`twitter-reader` / `opencli-reader` config in `daily_research_config.yaml`).

**Prefer instead:** Exa MCP + Brave for OSINT default path; Agent-Reach as gap-fill when paywalled threads block Exa.

## Snippets

> "Leverages localized browser session cookies for authentication, allowing agents to impersonate authenticated human traffic." [Source: eval docx URL 7 (retrieved 2026-06-29)]
