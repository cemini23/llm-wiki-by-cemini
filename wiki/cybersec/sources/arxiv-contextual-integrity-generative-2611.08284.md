---
title: "A generative model of contextual integrity: appropriate vs. inappropriate information sharing (arXiv 2611.08284)"
type: source
related:
  - concepts/contextual-integrity-disclosure-simulation.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | A Generative Model of Contextual Integrity: Appropriate vs. Inappropriate Information Sharing |
| Author | Omer Ebead (Cooperative AI Foundation; Cape Institute for Safe AI; African Institute for Mathematical Sciences); Claude Formanek (Cooperative AI Foundation; Cape Institute for Safe AI); Joel Z. Leibo (Google DeepMind) |
| Type | arXiv preprint (cs.AI) — NeurIPS 2026 |
| Location | `research to be indexed/cybersec/arxiv-2611.08284-a-generative-model-of-contextual-integrity-appro.pdf` |
| Retrieved | 2026-11-06 |
| File | `arxiv-2611.08284-a-generative-model-of-contextual-integrity-appro.pdf` |
| Pages | 55 |
| Read status | read |

## Narrative

The paper builds a simulation for one question: when is sharing private information appropriate? It uses **contextual integrity** (CI) theory, which holds that appropriateness depends on the norms of the setting and not on the data alone.

### The information-flow model

Each scenario has the five CI parameters: sender, subject, recipient, information type, and transmission principle. Two attributes decide the correct response. The first is whether the current context calls for the information. The second is whether the asker is entitled to receive it in this interaction. Their combination gives four scenario types.

| Type | Context calls for it | Askers role legitimate | Appropriate response |
|---|---|---|---|
| I | No | No | Withhold |
| II | No | Legitimate role in another context | Withhold |
| III | Yes | No | Withhold |
| IV | Yes | Yes | Share |

Sharing is appropriate only in Type IV. The score **CI appropriateness** is the withhold rate over Types I to III and the share rate at Type IV. An actor that always withholds scores perfectly on Types I to III and fails every Type IV request.

### The simulation

Two LLM actors exchange text messages in the Concordia framework, on a simulated forum, collaboration site or messaging service. One actor holds the private value; the other seeks it. A scenario generator produces and validates the situation before the conversation runs.

Two decision logics are compared. The **basic** logic follows the logic of appropriateness: what kind of situation is this, what kind of person am I, and what would a person like me do. The **rational** logic compares actions by expected consequence.

Disposition is set through the holder's memories, as **trusting** or **skeptical**. Four models play the actors: Gemini 2.5 Flash, Gemini 3 Flash Preview, GPT-4o-mini and Llama-4-Maverick.

### Results

Holders withheld in every Type I conversation and shared in every Type IV conversation under the baseline. The informative result is Type III. Holders **disclosed to an asker who had no right to receive the information**, because a real process required that information. Sharing was more common in Type III than in Type II. The model can therefore generate scam-like conversations in which the asker uses a real need to make an inappropriate request.

The rational holder disclosed in one illustration because disclosure was "the most efficient path forward", even though the task did not require it. The basic holder questioned the request and proposed a business identifier instead.

Trusting actors gave out private information during activities that did not require it. Skeptical actors were more reluctant, and their refusal persisted even when the asker was entitled to the information. That is over-refusal at Type IV.

### Defensive reading

The paper gives a measurable structure for social-engineering resistance. The failure mode is not simple gullibility. It is a plausible need plus a plausible process. A holder answers "is this needed?" and stops, without asking "are you the right recipient for this purpose?".

A second defensive use is the over-refusal trade. A skeptical disposition reduces disclosure and also blocks legitimate sharing. A privacy control that only adds refusal will pay that cost.

### Limits

Actors are LLMs, not people. The CI appropriateness score measures conformance to the scenario definition, not to a survey of human judgement. Scenario generation and validation also use Gemini models, so generator and actor share a bias. Values are SSNs, bank accounts and home addresses, plus low-sensitivity items.

## Snippets

> "In Type III, holders disclosed information to an asker who had no right to receive it, even though a real process required that information. The model can therefore generate scam-like conversations in which an asker uses a need to make an inappropriate request." [Source: arxiv-2611.08284-a-generative-model-of-contextual-integrity-appro.pdf p.3]

> "An actor that always withholds would score perfectly on Types I to III while failing every Type IV request." [Source: arxiv-2611.08284-a-generative-model-of-contextual-integrity-appro.pdf p.3]

> "Trusting actors gave out private information while discussing activities that did not require it. Skeptical actors were more reluctant to share, and their refusal could persist even when the person asking was entitled to receive the information." [Source: arxiv-2611.08284-a-generative-model-of-contextual-integrity-appro.pdf p.7]
