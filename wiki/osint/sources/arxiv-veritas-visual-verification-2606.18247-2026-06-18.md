---
title: "VERITAS — Visual Verification for Inference-time Steering — arXiv 2606.18247"
type: source
tags: [source, arxiv, robotics, verifier, self-improvement, k123]
keywords: [2606.18247, VERITAS, generator-verifier, inference-time steering, Best-of-N, policy improvement]
related:
  - sources/arxiv-probabilistic-agent-verification-2606.20510-2026-06-21.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/llm-agent-systems.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - sources/arxiv-red-queen-godel-machine-2606.26294-2026-06-29.md
maturity: draft
read_status: read
created: 2026-06-18
updated: 2026-10-25
clusters: [llm-agents]
---

## Relations

- @concepts/generator-verifier-inference-time-steering.md — K123 synthesis
- @concepts/continual-harness-online-self-improvement.md — online self-improvement sibling (harness vs verifier)
- @concepts/poker-arena-multi-axis-cognitive-profile.md — multi-axis eval as verifier analog for poker
- @concepts/devfun-poker-agent-challenge-2026.md — Cemini steal target

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement |
| **Authors** | Mingtong Zhang, Dhruv Shah |
| **arXiv** | 2606.18247 (16 Jun 2026) |
| **sha256** | `1174fb20f0f7fe9982b8adf30da6c78e062d46c6e23ee3ae68b1b6ca0e17c4c3` |
| **Project** | https://veritas-improvement.github.io/ [NEEDS VERIFICATION 2026-06-18] |
| **Repo** | none public at ingest time |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.18247-2606-18247v1-visual-verification-enables-inferen.pdf` |
| **Retrieved** | 2026-06-18 (daily digest 2026-06-19 inbox) |
| **Read status** | read (abstract + mechanism summary) |

## Narrative

**VERITAS** pairs a pre-trained **generator** policy (proposes candidate action chunks) with a gradient-free **visual verifier** that scores outcomes at **inference time**. **Best-of-N** selection steers execution without weight updates; verified rollouts accumulate into **D_auto** for offline behavior-cloning fine-tuning — reportedly comparable sample efficiency to expert demos without human labels.

**Reported gains [TENTATIVE — paper claims]:** inference-time verification beats vanilla generalists without extra demo data; verified self-rollouts match expert-demo fine-tuning efficiency on robot manipulation benchmarks (π₀ family).

**Cemini posture:** **REFERENCE / steal-from pattern** — not a robotics install. Poker analog: `decide()` as generator + **deterministic verifier stack** (legality, regression oracle, MC equity, axis proxies) for inference-time steering; Researcher trajectories as **D_auto** for HL loop. Phase-0: no OSS repo → REFERENCE until `veritas-improvement` publishes code + license.

## Snippets

> "We use a pre-trained generalist robot policy as a `generator' and pair it with a gradient-free `visual verifier' that evaluates actions at inference time." [Source: arXiv:2606.18247 abstract (retrieved 2026-06-18)]

> "Post-training with verified rollouts achieves comparable efficiency to expert demonstrations, while requiring no human interventions." [Source: arXiv:2606.18247 abstract (retrieved 2026-06-18)]

## Dead Ends

- **Visual** verifier assumes camera observations — poker state is symbolic; steal is **verifier-at-inference** architecture, not pixel pipeline.
- No GitHub license to audit — do not Adopt until repo ships.
