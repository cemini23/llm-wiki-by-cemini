---
title: Heuristic Portfolio Optimization (HPO) — optimality sets and GRS falsification
type: concept
tags: [concept, portfolio-optimization, hrp, risk-parity, theory, k120]
keywords: [hpo, rlpo, ra-hrp, optimality-set, grs-test, implied-returns, schur-complement, allocation-ladder]
related:
  - sources/arxiv-heuristic-portfolio-optimization-2606-12612-2026-06-17.md
  - entities/tools/riskfolio-lib.md
  - sources/toplogical-risk-parity.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/regime-adaptive-continual-portfolio-learning.md
maturity: draft
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- @sources/arxiv-heuristic-portfolio-optimization-2606-12612-2026-06-17.md — K120 anchor source
- @entities/tools/riskfolio-lib.md — Cemini convex/HRP engine
- @sources/toplogical-risk-parity.md — TRP as topology-aware HRP alternative
- @concepts/regime-conditioned-evaluation.md — falsification / regime disclosure sibling
- @concepts/regime-adaptive-continual-portfolio-learning.md — dynamic RLPO extension

## Narrative

**HPO** (2606.12612) formalizes why naive rules (EW, inverse vol, ERC, HRP, RA-HRP) survive estimation error: each rule is optimal for a **specific optimality set** O(w°) in (μ_e, Σ) space. Adopting a heuristic = asserting membership in that set.

**Implied-return principle:** maximum-Sharpe fully-invested w is optimal iff μ_e ∝ Σw. The **defect** D_Φ(w) = implied-return projection error = squared Sharpe inefficiency — measurable without full μ estimation.

**Allocation ladder (operational steal):**

| Rule | Uses | Falsification test |
|------|------|-------------------|
| Equal weight | nothing | zero alpha vs EW |
| Inverse vol | σ_i | Sharpe ∝ correlation row sums |
| ERC / risk parity | Σ | equal w_i μ_{e,i} (performance parity) |
| HRP | tree + cluster variances | Schur GMV coincidence regimes |
| RA-HRP | tree + local Sharpe | node-wise Schur-tangency match |
| Tangency | μ_e, Σ | GRS spanning (benchmark) |

**RLPO bridge:** static HPO policy as **prior**; RL layer pays continuation-value gap vs myopic HPO defect. Relevant when Cemini adds dynamic rebalancing on top of Riskfolio HRP baseline.

**Cemini posture:** **REFERENCE** — wire GRS / angular-loss diagnostics into quarterly equity + PM cluster sizing reviews before changing conviction weights. No new library install.

## Snippets

> "Adopting the rule is behaviorally equivalent to asserting membership" in O(w°). [Source: arxiv-2606.12612-pdf-the-mathematics-of-heuristic-portfolio-optim.pdf §1]

> "The theory supplies falsification diagnostics but does not report new numerics." [Source: arxiv-2606.12612-pdf-the-mathematics-of-heuristic-portfolio-optim.pdf §17]
