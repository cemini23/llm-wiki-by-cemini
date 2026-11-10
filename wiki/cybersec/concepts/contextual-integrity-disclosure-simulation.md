---
title: "Contextual integrity simulation: need is not entitlement"
type: concept
related:
  - sources/arxiv-contextual-integrity-generative-2611.08284.md
updated: 2026-11-10
---

## Raw Concept

Question: **why do people and models disclose private information to a party that should not receive it?** From arXiv 2611.08284, an LLM-actor simulation of information sharing under contextual integrity theory.

## Narrative

Contextual integrity (CI) holds that the appropriateness of a disclosure depends on the norms of the setting, not on the data. The model has five parameters: sender, subject, recipient, information type, and transmission principle.

Two questions decide the correct response.

1. Does the current context call for this information?
2. Is this person entitled to receive it, in this interaction, for this purpose?

Their combination gives four scenario types. Sharing is appropriate only when both answers are yes.

| Type | Context needs it | Recipient entitled | Appropriate response |
|---|---|---|---|
| I | no | no | withhold |
| II | no | entitled elsewhere only | withhold |
| III | yes | no | withhold |
| IV | yes | yes | share |

### The failure mode is Type III

In the simulation, holders withheld in every Type I conversation and shared in every Type IV conversation. The informative result is Type III: a real process required the information, and the asker was not entitled to receive it. Holders **disclosed** in most Type III conversations. Sharing was more common in Type III than in Type II.

This is the shape of a social-engineering pretext. The attacker states a genuine need and claims a role that would normally receive the information. A holder who checks only "is this needed?" answers yes and stops.

### Decision logic changes the outcome

Two decision logics are compared. The **basic** logic asks what kind of situation this is, what kind of person I am, and what a person like me would do. The **rational** logic compares actions by expected consequence.

In one illustration, a rational holder disclosed a tax number because disclosure was "the most efficient path forward", even though the task did not require it. A basic holder in the same scenario questioned the request and proposed a business identifier instead. The authors present this as an illustration, not as evidence that one logic is safer.

### The over-refusal cost

Disposition is a separate axis. Trusting actors shared during activities that did not require it. Skeptical actors withheld more often, and their refusal persisted even at Type IV, where sharing is correct. A control that only raises suspicion trades disclosure for blocked legitimate requests.

The CI appropriateness score states this directly. An actor that always withholds scores perfectly on Types I to III and fails every Type IV request.

### How to use this defensively

**For a human-facing control:** test both error directions. A prompt-injection or pretext drill that scores only "did the model withhold" rewards an always-refuse policy. Add Type IV cases where sharing is the correct answer.

**For a threat model:** split "need" from "entitlement" in any verification script. The Type III case fails a check that stops at need.

**For agent design:** a retrieval or data-sharing agent that receives a plausible business justification from an unentitled requester reproduces Type III.

### Limits

Actors are LLMs, not people. Scenario generation and validation also use Gemini models, so generator and actor share a bias. The score measures conformance to the scenario definition, not to surveyed human judgement. The values tested are SSNs, bank accounts, home addresses, birth dates and marital status.

Confidence: `[TENTATIVE]` — one simulation study, no human-subject baseline.

## Snippets

> "In Type III, holders disclosed information to an asker who had no right to receive it, even though a real process required that information. The model can therefore generate scam-like conversations in which an asker uses a need to make an inappropriate request." [Source: arxiv-2611.08284-a-generative-model-of-contextual-integrity-appro.pdf p.3]

> "An actor that always withholds would score perfectly on Types I to III while failing every Type IV request." [Source: arxiv-2611.08284-a-generative-model-of-contextual-integrity-appro.pdf p.3]
