---
title: openmed — local clinical NER and PII de-identification
type: entity
tags: [tools, privacy, pii, ner, on-device, apple-silicon]
keywords: [openmed, clinical-ner, pii-deidentification, hipaa, mlx, coreml, on-device]
related:
  - sources/eval-url-revenue-opportunity-2026-10-13.md
  - concepts/k290-eval-wave.md
  - concepts/atto-local-first-threat-model.md
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md
maturity: draft
created: 2026-10-13
updated: 2026-11-02
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

### Re-surfaced — v10.10 batch C (2026-11-02)

`@sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md` URL 12 rates openmed **Extract** again and routes it to Atto and `Desktop/family/research/` for pre-share PII scrubbing on the Access share surface.

**The new finding corrects the licence claim.** The report says "Apache-2.0 — permissive, cleanly avoids Atto's GPL vendor ban". Phase-0 on 2026-11-02 found that statement is true of the **SDK only**:

> The SDK is Apache-2.0. The README states that **model and dataset licenses differ**, and third-party notices are in a `NOTICE` file.

The PII stack is a family of weights — `pii_superclinical_large`, and a "Privacy Filter" line with three variants (OpenAI Privacy Filter, a Nemotron-PII fine-tune, and an OpenMed Multilingual build), each in PyTorch, MLX, and MLX 8-bit. **Each of those carries its own terms.** The GPL-clearance argument holds for the code and must be re-checked per checkpoint before anything ships inside an Atto kit.

**Language coverage — the open question for Atto.** There are **42 PII language codes, of which 35 are model-backed**. The list returned by the fetch named en, es, fr, de, pt, nl, ar, hi, ja, tr, zh, ta, bn, ru, sw — **Italian was not among them**. The workspace's actual PII classes are Italian civil-registry, citizenship, and genealogy records. Confirm that Italian is model-backed, and test it on real record text, before planning on it. `[NEEDS VERIFICATION 2026-11-02]`

**Performance.** MLX is claimed at **24–33× faster than CPU PyTorch** for the Privacy Filter. Repository is on **`master`**, not `main` — the `main` raw path 404s.

**Routing note.** The report lists family-tree as a secondary overlap. The 2026-10-13 caveat still stands unchanged: a clinical-NER model is not tuned on Italian civil records, and transfer has not been tested.

## Snippets

> Local-first clinical NER + HIPAA-grade PII de-identification on Apple MLX/CoreML. [Source: Repository Revenue Opportunity Analysis.docx — entry 8]
