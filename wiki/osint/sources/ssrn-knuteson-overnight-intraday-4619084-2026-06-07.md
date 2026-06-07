---
title: "Nothing to See Here — Knuteson overnight/intraday anomaly paper (SSRN 4619084)"
type: source
tags: [source, ssrn, market-microstructure, satire, manipulation]
keywords: [knuteson, overnight-returns, intraday-returns, market-manipulation, nikkei, sse]
related:
  - concepts/knuteson-overnight-intraday-anomaly.md
  - concepts/market-microstructure.md
maturity: draft
read_status: skimmed
created: 2026-06-07
updated: 2026-06-07
clusters: [market-microstructure, quant-finance]
---

## Relations

- @concepts/knuteson-overnight-intraday-anomaly.md — synthesized takeaway

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Nothing to See Here: How to Say It When You Need to |
| **Author** | Bruce Knuteson |
| **SSRN** | 4619084 |
| **sha256** | `06cacab58993d597fb1fba73a958eaf96c3260d597d5fc2b4edf245b12c54ec3` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/ssrn-4619084.pdf` |
| **Retrieved** | 2026-06-07 |
| **Read status** | skimmed (intro + figure methodology; 224 plots cited) |

## Narrative

Satirical research paper documenting **decades-long suspicious overnight vs intraday return patterns** across global indices and single stocks (Nikkei 225, SSE 50, CAC/DAX/FTSE constituents, Nifty 50, etc.). Uses Yahoo Finance data; code public per author.

Core empirical claim: many names show **large positive overnight returns** paired with **negative or flat intraday returns** over long windows — patterns the author argues persist with little public fuss. Paper interleaves:

1. **"Nothing to see here"** reassurance examples (figures 3–10, six pages of plots).
2. **"How to say it"** — rhetorical techniques (Financial Times column cited) for dismissing incriminating evidence.
3. **"When you need to"** — incentive design for large quant hedge funds to run manipulation with minimized detection risk.

**Cemini relevance:** REFERENCE for **regime / microstructure skepticism** when backtesting equity signals — not a trading signal source. Treat satirical framing as methodological warning about institutional blind spots, not actionable alpha. Cross-check any overnight-intraday factor claims against ArcticDB equity backtest cadence before prod weighting.

## Snippets

> "If your fraud is properly designed, you can leave footprints as blatant as Figures 3–10 around the world for decades. Few people will notice." [Source: ssrn-4619084.pdf §I — satirical framing]

> Data: publicly available from Yahoo Finance; code publicly available at author reference [9]. [Source: ssrn-4619084.pdf Contents]
