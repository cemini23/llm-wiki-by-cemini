---
title: wc-ticket-monitor (FIFA WC26 knockout ticket alerts)
type: entity
tags: [tool, world-cup-2026, tickets, resale, discord, open-source, cemini23]
keywords: [wc-ticket-monitor, fifa-resale, stubhub, ticketwave, great-reviewer, price-floor, knockout]
related:
  - entities/tools/world-cup-bot.md
  - concepts/active-project-research-routing.md
  - meta/daily-research-digest-cadence.md
  - "@gambling-wiki/concepts/world-cup-pm-retail-hygiene.md"
maturity: validated
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @entities/tools/world-cup-bot.md — PM/Kalshi advance-market bot (different surface: event contracts, not physical tickets)
- @concepts/active-project-research-routing.md — morning digest + brief routing
- @meta/daily-research-digest-cadence.md — daily Exa digest cadence
- @gambling-wiki/concepts/world-cup-pm-retail-hygiene.md — wagering cross-ref only

## Raw Concept

Portfolio repo added 2026-06-20. Hourly Discord alerts when FIFA World Cup 2026 **knockout** resale listings drop under configurable per-round price floors.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [github.com/cemini23/wc-ticket-monitor](https://github.com/cemini23/wc-ticket-monitor) |
| **Local path** | `~/Desktop/projects/wc-ticket-monitor` |
| **Brief home** | `../projects/wc-ticket-monitor/briefs/` |
| **License** | MIT |
| **Sources** | The Great Reviewer (FIFA official API), TicketWave (Viagogo/Ticombo/LFT/FootballTicketNet); optional StubHub (Playwright, off by default) |
| **Scope** | 30 knockout matches (R32–SF); R16+ floors default $1,250–$1,700 |

### Ingest routing

- **Secondary tier** — route briefs when source is physical-ticket resale (not co-primary morning digest)
- Secondary-market scraping, floor calibration, alert dedupe → **this entity + code briefs**
- PM/Kalshi WC advance markets, LP conviction → `@entities/tools/world-cup-bot.md`
- Sportsbook WC wagering retail hygiene → `@gambling-wiki`

### Research steal-from (morning digest)

- FIFA official resale policy + API stability
- Secondary aggregator price dynamics by knockout round
- Outlier/median floor tuning from historical TicketWave medians
- Degraded-source observability patterns (Discord digest + cooldown dedupe)
