---
title: Quantization instrument artifacts — separate the model change from the meter
type: concept
related:
  - sources/arxiv-measurement-artifacts-quantized-trustworthiness-2611.32848.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/low-asr-is-not-refusal.md
maturity: draft
updated: 2026-11-25
---

## Raw Concept

The question: when a compressed small model scores worse on a safety or trustworthiness benchmark, how much of the drop belongs to the model and how much to the measuring instrument? Abbas, Zia and Windridge answer with paired tests on eight models below two billion parameters at float16, LLM.int8() and NF4.

## Narrative

**The identity.** Write the measured change as ∆meas = ∆true + ∆inst, where ∆inst is the change in instrument error between the two precisions. Instrument error that is constant across precisions can shrink a paired difference. It cannot create or reverse one. Instrument error that interacts with precision can do both. Only the second kind corrupts a conclusion, and it is usually reported as a quantization effect.

**Three instrument choices that interact with precision.**

1. **Refusal detection.** A keyword detector that misses a phrasing of refusal inflates the apparent safety loss. After calibration against two human annotators, the 4-bit rise in harmful compliance is 2.6 points. A corrected keyword detector records a 4.7-point refusal drop on the same items. The safety effect is about half to two-thirds of the refusal effect.
2. **Scoring protocol.** On identical items, cloze and lettered multiple-choice scoring disagree in sign. For one 1.7B model the 4-bit HaluEval change is +9.8, +0.8, −13.6 and −7.3 points under four protocols. The two protocol classes correlate at ρ = 0.10 against a ceiling of about 0.77. Averaging over option orders does not remove the disagreement.
3. **Batch composition.** LLM.int8() is deterministic but not batch-invariant. Reordering a batch changes 57–119% as many 8-bit answers as quantization from float16 changes. Padding alone changes 2.2–5.6% of 8-bit choices. The cause is rounding activations to 8 bits; NF4 is batch-invariant because it quantizes weights only.

**Calibration at low discrimination.** Of 80 ECE changes, 11 exclude zero, against about 4 by chance. They split 6 improvements to 5 losses with no consistent direction. The two largest reported losses are response-bias shifts, not discrimination losses. Recentring on a cross-fitted intercept turns one 0.154 loss into −0.031. Report a calibration change together with the model's discrimination on that task; otherwise the number measures response bias.

**Operational rules for a lab or a guardrail.** Fix the detector before you report a delta. Fix the option order and the scoring rule. Record the batch shape, and do not compare runs that used different packing. Prefer NF4 when reproducibility across batch shapes matters more than the last point of accuracy. A guardrail or classifier that returns different answers for the same item in a different batch is not a stable control.

**Scope limits.** Eight models under two billion parameters, one human-label set, and common multiple-choice benchmarks. The magnitudes will differ at larger scale. The direction of the artifact — that protocol and batch choices can flip a safety conclusion — is the transferable result. See @concepts/guardrail-construct-validity-agent-eval.md for the wider construct-validity frame.

## Snippets

> "Error that is the same at every precision can shrink a paired comparison but cannot create or reverse an effect. Error that interacts with quantization can do both, and it is reported as an effect of quantization." [Source: arxiv-2611.32848 p.1]

> "Rounding activations to 8 bits is enough to produce this dependence. NF4 is batch-invariant." [Source: arxiv-2611.32848 p.1]
