---
title: git-rewind — AI-Powered Git State Briefing CLI (Rust)
type: entity
tags: [tool, dev-workflow, git-utility, rust, ollama, adopt-tier, laptop-only]
keywords: [git-rewind, rust-cli, ai-git-briefing, ollama-local, workflow-utility]
related:
  - sources/5-5-moarrr-tool-eval.md
  - entities/tools/codegraph.md
  - entities/tools/leaf.md
  - entities/infrastructure/ollama.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-moarrr-tool-eval.md — origin source: K31 Gemini DR eval URL 3, **Adopt** tier
- @entities/tools/codegraph.md — companion laptop-side workflow utility (token-efficient AST indexer); both serve Claude Code dev sessions
- @entities/tools/leaf.md — companion laptop-side terminal markdown viewer; same workflow tier
- @entities/infrastructure/ollama.md — git-rewind uses local Ollama for natural-language briefing — synergizes without exposing proprietary code

## Raw Concept

AI-powered command-line interface developed in Rust. Evaluates the current state of a Git repository and provides a **natural-language briefing** to the developer. Reads branch histories, recent commits, working-tree state. Operates locally with Ollama. Identified as **Adopt-tier** in the K31 Gemini DR eval (`@sources/5-5-moarrr-tool-eval.md` URL 3).

## Narrative

- **URL**: per K31 eval URL 3 (verify exact GitHub path during install)
- **License**: per eval claim — [NEEDS VERIFICATION 2026-05-05]
- **Stack**: Rust binary
- **Local-LLM integration**: Ollama-compatible (no proprietary-research exposure to external APIs)

### Why Adopt for laptop-side workflow

Per K31 eval recommendation: install locally on the primary macOS laptop. Synergizes with the existing Karpathy LLM Wiki-pattern workflow without exposing proprietary research or codebase to external LLM providers.

Use cases:
- "What did I touch last in this branch?" — natural-language summary of recent activity
- Pre-commit context check before authoring a commit message
- Cross-session resume — synergizes with `hot.md` session-state cache

### Integration with existing laptop tooling

Cemini's laptop already has:
- **codegraph** v0.7.3 (K28 Adopt) — AST indexing for Claude Code
- **leaf** v1.18.2 (K28 Adopt) — terminal markdown viewer
- **Ollama** runtime (local LLM substrate; deployed on librarian, available via SSH tunnel from laptop)

git-rewind plugs into the same workflow tier. All three are local-only, Ollama-compatible, no server-side ops impact.

### Install

```bash
# If distributed via cargo (Rust convention):
cargo install git-rewind  # requires Rust toolchain (not currently on laptop per K28 leaf decision)

# OR if a homebrew formula / npm wrapper exists, prefer that
# (no Rust toolchain needed)

# Verify after install:
git-rewind --version
```

[NEEDS VERIFICATION 2026-05-05] — Cemini's laptop doesn't have `cargo` per the K28 npm-prefix decision (`leaf` was installed via npm wrapper instead). Check if git-rewind has a similar npm/homebrew distribution path before requiring Rust toolchain.

### Open questions [NEEDS VERIFICATION 2026-05-05]

- Exact GitHub URL + license verification
- Distribution method: cargo only, or also npm / homebrew / pre-built binary?
- Star count, commits, latest version
- Bus factor / maintainer activity
- Compatibility with the laptop's Ollama setup (currently Ollama runs on librarian, not laptop directly — does git-rewind support remote Ollama via env var, or does it require local Ollama?)

### Adoption gating

Low-stakes Adopt. Install path Phase 0 (verify license + distribution method) → Phase 1 (install + smoke test on a recent Cemini commit). If git-rewind requires laptop-local Ollama and the laptop doesn't run Ollama (only librarian does), this becomes a deferred-pending-Ollama-laptop-install adoption.

## Snippets

- **Scope framing** (K31 eval): "Artificial Intelligence-powered command-line interface developed in Rust that evaluates the current state of a Git repository and provides a natural-language briefing to the developer. Operating directly within the local repository, it reads branch histories, recent commit[s, working-tree state]." [Source: 5_5 moarrr links.docx URL 3]

- **Recommendation tier (privacy-friendly framing)**: "Adopt. The developer should install the utility locally on the primary macOS laptop to enhance the workflow sequence. Because the architecture supports local Ollama instances, it synergizes perfectly with the existing Karpathy LLM Wiki-pattern workflow without exposing proprietary research or codeba[se]." [Source: 5_5 moarrr links.docx URL 3]
