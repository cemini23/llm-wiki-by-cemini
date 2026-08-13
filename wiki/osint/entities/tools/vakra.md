---
title: VAKRA — multi-hop API/retrieval benchmark (IBM)
type: entity
tags: [entity, tool, benchmark, tool-policy, ccc, cyber, k235, reference]
keywords: [VAKRA, IBM, multi-hop, tool-use-policy, API-benchmark, ReAct-harness]
related:
  - sources/arxiv-2608.12282-vakra-tool-policies-2026-08-13.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/arxiv-2608.12282-vakra-tool-policies-2026-08-13.md — paper
- @concepts/agent-toolkit-routing-research-backlog.md — K235 backlog bump

## Raw Concept

Repo `github.com/IBM/VAKRA` (64★, pushed 2026-08-10); dataset `huggingface.co/datasets/ibm-research/VAKRA`. 8,000+ executable APIs across 62 domains; correctness verified by re-executing predicted tool calls against live APIs.

## Narrative

**Verdict: Reference only — CC BY-NC-SA 4.0** (LICENSE file verified; gh api NOASSERTION). Non-commercial share-alike → no adoption, no clone, no vendored eval use in a commercial stack; usable only as a methodology reference for CCC /route and the cyber lab's tool-policy eval design. Key transferable finding: failures concentrate at language-mediated reasoning (entity disambiguation, cross-source grounding), not tool mechanics — policy-constrained questions expose failures down to 2.4% on unanswerable queries.

[Source: IBM/VAKRA (retrieved 2026-08-13)]
