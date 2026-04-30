---
title: "kukapay/polymarket-predictions-mcp — Polymarket Real-Time Odds MCP Server (Python, MIT, 3★)"
type: source
tags: [github, mcp-server, polymarket, prediction-markets, real-time-odds, python, mit-license, cemini-adopt-candidate-with-caveat, single-day-development, fork-and-maintain-required, gemini-dr-wave4]
keywords: [polymarket-predictions-mcp, kukapay, polymarket-odds, prediction-market-mcp, real-time-market-data, llm-tool-call, decentralized-prediction-data, single-day-development-bus-factor, gomez-cram-informed-flow-deployment-surface]
clusters: [prediction-markets, infrastructure, llm-agents]
related:
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - sources/polymarket-informed-minority-gomezcram-2026.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/ip-sale-readiness.md
  - concepts/high-signal-paper-patterns.md
  - sources/last30days-skill-mvanhorn.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
read_status: read-skim
created: 2026-04-29
updated: 2026-04-30
---

## Relations

- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — Wave 4A canonical brief; URL 19 Adopt-with-caveat; promoted to dedicated source this session
- @sources/gemini-dr-wave5b-osint-2026-04-30.md — Wave 5B canonical brief surfaces a sibling Polymarket MCP (caiovicentino's, 395★ / 45 tools / 5 categories) as a Wave 5B Adopt. The two MCPs together form the **dual-MCP-Polymarket pattern**: this server is read-mostly real-time-odds; caiovicentino's server is read-and-trade with full CLOB API + on-chain settlement (USDC.e + MetaMask). Decision tree: read-only odds → this MCP; trading + market discovery + portfolio → caiovicentino's; both → run both servers, scope tool-allowlists per use case
- @sources/caiovicentino-polymarket-mcp-server.md — sibling Polymarket MCP, dual-MCP-Polymarket pattern. caiovicentino's is more comprehensive (395★ vs 3★, 45 tools vs ~6, 5 categories vs single-day-dev) but bus-factor caveat applies to both (1 contributor each); this MCP's narrower surface (real-time odds only) makes the fork-and-maintain footprint smaller
- @sources/polymarket-informed-minority-gomezcram-2026.md — **directly pairs**: this MCP is the **data-access layer** for the "Polymarket informed-flow analyst" service that paper proposes. Without a Polymarket data layer, the informed-minority signal can't be extracted; with this MCP (or a fork of it), the analyst node can consult live odds during reasoning.
- @entities/platforms/polymarket.md — direct subject; the MCP wraps Polymarket's odds API
- @entities/platforms/kalshi.md — sibling prediction market in Cemini's watchlist; analogous Kalshi MCP would be the natural extension if this pattern works
- @concepts/ip-sale-readiness.md — MIT license clean
- @concepts/high-signal-paper-patterns.md — rubric negative-signals **trigger**: 3 stars / 1 contributor / single-day-development = severe bus-factor caveat. Adoption requires fork-and-maintain pattern, not upstream-follow.

## Raw Concept

- **URL**: https://github.com/kukapay/polymarket-predictions-mcp
- **Type**: Open-source MCP server
- **License**: MIT (Exa-verified 2026-04-29; same kukapay author as `dune-analytics-mcp`)
- **Stars / Forks (Exa-verified 2026-04-29)**: 3 ★ / 2 forks ⚠️
- **Stack**: Python (primary)
- **Org**: kukapay (single author/contributor)
- **Created**: 2025-09-23; **Last push**: 2025-09-23 ⚠️ **single-day-development** (created and last-modified on the same day)
- **Required deps**: Python; Polymarket API access (presumably public; verify)
- **Discovered via**: Gemini DR Wave 4A 2026-04-29 (URL 19); promoted to dedicated source page same session

## Narrative

### What it is

A Python MCP server delivering **real-time market odds from Polymarket**. Wraps Polymarket's odds API and exposes it as MCP tools so AI agents can query live prediction-market data during reasoning.

Quote from the README: "An MCP server that delivers real-time market odds from Polymarket, enabling AI agents and analysts to access, compare, and act on decentralized prediction data."

### Why Cemini-direct

This MCP is the **data-access layer** for the Cemini deployment surface proposed in `@sources/polymarket-informed-minority-gomezcram-2026.md`. That paper:
- Identifies that **3.14% of Polymarket accounts** are skilled persistent winners
- Their order flow predicts both next-period prices AND final outcomes (1pp ↑ skilled net buying = 8bp ↑ correct-outcome probability)
- Skill persistence is **44% out-of-sample** (vs 10% for mutual funds)
- The "informed-flow analyst" service for Cemini that the paper sketches: ingest Polymarket trade data, apply sign-randomization test, identify the top 3% accounts, emit their order flow as a signal to Cemini's analysts

For that service to exist, Cemini needs:
1. **Polymarket data access** (this MCP)
2. **Sign-randomization test implementation** (not in this MCP; would be Cemini-side Python)
3. **Skilled-trader identification storage** (Cemini-side, e.g. PostgreSQL table)
4. **Analyst-orchestrator integration** (call the skilled-flow signal during ticker research)

This MCP solves step 1.

### The bus-factor caveat (severe)

The rubric's negative-signals fire hard here:
- **3 stars** — barely-noticed project
- **1 contributor** — solo author
- **Created and last-modified on the same day** (2025-09-23) — single-day-development repo, possibly an experiment that wasn't continued

Possible interpretations:
1. **Author abandoned after initial push** — most likely. Common pattern for solo-explorer github repos.
2. **Author ran a workshop / one-off project** — also possible. The kukapay user has multiple MCP-server repos in the same shape (`dune-analytics-mcp`, polymarket-predictions, etc., all in `kukapay-mcp-servers` aggregator at `github.com/kukapay/kukapay-mcp-servers`).
3. **Stable + complete from day one** — least likely but possible if the underlying API surface is small and well-documented.

**Mitigation**: fork-and-maintain pattern. Clone the repo, audit the actual code (the README claims more than the code may deliver), bring it in-house, accept that upstream is dead. **Pre-deployment gate**: clone + read the entire codebase (it's small) before declaring this Adopt + deployable.

### Cemini-side adoption assessment

**Decision: Conditional Adopt** (gated on code-read + fork-and-maintain commitment). Concrete next-steps:

1. **Clone + read the entire codebase** — should take 30 min given the project size. Verify the MCP tool surface matches what Cemini's informed-flow analyst needs.
2. **Test against Polymarket public API** — does the MCP actually work? With 3 stars and zero issues, real-world testing is light.
3. **Fork to a Cemini-controlled repo** + pin commit hash. ~5 min.
4. **Implement the missing pieces** for the informed-flow analyst service (sign-randomization test, skilled-trader storage, analyst integration). ~1-2 days dev work, separate from this MCP.
5. **Brief to cemini-prod** for the full informed-flow analyst service when ready.

### Risks & open questions

1. **Code may not match README claims** — single-day-dev repos are notorious for over-promising in the README and under-delivering in code. Pre-adoption gate: actual code-read.
2. **Polymarket API access pattern** [NEEDS VERIFICATION 2026-04-29] — public vs authenticated? Rate-limited?
3. **The full informed-flow analyst service requires substantial Cemini-side work**. This MCP is just the data layer; the analytical layer (sign-randomization test, skill-persistence tracking) is separate and non-trivial.
4. **Polymarket platform risk** — Polymarket itself is decentralized and crypto-coupled. Regulatory environment is in flux (cf. CFTC ANPRM in `@sources/cftc-anprm-prediction-markets-2026-03-16.md`). Cemini's Polymarket exposure has both data-source-risk and platform-risk dimensions.
5. **Kalshi sibling expansion** — the same pattern (Kalshi MCP) doesn't yet exist publicly. If Cemini commits to this MCP, it may need to **build a Kalshi-MCP itself**, since Cemini's watchlist includes Kalshi-traded events.

### Citation

> kukapay. (2025). *Polymarket Predictions MCP*. https://github.com/kukapay/polymarket-predictions-mcp (MIT License; created and last-pushed 2025-09-23 — single-day-development repo; 3 stars / 2 forks / 1 contributor as of 2026-04-29)

## Snippets

> **Project mission (from README)**:
>
> "An MCP server that delivers real-time market odds from Polymarket, enabling AI agents and analysts to access, compare, and act on decentralized prediction data." [Source: https://github.com/kukapay/polymarket-predictions-mcp README, retrieved 2026-04-29 via Exa]

> **Cross-link operational pairing with the LBS/Yale paper**:
>
> The paper `@sources/polymarket-informed-minority-gomezcram-2026.md` provides the **why** (3.14% of accounts drive accuracy; 44% skill persistence; 8bp/1pp informed-flow predictive power); this MCP provides the **how** (LLM-agent data access to live odds). Without this MCP (or equivalent), the analyst service cannot be built. [Workspace cross-reference 2026-04-29]
