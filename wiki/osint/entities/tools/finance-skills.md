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
  - entities/tools/tradingview-mcp-atilaahmettaner.md
  - entities/tools/opencli.md
  - sources/tradesdontlie-tradingview-mcp.md
maturity: validated
created: 2026-05-10
updated: 2026-09-18
laptop_install: VERIFIED 2026-05-10 — 6 plugins / 24 skills via `npx plugins add himself65/finance-skills`. Cursor plugin `finance-data-providers` live 2026-09-18 (tradingview MCP, 37 tools). OpenCLI Hyperliquid plugin installed 2026-09-18. OpenCLI tradingview skipped (needs Desktop + login).
upstream_issue: https://github.com/himself65/finance-skills/issues/64 (filed 2026-05-10; LICENSE file added — close if resolved)
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 15)
- `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` — Gemini Reject overturned; MIT on GitHub API 2026-05-31
- `@sources/trading-posts-compilation-42-2026-05-31.md` — K88 ingest
- `@concepts/tool-evaluation-framework.md`
- `@concepts/declarative-data-labeling-skills.md` — Agent Skills pattern relevant here
- `@entities/tools/tradingview-mcp-atilaahmettaner.md` — Cursor `tradingview` MCP (37 tools) live 2026-09-18
- `@entities/tools/opencli.md` — Hyperliquid public `/info` plugin installed; OpenCLI TV skipped
- `@sources/tradesdontlie-tradingview-mcp.md` — CDP Desktop MCP; not installed (no TradingView.app)

## Raw Concept

TypeScript monorepo implementing the open Agent Skills standard for financial analysis. Plugins query live market data (yfinance, Funda AI), execute sentiment analysis (Adanos API), monitor Telegram/Twitter/Discord social intelligence. Renders interactive Generative UI widgets in compatible chat interfaces.

- **Repo**: `github.com/himself65/finance-skills`
- **License**: **MIT `[CONFIRMED 2026-05-31]`** — GitHub API `license.spdx_id=MIT` and **LICENSE file present** in repo root (K88 `gh api contents/LICENSE`). K36 blocker closed; close upstream issue #64 if still open.
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

**Cursor 2026-09-18:** plugin `finance-data-providers` exposes MCP server `tradingview` (atilaahmettaner pin). Smoke: `yahoo_price(SPY)` and `bitcoin_market_pulse`. **Do not dump these 37 tools into Grok `/route`.**

**OpenCLI 2026-09-18:** `opencli plugin install github:himself65/finance-skills/hyperliquid` → `hyperliquid @0.1.0`. Smoke: `opencli hyperliquid markets --limit 3` (BTC/ETH/ZEC marks) and `funding-compare --coin BTC`. Public HL `/info` — no key. **Skip `finance-skills/tradingview` OpenCLI plugin** until TradingView Desktop exists and the operator accepts a logged-in (often paid) TV account.

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
- **Generative UI hang:** Cursor `tradingview` MCP (2026-09-18 smoke) returned quotes with no HTML widgets. Do not enable finance-skills Generative UI plugins on Grok `/route` or dsh.
- **License verification**: confirm MIT before extracting

[Source: Evaluating Code for Trading Stacks.docx, URL 15]
