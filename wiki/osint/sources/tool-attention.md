---
title: "Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax"
type: source
tags: [MCP, tool-use, agent-infrastructure, context-engineering, middleware, token-efficiency]
keywords: [Tool Attention, MCP Tax, Tools Tax, lazy schema loading, intent routing, ISO score, token reduction, LangGraph middleware]
clusters: [llm-agents]
related:
  - concepts/mcp-tool-marketplace.md
  - concepts/mcp-context-optimization.md
maturity: validated
read_status: deep-read
created: 2026-04-30
updated: 2026-05-11
---

## Relations
- Concept gap: no dedicated MCP-infrastructure concept page exists (stub needed — `@concepts/mcp-tool-marketplace.md` covers the marketplace, not the middleware layer)

## Raw Concept
- Original title: Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows
- Author(s): Anuj Sadani, Deepak Kumar (Infrrd.ai)
- Type: arXiv preprint (arXiv:2604.21816)
- Retrieved: 2026-04-30 (Tier-2 sweep, via Exa crawling)
- Read status: deep-read (abstract + body via Exa)
- Code: https://github.com/asadani/tool-attention

## Narrative

Tool Attention addresses the **MCP Tax** (or "Tools Tax"): stateless MCP servers re-serialize full tool schemas on every conversational turn, consuming 15K-55K tokens per turn in typical 4-6-server deployments. This causes three cascading failures: economic (CLI $3.20 vs MCP $55.20 for 10K operations), cognitive (reasoning degrades past ~70% context utilization), and adversarial (tool descriptions shape attention masks — injectable via Tool Poisoning Attacks). [Source: arXiv:2604.21816 §1]

**Three-component architecture**:

1. **Intent-Schema Overlap (ISO) score** — commodity sentence embeddings compute query-to-tool relevance, replacing uniform injection with query-conditioned selection.

2. **State-aware gating function** — enforces preconditions and access scopes. Tools are gated based on current agent state, not just query similarity.

3. **Two-phase lazy schema loader** — compact summary pool stays in context; full JSON schemas promoted only for top-k gated tools.

**Results** (simulated 120-tool, 6-server benchmark calibrated to public MCP deployment audits):
- Per-turn tool tokens: 47.3K → 2.4K (**95.0% reduction**)
- Effective context utilization: 24% → 91%
- Author note: end-to-end figures reported as projections from measured token counts combined with published deployment telemetry; marked explicitly as projected. [Source: arXiv:2604.21816 Abstract]

**Relevance to Cemini**: Directly deployable as LangGraph middleware. Cemini's FastMCP tool surface (22+ tools, growing across Wave 5 adoptions) pays the MCP Tax on every orchestrator turn. The 95% token reduction would compound across the multi-agent pipeline. MIT-licensed code at github.com/asadani/tool-attention. The two-phase lazy loader pattern generalizes beyond MCP — applicable to any agent framework with growing tool catalogs.

## Snippets

"Protocol-level efficiency, not raw context length, is a binding constraint on scalable agentic systems." [Source: arXiv:2604.21816 Abstract]

"Tool Attention directly reduces measured per-turn tool tokens by 95.0% (47.3k → 2.4k) and raises effective context utilization from 24% to 91%." [Source: arXiv:2604.21816 Abstract]

"Empirical audits consistently place this overhead between 15,000 and 55,000 tokens per turn in typical four-to-six-server deployments, reaching >150k with aggressive tool sprawl." [Source: arXiv:2604.21816 §1]

"One published benchmark reports CLI-equivalent workflows at $3.20 versus MCP at $55.20 for the same 10,000 operations." [Source: arXiv:2604.21816 §1]
