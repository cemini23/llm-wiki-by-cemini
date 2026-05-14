---
title: "Zijian-Ni/awesome-ai-agents-2026 — Frontier-Model Index"
type: entity
tags: [tool, awesome-list, frontier-models, index, mit, reference-only, github-eval-2026-05-13]
keywords: [awesome-ai-agents-2026, frontier-model-index, gemini-3-1-pro, claude-opus-4-7, gemma-4-31b, benchclaw, reference-only]
related:
  - sources/eval-github-repos-2026-05-13.md
  - concepts/agent-cost-routing-model-orchestra.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @sources/eval-github-repos-2026-05-13.md — Phase-0 eval source (REFERENCE-ONLY verdict)
- @concepts/agent-cost-routing-model-orchestra.md — periodic refresh source for the model orchestra config

## Raw Concept

What prompted this page: Phase-0 eval (May 13 2026) flagged as REFERENCE-ONLY — useful as a discovery index for frontier-model entries, not as an adoptable codebase. MIT-licensed (but moot for reference-only use).

## Narrative

### Identity

- **Repo**: `Zijian-Ni/awesome-ai-agents-2026` (GitHub)
- **License**: MIT (curated list; license applies to the list itself, not the linked tools)
- **Type**: Awesome-list / discovery index for frontier AI models + agents

### Notable entries cataloged

- **Gemini 3.1 Pro** (Google)
- **Claude Opus 4.7** (Anthropic)
- **Gemma 4 31B** (Google open-weights)
- **BenchClaw** (benchmark / evaluation tooling)

These four are flagged as the headline 2026 frontier entries.

### Adoption posture

**REFERENCE-ONLY** — Cemini does not code-couple to awesome-lists. The use-pattern is:

1. Periodic refresh of `@concepts/agent-cost-routing-model-orchestra.md` — when a new frontier model lands, this list is one signal that the orchestra config needs review
2. Discovery source for individual repos to audit under the normal Phase-0 audit pattern
3. Pricing/capability lookup when comparing model options at the cost-routing layer

### Refresh cadence

Quarterly. The awesome-list churn rate is fast; entries can lag the latest releases by 1–2 weeks. Cemini's orchestra config should not be slaved to this list — use it as a starting point, then verify directly with the model provider for current pricing and capability.

### Why MIT matters less here

Cemini doesn't depend on the list as code — it's a markdown file consulted by humans. MIT license is fine, but moot.

## Snippets

> "Frontier 2026 entries: Gemini 3.1 Pro, Claude Opus 4.7, Gemma 4 31B, BenchClaw." [Source: eval-github-repos-2026-05-13.docx, derived from the list contents]

## Dead Ends

- **Auto-syncing the orchestra config to this list** — list churn rate is too high and verification quality varies entry-to-entry. The list is a discovery aid, not a config source.
- **Treating awesome-list entries as pre-vetted** — every entry still needs the standard Cemini Phase-0 audit before adoption. The list filters for "exists and has eyeballs," not for "production-ready for Cemini's use case."
