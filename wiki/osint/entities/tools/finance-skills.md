---
title: "finance-skills (himself65) — Agent Skills for Financial Analysis"
type: entity
tags: [tool, steal-and-adopt, agent-skills, finance, yfinance, social-intelligence, generative-ui, adopted]
keywords: [finance-skills, Agent Skills, yfinance, Funda AI, Adanos, Telegram, Twitter, Discord, generative UI, market data]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - sources/trading-posts-compilation-42-2026-05-31.md
  - concepts/tool-evaluation-framework.md
  - concepts/declarative-data-labeling-skills.md
maturity: validated
created: 2026-05-10
updated: 2026-05-31
laptop_install: VERIFIED 2026-05-10 — 6 plugins / 24 skills via `npx plugins add himself65/finance-skills --target claude-code --scope user -y`. Marketplace registered at `~/.claude/plugins/marketplaces/finance-skills`. All 6 enabled in `~/.claude/settings.json`. Requires Claude Code restart to load skills.
upstream_issue: https://github.com/himself65/finance-skills/issues/64 (LICENSE missing despite README MIT claim — filed 2026-05-10)
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 15)
- `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` — Gemini Reject overturned; MIT on GitHub API 2026-05-31
- `@concepts/declarative-data-labeling-skills.md` — Agent Skills pattern relevant here

## Raw Concept

TypeScript monorepo implementing the open Agent Skills standard for financial analysis. Plugins query live market data (yfinance, Funda AI), execute sentiment analysis (Adanos API), monitor Telegram/Twitter/Discord social intelligence. Renders interactive Generative UI widgets in compatible chat interfaces.

- **Repo**: `github.com/himself65/finance-skills`
- **License**: **MIT `[CONFIRMED 2026-05-31]`** — GitHub API `license.spdx_id=MIT` (K88 spot-check). Prior K36 blocker (no LICENSE file, issue #64) appears resolved; verify LICENSE file in repo before prod embedding.
- **Install paths** (Phase-0 verified 2026-05-10):
  - Author's wrapper CLI: `npx plugins add himself65/finance-skills` (installs all 6 plugins) or `--plugin <name>` for one
  - Native Claude Code (no Claude restart required if marketplace API is reachable): `/plugin marketplace add himself65/finance-skills` then `/plugin install <name>@finance-skills` for each of 6: finance-market-analysis, finance-social-readers, finance-data-providers, finance-startup-tools, finance-ui-tools, finance-skill-creator
  - Non-Claude runtimes: `npx skills add himself65/finance-skills -a <agent-name>`
- **Stack**: TypeScript monorepo (6 plugins, v7.0.0)
- **Maturity**: 1,685 ★, last push 2026-05-09 (active)
- **Warning**: README explicitly tags "educational and informational purposes only"

## Narrative

**Recommendation: Split — Steal-from for Cemini prod, Adopt for workflow laptop.**

### Workflow laptop (Adopt — ✅)

Run the TypeScript tools natively via Claude Code during academic-paper analysis. When evaluating algorithmic market anomalies, Claude can autonomously invoke skills to pull historical stock data (yfinance) and back-verify paper claims without manual scraping scripts. Lightweight Node.js footprint.

### Cemini prod (Steal-from — ⚠️ BLOCKED 2026-05-10)

**Phase-0 audit 2026-05-10 surfaced license blocker**: no LICENSE file in repo despite README's MIT claim. Under default copyright, source code is "all rights reserved" — pattern extraction for Cemini-prod re-implementation is not legally safe without upstream clarification. Options:

1. File upstream issue requesting LICENSE clarification (one-line PR offering MIT LICENSE file is the friendly fix)
2. If author responds with explicit MIT confirmation in writing, proceed with extraction
3. If unresolved within 30 days, downgrade Cemini-prod half to **Reject** and rely solely on alternative data sources

Extraction targets (deferred pending license clarification):

1. **Extract API endpoint patterns** for Funda AI + Adanos — connection params, payload structures
2. **Reimplement yfinance polling logic** in Python (extraction strategies + SEC filings parsing patterns)
3. **Skip Generative UI rendering** — irrelevant to headless trading stack

### Risks

- **Educational disclaimer**: README explicit "informational only" warning → robust fail-safes/retry mechanisms likely absent. Don't trust extracted code in live-order paths without hardening.
- **API rate limits + commercial licensing**: Adanos + Funda AI likely require commercial keys for sustained quantitative scraping.
- **Generative UI latency [NEEDS VERIFICATION 2026-05-10]**: if invoked accidentally in headless agent calls, may hang attempting to render HTML/CSS.
- **License verification**: confirm MIT before extracting

[Source: Evaluating Code for Trading Stacks.docx, URL 15]
