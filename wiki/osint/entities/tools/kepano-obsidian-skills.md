---
title: "kepano/obsidian-skills — Agent Skills for Obsidian Markdown"
type: entity
tags: [tool, agent-skills, obsidian, markdown, claude-code, workflow, k39, adopt-tier, phase-0-pending]
keywords: [obsidian-skills, agent skills spec, obsidian flavored markdown, wikilinks, dataview, claude code skills]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 2)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL** (per source brief): `github.com/kepano/obsidian-skills`
- **Tier (per source brief)**: **Adopt** (Workflow only)
- **License** (per source brief): MIT
- **Stack**: JSON Agent Skills spec, JavaScript/TypeScript; compatible with Claude Code, Codex CLI, OpenCode
- **Maturity** (per source brief): 30.5K★ / 2.1K forks / 181 watchers (claim) — **NEEDS Phase-0 verification**

## Narrative

Agent Skills schemas teaching LLM agents to manipulate Obsidian Flavored Markdown (wikilinks, embeds, block refs, callouts, Bases, JSON Canvas). Eval brief recommends Adopt for the laptop Claude Code workflow to prevent CommonMark-only formatting degradation on wiki-curation tasks.

### Integration vector

**Adopt (pending Phase-0)** — Workflow only. Install via `/plugin marketplace add` or copy into `~/.claude/skills/`. Improves agent reliability on Obsidian-flavored content.

### Caveats

- **Cemini wiki uses CommonMark, not Obsidian-flavored markdown.** The bidirectional `@path` and `[[link]]` conventions in this wiki are CommonMark-compatible. Obsidian-specific skill schemas may or may not provide a net win on the wiki-curation workflow.
- **Token bloat risk**: exposing full Obsidian skill schemas to Claude Code inflates context window. Eval brief flagged this.
- **Vendor lock-in**: if Cemini migrates away from any Obsidian-syntax usage, skills become dead weight.

### NEEDS VERIFICATION

- 30.5K-star claim — verify on GitHub API (kepano is a real high-profile maintainer; star count plausible but not yet confirmed)
- Whether the Obsidian-specific schemas help or hurt a CommonMark-only wiki workflow
- Token overhead per request when schemas are injected into the system prompt

### Phase-0 audit status

Not yet performed. Defer install until Phase-0 confirms: (a) license file present, (b) star/fork numbers, (c) actual benefit on Cemini's CommonMark-leaning workflow.

[Source: Evaluating Project Links for Stacks.docx URL 2; retrieved 2026-05-11]
