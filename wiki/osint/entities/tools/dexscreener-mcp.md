---
title: DexScreener MCP — Claude Desktop DEX research bridge
type: entity
tags: [entity, tool, mcp, dex, defi, crypto-research, k106]
keywords: [dexscreener, mcp-server, claude-desktop, node-js, pre-trade-diligence, no-api-key]
related:
  - sources/trading-posts-compilation-6-2026-06-08.md
  - concepts/hermes-onchain-forensics-pipeline.md
  - "@ccc-wiki/briefs/2026-06-08_k106-ccc-dexscreener-mcp-from-osint.md"
maturity: draft
created: 2026-06-08
updated: 2026-06-08
---

## Relations

- @sources/trading-posts-compilation-6-2026-06-08.md — @AlphaCartell Post 5 (K106)
- @concepts/hermes-onchain-forensics-pipeline.md — K78 Hermes skill bundle also uses DexScreener (different stack: agent runtime + x402)
- @ccc-wiki/briefs/2026-06-08_k106-ccc-dexscreener-mcp-from-osint.md — setup handoff

## Raw Concept

Community **MCP server** exposing DexScreener's free REST API as Claude Desktop tools — live DEX prices, liquidity, pairs, trending tokens across 60+ chains. K106 documents Claude Desktop config path (Node 18+, `claude_desktop_config.json`).

## Narrative

### Architecture

`Claude Desktop → MCP Server (Node.js) → DexScreener API → live DEX data`

Distinct from K78 **Hermes + x402 forensics** pipeline (Nansen/Tokenomist/Cookie paid legs). This path is **zero API key**, ~15–30 min laptop setup, pre-trade diligence only — **not execution**.

### Audience (per source)

Crypto researchers, DeFi analysts, content creators, developers building market mental models. Explicit risk section in source: honeypots, illiquid pairs, AI hallucination on thin data.

### Cemini posture

**REFERENCE / laptop tooling** — useful for OSINT crypto-entity research sessions. Prod trading stack uses Cemini EMS + audited connectors; do not wire DexScreener MCP into prod execution path without Phase-0 + security review.

License of specific MCP repo: **[NEEDS VERIFICATION 2026-06-08]** — verify via `gh api` before any install (ingest gate).

## Snippets

> "Claude cannot directly query APIs. But MCP gives it a structured way to request external data through predefined tools." [Source: Posts.docx K106, @AlphaCartell Post 5]
