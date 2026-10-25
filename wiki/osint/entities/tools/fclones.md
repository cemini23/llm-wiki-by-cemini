---
title: "fclones — APFS/CoW duplicate finder (Atto vault Extract, K239)"
type: entity
tags: [tool, atto, dedupe, rust, k239, phase-0]
keywords: [fclones, pkolaczk, APFS, reflink, BLAKE3, vault]
related:
  - sources/eval-url-revenue-opportunity-2026-08-15.md
  - concepts/atto-genealogy-agent-kit.md
  - entities/tools/openai-privacy-filter.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
harness_verb: FILE
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-15.md — K239 eval (GO Extract)
- @concepts/atto-genealogy-agent-kit.md — IIIF/PDF vault dedupe
- @entities/tools/openai-privacy-filter.md — PII strip after/before archive ingest

## Raw Concept

What prompted this page: K239 eval URL 7. Docx Extract + **MIT verified** via `gh api`. Cloned `.local/adopts/fclones` (1MB).

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/pkolaczk/fclones |
| License | **MIT** (`gh api` + LICENSE file) |
| Local | `.local/adopts/fclones` (1MB, depth-1) |
| Verdict | **GO Extract** — CLI pattern into Atto vault packaging; do not vendor as a required runtime if a one-shot `fclones group` + `cp -c` script suffices |

Rust duplicate finder (Rayon, xxHash/BLAKE3). Prefix/suffix hash before full-file hash. Native **APFS / Linux reflink CoW** so identical Antenati IIIF tiles or PDFs can live under multiple ancestor folders without doubling disk.

### Steal-for-Atto

- One-shot vault hygiene: `fclones group` then reflink (`cp -c`) — not a destructive `rm` default.
- Guard delete flags. Do not run unsupervised `--delete` on `~/Desktop/family` or AttoVault.
- Confirm reflink survival when copying a vault to an external backup volume `[OPEN QUESTION 2026-08-15]`.

**Do not** put private Barone paths or living-person filenames into git examples.

Tier: `[TENTATIVE]`.
