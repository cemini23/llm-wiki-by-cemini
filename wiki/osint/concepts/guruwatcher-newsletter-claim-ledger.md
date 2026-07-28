---
title: GuruWatcher — newsletter claim ledger → Discord (alert-only)
type: concept
tags: [concept, guruwatcher, discord, macro, k200, core-candidate]
keywords: [claim ledger, most-recent-wins, sustain, verbatim guards, Macro Charts]
related:
  - sources/substack-rss-outlier-weekly-2026-07-28-guruwatcher-discord.md
  - entities/tools/guruwatcher.md
  - concepts/macro-charts-regime-signals.md
  - concepts/active-project-research-routing.md
  - sources/macro-charts-paid-forward-2026-07-28-korea-wti-fomc.md
maturity: draft
created: 2026-07-28
updated: 2026-07-28
---

## Relations

- @sources/substack-rss-outlier-weekly-2026-07-28-guruwatcher-discord.md — public methodology post
- @entities/tools/guruwatcher.md
- @concepts/macro-charts-regime-signals.md — levels come from regime letters
- @concepts/active-project-research-routing.md — Priority #2 brief home
- @sources/macro-charts-paid-forward-2026-07-28-korea-wti-fomc.md

## Raw Concept

How do paid regime newsletters become reliable Discord level alerts without becoming an order bot?

## Narrative

**GuruWatcher** (Priority #2) turns newsletter **stated numbers** into armed watches:

| Rule | Meaning |
|------|---------|
| Alert-only | Discord webhook; never orders / CeminiSuite executor |
| Claim ledger | `(symbol, op, level, verbatim, published_at)` |
| Most-recent-wins | New issue updates mentioned symbols only; others persist |
| Verbatim guards | Snippet must appear; level in snippet; instrument near level; band sanity; reject year-truncation (`2026` ≠ VIX 20) |
| Soft lists / chart-only | Unarmed — no invented numbers |
| Sustain | Default 2×15min polls ≈ 30 min before fire |
| Prod owns state | Laptop extract → sync **claims**; do not wholesale replace watches.json |

Ops: dedicated Discord webhook; fail closed if missing; UW OHLC + yfinance fallback. Code: `~/Projects/GuruWatcher` · inbox hook `scripts/guru_watcher_inbox_hook.sh` · OSINT `scripts/macro_charts_watch.py` cousin.
