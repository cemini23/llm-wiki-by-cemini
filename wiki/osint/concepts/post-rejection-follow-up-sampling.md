---
title: Post-Rejection Follow-up Sampling (PRFS)
type: concept
tags: [concept, counterfactual, filter-calibration, algorithmic-trading, prediction-markets, k119]
keywords: [prfs, rejection-audit, false-negative, forward-tracking, dex]
related:
  - sources/arxiv-prfs-counterfactual-dex-2606.08228-2026-06-16.md
  - concepts/event-based-prediction-market-ml.md
  - concepts/quant-finance.md
  - concepts/llm-agent-systems.md
maturity: draft
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- @sources/arxiv-prfs-counterfactual-dex-2606.08228-2026-06-16.md — K119 primary source
- @concepts/event-based-prediction-market-ml.md — silent backtest failure on event markets
- @concepts/quant-finance.md — corpus hub

## Raw Concept

K119 arXiv 2606.08228 — measure **counterfactual outcomes of rejected candidates** via forward price/liquidity sampling instead of assuming rejects were correct.

## Narrative

### Problem

Algo systems (DEX snipers, PM scanners, conviction gates) reject most candidates. Without forward tracking, **filter false negatives** are invisible — backtests look clean because rejects are never scored.

### PRFS loop

```
reject candidate → log rejection event → sample forward outcomes (cadence × horizon)
→ compare filter precision to realized paths
```

### Cemini mapping

| Surface | PRFS analog |
|---------|-------------|
| PM cross-venue scanner | Log skipped markets; Exa/Gamma forward check resolution path |
| Conviction.yaml gates | Sample rejected WC markets through public APIs post-kickoff |
| Intel filter blocklist | Quarterly false-negative audit on `REJ_*` codes |

**Verdict:** REFERENCE methodology — no Zenodo dataset install on prod. Brief stages **rejection follow-up audit** spec for server-Claude.

## Snippets

> "Evaluate filter precision against actual market outcomes of rejected candidates, not against synthetic backtest reconstructions." [Source: arxiv-2606.08228-tier2-sweep.pdf abstract]
