---
title: "Multi-Wiki Link Evaluation.docx — Discord monitor/alerts batch (2026-06-28)"
type: source
tags: [tool-evaluation, discord, tipdrop, k133]
keywords: [discord-monitor, discord-alerts, self-bot, tipdrop, sp500-form4, gemini-deep-research-v9]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - entities/tools/discord-alerts-trader.md
  - sources/eval-github-batch-unusualwhales-2026-06-28.md
  - sources/eval-repo-plan-tipdrop-legacy-2026-06-28.md
  - sources/eval-github-repos-plan-multi-wiki-2026-06-29.md
maturity: draft
read_status: read
created: 2026-06-28
updated: 2026-06-28
clusters: [agent-harness, wiki-tooling]
---

## Relations

- @entities/tools/discord-alerts-trader.md — Steal-from (signal parsing)
- @sources/eval-github-batch-unusualwhales-2026-06-28.md — sibling UW MCP batch
- @sources/eval-repo-plan-tipdrop-legacy-2026-06-28.md — sibling TipDrop legacy batch

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Multi-Wiki Link Evaluation |
| **Type** | DOCX (Gemini Deep Research RUNTIME v9) |
| **sha256** | `e26f5842d32a5e48bf4d4dcf84cb51ca88382d4a7502fc844b8c218c52f5d98f` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Cemini Multi-Wiki Link Evaluation.docx` |
| **Retrieved** | 2026-06-28 |
| **Read status** | read (tier aggregation; gh spot-check on Adopt/Steal rows) |

## Narrative

K133 batch — **20 URLs** on Discord monitors, DiscordAlerts forks, S&P500 macro alerts. Theme: options-flow ingestion, compliance-first Discord routing, macro S&P intelligence.

### Tier distribution

| Tier | Count | Repos |
|------|-------|-------|
| **Steal-from** | 1 | AdoNunes/DiscordAlertsTrader |
| **Reference-only** | 1 | 0xbuya/sp500discordalerts |
| **Reject** | 1 | Ramzi-Sah/discordMonitorChannel-selfBot (ToS self-bot) |
| **UNAVAILABLE** | 17 | Dead/private DiscordMonitor clones |

### Steal-from — `gh api` spot-check (2026-06-28)

| Repo | Docx | Verified | Posture |
|------|------|----------|---------|
| AdoNunes/DiscordAlertsTrader | Steal-from | **BSD-3-Clause**, 77★, pushed 2026-01-17 | **Steal-from** — `server_formatting.py` BTO/STC/SL/PT parsers; human-in-loop GUI; no user-token injection |

### Rejects aggregated

- **Self-bot (hard reject):** Ramzi-Sah/discordMonitorChannel-selfBot — Discord ToS violation; TipDrop compliance FAIL.
- **17× UNAVAILABLE:** Gemini runtime could not retrieve README/license; no entity stubs (anti-stub-farm).

### Reference-only

- **0xbuya/sp500discordalerts** — Finnhub Form 4 + Wikipedia S&P500 constituent scrape for insider cross-ref; **no verified license** → blueprint only for XSP/TipDrop confluence module.

## Snippets

> Deploying self-bot scripts violates Discord ToS and triggers account termination — rejected for TipDrop. [Source: eval docx URL 12, 2026-06-28]

> DiscordAlertsTrader parses diverse analyst alert formats (BTO, STC, SL, PT) with broker adapters (TDA, eTrade, Webull, IBKR). [Source: eval docx URL 13, 2026-06-28]
