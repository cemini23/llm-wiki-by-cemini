---
title: ttok — Token-Counting CLI Utility (Simon Willison)
type: entity
tags: [tool, token-counting, cli-utility, cost-discipline, adopt-tier, universal-install, simon-willison]
keywords: [ttok, simonw, token-count, llm-cost-discipline, pre-call-audit, brief-token-estimation]
related:
  - sources/5-5-moarrr-tool-eval.md
  - entities/tools/codegraph.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-moarrr-tool-eval.md — origin source: K31 Gemini DR eval URL 19, **Adopt** tier
- @entities/tools/codegraph.md — companion laptop-side workflow tool (token efficiency via AST indexing); ttok complements by measuring the savings

## Raw Concept

Ultra-lightweight Python CLI utility by Simon Willison. Single-purpose: **audit, count, and truncate text payloads against specific LLM token limits**. Identified as **Adopt-tier** in the K31 Gemini DR eval (`@sources/5-5-moarrr-tool-eval.md` URL 19).

## Narrative

- **URL**: github.com/simonw/ttok (Simon Willison's standard repo namespace)
- **License**: per eval — [NEEDS VERIFICATION 2026-05-05]; Simon Willison's published tools are consistently Apache-2.0
- **Stack**: Python, single-file dependency
- **Distribution**: `pip install ttok`
- **Maintainer**: Simon Willison (high reliability + active maintenance, per his track record across `llm`, `datasette`, `sqlite-utils`, etc.)

### Why Adopt (universally)

Per K31 eval recommendation: install **universally across the Cemini backend Python environment AND the local macOS developer workstation**. Single-purpose, virtually nonexistent architectural risk.

Use cases for Cemini:

| Use case | Why ttok helps |
|---|---|
| Pre-call token budget audit in DeepSeek wrappers | Verify a prompt fits in the context window before issuing the call (avoids truncation surprises) |
| Brief-staging token estimation | When a brief at `briefs/<file>.md` will be fed to a downstream agent, estimate tokens before scp; pair with `scripts/skill_audit.py` |
| Conductor cost discipline | The audit-trail Phase 1+5 brief (`@briefs/2026-05-05_conductor-audit-trail-phase1.md`) computes per-query cost; ttok provides the input-token half of that |
| Wiki-page token-budget audits | Long source pages (e.g., the 37 KB Kalshi llms.txt page at `@concepts/kalshi-api-reference.md`) — verify they're chunkable for kb-server retrieval |
| K-series ingest discipline | When evaluating whether a paper deep-read fits in DeepSeek's context, count tokens first |

### Integration

```bash
# Laptop install (workspace-side)
pip install ttok

# Pre-call audit example
cat briefs/2026-05-05_polymarket-stack-adoption.md | ttok        # token count
cat briefs/2026-05-05_polymarket-stack-adoption.md | ttok -t 100000  # truncate to 100k

# Cemini-prod side
# Add to /opt/cemini/Pipfile or pyproject.toml
# Use in pre-call hooks in services/llm_analyst/deepseek_client.py
```

### Open questions [NEEDS VERIFICATION 2026-05-05]

- License confirmation (Apache-2.0 expected per Simon Willison's pattern; verify)
- Tokenizer compatibility — ttok defaults to OpenAI's tiktoken; confirm compatibility with DeepSeek's tokenizer (typically tiktoken-compatible)
- Latest version + dependency tree (likely zero deps beyond tiktoken)

### Adoption gating

Minimal. Single-purpose tool, low risk, high frequency-of-use. Stage as a tiny brief addendum to the K30 Conductor audit-trail brief (`@briefs/2026-05-05_conductor-audit-trail-phase1.md`) — token-counting is part of fitness-function input.

## Snippets

- **Scope framing** (K31 eval): "Ultra-lightweight, dedicated Python utility engineered exclusively to audit, count, and truncate text payloads against specific LLM token limits." [Source: 5_5 moarrr links.docx URL 19]

- **Recommendation tier**: "Adopt. The software must be installed universally across the Cemini backend Python environment and the local macOS developer workstation. Its single-purpose, highly refined design creates massive operational utility with virtually nonexistent architectural risk." [Source: 5_5 moarrr links.docx URL 19]
