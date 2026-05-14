---
title: "atilaahmettaner/tradingview-mcp — TradingView MCP Server"
type: entity
tags: [tool, mcp-server, tradingview, mit, no-go-phase-0-2026-05-13, screener, indicators, github-eval-2026-05-13, tos-blocked]
keywords: [tradingview-mcp, atilaahmettaner, mcp-server, 30-tools, tradingview-screener, technical-analysis-mcp, mit-license, tos-redistribution-blocker, no-go-pending-legal]
related:
  - sources/eval-github-repos-2026-05-13.md
  - entities/tools/bukosabino-ta.md
  - entities/platforms/polymarket.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
maturity: validated
created: 2026-05-13
updated: 2026-05-14
---

## Relations

- @sources/eval-github-repos-2026-05-13.md — K43 source-doc Phase-0 eval (ADOPT verdict at doc-level; superseded by 2026-05-13 source audit below)
- @entities/tools/bukosabino-ta.md — adjacent TA tooling (also NO-GO 2026-05-13 Phase-0); both invalidated by Phase-0 audits
- @entities/platforms/polymarket.md — would-be consumer venue if/when TOS clears
- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md — canonical K43-failure example (TOS gate) powering the two-gate pattern formalization

**Brief references (informational; not `related:` per wiki schema)**:
- `briefs/2026-05-10_tradingview-mcp-adoption.md` — prior adoption brief on cemini-prod (GO conditional on license + IP-ban mitigation); now gated by this 2026-05-13 audit's TOS-redistribution finding
- `briefs/2026-05-11_tradingview-mcp-phase0-spike.md` — prior phase-0 spike on cemini-prod; this audit reinforces TOS gate

## Raw Concept

What prompted this page: Phase-0 eval verdict (May 13 2026) flagged atilaahmettaner/tradingview-mcp as ADOPT-tier. MIT-licensed, 30+ MCP tools exposing TradingView screener / indicator / chart APIs. Direct fit for Cemini's MCP-server-tooling pattern.

## Narrative

### Identity

- **Repo**: `atilaahmettaner/tradingview-mcp` (GitHub)
- **License**: **MIT**
- **Tool count**: 30+ MCP tools
- **Surface**: TradingView screener, indicator queries, chart-data retrieval

### Adoption posture

**NO-GO 2026-05-13** pending TradingView TOS legal review. See `## Phase-0 audit verdict` below. Source-doc-level K43 ADOPT verdict was license + tool-count filter only; the Phase-0 source audit caught the TOS redistribution gate.

### Phase-0 audit verdict (2026-05-13)

| Dimension | Finding | Status |
|-----------|---------|--------|
| License (own repo) | MIT verified (LICENSE + pyproject.toml; Copyright 2025 Ahmet Taner Atila) | PASS |
| Maturity (stars / age / contributors / version) | 2,642 / 9 months / 12 / v0.7.1 stable | PASS |
| Last commit | 2026-05-13T18:37:20Z (active development, today) | PASS |
| MCP tool count | 30 claimed → 30 verified (exact match) | PASS |
| Data-source mechanism | Official TradingView Python libs (`tradingview-screener>=0.6.4` + `tradingview-ta>=3.3.0`); not scraping the website directly | PARTIAL |
| **Dependency-library license + TOS** | `tradingview-screener` + `tradingview-ta` licenses + TradingView ToU **NOT audited in this Phase-0**; their redistribution stance under an MCP-server wrapper is unknown | **FAIL** |
| **TradingView TOS** for commercial-quant-stack MCP redistribution | No README disclaimer; rotating-proxy support hints upstream IP-ban risk (also flagged by prior `@briefs/2026-05-10_tradingview-mcp-adoption.md`) | **FAIL** |
| Intraday auth (1m/5m) | May require authenticated TradingView session cookies; not clearly documented | UNKNOWN |

**Verdict: NO-GO pending legal review of TradingView ToU.**

This audit supersedes the doc-level ADOPT verdict in the K43 source page (`@sources/eval-github-repos-2026-05-13.md`) and gates the existing `@briefs/2026-05-10_tradingview-mcp-adoption.md` (GO-conditional) on cemini-prod. Do not proceed with Docker deployment or Conductor wiring until TOS redistribution rights are confirmed in writing.

### Phase-0 gates that must clear before reconsidering

1. **Audit `tradingview-screener` + `tradingview-ta` licenses + their TradingView-relationship status** (are these official, sanctioned community projects, or reverse-engineered)
2. **Review TradingView's ToU** on API/library redistribution for commercial use
3. **Determine MCP-wrapper classification** under TradingView TOS — is it "API consumer" (likely allowed) or "re-distributor" (likely not)
4. **Contact TradingView legal** if §1-§3 are ambiguous
5. **Rate-limit + IP-ban tolerance budget** documented before any production wiring
6. **Intraday auth-cookie handling** documented if Cemini will consume 1m/5m timeframes

### Cemini integration target

**None pending TOS clearance.** If §1-§6 clear, the previously planned wiring at `/opt/cemini/conductor/tools.py` would consume the 30 MCP tools for screener / TA / backtesting flows.

### Why MIT matters here

Same posture as bukosabino/ta — MIT keeps Cemini's IP-sale path clean. No license issue from depending on this tool as an MCP server.

### Caveat — TradingView TOS (now the load-bearing gate, not a side caveat)

The MCP tool wraps TradingView's API surface, which is subject to TradingView's own Terms of Service. Even with MIT-licensed wrapper code, Cemini's use of TradingView data is governed by TradingView's TOS. The 2026-05-13 Phase-0 audit elevated this from "caveat" to **blocking NO-GO**. The TOS questions to answer:

- Is MCP-server redistribution of `tradingview-screener` / `tradingview-ta`-derived data considered "API consumer" use or "re-distribution"?
- Does the wrapping change the classification?
- Is commercial use by a private quant stack (non-open-source) allowed under standard TradingView ToU?

Until these are answered in writing, the entity is parked at NO-GO.

## Snippets

> "atilaahmettaner/tradingview-mcp: MIT, 30+ MCP tools. ADOPT." [Source: eval-github-repos-2026-05-13.docx]

## Dead Ends

- **Source-doc ADOPT verdict on its own is insufficient** (2026-05-13 Phase-0) — the K43 doc-level eval was license + tool-count filter; the data-source chain's TOS posture was not part of the doc-level eval. The Phase-0 audit found MIT-clean wrapper but unaudited dependency-library licenses and missing TradingView ToU clearance for MCP redistribution. Lesson: when the wrapped service is a major commercial platform (TradingView, Bloomberg, Refinitiv, S&P), the TOS gate runs ahead of the license gate.
- **Treating TradingView output as primary truth** — TradingView is a UI layer over multiple data vendors; the same indicator can return different values across data feeds. Cross-verify against a primary source for any signal that gates execution.
- **Skipping the TOS check** — wrapper license ≠ data-source TOS. Verify TradingView's commercial-use position before depending on the tool for executable signals.
