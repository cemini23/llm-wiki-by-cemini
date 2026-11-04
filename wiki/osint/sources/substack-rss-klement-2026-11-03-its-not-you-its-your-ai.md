---
title: "Klement — a single neuron switches an LLM's investment bias"
type: source
tags: [source, newsletter, llm-bias, investment-advice, interpretability, risk]
related: []
maturity: draft
read_status: read
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | It's not you, it's your AI |
| Source | klement (Klement on Investing) |
| Published | 2026-11-03 |
| URL | https://klementoninvesting.substack.com/p/its-not-you-its-your-ai |
| Read status | read |

## Narrative

**The most consequential finding in this newsletter batch.**

A paper by Park et al. (2026), from researchers in South Korea and the US, identifies **a single neuron** in each of several open-weight models whose activation controls the model's **investment bias**.

Models tested: **Qwen3, Llama 4, DeepSeek R1, Gemma 4, Mistral Small.**

By changing that one neuron's activation, the model's recommendation for a single stock or an entire portfolio **flips** — with **no prompt change and no parameter update**.

### The double bind Klement names

He states it precisely:

- **Closed-weight models.** The adviser cannot change the activation parameter, but also **cannot know what the model's bias is**. They get an unknown bias, unmodifiable.
- **Open-weight models.** The parameter can be found and manipulated — which just means **the model carries whatever bias the adviser wants it to have**.

Either way the client's own preferences are not what is being represented. In one case a vendor's bias is invisible; in the other a seller's bias is deliberate and equally invisible to the recipient.

### Why "one neuron" is the alarming part

A bias that requires retraining is at least expensive to introduce and therefore rare. A bias that lives in **one activation value** is:

- trivially adjustable,
- effectively undetectable from outputs alone,
- and not visible in any licence, model card, or benchmark.

Any evaluation that measures a model's advice quality on average will not show this. The same weights produce different recommendations depending on a number nobody reports.

### Relevance here

Any use of an LLM for a directional view — including this workspace's own research summaries — inherits this. The control that survives it is the one already in place: **a recommendation is not evidence; the underlying data and reasoning are.** An agent that can flip its view by changing one activation has no track record worth trusting, only an output worth checking.

**Caveat.** Single source, summary of a paper not read here. The specific neuron, magnitude, and robustness across models are unverified on this page.

## Snippets

> "By changing the activation of this single neuron in the one-weight model, they could switch the investment recommendation for single stocks or entire portfolios without modifying the prompt or updating model parameters." [Source: https://klementoninvesting.substack.com/p/its-not-you-its-your-ai (retrieved 2026-11-03)]

> "In a closed-weight model like the frontier models, advisers can't change the activation parameter but also don't know what the model bias is." [retrieved 2026-11-03]

## Dead Ends

- **Trusting an LLM's directional view as a track record.** One activation value flips it.
