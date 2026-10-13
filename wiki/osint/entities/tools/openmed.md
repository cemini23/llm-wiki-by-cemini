---
title: openmed — local clinical NER and PII de-identification
type: entity
tags: [tools, privacy, pii, ner, on-device, apple-silicon]
keywords: [openmed, clinical-ner, pii-deidentification, hipaa, mlx, coreml, on-device]
related:
  - sources/eval-url-revenue-opportunity-2026-10-13.md
  - concepts/k290-eval-wave.md
  - concepts/atto-local-first-threat-model.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
wire_status: extract_only
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-10-13.md
- @concepts/k290-eval-wave.md
- @concepts/atto-local-first-threat-model.md

## Raw Concept

**What prompted this page:** K290 tool eval (2026-10-13), entry 8 — **Extract tier**. `github.com/maziyarpanahi/openmed`.

## Narrative

**Local-first clinical named-entity recognition plus HIPAA-grade PII de-identification**, running on **Apple MLX / CoreML**. Everything stays **on device** — no model call, no network path for the sensitive text.

**License:** **Apache-2.0** — `[CONFIRMED]`. **Docx star count was wrong** (2.2k claimed; **5.7k actual**).

**Docx tier: Extract** (high value, 30d) — *"protect Atto kit privacy / prevent living-individual PII leaks."*

**Why it matters here:** this fits the **existing workspace rule** that **PII is stripped before any LLM sees civil documents**, with the established pattern set (`@concepts/atto-local-first-threat-model.md`, plus the `pii-redaction`, `privacy-filter` and `openredaction` tool pages). `openmed` is a **local NER-and-redaction** option in that chain: **neither the document nor the extracted entities leave the machine.**

**Caveats to verify before use:** the docx lists **issues NOT FOUND** — thread health is unverified. And a clinical-NER model is tuned on **health records**, not on **Italian civil-registry, citizenship or genealogy documents**, which are this workspace's actual PII classes. **Do not assume transfer without testing.** **Phase-0 ran 2026-10-13** — **Apache-2.0** confirmed by `gh api`; cloned to `.local/adopts/k290/openmed` (151 MB). The transfer caveat above is still untested.

## Snippets

> Local-first clinical NER + HIPAA-grade PII de-identification on Apple MLX/CoreML. [Source: Repository Revenue Opportunity Analysis.docx — entry 8]
