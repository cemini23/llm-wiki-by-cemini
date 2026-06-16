---
title: "Price-Discovery Admissibility in Tokenized Fixed Income (arXiv 2606.13822)"
type: source
tags: [source, arxiv, tokenization, fixed-income, price-discovery, quant-finance, k118]
keywords: [2606.13822, tokenized-treasuries, convenience-yield, affine-term-structure, measurement-reconciliation, collateral-haircut]
related:
  - concepts/tokenized-fixed-income-price-discovery.md
  - concepts/tokenized-us-equities-onchain-basis-trade.md
  - concepts/quant-finance.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-06-16
clusters: [quant-finance, crypto, prediction-markets]
---

## Relations

- @concepts/tokenized-fixed-income-price-discovery.md — admissibility criterion + affine basis model
- @concepts/tokenized-us-equities-onchain-basis-trade.md — sibling on-chain wrapper / basis lane
- @concepts/quant-finance.md — corpus hub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Price-Discovery Admissibility in Tokenized Fixed Income: Identification, Affine Characterization, and the Structure of the Token-to-Fiat Mapping |
| **Authors** | Alkhamov (ESSEC), Kriuk (HKUST) |
| **arXiv** | 2606.13822 |
| **sha256** | `f76370d49844b3afeb309cf32b8da2b68a4324e62875e12bb8140c85ea5f56af` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.13822-price-discovery-admissibility-in-tokenized-fixed.pdf` |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (abstract + §1–2 framing + admissibility setup) |

## Narrative

Reframes tokenized U.S. Treasury research: before asking "what is the yield discount?", ask whether on-chain series is **commensurable** with off-chain reference and **market-informative**.

**Three-step pipeline:**

1. **Measurement reconciliation** — day-count, fee wedge, amortized-cost lag, benchmark maturity mismatch (signed, jointly ~tens of bps — comparable to headline "~70–80 bps discount").
2. **Price-discovery admissibility test** — falsifiable necessary conditions on serial dependence + idiosyncratic dispersion of reconciled basis. Weak criterion: not "efficiently priced" but "not obviously accounting output."
3. **Affine characterization** (admitted product only) — two-factor model: rate factor (risk-neutral, Treasury cross-section) + **additive orthogonal basis factor** (physical measure). Quarterly mean-reversion half-life; small positive long-run basis; **March 2026 regime change** toward parity with volatility collapse.

**Principal finding:** of four products with sufficient history (~$6B tokenized Treasury universe), **exactly one admissible**; three fail (no serial dependence, dispersion too large — republication mechanics dominate).

**Downstream illustration:** collateral haircut from affine model — dominated by **persistence uncertainty** (weak ID on ~70 post-reconciliation obs) → sensitivity surface, not point estimate.

**Cemini posture:** **REFERENCE** — measurement discipline for any future on-chain fixed-income / stablecoin-adjacent feeds. No prod data pipeline today; monitor if PM/crypto desk adds tokenized Treasury marks.

## Snippets

> "Before one can ask what a tokenized claim is worth relative to its reference, one must establish that the on-chain series and the off-chain reference are commensurable… and… carries recoverable information." [Source: arxiv-2606.13822-price-discovery-admissibility-in-tokenized-fixed.pdf §1]

> "Of four products with sufficient history… exactly one is admissible." [Source: arxiv-2606.13822-price-discovery-admissibility-in-tokenized-fixed.pdf abstract]

> "The raw difference therefore bundles at least four deterministic measurement gaps… together with whatever genuine economic difference exists." [Source: arxiv-2606.13822-price-discovery-admissibility-in-tokenized-fixed.pdf §1]
