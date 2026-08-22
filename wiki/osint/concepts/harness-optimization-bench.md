---
title: Harness optimization as first-class capability (HarnessOpt-Bench)
type: concept
tags: [agents, harness, eval, ccc, k226]
keywords: [HarnessOpt-Bench, harness optimization, Scale AI]
related:
  - sources/arxiv-2608.17804-grpo-unlearning.md
  - entities/tools/grpo-llm-unlearning.md
  - sources/arxiv-2608.19902-brain-researcher.md
  - sources/newsletter-rss-latent-space-2026-08-21-simile-simulation.md
  - sources/newsletter-rss-latent-space-2026-08-22-agent-harness.md
  - sources/newsletter-rss-latent-space-2026-08-08-zawinski-multiagents.md
  - concepts/zawinski-law-of-multiagents.md
  - sources/arxiv-2608.06301-harnessopt-bench-2026-08-07.md
  - sources/newsletter-rss-latent-space-2026-08-07-amd-taalas-muse.md
  - entities/tools/anton-mindsdb.md
  - concepts/code-as-agent-harness.md
  - sources/newsletter-rss-latent-space-2026-08-11-muse-glimmer.md
  - sources/arxiv-2608.16798-clawgym-ii-2026-08-18.md
  - sources/arxiv-2608.16859-harnesseval-w-2026-08-18.md
maturity: draft
created: 2026-08-07
updated: 2026-08-22
---

## Relations

- @sources/arxiv-2608.17804-grpo-unlearning.md — K245 GRPO reward ≠ RWKU endpoint
- @entities/tools/grpo-llm-unlearning.md — Apache-2.0 Extract; wont_wire
- @sources/arxiv-2608.19902-brain-researcher.md — K245 neuroimaging harness +70.2 pp tool-select
- @sources/newsletter-rss-latent-space-2026-08-21-simile-simulation.md — K245 Simile 85% twins; verification-gated synthetic flips
- @sources/newsletter-rss-latent-space-2026-08-22-agent-harness.md — K245 Harness-Bench 52.4–76.2; attention-interface
- @sources/newsletter-rss-latent-space-2026-08-11-muse-glimmer.md

- @concepts/zawinski-law-of-multiagents.md — harness > model (K227)

- @sources/arxiv-2608.06301-harnessopt-bench-2026-08-07.md
- @sources/newsletter-rss-latent-space-2026-08-07-amd-taalas-muse.md
- @entities/tools/anton-mindsdb.md
- @concepts/code-as-agent-harness.md

## Raw Concept

Scale AI HarnessOpt-Bench (2608.06301): measure LLMs at improving the **harness** (prompts, tools, control flow, memory, orchestration), not weights alone.

## Narrative

Aligns with Cemini “code as agent harness” + Latent Space Muse/Agent Plugins framing. CCC should track harness-opt protocols when evaluating Cursor/Claude/Grok lane changes. Atto: treat playbook/skill edits as harness changes requiring review (pairs K253).

**K245 (2026-08-22).** Latent Space harness essay: same-model Harness-Bench spread **52.4–76.2 (23.8 pt)**; OpenAI compaction tripled ARC-AGI-3 13.3%→38.3%; next leftover is an **attention-interface** (when to interrupt the human), not more tool wrappers. Simile 85% digital-twin accuracy is a *simulation* eval, not a coding-harness score. GRPO unlearning paper: RWKU forget scores can look successful while the endpoint is refusal collapse — same diagnostic lesson as harness-opt (score the behavior, not the proxy). Brain Researcher OOD neuroimaging, but the +70.2 pp tool-selection lift is another “harness > model” data point. **Do not swap `/route`.** Phase-1 leftover: propose attention-policy surface only — do not edit `.cursor/skills` here.

[Source: arXiv:2608.06301; Latent Space 2026-08-22]
