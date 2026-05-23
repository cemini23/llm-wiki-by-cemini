---
title: "Polymarket Insider Tracker — on-chain 'informed money' surveillance"
type: entity
tags: [tool, prediction-markets, polymarket, on-chain-forensics, surveillance, anomaly-detection, adopt, k49]
keywords: [polymarket-insider-tracker, informed-money, fresh-wallet-detection, dbscan-clustering, sniper-clusters, funding-chain-analysis, polygon-rpc, postgresql, redis, mit-license]
related:
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
  - entities/tools/polyterm.md
  - entities/tools/arkham-intelligence.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/prediction-market-information-leakage-score.md
  - sources/arxiv-foresightflow-ils-polymarket-2605.00493.md
  - sources/arxiv-polymarket-ils-population-scale-2605.00459.md
maturity: draft
created: 2026-05-16
updated: 2026-05-23
phase_0_verdict: NO-GO 2026-05-16 — no LICENSE file in repo; GitHub reports licenseInfo=null. Code is substantive (real DBSCAN + funding-chain), but absent an explicit license the default is all-rights-reserved — incompatible with the IP-sale-bound proprietary stack. Re-audit only if upstream adds an OSI license file.
---

## Relations

- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — evaluated in the v3-iteration eval (Adopt tier, Cemini-financial primary fit)
- @entities/tools/polyterm.md — sibling surveillance tooling; complementary (order-flow vs on-chain forensics)
- @entities/tools/arkham-intelligence.md — sibling blockchain-analytics tool; both trace wallet funding chains for entity resolution
- @concepts/polymarket-microstructure-findings.md — informed-money detection is a microstructure-edge finding
- @cybersecurity-wiki/concepts/blockchain-security.md — cross-wiki: funding-chain analysis (tracing wallets to CEX hot wallets) feeds threat-actor financial profiling

## Raw Concept

Promoted from the 2026-05-16 "Tool Evaluation and Wiki Fit v3 Iteration" 46-repo eval. Tier: **Adopt**. Primary fit: Cemini-financial. Cross-route: cybersecurity-wiki (blockchain-security / threat-actor financial profiling).

- URL: https://github.com/pselamy/polymarket-insider-tracker
- License: **NONE** — no LICENSE file in repo; GitHub `licenseInfo: null`. README badge/link claim MIT but the file they point to does not exist (audit 2026-05-16). Eval-claimed MIT is **unverified / contradicted**.
- Stars / last commit / open issues: 139 / 2026-04-11 / 2 (audit 2026-05-16; eval claimed 138 / NOT FOUND / 2)
- Stack: Python 3.11+ / PostgreSQL 15 / Redis 7 / Docker

## Narrative

**Polymarket Insider Tracker** is a surveillance and intelligence engine designed to unmask **"informed money"** before public market shifts. It bridges on-chain forensic analysis with order-book microstructure monitoring on a PostgreSQL 15 + Redis 7 stack.

Core detections:

- **Fresh Wallets** — accounts with fewer than 5 lifetime transactions that suddenly execute positions exceeding $1,000 (insider/sybil indicator), detected via Polygon RPC endpoints.
- **Sniper Clusters** — **DBSCAN clustering** identifies coordinated groups of wallets entering obscure, low-volume markets simultaneously, ahead of public news.
- **Funding-chain analysis** — traces capital origins back to centralized-exchange hot wallets (e.g. Binance), providing entity-resolution OSINT.
- **Liquidity-impact analysis** — flags trades consuming >2% of visible order-book depth.

**Cemini fit**: a mathematically robust anomaly-detection capability for the analyst-node prediction layer, and liquidity-impact metrics for backtesting frameworks. The stack mirrors the `/opt/cemini` market-data ingestion layer (Python/PostgreSQL/Redis). MIT clears the IP sale. Deployment belongs on **cemini-prod** — staged via adoption brief. The funding-chain analysis is cross-routed to cybersec for threat-actor financial profiling.

- `[NEEDS VERIFICATION 2026-05-16]` DBSCAN clustering latency overhead against real-time high-velocity Polymarket CLOB WebSocket feeds. (Unresolved — Phase-0 is inspect-only, no execution; would need a runtime benchmark.)
- `[RETRACTED 2026-05-16]` "Phase-0 clone audit: confirm MIT LICENSE." Audit done — there is **no LICENSE file** and GitHub reports `licenseInfo: null`. The MIT claim is contradicted, not confirmed. See Phase-0 Audit section below.

## Phase-0 Audit (2026-05-16)

Clone-and-inspect audit per CLAUDE.md § "Phase-0 audit pattern". Repo cloned to `/tmp/insider-tracker-audit/` (shallow, depth 50). No execution.

**License — FAIL (the deciding finding).** There is **no LICENSE file** anywhere in the repository. GitHub's API returns `licenseInfo: null`. The README carries an `[![License: MIT]]` shields badge and a `## License` section stating "MIT License - see [LICENSE](LICENSE) for details" — but the linked `LICENSE` file does not exist. `pyproject.toml` declares no `license` field either. Under copyright law, source published with no license grant defaults to **all rights reserved**: no right to use, modify, or redistribute. For an IP-sale-bound proprietary stack this is a hard blocker — adopting it would mean shipping unlicensed third-party code in a saleable asset. The eval's "License: MIT (per report)" was a documentation artifact (README badge), not a verified grant.

**Dependency license scan — clean (moot given the above).** `pyproject.toml` lists 14 runtime deps (py-clob-client, web3, httpx, redis, sqlalchemy, alembic, pydantic, pydantic-settings, python-dotenv, websockets, prometheus-client, aiohttp, scikit-learn, numpy) — all standard permissive (MIT / BSD / Apache-2.0 / PSF) PyPI packages. A copyleft grep (`gpl|agpl|lgpl|mpl|epl`) over the 585 KB `uv.lock` returned zero matches. No GPL/AGPL transitive contamination. This does not rescue the verdict — the project's *own* missing license is the blocker.

**Code substance — real, NOT vaporware.** 37 source modules under `src/polymarket_insider_tracker/`, layered ingestor → detector → profiler → alerter → storage with a `pipeline.py` orchestrator. `detector/sniper.py` is a genuine implementation: imports `sklearn.cluster.DBSCAN`, builds a 3-feature matrix (normalized market hash, entry-delta hours, log-normalized position size), runs `DBSCAN(eps, min_samples, metric="euclidean")`, post-processes labels into clusters with a weighted confidence score (0.3·size + 0.4·speed + 0.3·overlap). `profiler/funding.py` (359 lines) traces USDC transfers backward via `web3.AsyncWeb3` with a max-hop limit, terminating at known entities; `profiler/entities.py` defines a CEX registry (Binance, Coinbase, Kraken, OKX, KuCoin, Bybit, Crypto.com) and bridge classification — funding-chain-to-CEX-hot-wallet tracing is real. `detector/fresh_wallet.py` enforces the claimed thresholds ($1,000 min trade, nonce/lifetime checks). A `tests/` tree mirrors the source layout. All four eval-claimed detections are implemented as described.

**Maintenance health — single-author, stalled.** Created 2026-01-04, last push 2026-04-11 (~5 weeks before audit). Effectively one author: ~all commits are "Patrick Selamy" (pselamy); one outside contributor ("axel-claw") landed a single fix (#91). Commit history shows long churn loops — e.g. PRs #63–#88 are ~25 near-identical "fix: resolve broken alembic migrations" / "ruff UP042" commits, a sign of CI-thrash rather than feature progress. 2 open issues (matches eval). Bus-factor 1; no release tag (`version = "0.1.0"`, pre-release).

**Comparison vs existing Cemini coverage.** Sibling tools `@entities/tools/polyterm.md` (order-flow surveillance) and `@entities/tools/arkham-intelligence.md` (wallet funding-chain entity resolution) already cover adjacent ground. Insider-tracker's distinct contribution is the DBSCAN sniper-cluster detector, which Cemini does not currently have — but that single module (~470 lines) is not worth importing an unlicensed, single-author, pre-release dependency.

**Verdict — NO-GO.** Disqualified on license alone: no LICENSE file = all-rights-reserved = cannot ship inside an IP-sale-bound proprietary stack. Secondary concerns (bus-factor 1, pre-release, stalled, CI-thrash history) reinforce it. The code is real and the DBSCAN approach is sound, so the detection *technique* is worth borrowing as a documented pattern (clean-room reimplementation), but the **repository itself is not adoptable**. Re-audit only if upstream adds an OSI-approved LICENSE file and reaches a tagged release.

## Snippets

> "It utilizes Polygon RPC endpoints to detect 'Fresh Wallets' — accounts with fewer than five lifetime transactions that suddenly execute positions exceeding $1,000 ... it employs complex DBSCAN clustering algorithms to identify 'Sniper Clusters'." [Source: Tool Evaluation and Wiki Fit Analysis.docx — URL 6]
