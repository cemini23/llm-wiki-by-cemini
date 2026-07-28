---
title: "Outlier Weekly — Discord Only Fires When the Newsletter Level Is Real"
type: source
tags: [source, outlier-weekly, guruwatcher, discord, macro-charts, k200]
keywords: [GuruWatcher, claim ledger, most-recent-wins, sustain, Macro Charts, Discord webhook]
related:
  - concepts/guruwatcher-newsletter-claim-ledger.md
  - concepts/macro-charts-regime-signals.md
  - concepts/active-project-research-routing.md
  - entities/tools/guruwatcher.md
  - sources/macro-charts-paid-forward-2026-07-28-korea-wti-fomc.md
maturity: draft
read_status: read
created: 2026-07-28
updated: 2026-07-28
clusters: [k200-ingest]
---

## Relations

- @concepts/guruwatcher-newsletter-claim-ledger.md
- @concepts/macro-charts-regime-signals.md
- @concepts/active-project-research-routing.md
- @entities/tools/guruwatcher.md
- @sources/macro-charts-paid-forward-2026-07-28-korea-wti-fomc.md — same-day Macro Charts levels to arm

## Raw Concept

| Field | Value |
|-------|-------|
| **URL** | https://outlierweekly.substack.com/p/discord-only-fires-when-the-newsletter |
| **Published** | 2026-07-28 |
| **Filename** | `substack-rss-outlier-weekly-2026-07-28-discord-only-fires-when-the-newsletter-level-is.md` |
| **sha256** | `44b566fa1060f9e3e00a356d627bcf6d56eb4eb5db850ea7a7edbbdde232409d` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-outlier-weekly-2026-07-28-discord-only-fires-when-the-newsletter-level-is.md` |

## Narrative

Operator Outlier Weekly public write-up of **GuruWatcher**: alert-only Discord parameter watches from newsletter prose (Macro Charts). Reframe: not “summarize and trade” — extract **stated levels**, keep a **claim ledger**, Discord buzzer only. **No orders.** Private repo; steal the pattern.

Four pieces: (1) inbox forward → durable markdown drop; (2) claim ledger with **most-recent-wins** per symbol (manual watches never auto-touched; prod owns armed state); (3) verbatim guards (regex ∪ DeepSeek; span/level/instrument/op/band/history/negation/year-truncation checks); (4) Discord + 15-min poll (UW OHLC / yfinance fallback; dedicated webhook; fail closed).

Sustain default: **2 checks ≈ 30 min**. Soft lists without numbers and chart-only levels stay unarmed. Audit scars: index/ETF scale mismatch, re-arm spam loops, wrong Discord room. Weekend dumb-loop recipe included.

**Cross-wiki note:** RSS stub tagged gambling-wiki — **wrong**. This is GuruWatcher (#2), not PM/sports wagering.

## Snippets

> "You are not building a guru. You are building a claim ledger with a Discord buzzer."

> "Newest article wins on conflict… SOX from Monday keeps living until a later letter updates it"

> "If the number is not in this issue’s text, it does not arm."
