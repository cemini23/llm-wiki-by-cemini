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
  - sources/eval-url-revenue-opportunity-2026-08-17.md
  - entities/tools/filekey.md
  - sources/eval-multi-wiki-revenue-plan-2026-08-18.md
  - entities/tools/google-sam.md
  - entities/tools/llm-as-a-verifier.md
  - entities/tools/diagram-design.md
  - concepts/sovereign-agent-mesh-biscuit.md
  - sources/eval-project-revenue-url-2026-08-19.md
  - sources/eval-local-agent-infra-2026-08-19.md
  - entities/tools/mdflux.md
  - entities/tools/easy-agent.md
  - entities/tools/betterwright.md
  - entities/tools/ai-memory.md
  - sources/eval-multi-repo-revenue-2026-08-20.md
  - sources/eval-repository-revenue-2026-08-20.md
  - entities/tools/whisperlivekit.md
  - entities/tools/legal-templates.md
  - entities/tools/lore.md
  - entities/tools/google-timeline-visualizer.md
  - sources/arxiv-2608.17915-computational-prosopography-2026-08-20.md
maturity: draft
created: 2026-08-12
updated: 2026-08-20
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
- @sources/eval-url-revenue-opportunity-2026-08-17.md — K240 filekey GPL Extract-only
- @entities/tools/filekey.md — passkey isolate **pattern**; do not vendor GPL
- @sources/eval-project-revenue-url-2026-08-19.md — K242 eval
- @sources/eval-local-agent-infra-2026-08-19.md — K242 eval
- @entities/tools/mdflux.md — MIT local OCR wrapper; Transkribus sole HTR
- @entities/tools/easy-agent.md — MIT harness; human-gate `truth.ged`
- @entities/tools/betterwright.md — Playwright; Antenati IIIF local-only
- @entities/tools/ai-memory.md — reconstruct-before-inject; no Barone PII
- @sources/eval-multi-repo-revenue-2026-08-20.md — K243 WhisperLiveKit / legal-templates Extract
- @sources/eval-repository-revenue-2026-08-20.md — K243 Lore / timeline-visualizer Extract
- @entities/tools/whisperlivekit.md — Apache-2.0 streaming STT; not HTR; no Barone audio
- @entities/tools/legal-templates.md — CC0-1.0 ToS templates; HITL lawyer review
- @entities/tools/lore.md — MIT narrative/entity schemas; no living-person vitals
- @entities/tools/google-timeline-visualizer.md — MIT timeline maps; no Barone coordinates
- @sources/arxiv-2608.17915-computational-prosopography-2026-08-20.md — lineage/entity-resolution methodology; no Barone names

## Raw Concept

What this page answers: what Atto is, its product boundaries, and which K233 tools feed it.

## Narrative

Atto is a **local-first desktop kit for organizing Italian civil records and citizenship paperwork** — private, approve-only document organization; it does *not* decide eligibility. Product rule: "A fluent sentence is not a civil record" — judgment stays with the user or retained counsel. K233 feeds: anydoc (doc→Markdown), clapgrep (deep PDF search), tunnelto (ephemeral client vault previews). Never: private Barone/living-person vitals into Atto fixtures or git.

**K239 vault hygiene (Extract, not Integrate):** `fclones` (MIT) for APFS/CoW dedupe of IIIF/PDF trees — `fclones group` then reflink (`cp -c`); never unsupervised `--delete`. `openai/privacy-filter` (Apache-2.0) for fail-closed PII strip before MCP/LLM; **not** packyme/privacy-filter (K215). LFM encoder weights skipped (`license=other`). rachoon stays **AGPL isolate**. Brief: `../atto/briefs/2026-08-15_k239-atto-fclones-privacy-filter-cpu-pii.md`.

**K243 STT + legal + entity-resolution (2026-08-20):** `WhisperLiveKit` (Apache-2.0, ~43MB) is streaming **speech-to-text** for oral-history capture — **not handwriting**; Transkribus stays sole product HTR and any STT path stays local. `legal-templates` (CC0-1.0) feeds ToS drafting under **HITL lawyer review** before ship. `Lore` (MIT) contributes narrative/entity schemas and `google-timeline-visualizer` (MIT) timeline maps — both with **no living-person vitals / no Barone coordinates in git**. Prosopography (arXiv 2608.17915) is a lineage/entity-resolution methodology reference — **no Barone names**. Brief: `briefs/2026-08-20_k243-atto.md`.

[Source: Outlier Weekly 2026-08-11; K239/K243 evals; workspace Atto context]
