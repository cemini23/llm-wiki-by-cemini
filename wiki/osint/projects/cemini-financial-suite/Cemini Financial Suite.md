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
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Key decisions.md
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

- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md — **prod** architecture @ `e3674e4` (handoff 2026-06-01)
- @projects/cemini-financial-suite/Architecture/Architecture - Key decisions.md — commit-mined signals from `/opt/cemini`
- @projects/osint-workspace/OSINT Workspace.md — research wiki + briefs staging (this repo federation)
- @concepts/cemini-repository-topology.md — why deploy monorepo stays separate from `llm-wiki-by-cemini`
- @entities/infrastructure/cemini-stack.md — two-server prod + librarian topology
- @concepts/librarian-server-architecture.md — kb-server, bulk, conductor overlay
- @concepts/laptop-prod-research-split.md — laptop vs prod execution boundary

## For future Claude

Project hub for **`cemini23/Cemini-Financial-Suite`** — runnable trading stack on **`cemini-prod:/opt/cemini`**. Architecture notes under `Architecture/` were generated on prod by server-Claude (`briefs/out/architecture-2026-06-01/`) @ **`e3674e4`** and ingested into this wiki 2026-06-01. **Deployed SHA wins** over laptop clone (`~/Desktop/projects/CeminiSuite`).

## Overview

| Field | Value |
| --- | --- |
| **Role** | Deploy monorepo: brain (LangGraph), EMS, QuantOS, Kalshi, Polymarket/HL compose profiles, `cemini_mcp` |
| **Prod path** | `/opt/cemini` on `cemini-prod` |
| **Laptop clone** | `/Users/claudiobarone/Desktop/projects/CeminiSuite` (may lag prod) |
| **Wiki input** | OSINT briefs → `/opt/cemini/briefs/` only |

## Architecture notes (prod @ e3674e4)

- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - QuantOS.md
- @projects/cemini-financial-suite/Architecture/Architecture - Kalshi by Cemini.md
- @projects/cemini-financial-suite/Architecture/Architecture - core.md
- @projects/cemini-financial-suite/Architecture/Architecture - agents.md
- @projects/cemini-financial-suite/Architecture/Architecture - ems.md
- @projects/cemini-financial-suite/Architecture/Architecture - cemini_mcp.md

## Handoff provenance

- [Source: cemini-prod:/opt/cemini/briefs/out/architecture-2026-06-01/ (retrieved 2026-06-01)]
- [Source: briefs/2026-06-01_cemini-suite-obsidian-architect.md — ship brief]

## Recent activity

- **2026-06-01** — Prod handoff ingested from `architecture-2026-06-01/` @ `e3674e4`.
