---
title: "voicemode — Whisper.cpp + Kokoro voice MCP for Claude Code (Adopt, workflow)"
type: entity
tags: [tool, voice, mcp, whisper, kokoro, claude-code, m-series-mac, gemini-eval-doc1, phase-0-adopt-candidate]
keywords: [voicemode, voice mode, mbailey, whisper.cpp, kokoro tts, core ml, m-series, mcp-native, bidirectional voice]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - "@image-gen-wiki/entities/persona-ops/voicemode.md"
maturity: draft
created: 2026-05-12
updated: 2026-05-17
gemini_eval_doc1_url: 19
phase_0_verdict: GO 2026-05-17 (workflow-laptop, M-series Mac fit; MIT verified, bus-factor acceptable)
adoption_status: PHASE-0-COMPLETE 2026-05-17
---

## Relations

- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — source eval (URL 19)
- `@sources/multi-wiki-gemini-eval-prompt-2026-05-12.md` — corrected multi-wiki prompt
- `@image-gen-wiki/entities/persona-ops/voicemode.md` — cross-routed for persona-ops voice angle

## Raw Concept

- **Repo**: `github.com/mbailey/voicemode`
- **License** [per Gemini eval]: MIT
- **Tier**: Adopt
- **Primary fit**: Workflow (laptop-side Claude Code)
- **Cross-route**: image-gen wiki (persona-voice ops on M-series Mac)

## Narrative

Bidirectional voice MCP server for Claude Code: Whisper.cpp (STT) + Kokoro (TTS), Core ML accelerated on M-series Mac. Replaces cloud-API voice loops with fully local stack — privacy-preserving, no per-token cost, no network dependency.

### Integration vector

Direct workflow adopt for laptop-side Claude Code sessions. Phase-0 audit: license verification, M-series Core ML model size + RAM footprint, MCP wiring against existing skill stack. Cross-route stub to image-gen wiki for persona-voice angle.

### Open questions

- Latency: STT round-trip on M-series for 30-second clip
- Kokoro voice quality + voice-set variety for persona-ops use

## Phase-0 Audit (2026-05-17)

**Repo**: `github.com/mbailey/voicemode` — cloned shallow to `/tmp/ph0-voicemode/`.

### License — claim vs actual
- Gemini eval claimed **MIT**. **CONFIRMED**: `LICENSE` is verbatim MIT (`Copyright (c) 2026 Mike Bailey`); GitHub `licenseInfo.key = mit`. SPDX: `MIT`. No copyleft. PASS.

### Maturity — observed
| Metric | Value |
|--------|-------|
| Stars | 1,182 |
| Forks | 164 |
| Open issues | 28 |
| Created | 2025-06-08 (~11 months old) |
| Last push | 2026-05-17 (same-day — actively developed) |
| Contributors | 11 total |

Healthy for a Claude Code voice tool. Active `[Unreleased]` changelog with recent VM-numbered work items (issue-tracker discipline). Semantic-versioned, Keep-a-Changelog format.

### Failure-mode probe — single-dev bus-factor
- Contribution distribution: **mbailey 1,480 commits, ai-cora 331, dependabot 10, then a long tail of 1-3 commits each** (licht1stein 3, ai-tesi 2, 7 others with 1).
- Truck factor effectively **1-2**: `mbailey` is the clear principal; `ai-cora` is a secondary substantial contributor (likely an AI-assisted persona/account given the name pattern alongside `ai-tesi`). Real independent human bus-factor is **~1**.
- **Mitigant**: this is a *laptop-side workflow tool*, not a serving-path dependency. Per CLAUDE.md deployment boundary, voicemode never sits in the kb-server / prod path — abandonment would only pause a convenience workflow, not break any 24/7 system. MIT license means a fork is always possible. Bus-factor risk is therefore **tolerable for this tool class**.

### Comparison vs existing Cemini coverage
No existing local voice-I/O tooling in the OSINT wiki. Cross-routed stub exists at `@image-gen-wiki/entities/persona-ops/voicemode.md` for the persona-voice angle — non-overlapping use case. No parallel implementation to displace.

### Decision — GO
MIT verified, maturity solid (1.2k★, same-day commits), and the single-dev bus-factor is acceptable because voicemode is a non-serving laptop convenience tool with a clean MIT fork escape hatch. Proceed to install + measure the open questions (M-series STT latency, Kokoro voice quality). Verdict: **GO** (workflow-laptop).
