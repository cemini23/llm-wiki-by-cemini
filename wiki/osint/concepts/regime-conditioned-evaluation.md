---
title: "Regime-Conditioned Evaluation — PRS, No-Free-Leaderboard, and Cemini's Brief-Audit Discipline"
type: concept
tags: [concept, evaluation-discipline, bayesian-optimization, hpo, treatment-effects, brief-audit, conductor, applied-during-ingest, no-free-leaderboard, mathematically-grounded]
keywords: [PRS, portable-regime-score, regime-conditioned, CATE, ATE, no-free-leaderboard, B-over-A, budget-action-ratio, prior-rank-correlation, REGIMEPLANNER, brief-audit, regime-disclosure-gate, conductor-evaluation, strategy-backtest-rigor, minimum-reporting-standard]
related:
  - sources/regime-conditioned-bo-evaluation.md
  - concepts/conductor-orchestrator.md
  - concepts/evidence-withheld-verification.md
  - concepts/high-signal-paper-patterns.md
  - concepts/algorithmic-stopping-conditions.md
  - concepts/llm-listwise-alignment.md
  - concepts/cemini-license-posture.md
  - sources/controlled-study-of-multi-agent-debate-in-logical-reasoning.md
  - sources/evonash-marl.md
  - sources/test-time-adaptation-for-non-stationary-time-series.md
  - concepts/markov-regime-switching-models.md
maturity: draft
created: 2026-05-07
updated: 2026-05-16
---

## Relations

- @sources/regime-conditioned-bo-evaluation.md — K33 anchor source: 42-page paper introducing PRS + No-Free-Leaderboard proposition + REGIMEPLANNER.
- @concepts/conductor-orchestrator.md — Conductor's fitness function is the highest-action-value Cemini target for regime-conditioned eval discipline.
- @concepts/evidence-withheld-verification.md — sibling anti-fabrication structure; ARA hides answers, regime-disclosure makes the regime observable.
- @concepts/high-signal-paper-patterns.md — this paper exemplifies the rubric: formal proposition + 79-condition empirical validation + actionable diagnostic + reporting protocol.
- @concepts/algorithmic-stopping-conditions.md — budget B/|A| is a stopping-condition coordinate, formalized here as the dominant effect modifier.
- @concepts/llm-listwise-alignment.md — sibling K33 concept; both are about training/eval rigor mismatches.
- @concepts/cemini-license-posture.md — license-evaluation policy is structurally a regime-conditioned decision (license × use-case × deployment-tier); the rubric here echoes that discipline.
- @concepts/markov-regime-switching-models.md — sibling: detects the regime (Markov/HMM); this page evaluates strategies *conditioned on* the regime.
- @sources/test-time-adaptation-for-non-stationary-time-series.md — applied example: TTA paper splits real markets into pandemic/high-inflation/recovery regimes and gates claims with Diebold–Mariano + Newey–West HAC tests.
- @sources/controlled-study-of-multi-agent-debate-in-logical-reasoning.md — exemplar of the controlled-study discipline: disentangles six debate factors against a fixed anchor instead of reporting a single aggregate "debate helps" number.
- @sources/evonash-marl.md — applies the conservative-validation half of this discipline (walk-forward, White Reality Check, SPA-lite, deflated Sharpe) and honestly reports non-significance rather than overclaiming alpha.

## Raw Concept

The K33 ingest of @sources/regime-conditioned-bo-evaluation.md (Noel Thomas, MBZUAI, arXiv 2605.04895) provides formal grounding for an evaluation discipline Cemini already practices heuristically: **algorithm/strategy comparisons must report regime variables, or they are estimating Conditional Average Treatment Effects masquerading as algorithmic rankings.** This page is the Cemini-side concept hub that operationalizes the paper's contributions.

## Narrative

### The core problem (formalized)

A benchmark comparison of algorithm $X$ vs $Y$ produces a number — call it the Average Treatment Effect (ATE) of choosing $X$ over $Y$ on that benchmark mixture. Practitioners read this as "X beats Y."

But each algorithm's effectiveness depends on **regime variables** — quantities that vary across deployments but are typically not held fixed in benchmarks. In Bayesian Optimization specifically: budget per context $B$, action-space size $|A|$, prior-quality $\rho$ (Spearman correlation between prior means and observed outcomes), context count $K$, metric type (terminal Hit@K vs cumulative AUC).

When the **Conditional Average Treatment Effect** $\mathrm{CATE}(\text{regime})$ changes sign across the regime axis, the No-Free-Leaderboard proposition applies (3-line proof from linearity of expectation; Proposition A.11 in the source paper):

> If $\exists$ regime conditions $r_1, r_2$ such that $\mathrm{CATE}(r_1) > 0 > \mathrm{CATE}(r_2)$, then ATE on any benchmark mixture is a **free parameter of the mixture choice**. Any ranking — including ties or reversals — is achievable by choosing evaluation conditions, with no fabrication required.

### The paper's headline reversal

GDSC2 drug-response benchmark, four planners (Greedy, UCB, Thompson, REIGN). At $B=50$: Greedy wins Hit@1 by +0.050. At $B=100$: UCB wins by +0.035. **Same benchmark, same data, same surrogate.** Both papers reporting these are correct — they're estimating different CATEs.

Across a 40-paper audit (NeurIPS, ICML, ICLR, AISTATS, UAI, TMLR, JMLR, AutoML-Conf 2022–2025), **98% of transfer-BO papers do not vary B/|A|** as a controlled axis. Existing leaderboards estimate ATEs over hidden regime variables.

### Portable Regime Score (PRS)

The paper's diagnostic: a single observable scalar that orders exploration advantage.

$$\mathrm{PRS}(B, |A|, \rho) = \frac{B}{|A|} \cdot (1 - \rho)$$

- $B/|A|$ = **budget ratio** — fraction of action space that can be queried per context.
- $1 - \rho$ = **prior weakness** — how much the prior fails to rank actions correctly.

Higher PRS = more exploration value. Lower PRS = exploitation (Greedy) wins.

Empirical validation across 79 conditions:
- Hierarchical model: $\beta = 0.50$ (95% CI [0.34, 0.66]), $p = 1.1\times10^{-9}$, ICC = 0.36.
- Per-benchmark Spearman: Buchwald $r=0.75$, GDSC2 $r=0.96$, HPO-B $r=0.83$.
- Pre-registered honesty-bound: 27/40 = 67.5% predictive accuracy on held-out conditions, **below the 90% target the paper set itself**. Failure splits cleanly: 93.8% accuracy on families where EMA priors accumulate ($\hat{\rho} > 0$), zero signal on families where $\hat{\rho} \approx 0$ throughout.

PRS is **best as a within-domain ordering**; cross-benchmark threshold shifts with observation noise $\sigma^2$.

### Application protocol (from §2)

Before deploying a BO planner in a new domain:

1. Run $K_0 \geq 3$ pilot contexts with any fixed planner (Greedy is conservative).
2. Compute $\hat{\rho}$ as Spearman correlation between EMA posterior means and observed outcomes across pilot-queried actions.
3. Compute $\widehat{\mathrm{PRS}} = (B/|A|)(1-\hat{\rho})$.
4. Use **Greedy** if $\widehat{\mathrm{PRS}} < 0.10$; otherwise **UCB** or REGIMEPLANNER (online switching).

Three pilot contexts suffice for a rough estimate. Paper reports threshold sensitivity is approximately flat over $\theta \in [0.05, 0.10]$.

### Cemini operational targets

Three places this discipline applies directly. Action-value ordering:

#### 1. Brief-audit `regime-disclosure` gate (highest-leverage, 1–2 hour port)

Current state: `scripts/skill_audit.py` checks structural properties (sections present, cross-links resolve, citation tags present, NEEDS-VERIFICATION freshness, prose quality, frontmatter validity). It does **not** check whether briefs comparing algorithmic alternatives disclose regime variables.

Proposed gate: when a brief's `## Body` section contains an algorithm/strategy comparison (detect by keyword pattern: "X vs Y", "X outperforms Y", "X beats Y"), require the brief to also report:

- Budget / horizon / sample-size variable.
- Prior-quality / baseline-strength signal.
- Context count or evaluation breadth.
- Metric type (terminal vs cumulative; absolute vs relative).

REJECT verdict if comparison present without regime disclosure. WARN if regime variables are present but not held fixed across compared methods.

This is the most directly portable contribution of the paper to Cemini's workflow. Brief-audit-upgrade sprint (already on roadmap from K32) should bundle this with the academic-paper-skills 35-point peer-review framework port.

#### 2. Conductor fitness-function evaluation

Conductor's fitness function evaluates routing decisions over (model, tool) bundles. Current rubric (per @concepts/conductor-orchestrator.md):

- End-to-end success rate.
- Cost per successful query.
- Latency.
- Confidence-calibration check.

Missing: **regime disclosure on the evaluation traffic mix.** If Conductor is evaluated on traffic mix $M_1$ and shows Routing-Policy-A wins, but mix $M_2$ would show Routing-Policy-B wins, the leaderboard is a CATE in disguise.

Concrete additions:
- Per-evaluation: report query-budget per category, candidate-bundle size $|A|$, prior policy quality $\rho$ (rank correlation between prior routing scores and actual outcomes), context count $K$ (distinct query categories).
- Compute Conductor's $\widehat{\mathrm{PRS}}$ on each routing decision; track how often Conductor's chosen bundle aligns with PRS recommendation.
- When deploying Conductor across a new domain (e.g., new analyst tool, new market regime), run the 3-pilot-context PRS protocol before claiming any policy-A vs policy-B win.

#### 3. Strategy backtest evaluation discipline

Trading-strategy backtests are structural twins of BO acquisition comparisons. Mapping:

| BO concept | Trading concept |
|---|---|
| Action-space $A$ | Strategy / asset universe |
| Per-context budget $B$ | Trades-per-period budget |
| Prior $\rho$ | Ex-ante alpha-rank correlation (e.g., signal-to-realized-PnL Spearman over a calibration window) |
| Context count $K$ | Distinct regime contexts (volatility regimes, sectors, market states) |
| Metric (terminal vs cumulative) | Sharpe / Calmar / drawdown vs cumulative-PnL |

A strategy ranking that doesn't disclose these variables is the same kind of unconditional ATE the paper diagnoses in BO. Practical implication for Cemini's prediction-market work: when comparing strategy ensembles across Polymarket vs Kalshi vs equity markets, regime variables differ enough that a single ranking is **almost certainly a benchmark-mixture artifact**, not an algorithmic finding.

### Minimum reporting standard (Cemini-adapted)

Adapted from the paper's §2.1 protocol. For any Cemini brief that compares algorithms / strategies / planners / routing policies:

1. **Budget/horizon variable** — what's the per-context resource limit?
2. **Action-space size** — how many alternatives are being chosen among?
3. **Prior quality signal** — how good is the baseline ranker before the comparison runs?
4. **Context count** — how many independent evaluation contexts? (Paper requires $K \gtrsim (2$–$4) \cdot |A|/B$ for PRS reliability.)
5. **Metric specification** — terminal vs cumulative; absolute vs relative; any non-monotonic transformation.

Without these five numbers, the comparison ranks regimes, not algorithms.

### Open question: cross-benchmark PRS calibration

Paper's own honesty-bound: cross-benchmark Spearman CI [0.19, 0.80] excludes zero only with HPO-B included. PRS is a **within-domain ordering**, not a universal score. For Cemini, this means PRS calibration is **per-domain** (Conductor PRS ≠ strategy-backtest PRS ≠ brief-audit PRS thresholds). Each domain needs its own threshold-selection process via cross-validation on held-out cases.

This is a non-trivial overhead that argues for **starting with the brief-audit gate** (lowest data needs, highest leverage) before extending to Conductor and strategy backtests.

## Snippets

- "If CATE changes sign across the PRS axis, any ATE including zero is achievable by benchmark mixture alone, formalising why the 98%-non-sweeping evaluation literature produces unreliable rankings." [Source: Regime-Conditioned BO p.1 abstract]

- "$\mathrm{PRS}(B, |A|, \rho) = (B/|A|)(1-\rho)$. Higher PRS = larger budget ratio and/or weaker prior = exploration more likely to pay." [Source: Regime-Conditioned BO p.3 Definition 2.1]

- "Before claiming method X beats Greedy, report: (1) prior condition, (2) budget ratio B/|A|, (3) metric (terminal or cumulative), (4) context count K." [Source: Regime-Conditioned BO p.3]

- "98% of transfer-BO papers never vary B/|A| as a controlled axis, 80% report only one metric family, and 76% fix context count K." [Source: Regime-Conditioned BO p.2]

- "Acquisition comparisons that omit B/|A|, ρ, K, and metric type estimate an ATE over hidden regime variables." [Source: Regime-Conditioned BO p.2]

## Dead Ends

- **Universal PRS threshold attempt** — paper's own data shows the cross-benchmark threshold shifts with observation noise $\sigma^2$. Don't try to ship a single Cemini-wide PRS=0.10 cutoff; calibrate per-domain.

- **Brief-audit gate via LLM-as-judge** [NEEDS VERIFICATION 2026-05-07] — tempting to delegate "is this brief comparing algorithms?" detection to an LLM. Per @concepts/evidence-withheld-verification.md, this would need the judge to receive only the brief body, not the algorithm identities or any ground truth. Mechanical keyword detection ("X vs Y", "X beats Y", "X outperforms") is more robust as a starting point; LLM augmentation is a v2 enhancement.
