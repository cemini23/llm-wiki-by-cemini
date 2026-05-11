---
title: "Perplexity MCP Server (official)"
type: entity
tags: [tool, mcp-server, live-web-search, perplexity, cemini-prod-candidate, k38, phase-0-go]
keywords: [perplexity, mcp, adopt, three-surface-eval, live-search, sonar]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/mcp-tool-marketplace.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
phase_0_audit: GO 2026-05-11 (workflow first, prod after 30-day soak)
adoption_status: DEFERRED 2026-05-11 (no spend now; pay-per-query Perplexity API ~$5-20/M tokens Sonar Pro, $5-200+/run Deep Research)
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 7)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context
- `@concepts/mcp-tool-marketplace.md` — official-vendor MCP profile (lowest bus-factor tier)

## Raw Concept

- **Repo / URL** [VERIFIED 2026-05-11]: `github.com/perplexityai/modelcontextprotocol`
- **Tier (per source brief)**: **Adopt**
- **License** [VERIFIED 2026-05-11]: **MIT**
- **Phase-0 audit** [VERIFIED 2026-05-11]: 2,181★ / 324 forks / 14 contributors / 4 open issues. Created 2025-03-10; last push 2026-04-14 (~3wk fresh). v0.9.0 (npm-only; no GitHub releases tagged). Real `@modelcontextprotocol/sdk@^1.21.1`, vitest test suite present, Docker image + HTTP-mode for cloud. 4 named tools: `perplexity_search`, `perplexity_ask`, `perplexity_research`, `perplexity_reason`.

## Narrative

Official MCP server for Perplexity's API Platform. TypeScript service. Exposes Sonar Pro + Deep Research + Reasoning Pro models to MCP-compatible agents via stdio + HTTP transports. **Phase-0 verdict: GO** — closes the live-web-search gap.

### Integration vector

**GO 2026-05-11 — DEFERRED on spend**. Recommended sequencing: adopt to Workflow first (30-day analyst-research soak with cost-cap), evaluate prod adoption after data. Docker-isolate per eval brief. Cost-cap with `PERPLEXITY_TIMEOUT_MS` + per-tool budget limits in the agent loop. Closes a real gap — `mcp__exa__*` is currently the only live-search surface; 2nd vendor reduces single-vendor exposure.

### Risks

1. **Vendor cost lock-in** — `PERPLEXITY_API_KEY` required; all 4 tools meter against Perplexity's paid plans (Sonar Pro / Deep Research / Reasoning Pro). Trading-volatility queries during market events = unbounded burn without strict caps.
2. **Prompt-leakage to vendor** — every query POSTs to `api.perplexity.ai` with `X-Source: pplx-mcp-server` header. Per Perplexity ToS, prompts may be logged/trained on. Treat queries as non-confidential; no proprietary alpha goes in.

### Cost / footprint

| Item | Value |
|---|---|
| Subscription | None — pay-per-query |
| API cost (Sonar Pro) | ~$5-20/M tokens |
| API cost (Deep Research) | ~$5-200+/run |
| RAM idle | ~50-80 MB (Node) |
| RAM loaded | ~80-120 MB |
| CPX21 fit | OK (stateless TS, no in-process model) |

### Activation trigger

Reactivate this brief when: (a) workflow-laptop Workflow live-research need surfaces a hard gap unaddressable by `mcp__exa__web_search_exa`, OR (b) user explicitly clears a $50-200/mo Perplexity API budget for trading-research load.

[Source: Link Evaluation Brief Trading Stack.docx, URL 7; Phase-0 audit 2026-05-11]
