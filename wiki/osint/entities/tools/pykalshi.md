---
title: pykalshi — High-Performance Unofficial Kalshi Client (MIT)
type: entity
tags: [tool, prediction-markets, kalshi, mit, adopt-tier, replace-official-sdk]
keywords: [pykalshi, kalshi-client, prediction-market-trading, async-python, kalshi-sdk-replacement]
related:
  - sources/5-5-links-2-tool-eval.md
  - entities/platforms/kalshi.md
  - entities/tools/kalshi-llms-txt.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-links-2-tool-eval.md — origin source: 2026-05-05 Gemini DR eval, URL 27, **Adopt** tier ("the optima[l]" Kalshi client)
- @entities/platforms/kalshi.md — Kalshi venue entity; pykalshi is the recommended client library for it
- @entities/tools/kalshi-llms-txt.md — companion Adopt-tier from same batch (Kalshi's LLM-readable docs)

## Raw Concept

Unofficial high-performance Python client for the Kalshi API. Per Gemini DR eval: "completely replaces the bloated official SDK." MIT-licensed (clean for IP-sale). Adopt-tier verdict in K30 5_5-links-2 batch.

## Narrative

- **URL**: per K30 eval (specific URL TBD — need to confirm in repo)
- **License**: MIT
- **Stack**: Python async-first
- **Maturity**: per eval, "high-performance" + "completely replaces" framing implies production-grade

### Why Adopt for Cemini

Cemini's existing Kalshi integration uses the official Kalshi Python SDK. Per the K30 Gemini DR eval, the official SDK is "bloated" and pykalshi delivers a cleaner, faster alternative. Direct Cemini production-stack replacement.

Integration flow:
1. Replace `import kalshi` (official) with `import pykalshi` in `services/llm_analyst/kalshi_client.py` (or wherever the existing import lives)
2. Adapt method signatures (likely small surface — both clients wrap the same Kalshi REST API)
3. Update `services/llm_analyst/conductor_client.py` if Conductor routes Kalshi-specific queries through pykalshi
4. Backtest equivalent calls before flipping production

### Open questions [NEEDS VERIFICATION 2026-05-05]

- Exact GitHub URL (need to verify against the eval doc)
- Star count, commits count, latest version — eval mentions "high-performance" but specific maturity numbers not extracted
- Async-first claim: confirm coroutine-based API vs sync. Cemini's existing trading loop is mostly synchronous; an async-first client may need an asyncio bridge.
- Test coverage / soundness signals
- Whether pykalshi covers all endpoints Cemini currently uses (markets, orders, positions, fills, user-balance)

### Adoption gating

- Phase 0: clone repo, audit license + maturity + endpoint coverage
- Phase 1: drop into a sandbox `services/` test env; replicate Cemini's existing Kalshi calls; benchmark vs official SDK
- Phase 2: production cut-over with rollback plan

Stage as part of the K30 Polymarket-readiness brief (since both venue clients change together) OR as a standalone Kalshi-only brief.

## Snippets

- **Adopt-tier framing** (K30 eval): "completely replaces the bloated official SDK." [Source: 5_5 links 2.docx URL 27]
- **Recommendation tier**: "Adopt. This is the optima[l] Kalshi client." [Source: 5_5 links 2.docx URL 27]
