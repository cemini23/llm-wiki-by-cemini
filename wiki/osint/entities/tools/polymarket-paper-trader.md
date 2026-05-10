---
title: "polymarket-paper-trader — MCP-Based Paper Trading Simulator"
type: entity
tags: [tool, polymarket, paper-trading, mcp, simulation, prediction-markets]
keywords: [polymarket, paper trader, MCP server, forward-testing, LLM trading, slippage modeling]
related:
  - sources/project-link-evaluation-brief-5_10.md
  - entities/tools/polybot.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/project-link-evaluation-brief-5_10.md` — source evaluation brief (URL 4)

## Raw Concept

A high-fidelity Polymarket paper trading simulator exposing 26 MCP tools for AI agents. Models real exchange mechanics (slippage, order book depth, fee structures) against live Polymarket data.

- **Repo**: `github.com/agent-next/polymarket-paper-trader`
- **License**: MIT
- **Stack**: Python 100%, Python 3.10+
- **Maturity**: 312 stars, v0.1.6 (March 2026)

## Narrative

Polymarket-paper-trader consumes real Polymarket order book data and allows LLMs to execute simulated trades with $10,000 initialized virtual capital. It accurately models slippage, order book depth, and exchange fee structures, providing a safe sandbox for testing LLM-driven trading strategies without financial risk.

### Integration vectors

- **Cemini prod (Adopt)**: Mount as discrete FastMCP service within Docker Compose. The `agents/orchestrator.py` LangGraph node invokes the 26 MCP tools via DeepSeek API to test algorithmic strategies in a hallucination-resistant environment before live deployment.
- **Workflow (Adopt)**: Run locally on macOS; Claude Code attaches to the MCP server for interactive strategy debugging and prompt structure testing.

### Risks

- **Nascent project**: v0.1.6 with March 2026 release — internal limit order state machine may contain edge-case bugs regarding order execution parity with live Polymarket
- **Dependency audit needed**: Transitive Python dependencies require verification for copyleft contamination

### Cemini significance

This is the highest-value Polymarket tool evaluated across all briefs. It provides the missing bridge between LLM strategy generation and safe forward-testing. Complements the existing Polymarket stack (py-clob-client, polymarket-mcp-server) with a simulation layer that doesn't exist in the current architecture.

[Source: Project Link Evaluation Brief 5_10.docx, URL 4]
