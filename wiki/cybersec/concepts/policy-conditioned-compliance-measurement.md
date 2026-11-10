---
title: "Policy-conditioned compliance measurement: the policy is the argument"
type: concept
related:
  - sources/arxiv-bmms-policy-conditioned-behavioral-compliance-2611.09147.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/compliance-verdict-rule-invariance.md
updated: 2026-11-10
---

## Raw Concept

Question: **how do you measure whether a deployed model does what your rulebook requires, when no fixed benchmark covers your rulebook?** From arXiv 2611.09147, a metric suite that takes a policy corpus as an input argument.

## Narrative

A fixed-taxonomy benchmark measures dimensions its authors chose. That makes results comparable and makes them silent about any particular regulation. A bank under MiFID II, a broker-dealer under FINRA suitability rules, and a deployer under EU AI Act Article 50 are bound by different codified obligations. None of those sets appears in a general benchmark.

A policy-conditioned instrument inverts the design. You supply the obligations; the suite returns a profile over them.

### The four metrics

| Metric | Measures | Failure it names |
|---|---|---|
| CAS — Compliance Attainment Score | severity-weighted share of binding obligations met | low compliance |
| CRM — Compliance Robustness Margin | loss of attainment from direct to adversarial pressure | an obligation honoured only when asked politely |
| BIV — Behavioral Invariance | compliance under a meaning-preserving rephrase | having the phrasing, not the rule |
| BDI — Behavioral Disposition Index | dispositions such as over-refusal | refusal raises CAS without meeting an obligation |

The suite reports a vector, not a scalar. A composite needs a weight vector across dimensions, and no source document supplies one.

### The admission test is the content

A dimension enters only if it passes five criteria. The binding one is **attribution**: a quantity that moves when the judge changes, holding the target fixed, is measuring the instrument. The suite applied its own test, and one of its reported quantities failed.

Two operational rules follow.

**Admit only obligations an assistant can violate in one response or one tool call.** A duty discharged by a firm, a committee or a records system is not testable this way. In the published corpus this funnel reduces 1,003 candidate obligations to 231 non-mixed ones.

**Probe once, freeze the set, and re-score stored records under other judges.** A judge swap then costs no target queries. The BMMS panel re-scored 2,672 records under two further judges.

### The finding that surprised the authors

Admission yield differs by more than four times across document registers. Vendor specifications admit at 68.0%; AI-transparency statutes at 32.3%; conduct regulation at 25.4%; analytical guidance at 16.0%. Correcting each register by its own measured precision widens the spread.

The mechanism is specific. Regulation often binds the firm rather than the utterance. EU AI Act Article 50 requires a provider to design a system that informs users they are interacting with AI; the governed act is a disclosure, but the obligation is a design duty. A vendor model specification states assistant behaviour directly.

**For a defensive audit: the vendor's own published specification is usually a better source of testable obligations than the regulation over the same conduct.**

### Judge variance

Three judges from three providers agree about ordering and disagree about level. Kendall τ is +1.000 between the two swap judges and +0.905 against the primary. One target's absolute CAS spans 0.216 across judges.

The reporting rule: **rank a fleet with confidence; quote an absolute number with its panel range.**

### Limits

The absolute compliance figures rest on one corpus and one primary judge. The level form of attribution failed on most targets. BIV and BDI carry partial evidence. The own-specification comparison cannot separate self-preference from document difficulty.

Confidence: the register yield pattern is `[TENTATIVE]` — one corpus of eleven documents.

## Snippets

> "Customizability to a regulated industry is not a claim about the framework; it is a structural property of taking the policy as an argument." [Source: arxiv-2611.09147-bmms-policy-conditioned-measurement-of-behaviora.pdf p.2]

> "An organization governing deployed agent behavior therefore finds more actionable material in a vendor's specification than in the regulation nominally covering the same conduct." [Source: arxiv-2611.09147-bmms-policy-conditioned-measurement-of-behaviora.pdf p.6]

> "Evaluator choice moves the level of a policy-conditioned reading and leaves its ordering intact. That is the operating characteristic a user of this instrument needs: rank a fleet with confidence, quote an absolute number with its panel range." [Source: arxiv-2611.09147-bmms-policy-conditioned-measurement-of-behaviora.pdf p.7]
