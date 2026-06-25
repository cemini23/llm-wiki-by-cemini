---
title: "The Metanym Game — LLM peer-community benchmark (arXiv 2606.21008)"
type: source
tags: [source, arxiv, benchmark, llm-evaluation, structural-intelligence, k129]
keywords: [2606.21008, Metanym, spectral rating, GPQA Diamond, contamination-resistant, council-of-peers]
related:
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - sources/arxiv-poker-arena-multi-axis-2606.13815-2026-06-18.md
  - sources/arxiv-agentbeats-aaa-assessment-2606.13608-2026-06-12.md
  - concepts/high-signal-paper-patterns.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-06-25
clusters: [llm-agents]
---

## Relations

- @concepts/poker-arena-multi-axis-cognitive-profile.md — multi-axis vs scalar leaderboard parallel
- @sources/arxiv-poker-arena-multi-axis-2606.13815-2026-06-18.md — poker multi-axis eval (K122)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Metanym Game: A Self-Contained, Self-Consistent LLM Peer-Community Benchmark for Structural Intelligence |
| **Authors** | David Nordfors |
| **arXiv** | 2606.21008v1 (Jun 2026) |
| **sha256** | `42585a4d8daeb0b08420f724df534ca9d2827eaec5135fa1b74d3e09445e7f88` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.21008-2606-21008v1-the-metanym-game-a-self-contained-s.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + rating mechanism) |

## Narrative

**Metanym game:** competitive word game where LLMs **create** analogical content (no fixed test set → contamination-resistant). **Council-of-peers:** contestants also rate each other's outputs.

**Spectral solution:** single SVD on evaluators' ratings matrix yields competence as both **generators** and **judges** of factual statements without golden keys. Factual rating correlates with GPQA Diamond at **r = 0.92** [TENTATIVE — single paper claim].

**Generator/judge dissociation:** strongest generators can be middling judges; sharpest judge may be mid-pack generator — judging scarcer than generating.

**Self-contained gauge:** strongest players form contestable official council; benchmark stable over time.

**Cemini posture:** **REFERENCE** — peer-rating + multi-axis dissociation steal for poker-arena evaluator design; not a prod benchmark install.

## Snippets

> "No content is given in advance; the contestants create all of it — a new kind of analogy test … with no fixed test set to leak into training." [Source: arXiv:2606.21008 abstract (retrieved 2026-06-25)]

> "One singular value decomposition of the evaluators' ratings matrix yields their competence as both generators and judges of true statements at once." [Source: arXiv:2606.21008 abstract (retrieved 2026-06-25)]

> "Making and judging dissociate — judging is the scarcer skill." [Source: arXiv:2606.21008 abstract (retrieved 2026-06-25)]

## Dead Ends

- Word-game domain ≠ poker action space — steal is **evaluation topology**, not task transplant.
