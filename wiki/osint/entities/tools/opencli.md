---
title: "OpenCLI — logged-in browser → CLI for agents"
type: entity
tags: [tool, atto, browser-agent, k197, integrate]
keywords: [OpenCLI, jackwener, portal scrape, Antenati]
related:
  - sources/eval-revenue-opportunity-url-analysis-plan-2026-07-27.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/atto-local-first-threat-model.md
  - entities/tools/ego-lite.md
  - concepts/wiki-tooling-evaluation.md
  - sources/eval-revenue-opportunity-url-analysis-2026-07-27.md
  - entities/tools/openclicky.md
  - entities/tools/qiaomu-opencli-skills.md
  - entities/tools/finance-skills.md
  - entities/tools/tradingview-mcp-atilaahmettaner.md
  - sources/tradesdontlie-tradingview-mcp.md
maturity: draft
created: 2026-07-27
updated: 2026-09-18
laptop_install: VERIFIED 2026-09-18 — OpenCLI 1.8.4; plugin `hyperliquid @0.1.0` (finance-skills). `opencli tradingview` not installed (no TradingView.app; login/paid-tier gate).
---

## Relations

- @entities/tools/qiaomu-opencli-skills.md — K197

- @entities/tools/openclicky.md — K197

- @sources/eval-revenue-opportunity-url-analysis-2026-07-27.md — K197

- @sources/eval-revenue-opportunity-url-analysis-plan-2026-07-27.md
- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/atto-local-first-threat-model.md
- @entities/tools/ego-lite.md — complementary authenticated browse (K195)
- @concepts/wiki-tooling-evaluation.md
- @entities/tools/finance-skills.md — OpenCLI Hyperliquid plugin 2026-09-18; TV plugin skipped
- @entities/tools/tradingview-mcp-atilaahmettaner.md — Cursor TV MCP is the free quote path; OpenCLI TV is not
- @sources/tradesdontlie-tradingview-mcp.md — CDP Desktop sibling; also needs TradingView.app

## Raw Concept

Phase-0 K197 Integrate. https://github.com/jackwener/OpenCLI

## Narrative

| Field | Value |
|-------|-------|
| **License** | Apache-2.0 `[CONFIRMED]` |
| **Tier** | Integrate |
| **Fit** | Zero-cost CLI over logged-in browser for Antenati / FamilySearch / comune portals |

**Security:** same session-hijack class as ego-lite — isolate profiles; sever egress on family portals; never Barone PII in demos.

### Laptop plugins (2026-09-18)

| Plugin | Verdict | Evidence |
|---|---|---|
| `github:himself65/finance-skills/hyperliquid` | **GO** | Public `/info` API. Smoke: BTC mark 78028, ETH 2507.5, ZEC 1458.9. `funding-compare --coin BTC`: HL APR 10.95 vs Binance 4.52. No key. |
| `github:himself65/finance-skills/tradingview` | **SKIP** | Requires `TradingView.app` + logged-in session. This Mac has no Desktop app. Options often need a paid TV tier. Operator: no paid TV account. |

Do not confuse OpenCLI `tradingview` with Cursor MCP `plugin-finance-data-providers-tradingview` (Yahoo/screener; no Desktop). Do not wire either into `/opt/cemini`.
