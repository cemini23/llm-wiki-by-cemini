---
title: "tradingview-mcp — MCP Server for TradingView Data"
type: entity
tags: [tool, trading, mcp, technical-analysis, data, market-data]
keywords: [tradingview, MCP server, technical analysis, screener, real-time data, crypto, stocks]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 8)

## Raw Concept

A comprehensive MCP (Model Context Protocol) server that exposes TradingView's technical analysis, screener, and market data capabilities as callable tools for AI agents like Claude Code and DeepSeek.

- **Repo**: `github.com/atilaahmettaner/tradingview-mcp`
- **License**: To verify
- **Stack**: Python, MCP protocol, Docker-deployable

## Narrative

The tradingview-mcp server consumes natural language prompts from AI clients and produces structured institutional-grade technical analysis, historical correlation data, and walk-forward strategy simulations. It bridges the gap between LLM reasoning and real-time market data.

### Integration vectors

- **Cemini prod (Adopt)**: Deploy as isolated Docker container within the `docker-compose.yml` cluster. Map its MCP endpoints into the existing registry of ~130 `@mcp.tool` decorators. The LangGraph orchestrator can then invoke technical analysis, screener queries, and correlation studies natively during strategy evaluation.
- **Workflow (Adopt)**: Connect to local macOS Claude Code for interactive historical correlation mapping and walk-forward simulations during research sessions.

### Risks

- **Web scraping reliance**: Underlying dependencies (`tradingview-screener`, `tradingview-ta`) scrape TradingView and Yahoo Finance without official API keys, introducing IP ban risk. For 24/7 crypto trading, a single IP ban breaks the data pipeline.
- **Session authentication**: Lower-timeframe data (1m, 5m) may require authenticated TradingView session cookies.

### Open questions

- Do the underlying scrapers require paid TradingView session cookies for reliable 1m/5m tick data? `[NEEDS VERIFICATION 2026-05-10]`

### Cemini significance

This is one of the highest-value adopt recommendations across all three evaluation briefs. It provides the real-time technical analysis layer that the current stack lacks, directly augmenting the LLM's decision matrix with structured market data.

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 8]
