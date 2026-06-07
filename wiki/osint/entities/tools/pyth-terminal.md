---
title: Pyth Terminal — public browse layer for Pyth price feeds
type: entity
tags: [entity, tool, oracle, market-data, pyth, k67, workflow]
keywords: [pyth-terminal, app-pyth-com, pyth-network, csv-export, metamorphicc, pyth-terminalcsv, prediction-market-verification, pyth-pro]
related:
  - sources/trading-posts-compilation-19-2026-06-07.md
  - concepts/pyth-pro-saas-build-patterns.md
  - sources/trading-posts-compilation-38-2026-05-26.md
  - entities/tools/chainlink-data-streams.md
  - entities/platforms/polymarket.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-26
updated: 2026-06-07
---

## Relations

- @sources/trading-posts-compilation-38-2026-05-26.md — K67 Post 28 review
- @entities/tools/chainlink-data-streams.md — alternate oracle path on Polymarket UpDown bots (BTC truth feed)
- @entities/platforms/polymarket.md — PM markets that may resolve against Pyth benchmarks
- @concepts/cemini-license-posture.md — prod redistribution / API terms gate

## Raw Concept

- **Terminal UI**: [app.pyth.com/explore](https://app.pyth.com/explore) — browse **3,000+** feeds (crypto, equities, FX, commodities), historical charts, benchmark overlays, free Pyth Pro trial key from browser [Source: [Pyth Terminal docs](https://docs.pyth.network/price-feeds/pro/pyth-terminal) (retrieved 2026-05-28)]
- **Local analyzer**: [metamorphicc/PythTerminalCSV](https://github.com/metamorphicc/PythTerminalCSV) — offline stats on exported CSV (log returns, drawdown, z-score moves, live TUI)
- **API**: Pyth Pro History API + laptop `.env` (`PYTH_*` / trial token) — **gitignored**; never commit keys

## Narrative

Pyth Terminal is an **evaluation and verification layer**, not a Cemini execution feed. Use it to inspect feed quality, publisher composition, and benchmark alignment **before** paying for Pyth Pro or wiring oracle prices into prod.

Polymarket-facing angle (K67 Post 28): Terminal + CSV sanity checks complement PM research; PM’s published Pro package includes metals, US equities, and commodities used in RWA-style markets [Source: [Pyth Pro × Polymarket](https://docs.pyth.network/price-feeds/pro/pyth-terminal) (retrieved 2026-05-28)].

### Which CSV to download (Cemini playbook)

**Rule:** export the feed that matches the **underlying your Polymarket market resolves on**, for the **same time window** you are analyzing (market open → resolution, plus ~24h buffer).

| If you are working on… | Download this feed first | Notes |
|------------------------|--------------------------|--------|
| BTC 15m / crypto Up-Down PM | **Crypto.BTC/USD** | Compare against `@entities/tools/chainlink-data-streams.md` truth-feed choice on Gustafsson-style bots |
| ETH / alt crypto PM | **Crypto.ETH/USD** | Sample path in PythTerminalCSV repo uses ETH 5m bars |
| SOL / HYPE / other crypto PM | **Crypto.SOL/USD**, **Crypto.HYPE/USD**, etc. | Match ticker to market text |
| US equity PM (NVDA, TSLA, …) | **Equity.US.NVDA/USD**, **Equity.US.TSLA/USD**, … | Polymarket Pro package lists SPY, QQQ, AAPL, NVDA, MSFT, AMZN, GOOGL, META, TSLA, COIN, HOOD, PLTR, … |
| Metals / commodities PM | **Metal.XAU/USD**, **Metal.XAG/USD**, WTI, Henry Hub, … | Same Polymarket package per Pyth docs |
| “Is Pyth worth Pro?” (generic) | **Crypto.BTC/USD** + one **Equity.US.SPY/USD** or **Metal.XAU/USD** | Two asset classes = enough to judge latency, gaps, benchmark overlay |

**Time range & bar size**

- **Intraday PM / short-dated crypto:** last **3–7 days**, **1m or 5m** bars (PythTerminalCSV sample `eth.csv` is **5m**).
- **Multi-day event markets:** last **30–90 days**, **1h or 1d** bars.
- **Regime / Hurst-style studies:** align window with your backtest (see `@concepts/monte-carlo-permutation-test-mcpt.md`).

**How to export (Terminal UI)**

1. Open [app.pyth.com/explore](https://app.pyth.com/explore) → search feed (e.g. `BTC/USD`).
2. Open feed detail → set chart **interval** (1m / 5m / 1h / 1d) and **date range** to cover your PM window.
3. Use **Export / Download CSV** on the chart (wording varies by UI revision).
4. If export is **OHLC** (`timestamp,open,high,low,close,volume`), either:
   - rename column **`close` → `price`** before running PythTerminalCSV, or
   - add a `price` column copied from `close` (analyzer requires `timestamp` + `price`, not full OHLC).

**API path (wired on laptop)**

- Set `PYTH_TERMINAL_API_KEY` in workspace `.env` (see `.local/pyth.env.example`; never commit).
- Export feed catalog from Terminal → e.g. `~/Desktop/pyth-feeds-YYYY-MM-DD.csv` (channel + `hermes_id` mapping).
- Run automated reports:

```bash
cd "OSINT WORKSPACE"
python3 scripts/pyth_feed_report.py --verify-key   # ping Pro /v1/live
bash scripts/run_pyth_feed_reports.sh              # → ~/Desktop/pyth-reports-<date>/
```

- **Pro History API** (`auto` / `--source pro`): `https://pyth.dourolabs.app/v1/{channel}/history` with `Authorization: Bearer $PYTH_TERMINAL_API_KEY`. Uses catalog `min_channel` + API symbol rules (crypto/metal: full `Crypto.BTC/USD`; equities: short ticker `NVDA`).
- **Fallback** (`--source benchmark`): `benchmarks.pyth.network` when no key or Pro error.
- Outputs per feed: `*-5m-7d.csv` (`timestamp,price`) + `*-report.json` (drawdown, z-moves, anomalies). Latest run: `~/Desktop/pyth-reports-2026-05-28/`.

Prod still needs explicit Pyth **terms** check before storing/redistributing series on Hetzner.

### PythTerminalCSV workflow (laptop)

```bash
git clone https://github.com/metamorphicc/PythTerminalCSV.git
cd PythTerminalCSV
node main.ts --input /path/to/btc-usd.csv --summary-only --out report.json
node main.ts --input /path/to/btc-usd.csv --live --refresh 2   # optional live TUI
```

Store exports under `.local/` or `research to be indexed/` (transient), not wiki git.

### Phase-0 audit — Pyth Terminal (UI)

| Check | Result |
|-------|--------|
| Role | Browse + chart + trial API key; not execution |
| Cemini fit | **CONDITIONAL-GO (workflow / oracle eval)** |
| Prod | Do not treat Terminal CSV as signed oracle input without Pro + compliance review |

### Phase-0 audit — PythTerminalCSV (2026-05-28)

Repo: [metamorphicc/PythTerminalCSV](https://github.com/metamorphicc/PythTerminalCSV)

| Check | Result |
|-------|--------|
| License | **None** (no `LICENSE` file) |
| Maturity | ~2★, single `main.ts`, no README/tests |
| Function | Parses `timestamp` + `price` CSV → JSON report + optional live dashboard |
| Cemini fit | **CONDITIONAL-GO (workflow only)** — use repo as reference CLI or reimplement stats in `scripts/`; **NO-GO** as git dependency |

**Verdict:** Keep Terminal; treat PythTerminalCSV as **optional local helper**, not an adopted package.

## Snippets

> "See the data before you pay for it. That's the whole pitch." [Source: Posts.docx K67 Post 28, @morpphhhaw]

> Polymarket Pro package (via Terminal docs): metals (XAU, XAG), equities (SPY, QQQ, NVDA, …), commodities (WTI, Henry Hub). [Source: https://docs.pyth.network/price-feeds/pro/pyth-terminal (retrieved 2026-05-28)]
