---
title: Coding-agent substrate steerability
type: concept
tags: [concept, agent-harness, coding-agents, security, verification, k146]
keywords: [substrate constraints, projection layer, docs CLI, backdoor audit, enforceable guardrails, MCP alternative]
related:
  - sources/arxiv-steerability-constraints-2607.02389-2026-07-05.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/probabilistic-agent-policy-verification.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/serena.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @sources/arxiv-steerability-constraints-2607.02389-2026-07-05.md — K146 primary source
- @concepts/generator-verifier-inference-time-steering.md — inference-time verifier steering (prompt-level)
- @concepts/probabilistic-agent-policy-verification.md — trajectory-level verification bounds
- @concepts/poker-arena-multi-axis-cognitive-profile.md — auditability for decide() sessions
- @entities/tools/serena.md — semantic retrieval alternative to raw grep/MCP dumps

## Raw Concept

K146 concept from arXiv 2607.02389: scalable oversight for coding agents via **enforceable substrate** (linters, types, strict pydantic, isolation) plus lightweight **projection tools** (~200 LoC AST docs CLI) instead of unconstrained MCP context dumps.

## Narrative

Three-layer pattern:

1. **Non-advisory substrate** — ruff/pyrefly/beartype/pydantic `extra="forbid"` refuse invalid code; network/VM isolation for secrets.
2. **Projection over raw code** — `docs module` / `docs symbol` return headers+docstrings so reviewers (human or small model) navigate topology without full-repo context.
3. **Small composable CLIs over protocol sprawl** — local dev favors inspectable shell tools; MCP reserved for multi-tenant hosted cases.

Winninger reports independent gains from substrate and tools on backdoor recall (54.5% → 90.9% with Gemma 4 e4b reviewer). For Cemini federation: steal projection + substrate discipline for **Poker Arena verifier harness**, TipDrop rule-checkers, and CCC agent sessions — not wholesale VM sandbox replication on laptop ingest path.

Contrast with `@entities/tools/serena.md` (LSP semantic search): complementary — substrate shrinks what must be read; Serena finds symbols once scope is bounded.

## Snippets

> "We argue that the same battle tested engineering methods scale to coding agents." [Source: arxiv-steerability-constraints-2607.02389 PDF §1 (retrieved 2026-07-05)]
