---
title: Value Investing Tools (VIT) — MCP + DCF scenario library
type: entity
tags: [entity, tool, valuation, mcp, reject-tier, license-gap, k75]
keywords: [value-investing-tools, vit, zhijingeu, dcf-scenarios, mcp-server, peer-multiples]
related:
  - concepts/equity-fair-value-evaluation.md
  - entities/tools/financetoolkit.md
  - concepts/mcp-tool-marketplace.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/equity-fair-value-evaluation.md — compare Low/Mid/High DCF scenario pattern vs prod weighted synthesis
- @entities/tools/financetoolkit.md — FinanceToolkit is MIT-verified Adopt-tier; VIT is unverified license
- @concepts/mcp-tool-marketplace.md — MCP server surface; evaluate against existing FastMCP stack
- @concepts/cemini-license-posture.md — README MIT claim without LICENSE file

## Raw Concept

K75 Phase-0 (2026-05-28) on `github.com/ZhijingEu/value-investing-tools` — Python library + STDIO MCP server for value-investing workflows (peers, DCF scenarios, implied EV/equity).

## Narrative

- **URL**: https://github.com/ZhijingEu/value-investing-tools
- **License**: README §14 claims **MIT** [TENTATIVE]; **no LICENSE file in repo root**; GitHub API `license.spdx_id` = null [CONFIRMED 2026-05-28]
- **Stars**: 0; last push 2026-03-03
- **Surface**: `ValueInvestingTools.py`, `vit/` package, `server.py` MCP, demo notebook, provider adapters

### Architectural overlap with Cemini

| VIT capability | Cemini prod today |
|----------------|-------------------|
| Low/Mid/High DCF scenarios | Single weighted fair value in `core/equity_valuation.py` |
| Peer multiples → implied price | FMP consensus + forward EPS×P/E |
| MCP tools for Claude | FastMCP + `cemini_mcp` (~130 tools) |
| Charts/CSV export | Redis intel + design/ UI |

Adding VIT as a parallel MCP server duplicates brain-facing valuation unless scoped as **offline research/backtest only**.

### Phase-0 verdict (2026-05-28)

| Gate | Result |
|------|--------|
| G0 Repo | PASS |
| G2 License | **FAIL** — README MIT without LICENSE file (same pattern as LESSONS.md K38 AI-Trader) |
| G3 Fit | PARTIAL — scenario DCF useful; MCP duplication risk |
| G4 Maturity | LOW — 0★ |

**Verdict: REJECT Adopt** until maintainer adds LICENSE file verified via `gh api`. **STEAL-FROM (methodology only)**: three-scenario DCF reporting + peer-implied price table as optional enrichment on `intel:equity_fair_value` payload — implement in prod code, do not install VIT package.

## Snippets

> "This project is licensed under the MIT License - you are free to use, modify, and distribute it, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software." [Source: value-investing-tools README §14 — **not legally binding without LICENSE file**]

## Dead Ends

- **pip install on prod/librarian** — blocked until LICENSE file verified.
