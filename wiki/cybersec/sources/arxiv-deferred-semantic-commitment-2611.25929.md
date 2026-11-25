---
title: "Question, Then Affirm — Deferred Semantic Commitment bypasses image guardrails (2611.25929)"
type: source
maturity: draft
related:
  - concepts/deferred-semantic-commitment.md
  - concepts/recognition-refusal-gap.md
  - concepts/guardrail-construct-validity-agent-eval.md
updated: 2026-11-22
read_status: read
---

## Raw Concept

- **Title:** Question, Then Affirm: Restoring Commitment Does Not Restore Refusal
- **Authors:** Haoyang Xu, Qirui Wang, Liuwan Zhu (University of Hawai'i at Manoa; independent)
- **Type:** arXiv preprint (cs.CR)
- **Location:** `research to be indexed/cybersec/arxiv-2611.25929-question-then-affirm-restoring-commitment-does-n.pdf`
- **Retrieved:** 2026-11-20
- **arXiv:** 2611.25929v1, 19 November 2026
- **Read status:** read — 8 of 12 pages extracted 2026-11-22

## Narrative

A sign that states a harmful proposition is blocked. The same proposition phrased as a question, followed by a check mark, is generated. The image endorses the original claim.

The authors call this Deferred Semantic Commitment (DSC). A message has two parts: the proposition, and whether the speaker commits to it. A question withholds commitment. A separate affirmation restores it. Safety behaviour follows the withdrawal but not the restoration.

Numbers on a 300-case challenge set. gpt-image-2 returns images for 43.3% of question-affirmation requests against 16.3% of direct statements. It endorses the original proposition in 41.3% of cases against 15.3%.

To see why, the authors study an open-weight language model where the affirmation is a following "Yes". The model reads the reaffirmed input as endorsing and harmful. It still does not refuse. Reaffirmation restores the meaning but only partially reverses the refusal-related change introduced by questioning. Restoring the remaining difference recovers refusal.

The defensive lesson is a design rule. A safeguard must assess the completed message, not its individual elements. Element-level screening lets an attacker split commitment from content. The result is the same class as recognition without refusal: the system represents the harm and still acts.

[Source: arxiv-2611.25929-question-then-affirm-restoring-commitment-does-n.pdf]

## Snippets

> "A sign stating a harmful proposition is blocked, but the same proposition phrased as a question and followed by a check mark is generated, even though the resulting image endorses the original claim."
[Source: arXiv:2611.25929v1 abstract]

> "These findings reveal a mismatch between recovered meaning and refusal behavior, motivating safeguards that assess the completed message rather than its individual elements."
[Source: arXiv:2611.25929v1 abstract]
