---
title: "Awesome-Polymarket-Tools (harish-garg) — CC0-licensed Polymarket dev resource directory"
type: entity
category: tool
tags: [entity, tool, awesome-list, polymarket, prediction-markets, cc0-license, k44, reference-only]
keywords: [awesome-polymarket-tools, harish-garg, cc0-1-0, gamma-api, py-clob-client, websocket-streaming, sim-ai-mcp, public-domain]
related:
  - sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/awesome-prediction-market-tools-aarora4.md
  - concepts/cemini-license-posture.md
maturity: reference-only
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @entities/tools/polymarket-clob-api.md — directory references CLOB tooling
- @entities/tools/polymarket-gamma-api.md — directory references Gamma API
- @entities/tools/awesome-prediction-market-tools-aarora4.md — K44 rejected alternative (no license); this CC0 page is the mitigated replacement
- @concepts/cemini-license-posture.md — CC0-1.0 = public domain, IP-sale-safest

## Raw Concept

A curated Markdown directory of Polymarket developer tools and integrations. **CC0-1.0 (Public Domain) — 80 stars** per K44 doc-level eval. Verdict: **Reference-only**. The CC0 license is the safest possible for IP-sale; the directory may be ingested, adapted, or quoted without restriction.

## Narrative

K44 primary fit: OSINT-wiki. Cross-routes: Cemini-financial (API integration reference for trading bots), CCC-wiki (MCP server mapping for prediction-market agents).

**Documented contents per K44**:
- Official Polymarket Gamma API reference
- `py-clob-client` WebSocket streaming
- Model Context Protocol (MCP) integrations — specifically **Sim.ai–Polymarket** MCP allowing AI agents direct access to order-book telemetry

**Status**: K43 already established `@entities/tools/polymarket-clob-api.md` and `@entities/tools/polymarket-gamma-api.md` with first-party tradecraft. This directory complements those pages by enumerating third-party tools and MCP integrations. **Use case**: scan periodically for new Polymarket MCP servers worth Phase-0-auditing.

**Phase-0 gates**: minimal — Reference-only items don't get code-coupled, so the audit reduces to (a) verify the repo exists at the URL, (b) verify CC0 license actually applied, (c) cross-check listed tools against Cemini's own Polymarket adapter to identify missing integrations.

## Snippets

> "In stark contrast to the previous asset, this Polymarket directory is explicitly licensed under CC0-1.0 (Public Domain), rendering it completely safe for integration."
[Source: K44 eval ¶241]
