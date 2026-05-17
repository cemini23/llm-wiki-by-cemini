---
title: "veloxdb — Tauri+Rust native PostgreSQL client (Adopt, Cemini PG admin)"
type: entity
tags: [tool, postgresql, database-client, tauri, rust, macos-keychain, ssh-tunnel, er-diagrammer, gemini-eval-doc1, phase-0-adopt-candidate]
keywords: [veloxdb, abeni16, tauri, native pg client, macos keychain, ssh tunnel, er diagrammer, cemini-pg-admin]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-deployment.md
maturity: draft
created: 2026-05-12
updated: 2026-05-17
gemini_eval_doc1_url: 16
phase_0_verdict: CONDITIONAL-GO 2026-05-17 (workflow-laptop; MIT verified, SBOM clean, but young repo + low bus-factor)
adoption_status: PHASE-0-COMPLETE 2026-05-17
---

## Relations

- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — source eval (URL 16)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — corrected multi-wiki prompt
- `@concepts/cemini-deployment.md` — Cemini PostgreSQL deployment context

## Raw Concept

- **Repo**: `github.com/abeni16/veloxdb`
- **License** [per Gemini eval]: MIT
- **Tier**: Adopt
- **Primary fit**: Workflow (Cemini PostgreSQL admin)

## Narrative

Native Tauri + Rust PostgreSQL client for macOS. Features: macOS Keychain credential storage, SSH-tunnel support (for hetzner-hosted Cemini PG), built-in ER diagrammer. Replaces pgAdmin / DataGrip-class tools for daily Cemini DB admin.

### Integration vector

Laptop-side install. Phase-0: verify macOS Keychain integration handles SSH-tunnel-protected hetzner targets cleanly, confirm ER diagrammer captures Cemini's full schema (LangGraph agent state tables + market data + strategy state).

## Phase-0 Audit (2026-05-17)

**Repo**: `github.com/abeni16/veloxdb` — cloned shallow to `/tmp/ph0-veloxdb/`. Tauri 2 + Rust backend (`src-tauri/`), Vite/TS frontend. Note: despite the wiki title saying "PostgreSQL client", the Rust deps also pull `sqlx` with `mysql`+`sqlite` features — it is a multi-DB client, PostgreSQL-primary.

### License — claim vs actual
- Gemini eval claimed **MIT**. **CONFIRMED**: `LICENSE` is verbatim MIT (`Copyright (c) 2026 Abenezer`); GitHub `licenseInfo.key = mit`. SPDX: `MIT`. PASS.

### Maturity — observed
| Metric | Value |
|--------|-------|
| Stars | 323 |
| Forks | 20 |
| Open issues | 4 |
| Created | 2026-03-17 (~2 months old) |
| Last push | 2026-05-14 (3 days before audit) |
| Contributors | 5 total |

Young repo, modest traction. Active but small. Note: repo ships a stray `rustup-init.exe` binary at root — minor housekeeping smell, not a blocker.

### Failure-mode probe — Rust dependency SBOM (`cargo license`)
- `Cargo.lock` resolves **667 crates**. Full license scan via `cargo-license`:
  - **Apache-2.0 OR MIT: 391 crates** — permissive, no concern.
  - **MIT: 160 crates** — permissive, no concern.
  - **MPL-2.0: 9 crates** — `cssparser` (×2), `cssparser-macros`, `dtoa-short`, `option-ext`, `resvg`, `selectors` (×2), `usvg`. All pulled in transitively (SVG icon rendering via `resvg`/`usvg`, CSS parsing).
  - Remaining crates split across the usual permissive set (BSD/ISC/Unicode/Zlib).
- **No GPL, no LGPL, no AGPL anywhere in the tree.** `grep` for gpl/copyleft crate names returned none.
- **MPL-2.0 assessment**: MPL-2.0 is *file-level weak copyleft* — it obliges sharing modifications to the MPL-licensed files themselves, but explicitly does NOT infect the larger work that merely links/consumes them. Since Cemini would use veloxdb as an unmodified binary (and would not patch `resvg`/`cssparser` source), MPL-2.0 imposes **zero practical obligation**. SBOM is **clean for our use**.

### Bus-factor (secondary observation)
Contribution distribution: `abeni16` 105 commits, then MowlCoder 3, Abzaek/amikingo 2 each, pranavmishra90 1. Truck factor **~1** — single-dev project, like voicemode. Tolerable for the same reason: laptop-side non-serving tool, MIT fork escape hatch.

### Comparison vs existing Cemini coverage
No existing PG-admin GUI tool in the OSINT wiki. veloxdb would replace pgAdmin/DataGrip-class tools for Cemini DB admin — fills a real gap, no parallel implementation.

### Decision — CONDITIONAL-GO
License MIT verified; Rust SBOM clean (no GPL/AGPL; the 9 MPL-2.0 crates are weak file-level copyleft that does not infect a consuming app). Two soft concerns hold this short of unqualified GO: (1) very young repo (~2 months, 323★) and (2) single-dev bus-factor (~1). Neither is fatal for a laptop-side non-serving tool with an MIT fork path. **CONDITIONAL-GO**: proceed to install for evaluation, but before relying on it for daily Cemini DB admin, validate the two original Phase-0 open questions — Keychain credential storage over SSH-tunneled Hetzner targets, and ER-diagrammer fidelity against Cemini's full schema. Do not treat it as a load-bearing tool until those pass.
