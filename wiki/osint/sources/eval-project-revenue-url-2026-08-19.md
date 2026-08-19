---
title: "Eval — Project Revenue URL 2026-08-19 (20-URL, K242)"
type: source
tags: [eval, phase-0, k242, atto, cyber, ccc]
keywords: [aliens-eye, betterwright, rybbit, deepteam, qwen-uncensored, privfu]
related:
  - entities/tools/aliens-eye.md
  - entities/tools/betterwright.md
  - entities/tools/watermarks-remover.md
  - entities/tools/deepteam.md
  - sources/eval-local-agent-infra-2026-08-19.md
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/atto-genealogy-agent-kit.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/agent-harness-verification-bottleneck.md
maturity: draft
created: 2026-08-19
updated: 2026-08-19
read_status: read
---

## Relations

- @entities/tools/aliens-eye.md — MIT Extract username OSINT
- @entities/tools/betterwright.md — MIT Extract Playwright wrappers
- @entities/tools/watermarks-remover.md — MIT Extract; Image-gen skip local wire
- @entities/tools/deepteam.md — Apache-2.0 Extract REFERENCE (skip clone; vendor-pull Watch)
- @sources/eval-local-agent-infra-2026-08-19.md — same-day K242 Untitled eval
- @concepts/cemini-license-posture.md — never trust eval SPDX
- @concepts/wiki-tooling-evaluation.md
- @concepts/atto-genealogy-agent-kit.md
- @concepts/local-abliterated-llm-pentest-stack.md — Qwen uncensored Watch, no weights
- @concepts/agent-harness-verification-bottleneck.md — Dual-ID: this ingest is **OSINT K242**, not Trajectory Sentinel K242

## Raw Concept

| Field | Value |
|-------|--------|
| File | `Project Revenue URL Evaluation.docx` |
| sha256 | `5121154f0472bbe5334fef617f1886a4aa2929d2f8643d70c55c2e8a37c10e81` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Project Revenue URL Evaluation.docx` |
| retrieved | 2026-08-19 |
| URLs evaluated | 20 |
| Theme | Genealogy kits, local abliterated inference, verification, privacy telemetry, UI |
| License report | `.local/reports/license-k242-2026-08-19.md` |
| Dual-ID | **OSINT K242** = this inbox (19 Aug 2026). Do not collapse onto Trajectory Sentinel K242. |

## Narrative

20-URL multi-wiki revenue evaluation. **Docx license claims were never trusted.** **0 new runtime Integrate GO** after `gh api` SPDX. Docx Integrate on Qwen uncensored MLX, rybbit (AGPL), and aceternity commercial UI is overridden.

### Verdict aggregate (license-corrected)

| Tier | Count | URLs |
|------|-------|------|
| Integrate (new GO) | **0** | Qwen / rybbit / aceternity Integrate overridden |
| Extract clone | 3 | **Aliens_eye** MIT; **betterwright** MIT; **watermarks-remover** MIT |
| Extract REFERENCE skip-clone | 1 | **deepteam** Apache-2.0 (existing entity) |
| Watch no-clone | 5 | Qwen uncensored MLX (no HF weights); rybbit AGPL ~410MB; App-Store-Connect MIT; box.ascii.dev commercial; autonomous-computer SIZE-SKIP ~350MB; KrillinAI GPL |
| Context no-clone | 6 | headway (tile disk); Mojo; contentarchitecture; PrivFu PoC; QUIC C2 article; gist |
| Context listed-only (offensive) | 1 | pwneye camera-hack (docx Pass too soft) |
| Pass | 3 | PureMac MIT; amicro; aceternity commercial UI |

### License re-verification (gh api)

| Repo / URL | Docx claim | gh SPDX | Action |
|------------|-----------|---------|--------|
| arxhr007/Aliens_eye | NOT FOUND / Extract | **MIT** | **CLONE Extract** (~1.3MB) |
| BetterWright/betterwright | NOT FOUND / Extract | **MIT** | **CLONE Extract** (~17MB) |
| guillaumemeyer/watermarks-remover | NOT FOUND / Extract | **MIT** | **CLONE Extract** (~1.8MB) |
| confident-ai/deepteam | Apache / Extract | **Apache-2.0** | Skip clone; bump entity |
| rybbit-io/rybbit | AGPL / **Integrate** | **AGPL-3.0** | **Watch, no clone**. Do not vendor into Atto |
| orcarouter/Qwen3.8-27B-Uncensored-MLX | OSS / **Integrate** | weights | **Watch, no download** |
| daem0nc0re/PrivFu | Context | BSD-3 (K241) | Context-no-clone PoC |
| krillinai/KrillinAI | Watch | **GPL-3.0** | Watch, no clone |
| ui.aceternity.com | **Integrate** | commercial | **Context**. Skip Image-gen local wire |

[Source: `.local/reports/license-k242-2026-08-19.md`]
