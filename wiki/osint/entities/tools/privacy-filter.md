---

title: privacy-filter
type: entity
tags: [entity, tool, atto, phase-0, k215, pii]
keywords: [packyme/privacy-filter]
related:
  - sources/eval-github-repo-revenue-opportunity-analysis-2026-07-31-pii-privacy.md
  - sources/eval-url-revenue-opportunity-2026-08-15.md
  - entities/tools/openai-privacy-filter.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-07-31
updated: 2026-08-15
harness_verb: FILE
---

## Relations

- @sources/eval-github-repo-revenue-opportunity-analysis-2026-07-31-pii-privacy.md — K215
- @sources/eval-url-revenue-opportunity-2026-08-15.md — K239 eval cites this as name-collision
- @entities/tools/openai-privacy-filter.md — **different repo** (`openai/privacy-filter`, Apache-2.0, K239)
- @concepts/gpuology-genealogy-agent-kit.md — vault PII

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/packyme/privacy-filter |
| License | **MIT** |
| Local | `.local/adopts/privacy-filter (~464KB)` |
| Verdict | **GO Extract** — privacy filter patterns |

**Name collision (K239):** this page is `packyme/privacy-filter` (MIT). K239 Extract is `openai/privacy-filter` (Apache-2.0) → `@entities/tools/openai-privacy-filter.md`. Do not merge.
