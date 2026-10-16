---
title: Cap — open-source screen recorder
type: entity
tags: [tools, screen-recording, video, k292]
keywords: [cap, screen-recorder, tauri, whisper, parakeet, byo-s3, agpl]
related:
  - sources/eval-url-multi-wiki-repository-2026-10-16.md
maturity: draft
created: 2026-10-16
updated: 2026-10-16
wire_status: extract_only
---

## Relations

- @sources/eval-url-multi-wiki-repository-2026-10-16.md

## Raw Concept

**What prompted this page:** K292 tool eval (2026-10-16). Phase-0 licence read via `gh api`; shallow-cloned to `.local/adopts/k292/` as REFERENCE. **No install. 0 Integrate GO.**

## Narrative

An **open-source screen recorder** (Rust/Tauri) with **local Whisper/Parakeet captioning** and **bring-your-own-S3** storage.

**Licence:** **AGPL-3.0** on the main tree, with **MIT** parts (`cap-camera`, `scap`) — `gh api` reports **NOASSERTION** because GitHub cannot express the split. The docx's AGPL claim is correct, and a **commercial desktop licence** is required separately. **Isolate; never vendor.**

**Docx tier: Extract.** **Clone dropped in the 2026-10-16 prune.** It was the largest clone (324 MB) and the batch was 50% over a 500 MB budget. It is the one to lose: biggest, most licence-encumbered (AGPL-3.0 plus a separate commercial desktop licence), and its proposed use is promotional media rather than engineering. **No working copy is held**; `scripts/adopt_k292_phase0.sh` no longer clones it by default. Re-clone from `github.com/CapSoftware/Cap` if that changes.

**Proposed uses:** **PII-safe Atto walkthroughs and Basgiath clips**. The local captioning is the point — the recording never needs to leave the machine, which fits the workspace's local-first posture. **The AGPL main tree and the separate commercial licence are the constraints to check before any product use.**
