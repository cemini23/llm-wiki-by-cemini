---
title: "agent-skills-eval — SKILL.md Validation Framework"
type: entity
tags: [tool, skill-eval, nodejs, defer, k38]
keywords: [agent, skills, eval, defer, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - entities/tools/agent-skills.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 4)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/darkrishabh/agent-skills-eval`
- **Tier (per source brief)**: **Defer**
- **License**: License compliance noted in brief (presumed permissive)

## Narrative

Node.js evaluation framework for AI agent skills formatted as SKILL.md per the agentskills.io spec. OpenAI-compatible chat APIs (incl. local Ollama / vLLM). Logs traces; benchmarks prompt interpretation.

### Integration vector

Defer — structurally sound but priority is migrating wiki to Hetzner + finalizing Cemini ingest. Adopt only after core infra is hardened and formal skill-quality measurement becomes a bottleneck.

### Risks

Iterating against paid endpoints accumulates costs. Strict agentskills.io spec compliance may false-negative custom internal skill formats.

[Source: Link Evaluation Brief Trading Stack.docx, URL 4]
