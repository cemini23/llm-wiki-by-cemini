---
title: Tint (dhfbk) — Italian NLP Tool
type: entity
tags: [tool, genealogy, nlp, italian, k175, integrate]
keywords: [Tint, CoreNLP, named entity, Italian morphology, Antenati HTR post-process]
related:
  - sources/gemini-gpuology-genealogy-business-analysis-2026-07-20.md
  - concepts/gpuology-genealogy-agent-kit.md
  - sources/eval-url-revenue-and-project-analysis-2026-07-20.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - entities/tools/transkribus.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations
- @concepts/gpuology-genealogy-agent-kit.md — product strategy (K176)

- @sources/eval-url-revenue-and-project-analysis-2026-07-20.md — K175 Integrate
- @concepts/computational-genealogy-archival-automation.md — HTR → entity extraction step
- @concepts/italian-regional-genealogy-archive-playbook.md — Italian text stack
- @entities/tools/transkribus.md — upstream HTR; Tint is post-OCR/HTR NLP

## Raw Concept

Italian-specific NLP pipeline on Stanford CoreNLP (FBK). Eval hypothesis: parse Antenati/HTR transcriptions for names, dates, kinship roles.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [dhfbk/tint](https://github.com/dhfbk/tint) |
| **License** | GPL-3.0 [CONFIRMED Phase-0 license API 2026-07-20] |
| **Stars / push** | ~73★ · last push 2023-04 [CONFIRMED] |
| **Verdict** | **CONDITIONAL-GO** — private family only; no SaaS vendor |
| **Routing** | family-tree · GPUOLOGY playbook (patterns), not SaaS vendoring |
| **Risks** | Inference RSS ~1.2 GB; GPL copyleft if shipped in commercial kit; stale upstream (last push 2023) |

### Phase-0 (2026-07-20)

| Field | Value |
|-------|-------|
| **Install** | `~/Desktop/family/research/tools/tint/` (from `/tmp/k175-tint-audit`) |
| **SPDX** | GPL-3.0 [CONFIRMED] |
| **Verdict** | **CONDITIONAL-GO** — private family only |
| **Build** | `mvn -DskipTests package` SUCCESS; build peak RSS ~410 MB |
| **Infer smoke** | `TintRunner` JSON on synthetic Italian act sentence SUCCESS; peak RSS **~1226 MB** |
| **Risk** | Budget ≥1.2 GB RAM; GPL SaaS binary ship blocked |

Notes: `~/Desktop/family/research/tools/TINT-SMOKE-2026-07-20.md`. Phase-0 report: `.local/reports/k175-phase0-2026-07-20.md`.

## Snippets

> "Tint … POS tagging, entity linking, dependency parsing" for Italian — eval paraphrase [Source: @sources/eval-url-revenue-and-project-analysis-2026-07-20.md]
