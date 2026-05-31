---
title: "NVIDIA SkillSpector — agent skill security scanner"
type: entity
tags: [tool, adopt-candidate, cybersec, mcp, skill-audit, k88, phase-0-pending]
keywords: [skillspector, nvidia, langgraph, supply-chain, prompt-injection, skill-audit]
related:
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
phase_0_verdict: PENDING — K88 Adopt; Apache-2.0 confirmed
---

## Relations

- @sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md — K88 v5 Adopt (primary fit cybersec-wiki)
- @concepts/tool-evaluation-framework.md — Phase-0 queue

## Raw Concept

- **Repo**: `github.com/nvidia/skillspector`
- **License**: Apache-2.0 `[CONFIRMED 2026-05-31]` via GitHub API
- **Prompted by**: K88 multi-wiki eval — supply-chain scanning for Claude skill repos before kb-server ingest

## Narrative

LangGraph-based scanner for MCP/agent skill repos — prompt injection, tool poisoning, excessive agency. **Integration vector:** embed `skillspector.graph` in OSINT `scripts/skill_audit.py` / `preingest_check.py` pipeline. Apache-2.0 clean for IP-sale boundary.

**Phase-0 open:** offline OSV.dev behavior on librarian air-gap subnet `[NEEDS VERIFICATION 2026-05-31]`.
