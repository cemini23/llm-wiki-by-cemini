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
  - projects/cemini-financial-suite/Architecture/Architecture - Key decisions.md
  - projects/cemini-financial-suite/Architecture/Architecture - cemini_contracts.md
  - projects/cemini-financial-suite/Architecture/Architecture - services.md
  - projects/cemini-financial-suite/Architecture/Architecture - trading_playbook.md
  - projects/cemini-financial-suite/Architecture/Architecture - Docker services.md
  - projects/cemini-financial-suite/Architecture/Architecture - Polymarket.md
  - projects/cemini-financial-suite/Architecture/Architecture - deploy-systemd.md
  - projects/cemini-financial-suite/Architecture/Architecture - QuantOS.md
  - projects/cemini-financial-suite/Architecture/Architecture - Kalshi by Cemini.md
  - projects/cemini-financial-suite/Architecture/Architecture - core.md
  - projects/cemini-financial-suite/Architecture/Architecture - agents.md
  - projects/cemini-financial-suite/Architecture/Architecture - ems.md
  - projects/cemini-financial-suite/Architecture/Architecture - cemini_mcp.md
  - projects/osint-workspace/OSINT Workspace.md
  - concepts/cemini-repository-topology.md
  - entities/infrastructure/cemini-stack.md
  - concepts/librarian-server-architecture.md
  - concepts/laptop-prod-research-split.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Architecture/Architecture - Index.md — MOC for all prod architecture notes
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md — prod stack @ **`de5ad93`** (gap-close P0–P2)
- @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md — explicit deferred areas (do not re-audit blindly)
- @projects/osint-workspace/OSINT Workspace.md — research wiki + briefs staging
- @concepts/cemini-repository-topology.md — federation vs deploy monorepo
- @entities/infrastructure/cemini-stack.md — prod + librarian runtime
- @concepts/librarian-server-architecture.md — kb-server, conductor overlay
- @concepts/laptop-prod-research-split.md — laptop vs prod boundary

## For future Claude

Project hub for **`cemini23/Cemini-Financial-Suite`** on **`cemini-prod:/opt/cemini`**. Architecture refreshed **2026-06-01** from prod handoff `briefs/out/architecture-2026-06-01/` @ **`de5ad93`** (P0–P2 gap-close; see @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md). Supersedes initial ingest @ `e3674e4`.

## Overview

| Field | Value |
| --- | --- |
| **Role** | Deploy monorepo: brain, EMS, contracts, playbook, QuantOS, Kalshi, Polymarket, MCP |
| **Prod path** | `/opt/cemini` on `cemini-prod` |
| **Laptop clone** | `/Users/claudiobarone/Desktop/projects/CeminiSuite` (may lag prod) |
| **Wiki input** | OSINT briefs → `/opt/cemini/briefs/` only |

## Architecture (prod @ de5ad93)

Start at @projects/cemini-financial-suite/Architecture/Architecture - Index.md.

## Handoff provenance

- [Source: cemini-prod:/opt/cemini/briefs/out/architecture-2026-06-01/ (retrieved 2026-06-01, @ de5ad93)]
- [Source: briefs/2026-06-01_cemini-suite-obsidian-architect.md]
- [Source: prod OPEN-GAPS.md — P0–P2 closed items listed in-file]

## Recent activity

- **2026-06-01** — Gap-close refresh: +7 pages (contracts, services, playbook, Docker catalog, Polymarket, systemd, Index) + OPEN-GAPS.md @ `de5ad93`.
- **2026-06-01** — Initial handoff ingest @ `e3674e4`.
