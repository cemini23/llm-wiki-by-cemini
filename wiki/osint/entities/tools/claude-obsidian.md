---
title: claude-obsidian — Markdown-vault autoresearch loop (Adopt-tier, parallel-impl risk)
type: entity
tags: [tool, claude-code, obsidian, markdown-vault, autoresearch, adopt-tier, librarian-candidate, parallel-impl-risk]
keywords: [claude-obsidian, obsidian, markdown vault, autoresearch, contradiction flag, librarian, claude-mem]
related:
  - sources/evaluating-urls-cemini-project-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - entities/tools/claude-mem.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/evaluating-urls-cemini-project-2026-05-13.md` — origin source (Doc 1, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology
- `@entities/tools/claude-mem.md` — **parallel-impl risk**: claude-mem (v13.0.1, Phase-2 PASS 2026-05-12) already adopted laptop-side for session-memory; claude-obsidian's autoresearch + `[!contradiction]` syntax overlaps partially

## Raw Concept

Stub created from Doc 1 K42 eval (2026-05-13). Adopt-tier; cross-routed to OSINT (3-round autoresearch loop) + Cybersec (`[!contradiction]` syntax for pentest report cross-ref).

## Narrative

- **Eval claim**: `/autoresearch` 3-round autonomous loop integrated into Obsidian markdown vault; `[!contradiction]` syntax for cross-referencing conflicting reports.
- **Use case**: continuous threat-actor profiling (OSINT) or pentest report contradiction surfacing (Cybersec).
- **Parallel-impl decision required**: claude-mem covers session memory (semantic injection, observation indexing). claude-obsidian appears to target vault-side reasoning across markdown documents — different scope, potentially additive rather than substitutive.

### Phase-0 audit (PENDING) — load-bearing questions

1. License (verify LICENSE file)
2. Does it require an Obsidian vault, or any markdown directory tree?
3. Cemini's wiki uses nested entity subdirectories — does claude-obsidian respect nesting?
4. How does the 3-round autoresearch loop scope its queries? Cost profile per query?
5. Does `[!contradiction]` syntax conflict with existing Cemini convention (`[NEEDS VERIFICATION YYYY-MM-DD]`)?
6. Hook overlap with claude-mem (e.g., SessionStart hooks, statusline)?

→ Update `@concepts/wiki-tooling-evaluation.md` with claude-obsidian as new candidate

[NEEDS VERIFICATION 2026-05-13]

[Source: Evaluating URLs for Cemini Project.docx (retrieved 2026-05-13)]
