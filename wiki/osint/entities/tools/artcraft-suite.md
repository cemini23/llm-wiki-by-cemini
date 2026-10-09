---
title: "ArtCraft (storytold/*) — Rust clean-room Adobe-suite replacements"
type: entity
tags: [tool, creative, rust, apache-2.0, atto, k284]
keywords: [artcraft, storytold, photocraft, printcraft, designcraft, vectorcraft, lightcraft, filmcraft, effectcraft, clean-room, k284]
related:
  - sources/eval-url-revenue-opportunity-2026-10-07.md
  - concepts/k284-eval-wave.md
  - sources/eval-multi-repo-revenue-2026-10-09.md
maturity: draft
created: 2026-10-07
updated: 2026-10-09
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-10-07.md — K284 eval (tier: **Integrate**, three apps)
- @concepts/k284-eval-wave.md — K284 cluster hub
- @sources/eval-multi-repo-revenue-2026-10-09.md — K287 fold. Umbrella repo stays NOASSERTION.

## Raw Concept

- **Org:** `github.com/storytold` (the "ArtCraft" project)
- **Tier (K284):** **Integrate** — photocraft, printcraft, designcraft. Extract — vectorcraft, lightcraft. Watch — effectcraft, filmcraft.
- **License:** **Apache-2.0** (all seven, verified 2026-10-07)
- **Activity:** all active, pushed 2026-10-06/07

## Narrative

A family of **seven clean-room, pure-Rust reimplementations of the Adobe apps**:

| App | Replaces | Stars (verified) | K284 tier |
|-----|----------|------------------|-----------|
| photocraft | Photoshop | 12,693 | Integrate |
| filmcraft | Premiere Pro | 2,443 | Watch |
| lightcraft | Lightroom | 2,006 | Extract |
| printcraft | Acrobat | 1,751 | Integrate |
| vectorcraft | Illustrator | 1,610 | Extract |
| effectcraft | (motion graphics) | 1,236 | Watch |
| designcraft | InDesign | 738 | Integrate |

### Why it matters here

The **Atto document pipeline**: **enhance archive scans (photocraft) → typeset a family-history monograph (designcraft) → bind the evidentiary PDF packet (printcraft)**. This removes Adobe licensing cost and keeps **client PII entirely local** — a genuine margin and privacy win for Concierge cases. `lightcraft` (RAW/colour) and `vectorcraft` (pedigree charts) extend it.

### Constraints

- photocraft needs explicit `--automation-read-root` / `--automation-write-root` boundary flags for agent use.
- The `filmcraft` / `effectcraft` rows are **Watch** (headless NLE / motion graphics) — not yet proven.
- Apache-2.0 is a clean licence for internal use.

### Boundary

FILE only — no install. Human-gated. Client PII stays in `~/AttoVault/`.

### K287 fold (2026-10-09)

The docx names `storytold/artcraft` again as Extract. Already audited. `gh api` on 2026-10-09: umbrella repo licence **NOASSERTION**, 11,194 stars, last push 2026-10-09. The seven app repos on this page stay Apache-2.0 from K284. No new brief. No install. No image-generation wire.

## Snippets

> "Integrating PhotoCraft, DesignCraft, and PrintCraft eliminates external Adobe licensing costs and automates dossier compilation." [Source: eval-url-revenue-opportunity-2026-10-07.md]
