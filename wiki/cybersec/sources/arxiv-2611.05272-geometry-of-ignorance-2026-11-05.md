---
title: "The geometry of ignorance — separating suppression from genuine absence"
type: source
tags: [source, arxiv, interpretability, unlearning, knowledge, probing]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-05
updated: 2026-11-05
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Geometry of Ignorance: Detecting Suppressed Knowledge in LLMs through Activation Fragmentation |
| Authors | Adar Peleg, Dvir Alsheich, Tomer Ashuach, Avi Mendelson (Technion) |
| arXiv | 2611.05272 |
| Pages | 27 |
| Read status | skimmed (abstract) |

## Narrative

**The problem it names is the one behavioural evaluation cannot solve:** a model that refuses to answer may still **harbour recoverable knowledge**. A refusal is a behaviour; it is not evidence of absence.

### The method

It measures the **geometric coherence of "anon-vectors"** — the differences in hidden states between a concept-specific query and its anonymised paraphrase.

The finding: **genuine knowledge forms a tight, low-entropy cluster**, while **ignorance forces geometric fragmentation**.

Across **ten instruction-tuned LLMs from three model families**, all fragmentation metrics reliably separate known from unknown concepts.

### The unlearning result, and its honest caveat

After unlearning, fragmentation geometry **correlates with adversarial recovery** across four attack types and five unlearning algorithms — but the authors state plainly that **the direction of that relationship depends on attack methodology**.

That is an unusually careful thing to publish. The headline would be "geometry predicts recovery"; the actual claim is "geometry is informative about recovery, with a sign that flips by attack type". The second is much less useful and much more likely true.

A layer-resolved analysis shows different adversarial mechanisms exploit this geometry at **varying depths**, with attack-specific correlations **invisible to behavioural evaluation**.

### Why it matters here

Any claim that a model "does not know" something — an unlearned capability, a scrubbed fact, a removed refusal direction — is a behavioural claim until something geometric backs it. This gives the geometry.

It also bears on the single-neuron investment-bias finding in this workspace: if knowledge can be suppressed and recovered, then so can bias. A model whose bias is not exhibited is not a model without one.

**Caveat.** Abstract only; no separation accuracy reproduced.

## Snippets

> "A model that refuses to answer may still harbor recoverable knowledge." [Source: arxiv-2611.05272 p.1]

> "The direction of that relationship is shown to depend on attack methodology." [Source: arxiv-2611.05272 p.1]

## Dead Ends

- **Reading a refusal as absence of knowledge.** That is the assumption the paper breaks.
