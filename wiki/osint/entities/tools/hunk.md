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
updated: 2026-05-17
gemini_eval_doc1_url: 20
phase_0_verdict: GO 2026-05-17 (workflow-laptop; MIT verified, 4.1k stars, healthy contributor base)
adoption_status: PHASE-0-COMPLETE 2026-05-17
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

## Phase-0 Audit (2026-05-17)

**Repo**: `github.com/modem-dev/hunk` — cloned shallow to `/tmp/ph0-hunk/`. npm package name `hunkdiff`, current version `0.13.0-beta.0` (TypeScript/Bun, ES module).

### License — claim vs actual
- Gemini eval claimed **MIT**. **CONFIRMED**: `LICENSE` is verbatim MIT (`Copyright (c) Ben Vinegar`); GitHub `licenseInfo.key = mit`. SPDX: `MIT`. No copyleft. PASS.

### Maturity — observed vs claimed
| Metric | Value | vs Gemini claim |
|--------|-------|-----------------|
| Stars | 4,131 | claimed 3.8k — claim was conservative; actual is higher |
| Forks | 91 | — |
| Open issues | 22 | — |
| Created | 2026-03-17 (~2 months old) | — |
| Last push | 2026-05-17 (same-day) | — |
| Contributors | 24 total | — |

Very young repo (2 months) but rapid traction (4.1k★) and actively shipping (same-day push, beta-tagged releases with PR-numbered commits). Still pre-1.0 / beta — expect API churn.

### Failure-mode probe — license + maturity
- License: clean MIT, no concern.
- Maturity caveat: `0.13.0-beta.0` — **pre-1.0 beta software**. Fine for a laptop diff-viewer where breakage is low-stakes (worst case: fall back to `git diff`). Contributor base is healthier than a single-dev project — principal `benvinegar` 337 commits, but 23 other contributors (aliou 5, ferologics/elucid 4 each, plus a wide 1-commit tail). Truck factor ~2-3, better bus-factor than voicemode.

### Comparison vs existing Cemini coverage
No existing diff-review tool in the OSINT wiki. hunk replaces ad-hoc `git diff | less` for Claude-Code multi-file edit review — fills a genuine gap, no parallel implementation.

### Decision — GO
MIT verified, maturity strong for its age (4.1k★, 24 contributors, same-day commits), failure mode is low-stakes (laptop convenience tool, trivial fallback). Only caveat: pin a known-good beta version and re-pin deliberately given pre-1.0 churn. Verdict: **GO** (workflow-laptop).
