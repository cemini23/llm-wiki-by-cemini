---
title: "VAKRA — Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies"
type: source
tags: [arxiv, k235, tool-use, benchmark, api, retrieval, policy, ccc, cyber]
keywords: [2608.12282, VAKRA, IBM, multi-hop, tool-policies, API-reasoning, ReAct]
related:
  - entities/tools/vakra.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: skimmed
---

## Relations

- @entities/tools/vakra.md — CC BY-NC-SA 4.0, reference-only
- @concepts/agent-toolkit-routing-research-backlog.md — K235 bump: language-mediated reasoning is the bottleneck

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.12282 (2026-08-12) |
| Authors | Naik, Murthi, Elder, Huo, Gupta, Jain, Venkateswaran, Adebayo, Contractor (IBM Research) |
| sha256 | `83e498ad149d55361be35a5a3e999b561f6d98f003e7e3f68e4b26b37b624cf4` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.12282-vakra-evaluating-multi-hop-reasoning-across-apis.pdf` |
| retrieved | 2026-08-13 |

## Narrative

IBM benchmark: **8,000+ executable APIs across 62 domains**, three difficulty settings — diverse API interaction styles, multi-hop reasoning over structured APIs, multi-source reasoning under **natural-language tool-use policy constraints**. Correctness verified by **re-executing predicted tool calls against live APIs**, accommodating multiple valid paths. Fixed ReAct harness isolates model capability from agent architecture.

Results: best model 70.4% on single-hop endpoint tasks → **50–51% on compositional APIs**; performance degrades >50% as reasoning depth increases; policy-constrained questions expose severe failures (**as low as 2.4% on unanswerable queries**). Trace analysis: failures concentrate at **language-mediated reasoning** — entity disambiguation, cross-source grounding — not tool-invocation mechanics. Repo `github.com/IBM/VAKRA` (**CC BY-NC-SA 4.0** — reference only, no clone); dataset `huggingface.co/datasets/ibm-research/VAKRA`.

Relevance: CCC /route (tool-policy composition is the weakest agent capability — policy wiring order matters) + cyber (policy-constrained tool-use eval surface for the local lab's harness).

[Source: arXiv:2608.12282]

## Snippets

> "even the best model achieves only 70.4% on single-hop endpoint-style tasks and drops to 50–51% on compositional APIs; performance degrades by over 50% as reasoning depth increases" [Source: arXiv:2608.12282 p.1]

> "failures concentrate at language-mediated reasoning — entity disambiguation, cross-source grounding, rather than tool invocation mechanics" [Source: arXiv:2608.12282 p.1]
