---
title: Active project research routing — brief targets vs legacy CeminiSuite
type: concept
tags: [concept, meta, workflow, briefs, k121]
keywords: [brief-routing, castle-sim, poker-arena, xsp-killer, polymarket, kalshi, ingest, daily-digest]
related:
  - meta/daily-research-digest-cadence.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/game-dev-wiki-federation.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - "@gambling-wiki/concepts/poker-hl-analyst-loop.md"
  - concepts/xsp-lane-trading-framework.md
  - concepts/polymarket-bot-architecture.md
maturity: core
created: 2026-06-17
updated: 2026-06-18
---

## Relations

- @meta/daily-research-digest-cadence.md — morning digest config
- @concepts/cemini-wiki-ingest-workflow.md — four-phase pipeline
- @concepts/game-dev-wiki-federation.md — castle-sim wiki sibling
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — Poker Arena fix loop
- @concepts/xsp-lane-trading-framework.md — XSP killer lanes A–D
- @concepts/devfun-poker-agent-challenge-2026.md — researcher track pivot (K122)
- @sources/devfun-poker-agent-challenge-onepager-2026-06-18.md

## Raw Concept

Operator pivot (2026-06-17): research discovery and ingest briefs should serve **active hobby bots**, not automatic prod handoffs to legacy CeminiSuite stacks (MAPPO equity, Riskfolio ladder, conductor harness KPIs).

## Narrative

### Active projects (priority order)

| Project | Code / brief home | Prod `scp`? |
|---------|-------------------|-------------|
| **castle-sim** | `../projects/castle-sim/briefs/` + `@game-dev-wiki` | No — laptop Godot repo |
| **Poker Arena** | `agents/devfun-poker-arena/briefs/` | No — deploy via `cemini_hl_loop.sh` / rsync |
| **XSP killer bot** | `briefs/xsp-*` → `cemini-prod:/opt/cemini/briefs/` | Yes — Lane A/B monitors only |
| **PM / Kalshi bot** | `briefs/pm-*` → prod when bot-touching | Yes — exploratory retail bot |

### Default ingest rule

1. **Wiki always** — source + concept updates in `wiki/` (or cross-wiki route).
2. **Brief only if** steal-from maps to a row above (`scripts/active_project_brief_targets.yaml`).
3. **Prod scp only if** `scp_target` is set for that project **and** `skill_audit.py` PASS.
4. **Legacy deprioritized** — generic quant-finance / portfolio RL / conductor eval → **wiki-only** unless ROADMAP reopens the stack.

### Config files

| File | Role |
|------|------|
| `scripts/daily_research_config.yaml` | Exa queries + `active_topics` in daily sweep |
| `scripts/active_project_brief_targets.yaml` | Brief destination + scp gates per project |
| `ROADMAP.md` | Human-readable workstream list (sync on pivot) |

### Cross-wiki

- **castle-sim** deep ingest → open Game Dev wiki folder; OSINT may stub-route via `cross_wiki_route.py`.
- **Poker** session intel stays in `agents/devfun-poker-arena/`; wiki holds methodology (`poker-hl-analyst-loop`).
- **PM/Kalshi** OSINT wiki owns architecture; prod execution still server-Claude boundary.

## Snippets

> "Do NOT default prod scp to cemini-prod for generic quant-finance / MAPPO / Riskfolio papers." [Source: scripts/daily_research_config.yaml brief_routing_note, 2026-06-17]
