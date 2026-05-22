---
title: "Clawdbot — Claude-powered AI agent framework for Polymarket weather bots"
type: entity
tags: [entity, tool, polymarket, claude-bot-framework, weather-trading, automation, k55]
keywords: [clawdbot, claude-bot-framework, coldmath, polymarket-weather-trader-1, pilot-aviation-reports, 24-7-bot]
related:
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/people/polymarketsuccubus.md
  - entities/people/polydao-mr-buzzoni.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-20
updated: 2026-05-22
---

## Relations

- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — K55 Posts.docx Post 5 references Clawdbot as the framework underpinning ColdMath (#1 weather trader, +$124K PnL)
- @concepts/polymarket-weather-trading-strategy.md — concept page where Clawdbot is now cross-referenced
- @entities/people/polymarketsuccubus.md — referencing creator
- @entities/people/polydao-mr-buzzoni.md — K57 weather post watchlist cites ColdMath stack

## Raw Concept

K55 ingest surfaces Clawdbot as "a Claude-powered AI agent framework" used by ColdMath, the #1-ranked weather-market trader on Polymarket per the @polysuccubus Top-7 ranking. The framework is mentioned but not deep-described in the source post; this page records what is known and flags follow-up Phase-0.

## Narrative

### Source attribution (from K55 Posts.docx Post 5)

> "[ColdMath] doesn't trade manually. Instead, he runs a highly sophisticated automated trading bot built on Clawdbot (a Claude-powered AI agent framework). ColdMath himself developed and refined this bot, which scans real-time weather data from multiple sources (including pilot aviation reports), compares it against market prices 24/7, and executes trades with machine-like precision."

### Reported usage

| Operator | Framework | Strategy | Result (per Parity/@polysuccubus) |
|---|---|---|---|
| ColdMath | Clawdbot | Real-time weather data → pilot aviation reports → market-price comparison → small-entry-large-payout trades | +$124,896 PnL, 81.7% WR, 6,575 predictions, biggest single win $12,400 |

### Open questions [NEEDS VERIFICATION 2026-05-20]

1. **Public or proprietary?** Is Clawdbot a public open-source framework, a closed-source product, or a custom internal framework that ColdMath self-named? The @polysuccubus post describes it but does not link to a repo or product page.
2. **License?** If public, what license — MIT? Apache? Closed?
3. **Architecture?** "Claude-powered AI agent framework" is broad — does it use MCP? Is it Claude-API-direct? Does it wrap Claude Code?
4. **Adoption surface?** If openly licensed, it's a candidate for Phase-0 audit; if proprietary, it's reference-only.

### Cemini-relevant signal

Whether or not Clawdbot is adoptable, the **datapoint that a Claude-driven bot framework was the #1 performer** in a competitive Polymarket vertical is meaningful. It validates that LLM-orchestrated trading agents in narrow domains (with clean data feeds + price-comparison logic + small-entry-large-payout discipline) can outperform manual operators by a significant margin. The 81.7% WR + 6,575-trade volume is exceptional regardless of framework name.

### Cemini fit

- **Deferred** pending verification of Clawdbot's existence as a public artifact (1) and its license (2).
- If it turns out to be open + permissively licensed, this becomes an Adopt-candidate to evaluate against Hermes Agent (already in wiki, K52) and against the Cemini conductor architecture.
- If it turns out to be proprietary or a custom internal framework, this page stays Reference-only and the surfacing of the *strategy class* (Claude-driven weather-market bot) is the actual takeaway.

### Follow-up action

Web search for "Clawdbot Claude framework" or "ColdMath Clawdbot Polymarket" to find the canonical artifact (GitHub repo, product page, or absent both, a tweet thread). Defer to next session.
