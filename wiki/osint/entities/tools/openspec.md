---
title: OpenSpec — Spec-Driven Development for AI coding (Adopt-tier)
type: entity
tags: [tool, sdd, spec-driven-development, ai-coding, adopt-tier, workflow, cemini-cross-route, mit]
keywords: [openspec, spec-driven development, SDD, opus 4.5, gpt 5.2, proposal.md, /opsx, slash commands]
related:
  - sources/multi-wiki-link-eval-prompt-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/claude-md-12-rule-template.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/multi-wiki-link-eval-prompt-2026-05-13.md` — origin source (Doc 2, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/claude-md-12-rule-template.md` — complements 12-rule framework (Rule 10 checkpoint discipline aligns with SDD)

## Raw Concept

- **URL**: `https://github.com/Fission-AI/OpenSpec`
- **License**: MIT
- **Stars**: 47.6k
- **Stack**: TypeScript (98.9%), Node.js
- **Tier**: Adopt
- **Primary fit**: Workflow

## Narrative

Imposes Spec-Driven Development (SDD) via structured artifacts (`proposal.md`, `specs/`, `design.md`) before any code generation. Slash commands: `/opsx:propose`, `/opsx:apply`. Tool-agnostic (no Kiro-style ecosystem lock-in). Tuned for Opus 4.5 + GPT 5.2.

### Cemini use case

Standardize SDD across Cemini dev team for Python algorithmic trading module updates. Direct alignment with claude-md-12-rule Rule 10 checkpoint discipline.

### Phase-0 audit (PENDING)

- /opsx command latency in Nix flake environments
- Conflict check against Cemini's existing brief/concept workflow

[NEEDS VERIFICATION 2026-05-13]

[Source: Multi-Wiki Link Evaluation Prompt.docx URL 28 (retrieved 2026-05-13)]
