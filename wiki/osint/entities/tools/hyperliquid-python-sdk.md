---
title: hyperliquid-python-sdk — official HL Python client
type: entity
tags: [entity, tool, hyperliquid, perps, xsp, k148]
keywords: [hyperliquid-python-sdk, EIP-712, perps, shadow, xsp-killer]
related:
  - sources/eval-repository-revenue-integration-2026-07-07.md
  - entities/platforms/hyperliquid.md
  - entities/frameworks/ccxt.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/hyperliquid-hlp-vs-user-vaults.md
  - sources/gemini-dr-pm-hl-strategies-2026-07-14.md
  - sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md
maturity: draft
created: 2026-07-07
updated: 2026-07-14
---

## Relations

- @entities/platforms/hyperliquid.md — prod stack already pins SDK in requirements
- @concepts/xsp-lane-trading-framework.md — Lane A timing **shadow** only (not Robinhood executor)
- @concepts/hyperliquid-hlp-vs-user-vaults.md — K165 vault-follow APIs preferred over DIY copy bots
- @sources/gemini-dr-pm-hl-strategies-2026-07-14.md — official SDK as INTEGRATE path
- @sources/gemini-dr-pm-trading-strategies-capital-2026-07-14.md — K165 capital matrix INTEGRATE list

## Raw Concept

K148 Phase-0 on [hyperliquid-dex/hyperliquid-python-sdk](https://github.com/hyperliquid-dex/hyperliquid-python-sdk).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `hyperliquid-dex/hyperliquid-python-sdk` |
| **License** | **MIT** |
| **Stars / pushed** | ~1.7k★; pushed 2026-06-04 |
| **Verdict** | **Integrate** — xsp-killer HL SP500 perp shadow for overnight swing timing |
| **Note** | Already in Cemini `requirements.txt`; K148 brief focuses operator Lane A shadow wiring |

Brief: `briefs/xsp-2026-07-07_hl-sdk-shadow-integrate.md` → cemini-prod scp.

## Snippets

> "Direct, authenticated access to a premier DeFi liquidity venue is a massive capability expansion for any quantitative trading desk." [Source: eval docx — Integrate tier]
