---
title: "Measurement Artifacts in Trustworthiness Evaluations of Quantized Small Language Models (arXiv:2611.32848)"
type: source
related:
  - concepts/quantization-instrument-artifacts.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/low-asr-is-not-refusal.md
maturity: draft
read_status: read
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Measurement Artifacts in Trustworthiness Evaluations of Quantized Small Language Models |
| Authors | Tanzeel Abbas, Tehseen Zia (COMSATS University Islamabad); David Windridge (Middlesex University London) |
| Type | arXiv preprint, cs.AI |
| ArXiv | 2611.32848v1 (24 November 2026) |
| URL | https://arxiv.org/abs/2611.32848 |
| Location | `research to be indexed/cybersec/arxiv-2611.32848-measurement-artifacts-in-trustworthiness-evaluat.pdf` |
| Pages | 20 |
| Retrieved | 2026-11-25 |
| Read status | read |

## Narrative

The paper separates a real change in model behavior from a change in the measuring instrument. It writes the measured change as ∆meas = ∆true + ∆inst. Error that is equal at both precisions can shrink a paired comparison. It cannot create or reverse an effect. Error that interacts with quantization can do both. That part is often reported as an effect of quantization.

The scope is 8 instruction-tuned models below two billion parameters, from five families. Each model runs at float16, LLM.int8() and 4-bit NormalFloat (NF4), on identical items. All comparisons are paired tests. Two human annotators supply the safety labels.

**Safety effect after calibration.** Four-bit quantization raises harmful compliance by 2.6 points (3.0 with WildGuard as the judge). A corrected keyword detector records a 4.7-point drop in refusal on the same items. The corrected safety effect is about half to two-thirds of the drop that a refusal detector alone would report. A keyword list that misses a new phrasing of refusal inflates the apparent safety loss.

**Scoring protocol changes the sign.** On 2,000 HaluEval items, the 4-bit change for SmolLM2-1.7B is +9.8 points under mean-normalized cloze scoring, +0.8 under summed cloze, −13.6 under lettered scoring in the released option order, and −7.3 when averaged over two orders. Same model, same items, same precisions. Cloze and lettered estimates correlate at ρ = 0.10, against a ceiling of about 0.77. The protocols disagree far beyond their noise.

**LLM.int8() is deterministic but not batch-invariant.** The number of 8-bit answers that change when the batch is rearranged is 57–119% of the number that change under quantization from float16. Padding alone changes 2.2–5.6% of 8-bit choices and at most 0.4% of float16 choices. Disabling the outlier decomposition does not remove the dependence. Keeping activations in float16 removes it. Rounding activations to 8 bits is therefore enough to cause the effect. NF4 quantizes only weights and is batch-invariant.

**Calibration losses are mostly response bias.** Of 80 changes in expected calibration error, 11 have uncorrected intervals that exclude zero, against about 4 expected by chance. The 11 have no consistent direction: 6 improvements and 5 losses. The two largest reported losses are response-bias shifts. After recentring on a cross-fitted intercept, one loss of 0.154 becomes −0.031.

Defensive reading. A team that accepts a compressed small model for a guardrail or a classifier must fix three things before it trusts a safety delta: the refusal detector, the multiple-choice scoring protocol, and the batch shape. A batch-level result is not reproducible if the runtime packs items differently. This matters for the local lab stack, where NF4 and LLM.int8() are normal deployment choices. See @concepts/quantization-instrument-artifacts.md and @concepts/local-abliterated-llm-pentest-stack.md.

The paper releases item-level predictions, raw option scores for every protocol, detector outputs, and the adjudicated human annotations. That release makes the instrument error checkable rather than only argued.

## Snippets

> "We write the measured change as ∆meas = ∆true + ∆inst, where ∆inst is the change in the instrument's error between the two precisions." [Source: arxiv-2611.32848 p.1]

> "Cloze and lettered multiple-choice scoring disagree about the effect of quantization far more than their noise allows: their estimates correlate at ρ = 0.10, against a ceiling of about 0.77." [Source: arxiv-2611.32848 p.1]

> "LLM.int8() answers and generations depend on which items share a batch, and padding alone changes its answers." [Source: arxiv-2611.32848 p.1]

> "The two largest reported calibration losses are response-bias shifts." [Source: arxiv-2611.32848 p.1]
