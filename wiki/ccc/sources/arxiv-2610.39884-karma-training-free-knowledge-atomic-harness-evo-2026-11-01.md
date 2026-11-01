---
title: "KARMA: training-free knowledge-atomic harness evolution"
type: source
tags: [source, arxiv, llm-agents, harness-evolution, training-free]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising Agents |
| Authors | Xinhua Miao et al., Alibaba International Digital Commerce Group |
| arXiv | 2610.39884 |
| File | `arxiv-2610.39884-karma-training-free-knowledge-atomic-harness-evo.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.39884 |
| Read status | skimmed (abstract + intro) |

## Narrative

Industrial advertising agents must keep decision knowledge current as product offerings, traffic patterns, and operating policies change. The introduction says web-marketplace merchants choose which products to promote, how much budget to allocate, and how aggressively to bid. LLM agents retrieve business evidence and combine it with operating knowledge. Their recommendations depend on rules that can become incomplete or outdated. A rule update can change the selected control (budget, bid, or item) and the direction of the intervention.

KARMA (Knowledge-Atomic, Regression-Gated Modular Adaptation) is a training-free framework. It evolves six typed knowledge modules. Model weights stay frozen. Executable harness code stays frozen. A deterministic Trace Verifier maps observed errors to candidate modules. A Critic compares successful and failed trajectories and guides a tool-constrained Evolver. The Evolver applies atomic knowledge edits. A fixed validation gate keeps an edit only when the measured gain reaches a threshold. If the gain stays below that threshold, the gate restores the previous knowledge state.

The authors evaluate KARMA with three LLM families. Cases come from a corpus of approximately half a million real-world operation logs across six e-commerce domains. Across 18 domain–model settings, the paper reports that KARMA raises the average hold-out score from 30.19 to 39.15 (+8.96 points, +29.7%). Ablations show that removing either successful or failed trajectories more than halves the average hold-out gain. Evolved knowledge transfers across domains without further adaptation. The paper reports an average hold-out gain of 8.54 points across all source–target pairs. These figures come from this paper alone.

For an AI-agent and coding-harness practitioner, the paper separates frozen executable harness code from editable knowledge. Retained patches stay linked to their diagnostic evidence and validation outcomes. The paper says this supports inspectable, reversible knowledge adaptation for agents in web marketplaces.

## Snippets

> "We present KARMA (Knowledge-Atomic, Regression-Gated Modular Adaptation), a training-free framework that evolves six typed knowledge modules while keeping model weights and executable harness code frozen. Across 18 domain–model settings, KARMA raises the average hold-out score from 30.19 to 39.15 (+8.96 points, +29.7%)." [Source: `arxiv-2610.39884-karma-training-free-knowledge-atomic-harness-evo.pdf` p.1 (arXiv 2610.39884), retrieved 2026-11-01]
