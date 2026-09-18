---
title: "GuruWatcher"
type: entity
tags: [tool, guruwatcher, discord, alert-only, k200]
keywords: [GuruWatcher, claim ledger, Discord, Macro Charts]
related:
  - entities/tools/weathernext.md
  - entities/tools/flights-rpc.md
  - concepts/guruwatcher-newsletter-claim-ledger.md
  - sources/substack-rss-outlier-weekly-2026-07-28-guruwatcher-discord.md
  - concepts/active-project-research-routing.md
  - concepts/macro-charts-regime-signals.md
  - sources/macro-charts-paid-forward-2026-07-28-korea-wti-fomc.md
  - sources/macro-charts-paid-forward-2026-07-29-kospi-sox-fomc.md
  - entities/infrastructure/cemini-egress-fi.md
maturity: draft
created: 2026-07-28
updated: 2026-09-18
---

## Relations
- @entities/tools/weathernext.md — K230
- @entities/tools/flights-rpc.md — K229

- @concepts/guruwatcher-newsletter-claim-ledger.md
- @sources/substack-rss-outlier-weekly-2026-07-28-guruwatcher-discord.md
- @concepts/active-project-research-routing.md
- @concepts/macro-charts-regime-signals.md
- @sources/macro-charts-paid-forward-2026-07-28-korea-wti-fomc.md — watch candidates
- @sources/macro-charts-paid-forward-2026-07-29-kospi-sox-fomc.md — day-2 reconcile
- @entities/infrastructure/cemini-egress-fi.md — runtime 2026-09-18 (`/opt/guru-watcher`, 15-min timer)


## Raw Concept

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/cemini23/GuruWatcher (private) |
| **Local** | `~/Projects/GuruWatcher` |
| **Runtime** | `cemini-egress-fi:/opt/guru-watcher/` — systemd timer every 15 min (2026-09-18). Former Ashburn `/opt/guru-watcher` deleted with prod. |
| **Briefs** | `../GuruWatcher/briefs/` |
| **Boundary** | Alert-only — not CeminiSuite order path |

## Narrative

Private alert bot: newsletter claim extract → Discord. Public methodology in Outlier Weekly 2026-07-28. Do not confuse with TipDrop scanner Discord or World Cup Bot OSS cousin.
