---
title: leaf — Rust Terminal Markdown Viewer (wiki-authoring UX)
type: entity
tags: [dev-tooling, markdown, terminal-ui, rust, mit, adopted-tier, laptop-only]
keywords: [leaf, terminal-markdown, rust, latex-rendering, watch-mode, wiki-authoring]
related:
  - sources/links-2-5-4-tool-eval.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/git-rewind.md
maturity: validated
created: 2026-05-04
updated: 2026-05-11
---

## Install state — installed laptop-side 2026-05-04

- Installed via `npm install -g @rivolink/leaf` (the @rivolink scoped npm package + platform-specific binaries via optionalDependencies)
- Binary at `~/.local/bin/leaf` (symlinked from `~/.local/lib/node_modules/@rivolink/leaf/bin/leaf.js`)
- Version: v1.18.2 (released 2026-05-03 per upstream — extremely fresh)
- Smoke test: `--version` returns "leaf 1.18.2"; non-TTY stdin returns "Device not configured (os error 6)" which is expected for a TUI tool

## Usage

Interactive viewer:
```
leaf wiki/concepts/autoresearch-loop-pattern.md
leaf --watch wiki/sources/gemini-sci-research-2602-03837.md  # live-reload while editing
leaf --picker  # file browser
echo '# heading' | leaf  # stdin (TTY-attached only)
```

Themes available: `arctic | forest | ocean | solarized-dark`. Edit config: `leaf --config`.

Use leaf alongside Claude Code editing sessions: edit a wiki page in Claude Code (or any editor) → switch to a terminal running `leaf --watch <page>` to verify LaTeX renders, frontmatter parses, and tables align before invoking `python3 scripts/wiki_lint.py`.

## Relations

- @sources/links-2-5-4-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 4, **Adopt** tier verdict
- @concepts/wiki-tooling-evaluation.md — laptop-side UX tool for wiki authoring; complements `wiki_lint.py` validation

## Raw Concept

Highly optimized terminal-based markdown viewer with watch mode. Renders LaTeX, YAML frontmatter, multi-tier tables, syntax-highlighted code blocks. Identified as **Adopt-tier** in the 2026-05-04 Gemini DR eval — laptop install only.

## Narrative

- **URL**: https://github.com/RivoLink/leaf
- **License**: MIT
- **Stack**: Rust (96.1%), Cargo build
- **Distribution**: npm, ArchLinux User Repository (AUR), source build
- **Maturity**: 601 stars, 194 commits, v1.18.2 released 2026-05-03 (extremely fresh)
- **Cross-platform**: macOS, Linux, Windows

### Why Adopt for laptop only

The deep-read curation workflow involves dense markdown with strict YAML frontmatter, complex quantitative equations (LaTeX), and bidirectional cross-link integrity. leaf provides instant visual feedback alongside Claude Code editing sessions — verifies LaTeX renders correctly, frontmatter is well-formed, before invoking `wiki_lint.py`.

Headless production hosts have no terminal display surface, so leaf belongs only on the developer's macOS laptop.

### Risks (per Gemini DR)

- Terminal-emulator compatibility: complex ANSI escapes / font ligatures may render differently across Terminal.app vs iTerm2 vs Alacritty
- Obsidian-specific syntax (Dataview queries, callouts, block references) may not parse correctly in standard markdown rendering — requires testing with our existing wiki pages

## Snippets

- **Rendering scope**: "successfully rendering LaTeX mathematical formulations, YAML frontmatter data, multi-tiered tables, and syntax-highlighted code blocks directly into the terminal." [Source: links 2 5_4.docx URL 4]

- **Recommendation tier**: "Adopt. Install the binary locally on the macOS development environment to streamline the markdown editing loop and instantly verify quantitative formula rendering prior to initiating the final scp transfer to the production distribution directories." [Source: links 2 5_4.docx URL 4]
