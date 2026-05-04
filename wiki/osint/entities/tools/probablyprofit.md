---
title: probablyprofit — Polymarket Trading Framework (MIT)
type: entity
tags: [llm-agents, prediction-markets, polymarket, kelly-criterion, llm-ensemble, mit, steal-from]
keywords: [probablyprofit, polymarket, kelly-criterion, llm-ensemble-consensus, kill-switch, drawdown-protection, prediction-market-trading]
related:
  - sources/5-4-links-tool-eval.md
  - entities/tools/riskfolio-lib.md
  - entities/tools/atlas-gic-autoresearch.md
maturity: draft
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/5-4-links-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 12, **Steal-from** tier verdict
- @entities/tools/riskfolio-lib.md — Riskfolio-Lib provides BSD-3-Clause-licensed alternative for the Kelly + risk-management math; preferred path for production unless probablyprofit's LLM-ensemble pattern is needed
- @entities/tools/atlas-gic-autoresearch.md — atlas-gic's 25-agent debate is the larger-scale evolution of probablyprofit's LLM-ensemble consensus pattern

## Raw Concept

Robust Python algorithmic trading framework engineered explicitly for prediction markets — primarily Polymarket. Production-grade safeguards: Kelly criterion sizing, automated drawdown protection, multi-vector emergency kill switch, LLM ensemble consensus mode (Claude + GPT-4 + Gemini vote on trades). Identified as **Steal-from-tier** in the 2026-05-04 Gemini DR eval.

## Narrative

- **URL**: https://github.com/randomness11/probablyprofit
- **License**: MIT (clean for IP-sale)
- **Stack**: Python 3.10+, Docker, Alembic (DB migrations), real-time WebSocket feeds, Polymarket CLOB API
- **Maturity**: 100 commits, v1.0.1 released 2026-01, 30 stars

### Why Steal-from (not Adopt directly)

The Polymarket-targeted networking adapters (CLOB API, WebSocket feeds, USDC settlement on Polygon) require a full rewrite for Cemini's prediction-market venue mix (Kalshi primary; Polymarket secondary). But the **internal Python architecture** is exceptional and lifts cleanly:

1. **Ensemble consensus mode** — 3-LLM voting topology (Claude + GPT-4 + Gemini); each casts a recommendation; trade executes only on supermajority. Direct application: `agents/orchestrator.py` consensus node before execution.
2. **Kelly criterion sizing** — production-tested implementation. (Riskfolio-Lib provides a more academically-grounded alternative; pick whichever matches Cemini's existing code style better.)
3. **Multi-vector emergency kill switch** — hardware AND HTTP-based shutdown triggers. Defensive depth pattern; useful for any high-frequency execution loop.
4. **Automated drawdown protection** — preflight checks, real-time Telegram alerts, automated max-drawdown halt.

### Prediction-market scope alignment

probablyprofit is **directly in-domain** for Cemini's prediction-market work (per user note 2026-05-04): Kalshi + Polymarket cover sports, healthcare/biotech, politics, weather, economic indicators. The Kelly-sizing and ensemble-consensus patterns work on any binary-contract prediction market regardless of underlying topic. The networking layer needs adaptation; the decision-and-execution layer translates near-directly.

### Key adaptation work

- Strip Polymarket-specific networking (CLOB API, USDC settlement on Polygon)
- Rewire to Kalshi API (primary) and/or Polymarket via separate adapter (secondary)
- Preserve Kelly + ensemble-consensus + kill-switch logic as core Cemini modules

### Caveats

- Live-trading safeguards depend on assumptions about Polygon's network behavior — verify equivalent assumptions hold for Kalshi's infrastructure before transplanting
- LLM ensemble consensus adds 3× API token cost per decision; benchmark against single-LLM-with-self-correction (Gemini paper §2.1) before committing to the ensemble cost

## Snippets

- **Kelly + ensemble + kill-switch summary**: "leveraging a sophisticated 'ensemble consensus mode,' which orchestrates multiple LLMs (Claude, GPT-4, Gemini) to vote dynamically on trade executions. The system is hardened with advanced financial risk controls, natively implementing Kelly criterion position sizing, automated maximum drawdown protection, and a multi-vector emergency kill switch." [Source: 5_4 links.docx URL 12]

- **Recommendation tier**: "Steal-from. While the platform's networking layer strictly targets the Polymarket CLOB API on the Polygon network (whereas Cemini currently targets Kalshi), the internal Python architecture is exceptional. The modules calculating Kelly criterion sizing, the hardware and HTTP-based emergency kill switch triggers, and the LLM voting consensus mechanisms should be extracted, refactored, and integrated into the Cemini FastMCP/LangGraph orchestration engine immediately." [Source: 5_4 links.docx URL 12]

- **Network-layer rewrite caveat**: "The execution adapters will require a total rewrite, as they are tightly coupled to Polymarket's specific WebSocket feeds and USDC settlement contracts. Consequently, the core extractable value lies entirely in the risk management mathematics and consensus logic, rather than the networking or routing layers." [Source: 5_4 links.docx URL 12]
