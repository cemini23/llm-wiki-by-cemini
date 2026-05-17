---
title: "kukapay/dune-analytics-mcp — Dune Analytics MCP Server (Python, MIT)"
type: source
tags: [github, mcp-server, on-chain-analytics, dune-analytics, blockchain-data, python, mit-license, cemini-adopt-candidate, ip-sale-clean, gemini-dr-wave4, small-project-bus-factor]
keywords: [dune-analytics-mcp, kukapay, dune-analytics, on-chain-data, mcp-server, blockchain-analytics, defi-metrics, smart-contract-events, wallet-flows, ethereum-analytics, cemini-crypto-pipeline, fork-and-maintain-pattern]
clusters: [crypto, infrastructure, llm-agents]
related:
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - concepts/crypto-asset-taxonomy.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
read_status: read-skim
created: 2026-04-29
updated: 2026-05-17
---

## Relations

- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A canonical brief; URL 18 Adopt; promoted to dedicated source this session as Cemini's primary on-chain analytics MCP candidate
- @concepts/ip-sale-readiness.md — MIT license clean
- @concepts/high-signal-paper-patterns.md — rubric: 40 stars / 11 forks / 2 contributors = small-project bus-factor caveat (rubric's "single-author + extraordinary claims" pattern is adjacent; not exactly that, but the upstream-maintenance-risk applies)
- @concepts/crypto-asset-taxonomy.md — Cemini's crypto pipeline currently consults Coinbase + Polygon for OHLC/trades; Dune adds the **on-chain analytics layer** (smart contract events, wallet flows, DeFi metrics) — a complementary data axis
- @sources/caiovicentino-polymarket-mcp-server.md — Wave 5B sibling Adopt; another MIT Python MCP server bridging an external data/trading API to LLM agents. Same architectural family (FastMCP-compatible Python wrapper, fork-and-pin maintenance pattern, single-contributor bus-factor caveat) — different data domain (Polymarket trade-execution + odds vs Dune SQL queries). Pattern: kukapay-style MCP adapters dominate the Cemini-stack data-access surface

## Raw Concept

- **URL**: https://github.com/kukapay/dune-analytics-mcp
- **Type**: Open-source MCP server
- **License**: MIT (Exa-verified 2026-04-29 against both `main` and `master` branch LICENSE files; Copyright 2025 kukapay)
- **Stars / Forks (Exa-verified 2026-04-29)**: 40 ★ / 11 forks
- **Stack**: Python 86.8% / Dockerfile 13.2%
- **Org**: kukapay (solo author + calclavia as second contributor)
- **Created**: 2025-03-16; **Last push**: 2025-05-04 (~12 months stale at evaluation time)
- **Required deps**: Python 3.10+, Dune Analytics API key
- **Discovered via**: Gemini DR Wave 4A 2026-04-29 (URL 18); promoted to dedicated source page same session

## Narrative

### What it is

A Python MCP server that **bridges Dune Analytics data to AI agents**. Dune Analytics is a leading on-chain data platform (Ethereum + 30+ chains) where analysts write SQL queries against indexed blockchain data and produce dashboards. Dune's API exposes those queries + dashboards programmatically; this MCP wraps the API as MCP tools for LLM agent consumption.

Practical effect: a DeepSeek-V4-flash analyst node can issue `dune_query(...)` MCP tool calls during reasoning to fetch live on-chain metrics — wallet flows, DEX volume, NFT mint activity, validator behavior, etc. — without writing SQL.

### Why Cemini-direct

Cemini's existing crypto data layer:
- **Coinbase** — OHLC + trades + order book for major spot pairs
- **Polygon** — equity options chains + crypto OHLC
- **CCXT** — multi-exchange aggregation

What's missing: **on-chain analytics**. Cemini currently can't see wallet behavior, smart contract events, DeFi protocol metrics, or stablecoin flows. Dune fills exactly this gap.

Concrete deployment surface for Cemini: 
- **`agents/orchestrator.py`** registers the Dune MCP server alongside the existing MCP tools
- **DeepSeek analyst nodes** can call `dune_query("...")` when ticker research touches on-chain context (e.g., assessing a stablecoin de-peg risk requires looking at on-chain reserve composition, not OHLC)
- **Crypto-pair watchlist analysts** (BTC/ETH/SOL/AVAX/LINK/ADA/DOGE etc.) gain a complementary on-chain lens

### Bus-factor caveat (high-signal-paper-patterns rubric)

Per `@concepts/high-signal-paper-patterns.md` negative-signals: 
- 40 stars / 11 forks: small project
- 2 contributors (kukapay solo + calclavia): bus-factor risk
- Last push 2025-05-04, ~12 months without updates as of 2026-04-29: maintenance-uncertain
- BUT clean MIT license + Python + functional codebase

**Mitigation pattern: fork-and-maintain-in-house**. Clone the repo, pin a commit hash, accept that upstream may go stale. Cemini maintains the fork going forward; benefits from the existing implementation work without depending on upstream maintenance. This is a different pattern from "follow upstream" (which works for Microsoft qlib's 40k-star ecosystem) and matches the rubric's small-project deployment guidance.

### Cemini-side adoption assessment

**Decision: Adopt with fork-and-maintain pattern**. Concrete next-steps:

1. **License + dep tree audit** — Exa-verified MIT at `LICENSE` file; transitive Python deps need `pip-audit` + `licensecheck`. ~30 min.
2. **Dune Analytics API key procurement** — paid tier required for production volumes. Cost-estimate vs current Polygon spend. ~15 min.
3. **Fork to a Cemini-controlled repo** + pin commit hash. ~5 min.
4. **Deploy the MCP server on cemini-prod** alongside existing MCP infrastructure. ~half-day.
5. **Wire analyst-orchestrator** to consult `dune_query()` when ticker research touches on-chain context. ~half-day.
6. **Monitor query latency + cost** during first 30 days; adjust analyst-prompts to call sparingly (Dune queries are slow + paid).

### Risks & open questions

1. **Bus-factor** — already covered above. Fork-and-maintain mitigates.
2. **Dune Analytics API pricing** [CONFIRMED 2026-05-17] — Exa-verified against Dune's official pricing + credits-billing docs (dune.com/pricing, docs.dune.com). Dune uses a usage-based **credit** model (credits consumed reflect query compute): **Free** = $0/mo, 2,500 credits/mo, API access included but limited to Small/Medium engine; **Analyst** = $65/mo billed annually (or $75/mo monthly), 4,000 credits/mo, faster engine + higher API rate limits; **Plus** = $349/mo billed annually (or $399/mo), 25,000 credits/mo, largest engine + private queries; **Enterprise** = custom. Extra credits ~$0.014–0.016 each. Metadata endpoints are free; execution endpoints are credit-based. Cemini's expected query volume remains an internal estimate — but the Free tier (2,500 credits, includes API) is enough for low-volume evaluation; production use likely needs Analyst tier.
3. **Query latency** — Dune queries can take seconds-to-minutes for complex ones. Cemini's analyst-orchestrator timeouts may need adjustment.
4. **Schema drift** — Dune's tables periodically schema-shift; queries that work today may break later. Pin against specific table schemas where possible.
5. **MCP Tool surface mismatch** — the kukapay implementation may not expose all the Dune-API tools Cemini wants. Read the actual tool list pre-deployment; may need to extend.

### Citation

> kukapay. (2025). *Dune Analytics MCP Server*. https://github.com/kukapay/dune-analytics-mcp (MIT License; created 2025-03-16, last push 2025-05-04)

## Snippets

> **Project description (from GitHub repo description)**:
>
> "A mcp server that bridges Dune Analytics data to AI agents." [Source: https://github.com/kukapay/dune-analytics-mcp, retrieved 2026-04-29 via Exa]

> **License confirmation**:
>
> "MIT License. Copyright (c) 2025 kukapay. Permission is hereby granted, free of charge, to any person obtaining a copy of this software…" [Source: https://github.com/kukapay/dune-analytics-mcp/blob/main/LICENSE, retrieved 2026-04-29 via Exa]
