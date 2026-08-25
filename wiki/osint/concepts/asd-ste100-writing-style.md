---
title: "ASD-STE100 writing style for agent instructions"
type: concept
tags: [concept, harness, writing, ccc]
keywords: [ASD-STE100, Simplified Technical English, CLAUDE.md, readability]
related:
  - concepts/practical-loop-engineering.md
  - entities/tools/loop-engineering.md
  - "@ccc-wiki/concepts/claude-md-five-section-template.md"
maturity: draft
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- Federation `CLAUDE.md` files — runtime adoption surface
- @concepts/practical-loop-engineering.md — harness prose alongside loop primitives
- @ccc-wiki/concepts/claude-md-five-section-template.md — STE100 lives under **Style** in five-section bootstrap
- Brief: `briefs/2026-08-25_ste100-claude-md-federation-rollout.md` (local, gitignored)
- Paste block: `scripts/snippets/claude-md-ste100-section.md`

## Raw Concept

What this page answers: why and how to add **ASD-STE100 Simplified Technical English** (adapted) to Cemini federation agent schemas so technical explanations read like a clear engineering manual.

## Narrative

ASD-STE100 is a controlled writing standard from aerospace maintenance manuals. For LLM harness use (2026-08-25, prompted by @isitmidnite X post + operator request):

**Apply to:** chat replies, explanations, summaries, commit messages, PR descriptions, brief prose.

**Rules (adapted — not certified STE):**

- Short, direct sentences (~20 words for instructions, ~25 for descriptions).
- One plain word per concept; avoid jargon and synonyms.
- One instruction per sentence; imperative mood for steps.
- Active voice; simple tenses.
- Keep articles (the, a, an).
- One term per thing — use the same word every time.

**Do not rewrite:** source code, identifiers, file paths, CLI output, direct quotes, error messages.

**Rollout:** `## Writing style (ASD-STE100)` section added to federation root `CLAUDE.md` files (OSINT, CCC, CeminiSuite, wiki roots, federation-hub). Submodule / adopt clones listed in rollout brief for optional manual pass. Optional global copy: `~/.claude/CLAUDE.md`.

### Setup checklist (when helping someone new)

Use this every time you scaffold a workspace, fork `wiki-template`, or onboard a friend:

1. **Paste** `scripts/snippets/claude-md-ste100-section.md` into the root `CLAUDE.md` (before env/secrets section).
2. **Wiki fork:** confirm `wiki-template/SETUP.md` step 4 ran — template ships the section by default.
3. **Claude Code global:** copy the same block to `~/.claude/CLAUDE.md` so Home / empty-window sessions get it.
4. **CeminiSuite submodules:** only if the repo has per-package `CLAUDE.md` — see rollout brief list.
5. **Do not** paste into `.local/adopts/` clones or test harness `CLAUDE.md` files.

Agents: if you set up a new repo and the root `CLAUDE.md` lacks STE100, add it before claiming setup done. Log in `LESSONS.md` only when the rule itself changes — not per repo.

Reference implementations: [7a6ac0/asd-ste100-style](https://github.com/7a6ac0/asd-ste100-style), Medium "ASD-STE100 for Claude Code" (2026).

## Snippets

> Always explain technical things like a highly readable engineering manual.

[Source: operator prompt / X STE100 explainer image, 2026-08-25]
