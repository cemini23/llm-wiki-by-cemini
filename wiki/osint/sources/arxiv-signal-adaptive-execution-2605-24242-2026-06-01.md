---
title: "Explicit signal-adaptive sequential optimal execution quotes (2605.24242)"
type: source
tags: [source, arxiv, quant-finance, market-microstructure, execution, k92]
keywords: [optimal execution, limit order book, quoting, CARA, inventory risk, signal-adaptive]
related:
  - concepts/sequential-optimal-execution-quoting.md
  - concepts/market-microstructure.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - sources/arxiv-alphaforgebench-2602-18481-2026-06-01.md
maturity: draft
read_status: read
created: 2026-06-01
updated: 2026-06-01
clusters: [quant-finance, market-microstructure]
---

## Relations

- @concepts/sequential-optimal-execution-quoting.md — synthesis hub
- @sources/arxiv-alphaforgebench-2602-18481-2026-06-01.md — K92 pair (LLM research vs execution math)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Explicit Signal-Adaptive Sequential Optimal Execution Quotes |
| **Author** | Fenghui Yu (TU Delft) |
| **Type** | PDF (arXiv q-fin.TR) |
| **arXiv ID** | 2605.24242 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2605.24242-pdf-explicit-signal-adaptive-sequential-optimal.pdf` |
| **Retrieved** | 2026-06-01 |
| **Read status** | read (abstract + introduction) |

## Narrative

K92 daily-digest fetch. Unifies **metaorder scheduling** (Almgren–Chriss style) with **micro-level limit-order quoting**: trader chooses quote paths over a horizon; fills are controlled jump processes with quote-dependent intensity. Four criteria (expected wealth ± inventory penalty, CARA ± penalty) reduce to **explicit triangular finite-dimensional solutions** — closed-form value functions and optimal quotes.

**Cemini relevance:** theoretical backing for **signal-adaptive LP/quoter modules** (world-cup-bot quoter, PM maker). Gemini eval flagged `sedemmler/WagerBrain` as steal-from for “module 3 (quoter)” — this paper is the academic counterpart for inventory + signal + fill-risk quoting, not venue-specific.

## Snippets

> "Rather than separating the scheduling of a metaorder from the placement of its individual child orders, we study an integrated sequential execution problem." [Source: arxiv-2605.24242.pdf, §1]

> "All four problems reduce to a triangular finite-dimensional structure which can be solved explicitly." [Source: arxiv-2605.24242.pdf, Abstract]

## Dead Ends

- Direct paste of formulas into prod without empirical calibration on PM/Kalshi LOB data — paper is equity LOB theory; venue transfer is `[TENTATIVE]`.
