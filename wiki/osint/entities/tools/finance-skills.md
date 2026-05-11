---
title: "finance-skills (himself65) — Agent Skills for Financial Analysis"
type: entity
tags: [tool, steal-and-adopt, agent-skills, finance, yfinance, social-intelligence, generative-ui, mit-license]
keywords: [finance-skills, Agent Skills, yfinance, Funda AI, Adanos, Telegram, Twitter, Discord, generative UI, market data]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/declarative-data-labeling-skills.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 15)
- `@concepts/declarative-data-labeling-skills.md` — Agent Skills pattern relevant here

## Raw Concept

TypeScript monorepo implementing the open Agent Skills standard for financial analysis. Plugins query live market data (yfinance, Funda AI), execute sentiment analysis (Adanos API), monitor Telegram/Twitter/Discord social intelligence. Renders interactive Generative UI widgets in compatible chat interfaces.

- **Repo**: `github.com/himself65/finance-skills`
- **License**: MIT [NEEDS VERIFICATION 2026-05-10]
- **Install**: `npx plugins add himself65/finance-skills`
- **Stack**: TypeScript monorepo
- **Warning**: README explicitly tags "educational and informational purposes only"

## Narrative

**Recommendation: Split — Steal-from for Cemini prod, Adopt for workflow laptop.**

### Workflow laptop (Adopt — ✅)

Run the TypeScript tools natively via Claude Code during academic-paper analysis. When evaluating algorithmic market anomalies, Claude can autonomously invoke skills to pull historical stock data (yfinance) and back-verify paper claims without manual scraping scripts. Lightweight Node.js footprint.

### Cemini prod (Steal-from — ⚠️)

Do NOT integrate TypeScript natively into Cemini's Python stack (130 `@mcp.tool` Python decorators). Bridging Node child processes or running a separate MCP server adds operational complexity. Instead:

1. **Extract API endpoint patterns** for Funda AI + Adanos — connection params, payload structures
2. **Reimplement yfinance polling logic** in Python (extraction strategies + SEC filings parsing patterns)
3. **Skip Generative UI rendering** — irrelevant to headless trading stack

### Risks

- **Educational disclaimer**: README explicit "informational only" warning → robust fail-safes/retry mechanisms likely absent. Don't trust extracted code in live-order paths without hardening.
- **API rate limits + commercial licensing**: Adanos + Funda AI likely require commercial keys for sustained quantitative scraping.
- **Generative UI latency [NEEDS VERIFICATION 2026-05-10]**: if invoked accidentally in headless agent calls, may hang attempting to render HTML/CSS.
- **License verification**: confirm MIT before extracting

[Source: Evaluating Code for Trading Stacks.docx, URL 15]
