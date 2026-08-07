---
title: Panniantong/Agent-Reach — wrapper-only social snapshot normalizer
type: entity
tags: [entity, tool, osint, scraping, adopt-wrapper, k134, k142]
keywords: [agent-reach, yt-dlp, twitter-cli, reddit, cookie-auth, mit, social-snapshot, prompt-injection]
related:
  - entities/tools/grok2api.md
  - sources/eval-github-repos-plan-multi-wiki-2026-06-29.md
  - sources/multi-wiki-url-evaluation-2026-07-03.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/polymarket-bot-architecture.md
maturity: draft
created: 2026-06-29
updated: 2026-07-14
---

## Relations

- @entities/tools/grok2api.md — cookie-auth hazard class (K163/K226)

- @sources/eval-github-repos-plan-multi-wiki-2026-06-29.md — K134 URL 7
- @sources/multi-wiki-url-evaluation-2026-07-03.md — K142 re-audit; direct integration Defer, wrapper-only Adopt
- @concepts/polymarket-bot-architecture.md — PM/Kalshi sentiment ingest steal

## Raw Concept

K134 eval Adopt row for [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) — unified CLI over yt-dlp, twitter-cli, rdt-cli using browser session cookies.

## Narrative

Orchestrates read/search on Twitter/X, Reddit, YouTube, Bilibili without paid API keys by reusing authenticated browser cookies.

**Phase-0 (2026-06-29):** **CONDITIONAL-GO (wiki-only)** — MIT; 45k★; active. **Failure modes:** platform ToS on automated cookie reuse; account ban risk; injection via scraped content. Do not wire to cemini-prod or TipDrop without operator legal review.

**Phase-0 refresh (2026-07-03):** **DEFER** for direct TipDrop/OSINT integration despite strong social-ingest utility. New audit found improved tests around cookie-file permissions and shell metacharacters, but the architectural hazard remains: agents are asked to reuse browser/cookie state and run broad scraping backends. Treat upstream direct integration as no-go until a hardened fork removes cookie exfiltration, account-ban, install-script, and scraped-content injection risk.

**OSINT local adoption (2026-07-03):** **ADOPT WRAPPER-ONLY**. The approved path is `scripts/agent_reach_wrapper/`: a DRY_RUN manual snapshot normalizer that does not launch upstream Agent-Reach, import browser cookies, copy browser profiles, call live networks, or hand data to prod. It enforces source/domain/author allowlists, strict provenance schema, duplicate rejection, prompt-injection rejection, `operator_review: true`, and workspace-confined `.local/agent-reach-wrapper/` output. Tests: `python3 -m unittest scripts.tests.test_agent_reach_wrapper`.

**Steal:** CLI composition pattern for daily digest social pass (`twitter-reader` / `opencli-reader` config in `daily_research_config.yaml`).

**Prefer instead:** Exa MCP + Brave for OSINT default path; wrapper-only Agent-Reach snapshots as a human-reviewed gap-fill when paywalled/social threads block Exa.

## Snippets

> "Leverages localized browser session cookies for authentication, allowing agents to impersonate authenticated human traffic." [Source: eval docx URL 7 (retrieved 2026-06-29)]
