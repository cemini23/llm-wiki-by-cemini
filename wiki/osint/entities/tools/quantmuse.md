---
title: "QuantMuse — Python+C++17 Quantitative Trading System"
type: entity
tags: [tool, quant-finance, rejected, no-go, cosmetic-cpp, factor-analysis]
keywords: [QuantMuse, factor analysis, momentum, value, volatility, VaR, CVaR, C++ core engine, low-latency, MIT, NO-GO]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/quant-finance.md
  - concepts/market-microstructure.md
maturity: validated
created: 2026-05-10
updated: 2026-05-10
phase_0_audit: NO-GO (2026-05-10)
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 12)
- `@concepts/quant-finance.md` — factor analysis + risk metrics relevant here
- `@concepts/market-microstructure.md` — C++ order-routing engine targets low-latency execution
- `@concepts/cemini-license-posture.md` — MIT, IP-sale clean

## Raw Concept

QuantMuse advertised itself as a production-ready quantitative trading system combining Python factor analysis + ML with a compiled C++17 "Core Engine" for low-latency order routing. **Phase-0 audit 2026-05-10 revealed the C++ engine is cosmetic** — pybind11-wrapped Python with 100ms `std::this_thread::sleep_for` loops in `main.cpp`. VaR/CVaR is trivial `np.percentile(returns, 5)` — equivalent to (not better than) Cemini's existing scipy code.

- **Repo**: `github.com/0xemmkty/QuantMuse`
- **License**: MIT [CONFIRMED 2026-05-10] — top-level LICENSE clean
- **Stack**: Python + thin C++17 wrapper (pybind11 embeds Python into the "core engine")
- **Maturity**: **POOR** — 9 commits total, 0 tags, last push 10 months pre-audit, no CI/CD, no test suite results
- **Data sources**: Yahoo + Alpha Vantage adapters (NOT Alpaca WebSockets as claimed)
- **Built-in**: Strategy schema validation exists, but no backtest results / no robustness metrics / no cold-start data
- **LLM orchestration**: LangChain (36KB across `langchain_agent.py` + `llm_integration.py`)

## Narrative

The K36 source brief evaluated QuantMuse as the highest-impact Cemini-prod Adopt candidate. Phase-0 audit overturned that verdict.

### Phase-0 audit findings (2026-05-10) — **NO-GO** ❌

The C++ engine is the entire value proposition in the original brief, and the audit found it does not deliver:

1. **Architecture is toy-shaped**: `TradingEngine` in `main.cpp` is a demo class with `std::this_thread::sleep_for(std::chrono::milliseconds(100))` loop — disqualifying for any sub-ms latency claim. No real multi-threading for concurrent order handling; naive sequential signal processing.
2. **Data flow is Python-over-C++**: `data_loader.cpp` embeds pybind11 to call Python fetchers (`YahooFetcher`, `BinanceFetcher`). WebSocket subscription is a callback to Python (`fetcher_.attr("start_websocket")`), not native C++ socket handling. Latency is still bound by Python GIL round-trips.
3. **Order executor is stub**: no order-submission logic, no exchange API connection, no retry/timeout/partial-fill handling.
4. **Risk math is no better than Cemini's existing**: VaR/CVaR is `np.percentile(returns, 5)` in `performance_analyzer.py` — same one-liner Cemini already has via scipy. Zero incremental value.
5. **Maturity poor**: 9 commits total, 0 release tags, last push 10 months pre-audit. No CI/CD pipeline. Build untested on Debian 12 / Alpine.
6. **No Hyperliquid adapter**: confirmed absent. Only Yahoo + Alpha Vantage + python-binance.
7. **LangChain strip cost**: ~36KB across two files; not deeply embedded but adds dependency-management overhead Cemini doesn't need.

**Verdict**: NO-GO. The C++ "core engine" is cosmetic, the strategies are real-but-untested template stubs, and the risk math is equivalent to Cemini's existing scipy code. Adopting QuantMuse adds maintenance burden (CMake build, pybind11 install, LangChain pins) for zero net capability gain.

### Recommendation

**Pass.** Reallocate engineering effort to a native Alpaca/Hyperliquid WebSocket adapter in Cemini's existing Python+FastMCP stack. If sub-ms execution latency ever becomes operationally required (not yet demonstrated), the better path is QuantLib (battle-tested, MIT) or a clean Rust/C++ adapter built in-house. QuantMuse is a distraction.

### Anti-pattern caught

The K36 source brief asserted "production-ready quantitative trading system" with "compiled C++17 Core Engine". The README and `core/` directory structure support that framing superficially — but the actual implementations are template/demo code. **Lesson**: Phase-0 audits must read source files, not directory structure or README claims, when verifying performance-critical adoptions.

[Source: Evaluating Code for Trading Stacks.docx, URL 12]
[Audit: Phase-0 Explore agent, 2026-05-10 — NO-GO]
