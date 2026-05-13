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
updated: 2026-05-12
gemini_eval_doc1_url: 16
phase_0_verdict: ADOPT-CANDIDATE 2026-05-12 (workflow-laptop, Cemini PostgreSQL admin)
adoption_status: PRE-PHASE-0 2026-05-12
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
