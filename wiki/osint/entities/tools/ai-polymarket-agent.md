---
title: "ai-polymarket-agent — Polymarket MCP claim (Phase-0 NO-GO)"
type: entity
tags: [entity, tool, polymarket, mcp-server, no-go, license-gap, k55]
keywords: [ai-polymarket-agent, kaktusesquire6rmu, polymarket-mcp, no-license, readme-only, false-positive-adopt, conditionid, search-markets, get-market-odds]
related:
  - sources/multi-wiki-tool-eval-19url-2026-05-20.md
  - entities/tools/polymarket-agents.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - entities/tools/polymarket-clob-api.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/cemini-license-posture.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-20
updated: 2026-05-28
---

## Relations

- @sources/multi-wiki-tool-eval-19url-2026-05-20.md — K55 tool eval URL 5, **Adopt**, primary fit Cemini financial + CCC
- @entities/tools/polymarket-agents.md — Polymarket's OWN official MIT framework; the K55 candidate may build on this
- @sources/caiovicentino-polymarket-mcp-server.md — K30 Wave 5 Adopt MCP-server bridge; overlapping coverage
- @entities/tools/polymarket-clob-api.md — the API surface the MCP wraps
- @concepts/polymarket-bot-architecture.md — bot-side use case
- @concepts/polymarket-lp-rewards-farming.md — LP-bot use case (also wraps order placement)

## Raw Concept

- **URL**: `https://github.com/kaktusesquire6rmu/ai-polymarket-agent`
- **License**: NONE (no LICENSE file, verified 2026-05-28)
- **Stars / last commit / open issues**: ~547 / 2026-05-28 / 0 (GitHub API check 2026-05-28)
- **Stack**: Python / FastAPI / Web3.py / Node.js
- **Tier**: **NO-GO**
- **Primary fit**: Cemini financial (with CCC secondary fit as a MCP-architecture exemplar)
- **K55 verdict**: superseded by source-level Phase-0 audit (README-only scaffold + no license)

## Narrative

Third-party Polymarket MCP server bridging AI agents (Claude / ChatGPT / others) to Polymarket via Model Context Protocol. Per the K55 eval (URL 5): "comprehensive, production-grade developer framework engineered to interface AI agents directly with Polymarket via the Model Context Protocol (MCP) ... clear standard input/output transport mechanisms ... AI utility functions such as `search_markets` and `get_market_odds` using the specific `conditionId` parameters."

### Key surface area (per eval)

- `search_markets` — discovery / filter
- `get_market_odds` — price + orderbook fetch by `conditionId`
- Event-driven structure, FastAPI + Web3.py
- Standard MCP stdio transport (works with Claude Code, Cursor, etc.)
- MIT license — clean for Cemini IP-sale readiness

### Overlap with existing Cemini coverage

Cemini already has:
- @entities/tools/polymarket-agents.md — Polymarket's **own** official MIT-licensed framework
- @sources/caiovicentino-polymarket-mcp-server.md — K30 Wave 5 MCP-bridge Adopt
- @entities/tools/polymarket-python-order-utils.md — order-signing layer
- @entities/tools/polymarket-clob-api.md, polymarket-gamma-api.md, polymarket-websocket-api.md, polymarket-bridge-api.md, polymarket-lb-api.md — six API surface entity pages

`kaktusesquire6rmu/ai-polymarket-agent` is **not** the same as `Polymarket/agents`. It's a third-party builder on top of the official framework. The K55 eval explicitly cites both repos in its "Works cited" (entries 10 and 11) but evaluates only the third-party one.

### Verification needed (pre-Phase-0)

1. **License confirmation via GitHub API** — eval is reliable for MIT verdict per K53/K54 verification pattern, but spot-check anyway.
2. **Compare scope** against `caiovicentino-polymarket-mcp-server` — what does this offer that the existing Adopt doesn't?
3. **Last-commit + open-issues check** — the eval didn't report these fields. Stale repo = lower priority.
4. **Code-quality review** — eval flagged "WebSocket connection stability + failure recovery during high-frequency polling" as a NEEDS VERIFICATION item.

### Cemini fit

- **Adopt-eligible pending Phase-0 audit** to confirm differentiation vs existing MCP bridge.
- **Likely path**: if it has materially better `search_markets` ergonomics or covers Polymarket surfaces (Gamma + CLOB + Data) the existing bridge doesn't, **adopt it as the unified MCP layer** for the Polymarket adapter cluster. If not, defer to existing tools.

### Phase-0 checklist

1. Clone to `/tmp/ai-polymarket-agent-audit/`
2. Verify LICENSE in-file = MIT
3. Verify last-push date + open-issues count from `git log` + `gh issue list`
4. Cross-compare tool surface (`search_markets`, `get_market_odds`, etc.) against `caiovicentino-polymarket-mcp-server` MCP `tools/list`
5. Test against actual Polymarket Gamma + CLOB endpoints on a clean Python venv
6. Decision: Adopt as unified bridge / Adopt as complement / Defer

### Phase-0 audit update (2026-05-28)

- `gh api repos/kaktusesquire6rmu/ai-polymarket-agent` returns `license=NONE` (no LICENSE file).
- Repo currently contains README-only scaffold (no executable server code in tree).
- Eval claim of a production-grade MIT MCP server is **not reproducible from source today**.

**Verdict: NO-GO (2026-05-28)** for adoption until a real licensed codebase appears.

### Status

K55 Adopt claim is superseded by source-level Phase-0 evidence. Keep as reference-only cautionary case.
