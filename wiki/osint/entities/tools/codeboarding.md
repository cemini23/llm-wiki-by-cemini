---
title: "CodeBoarding — Interactive Architecture Mapping Tool"
type: entity
tags: [tool, documentation, architecture, visualization, code-analysis, ip-readiness, adopted]
keywords: [CodeBoarding, architecture mapping, LSP, static analysis, code visualization, due diligence]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: validated
created: 2026-05-10
updated: 2026-05-10
laptop_install: VERIFIED 2026-05-10 (uv tool at ~/.local/bin/codeboarding; 7 LSPs bootstrapped via codeboarding-setup; csharp skipped — dotnet absent)
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 25)

## Raw Concept

CodeBoarding combines deterministic static analysis via Language Server Protocols (LSP) with contextual LLM reasoning to auto-generate interactive architecture diagrams and documentation from multi-language repositories.

- **Repo**: `github.com/CodeBoarding/CodeBoarding`
- **License**: MIT [VERIFIED 2026-05-10 via Phase-0 audit]
- **Stack**: Python 3.12+, Node.js v20.18.1 (auto-bootstrapped via `nodeenv`), installable via `pipx install codeboarding`
- **Maturity**: 1,458 ★, last commit 2026-05-07, latest release v0.11.0 (Beta)
- **LSP coverage**: Python, TypeScript, JavaScript, PHP (npm), Java (JDTLS), Go (gopls), Rust (rust-analyzer)
- **macOS compat**: CI matrix passing for Apple Silicon + Intel; Node 20.18.1 auto-installed to `~/.codeboarding/servers/nodeenv/` if absent
- **Output license**: generated diagrams + Markdown inherit user repo license; no output-licensing lock-in

## Narrative

CodeBoarding ingests massive multi-language software repositories and produces interactive architecture maps, sequence diagrams, and dependency graphs. It uses LSP for deterministic structural analysis and LLM reasoning for semantic interpretation of code intent.

### Integration vectors

- **Workflow (Adopt)**: Install via `pipx` on macOS. Set up cron job or pre-commit hook to auto-generate architecture documentation for the Cemini git repository. Generated diagrams ship to the wiki server as documentation artifacts.
- **Cemini prod (No)**: Static codebase analysis doesn't belong in the live trading execution container.
- **Wiki server (Subject)**: The server is an excellent destination for generated diagrams, but heavy compilation occurs off-server on the laptop.

### Risks

- **Node.js dependency**: resolved by Phase-0 audit — Node 20.18.1 pinned and auto-bootstrapped via `nodeenv` into `~/.codeboarding/servers/nodeenv/`, isolated from system NVM. macOS CI matrix verified.
- **Beta-release maturity**: v0.11.0 ships as Beta; API + output format may shift. Pin to specific commit at install; re-verify schema at quarterly cadence.
- **LLM hallucination in semantic layer**: residual risk — human-triage generated artifacts before wiki upload; keep deterministic structural outputs only.

### Cemini significance

Directly supports IP-sale readiness by auto-documenting Cemini execution paths. Auto-generated architecture documentation is a critical deliverable for technical due diligence. Reduces manual documentation burden for the 40-container Docker Compose topology.

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 25]
