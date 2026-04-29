---
title: kepano/obsidian-skills — Agent Skills for Obsidian Markdown (MIT)
type: source
tags: [llm-tooling, obsidian, agent-skills, claude-code, codex, markdown, json-canvas, obsidian-bases, workflow-adopt, ip-sale-clean]
keywords: [obsidian-skills, kepano, obsidian-flavored-markdown, json-canvas, base-files, agent-skills, npx-skills, claude-code, codex-cli, defuddle, opencode, openclaw]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - sources/atomicmemory-llm-wiki-compiler.md
  - sources/obsidian-second-brain-eugeniughelbur.md
maturity: validated
created: 2026-04-28
updated: 2026-04-28
clusters: [llm-agents, librarian-tooling]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — parent canonical Gemini DR source; one of 7 Adopt-for-Workflow recommendations (with `obsidian-bases` sub-skill folded in)
- @concepts/wiki-tooling-evaluation.md — Wave 2 evaluation parent
- @concepts/ip-sale-readiness.md — MIT license clears IP-sale checks (Exa-verified 2026-04-28: 26969 ★)
- @sources/atomicmemory-llm-wiki-compiler.md — WTE Wave 1 adoption candidate; the obsidian-skills schema specifications can be referenced by the llm-wiki-compiler's parsers when building error-handling for non-standard Markdown
- @sources/obsidian-second-brain-eugeniughelbur.md — sibling Workflow-Adopt from the same Gemini DR wave; both target the laptop Obsidian + Claude Code curation loop

## Raw Concept

- **URL**: https://github.com/kepano/obsidian-skills
- **Type**: Open-source repository / Agent skill definitions
- **License**: MIT (Exa-verified 2026-04-28)
- **Stars / Forks (Exa-verified 2026-04-28)**: 26969 ★ / 1778 forks / 33 open issues
- **Stack**: Obsidian Flavored Markdown + JSON Canvas + native CLI integrations (.md and YAML; no compiled code)
- **Org**: kepano (Steph Ango, Obsidian's CEO and a known voice in PKM tools — high authoritative signal)
- **Created**: 2026-01-02; **Last push**: 2026-04-02
- **Topics**: claude, clawdbot, cli, codex, defuddle, obsidian, openclaw, opencode, skills
- **Sub-component evaluated**: `obsidian-bases` directory (URL 23 in the Gemini wave) — folded into this page

## Narrative

### What it does
A centralised collection of standardised "Agent Skills" instruction files designed to teach LLMs how to precisely generate and manipulate Obsidian's proprietary syntax extensions. Provides zero-shot formatting templates for:
- Obsidian Flavored Markdown (wikilinks, callouts, frontmatter properties)
- Obsidian Bases (`.base` files: structured database-like views over frontmatter properties)
- JSON Canvas (`.canvas` files: visual node maps)

The skills are static `.md` files digested locally by tools like Claude Code and Codex CLI to expand contextual understanding of the user's vault.

### Why Adopt-for-Workflow

This is a tight match for the workspace's primary curation methodology (Obsidian + Claude Code). Reasoning:

1. **Identical technology stack** — kepano is the Obsidian CEO; the skills are first-party-grade documentation of Obsidian's own syntax. No third-party interpretation drift.
2. **MIT license** — clears IP-sale-readiness.
3. **Eliminates Markdown syntax hallucinations** — when Claude Code generates wiki pages, it currently invents YAML frontmatter syntax variations. The `obsidian-bases` sub-skill provides flawless YAML templates that align exactly with what Obsidian's parser expects.
4. **Zero local footprint** — pure Markdown documentation; no runtime, no daemon, no embeddings.
5. **NPX install path is one command** — `npx skills add git@github.com:kepano/obsidian-skills.git` into the laptop's `.claude` directory.

### Where it falls short

1. **Cemini production stack fit: ❌** — Cemini operates on Python dictionaries and Polars dataframes. Obsidian formatting offers zero utility there.
2. **Wiki / librarian server fit: ⚠️** — the llm-wiki-compiler must parse standard Markdown. Reading these schema specifications can inform the compiler's error-handling parsers, but no executable code is deployed on the server.

### Integration vector

```
Local laptop:
  npx skills add git@github.com:kepano/obsidian-skills.git
        ⬇
  installs to ~/.claude/skills/kepano-obsidian-skills/
        ⬇
  Claude Code reads on session start
        ⬇
  Agent now has zero-shot templates for:
    - Obsidian Flavored Markdown
    - Obsidian Bases (.base files)  
    - JSON Canvas (.canvas files)
    - Obsidian wikilinks
    - YAML frontmatter properties
```

The `obsidian-bases` sub-skill (originally URL 23 in the Gemini wave, evaluated separately) is the sub-directory `skills/obsidian-bases` within this repo. Adopt the parent package; the sub-skill comes along automatically.

### Risks & open questions

1. **Obsidian internal spec drift** — Obsidian is under active development; specifications for JSON Canvas and `.base` file architectures change periodically. The static skills risk YAML-parsing-error deprecation if not synchronised from upstream. Schedule quarterly resync (e.g., `git pull` against the skills repo each quarter).
2. **`obsidian-bases` schema validation boundaries** [NEEDS VERIFICATION 2026-04-29] — Gemini flagged: "The exact boundaries of the schema validation rules provided by the obsidian-bases skill regarding complex, nested mathematical formulas require strict verification." Less critical for the wiki use-case (no nested math formulas in librarian content), but worth flagging if Cemini ever uses Bases for portfolio metrics.
3. **kepano's ongoing maintenance** — high signal (Obsidian CEO maintains personally) but bus factor concern if his focus shifts. 20 contributors counted on the repo, second-tier contributors should be tracked for community vitality.

## Snippets

> "Agent skills for Obsidian. Teach your agent to use Markdown, Bases, JSON Canvas, and use the CLI." [Source: GitHub repo description, retrieved via Exa crawling_exa 2026-04-28]

> "Adopt for Workflow. Install these skill definitions directly into the laptop's Claude Code environment to immediately eliminate markdown syntax hallucinations and enable the agent to reliably generate dataviews and bases during rapid curation sessions." [Source: Gemini DR report, URL 7]
