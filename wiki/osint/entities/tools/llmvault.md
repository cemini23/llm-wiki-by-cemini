---
title: "LLMVault — intentionally vulnerable LLM security lab"
type: entity
tags: [tool, k231, cyber, llm-security, pentest]
keywords: [LLMVault, OWASP LLM Top 10, prompt injection, RAG security, air-gapped]
related:
  - sources/eval-project-evaluation-revenue-2026-08-11.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
phase_0_verdict: "GO Extract 2026-08-11 (MIT, ~29MB)"
---

## Relations

- @sources/eval-project-evaluation-revenue-2026-08-11.md — GO Extract (cyber lab)
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

- **Repo**: `github.com/CyberSunil/LLMVault`
- **License**: MIT [gh api override]
- **Tier**: Extract
- **Primary fit**: local-abliterated-lab — OWASP LLM Top 10 (2025) training range
- **Phase-0**: `.local/adopts/LLMVault` ~25MB

## Narrative

Pre-packaged CTF-style range with intentionally vulnerable LLM endpoints (prompt injection, RAG security, agent security, GenAI pentest). Gives the operator reproducible, air-gapped fixtures for authorized assessment — improving the security posture of in-house tools (e.g. atto-mcp) without touching production.

**Constraints:** strict network isolation; air-gapped; authorized targets only; never expose vulnerable endpoints to untrusted networks; no crimeware.
