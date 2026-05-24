---
title: OpenEvolve — evolutionary coding agent (AlphaEvolve-class, Apache-2.0)
type: entity
tags: [entity, tool, ccc, agent-harness, evolutionary-search, adopt, k63]
keywords: [openevolve, alphaevolve, evolutionary-coding, apache-2, token-budget, optillm]
related:
  - sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md
maturity: draft
created: 2026-05-24
updated: 2026-05-24
---

## Relations

- @sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md — K63 URL 2 Adopt

## Raw Concept

K63 eval: Apache-2.0 evolutionary agent for autonomous code optimization (~6.4k★). **Adopt** for CCC-wiki harness / token-budget patterns — not a prod `/opt/cemini` deploy without Phase-0 scoping.

## Narrative

- **Repo**: [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve)
- **License**: Apache-2.0 [CONFIRMED 2026-05-24]
- **Stack**: Python, Docker; supports single-model local weights + OptiLLM router

### Verdict: **Adopt (CCC-primary)**

Extract: evolutionary search for agent harness heuristics, constraint-handling patterns, problem decomposition — applicable to conductor / lazy-tool routing design. **Do not** run unreviewed Docker images on cemini-prod.

### Phase-0 (CCC server)

Clone to `/tmp/openevolve-audit/`; verify OptiLLM + stash tunnel compatibility per eval note.

## Snippets

> "Integrating its stateless code generation logic into the .cursor/rules configuration… enhances local IDE capabilities." [Source: Tool Evaluation for Wiki Ingestion.docx, URL 2]
