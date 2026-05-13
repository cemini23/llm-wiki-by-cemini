---
title: "multi-model-redteam — parallel red-team prompt (Conditional-Adopt, no-LICENSE)"
type: entity
tags: [tool, red-team, parallel-models, no-license-found, conditional-adopt, gemini-eval-doc2, catalog-mode-1]
keywords: [multi-model-redteam, permoon, no license file, red team prompt, parallel adversarial]
related:
  - sources/evaluating-project-links-systems-2-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/cemini-license-posture.md
  - "@cybersecurity-wiki/entities/tools/multi-model-redteam.md"
maturity: draft
created: 2026-05-12
updated: 2026-05-12
gemini_eval_doc2_url: 14
phase_0_verdict: CONDITIONAL-ADOPT (laptop only) 2026-05-12 — README content public, but NO LICENSE blocks any IP-sale-bearing surface
---

## Relations

- `@sources/evaluating-project-links-systems-2-2026-05-12.md` — source eval (URL 14)
- `@concepts/cemini-license-posture.md` — NO LICENSE catalog tracker
- `@cybersecurity-wiki/entities/tools/multi-model-redteam.md` — cybersec primary

## Raw Concept

- **Repo**: `github.com/permoon/multi-model-redteam`
- **License**: NO LICENSE FOUND (catalog mode #1 occurrence)
- **Tier**: Conditional-Adopt (laptop only)
- **Primary fit**: Workflow (laptop-side adversarial prompt) + cybersec wiki

## Narrative

~30-line parallel red-team prompt running multiple LLMs against a single target. Gemini eval flagged "Adopt despite no LICENSE." Re-graded: **content is in the public README** (the prompt itself is the value), so laptop-side use carries no IP risk. **But** cannot ship to Cemini prod or librarian server until LICENSE clarified.
