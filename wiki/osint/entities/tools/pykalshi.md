---
title: pykalshi — High-Performance Unofficial Kalshi Client (MIT)
type: entity
tags: [tool, prediction-markets, kalshi, mit, adopt-tier, replace-official-sdk]
keywords: [pykalshi, kalshi-client, prediction-market-trading, async-python, kalshi-sdk-replacement]
related:
  - sources/5-5-links-2-tool-eval.md
  - entities/platforms/kalshi.md
  - entities/tools/kalshi-llms-txt.md
  - concepts/kalshi-api-reference.md
maturity: validated
created: 2026-05-05
updated: 2026-05-28
---

## Relations

- @sources/5-5-links-2-tool-eval.md — origin source: 2026-05-05 Gemini DR eval, URL 27, **Adopt** tier ("the optima[l]" Kalshi client)
- @entities/platforms/kalshi.md — Kalshi venue entity; pykalshi is the recommended client library for it
- @entities/tools/kalshi-llms-txt.md — companion Adopt-tier from same batch (Kalshi's LLM-readable docs)

## Raw Concept

Unofficial high-performance Python client for the Kalshi API. Per Gemini DR eval: "completely replaces the bloated official SDK." MIT-licensed (clean for IP-sale). Adopt-tier verdict in K30 5_5-links-2 batch.

## Narrative

- **URL**: `https://github.com/ArshKA/pykalshi` (verified 2026-05-05 via gh API)
- **License**: **MIT** (verified)
- **Stack**: Python (PyPI v1.0.6); WebSocket streaming; pandas integration; automatic retries; Action/Side enum-driven API surface
- **Maturity**: 85 stars, 16 forks, 30 commits, 0 open issues, last push 2026-05-02 (3 days fresh), CI test workflow active

### Why Adopt for Cemini

Cemini's existing Kalshi integration uses the official Kalshi Python SDK. Per the K30 Gemini DR eval, the official SDK is "bloated"; pykalshi delivers a cleaner, faster alternative with WebSocket streaming + pandas integration baked in (the official SDK doesn't ship pandas helpers; downstream code currently builds them by hand).

Integration flow per `@briefs/2026-05-05_pykalshi-adoption.md`:

1. Phase 0 verification: smoke test in sandbox; verify auth-format compatibility with Cemini's existing API key + RSA private key
2. Replace official-SDK calls in `services/llm_analyst/kalshi_client.py` with pykalshi imports + wrapper class preserving Cemini's existing method signatures
3. Update FastMCP tool decorators in `services/llm_analyst/mcp_tools/kalshi_tools.py` (minimal — wrapper preserves shape)
4. Update Conductor `config.yaml` with planned `prediction_market_kalshi` taxonomy class (per K30 #19 → planned-class section in `@concepts/conductor-orchestrator.md`)
5. Retain `kalshi_client_legacy.py` for 30-day rollback window
6. Paper-trading dry-run ≥ 1 week before live cutover

### Resolved Phase 0 questions (2026-05-05)

- ✅ **Exact GitHub URL**: `https://github.com/ArshKA/pykalshi`
- ✅ **License**: MIT (verified via `gh api repos/ArshKA/pykalshi`)
- ✅ **Maturity signals**: 85 stars / 16 forks / 30 commits / v1.0.6 PyPI / CI-active / 3-day-fresh push / 0 open issues
- ✅ **Bus factor**: single primary maintainer (ArshKA). Pin version; fork if maintainer disappears.
- ✅ **WebSocket + pandas**: confirmed in README

### Outstanding Phase 0 questions (gate Phase 1)

- [NEEDS VERIFICATION 2026-05-05] Auth-format compatibility with Cemini's existing API key + RSA private key (likely identical — both wrap the same Kalshi REST API)
- [NEEDS VERIFICATION 2026-05-05] Endpoint coverage vs the ~150 endpoints documented in `@concepts/kalshi-api-reference.md` (especially FCM, RFQ/quote, live-data milestones — newer Kalshi features that may or may not be wrapped yet)
- [NEEDS VERIFICATION 2026-05-05] Rate-limit handling — pykalshi's "automatic retries" needs to respect Kalshi's specific tier-based rate-limit headers under load

### Adoption status

**Brief staged 2026-05-05**: `briefs/2026-05-05_pykalshi-adoption.md` (also at `cemini-prod:/opt/cemini/briefs/`). Sister to `briefs/2026-05-05_polymarket-stack-adoption.md`; together they refresh both prediction-market venue clients. Awaiting prod-side execution.

### Phase-0 clone audit (2026-05-28)

Clone: `/tmp/k73-phase0-batch2/pykalshi` (supplements 2026-05-05 API verification)

| Check | Result |
|-------|--------|
| License | **MIT** in-file + GitHub API |
| Maturity | ~96★, active CI/tests, WebSocket + REST modules present |
| Code quality | Structured client package with tests; no hardcoded Cemini paths observed |
| Remaining gates | Auth compatibility + endpoint coverage vs `@concepts/kalshi-api-reference.md` still require prod sandbox smoke test |

**Verdict: CONDITIONAL-GO** — remains the leading Kalshi client replacement candidate; proceed via existing `briefs/2026-05-05_pykalshi-adoption.md` with Phase-1 sandbox checks.

## Snippets