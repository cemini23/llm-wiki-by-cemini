---
title: "SEOYUN — refusal-inducing exam documents for AI-glasses pipelines (2611.26033)"
type: source
maturity: draft
related:
  - concepts/refusal-induction-as-defense.md
  - concepts/recognition-refusal-gap.md
updated: 2026-11-22
---

## Raw Concept

- **Title:** SEOYUN: Refusal-Inducing Exam Documents for AI-Glasses Pipelines
- **Author:** Dohyeon Raphael Kwon (PEACE-UNIVERSE, Cheongju, Republic of Korea)
- **Type:** arXiv preprint (cs.AI), research framework
- **Location:** `research to be indexed/cybersec/arxiv-2611.26033-seoyun-refusal-inducing-exam-documents-for-ai-gl.pdf`
- **Retrieved:** 2026-11-20
- **arXiv:** 2611.26033v1, 19 November 2026
- **Read status:** read — 8 of 10 pages extracted 2026-11-22

## Narrative

Camera-equipped glasses turn an exam page into a query for a vision-language model. A device ban addresses possession. This paper asks a different question: can the examination document itself make unauthorized machine capture less useful.

The proposal is refusal-inducing exam documents. The authors call the objective reverse jailbreaking: raise abstention where a jailbreak seeks compliance. They are explicit that refusal induction and defensive visual prompt injection already have precedents. The contribution is a threat model, analytical limits, and an evaluation protocol for examinations.

Three analytical points:

- Refusal differs from correct-answer leakage. Answer suppression is the target, not the model's politeness.
- Removing an added dummy option is not a reduction in the original answer space. It removes a distractor, not the answer.
- The sampling comparison needs stated camera assumptions. At alpha = 1 arcminute and viewing distance 350 mm, the geometric detail scale is about 0.102 mm. A 4032-pixel sensor with a 100-degree field of view gives about 0.207 mm per pixel. These are calculations, not device measurements.

The protocol separates digital, simulated, and physical inputs. It requires held-out evaluation after subject-specific selection, so the selection set is not the test set.

Scope is stated plainly. A local CSAT candidate corpus and renderer are prepared. This version reports no model-performance measurements, no physical validation, and no human-subject results. It is a research framework, not a validated defense, and not a basis for allegations against a candidate.

[Source: arxiv-2611.26033-seoyun-refusal-inducing-exam-documents-for-ai-gl.pdf]

## Snippets

> "A device ban, a supervisor's observation, and a radio-frequency survey address whether prohibited equipment is present. They do not determine whether a photographed page yields a useful answer."
[Source: arXiv:2611.26033v1 §1]

> "A proposal to protect examinations must not itself become an unsupported reason to suspect a candidate."
[Source: arXiv:2611.26033v1 §1]
