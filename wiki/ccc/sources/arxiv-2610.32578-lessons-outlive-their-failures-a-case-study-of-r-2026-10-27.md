---
title: "Lessons Outlive Their Failures: Rules for AI Coding Agents"
type: source
tags: [source, arxiv, agent-rules, documentation-drift]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Lessons Outlive Their Failures: A Case Study of Rules for AI Coding Agents |
| Authors | Hassan Hassanzadeh Aliabadi (independent researcher) |
| arXiv | 2610.32578 |
| File | `arxiv-2610.32578-lessons-outlive-their-failures-a-case-study-of-r.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32578 |
| Read status | skimmed (abstract + intro) |

## Narrative

A six-week case study of one personal markdown repository that three AI agent tools edited daily under one shared rule set. The harness is the familiar one: rule files such as `AGENTS.md`, on-demand skills, runtime hooks, and automated checks.

The author kept a **ledger of 118 agent failures**, the fix for each, and whether the failure returned.

Key findings:

- **Drift was the largest failure class** — 48 of 118 failures were stale documentation. 35 of those 48 were found on a single audit day.
- A single documentation audit found about half of known drift (Claude Sonnet 5.5 mean: 50%). At least 93% of its findings were correct.
- On Sonnet 5.5 the agent finished four of five replayed tasks. In three of those four, the failure did not happen with or without its fix. Only the stale-count failure returned without its check, and the check stopped it in every run.
- A written rule on run-time estimates did not change Sonnet 4.5's overestimates.
- On older models, an agent drafted an em-dash once while the em-dash lint check was active, and the check rejected it.

**The core claim:** harness lessons can outlive the failures they were written to fix. A rule that fixed a failure on one model may be inert on the next. Drift, by contrast, persists and still needs mechanical checks, not prose rules.

The author states the limits plainly: one repository, three runs per condition, exploratory results.

**Why it matters.** This is direct evidence for a rule this workspace already follows — mechanical gates beat written rules. It also warns that a lint check can outlive its original bug and should be re-tested per model.

## Snippets

> "Stale documentation (drift) was the largest failure class (48 of 118), although 35 of those were found on one audit day." [Source: `arxiv-2610.32578-lessons-outlive-their-failures-a-case-study-of-r.pdf` p.1 (arXiv 2610.32578), retrieved 2026-10-27]

> "These results suggest that harness lessons can outlive the failures they were written to fix, while drift persists and still needs mechanical checks." [Source: same, p.1]
