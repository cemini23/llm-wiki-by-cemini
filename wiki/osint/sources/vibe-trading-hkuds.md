---
title: HKUDS/Vibe-Trading — Personal Trading Agent (Python+FastAPI+MCP, MIT)
type: source
tags: [llm-agents, multi-agent, algorithmic-trading, mcp, fastapi, python, hkuds, cemini-adopt-candidate, ip-sale-clean]
keywords: [vibe-trading, hkuds, mcp-tool, ccxt, yfinance, akshare, okx, swarm-presets, backtest-engine, pine-script, mql5, langgraph-orchestrator, agents-orchestrator-py, fastapi-backend, react-frontend-strip, polygon-alpaca-swap]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/scatter-gather-topology.md
  - concepts/ip-sale-readiness.md
  - concepts/ai-organisation-design.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/fastmcp.md
  - entities/frameworks/ccxt.md
  - entities/infrastructure/deepseek-api.md
  - entities/infrastructure/yfinance.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
read_status: deep-read
created: 2026-04-28
updated: 2026-05-17
clusters: [llm-agents, trading-agents]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — parent canonical Gemini DR source; this URL is one of two Adopt-for-Cemini recommendations (the other is `sources/langextract-google.md`)
- @concepts/wiki-tooling-evaluation.md — Wave 2 evaluation parent; Vibe-Trading is the highest-impact Cemini-stack adoption from this wave
- @concepts/scatter-gather-topology.md — Vibe-Trading's 29 expert-agent swarms would interface with the existing scatter-gather pattern at `agents/orchestrator.py` via MCP
- @concepts/ip-sale-readiness.md — MIT license clears IP-sale checks; verified via Exa `crawling_exa` 2026-04-28 (3462 ★, 734 forks)
- @concepts/ai-organisation-design.md — Vibe-Trading is exactly the kind of agent-orchestration project that could be "a Container" under OMC's Talent+Container abstraction; pattern reference
- @entities/frameworks/langgraph.md — Cemini's StateGraph orchestrator is where Vibe-Trading's MCP tools would attach
- @entities/frameworks/fastmcp.md — native MCP support means Vibe-Trading bolts onto FastMCP via `@mcp.tool` decorators with no adapter glue
- @entities/frameworks/ccxt.md — CCXT integration in Vibe-Trading complements Cemini's existing Coinbase/OANDA pipelines (Coinbase is currently a CCXT-mediated integration, not a dedicated entity page yet)
- @entities/infrastructure/deepseek-api.md — current Cemini brain; Vibe-Trading is LLM-agnostic and can consume DeepSeek via OpenAI-compatible config
- @entities/infrastructure/yfinance.md — Vibe-Trading uses yfinance as a default data loader; per Cemini's Polygon-NOT_AUTHORIZED-doctrine memory, the data loader must be swapped to Polygon/Alpaca for institutional-grade feeds before deploy
- @sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md — **Wave 4A status-change cross-link**: 2026-04-29 Wave 4A reclassifies this URL from Wave 2's **Adopt-for-Cemini** to **Steal-from**. Reasoning per Wave 4A URL 22 evaluation: bloated React frontend (13.1% TS/JS) is non-starter for headless deployment; yfinance-fallback creates production-grade reliability risk under polygon_not_authorized_doctrine. Operational implication: extract the **agent-swarm topology + MCP-tool-decorator pattern** as Steal-from, do not deploy the project as-is. The Wave 2 Adopt-Cemini recommendation should be considered superseded for production deployment, while the architectural pattern remains usable as an internal reference.

## Raw Concept

- **URL**: https://github.com/HKUDS/Vibe-Trading
- **Type**: Open-source repository / Python framework
- **License**: MIT (Exa-verified 2026-04-28)
- **Stars / Forks (Exa-verified 2026-04-28)**: 3462 ★ / 734 forks / 32 watchers / 5 open issues
- **Stack**: Python 85.2%, TypeScript 13.1%, HTML 0.7%, CSS 0.7%, Jinja, Dockerfile
- **Org**: HKUDS (HKU Data Science Lab presumed; verify if adoption proceeds)
- **Created**: 2026-04-01; **Last push**: 2026-04-28; **Latest release**: v0.1.6 (2026-04-28)
- **Topics**: ai-agent, algorithmic-trading, backtesting, fintech, llm, mcp, multi-agent, python, quantitative-finance, trading
- **Homepage**: https://pypi.org/project/vibe-trading-ai/
- **Contributors**: 20 (top: warren618, hamza-mobeen, yule153604, MB-Ndhlovu, Matheus083)
- **Releases**: 3 published; v0.1.6 is the post-spot-check current

## Narrative

### What it does
Vibe-Trading is a multi-agent financial workspace that converts natural-language descriptions into backtested, executable trading code. Python+FastAPI backend orchestrates 29 pre-built expert agent "swarms" for tasks including risk management, portfolio analysis, and signal generation. Executes against 7 cross-market backtest environments and ships a "Shadow Account" system to validate trading rules extracted from broker journals. Bridges research and execution by exporting strategies to retail platforms — TradingView Pine Script v6 and MetaTrader 5 MQL5.

### Why Adopt-for-Cemini

The Gemini DR evaluation is unambiguous: this is the single highest-impact Cemini-stack adoption from the 24-URL wave. Reasoning (verified by Exa 2026-04-28):

1. **Stack alignment** — Python + FastAPI matches Cemini's backend architecture exactly (no language porting required).
2. **Native MCP** — `@mcp.tool` decorators mean direct attach to Cemini's existing FastMCP layer (`cemini_mcp` 130-tool container) without adapter code. The DeepSeek API instantly sees 7 backtest engines as MCP tools.
3. **CCXT** — complements existing Coinbase/OANDA crypto + FX ingestion at the data-source layer.
4. **MIT license** — clears all IP-sale-readiness gates per `concepts/ip-sale-readiness.md`.
5. **Active development** — v0.1.6 shipped 2026-04-28 (the same day as the Gemini DR), with 20 contributors and 734 forks. Not a one-author flash project.

### Required adaptations before deploy

Per the Gemini evaluation's caveats and Cemini's known constraints:

1. **Strip the React frontend** — the 13.1% TS/JS frontend is unnecessary for headless API-driven backend operations. Remove from `docker-compose.yml` to preserve the 7 GB RAM envelope. Vibe-Trading's CLI + MCP path is the entire integration surface Cemini needs.
2. **Swap yfinance for Polygon/Alpaca** — yfinance is notoriously rate-limited and silent-failure-prone. Per the workspace's `polygon_not_authorized_doctrine` memory: yfinance is acceptable as Cemini's *EOD-fallback* but not as a primary data loader. Vibe-Trading's data loader module needs systematic swap to prioritise paid Polygon/Alpaca endpoints with yfinance retained only as last-resort fallback.
3. **Aggressive Docker memory caps** — `deploy.resources.limits.memory` hardcoded in `docker-compose.yml` to prevent FastAPI+Pandas from crowding the 7 GB envelope already contested by Postgres, Polars, Redis, and Python.
4. **Verify Shadow Account state persistence** [CONFIRMED 2026-05-17 — local-disk, as feared] — verified via the repo's published directory tree + README (Exa 2026-05-17). Vibe-Trading's persistence is **file-based, not database-backed**: cross-session memory lives at `~/.vibe-trading/memory/` (`agent/src/agent/memory/persistent.py` — "file-based memory"), settings persist to `agent/.env`, and the Shadow Account flow (4 tools: `analyze_trade_journal`, `extract_shadow_strategy`, `run_shadow_backtest`, `render_shadow_report`) produces HTML/PDF report artifacts that are written to disk and "archived"/"persisted" as files — no PostgreSQL path. **This confirms the concern**: deployed as-is in an ephemeral Docker container, Shadow Account state and persistent memory would be lost on container recreation. Mitigation for Cemini deployment: mount a persistent volume for `~/.vibe-trading/memory/` and the report-artifact directory, OR (cleaner) treat Shadow Account as a Steal-from-only feature and not deploy it on the production critical path — consistent with the Wave 4A Steal-from reclassification already recorded above.
5. **Disable LLM auto-loading** — ensure no local LLMs load into the container's resident memory; Cemini's brain is the DeepSeek API, not a self-hosted model.

### Integration vector

```
Cemini orchestrator (LangGraph StateGraph at agents/orchestrator.py)
        ⬇ MCP attach via @mcp.tool decorator
Vibe-Trading FastAPI backend (Docker container, ~headless)
        ⬇ exposes
[backtest_engine_1, ..., backtest_engine_7, risk_manager, portfolio_analyzer, ...]
        ⬇ orchestrates 29 swarm agents internally
DeepSeek API (via OpenAI-compatible wrapper, OPENAI_BASE_URL=https://api.deepseek.com)
```

### Observed maturity signals (Exa-verified 2026-04-28)

- **Star drift from Gemini's claim**: ~1% (3.5k claimed vs 3462 actual)
- **3 published releases**: indicates real packaging discipline
- **20 contributors**: not a one-person project; some inbound community contribution
- **PyPI presence**: `pip install -U vibe-trading-ai` works (per latest README excerpt; preset YAMLs bundled in `src.swarm` package)
- **Active issue triage**: v0.1.6 release notes reference issue #55 (preset bundling fix), AKShare loader endpoint correction, 6-test regression suite

### Risks & open questions

1. **Solana/DeFi bias unknown** — the AutoHedge sibling repo (also evaluated in the Gemini DR wave, also Steal-from tier) is heavily Solana-focused. Vibe-Trading's broader exchange integrations (CCXT + Futu + AKShare for HK/A-share + OKX) suggest a different bias, but worth verifying that the framework doesn't have hidden Jupiter/Solana paths that would be unused/dead in Cemini's deployment.
2. **Strategy export to retail platforms (Pine Script v6, MQL5)** — useful for human-readable verification but Cemini's actual execution path is institutional-grade (Alpaca + OANDA + Coinbase). The export feature is decorative for Cemini, not core. Don't over-invest in maintaining it.
3. **Repository age** — created 2026-04-01, less than a month old at evaluation. High velocity (3 releases) but framework stability is unproven. **Pre-deployment soak**: run in isolation for 2 weeks before joining the production critical path.

## Snippets

> "AI-driven, multi-agent financial workspace architected to convert natural language descriptions directly into backtested, executable trading code and analytical strategies." [Source: Gemini DR report, URL 10]

> "Native MCP capabilities allow the framework to be bolted directly onto the LangGraph linear orchestrator at agents/orchestrator.py, granting the DeepSeek API instant access to the 7 backtest engines via standard @mcp.tool decorators." [Source: Gemini DR report, URL 10 — Cemini integration vector]

> "v0.1.6 released (`pip install -U vibe-trading-ai`): Fixes `vibe-trading --swarm-presets` returning empty after `pip install` / `uv tool install` (#55) — preset YAMLs now bundled inside the `src.swarm` package and pinned by a 6-test regression suite. Plus AKShare loader correctly routes ETFs (510300.SH) and forex (USDCNH) to the right endpoints with hardened registry fallback." [Source: GitHub README excerpt, retrieved via Exa crawling_exa 2026-04-28]
