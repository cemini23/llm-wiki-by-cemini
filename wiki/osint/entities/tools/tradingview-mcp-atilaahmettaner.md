---
title: "atilaahmettaner/tradingview-mcp — TradingView MCP Server"
type: entity
tags: [tool, mcp-server, tradingview, mit, adopt-tier, screener, indicators, github-eval-2026-05-13]
keywords: [tradingview-mcp, atilaahmettaner, mcp-server, 30-tools, tradingview-screener, technical-analysis-mcp, mit-license]
related:
  - sources/eval-github-repos-2026-05-13.md
  - entities/tools/bukosabino-ta.md
  - entities/platforms/polymarket.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @sources/eval-github-repos-2026-05-13.md — Phase-0 eval source (ADOPT verdict, May 13 2026)
- @entities/tools/bukosabino-ta.md — adjacent TA tooling; tradingview-mcp covers screener/chart, bukosabino/ta covers indicator math

## Raw Concept

What prompted this page: Phase-0 eval verdict (May 13 2026) flagged atilaahmettaner/tradingview-mcp as ADOPT-tier. MIT-licensed, 30+ MCP tools exposing TradingView screener / indicator / chart APIs. Direct fit for Cemini's MCP-server-tooling pattern.

## Narrative

### Identity

- **Repo**: `atilaahmettaner/tradingview-mcp` (GitHub)
- **License**: **MIT**
- **Tool count**: 30+ MCP tools
- **Surface**: TradingView screener, indicator queries, chart-data retrieval

### Adoption posture

**ADOPT** — drop into Cemini's MCP server registry. Conductor + librarian + chroma already speak MCP; this adds TradingView as a queryable surface.

### Cemini integration target

Wire into the Conductor's MCP-tool dispatch at `/opt/cemini/conductor/tools.py`. Likely consumed by:

- Equity-screening pre-stage (find candidates matching technical criteria)
- Cross-venue arbitrage detection (TradingView TA vs Polymarket implied)
- Newsletter-call validation (when WW references a chart pattern, query TradingView for confirmation)

### Verification before pinning

Per Cemini house policy on MCP-tool adoption:

1. **Maintenance signal**: check last-commit, release cadence, open-issue ratio
2. **Auth model**: confirm any TradingView API key requirement; document credential handling
3. **Rate limits**: TradingView's free tier has limits; document concurrent-request budget
4. **Output schema**: validate the MCP tool outputs are schema-stable across versions (MCP tool drift is a documented failure mode)

### Why MIT matters here

Same posture as bukosabino/ta — MIT keeps Cemini's IP-sale path clean. No license issue from depending on this tool as an MCP server.

### Caveat — TradingView TOS

The MCP tool wraps TradingView's API surface, which is subject to TradingView's own Terms of Service. Even with MIT-licensed wrapper code, Cemini's use of TradingView data is governed by TradingView's TOS — verify commercial-use posture before depending on it for production trading signals.

## Snippets

> "atilaahmettaner/tradingview-mcp: MIT, 30+ MCP tools. ADOPT." [Source: eval-github-repos-2026-05-13.docx]

## Dead Ends

- **Treating TradingView output as primary truth** — TradingView is a UI layer over multiple data vendors; the same indicator can return different values across data feeds. Cross-verify against a primary source for any signal that gates execution.
- **Skipping the TOS check** — wrapper license ≠ data-source TOS. Verify TradingView's commercial-use position before depending on the tool for executable signals.
