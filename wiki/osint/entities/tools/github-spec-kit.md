---
title: "GitHub Spec-Kit — Spec-Driven Development CLI"
type: entity
tags: [tool, development, specification, cli, claude-code, workflow, adopted]
keywords: [spec-kit, spec-driven development, SDD, GitHub, Claude Code, executable specifications]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: validated
created: 2026-05-10
updated: 2026-05-10
laptop_install: VERIFIED 2026-05-10 (specify-cli via uv tool at ~/.local/bin/specify)
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 4)

## Raw Concept

Spec Kit is GitHub's CLI toolkit for Spec-Driven Development (SDD) — a methodology that inverts the traditional development hierarchy by treating structured specifications as the source of truth, with code generated from specs.

- **Repo**: `github.com/github/spec-kit`
- **License**: MIT [VERIFIED 2026-05-10 via Phase-0 audit]
- **Stack**: CLI tool (PyPI package: `specify-cli`), installable via `pip install specify-cli` or `uv tool install specify-cli`
- **Maturity**: 95,247 ★, last commit 2026-05-08, latest release v0.8.7 (2026-05-07)
- **Claude Code integration**: ships upstream in `src/specify_cli/integrations/claude/`; `specify init --integration claude` scaffolds `~/.claude/skills/speckit-*.md` slash commands. No wrapper code required.

## Narrative

Spec Kit enforces a spec-first workflow: write structured specification → validate → generate scaffold code → implement. This bridges the critical gap between the 380-page curated wiki (knowledge) and deterministic Python code for the Cemini ecosystem (execution).

### Integration vectors

- **Workflow (Adopt)**: Install globally via `uv tool install` on the macOS environment. Use during the wiki→production transition phase — when research curated in the wiki must become production code, Spec Kit ensures the spec exists before implementation begins.
- **Cemini prod (No)**: Development tooling stays air-gapped from the live trading host.
- **Wiki server (No)**: Doesn't execute application code.

### Risks

- **Ecosystem alignment**: resolved by Phase-0 audit — Claude Code integration ships upstream (`src/specify_cli/integrations/claude/`). Slash commands materialize as Markdown skill files; no wrapper required.
- **Bus factor**: low — GitHub-org owned, 95,247 stars, release v0.8.7 on 2026-05-07. Pin to release tag at install.

### Cemini significance

The 380-page wiki represents structured knowledge without executable form. Spec-Kit provides the methodology bridge: wiki page → formal specification → test-driven Python implementation. This directly supports the IP-sale readiness goal by ensuring code is traceable to documented specifications.

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 4]
