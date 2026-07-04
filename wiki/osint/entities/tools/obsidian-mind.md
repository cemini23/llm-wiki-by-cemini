---
title: obsidian-mind — agent memory vault patterns
type: entity
tags: [entity, tool, agent-memory, obsidian, hooks, k143]
keywords: [obsidian-mind, qmd, vault-manifest, Claude Code hooks, Codex hooks, Gemini hooks, TipDrop]
related:
  - sources/cemini-repository-evaluation-plan-runtime-2026-07-04.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/headroom.md
  - concepts/context-compression-resume-pattern.md
maturity: draft
created: 2026-07-04
updated: 2026-07-04
---

## Relations

- @sources/cemini-repository-evaluation-plan-runtime-2026-07-04.md — K143 docx row; Phase-0 corrected Adopt → Steal-from
- @concepts/wiki-tooling-evaluation.md — Karpathy/wiki tooling register
- @entities/tools/headroom.md — sibling context/memory infrastructure candidate
- @concepts/context-compression-resume-pattern.md — memory persistence pattern overlap

## Raw Concept

K143 Phase-0 audit of [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind), prompted by the runtime docx's Adopt recommendation for TipDrop/David.

## Narrative

| Check | Result |
|-------|--------|
| **License** | MIT (`gh api` + LICENSE file, 2026-07-04) |
| **Maturity** | 3.2k★, 13 open issues, latest release v6.2.1 on 2026-06-02; tests passed in Phase-0 clone |
| **Stack** | Obsidian vault scaffold + Node/QMD + Claude/Codex/Gemini hook surfaces |
| **Verdict** | **Steal-from**, not Adopt |

Strong patterns to steal:

- `vault-manifest.json` split between infrastructure, scaffold, and user content.
- QMD index + MCP wrapper pattern for local semantic search over markdown.
- Hook test discipline across Claude Code, Codex, and Gemini surfaces.
- Plan-first vault migration prompt shape.

Why not adopt wholesale:

- Duplicates OSINT's filesystem-first wiki and Obsidian graph layer.
- Ships `.claude`, `.codex`, `.gemini`, and `.mcp.json` integration surfaces; lifecycle hooks should not be blindly installed into TipDrop/David workflows.
- Assumes its own vault layout (`brain/`, `work/`, `perf/`, `org/`) and writes derived state under local cache/config paths.
- Does not directly solve TipDrop M4's actual gap: OCR/OKF extraction and safe local ingest.

**TipDrop/David routing:** no adoption brief. If David needs anything here, it is a "do not install; steal manifest/QMD/hook-test patterns" note, not an implementation packet.

## Snippets

> "An Obsidian vault that gives AI coding agents persistent memory. Claude Code, Codex CLI, Gemini CLI." [Source: https://github.com/breferrari/obsidian-mind README (retrieved 2026-07-04)]

## Dead Ends

- Docx marked this Adopt for TipDrop M4, but Phase-0 found the fit is indirect and the install surface too broad for David's workspace-kit.
