---
title: "pmxt — CCXT for prediction markets (unified middleware)"
type: entity
tags: [tool, prediction-markets, polymarket, kalshi, middleware, mcp, adopt, k49]
keywords: [pmxt, ccxt-for-prediction-markets, unified-api, polymarket, kalshi, limitless, hyperliquid, metaculus, gnosis-safe, eip-712, pmxt-mcp, mit-license]
related:
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
  - entities/tools/polyterm.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
phase_0_verdict: ADOPT (doc-level) 2026-05-16 — MIT verified in report; Phase-0 clone audit pending before cemini-prod integration
---

## Relations

- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — evaluated in the v3-iteration eval (Adopt tier, Cemini-financial primary fit)
- @entities/tools/polyterm.md — sibling Polymarket tooling; PolyTerm is the terminal/analytics layer, pmxt is the execution-abstraction layer
- @concepts/cemini-license-posture.md — MIT clears the IP-sale copyleft perimeter
- @ccc-wiki/entities/mcp-servers/pmxt-mcp-pattern.md — cross-wiki stub: `@pmxt/mcp` exposes prediction-market execution to Claude Code agents

## Raw Concept

Promoted from the 2026-05-16 "Tool Evaluation and Wiki Fit v3 Iteration" 46-repo eval. Tier: **Adopt**. Primary fit: Cemini-financial. Cross-route: CCC-wiki (`@pmxt/mcp`).

- URL: https://github.com/pmxt-dev/pmxt
- License: **MIT** (per report)
- Stars / last commit / open issues: 1700 / 2026-05-15 / 8
- Stack: TypeScript / Python / Node.js

## Narrative

**pmxt** is a unified middleware layer for prediction markets — the **CCXT equivalent** for the prediction-market ecosystem. Prediction markets suffer severe API fragmentation: every platform has its own auth protocol and data schema. pmxt standardizes interactions across **Polymarket, Kalshi, Limitless, Hyperliquid, and Metaculus** into a strict **Event → Market → Outcome** hierarchy with a common Python and TypeScript interface (`create_order`, `fetch_balance`, etc.).

Its key value for the Cemini financial suite: it natively resolves exchange-specific cryptographic auth — **Gnosis Safe signatures** for Polymarket, **EIP-712 signing** for Limitless — eliminating per-platform adapter maintenance. It also ships a `dome-to-pmxt` migration tool for moving off legacy API wrappers, and native `@pmxt/mcp` support so LLM agents can transact on prediction markets directly.

**Cemini fit**: candidate execution-abstraction layer for the `/opt/cemini` trading stack, replacing custom per-venue adapters. The MIT license clears it for the IP sale. Deployment belongs on **cemini-prod**, not the laptop/librarian — staged via adoption brief, not installed from this workspace.

- `[NEEDS VERIFICATION 2026-05-16]` Compatibility of the `dome-to-pmxt` automated migration tool with Cemini's customized Redis Streams data structures.
- `[NEEDS VERIFICATION 2026-05-16]` Phase-0 clone audit: confirm MIT LICENSE file present, no vendored copyleft deps.

## Snippets

> "It standardizes interactions across platforms including Polymarket, Kalshi, Limitless, Hyperliquid, and Metaculus into a strict Event, Market, and Outcome hierarchy ... it natively handles complex, exchange-specific cryptographic requirements, such as Gnosis Safe signatures for Polymarket and EIP-712 signing for Limitless." [Source: Tool Evaluation and Wiki Fit Analysis.docx — URL 4]
