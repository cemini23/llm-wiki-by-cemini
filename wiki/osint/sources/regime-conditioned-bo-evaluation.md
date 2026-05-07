---
title: "Regime-Conditioned Evaluation in Multi-Context Bayesian Optimization"
type: source
tags: [paper, bayesian-optimization, hpo, evaluation-discipline, treatment-effects, no-free-leaderboard, mbzuai, arxiv-2605, empirical-rigor]
keywords: [PRS, portable-regime-score, REGIMEPLANNER, B-over-A, budget-action-ratio, prior-rank-correlation, CATE, ATE, no-free-leaderboard, GDSC2, HPO-B, Buchwald-Hartwig, transfer-BO, regime-conditioned, Noel-Thomas, REIGN, sign-reversal, Greedy, UCB, Thompson, hierarchical-model]
related:
  - concepts/regime-conditioned-evaluation.md
  - concepts/conductor-orchestrator.md
  - concepts/high-signal-paper-patterns.md
  - concepts/evidence-withheld-verification.md
  - concepts/algorithmic-stopping-conditions.md
  - sources/blade-bayesian-listwise-alignment.md
maturity: draft
read_status: deep-read
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @concepts/regime-conditioned-evaluation.md — concept hub for the methodology; this source is the K33 anchor.
- @concepts/conductor-orchestrator.md — Conductor's fitness function performs acquisition-style decisions over routing; the No-Free-Leaderboard proposition applies to Conductor evaluation if regime variables are not held fixed.
- @concepts/high-signal-paper-patterns.md — fits the rubric: formal proposition (3-line proof) + 79-condition empirical validation + concrete pre-experiment diagnostic + actionable reporting protocol. **Highest action-value paper of K33.**
- @concepts/evidence-withheld-verification.md — both this paper and the ARA Seal pattern are anti-fabrication structures: ARA hides the answer; PRS makes the regime observable so winners can't be cherry-picked from benchmark mixture.
- @concepts/algorithmic-stopping-conditions.md — budget B/|A| is a stopping-condition coordinate; the paper formalizes its role as the dominant effect modifier.
- @sources/blade-bayesian-listwise-alignment.md — sibling K33 ingest; both attack alignment/optimization rigor.

## Raw Concept

**Title**: Regime-Conditioned Evaluation in Multi-Context Bayesian Optimization
**Author**: Noel Thomas (Mohamed bin Zayed University of Artificial Intelligence, Abu Dhabi)
**Venue**: Preprint
**arXiv**: 2605.04895v1 (cs.LG), submitted 6 May 2026
**License**: arXiv default; check before any code reuse
**Filename**: `Regime-Conditioned Evaluation in Multi-Context Bayesian Optimization.pdf` (2.2 MB, 42 pages)
**Canonical location**: `cemini-librarian:/opt/cemini-bulk/research/Regime-Conditioned Evaluation in Multi-Context Bayesian Optimization.pdf`
**Read status**: deep-read (pages 1–10 main text, appendices skimmed)

Surfaced in inbox 2026-05-06 alongside @sources/blade-bayesian-listwise-alignment.md. Deep-read 2026-05-07 (K33 ingest).

## Narrative

### The reversal that motivates the paper

Same GDSC2 drug-response benchmark, same surrogate, same four planners. At budget B=50, **Greedy wins** Hit@1 by +0.050 over UCB. At B=100, **UCB wins** by +0.035 over Greedy. Neither result is fabricated. The sign reversal is explained entirely by the unreported budget ratio B/|A|.

This is not measurement noise. It is the **conditional average treatment effect (CATE) of acquisition choice** changing sign across a regime variable. When CATE flips sign, the **average treatment effect (ATE) on any unconditional benchmark is a free parameter of the benchmark mixture** — any ranking, including ties or reversals, is achievable by choosing evaluation conditions, with no fabrication required (Proposition A.11, "No-Free-Leaderboard").

A 40-paper audit (NeurIPS, ICML, ICLR, AISTATS, UAI, TMLR, JMLR, AutoML-Conf 2022–2025) finds **98% of transfer-BO papers do not vary B/|A| as a controlled axis**. Existing leaderboards estimate ATEs over hidden regime variables and present them as algorithmic rankings. The cited reversals are not transfer-BO-specific: Adam-vs-SGD, MLP-vs-XGBoost, and 2018–2020 NAS literature all show the same pattern under different regime variables.

### Portable Regime Score (PRS)

The paper's central diagnostic:

$$\mathrm{PRS}(B, |A|, \rho) = \frac{B}{|A|} \cdot (1 - \rho)$$

where $B$ is per-context budget, $|A|$ is action-space size, and $\rho$ is the Spearman rank correlation between prior means and observed action values at context start (measurable from any pilot run).

**Higher PRS = larger budget ratio and/or weaker prior = exploration more likely to pay.** PRS is computed from the Greedy planner's $\rho$ (conservative: exploratory planners build higher-$\rho$ priors over time).

Application protocol (from §2):
1. Run $K_0 \geq 3$ pilot contexts with any fixed planner.
2. Compute $\hat{\rho}$ as Spearman correlation between EMA posterior means and observed outcomes across the actions queried in the pilot.
3. Compute $\widehat{\mathrm{PRS}} = (B/|A|)(1-\hat{\rho})$.
4. Use **Greedy** if $\widehat{\mathrm{PRS}} < 0.10$; otherwise use **UCB** or REGIMEPLANNER.

### Empirical validation across 79 conditions

- **Hierarchical model**: $\beta = 0.50$ (95% CI [0.34, 0.66]), $p = 1.1\times10^{-9}$, ICC = 0.36.
- **Cluster-robust Spearman CI**: [0.19, 0.80] across 9 benchmark families. Wide because of inter-family heterogeneity; without HPO-B family it crosses zero, but Buchwald + GDSC2 alone reject the global null (Fisher $\chi^2(4) = 23.0$, $p = 0.0001$).
- **Per-benchmark**: Buchwald $r = 0.75$, GDSC2 $r = 0.96$, HPO-B $r = 0.83$ — all surviving Holm-Bonferroni at $\alpha = 0.05$.
- **Five published reversals predicted from PRS** before the comparison ran: PriorBand argmax flip, $\pi$BO-UCB below GP-EI at wrong prior, MF-MES failure at irrelevant info source, BOHB ranking flip at large budget, HPO-B leaderboard re-analysis.

### REGIMEPLANNER — constructive validation

A simple adaptive rule: estimate $\hat{\rho}_t$ online from queries within each context; switch from UCB → Greedy when $\widehat{\mathrm{PRS}}_t < \theta = 0.10$. Threshold selected on Buchwald cross-validation, applied **unchanged** to all other benchmarks.

Results:
- HPO-B at B=100: **wins all 16 community search spaces** vs Greedy, mean +0.103 Hit@1, binomial $p = 1.5\times10^{-5}$.
- GDSC2 at B=50: **+18% over the matched per-context oracle** ({Greedy, UCB} arms) — the planner exceeds the upper bound a fixed-policy oracle could achieve.
- **Honesty bound**: under the wider 4-arm oracle ({Greedy, UCB, Thompson, REIGN}), REGIMEPLANNER trails by 12%. Pre-registered prediction accuracy: 27/40 = 67.5%, below the 90% target — the failure splits cleanly by whether EMA priors actually accumulate (HPOBench-NN, LCBench: 15/16 = 93.8% accuracy; PD1, TabRepo: zero signal).

### Cemini relevance — high action-value

This paper is the formal scaffolding for several disciplines Cemini already practices informally:

1. **Conductor fitness function**: every Conductor routing decision is an acquisition over (model, tool) bundles. If Cemini evaluates Conductor on a single fixed traffic mix without reporting $B/|A|$ (per-query budget vs candidate-bundle space), $\rho$ (prior quality of the routing policy), $K$ (context count), and metric type, then Conductor leaderboard rankings are CATEs in disguise. **PRS gives Cemini a pre-experiment diagnostic** for whether to expect routing wins from exploration.

2. **Brief-audit framework** (`scripts/skill_audit.py`): the validated→core maturity transition currently rests on inbound-citation count + freshness. The No-Free-Leaderboard proposition argues this is insufficient when claims involve algorithmic comparisons — **briefs comparing strategies/planners/algorithms must report regime variables before the comparison can be considered settled.** Adding a `regime-disclosure` static check is a 1–2 hour port.

3. **Strategy backtest evaluation**: any backtest comparing trading strategies has structural analogues — $B = $ trade budget per period, $|A| = $ strategy universe, $\rho = $ ex-ante alpha-rank correlation, $K = $ number of regime contexts (volatility regimes, sectors). A strategy ranking that doesn't disclose these is a CATE-in-disguise. Cross-regime strategy stability is a function of **whether the comparison's PRS sat in the boundary zone** ($\mathrm{PRS} \in [0.05, 0.15)$ → 53.8% predictive accuracy in the paper's own data).

4. **Cemini's existing anti-benchmark-shopping discipline** (per `cemini-license-posture` + `high-signal-paper-patterns` + the Phase-0 audit pattern in CLAUDE.md): this paper provides **formal grounding** for what Cemini already does heuristically. Promote regime-disclosure to a first-class brief-audit gate.

### Minimum reporting standard (from §2.1, paper's own protocol)

> Before claiming method X beats Greedy, report: (1) prior condition, (2) budget ratio B/|A|, (3) metric (terminal or cumulative), (4) context count K (requires $K \gtrsim (2$–$4) \cdot |A|/B$ for PRS to be reliable).

This becomes the proposed Cemini brief-audit `regime-disclosure` gate for any brief that compares algorithmic alternatives. Spec deferred to a brief at `briefs/2026-05-07_regime-disclosure-brief-audit-gate.md` — see ROADMAP.

## Snippets

- **The reversal**: "Run the same GDSC2 drug-response benchmark at $B=50$: Greedy outperforms UCB by 0.050 Hit@1. Run it at $B=100$: UCB outperforms Greedy by 0.035. Both results are correct […] the sign reversal is explained entirely by the unreported budget ratio B/|A|." [Source: Regime-Conditioned BO p.1]

- **No-Free-Leaderboard proposition** (Proposition A.11 stated in §3): "If $\exists (B/|A|, \rho)_1, (B/|A|, \rho)_2$ such that $\mathrm{CATE}(B/|A|, \rho)_1 > 0 > \mathrm{CATE}(B/|A|, \rho)_2$, then ATE is undefined as a decision rule. The regime map in Figure 2 certifies this condition holds for transfer BO." [Source: Regime-Conditioned BO p.4]

- **PRS definition**: "$\mathrm{PRS}(B, |A|, \rho) = (B/|A|)(1-\rho)$. Higher PRS = larger budget ratio and/or weaker prior = exploration more likely to pay. PRS is computed from the Greedy planner's $\rho$ (conservative: exploratory planners build higher-$\rho$ priors over time)." [Source: Regime-Conditioned BO p.3 Definition 2.1]

- **40-paper audit headline**: "A 40-paper audit […] finds 98% of papers do not vary B/|A|, so existing leaderboards are not regime-controlled." [Source: Regime-Conditioned BO p.1 abstract]

- **Variance decomposition headline** (Buchwald 4×4 prior-by-acquisition): prior family explains $\eta^2 = 0.8635$ of Hit@1 variance, planner choice explains $\eta^2 = 4.4\times10^{-5}$ — about **20,000× ratio**. [Source: Regime-Conditioned BO p.4 Table 3]

- **REGIMEPLANNER HPO-B**: "On HPO-B at $B=100$, it wins Greedy on all 16 community search spaces (mean +0.103 Hit@1, 95% CI [+0.075, +0.131], binomial $p=1.5\times10^{-5}$)." [Source: Regime-Conditioned BO p.6]

- **Minimum reporting standard**: "Before claiming method X beats Greedy, report: (1) prior condition, (2) budget ratio B/|A|, (3) metric (terminal or cumulative), (4) context count K." [Source: Regime-Conditioned BO p.3]

- **Pre-registered honesty bound**: "Pre-registered predictions on 40 held-out conditions gave 27/40 = 67.5% overall accuracy, below our 90% target. The failure splits cleanly: on families where EMA priors accumulate […] accuracy reached ≥90%; on families where $\hat{\rho} \approx 0$ throughout […] PRS carries no signal. This is not a hidden failure: it is the mechanism made visible." [Source: Regime-Conditioned BO p.2]

## Dead Ends

- **Single-author single-affiliation paper** — Noel Thomas at MBZUAI is the sole listed author. Empirically rigorous papers from solo authors at non-anchor institutions occasionally fail peer review on reproducibility grounds. Mitigation: paper's pre-registered predictions + 79-condition replication across 9 benchmark families is unusually thorough; the 67.5% honesty-bound disclosure is a strong reproducibility signal. Track for venue acceptance.

- **Cluster-robust CI [0.19, 0.80] excludes zero only with HPO-B included** — without HPO-B (n=48 of 79 conditions), cross-benchmark CI crosses zero. PRS's cross-benchmark generalization is **strong within each primary benchmark, uncertain across benchmark families with heterogeneous observation noise** (paper's own framing, p.3). For Cemini: PRS is a within-domain diagnostic, not a universal score.
