---
title: destructive_command_guard (dcg)
type: entity
tags: [tool, agent-safety, rust, k163, conditional-go]
keywords: [dcg, shell hook, SIMD, fail-open, MIT rider]
related:
  - sources/eval-github-repo-revenue-evaluation-2026-07-14.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-14
updated: 2026-07-14
---

## Relations

- @sources/eval-github-repo-revenue-evaluation-2026-07-14.md — K163 Integrate → CONDITIONAL

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) |
| **License** | MIT **with OpenAI/Anthropic rider** (GitHub SPDX **NOASSERTION**; ~4.1k★) |
| **Verdict** | **CONDITIONAL-GO** — local Cursor/user shell pre-exec guard OK; do not redistribute into OpenAI/Anthropic products |
| **Routing** | CCC + cybersec briefs; optional local binary adopt (<500MB) |

Rust SIMD-accelerated pre-execution firewall for agent-spawned shell (`rm -rf`, destructive git, etc.). **Fail-open** if AST parse times out — not a sole control plane. Rider forbids granting rights to OpenAI/Anthropic and affiliates; personal operator use to *constrain* agents is the intended class, but legal review if embedding inside vendor CLIs for redistribution.

### Phase-0

- License rider verified from LICENSE file (not plain MIT).
- Maturity: active, 4k★.
- Failure mode: fail-open + rider ambiguity → keep as defense-in-depth, not sole gate.

### Local adopt attempt (2026-07-14)

- `cargo install --git … destructive_command_guard` **FAILED** on stable rustc (`fsqlite-pager` needs nightly `core_intrinsics`).
- Source cloned to `.local/adopts/destructive_command_guard/` for reference; binary not on PATH.
- Hallmark + maths-compendium + codex-first-customer clones OK (<10MB total adopts).
