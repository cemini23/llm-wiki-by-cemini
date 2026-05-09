# hftbacktest Adoption — Microsecond-Tick Backtesting for Polymarket/Kalshi MM + Cross-Venue Arb

## Target

CeminiSuite (cemini-prod server-side Claude session)

## Summary

Adopt `hftbacktest` as Cemini's microsecond-tick backtesting substrate for prediction-market market-making (MM) parameter tuning + cross-venue arbitrage threshold tuning. Per the K31 Gemini DR eval (`@wiki/sources/5-5-moarrr-tool-eval.md` URL 15), hftbacktest is **Adopt-tier** and "ingests microsecond-level tick data — specifically Level-2 Market-By-Price and Level-3 Market-By-Order." It fills the **execution-resolution gap** in Cemini's existing backtest stack: yfinance EOD + FinanceToolkit GARCH-on-daily-bars cover daily/weekly resolution; Riskfolio-Lib covers portfolio-level optimization; nothing in the existing stack covers the queue-position / order-book-depth / latency-adjusted regime that MM and arb strategies actually live in.

This brief is the **sister to** `@briefs/2026-05-04_quant-libs-fastmcp-integration.md` (which covers daily-bar fundamentals via Riskfolio-Lib + FinanceToolkit + FinanceDatabase). Together they span the full backtest time-resolution stack.

## Background

Per K31 ingest 2026-05-06 (`@wiki/entities/tools/hftbacktest.md`), **Phase 0 verified 2026-05-08**:

| Property | Value |
|---|---|
| Repo | **[github.com/nkaz01/hftbacktest](https://github.com/nkaz001/hftbacktest)** — 4,015 ★, 780 forks, 30 contributors |
| License | **MIT** ✅ — verified against LICENSE file |
| Latest release | `rust-v0.9.4` / `py-v2.4.4` (Dec 10, 2025); PyPI maturity: **Production/Stable** |
| Stack | Python ≥3.11 + Rust core (76% Rust / 24% Python). Deps: `numpy>=2.0,<2.3`, `numba~=0.61`, `polars`, `matplotlib`, `holoviews` |
| Rust on Hetzner | **Not needed** — pre-built wheels on PyPI include compiled Rust backend. `pip install hftbacktest` ✅ |
| Data formats | Level-2 MBP + Level-3 MBO tick-by-tick; venue-agnostic ingestion |
| Distinguishing feature | Event-order correction algorithm (canonical primitive for latency-adjusted backtest) |

Why this is load-bearing for already-shipped Cemini work:

| Downstream consumer | Why hftbacktest is required |
|---|---|
| `@wiki/concepts/polymarket-market-making-architectures.md` | All 5 reference Polymarket MM impls (poly-market-maker, poly-maker, polymarket-market-maker, Polymarket Trading Bot v3.1, BTC-15-Minute-Trading-Bot) tune spread + inventory parameters via microstructure backtest |
| `@wiki/concepts/cross-venue-arbitrage-pattern.md` | Risk caveat #1 ("network latency between venues — windows close fast") — arb threshold tuning needs latency-adjusted backtest to set realistic profit-gating thresholds |
| `@briefs/2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md` | Tennis prediction-market live execution requires latency-adjusted entry timing |
| `@briefs/2026-05-05_polymarket-stack-adoption.md` | Order-placement strategy (which side to lean, which spread to quote) is parameterized off historical microstructure |

Per K31 eval (URL 15): "Highly specialized framework engineered for ultra-precise, high-frequency trading and market-making backtesting... ingests microsecond-level tick data—specifically Level-2 Market-By-Price and Level-3 Ma[rket-by-Order]." [Source: 5_5 moarrr links.docx URL 15]

## License posture

**Phase 0 verdict: MIT confirmed ✅** — verified against LICENSE file in repo root.

Per K31 eval, license was listed as "permissive (likely MIT or BSD-3-Clause)." Confirmed MIT. Clear to proceed under all 9 modes of the Cemini license-posture catalog (`@wiki/concepts/cemini-license-posture.md`).

No license-related blockers for adoption, code lift, or eventual IP-sale path.

## Architecture

```
cemini-prod (existing infrastructure)
├── agents/orchestrator.py
│   └── analyst nodes route historical-replay queries via Conductor
├── services/llm_analyst/
│   ├── backtest/
│   │   ├── riskfolio_runner.py            [unchanged — daily-bar portfolio backtest]
│   │   ├── financetoolkit_runner.py       [unchanged — daily-bar fundamentals]
│   │   ├── hftbacktest_runner.py          [NEW — microsecond-tick MM + arb backtest]
│   │   └── data_loaders/
│   │       ├── polymarket_mbp_loader.py   [NEW — Polymarket CLOB → MBP shape]
│   │       └── kalshi_mbp_loader.py       [NEW — Kalshi orderbook → MBP shape]
│   ├── conductor_client.py                [unchanged]
│   └── mcp_tools/
│       ├── backtest_tools.py              [EXTEND — new historical_replay tool surface]
│       └── ...
└── /opt/cemini/.env
    └── (no new secrets needed for backtest substrate)
```

The change is additive: `hftbacktest_runner.py` is a new substrate alongside the existing daily-bar runners. Conductor gains a `historical_replay` taxonomy class with FastMCP `@mcp.tool` decorators exposing the substrate to analyst nodes.

## What to build

### Phase 0 — Source audit (Explore subagent, ~30 min)

Per the K28+K30 Phase-0 audit pattern (3 clean rejections shipped — SwarmVault, PageIndex, Claude-OSINT):

1. Clone repo to `/tmp/hftbacktest-audit/`
2. **Verify license** matches the eval claim (LICENSE file vs eval claim — apply the 9-mode catalog above)
3. **Verify maturity** signals:
   - Stars / forks
   - Commits over last 90 days (active maintenance check)
   - Open issues count + age (bus-factor check)
   - Latest version + release cadence
   - PyPI / cargo / npm package name + install path
4. **Audit for the most-likely failure mode for HFT-backtester class**:
   - Hardcoded data-format assumption that locks out non-traditional venues (Polymarket CLOB / Kalshi orderbook are NOT traditional equity exchanges — verify the MBP/MBO ingest is venue-agnostic)
   - Compute footprint (microsecond-tick data is 10⁶× the volume of daily bars; Hetzner CPX31's 7 GB RAM + 75 GB disk envelope must handle realistic 6-month backtest windows)
   - Polars-friendliness (Cemini's existing data layer leans on Polars per `@CLAUDE.md` market-dataset conventions)
   - Whether Rust-core install requires `cargo` toolchain on Hetzner (Cemini-prod's Hetzner box doesn't currently have Rust per K28 leaf decision; npm/homebrew/PyPI wheels preferred)
5. **Compare against existing Cemini coverage** — confirm hftbacktest doesn't duplicate Riskfolio-Lib + FinanceToolkit (it shouldn't — different time resolution).
6. **Verdict gate**: GO / CONDITIONAL-GO / NO-GO. Record in `@wiki/entities/tools/hftbacktest.md`.

### Phase 1 — Sandbox replicate one Cemini backtest (~1-2 days)

Drop hftbacktest into `/tmp/hftbacktest-sandbox/`, replicate ONE specific Cemini backtest scenario end-to-end:

- **Target scenario**: Polymarket-Kalshi BTC 1h Bitcoin pricing arbitrage (per `@wiki/concepts/cross-venue-arbitrage-pattern.md` canonical entry pair)
- **Data inputs**: 30-day historical Polymarket CLOB snapshots + 30-day historical Kalshi orderbook snapshots (both adapter-shimmed into MBP shape)
- **Backtest output**: per-trade arb-attempt P&L, latency-adjusted fill probability, partial-fill-risk frequency
- **Compute envelope**: must fit Hetzner CPX31 (7 GB RAM, 75 GB disk). If it doesn't, fall back to a smaller window or NO-GO.
- **Comparison baseline**: compare to a manual SQL-over-Parquet replay (no microstructure simulation) to verify the framework's added value is meaningful for arb threshold tuning.

### Phase 2 — Production integration (~2-3 days)

- Move hftbacktest into Cemini's container build (`pyproject.toml` + `pip install hftbacktest==<pinned>` or equivalent)
- Implement `services/llm_analyst/backtest/hftbacktest_runner.py` with Cemini's existing AuditEntry / RoutingDecision types
- Implement `services/llm_analyst/backtest/data_loaders/polymarket_mbp_loader.py` + `kalshi_mbp_loader.py` adapter shims
- Wire Conductor: add `historical_replay` taxonomy class to `config.yaml` (per `@wiki/concepts/conductor-orchestrator.md` extension)
- Wire FastMCP `@mcp.tool` decorators in `services/llm_analyst/mcp_tools/backtest_tools.py`:
  - `replay_polymarket_kalshi_arb(window_days, threshold_bps)` → P&L + fill-rate + risk metrics
  - `replay_polymarket_mm(market_id, spread_bps, inventory_limit)` → P&L + queue-position metrics
  - `replay_kalshi_mm(market_id, spread_bps, inventory_limit)` → same
- Add JSONL audit-trail per `@briefs/2026-05-05_conductor-audit-trail-phase1.md` discipline (every backtest invocation produces an AuditEntry)

### Phase 3 — Strategy parameter tuning (downstream, optional)

Once Phases 0-2 are GO:
- Re-tune Polymarket MM spread/inventory parameters from `@briefs/2026-05-05_polymarket-stack-adoption.md` against backtested microstructure
- Re-tune cross-venue arb threshold from `@wiki/concepts/cross-venue-arbitrage-pattern.md` against latency-adjusted simulation
- Re-tune Klaassen-Magnus tennis-prediction-market entry timing from `@briefs/2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md`

Phase 3 is the payoff — it reduces parameter-uncertainty in already-shipped briefs.

## Risks and gating conditions

- **License-verification NO-GO**: if Phase 0 reveals AGPL-3.0 / GPL-3.0 / ELv2 / NO-LICENSE, this brief stops at Phase 0. Document NO-GO in `@wiki/entities/tools/hftbacktest.md` with eval-claim correction.
- **Compute footprint blowup**: Hetzner CPX31 has 7 GB RAM. Microsecond-tick data for a 6-month window across 2 venues × 100+ contracts may exceed memory budget. Phase 1 must verify before Phase 2 commits to integration. Fallback: smaller windows or single-venue scope.
- **Polymarket / Kalshi data-shape mismatch**: hftbacktest expects equity-style MBP data. Polymarket CLOB + Kalshi orderbook are binary-outcome contracts with different lifecycle semantics (resolution event, trading halt, etc.). The adapter shims (`polymarket_mbp_loader.py` / `kalshi_mbp_loader.py`) carry the schema risk. Phase 1 must validate the round-trip.
- **Rust toolchain dependency**: per `@wiki/entities/tools/git-rewind.md` open-questions discipline, Cemini-prod doesn't have Rust toolchain. If hftbacktest requires `cargo install`, Phase 0 should identify a pre-built wheel / PyPI distribution path.
- **Bus factor**: HFT-backtest tooling tends to have small maintainer counts. Pin version aggressively. If Phase 0 finds <5 maintainers and <90 days since last commit, flag elevated risk in `@wiki/entities/tools/hftbacktest.md`.
- **Coexistence with existing backtest substrates**: Riskfolio-Lib + FinanceToolkit are daily-bar; hftbacktest is microsecond-tick. They should NOT share the same `services/llm_analyst/backtest/` runner — keep them as parallel substrates with explicit `Conductor` taxonomy-class routing.

## Cross-references

- `@wiki/entities/tools/hftbacktest.md` — entity page (K31 Adopt-tier)
- `@wiki/sources/5-5-moarrr-tool-eval.md` URL 15 — origin Adopt-tier verdict
- `@wiki/concepts/polymarket-market-making-architectures.md` — primary downstream consumer (5 MM impls)
- `@wiki/concepts/cross-venue-arbitrage-pattern.md` — primary downstream consumer (Polymarket-Kalshi BTC arb)
- `@wiki/concepts/prediction-market-historical-analysis.md` — sibling concept (5-layer historical-data stack)
- `@briefs/2026-05-04_quant-libs-fastmcp-integration.md` — sister brief (daily-bar substrate; complementary time resolution)
- `@briefs/2026-05-05_polymarket-stack-adoption.md` — downstream consumer (MM parameter tuning)
- `@briefs/2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md` — downstream consumer (latency-adjusted entry timing)
- `@briefs/2026-05-05_conductor-audit-trail-phase1.md` — companion (AuditEntry discipline applies to backtest invocations)
- `@wiki/concepts/conductor-orchestrator.md` — `historical_replay` taxonomy class extension
- `@wiki/concepts/cemini-license-posture.md` — 9-mode license catalog (Phase 0 verdict gate)
- `@wiki/entities/tools/financetoolkit.md` — companion library (daily-bar fundamentals)
- `@wiki/entities/tools/riskfolio-lib.md` — companion library (portfolio optimization)

## Done when

- Phase 0 source audit complete + verdict recorded in `@wiki/entities/tools/hftbacktest.md`
- License verified against LICENSE file (one of MIT / BSD / Apache-2.0 / LGPL-clean)
- Phase 1 sandbox replication of Polymarket-Kalshi BTC arb backtest produces non-trivial output that materially differs from a naive SQL-replay baseline
- Phase 2 production integration: `services/llm_analyst/backtest/hftbacktest_runner.py` + 2 data-loader shims + 3 FastMCP `@mcp.tool` decorators
- Conductor `config.yaml` adds `historical_replay` taxonomy class
- AuditEntry JSONL discipline applied to all backtest invocations (per `@briefs/2026-05-05_conductor-audit-trail-phase1.md`)
- `@wiki/entities/tools/hftbacktest.md` updated from `[NEEDS VERIFICATION 2026-05-06]` → `[VERIFIED YYYY-MM-DD]` with deployment status
- One smoke test downstream: re-tune ONE parameter (e.g., cross-venue arb threshold) against the new backtest substrate and document the change in `@briefs/2026-05-05_polymarket-stack-adoption.md` Phase 3 OR `@wiki/concepts/cross-venue-arbitrage-pattern.md` Risk caveats section

## Sources

- [Source: `@wiki/sources/5-5-moarrr-tool-eval.md` URL 15] — K31 Gemini DR eval Adopt-tier verdict
- [Source: `@wiki/entities/tools/hftbacktest.md`] — entity page (NEEDS VERIFICATION 2026-05-06 tags pending Phase 0 resolution)
