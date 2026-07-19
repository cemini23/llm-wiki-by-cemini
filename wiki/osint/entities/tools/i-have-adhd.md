---
title: "i-have-adhd (Claude skill)"
type: entity
tags: [tool, k174, skill]
keywords: [i-have-adhd, claude-skill, action-first]
related:
  - sources/eval-repository-revenue-opportunity-analysis-2026-07-19.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/code-review-graph.md
maturity: draft
created: 2026-07-19
updated: 2026-07-19
---

## Relations

- @sources/eval-repository-revenue-opportunity-analysis-2026-07-19.md
- @concepts/wiki-tooling-evaluation.md
- @entities/tools/code-review-graph.md

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | ayghri/i-have-adhd |
| **License** | MIT (~0.3MB) |
| **Verdict** | **Extract** |
| **Routing** | CCC / TipDrop / xsp |

Claude Code skill: action-first, numbered steps, no preamble/tangent burial. Improves agent→human throughput.

## Wired (K174 local)

- Clone: `.local/adopts/i-have-adhd`
- Cursor skill symlink: `.cursor/skills/i-have-adhd` + TipDrop mirror
- Optional CC: `claude plugin marketplace add` + `install i-have-adhd@i-have-adhd`
