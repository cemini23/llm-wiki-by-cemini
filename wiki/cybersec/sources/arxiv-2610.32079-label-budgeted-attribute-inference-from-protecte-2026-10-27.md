---
title: "Label-budgeted attribute inference from edge-cloud split MLLM features"
type: source
tags: [source, arxiv, privacy, multimodal]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Label-Budgeted Attribute Inference from Protected Features in Edge–Cloud Split Multimodal LLMs |
| Authors | Junguang Yao, Peichun Hua, Hanxiu Zhang, Yue Zheng — The Chinese University of Hong Kong (Shenzhen) |
| arXiv | 2610.32079 |
| File | `arxiv-2610.32079-label-budgeted-attribute-inference-from-protecte.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32079 |
| Read status | skimmed (abstract + intro) |

## Narrative

Split inference runs the early layers of a multimodal LLM on the device and sends the
intermediate features to a server. Teams often treat this as a privacy win, because the raw
image stays local. The paper shows the win is smaller than assumed. An honest-but-curious
server can infer age, gender and race from the feature vector alone.

The authors argue that prior privacy evaluations are too weak. Most of them measure final
response refusals, or the failure of one fixed classifier. Both understate what an adaptive
server can do.

The contribution is a measurement framework. It reports a **recovery curve**: what share of
the unprotected leakage the server recovers, as a function of its labelled-sample budget.
The curve runs from zero labelled samples (a classifier trained on unprotected features) to a
full labelled set. This measures privacy at the representation level, not at the response level.

Two results follow across two MLLMs:

- In an unprotected pipeline, intermediate features leak all three attributes, **regardless of
  the split depth**. Moving the split does not fix the leak.
- Protection deployed at different stages still leaves the information recoverable under a
  small label budget. Safe-LLaVA removes biometric content from its responses. However, from
  the features it transmits in split inference, **20 labelled samples per class recover 75–85%
  of the unprotected leakage**.

Defensive implication: response-level privacy controls do not protect the wire. A blue team
that deploys split inference should treat the transmitted feature vector as sensitive data,
and should test it against an adaptive attacker with a small label budget. The paper
publishes these figures from its own experiments; treat them as single-source.

## Snippets

> "Safe-LLaVA removes biometric content from the model's responses, but from the features it transmits in split inference, 20 labeled samples per class recover 75–85% of the unprotected leakage." [Source: `arxiv-2610.32079-label-budgeted-attribute-inference-from-protecte.pdf` p.1 (arXiv 2610.32079), retrieved 2026-10-27]
