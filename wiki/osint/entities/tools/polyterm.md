---
title: "PolyTerm — terminal-native, zero-custody Polymarket analytics"
type: entity
tags: [tool, prediction-markets, polymarket, terminal-ui, analytics, zero-custody, adopt, k49]
keywords: [polyterm, terminal-native, polymarket-analytics, zero-custody, view-only, sqlite, websocket, ascii-charts, arbitrage-scanner, whale-tracking, mit-license]
related:
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
  - entities/tools/pmxt.md
  - entities/tools/polymarket-insider-tracker.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
phase_0_verdict: ADOPT (doc-level) 2026-05-16 — MIT verified in report; Phase-0 clone audit pending before cemini-prod integration
---

## Relations

- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — evaluated in the v3-iteration eval (Adopt tier, Cemini-financial primary fit)
- @entities/tools/pmxt.md — sibling Polymarket tooling; pmxt is execution-abstraction, PolyTerm is analytics/journaling
- @entities/tools/polymarket-insider-tracker.md — sibling surveillance tooling; PolyTerm does whale-tracking from order flow, the Insider Tracker does it from on-chain forensics
- @ccc-wiki/entities/tools/polyterm-tui-pattern.md — cross-wiki stub: ASCII depth-chart + TUI navigation as a Claude Code tool-UI template

## Raw Concept

Promoted from the 2026-05-16 "Tool Evaluation and Wiki Fit v3 Iteration" 46-repo eval. Tier: **Adopt**. Primary fit: Cemini-financial. Cross-route: CCC-wiki (terminal-UI patterns).

- URL: https://github.com/NYTEMODEONLY/polyterm
- License: **MIT** (per report)
- Stars / last commit / open issues: 256 / 2026-04-28 / 1
- Stack: Python / SQLite / WebSockets

## Narrative

**PolyTerm** is a terminal-native analytics and intelligence layer for Polymarket, built around **deep situational awareness and zero-custody security**. It runs entirely from the command line: a local SQLite database holds trade journals, bookmarks, and market snapshots; WebSockets drive real-time depth displays and ASCII charts. The 73 interactive screens use keyboard navigation shortcuts (e.g. `c15` for crypto markets, `mw`).

Analytics include volume-based **whale tracking**, an internal **Arbitrage Scanner** for intra-market discrepancies (where YES + NO prices sum below $1.00), and multi-factor forecasting (RSI + smart-money positioning + UMA dispute tracking). Its **view-only architecture** means no private keys ever touch the terminal — aligning with institutional opsec.

**Cemini fit**: strategy-backtesting and real-time risk-assessment reference for the `/opt/cemini` stack; the Arbitrage Scanner and forecasting logic are reusable. The TUI/ASCII-chart patterns are a UI template for laptop-side Claude Code tools (cross-routed to CCC). MIT clears the IP sale. Deployment belongs on **cemini-prod** — staged via adoption brief.

- `[NEEDS VERIFICATION 2026-05-16]` WebSocket stability + SQLite write-lock thresholds under extreme-volume events (resolution spikes).
- `[NEEDS VERIFICATION 2026-05-16]` Phase-0 clone audit: confirm MIT LICENSE, dependency license cleanliness.

## Snippets

> "By adopting a view-only architecture, PolyTerm ensures that no private keys ever touch the terminal environment ... an internal Arbitrage Scanner capable of identifying intra-market discrepancies (where YES + NO prices fall below $1.00)." [Source: Tool Evaluation and Wiki Fit Analysis.docx — URL 8]
