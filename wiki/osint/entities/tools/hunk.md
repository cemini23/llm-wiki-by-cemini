---
title: "hunk — TUI diff viewer for AI-generated multi-file changes (Adopt, workflow)"
type: entity
tags: [tool, diff-viewer, tui, claude-code-companion, code-review, gemini-eval-doc1, phase-0-adopt-candidate]
keywords: [hunk, modem-dev, pierre diffs, inline annotations, ai-diff, multi-file review]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
gemini_eval_doc1_url: 20
phase_0_verdict: ADOPT-CANDIDATE 2026-05-12 (workflow-laptop)
adoption_status: PRE-PHASE-0 2026-05-12
---

## Relations

- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — source eval (URL 20)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — corrected multi-wiki prompt
- `@concepts/tool-evaluation-framework.md` — three-surface methodology

## Raw Concept

- **Repo**: `github.com/modem-dev/hunk`
- **License** [per Gemini eval]: MIT
- **Tier**: Adopt
- **Primary fit**: Workflow (Claude Code companion)

## Narrative

TUI diff viewer specialized for AI-generated multi-file changes. Renders Pierre-style diffs with inline AI annotation support — designed for reviewing the kind of cross-file edits Claude Code emits on larger tasks. Replaces raw `git diff | less` for any session producing >2 file edits.

### Integration vector

Drop-in laptop install (single-binary TUI). Use as the standard reviewer between Claude Code's "edits applied" message and the user's commit decision. Phase-0: confirm star count + last commit date (Gemini eval cited 3.8k stars but flagged for verification).
