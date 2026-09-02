---

title: genealogy_ai (matthieugraziani) — French civil-status HTR
type: entity
tags: [entity, tool, genealogy, atto, htr, phase-0, k211]
keywords: [PaddleOCR, GEDCOM, état civil, Ollama, FastAPI]
related:
  - sources/eval-github-revenue-opportunity-analysis-2026-07-29-civil-legal.md
  - sources/eval-github-repo-revenue-evaluation-2026-07-29-genealogy-legal.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-07-29
updated: 2026-07-31
harness_verb: FILE
---

## Relations

- @sources/eval-github-revenue-opportunity-analysis-2026-07-29-civil-legal.md — paired opp analysis

- @sources/eval-github-repo-revenue-evaluation-2026-07-29-genealogy-legal.md — K211 Extract
- @concepts/gpuology-genealogy-agent-kit.md — product hub

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/matthieugraziani/genealogy_ai |
| License | **MIT** (`gh api`) |
| Local | `.local/adopts/genealogy_ai` (~232KB) |
| Verdict | **CONDITIONAL-GO Extract** — HTR/OCR → GEDCOM pipeline patterns for Atto; French spaCy defaults need Italian swap |
| Stack | OpenCV · PaddleOCR/EasyOCR/Tesseract · local Mistral via Ollama · RapidFuzz · NetworkX/Neo4j · FastAPI · Streamlit · GEDCOM 5.5.1 |

Do **not** vendor as Atto product dependency without Transkribus/HTR isolation review. Steal preprocess + export stages only.
