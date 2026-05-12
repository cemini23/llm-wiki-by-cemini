---
title: "kepano/obsidian-skills — Agent Skills for Obsidian Markdown (CONDITIONAL-GO 2026-05-12)"
type: entity
tags: [tool, agent-skills, obsidian, markdown, claude-code, workflow, k39, conditional-go, deferred]
keywords: [obsidian-skills, agent skills spec, obsidian flavored markdown, wikilinks, dataview, claude code skills]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-12
phase_0_audit: CONDITIONAL-GO 2026-05-12 — install only if user actively works in Obsidian vaults; measure token-overhead before adopting permanently
license_verified: MIT (gh api confirmed)
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

**CONDITIONAL-GO 2026-05-12** — adopt-eligible but skip if no Obsidian use case.

## Phase-0 audit findings (2026-05-12)

**Repo verified**: `github.com/kepano/obsidian-skills` — 30,698★ / 2,088 forks / 35 open issues / MIT confirmed / last push 2026-05-07 (5d fresh). 30.5K-star eval-brief claim **confirmed accurate** (eval brief was right on this one; first non-mischaracterization in K39 Phase-0 batch).

**Markdown-flavor compatibility — MINOR**: Obsidian-flavored markdown is a *superset* of CommonMark, not a subset. GFM-compatible: wikilinks `[[Note]]` render as plain text (no error, just no-link), embeds `![[Note]]` render inert, callouts `> [!type]` degrade to plain blockquotes, frontmatter preserved (both formats support YAML). Effect on Cemini's GFM wiki: zero render-breaks. Cemini's `@path` cross-link convention is custom, not Obsidian-native — wikilinks would degrade if used, but the convention isn't in use anyway.

**Cemini fit**: skills are **agent-side utilities**, not wiki infrastructure. Useful when the agent works on an Obsidian vault (e.g., personal research notes); irrelevant for Cemini's GFM wiki + GitHub workflows. **Token overhead is the real cost**: 5 full skill specs (~2K tokens each) inflates system prompt by ~10K tokens per Claude Code invocation. Net benefit only if Obsidian vault work is frequent.

### Verdict

**CONDITIONAL-GO 2026-05-12** — install ONLY if user actively works in Obsidian vaults outside this wiki. Conditions:
1. Install via Claude Code's `/plugin` mechanism (not raw `~/.claude/skills/` copy) for isolation
2. Measure system-prompt token overhead before/after via `ANTHROPIC_TOKEN_LOG=1`
3. Uninstall if overhead exceeds 5% of context budget AND Obsidian vault use is < 1×/week

If user doesn't use Obsidian beyond what's already in the wiki (Cemini uses GFM, not Obsidian-flavored), **SKIP — pure token overhead, zero benefit**.

[Source: Evaluating Project Links for Stacks.docx URL 2; retrieved 2026-05-11; Phase-0 audit 2026-05-12]
