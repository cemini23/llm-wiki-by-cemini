---
title: "universal-modder — agent skill library for game modding (2026-10-04)"
type: source
tags: [source, k281, basgiath, minecraft, agents, skills]
keywords: [k281, universal-modder, agent-skills, field-notes, mit]
related:
  - concepts/k281-harness-wave.md
  - concepts/k281-basgiath-wave.md
maturity: draft
created: 2026-10-04
updated: 2026-10-04
read_status: skimmed
---

## Relations

- @concepts/k281-harness-wave.md
- @concepts/k281-basgiath-wave.md

## Raw Concept

| Repo | `https://github.com/rehan-remade/universal-modder` |
| Checked | 2026-10-04 via `gh api` |
| SPDX | **MIT** |
| Size | 22,365 KB |
| Stars | **2,919** |
| Last push | **2026-10-04** (same day as this check) |
| Archived | no |
| Dual-ID | **OSINT K281** |

## Narrative

The operator named this repo directly to check. It is worth the check.

**What it is.** Skills, tools, and a shared knowledge base that let **any AI coding agent mod almost any PC game**. It lists Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, and OpenCode. The pipeline reads: the agent finds the game, works out the engine and the route, reads the real code, builds the mod, makes art and 3D and sound, tests it in the running game, cuts the video, and **writes down what it learned for the next agent.**

**Why it matters here.** Four things line up with what this workspace already does.

1. **Same skill format.** It ships Agent Skills, and links `.agents/skills`, `.claude/skills`, `.gemini/skills`, and `.github/skills` all to one `skills/` directory. That is the federation pattern this workspace has been hand-rolling — one canonical skill tree, several agent-specific entry points.
2. **A field-notes knowledge base.** It keeps a `knowledge/INDEX.md` and requires the agent to write down what it learned. That is our `wiki/` pattern, applied per-game instead of per-domain. **The instruction to record findings for the next agent is the part worth stealing outright.**
3. **It is agent-agnostic.** `AGENTS.md` is the canonical instruction file, and `CLAUDE.md` / `GEMINI.md` point at it. Our own federation ships Cursor rules and Claude skills separately; a single canonical file with thin pointers is a cleaner shape.
4. **The `um` CLI.** Installed as a plugin, a clone, or via `uv tool install` / `pipx`.

**Relevance to Basgiath.** Basgiath is a Minecraft **Bedrock** add-on. This repo targets "almost any PC game," and its examples are Terraria and Age of Empires II. Bedrock is not the same target as Java Minecraft, and the assets pipeline routes through a third-party generation service. **So it is not a drop-in for Bedrock.** What transfers is the structure: a canonical `AGENTS.md`, one skill tree with symlinked entry points, and the field-notes discipline.

**Cost note before adopting the asset path.** The asset generation runs through a paid external service. Adopting that specific pipeline means a new spend line and a new external dependency. The skill layout costs nothing to copy.

**Verdict.** Adopt the **shape**, not the pipeline. No install this wave.

**Cemini posture:** FILE. No install. **0 product Integrate GO.**
