---
title: "Deferred Semantic Commitment — split the claim from its endorsement to pass a guardrail"
type: concept
maturity: draft
related:
  - sources/arxiv-deferred-semantic-commitment-2611.25929.md
  - concepts/recognition-refusal-gap.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/crescendo-multi-turn-jailbreak.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: how does a message keep its harmful content and still pass an element-level filter? From 2611.25929.

## Narrative

A message has two parts: the proposition it states, and whether the speaker commits to it. "They are stealing our jobs" asserts and endorses. "They are stealing our jobs?" raises the same proposition without endorsing it. A check mark or a "Yes" restores the endorsement.

Deferred Semantic Commitment (DSC) is the pattern where commitment is withheld in one element and supplied in another. The completed message endorses the proposition as fully as the assertion. But none of its elements is an assertion.

**Measured on gpt-image-2 and a 300-case set.**

| Condition | Image generated | Image endorses the claim |
|---|---|---|
| Direct statement | 16.3% | 15.3% |
| Question plus affirmation | 43.3% | 41.3% |

**Why the guardrail misses it.** In an open-weight model where the affirmation is a following "Yes", the model reads the reaffirmed input as endorsing and harmful. It still does not refuse. Reaffirmation restores the meaning and only partially reverses the refusal-related change from questioning. Restoring the remaining difference recovers refusal.

**Design rule.** Screen the completed message, not its individual elements. Any safeguard that scores propositions and commitment separately can be split.

**Related families.** DSC is one case of splitting a harmful message across parts. Others split across prompt attributes, successive edits, conversation turns, or image and text. The common defense is to reconstruct the whole before the decision.

**Defensive note for a lab.** Test guardrails with reconstructed messages. A filter that blocks the assertion but passes the question-plus-affirmation is a false sense of coverage.

[Source: arxiv-2611.25929-question-then-affirm-restoring-commitment-does-n.pdf]

## Snippets

> "Safety behavior follows only the withdrawal."
[Source: arXiv:2611.25929v1 abstract]
