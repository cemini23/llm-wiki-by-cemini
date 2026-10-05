---
title: "PowerBench — Measuring language model bias in power-shifting requests"
type: source
tags: [arxiv, safety, bias, evaluation]
keywords: [2610.02303, power-shifting, refusal, nationality-bias, agent-requester]
related:
  - concepts/k282-agent-eval-wave.md
maturity: draft
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- @concepts/k282-agent-eval-wave.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | PowerBench: Measuring Language Model Bias in Power-shifting Requests |
| Authors | Nicolas Martorell, Wendy Brau, Gonzalo A. Heredia, Tomás Pablo Korenblit, Gaspar Labastié, Tomás Gimenez Molina |
| Type | arXiv paper |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.02303-powerbench-measuring-language-model-bias-in-powe.pdf` |
| Retrieved | 2026-10-05 |
| arXiv | 2610.02303 |
| read-status | read |

## Narrative

The paper introduces PowerBench, an evaluation of how language models assist
with power-shifting (PS) requests. It defines three request types: self-empowerment
(SE), disempowerment (DE), and power grabbing (PG). It adds control (CT) requests
that shift no power but still trigger refusals. The dataset holds 576 English PS
requests and 192 control requests. Each request exists in 8 languages and 18
nationality pairings, and in an AI-agent-user version.

The authors evaluate 24 models: 12 from US developers and 12 from Chinese
developers. They collect 495,936 responses. One automated judge grades every
response. The main findings: average refusal ranges from 1.0% to 35.1%; every
model refuses PG more than DE, and DE more than SE. Refusal of PG triples as the
affected party grows from an individual to a society. Models help others take
power from the US and resist US users taking power from others, but favor the US
when it gains power and nobody loses. An AI-agent requester is refused more than
a human. Language bias is large within a model but cancels across models on
average.

For this workspace: the paper gives a reusable refusal-bias harness for local and
API models. It matters to agent security and red-teaming, because it tests the
model as an actor and tests an AI agent as the requester. It also feeds the local
abliterated LLM lab, where refusal behavior is the object of study. The nationality
and language axes are useful for the web-browsing and multilingual agent work.

[Source: arXiv:2610.02303]

## Snippets

> "We introduce PowerBench, an evaluation of power-shifting requests that distinguishes self-empowerment, disempowerment, and power grabbing, plus a control of refusal-inducing requests that shift no power."
[Source: arxiv-2610.02303-powerbench-measuring-language-model-bias-in-powe.pdf p.1]

> "Average refusal ranges from 1.0% to 35.1%, yet every model refuses PG more than DE and DE more than SE. Refusal of PG triples as the affected party goes from an individual to a society, while we detect no such trend in the control."
[Source: arxiv-2610.02303-powerbench-measuring-language-model-bias-in-powe.pdf p.2]

> "When the user is an AI agent, refusal of power-shifting requests increases, especially in power grabbing against an individual."
[Source: arxiv-2610.02303-powerbench-measuring-language-model-bias-in-powe.pdf p.1]

> "We show that language models are biased in power-shifting requests. Some of these biases are specific to power-shifting scenarios and others are not, but all of them could alter the flow of power in society when models are used at scale."
[Source: arxiv-2610.02303-powerbench-measuring-language-model-bias-in-powe.pdf p.10]
