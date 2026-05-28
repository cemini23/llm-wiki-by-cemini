---
title: Equity fair-value evaluation — multi-source intrinsic vs market
type: concept
tags: [concept, equities, valuation, fair-value, brain, fmp, cemini-prod, k75]
keywords: [equity_valuation, fair_value_usd, value_gap_pct, fmp_dcf, fmp_consensus, llm_analyst, brain_playbook_v2, undervalued, overvalued, weighted-synthesis]
related:
  - concepts/pnl-attribution-versioning.md
  - concepts/production-trading-blind-spots.md
  - entities/tools/financetoolkit.md
  - entities/infrastructure/yfinance.md
  - concepts/regime-conditioned-evaluation.md
  - entities/infrastructure/cemini-stack.md
  - concepts/trading-dashboard-api-wiring.md
  - entities/tools/fp-dcf.md
  - entities/tools/value-investing-tools.md
maturity: validated
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/pnl-attribution-versioning.md — `brain_playbook_v2` versions equity logic that consumes fair-value gaps
- @concepts/production-trading-blind-spots.md — valuation rule changes need version bumps (row 11)
- @entities/tools/financetoolkit.md — standardized ratio/GARCH layer; complementary to FMP fair-value paths
- @entities/infrastructure/yfinance.md — EOD fallback per polygon-doctrine; not primary for intraday fair value
- @concepts/regime-conditioned-evaluation.md — gap thresholds may need regime conditioning [TENTATIVE]
- @entities/infrastructure/cemini-stack.md — `brain`, `edgar_pipeline`, `finnhub_calendar`, Redis `intel:*`
- @concepts/trading-dashboard-api-wiring.md — conviction/screener APIs surface related signals
- @entities/tools/fp-dcf.md — K75 Phase-0 REFERENCE ONLY (no LICENSE)
- @entities/tools/value-investing-tools.md — K75 Phase-0 REJECT adopt (README MIT, no LICENSE file)

## Raw Concept

What prompted this page: 2026-05-28 deploy of `core/equity_valuation.py` on cemini-prod — bot computes weighted fair value per ticker, derives `value_gap_pct`, labels over/under/fair, publishes to Redis, and feeds brain sleeve classification (`core/brain_pnl_attribution.py`). Distinct from prediction-market "fair value" (microstructure lag) in @concepts/polymarket-updown-bot-taxonomy.md.

## Narrative

### Question answered

For each equity symbol: **what is fair intrinsic value (USD/share), how far is market price from that, and is the name over- or under-valued?** Output drives fundamental score, Redis intel bus, and hold vs tactical sleeve inference — not a standalone auto-trade without brain gates.

### Prod pipeline (`core/equity_valuation.py`)

```
market_price (caller)
    → gather_valuation_evidence()
        → FMP stable API: consensus target, DCF, key metrics TTM
        → derived: forward EPS × trailing P/E, conservative P/E re-rate
        → intel:llm_signal:{SYM} fair_value_usd (LLM analyst)
        → intel:earnings_calendar context
        → edgar_filings_log (recent forms)
        → wiki RAG snippet (librarian context length)
        → intel:equity_fair_value:{SYM} cache read
    → synthesize_fair_value()  # weighted average of candidates
    → value_gap() → value_gap_pct
    → gap_label() → undervalued | modestly_* | fairly_valued | overvalued
    → IntelPublisher → intel:equity_fair_value:{SYM} (TTL 3600s)
```

**Candidate weights (default)**:

| Source | Weight | Role |
|--------|--------|------|
| `fmp_consensus` | 0.32 | Analyst target consensus/median |
| `fmp_dcf` | 0.28 | FMP discounted cash flow |
| `fmp_forward_eps_x_pe` | 0.22 | Forward EPS × current P/E |
| `fmp_pe_rerate` | 0.12 | Conservative fair P/E band |
| `llm_analyst` | 0.15–0.25 | Scales with LLM conviction |
| `intel_cache` | 0.05 | Short TTL reuse |

Weights are implicit in code — changing them is a **logic version bump** for `brain_equity`.

**Gap labels**:

| `value_gap_pct` | Label |
|-----------------|-------|
| ≥ +15% | `undervalued` |
| ≥ +5% | `modestly_undervalued` |
| ≤ −10% | `overvalued` |
| ≤ −5% | `modestly_overvalued` |
| else | `fairly_valued` |

**Fundamental score mapping**: `value_gap_to_fundamental_score()` maps gap to [0,1] for ensemble inputs.

### LLM integration

`services/llm_analyst/prompt_builder.py` requests structured output including `fair_value_usd`. `_read_llm_fair_value()` ingests `intel:llm_signal:{symbol}` — LLM is one candidate, not sole truth.

### Sleeve attribution (`core/brain_pnl_attribution.py`)

Sleeve rules (`value_gap_inferred` mode) use env thresholds:

- `BRAIN_CORE_VALUE_GAP_MIN` (default 12%) → core hold
- `BRAIN_SATELLITE_VALUE_GAP_MIN` (default 4%) → satellite hold
- `BRAIN_OVERVALUED_GAP` (default −6%) → overvalued handling
- Signals: fair value, FMP paths, earnings, EDGAR, wiki, hold-duration fallback

Optional legacy symbol-list override via `BRAIN_SLEEVE_USE_SYMBOL_LISTS` (off by default).

### Distinction from wiki FinanceToolkit path

@entities/tools/financetoolkit.md — 150 standardized metrics, GARCH/VaR, DuPont — **calculation library** for analyst MCP tools. `equity_valuation.py` — **prod runtime synthesizer** with FMP + intel bus + sleeve hooks. Triangulation pattern aligns with finance-skills company-valuation (DCF + relative + blend) but prod implementation is FMP-weighted, not full tri-method report.

### External reference implementations (Phase-0 complete 2026-05-28)

| Repo | Phase-0 verdict | Notes |
|------|-----------------|-------|
| @entities/tools/fp-dcf.md | **REFERENCE ONLY** | No LICENSE; steal JSON contract shape only |
| @entities/tools/value-investing-tools.md | **REJECT Adopt** | README MIT, no LICENSE file; steal 3-scenario DCF pattern in prod |
| @entities/tools/financetoolkit.md | MIT Adopt-tier (eval) | Complementary metrics MCP layer |

### Operational cautions

1. **FMP_API_KEY required** — without it, only LLM/cache/wiki paths run; notes include `FMP_API_KEY_missing`.
2. **Data freshness** — no automatic stale-FMP circuit breaker yet [NEEDS VERIFICATION 2026-05-28].
3. **Version discipline** — threshold or weight changes → bump `brain_playbook_v2` successor in @concepts/pnl-attribution-versioning.md.
4. **Not PM fair value** — do not apply gap math to Kalshi/Polymarket contracts without domain-specific models.

## Snippets

> "Multi-source fair value vs market price (FMP, EDGAR, earnings, wiki, LLM)." [Source: cemini-prod `core/equity_valuation.py` module docstring, retrieved 2026-05-28]

> `"signals": ["fair_value_usd_vs_market_price", "value_gap_pct", "fmp_consensus", "fmp_dcf", ...]` [Source: cemini-prod `core/brain_pnl_attribution.py` `attribution_rule_metadata()`, retrieved 2026-05-28]

## Dead Ends

- **Single-method DCF only** — prod explicitly blends; one source dominates error.
- **Yahoo as primary fair-value feed** — polygon-doctrine; FMP stable API is prod path.
