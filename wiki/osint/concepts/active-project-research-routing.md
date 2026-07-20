---
title: Active project research routing — brief targets vs legacy CeminiSuite
type: concept
tags: [concept, meta, workflow, briefs, k121, k156, genealogy]
keywords: [brief-routing, ceminidfs, wc-ticket-monitor, family-tree, genealogy, poker-arena, xsp-killer, polymarket, kalshi, ingest, daily-digest]
related:
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - meta/daily-research-digest-cadence.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - concepts/game-dev-wiki-federation.md
  - concepts/gambling-wiki-federation.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
  - sources/eval-url-revenue-and-project-analysis-2026-07-20.md
  - entities/tools/fivethirtyeight-data.md
  - "@gambling-wiki/concepts/diy-nfl-dfs-model-architecture.md"
  - "@gambling-wiki/entities/tools/ceminidfs.md"
  - entities/tools/wc-ticket-monitor.md
  - "@gambling-wiki/concepts/poker-hl-analyst-loop.md"
  - concepts/xsp-lane-trading-framework.md
  - concepts/polymarket-bot-architecture.md
  - "@image-gen-wiki/concepts/david-adoption-brief-routing.md"
  - "@ccc-wiki/concepts/deep-research-evaluation-prompt.md"
maturity: core
created: 2026-06-17
updated: 2026-07-20
---

## Relations
- @sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md — K176 GPUOLOGY business DR
- @concepts/gpuology-genealogy-agent-kit.md — product strategy concept

- @meta/daily-research-digest-cadence.md — morning digest config
- @concepts/cemini-wiki-ingest-workflow.md — four-phase pipeline
- @concepts/computational-genealogy-archival-automation.md — K153 family-tree methodology
- @concepts/italian-regional-genealogy-archive-playbook.md — K154 regional archive playbook
- @concepts/game-dev-wiki-federation.md — castle-sim legacy wiki sibling
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — Poker Arena fix loop
- @concepts/xsp-lane-trading-framework.md — XSP killer lanes A–D
- @concepts/devfun-poker-agent-challenge-2026.md — researcher track pivot (K122)
- @ccc-wiki/concepts/deep-research-evaluation-prompt.md — bulk URL eval v10 (revenue-first; `genealogy overlap`)
- @sources/eval-url-revenue-and-project-analysis-2026-07-20.md — K175 family-tree + CeminiDFS extracts
- @entities/tools/fivethirtyeight-data.md — K175 CeminiDFS Extract

## Raw Concept

Operator pivot (2026-06-17): research discovery and ingest briefs should serve **active hobby bots**, not automatic prod handoffs to legacy CeminiSuite stacks (MAPPO equity, Riskfolio ladder, conductor harness KPIs).

**Portfolio add (2026-06-20):** **CeminiDFS** joins co-primary digest routing. **XSP killer** promoted to co-primary (2026-06-21). **wc-ticket-monitor** demoted to secondary.

**Genealogy pivot (2026-07-10, K156):** **family-tree / computational genealogy** replaces **castle-sim** as co-primary #4. Private research on `~/Desktop/family/research/`; wiki holds methodology only (K153/K154). **castle-sim** → legacy deprioritized.

## Narrative

### Co-primary projects (equal ingest priority)

| Project | Code / brief home | Prod `scp`? |
|---------|-------------------|-------------|
| **Poker Arena** | `agents/devfun-poker-arena/briefs/` | No — deploy via `cemini_hl_loop.sh` / rsync |
| **CeminiDFS** | `../projects/CeminiDFS/briefs/` + `@gambling-wiki` | No — laptop pipeline repo |
| **XSP killer bot** | `briefs/xsp-*` → `cemini-prod:/opt/cemini/briefs/` | Yes — Lane A/B monitors only |
| **Family-tree / genealogy** | `~/Desktop/family/research/` (private) + `@osint-wiki` K153/K154 | No — never scp; no pedigree names on wiki |

### Secondary (route when source matches)

| Project | Code / brief home | Prod `scp`? |
|---------|-------------------|-------------|
| **wc-ticket-monitor** | `../projects/wc-ticket-monitor/briefs/` | No — Discord alert cron |
| **PM / Kalshi bot** | `briefs/pm-*` → prod when bot-touching | Yes — exploratory retail bot |
| **David persona image-gen** | `briefs/` (image-gen) → mirror `../projects/tipdrop-workspace-kit/briefs/*-david.md` | No — shared kit handoff |
| **castle-sim** (legacy) | `../projects/castle-sim/briefs/` + `@game-dev-wiki` | No — deprioritized Jul 2026 |

### Default ingest rule

1. **Wiki always** — source + concept updates in `wiki/` (or cross-wiki route).
2. **Brief only if** steal-from maps to a row above (`scripts/active_project_brief_targets.yaml`).
3. **Prod scp only if** `scp_target` is set for that project **and** `skill_audit.py` PASS.
4. **Family-tree privacy** — methodology stubs on wiki; private pedigree/DNA/living names stay in `~/Desktop/family/` only.
5. **Legacy deprioritized** — generic quant-finance / portfolio RL / conductor eval / castle-sim → **wiki-only** unless ROADMAP reopens.

### Config files

| File | Role |
|------|------|
| `scripts/daily_research_config.yaml` | Exa queries + `active_topics` in daily sweep |
| `scripts/active_project_brief_targets.yaml` | Brief destination + scp gates per project |
| `ROADMAP.md` | Human-readable workstream list (sync on pivot) |
| `@ccc-wiki/prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md` | Bulk URL eval — revenue-first + `genealogy overlap` |

### Cross-wiki

- **Family-tree** deep ingest → OSINT wiki methodology (`computational-genealogy-archival-automation`, regional playbook); private extracts → `Desktop/family/research/`.
- **CeminiDFS** deep ingest → open Gambling wiki folder; OSINT may stub-route methodology via `cross_wiki_route.py`.
- **wc-ticket-monitor** stays OSINT entity + code repo; cross-ref `@entities/tools/world-cup-bot.md` for PM bot boundary.
- **castle-sim** (legacy) → Game Dev wiki when Godot/RTS source explicitly matches; not co-primary default.
- **Poker** session intel stays in `agents/devfun-poker-arena/`; wiki holds methodology (`poker-hl-analyst-loop`).
- **PM/Kalshi** OSINT wiki owns architecture; prod execution still server-Claude boundary.

## Snippets

> "Co-primary ingest targets (equal priority): poker-arena · ceminidfs · xsp-killer · family-tree." [Source: scripts/daily_research_config.yaml brief_routing_note, 2026-07-10]

> "Do NOT default prod scp to cemini-prod for generic quant-finance / MAPPO / Riskfolio papers." [Source: scripts/daily_research_config.yaml brief_routing_note, 2026-06-17]
