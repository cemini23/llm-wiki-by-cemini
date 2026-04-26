---
title: "Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage"
type: source
tags: [pdf, ml-methods, graph-learning, fx, statistical-arbitrage, sortino, gnn, spatiotemporal, interest-rate-parity]
clusters: [ml-methods]
related:
  - entities/frameworks/langgraph.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
---

## Relations

- @entities/frameworks/langgraph.md — Cemini LLM orchestration framework; ML/agent-systems research context

## Raw Concept

- **Original title**: Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage
- **Author(s)**: Yoonsik Hong, Diego Klabjan (Northwestern University)
- **Type**: PDF (academic; CCS: Neural networks)
- **Location**: research for cemini/sort 9 4:3.pdf
- **Length**: 8p
- **Retrieved**: 2026-04-23
- **Read status**: read-skim
- **Primary cluster**: ml-methods
- **All clusters**: ml-methods

## Narrative

Two-step graph-learning framework for FX statistical arbitrage (FXSA) across currency triplets. Addresses two explicit gaps in prior work: (a) no GL method for FX-rate prediction (FXRP) that jointly leverages multi-currency and currency–interest-rate relationships via interest-rate parity (IRP); (b) prior FX-arb literature (cites [25, 26, 34]) ignores the time lag between price observation and trade execution — a look-ahead-bias problem the authors argue makes prior results "potentially inadmissible in practice."

**Step 1 — FXRP as edge-level regression on a spatiotemporal graph.** Nodes = currencies (features: interest rates); edges = FX pairs (features: FX rates). Edge-level regression predicts next-period FX rate. The graph structure encodes IRP directly: two currencies' IRs + FX rate form a triangular constraint.

**Step 2 — Stochastic optimization for FXSA with observation-execution lag.** A second graph (nodes = exchanges, edges = influence relationships) feeds into a projection + ReLU layer that enforces empirical arbitrage constraints. The FXRP output feeds in both as constraint parameters and as node features. The authors prove the resulting method satisfies empirical arbitrage constraints (not Hart-style no-arbitrage theorems, but bounded-deviation empirical versions).

**Reported results:** statistically significant MSE improvement on FX prediction; FXSA method achieves **+61.89% information ratio** and **+45.51% Sortino ratio** vs benchmark. The "sort" in the filename is Sortino — this is why the partition routed it to ml-methods.

Relevant to Cemini as a concrete precedent for: (1) edge-level regression on a financial relationship graph — directly portable to the Graph-Attentive MAPPO (arXiv:2511.00039) asset-graph architecture identified in `3-29-research-3.md`; (2) explicit observation-execution-lag modeling — should be lifted into Cemini backtests to avoid the look-ahead bias the paper flags; (3) Sortino-based performance reporting aligns with the DSR→DSoR migration prescribed in `rl-technical-audit-findings-3-9.md`. Honest limits: (a) 8-page paper, abstract-first read-skim; (b) "61.89% information ratio" and "45.51% Sortino" improvements are against a single benchmark of unspecified construction — could be a weak baseline; (c) FX triplet arbitrage is a well-mined space — edge cases and transaction-cost realism would need deeper inspection; (d) no public code repo referenced in the abstract.

## Key findings

- Two-step graph-learning FX statistical-arbitrage framework with spatiotemporal graph (nodes=currencies, edges=FX rates, IRs as node features).
- Step 1 is edge-level regression; step 2 is stochastic optimization with projection + ReLU constraint enforcement.
- Explicitly models observation-execution time lag — argues prior FX-arb literature is look-ahead-biased.
- Reported: +61.89% information ratio, +45.51% Sortino ratio over benchmark; statistically significant MSE improvement on FXRP.
- Proof of empirical-arbitrage-constraint satisfaction (not classic no-arb, but bounded-deviation version).
- Directly complementary to Graph-Attentive MAPPO thesis in `3-29-research-3.md` — same graph-learning + financial-graph-edges pattern.
- Sortino reporting aligns with Cemini's prescribed DSR→DSoR migration.

## Snippets

- **Abstract** — "In the first step, to capture complex multi-currency and currency–interest rate relationships, we formulate FXRP as an edge-level regression problem on a discrete-time spatiotemporal graph."
- **Abstract** — "our FXSA method… achieves a 61.89% higher information ratio and a 45.51% higher Sortino ratio than a benchmark."
- **§1** — "While the spot price and the actual trading price can differ due to the time lag between price observation and trade execution, such discrepancies have not been addressed in the existing literature… This omission renders prior methods potentially inadmissible in practice and subject to look-ahead bias."
