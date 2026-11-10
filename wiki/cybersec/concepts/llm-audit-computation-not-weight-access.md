---
title: "An LLM audit needs computation, not weight access"
type: concept
related:
  - sources/arxiv-llm-auditors-computation-not-weights-2611.07847.md
updated: 2026-11-10
---

## Raw Concept

Question: **what does a model auditor actually need — the raw weights, or the ability to run code against the model?** From arXiv 2611.07847, a factorial study of access mode and instruction on clinical prediction networks.

## Narrative

A claim circulated that frontier models can read the raw weights of a small network and explain what it computes. The claim mixed two conditions: weights in the prompt with no tools, and analysis by writing and running code. When the two conditions are separated, the capability moves with computation.

| Condition | Result on small networks | Result at 3,457 weights | Result at 38,401 weights |
|---|---|---|---|
| Weights in prompt, no tool | recovered 6/6 planted relationships at 353 weights | unstable; repeats disagreed | not tested |
| Calculator, white box | recovered | recovered 3/3 | recovered 3/3 |
| Calculator, black box (predictions only) | recovered | recovered 3/3 | recovered 3/3 |

With the calculator, 29 of 29 runs recovered the planted relationship, 15 null runs produced no false alarm, and a biased-label subgroup was found in 6 of 6 runs. A well-written script matched the comparator models on the audit.

### The security reading

Three points carry over to defensive work.

**White-box weight access is not a prerequisite for auditing what a model computes.** An auditor with a prediction function and a sandbox can reach the same answer. A vendor that offers only an inference endpoint is not withholding the audit, but it does withhold the raw file.

**A native "weight reading" claim needs the tool condition stated.** A result produced with a code tool is a result about tool use, not about weight perception.

**Elicitation is part of the measurement.** Under a one-sentence default instruction, 11 of 12 audit and repair runs declined as unidentifiable. The refusals were correct mathematics and operationally useless. One paragraph of explicit instruction removed them without adding false alarms. Any harness that depends on a model choosing an unstated option needs that paragraph.

### Where this does not transfer

The networks are small tanh multilayer perceptrons on simulated clinical data. The largest is 38,401 weights. Nothing here shows that the result holds for a language model with billions of parameters. The authors state the case for clinical model auditing only.

Confidence: the size boundary and the access-equivalence result are `[TENTATIVE]` — one study, one model family, simulated data.

## Snippets

> "Black-box access performed as well as white-box access, and other GPT-6 models read as accurately. A well-designed script matched the comparator models on the audit and the best LLM repair." [Source: arxiv-2611.07847-computation-not-weight-access-large-language-mod.pdf p.1]

> "Under the default instruction, 11 of 12 audit and repair runs declined (95% interval 0.65–0.99). ... Under the explicit instruction, with every prompt unchanged, none of 14 audit and repair runs declined." [Source: arxiv-2611.07847-computation-not-weight-access-large-language-mod.pdf p.6]
