---
title: K290 Eval Wave — 20-URL tool eval, license drift, 6 Integrate candidates (Oct 2026)
type: source-hub
tags: [k290, tool-eval, phase-0, licensing, dev-tooling]
keywords: [k290, eval, gh-api, license-drift, context-mode, xxhash, club-3090, takumi, anatomy, digup, openmed]
related:
  - sources/eval-url-revenue-opportunity-2026-10-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/k289-feeds-wave.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
  - entities/tools/context-mode.md
  - entities/tools/openmed.md
  - entities/tools/takumi.md
  - entities/tools/vercel-skills.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-10-13.md
- @concepts/tool-evaluation-framework.md
- @concepts/k289-feeds-wave.md
- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md
- @entities/tools/context-mode.md
- @entities/tools/openmed.md
- @entities/tools/takumi.md
- @entities/tools/vercel-skills.md

## Raw Concept

**OSINT K290 eval batch, 2026-10-13.** One .docx, **20 URLs**, batch theme *Developer Agent Tooling, Local Inference Engines, High-Performance Systems, Media Generation Stack*. **Phase-0 not run in-session** — the Bash sandbox denies `api.github.com`. Run `bash scripts/adopt_k290_phase0.sh` in the **Terminal panel**.

## Narrative

### The headline is the license drift, again

**The docx's license claims are wrong or misleading on 5 of 20** — the third wave in a row with a materially wrong SPDX read.

| Repo | Docx said | Actual | Direction of error |
|------|-----------|--------|--------------------|
| `momo5502/sogen` | NOT FOUND | **GPL-2.0** | **under-stated copyleft** |
| `noonghunna/club-3090` | AGPL-3.0 | **Apache-2.0** | **over-stated copyleft** |
| `storytold/wordcraft` | Apache-2.0 | MIT OR Apache-2.0 | minor |
| `ja7ad/hydra` | GPL-3.0-or-later / MIT | GPL-3.0 + 2 others | minor |
| `krishhgg/Insomnia` | NOT FOUND | MIT | none (permissive) |

**Docx star counts are unreliable and often ~2× off** — `wordcraft` was listed at 443 stars against an actual **10.7k**; `vercel-labs/skills` at 16.2k against **34.3k**.

### The six Integrate candidates

| Repo | License | Claimed payoff |
|------|---------|----------------|
| `vercel-labs/skills` | MIT | `npx skills` — install/symlink/update SKILL.md across Cursor / Claude Code / Codex |
| `Cyan4973/xxHash` | BSD-2-Clause (lib) | cut hashing CPU in CeminiDFS lineup-sim and Atto dedup |
| `SaladDay/cc-switch-cli` | MIT | provider-config TUI for Claude Code / Codex / Gemini / OpenCode — **page already exists** |
| `noonghunna/club-3090` | **Apache-2.0** | local vLLM/SGLang serving recipes for 3090/4090 — docx claims ~$500/mo API saving |
| `kane50613/takumi` | MIT OR Apache-2.0 | JSX/HTML/CSS → OG image + paged PDF in pure Rust, **no headless Chrome** |
| `wheresryan22/anatomy` | MIT | isometric SVG/WebGL system diagrams from a prompt — Atto landing pages |

**Extract (3):** `context-mode` (ELv2 — sandboxes tool output, ~98% context reduction, SQLite FTS5 memory; **patterns only, no redistribution**), `openmed` (Apache-2.0, local PII de-identification), `DigUp` (MIT, on-device macOS file search).

### The one internal contradiction

The docx tiers **`club-3090` as Integrate** while its own notes warn about **AGPL copyleft**. The live repo is **Apache-2.0**, so the risk note was based on a wrong SPDX read. **Integrate holds — after `gh api` confirms.**

### Cross-wiki routing
- **Cyber:** `N0zoM1z0/dx-ball`, `momo5502/sogen` — reference only, **authorized lab, no PoC**.
- **CCC:** `vercel-labs/skills`, `context-mode`, `cc-switch-cli`.
- **Image-gen / Basgiath:** `artcraft`, `VoiceStudio`, `anatomy`.

## Snippets

> Integrate 6, Extract 3, Watch 1, Context 8, Pass 2, UNAVAILABLE 0. [Source: Repository Revenue Opportunity Analysis.docx]

> AGPL-3.0 copyleft on noonghunna/club-3090 … Restrict usage strictly to internal inference backends. [Source: Repository Revenue Opportunity Analysis.docx — implementation friction; license since verified Apache-2.0]
