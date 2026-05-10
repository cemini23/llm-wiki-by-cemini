---
title: "GitHub Spec-Kit — Spec-Driven Development CLI"
type: entity
tags: [tool, development, specification, cli, claude-code, workflow]
keywords: [spec-kit, spec-driven development, SDD, GitHub, Claude Code, executable specifications]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 4)

## Raw Concept

Spec Kit is GitHub's CLI toolkit for Spec-Driven Development (SDD) — a methodology that inverts the traditional development hierarchy by treating structured specifications as the source of truth, with code generated from specs.

- **Repo**: `github.com/github/spec-kit`
- **License**: To verify (GitHub project — likely MIT or Apache-2.0)
- **Stack**: CLI tool, installable via `uv tool install`

## Narrative

Spec Kit enforces a spec-first workflow: write structured specification → validate → generate scaffold code → implement. This bridges the critical gap between the 380-page curated wiki (knowledge) and deterministic Python code for the Cemini ecosystem (execution).

### Integration vectors

- **Workflow (Adopt)**: Install globally via `uv tool install` on the macOS environment. Use during the wiki→production transition phase — when research curated in the wiki must become production code, Spec Kit ensures the spec exists before implementation begins.
- **Cemini prod (No)**: Development tooling stays air-gapped from the live trading host.
- **Wiki server (No)**: Doesn't execute application code.

### Risks

- **Ecosystem alignment**: Documentation heavily indexes on GitHub Copilot integrations (`/speckit.specify` slash commands). Translating this workflow to Claude Code may require custom system-prompt wrappers to ensure behavioral parity.
- **Bus factor**: GitHub-maintained project but the SDD methodology is opinionated and may not have broad community adoption.

### Cemini significance

The 380-page wiki represents structured knowledge without executable form. Spec-Kit provides the methodology bridge: wiki page → formal specification → test-driven Python implementation. This directly supports the IP-sale readiness goal by ensuring code is traceable to documented specifications.

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 4]
