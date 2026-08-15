---

title: Atto — Italian civil-record genealogy agent kit
type: concept
tags: [concept, atto, genealogy, product, k233]
keywords: [atto, italian-citizenship, civil-records, jure-sanguinis, local-first]
related:
  - sources/newsletter-outlier-weekly-italy-2026-08-11.md
  - concepts/computational-genealogy-archival-automation.md
  - entities/tools/anydoc.md
  - entities/tools/clapgrep.md
  - entities/tools/tunnelto.md
  - sources/arxiv-2608.12566-domus-2026-08-14.md
  - concepts/e2ee-vault-share.md
  - entities/tools/ente.md
  - sources/arxiv-2608.13463-mllm-ensembles-2026-08-14.md
  - sources/eval-url-revenue-opportunity-2026-08-15.md
  - entities/tools/fclones.md
  - entities/tools/openai-privacy-filter.md
maturity: draft
created: 2026-08-12
updated: 2026-08-15

---

## Relations

- @sources/newsletter-outlier-weekly-italy-2026-08-11.md
- @concepts/computational-genealogy-archival-automation.md
- @entities/tools/anydoc.md — GO Integrate
- @entities/tools/clapgrep.md — GO Extract
- @entities/tools/tunnelto.md — GO Extract
- @sources/eval-url-revenue-opportunity-2026-08-15.md — K239 fclones + openai/privacy-filter
- @entities/tools/fclones.md — APFS CoW vault dedupe (MIT)
- @entities/tools/openai-privacy-filter.md — Apache-2.0 PII strip (≠ packyme)

## Raw Concept

What this page answers: what Atto is, its product boundaries, and which K233 tools feed it.

## Narrative

Atto is a **local-first desktop kit for organizing Italian civil records and citizenship paperwork** — private, approve-only document organization; it does *not* decide eligibility. Product rule: "A fluent sentence is not a civil record" — judgment stays with the user or retained counsel. K233 feeds: anydoc (doc→Markdown), clapgrep (deep PDF search), tunnelto (ephemeral client vault previews). Never: private Barone/living-person vitals into Atto fixtures or git.

[Source: Outlier Weekly 2026-08-11; workspace Atto context]
