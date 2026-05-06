---
title: guidance-ai — Structured-Generation Library for LLMs (Microsoft)
type: entity
tags: [tool, structured-generation, deterministic-output, llm-tooling, adopt-tier, cemini-production-stack, microsoft]
keywords: [guidance-ai, structured-output, constrained-generation, json-enforcement, token-binding, deepseek-output-discipline]
related:
  - sources/5-5-moarrr-tool-eval.md
  - entities/infrastructure/deepseek-api.md
  - concepts/conductor-orchestrator.md
  - entities/frameworks/fastmcp.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-moarrr-tool-eval.md — origin source: K31 Gemini DR eval URL 17, **Adopt** tier
- @entities/infrastructure/deepseek-api.md — guidance-ai wraps DeepSeek calls to enforce deterministic structured output
- @concepts/conductor-orchestrator.md — Conductor's tool-orchestration stage requires structured outputs from each model in the pool; guidance-ai is the enforcement primitive
- @entities/frameworks/fastmcp.md — FastMCP `@mcp.tool` decorators have typed input/output contracts; guidance-ai forces LLM compliance with those contracts at the token-generation layer

## Raw Concept

Microsoft's library for **algorithmic control over LLM token-generation logic**. Instead of relying on stochastic natural-language prompts to enforce output formats (which fails unpredictably), guidance-ai *binds* the generation process to a structured grammar — token-by-token. Identified as **Adopt-tier** in the K31 Gemini DR eval (`@sources/5-5-moarrr-tool-eval.md` URL 17).

## Narrative

- **URL**: github.com/guidance-ai/guidance (per K31 eval URL 17 reference)
- **License**: per eval claim — [NEEDS VERIFICATION 2026-05-05]; verify against LICENSE file (Microsoft repos are typically MIT)
- **Maintainer**: guidance-ai org (Microsoft-affiliated, originated from MS Research)
- **Distribution**: pip install guidance

### Why Adopt for Cemini

Cemini's LangGraph orchestrator + FastMCP tool-use pipeline both require deterministic JSON outputs from DeepSeek. Currently, the discipline is enforced via prompt engineering — which works most of the time but produces parsing errors at scale. Per the K31 eval:

> "Guidance algorithmically binds the generation p[rocess]. Apply the @guidance decorator around the core DeepSeek execution wrappers to enforce deterministic JSON outputs, structurally eliminating parsing errors within the LangGraph orchestrat[or]." [Source: 5_5 moarrr links.docx URL 17]

This addresses a real pain point that compounds across:
- The K28 quant-libs FastMCP integration (`@briefs/2026-05-04_quant-libs-fastmcp-integration.md`) — 11 `@mcp.tool` decorators with typed responses
- The K30 Polymarket Stack brief (`@briefs/2026-05-05_polymarket-stack-adoption.md`) — order-placement tool calls that fail catastrophically on malformed JSON
- The K30 Conductor audit-trail Phase 1+5 (`@briefs/2026-05-05_conductor-audit-trail-phase1.md`) — fitness-function inputs require structured AuditEntry records
- Conductor's existing taxonomy classifier (`@concepts/conductor-orchestrator.md`) — needs reliable enum-style outputs for routing decisions

### Integration approach

Per the K31 eval recommendation: wrap DeepSeek execution calls with the `@guidance` decorator, define output schemas explicitly. Native `litellm` integration likely (similar to existing Cemini stack via the OpenAI-compatible base_url pattern).

```python
# services/llm_analyst/deepseek_guided.py (proposed)
import guidance

@guidance
def routing_decision(taxonomy_class: str, query: str):
    # Force the LLM to output JSON conforming to RoutingDecision schema
    # rather than free-form text that requires post-hoc parsing
    ...
```

### Open questions [NEEDS VERIFICATION 2026-05-05]

- Compatibility with DeepSeek's API (guidance-ai works natively with OpenAI / Anthropic / local models; verify DeepSeek base_url pattern integrates cleanly)
- License verification (Microsoft repos vary: MIT vs proprietary; check)
- Performance overhead at the token-generation layer (low for grammar-constrained, but verify under load)
- Compatibility with `litellm` (Cemini's existing LLM-routing wrapper)
- Star count / commits / latest version / release cadence

### Adoption gating

- Phase 0 source audit (clone, verify license + maturity)
- Phase 1: drop into a sandbox; wrap one DeepSeek call (e.g., the Conductor taxonomy classifier) with `@guidance`; A/B against the current prompt-engineered version on parsing-error-rate
- Phase 2: rollout across `services/llm_analyst/deepseek_client.py` if Phase 1 shows meaningful error-rate reduction
- Phase 3: extend to FastMCP tool decorators (each `@mcp.tool` gets a structured input/output schema enforced via guidance)

Stage as a brief candidate. Could be a quick-win brief separate from K28 quant-libs, or folded into the Conductor audit-trail Phase 1+5 brief if scope expands.

## Snippets

- **Philosophy** (K31 eval): "Advanced structural control paradigm designed specifically to intercept and manipulate the token-generation logic of Large Language Models. Instead of relying on stochastic natural-language prompts to hopelessly enforce output formats, Guidance algorithmically binds the generation p[rocess]." [Source: 5_5 moarrr links.docx URL 17]

- **Recommendation tier**: "Adopt. Integrate the library into the Cemini platform immediately via pip. The engineering team should aggressively apply the @guidance decorator around the core DeepSeek execution wrappers to enforce deterministic JSON outputs, structurally eliminating parsing errors within the LangGraph orchestrat[or]." [Source: 5_5 moarrr links.docx URL 17]
