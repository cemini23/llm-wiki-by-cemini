---
title: "Digital Marketing Pro — Claude Plugin Ecosystem (Steal: Hallucination Detection + Evals)"
type: entity
tags: [tool, steal-from, hallucination-detection, evals, mcp-templates, claude-plugin, mit-license]
keywords: [digital-marketing-pro, hallucination detection, claim verification, A-F grading, evals.json, 67 MCP servers, 115 commands, disable-model-invocation]
related:
  - sources/evaluating-code-for-trading-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/mcp-tool-marketplace.md
  - concepts/cemini-license-posture.md
  - concepts/reasoning-safety-monitor.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-code-for-trading-stacks.md` — source evaluation brief (URL 10)
- `@concepts/reasoning-safety-monitor.md` — A-F grading + claim verification belongs to this family
- `@concepts/mcp-tool-marketplace.md` — 67 MCP server implementations as reference templates

## Raw Concept

Massive Claude-plugin ecosystem (115 commands, 67 MCP servers, 5-layer memory architecture) ostensibly for digital marketing. The v3.0 QA/evaluation layer is the actual asset: hallucination detection, claim verification, output validation, A+→F grading; `disable-model-invocation: true` enforces human-in-the-loop write gates.

- **Repo**: `github.com/indranilbanerjee/digital-marketing-pro`
- **License**: MIT [NEEDS VERIFICATION 2026-05-10]
- **Architecture**: 5-layer memory (session, RAG/vector, temporal KG, universal, file-based)
- **External deps**: Salesforce, HubSpot, Pinecone, Qdrant, Graphiti

## Narrative

**Recommendation: Steal-from, never deploy the framework.** The marketing business logic is irrelevant; the underlying QA primitives are extremely relevant.

### Patterns worth stealing

1. **Hallucination detection / claim verification scripts** — port directly into `agents/orchestrator.py` to validate DeepSeek outputs before high-risk Alpha-generating trades execute via Alpaca.
2. **`evals/evals.json` schema** — reproducible test cases with quantitative + qualitative assertions. Harden `wiki_lint.py` regression suite (dangling links, parsing errors, structural integrity).
3. **A+→F grading scripts** — deterministic output grading; integrate into pre-trade gate.
4. **67 MCP server implementations** — reference templates; mine for patterns Cemini's own MCP tools can adopt.
5. **`disable-model-invocation: true` write-gate pattern** — human-in-the-loop write enforcement primitive.

### Why not adopt

- Stack relies on Salesforce/HubSpot/Pinecone/Qdrant + Graphiti → violates Cemini's offline-first, locally-embedded constraints for librarian server
- 5-layer memory stack would require spinning up Pinecone + Graphiti → network egress + latency unacceptable in trading loops
- Domain mismatch (marketing/SEO) requires meticulous decoupling — high-effort port

### Risks (if mining code)

- **14 HTTP-only MCP connectors [NEEDS VERIFICATION 2026-05-10]**: cryptographic-auth + session-state differences vs Cemini's stdio MCP standard
- **License verification**: confirm MIT before extracting
- **Decoupling cost**: ensure no SaaS API calls (Salesforce, HubSpot) remain in extracted scripts

[Source: Evaluating Code for Trading Stacks.docx, URL 10]
