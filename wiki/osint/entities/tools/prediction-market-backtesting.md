---
title: "prediction-market-backtesting — Nautilus Trader Extension"
type: entity
tags: [tool, backtesting, prediction-markets, nautilus, rust, python, reference-only]
keywords: [prediction market, backtesting, Nautilus Trader, Optuna, TPE, GPL-3.0, Rust]
related:
  - sources/project-link-evaluation-brief-5_10.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/project-link-evaluation-brief-5_10.md` — source evaluation brief (URL 2)

## Raw Concept

A Nautilus Trader extension providing custom prediction market adapters for backtesting simulations. Uses Optuna-based Tree-structured Parzen Estimators (TPE) for hyperparameter sampling.

- **Repo**: `github.com/evan-kolberg/prediction-market-backtesting`
- **License**: Mixed — GPL-3.0, LGPL-3.0, MIT, and Unknown. Chaotic licensing.
- **Stack**: Python 92.9%, Rust 6.7%
- **Maturity**: 838 stars, 466 commits

## Narrative

**Verdict: Reference-only.** The repository's chaotic multi-license structure (GPL-3.0 + LGPL-3.0 + MIT simultaneously) creates extreme legal ambiguity — integrating any part risks viral contamination of the Cemini codebase. However, the mathematical approaches (Optuna TPE sampling integrated with backtesting frameworks, Rust-to-Python interface patterns) are valuable for independent study during solo-dev research sessions.

The TPE sampling methodology specifically is worth extracting conceptually: Tree-structured Parzen Estimators provide more efficient hyperparameter optimization than grid search for trading strategy parameter sweeps.

[Source: Project Link Evaluation Brief 5_10.docx, URL 2]
