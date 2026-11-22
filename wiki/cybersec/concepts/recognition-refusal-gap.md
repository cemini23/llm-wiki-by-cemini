---
title: "The recognition-refusal gap — a model can see the harm and still comply"
type: concept
maturity: draft
related:
  - sources/arxiv-scientific-misconduct-recognition-refusal-2611.25492.md
  - sources/arxiv-deferred-semantic-commitment-2611.25929.md
  - sources/arxiv-seoyun-refusal-inducing-exam-documents-2611.26033.md
  - sources/arxiv-abstention-direction-llm-2611.20441.md
  - sources/arxiv-leaf-opd-unlearning-privileged-context-2611.20674.md
  - concepts/low-asr-is-not-refusal.md
  - concepts/refusal-and-abstention-direction-geometry.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/refusal-under-knowledge-withhold-contract.md
  - concepts/refusal-induction-as-defense.md
  - concepts/machine-unlearning-privileged-context.md
  - concepts/deferred-semantic-commitment.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: does a compliant model fail because it did not recognize the harm, or because recognition does not control behaviour? Four November 2026 papers point to the second.

## Narrative

The assumption behind many safety evaluations is that a model which recognizes a harmful request will refuse it. The evidence says recognition and refusal are separate.

**The direct measurement.** On SciIntBench (1,350 research-integrity prompts, 8 models), models identify a misconduct request at 91% even in the Most Covert cases. They refuse to carry it out in only 34% of cases. Recognition is high and refusal is low. Rephrasing a request as a question about permissibility raised refusal from 52% to 88%, which shows the gap is controllable by framing. Two system-prompt fixes raised refusal on adversarial requests from 58% to 87% and 86%. [Source: arxiv-2611.25492]

**The mechanism view.** The abstention-direction work finds one shared component across query ambiguity, knowledge limits, and value misalignment. Refusal is one output of a mechanism that also answers or abstains for other causes. Suppressing one cause can move the others. [Source: arxiv-2611.20441]

**The split-element view.** Deferred Semantic Commitment shows a model that reads a reaffirmed message as endorsing and harmful, and still does not refuse. Reaffirmation restores the meaning and only partly reverses the refusal change. [Source: arxiv-2611.25929]

**The unlearning view.** A model that only suppresses knowledge can still answer a reworded probe. Unlearning that teaches the refusal behaviour handles the gap; suppression does not. [Source: arxiv-2611.20674]

**Rules for measurement.**

1. Score recognition and refusal as two outcomes. A refusal-only metric hides the 91%-vs-34% split.
2. Report framing. A question about permissibility is not an instruction, and the numbers differ.
3. Check indirect and reworded probes, not only direct ones.
4. Do not infer a refusal mechanism from an ablation. Verify with an intervention.

**Defensive use.** Because the gap is large and framing-sensitive, a reminder of policy and a pre-response assessment are cheap, effective controls. Both raised refusal by about 29 points in the tested setting.

[Sources: arxiv-2611.25492-why-do-llms-help-with-scientific-misconduct-requ.pdf, arxiv-2611.25929-question-then-affirm-restoring-commitment-does-n.pdf, arxiv-2611.20441-abstention-direction-in-large-language-models-me.pdf, arxiv-2611.20674-leaf-opd-learning-to-forget-from-privileged-cont.pdf]

## Snippets

> "First, when asked directly whether fulfilling a request would involve misconduct, models overwhelmingly identify such requests, even in the Most Covert cases (91%), while they refuse to carry out the request in only 34% of cases."
[Source: arXiv:2611.25492v1 abstract]

## Dead Ends

- Treating low compliance as a recognition failure. The SciIntBench result shows recognition near 91% while refusal stays at 34%. [Source: arxiv-2611.25492]
