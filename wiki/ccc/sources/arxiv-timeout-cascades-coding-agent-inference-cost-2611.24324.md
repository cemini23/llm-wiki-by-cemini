---
title: "Reducing inference cost of coding agents with timeout cascades"
type: source
related:
  - concepts/timeout-cascade-cost-aware-routing.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/token-economics-and-prompt-caching.md
  - entities/skills/route.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Reducing Inference Cost of Coding Agents with Timeout Cascades |
| Author | Boxi Zhou, German Sviridov, Dmitrii Ustiugov, Haris Javaid (AMD, NTU) |
| Type | arXiv paper (cs.AI), 2611.24324 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.24324-reducing-inference-cost-of-coding-agents-with-ti.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 10 |
| Read status | read |

## Narrative

The paper evaluates 36 open-weight models released since mid-2024 on SWE-bench Verified with a fixed `mini-swe-agent` scaffold, served on AMD MI300X GPUs.

The accuracy gap between small and large models is not spread evenly. Small models are competitive on easy and medium tasks and weak on hard tasks. The authors exploit this shape with a **timeout cascade**: run the small model first, and escalate to the large model only when the small model fails or times out.

Reported results: up to 33% reduction in total GPU-hour cost, and 16.4% on all SWE-bench Verified tasks, with no accuracy loss. The cascade nearly matches an oracle task router.

The operational point is that a simple cascade is enough. A learned difficulty router adds complexity and buys little. [TENTATIVE] single source; results are vendor-authored by AMD researchers.

For Cemini this is the closest published evidence for the `/route` design. The `easy·mid·hard·money` lanes already send easy work to DeepSeek Flash. A timeout-based escalation rule is the cheap next step, and it needs no learned classifier.

## Snippets

> "By utilizing a hybrid inference strategy that tries a small model first and escalates to a large one only when needed, we can achieve up to 33% reduction in total GPU-hour costs and 16.4% on all tasks from SWE-bench Verified, without sacrificing accuracy." [Source: arxiv-2611.24324-reducing-inference-cost-of-coding-agents-with-ti.pdf p.1]
