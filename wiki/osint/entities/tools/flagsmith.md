---
title: "Flagsmith — Feature Flag Platform (License-Gated)"
type: entity
tags: [tool, feature-flags, python, django, postgresql, deferred, license-verification]
keywords: [Flagsmith, feature flags, Django, PostgreSQL, remote config, license verification]
related:
  - sources/project-link-evaluation-brief-5_10.md
  - entities/tools/growthbook.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/project-link-evaluation-brief-5_10.md` — source evaluation brief (URL 11)
- `@entities/tools/growthbook.md` — alternative feature flag platform (Steal-from tier)

## Raw Concept

Flagsmith is a feature management and remote configuration platform with a Python/Django API backend and PostgreSQL database. Self-hostable with minimal resource requirements.

- **Repo**: `github.com/Flagsmith/flagsmith`
- **License**: NOT FOUND — requires manual GitHub verification
- **Stack**: Python/Django, PostgreSQL, optional Node.js edge proxy
- **Footprint**: 512 MB RAM, 1 CPU core

## Narrative

**Verdict: Defer** — architectural fit is exceptional (Python/Django + PostgreSQL aligns perfectly with Cemini's existing stack), but adoption is strictly gated on human verification of the LICENSE file. The 512 MB RAM footprint fits within Hetzner constraints.

If license clears (MIT/Apache-2.0/BSD): Flagsmith would be a stronger fit than GrowthBook for Cemini — same stack (Python/Django + PostgreSQL vs TypeScript + MongoDB), smaller footprint, simpler architecture. The MCP integration would allow `agents/orchestrator.py` to dynamically toggle trading subroutines via feature flags.

### Open questions

- Explicit SPDX identifier must be manually retrieved from GitHub `[OPEN QUESTION 2026-05-10]`
- Transitive Python dependencies within Django API must be checked for AGPL/GPL contamination `[NEEDS VERIFICATION 2026-05-10]`

[Source: Project Link Evaluation Brief 5_10.docx, URL 11]
