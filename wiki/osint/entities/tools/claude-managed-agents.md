---
title: "Claude Managed Agents — Anthropic Hosted Agent Infrastructure"
type: entity
tags: [tool, anthropic, managed-agents, saas, vendor-lock-in, reference-only]
keywords: [Claude Managed Agents, Anthropic, hosted agents, multi-agent, vendor lock-in, pricing]
related:
  - sources/eval-url-revenue-plan-20url-2026-07-08.md
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-07-08
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 12)

## Raw Concept

Anthropic's hosted infrastructure for multi-agent coordination. Stateful agent sessions, tool execution, $0.08/session-hour pricing.

- **Site**: `claude.com/form/claude-managed-agents`
- **License**: Proprietary SaaS
- **Pricing**: $0.08/session-hour (per Verdent Guides, 2026)

## Narrative

**Verdict: Reference-only.** Claude Managed Agents represents the cutting edge of hosted agent infrastructure, but deploying it requires sacrificing both architectural autonomy (current LangGraph orchestrator replaced by Anthropic's proprietary state engine) and operational capital (per-session-hour pricing at scale). The vendor lock-in risk is severe — trading logic built into Anthropic's state engines cannot be ported if pricing changes or models are deprecated.

The product's architectural patterns (stateful agent sessions, multi-agent coordination protocols) are worth studying, but Cemini's existing linear 4-node LangGraph StateGraph + DeepSeek architecture remains the correct path for maintaining agnostic flexibility.

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 12]


### K149 update (2026-07-08)

Eval re-surfacing Anthropic **managed multi-agent** docs (coordinator + up to ~25 concurrent subagents, shared sandbox). **Verdict unchanged: pattern Extract / Integrate-with-caution** — useful for CeminiDFS parallel slate stages as *design reference*; do not rewrite prod orchestrators onto Anthropic-managed event streams without lock-in + billing review. Phase-0: proprietary SaaS (no OSS license).
