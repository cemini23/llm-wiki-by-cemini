---
title: Cemini Financial Suite (deploy monorepo)
type: project
status: active
date: 2026-06-01
updated: 2026-06-01
tags: [project, architecture, cemini-suite, prod]
keywords: [Cemini-Financial-Suite, /opt/cemini, cemini-prod, docker-compose]
local-path: /Users/claudiobarone/Desktop/projects/CeminiSuite
github: cemini23/Cemini-Financial-Suite
deploy-path: /opt/cemini
ai-first: true
related:
  - projects/cemini-financial-suite/Architecture/Architecture - Index.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/OPEN-GAPS.md
  - projects/cemini-financial-suite/Architecture/Architecture - Docker services.md
  - projects/cemini-financial-suite/Architecture/Architecture - Kalshi by Cemini.md
  - projects/cemini-financial-suite/Architecture/Architecture - Key decisions.md
  - projects/cemini-financial-suite/Architecture/Architecture - Polymarket.md
  - projects/cemini-financial-suite/Architecture/Architecture - QuantOS.md
  - projects/cemini-financial-suite/Architecture/Architecture - agents.md
  - projects/cemini-financial-suite/Architecture/Architecture - cemini_contracts.md
  - projects/cemini-financial-suite/Architecture/Architecture - cemini_mcp.md
  - projects/cemini-financial-suite/Architecture/Architecture - core.md
  - projects/cemini-financial-suite/Architecture/Architecture - data plane.md
  - projects/cemini-financial-suite/Architecture/Architecture - db ERD.md
  - projects/cemini-financial-suite/Architecture/Architecture - db.md
  - projects/cemini-financial-suite/Architecture/Architecture - debate and conductor.md
  - projects/cemini-financial-suite/Architecture/Architecture - deploy-systemd.md
  - projects/cemini-financial-suite/Architecture/Architecture - ems.md
  - projects/cemini-financial-suite/Architecture/Architecture - logit_pricing.md
  - projects/cemini-financial-suite/Architecture/Architecture - prod-snapshot-2026-06-01.md
  - projects/cemini-financial-suite/Architecture/Architecture - services.md
  - projects/cemini-financial-suite/Architecture/Architecture - shared and intelligence.md
  - projects/cemini-financial-suite/Architecture/Architecture - strategies.md
  - projects/cemini-financial-suite/Architecture/Architecture - tools.md
  - projects/cemini-financial-suite/Architecture/Architecture - trading_playbook.md
  - projects/cemini-financial-suite/Architecture/Architecture - ui.md
  - projects/cemini-financial-suite/Architecture/tool-adopt-matrix.generated.md
  - projects/osint-workspace/OSINT Workspace.md
  - concepts/cemini-repository-topology.md
  - entities/infrastructure/cemini-stack.md
  - concepts/librarian-server-architecture.md
  - concepts/laptop-prod-research-split.md
  - projects/world-cup-bot/World Cup Bot.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Architecture/Architecture - Index.md — MOC (26 pages @ wave 4)
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md — prod stack @ **`8faf94f`**
- @projects/cemini-financial-suite/Architecture/Architecture - prod-snapshot-2026-06-01.md — live compose ps snapshot (ephemeral)
- @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md — remaining deferred items (runtime snapshot, CI, …)
- @projects/osint-workspace/OSINT Workspace.md — research wiki federation
- @projects/world-cup-bot/World Cup Bot.md — related OSS bot (separate repo)

## For future Claude

Deploy monorepo on **`cemini-prod:/opt/cemini`**. Architecture @ **`8faf94f`** (wave 5): **prod runtime snapshot**, handoff CI, `@generated` patch scripts, Deephaven in data plane. Start at Index; remaining gaps in OPEN-GAPS.md (EMS down, octotools cached, gates).

## Recent activity

- **2026-06-01** — Wave 5 resync @ `8faf94f` (`prod-snapshot-2026-06-01.md`, narrowed OPEN-GAPS).
- **2026-06-01** — Wave 4 @ `e8fd49f`.
