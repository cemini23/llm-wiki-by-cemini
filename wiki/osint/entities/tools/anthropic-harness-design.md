---
title: "Anthropic harness-design blog — Planner/Generator/Evaluator (Steal-from, Cemini-direct)"
type: entity
tags: [tool, blog, anthropic, harness-design, planner-generator-evaluator, sprint-contract, cemini-direct, steal-from, gemini-eval-doc2]
keywords: [anthropic harness design, planner generator evaluator, sprint contract, structured handoff, langgraph adaptation, agents/orchestrator.py]
related:
  - sources/evaluating-project-links-systems-2-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/conductor-orchestrator.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
maturity: draft
created: 2026-05-12
updated: 2026-06-01
gemini_eval_doc2_url: 11
phase_0_verdict: STEAL-FROM 2026-05-12 (Planner/Generator/Evaluator trinity — Cemini-direct integration)
---

## Relations

- `@sources/evaluating-project-links-systems-2-2026-05-12.md` — source eval (URL 11)
- `@concepts/conductor-orchestrator.md` — Cemini orchestrator integration target

## Raw Concept

- **URL**: `anthropic.com/engineering/harness-design-long-running-apps` (March 24, 2026)
- **License**: proprietary (blog post, fair-use methodological extraction)
- **Tier**: Steal-from
- **Primary fit**: Cemini financial (✅ — only ✅ on Cemini in Doc 2)

## Narrative

Anthropic core engineering blog on harness design for long-running agents. Three load-bearing patterns: **Planner/Generator/Evaluator trinity** (separated agent roles with explicit handoff), **Sprint Contract mechanism** (scoped work blocks with success criteria), **structured handoff artifacts** (typed JSON blobs gated by Evaluator).

### Integration vector

Direct LangGraph adaptation at `agents/orchestrator.py`. Specific extension: add a GAN-style adversarial Evaluator node that gates state transitions on MCP-driven verification calls. Re-write blog patterns into Cemini-specific docstrings on existing orchestrator nodes.
