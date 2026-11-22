---
title: "Refusal induction as a defense — reverse jailbreaking against unauthorized machine capture"
type: concept
maturity: draft
related:
  - sources/arxiv-seoyun-refusal-inducing-exam-documents-2611.26033.md
  - concepts/recognition-refusal-gap.md
  - concepts/refusal-and-abstention-direction-geometry.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: can a defender raise a model's refusal on purpose, to make an unauthorized capture less useful? From 2611.26033 (SEOYUN). Framework only, no measurements.

## Narrative

A jailbreak seeks compliance. Refusal induction seeks abstention. The objective is the reverse: raise refusal where an attacker wants an answer.

The case is camera glasses against an exam paper. A device ban addresses possession. It does not determine whether a photographed page yields a useful answer. The proposal puts refusal-inducing content on or near the item, so a vision-language model abstains or answers wrongly.

**Three analytical limits the paper states.**

- Refusal is not the same as correct-answer leakage. The target is answer suppression, not politeness.
- Removing an added dummy option is not a reduction in the original answer space.
- The optical comparison needs stated assumptions. At alpha = 1 arcminute and 350 mm, the geometric detail scale is about 0.102 mm. A 4032-pixel sensor at a 100-degree field of view gives about 0.207 mm per pixel. These are calculations, not device measurements.

**Protocol.** Separate digital, simulated, and physical inputs. Hold out the evaluation set after subject-specific selection, so the selection set is not the test set. Do not treat a successful API request as defensive efficacy.

**Honest scope.** A local CSAT corpus and renderer exist. This version reports no model measurements, no physical validation, and no human-subject results. It is a framework, not a validated defense.

**Ethical guardrail.** The technique must not become a reason to suspect a candidate. Success is measured against an identically clean item, with a separate check on human accuracy, time, and comfort, including assistive technology.

**General reading.** Refusal induction is a legitimate defensive direction, and it inherits the recognition-refusal gap. It works only where the defender can reach the model's input and the model has not been tuned to comply with that input. Both are open questions.

[Source: arxiv-2611.26033-seoyun-refusal-inducing-exam-documents-for-ai-gl.pdf]

## Snippets

> "We use reverse jailbreaking to describe the direction of the objective: inducing abstention rather than bypassing refusal."
[Source: arXiv:2611.26033v1 abstract]

## Dead Ends

- **OPEN QUESTION 2026-11-22:** No efficacy numbers exist yet. Digital L3 pilot, optical lighting, encoder textures, and human legibility are future stages. [Source: arxiv-2611.26033 §1]
