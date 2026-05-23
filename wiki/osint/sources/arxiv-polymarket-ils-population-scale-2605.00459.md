---
title: "Information Leakage at Population Scale — Polymarket ILSdl evaluation 2020–2026 (arXiv:2605.00459)"
type: source
tags: [source, arxiv, polymarket, prediction-markets, informed-trading, ils, foresightflow, k59-2]
keywords: [ilsdl, deadline-ils, hazard-decay, ffic, scope-discovery, weibull, resolution-typology, nechepurenko, polymarket-deadline-ils-v3]
related:
  - sources/arxiv-foresightflow-ils-polymarket-2605.00493.md
  - concepts/prediction-market-information-leakage-score.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/polymarket-copy-trading-strategy.md
  - entities/tools/polymarket-insider-tracker.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
read_status: read
---

## Relations

- @sources/arxiv-foresightflow-ils-polymarket-2605.00493.md — methodology companion (ILS / ILSdl definitions)
- @concepts/prediction-market-information-leakage-score.md — population-scale synthesis
- @concepts/polymarket-microstructure-findings.md — informed-flow + microstructure context
- @concepts/polymarket-copy-trading-strategy.md — wallet-level methods vs market-level ILS
- @entities/tools/polymarket-insider-tracker.md — post-hoc trackers vs ILS scope limits

## Raw Concept

- **Title**: Information Leakage at Population Scale: An Evaluation of the Polymarket Insider-Relevant Subpopulation, 2020–2026
- **Author**: Maksym Nechepurenko (Devnull FZCO)
- **Type**: arXiv:2605.00459v1 [q-fin.TR], May 2026 (47 pp)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.00459_polymarket-ils-population-scale.pdf`
- **Retrieved**: 2026-05-23 (K59-2 companion to 2605.00493)
- **Read status**: read

## Narrative

**Scope-discovery study** scaling **deadline-ILS (ILSdl)** from single-case proof (Nechepurenko 2026c) to **12,708** insider-relevant Polymarket markets (Oct 2020 – Apr 2026). Principal bottleneck is **resolution semantics**, not score arithmetic.

### Four headline findings

1. **Coverage collapse:** Only **88 / 12,708 (0.7%)** yield computable ILSdl. On **FFIC** (32 documented cases): **1 in scope** (SEC Bitcoin ETF `fficd-005`, ILSdl ≈ 0.012); **14/32 unclassifiable** (strike/custody/leadership ambiguity — structural, not classifier bug).

2. **Anchor fragility:** **12 / 88 (13.6%)** pass anchor-sensitivity; independent T_event second pass **57.8%** exact-date agreement (below ≥90% ex-ante bar). Operational “interpretable” sample ≈ **12 markets**.

3. **Raw vs adjusted scores:** Raw ILSdl medians **negative in all six** (sub-bucket × period) cells. **Hazard-decay baseline** `ILSdl,adj` yields heterogeneity — e.g. regulatory_formal post-2024 near zero after adjustment; regulatory_announcement post-2024 CI still below zero.

4. **Hazard form:** Pooled post-2024 rejects constant exponential in favor of **Weibull**, but **per-subcategory** checks suggest pooled preference may reflect **category mixture**, not within-cell duration dependence.

### Positioning vs wallet-level work

Complements Mitts & Ofir (2026) and Gómez-Cram et al. (2026): wallet/account screens avoid resolution typology but are post-hoc; ILSdl offers **conditional in-flight** market-level diagnostic on a **tiny interpretable subset** (~12 / 12,708), not a standalone real-time detector.

**Artifacts:** dataset `polymarket-deadline-ils-v3` (CC-BY-4.0) — github.com/ForesightFlow/datasets.

**Cemini posture [TENTATIVE]:** reference for **scope limits** on any Polymarket surveillance product; do not treat ILSdl as production-ready without anchor QA + hazard adjustment + typology expansion (LLM re-classification flagged as paper 3b).

## Snippets

> "Only 88 of 12,708 candidate markets (0.7%) yield computable ILSdl values, and only 1 of 32 markets in the FFIC inventory is in scope." [Source: 2605.00459_polymarket-ils-population-scale.pdf p.1]

> "The conditional in-flight applicability of the market-level lens is narrow — approximately 12 markets out of the 12,708-market candidate sample." [Source: 2605.00459_polymarket-ils-population-scale.pdf p.4]

> "Detection of informed flow on the insider-relevant subpopulation requires methodological refinement on the resolution-typology axis and on the score-baseline axis, not only on the score-computation axis." [Source: 2605.00459_polymarket-ils-population-scale.pdf p.1]
