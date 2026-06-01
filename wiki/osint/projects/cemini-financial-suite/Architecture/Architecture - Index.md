---
title: Architecture — Index (prod MOC)
type: architecture-overview
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, gap-close]
keywords: [Cemini-Financial-Suite, /opt/cemini, de5ad93]
deploy-root: /opt/cemini
scanned-commit: de5ad93
provenance: prod-briefs-out-architecture-2026-06-01-gap-close
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/OPEN-GAPS.md
  - projects/cemini-financial-suite/Architecture/Architecture - Docker services.md
  - projects/cemini-financial-suite/Architecture/Architecture - Kalshi by Cemini.md
  - projects/cemini-financial-suite/Architecture/Architecture - Key decisions.md
  - projects/cemini-financial-suite/Architecture/Architecture - Overview.md
  - projects/cemini-financial-suite/Architecture/Architecture - Polymarket.md
  - projects/cemini-financial-suite/Architecture/Architecture - QuantOS.md
  - projects/cemini-financial-suite/Architecture/Architecture - agents.md
  - projects/cemini-financial-suite/Architecture/Architecture - cemini_contracts.md
  - projects/cemini-financial-suite/Architecture/Architecture - cemini_mcp.md
  - projects/cemini-financial-suite/Architecture/Architecture - core.md
  - projects/cemini-financial-suite/Architecture/Architecture - deploy-systemd.md
  - projects/cemini-financial-suite/Architecture/Architecture - ems.md
  - projects/cemini-financial-suite/Architecture/Architecture - services.md
  - projects/cemini-financial-suite/Architecture/Architecture - trading_playbook.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md — project hub
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md — deferred doc areas
- @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md
- @projects/cemini-financial-suite/Architecture/Architecture - Kalshi by Cemini.md
- @projects/cemini-financial-suite/Architecture/Architecture - Key decisions.md
- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - Polymarket.md
- @projects/cemini-financial-suite/Architecture/Architecture - QuantOS.md
- @projects/cemini-financial-suite/Architecture/Architecture - agents.md
- @projects/cemini-financial-suite/Architecture/Architecture - cemini_contracts.md
- @projects/cemini-financial-suite/Architecture/Architecture - cemini_mcp.md
- @projects/cemini-financial-suite/Architecture/Architecture - core.md
- @projects/cemini-financial-suite/Architecture/Architecture - deploy-systemd.md
- @projects/cemini-financial-suite/Architecture/Architecture - ems.md

## For future Claude

Map of contents (MOC) for prod CeminiSuite architecture handoff @ de5ad93.

# CeminiSuite architecture — index

Map of contents for prod handoff @ `/opt/cemini`. **Open items:** @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md.

## Core engines

- @projects/cemini-financial-suite/Architecture/Architecture - Overview.md
- @projects/cemini-financial-suite/Architecture/Architecture - agents.md — LangGraph brain (`brain` container)
- @projects/cemini-financial-suite/Architecture/Architecture - trading_playbook.md — regime, kill switch, `intel:playbook_snapshot`
- @projects/cemini-financial-suite/Architecture/Architecture - core.md — intel bus, `core/ems` library
- @projects/cemini-financial-suite/Architecture/Architecture - cemini_contracts.md — typed envelopes
- @projects/cemini-financial-suite/Architecture/Architecture - ems.md — `trade_signals` consumer

## Venue & execution

- @projects/cemini-financial-suite/Architecture/Architecture - QuantOS.md
- @projects/cemini-financial-suite/Architecture/Architecture - Kalshi by Cemini.md
- @projects/cemini-financial-suite/Architecture/Architecture - Polymarket.md

## Platform

- @projects/cemini-financial-suite/Architecture/Architecture - services.md — sidecars, analysts, shadow loggers
- @projects/cemini-financial-suite/Architecture/Architecture - cemini_mcp.md
- @projects/cemini-financial-suite/Architecture/Architecture - Docker services.md — compose service catalog
- @projects/cemini-financial-suite/Architecture/Architecture - deploy-systemd.md — host timers (PM, WC, weather)

## Meta

- @projects/cemini-financial-suite/Architecture/Architecture - Key decisions.md
- @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md
- [README](./README.md) — ingest instructions
- [Gap-close brief](../../2026-06-01_architecture-handoff-gap-close.md)
