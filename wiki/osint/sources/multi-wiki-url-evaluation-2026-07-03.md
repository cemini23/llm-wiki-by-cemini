---
title: "Multi-Wiki URL Evaluation.docx — OCR, agent harness, and compliance tools (2026-07-03)"
type: source
tags: [tool-evaluation, multi-wiki, agent-harness, ocr, tipdrop, k142, docx]
keywords: [olmocr, astryx, caveman, zero, ifixai, portable-llm-wiki, claude-real-video, agent-reach, meetily, tipdrop]
related:
  - entities/tools/olmocr.md
  - entities/tools/claude-real-video.md
  - entities/tools/ifixai.md
  - entities/tools/agent-reach.md
  - entities/tools/meetily.md
  - entities/tools/agent-skills-addyosmani.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-wiki-ingest-workflow.md
maturity: draft
read_status: read
created: 2026-07-03
updated: 2026-07-03
clusters: [wiki-tooling, agent-harness, ocr, tipdrop]
---

## Relations

- @entities/tools/olmocr.md — Adopt, Apache-2.0; OSINT + TipDrop M4 PDF OCR
- @entities/tools/claude-real-video.md — Steal-from, MIT; local video ingest pattern
- @entities/tools/ifixai.md — Adopt, Apache-2.0; agent deception/compliance diagnostics
- @entities/tools/agent-reach.md — Adopt wrapper-only; upstream scraping blocked by cookie/security risk
- @entities/tools/meetily.md — Defer; local ASR engine useful but monolithic desktop shape
- @entities/tools/agent-skills-addyosmani.md — Adopt selectively; avoid always-on context bloat
- @concepts/cemini-wiki-ingest-workflow.md — ingestion pipeline target surface
- @concepts/wiki-tooling-evaluation.md — multi-wiki tool-eval doctrine

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Multi-Wiki URL Evaluation |
| **Type** | DOCX + companion screenshot (`x.jpeg`) |
| **sha256** | `a49d1993fe30fadee9f6f7f630d19c4597a78e216753c3a07b359e4c2442a01d` |
| **x.jpeg Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/x.jpeg` |
| **x.jpeg sha256** | `dd45913a0d1281e83eef26dc550da8842c363d439999a56502f8be6faee2ed50` |
| **URLs** | 20 |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki URL Evaluation.docx` |
| **Retrieved** | 2026-07-03 |
| **Read status** | read (`gh api` license/maturity spot-check on GitHub rows; Phase-0 via `scripts/adopt_k142_phase0.sh`) |

## Narrative

K142 is a multi-wiki tool-eval batch centered on **OCR/OSINT extraction**, **agent/coding harnesses**, and **TipDrop compliance/ingest gaps**. License spot-checks confirmed the main GitHub SPDX claims: `olmocr` and `iFixAi` are Apache-2.0; Astryx, Caveman, Zero, Agent Skills, Agent-Reach, Meetily, claude-real-video, and the hardware/reference repos are MIT; Huly is EPL-2.0; `cs249r_book` remains `NOASSERTION`.

### Tier distribution

| Tier | Count | Items |
|------|-------|-------|
| **Adopt** | 5 | `allenai/olmocr`, `JuliusBrussee/caveman`, `Gitlawb/zero`, `ifixai-ai/iFixAi`, `addyosmani/agent-skills` |
| **Adopt wrapper-only** | 1 | `Panniantong/Agent-Reach` local manual snapshot wrapper |
| **Steal-from** | 3 | `facebook/astryx`, `HUANGCHIHHUNGLeo/claude-real-video`, `portablellm.wiki` |
| **Defer** | 3 | `CoreBunch/Instatic`, `Zackriya-Solutions/meetily`, `langflow-ai/langflow` |
| **Reference-only** | 5 | `logto-io/logto`, `harvard-edge/cs249r_book`, `Shubhamsaboo/awesome-llm-apps`, `autonomous-ai/autonomous-computer`, `tasteskill.dev` |
| **Reject** | 3 | `hcengineering/platform`, `microsoft/qlib`, `Archive228/loopkit` |

### Phase-0 decisions

- **OSINT / TipDrop M4:** `olmocr` is Adopt for complex PDFs, gated by local GPU/quality benchmarking against current parsers.
- **OSINT multimedia:** `claude-real-video` is Steal-from for scene-aware frames + transcript manifests; do not adopt dependency until fast-cut/context behavior is benchmarked.
- **Cybersec / TipDrop M2:** `iFixAi` is Adopt as an agent-output diagnostic harness, not as a legal compliance certification.
- **OSINT / TipDrop social ingest:** Agent-Reach upstream direct integration stays **Defer**, but OSINT now **Adopts wrapper-only** for manual snapshots after local P0 tests and operator approval.
- **CCC:** Astryx, Caveman, Zero, Addy Agent Skills, Portable LLM Wiki, and the `x.jpeg` model-selection note route to CCC as operator/harness material.

## Snippets

> "tipdrop genuine gaps: [allenai/olmocr (M4 - complex PDF OCR extraction), portablellm.wiki (M4 - Open Knowledge Format Markdown graph structuring), ifixai-ai/iFixAi (M2 - diagnostic guardrails against model deception)]." [Source: Multi-Wiki URL Evaluation.docx aggregate summary (retrieved 2026-07-03)]

> "Cost is a tie-breaker only; when axes conflict for anything that ships, intelligence > taste > cost." [Source: x.jpeg screenshot (retrieved 2026-07-03)]
