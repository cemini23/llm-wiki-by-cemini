---
title: prediction-market-analysis — Jon Becker's Polymarket + Kalshi dataset & analysis framework
type: entity
tags: [entity, tool, dataset, prediction-markets, polymarket, kalshi, backtest-data, adopt-eligible, k52]
keywords: [prediction-market-analysis, jon-becker, polymarket-dataset, kalshi-dataset, trade-history, parquet, mit-license, backtest-data, favorite-longshot]
related:
  - sources/x-posts-quant-oss-polymarket-bots-2026-05.md
  - concepts/prediction-market-statistical-arbitrage.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/prediction-market-historical-analysis.md
  - concepts/favorite-longshot-bias.md
  - sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md
maturity: validated
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/x-posts-quant-oss-polymarket-bots-2026-05.md — Post 4 (@ridark_eth) advertised this repo; this page records the verified reality (which differs materially from the post)
- @concepts/prediction-market-statistical-arbitrage.md — the dataset is a real backtest substrate for Method 1 (cointegration on trade/mid prices); it does **not** support Method 2 (no L2 order book)
- @concepts/cross-venue-arbitrage-pattern.md — the repo's `analysis/comparison/` scripts are cross-venue Polymarket↔Kalshi analyses, directly relevant to arb threshold-tuning
- @concepts/prediction-market-historical-analysis.md — historical price-divergence statistics; this dataset is a concrete source for them
- @concepts/favorite-longshot-bias.md — the repo ships FLB-style analyses (`win_rate_by_price`, `longshot_volume_share_over_time`, `mispricing_by_price`)

## Raw Concept

What prompted this page: K52 Post 4 (@ridark_eth) advertised `github.com/Jon-Becker/prediction-market-analysis` as the backtest sandbox for a cross-market statistical-arbitrage strategy. The source page flagged the repo `[NEEDS VERIFICATION]`. This page records the **2026-05-18 verification** — GitHub API + a Phase-0 clone of the code (no dataset download) — which both confirmed the repo is real and showed Post 4 materially misrepresents it.

## Narrative

### What it actually is — verified

`Jon-Becker/prediction-market-analysis` — **MIT license** (confirmed in-repo, not just the GitHub API), **~3,378★**, last pushed **2026-05-09** (actively maintained). Author Jon Becker is a known developer (heimdall-rs). A framework for **collecting, storing, and analyzing** prediction-market data, shipping "the largest publicly available dataset of Polymarket and Kalshi market and trade data."

- **Dataset** — `data.tar.zst`, **36 GiB compressed**, hosted on Cloudflare R2 (`s3.jbecker.dev/data.tar.zst`), pulled via `make setup`. Contents: `kalshi/{markets,trades}` and `polymarket/{blocks,markets,trades}`.
- **Code** — `indexers/` (Kalshi API + Polymarket API/blockchain collectors) + `analysis/` (per-venue + `comparison/` cross-venue scripts) + `common/`. Parquet storage, `uv`-managed, Python 3.9+. Clean dependency set (pandas, pyarrow, duckdb, scipy, web3, kalshi-python, polymarket-py). Repo ~2 MB code-only.
- The shipped analyses are **trade-level / calibration / favorite-longshot** studies: `win_rate_by_price`, `maker_vs_taker_returns`, `calibration_deviation_over_time`, `mispricing_by_price`, `vwap_by_hour`, `returns_by_hour`, `longshot_volume_share_over_time`.

### What Post 4 got wrong — `[RETRACTED]` the L2 claim

Post 4 described this repo as containing **"Full L2 order book snapshots (up to 20 levels deep) sampled at 100ms intervals"**, **"850 million state updates"**, a **55 GB** dataset, with setup steps `git clone …/prediction-market-analysis && cd prediction-market-arbitrage`, `make download-ob`, `orderbooks_l2.tar.zst`, `ls data/snapshots/polymarket/`.

Verification shows **none of that matches**:
- The dataset is **trades + market metadata**, *not* L2 order-book snapshots. There is no `snapshots/` directory and no order-book depth data — trade history is collected "via API and blockchain."
- Size is **36 GiB compressed**, not "55 GB" / "39 GB" (Post 4 itself was internally inconsistent).
- The `cd prediction-market-arbitrage` target is a **404** — no such repo exists.
- The real Makefile target is `make setup` (not `make download-ob`); the archive is `data.tar.zst` (not `orderbooks_l2.tar.zst`).

Conclusion: **the repo is real, MIT, and valuable — but Post 4 fabricated the L2/HFT specifics** on top of it. The author of Post 4 evidently did not run the repo. This is a documented case of an X post dressing a genuine project in invented detail to make a methodology section sound backable.

### Cemini posture

- **Adopt-eligible (server-side).** MIT — fully clean. The dataset is a genuine resource for Cemini's prediction-market backtesting: cross-venue Polymarket↔Kalshi trade-price divergence stats (the `comparison/` analyses) feed @concepts/prediction-market-statistical-arbitrage.md **Method 1** (cointegration / OU calibration on trade or mid prices) and @concepts/cross-venue-arbitrage-pattern.md threshold-tuning.
- **Does not support Method 2.** No L2 order book → no order-book-imbalance / micro-price backtesting from this dataset. If Method-2 work is ever scoped, Cemini must record its own L2 snapshots (the @0x_Punisher 6-layer websocket playbook is the path — see @concepts/polymarket-bot-architecture.md).
- **Server-side, not laptop.** The 36 GiB dataset belongs on `cemini-librarian` (raw-data layer), not the laptop. Adoption flows through the K52 `cemini-prod` brief. The Phase-0 code audit was done locally (clone to `/tmp`, no dataset download).
- **Phase-0 verdict: GO** — license MIT (in-file verified), maturity strong (3.4k★, active), deps clean, no failure-mode red flags for a data/analysis framework.

## Snippets

> "A framework for collecting and analyzing prediction market data, including the largest publicly available dataset of Polymarket and Kalshi market and trade data." [Source: github.com/Jon-Becker/prediction-market-analysis README (retrieved 2026-05-18)]

> "Download and extract the pre-collected dataset (36GiB compressed): `make setup` — This downloads `data.tar.zst` from Cloudflare R2 Storage and extracts it to `data/`." [Source: github.com/Jon-Becker/prediction-market-analysis README (retrieved 2026-05-18)]
