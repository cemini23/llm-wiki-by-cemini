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
maturity: draft
created: 2026-05-16
updated: 2026-05-16
phase_0_verdict: ADOPT (doc-level) 2026-05-16 — MIT verified in report; Phase-0 clone audit pending before cemini-prod integration
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
- License: **MIT** (per report)
- Stars / last commit / open issues: 138 / NOT FOUND / 2
- Stack: Python 3.11+ / PostgreSQL 15 / Redis 7 / Docker

## Narrative

**Polymarket Insider Tracker** is a surveillance and intelligence engine designed to unmask **"informed money"** before public market shifts. It bridges on-chain forensic analysis with order-book microstructure monitoring on a PostgreSQL 15 + Redis 7 stack.

Core detections:

- **Fresh Wallets** — accounts with fewer than 5 lifetime transactions that suddenly execute positions exceeding $1,000 (insider/sybil indicator), detected via Polygon RPC endpoints.
- **Sniper Clusters** — **DBSCAN clustering** identifies coordinated groups of wallets entering obscure, low-volume markets simultaneously, ahead of public news.
- **Funding-chain analysis** — traces capital origins back to centralized-exchange hot wallets (e.g. Binance), providing entity-resolution OSINT.
- **Liquidity-impact analysis** — flags trades consuming >2% of visible order-book depth.

**Cemini fit**: a mathematically robust anomaly-detection capability for the analyst-node prediction layer, and liquidity-impact metrics for backtesting frameworks. The stack mirrors the `/opt/cemini` market-data ingestion layer (Python/PostgreSQL/Redis). MIT clears the IP sale. Deployment belongs on **cemini-prod** — staged via adoption brief. The funding-chain analysis is cross-routed to cybersec for threat-actor financial profiling.

- `[NEEDS VERIFICATION 2026-05-16]` DBSCAN clustering latency overhead against real-time high-velocity Polymarket CLOB WebSocket feeds.
- `[NEEDS VERIFICATION 2026-05-16]` Phase-0 clone audit: confirm MIT LICENSE, dependency license cleanliness.

## Snippets

> "It utilizes Polygon RPC endpoints to detect 'Fresh Wallets' — accounts with fewer than five lifetime transactions that suddenly execute positions exceeding $1,000 ... it employs complex DBSCAN clustering algorithms to identify 'Sniper Clusters'." [Source: Tool Evaluation and Wiki Fit Analysis.docx — URL 6]
