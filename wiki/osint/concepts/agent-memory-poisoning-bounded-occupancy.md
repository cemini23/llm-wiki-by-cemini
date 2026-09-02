---
title: Agent memory poisoning — bounded occupancy + write-path grounding
type: concept
tags: [agents, memory, security, ccc-k304]
keywords: [memory poisoning, provenance, LongMemEval, content screening]
related:
  - sources/arxiv-2608.21230-agent-memory-poisoning.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
harness_verb: FILE
---

## Relations
- @sources/arxiv-2608.21230-agent-memory-poisoning.md

## Raw Concept
K246 source: arXiv 2608.21230 + CCC K304 policy wires (Aug 2026 federation batch).

## Narrative
Content screening cannot see payload-free lies: high injection recall coexists with zero refusal of plain false assertions. Small poison rates collapse long-memory eval accuracy. Additive provenance ranking lacks a usable weight — use provenance as **bounded occupancy** on retrieved context instead. External grounding is required before persistent writes; truth is not a text property alone.

## Snippets
> Poisoning 1.2% of a LongMemEval corpus reduces accuracy from 0.850 to 0.300. [Source: arxiv-2608.21230 abstract (retrieved 2026-08-25)]
