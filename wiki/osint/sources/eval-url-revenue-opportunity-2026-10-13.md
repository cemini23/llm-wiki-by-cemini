---
title: "Tool eval 2026-10-13 — Repository Revenue Opportunity Analysis (20 URLs)"
type: source
tags: [source, k290, tool-eval, phase-0, licensing, dev-tooling]
keywords: [eval, phase-0, license-verification, context-mode, vercel-skills, openmed, xxhash, cc-switch-cli, club-3090, takumi, anatomy, digup, k290]
related:
  - concepts/k290-eval-wave.md
  - concepts/tool-evaluation-framework.md
  - entities/tools/cc-switch-cli.md
  - entities/tools/context-mode.md
  - entities/tools/openmed.md
  - entities/tools/takumi.md
  - entities/tools/vercel-skills.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
read_status: read
---

## Relations

- @concepts/k290-eval-wave.md
- @concepts/tool-evaluation-framework.md
- @entities/tools/cc-switch-cli.md
- @entities/tools/context-mode.md
- @entities/tools/openmed.md
- @entities/tools/takumi.md
- @entities/tools/vercel-skills.md

## Raw Concept

| Title | Repository Revenue Opportunity Analysis |
| Type | .docx eval batch — 20 URLs, batch theme "Developer Agent Tooling, Local Inference Engines, High-Performance Systems, and Media Generation Stack" |
| Author | operator (auto-generated eval pass) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Repository Revenue Opportunity Analysis.docx` |
| Retrieved | 2026-10-13 |
| sha256 | `394e5e3c4c9692f3…` |
| Primary lens | revenue + project fit — #1 Atto · #2 GuruWatcher + Basgiath · #3 CeminiDFS · #4 CeminiParlays (poker + TipDrop retired) |
| read-status | read |

## Narrative

20 URLs, all verified to exist and be active. **License claims in the docx are wrong or misleading on 5 of 20** — re-verify every Adopt with `gh api` before tiering (workspace rule; the eval's own SPDX text is not trustworthy). **Star counts in the docx are unreliable and often roughly 2× off.**

**License discrepancies found (docx claim → actual):**

| Repo | Docx claim | Actual | Impact |
|------|-----------|--------|--------|
| `krishhgg/Insomnia` | NOT FOUND | MIT | none (permissive) |
| `momo5502/sogen` | NOT FOUND | **GPL-2.0** | **material** — copyleft |
| `noonghunna/club-3090` | AGPL-3.0 | **Apache-2.0** | **material, favourable** — docx over-tightened |
| `storytold/wordcraft` | Apache-2.0 | MIT OR Apache-2.0 | minor |
| `ja7ad/hydra` | GPL-3.0-or-later / MIT | GPL-3.0 + Apache-2.0 + MIT | minor |

**Docx aggregate tiers (its own count):** Integrate 6 · Extract 3 · Watch 1 · Context 8 · Pass 2 · UNAVAILABLE 0.

| Tier | Entries |
|------|---------|
| **Integrate (6)** | `vercel-labs/skills` (MIT), `Cyan4973/xxHash` (BSD-2-Clause), `SaladDay/cc-switch-cli` (MIT), `noonghunna/club-3090` (Apache-2.0 ✓), `kane50613/takumi` (MIT OR Apache-2.0), `wheresryan22/anatomy` (MIT) |
| **Extract (3)** | `mksglu/context-mode` (ELv2 — patterns only), `maziyarpanahi/openmed` (Apache-2.0), `ARahim3/DigUp` (MIT) |
| **Watch (1)** | `baidu/Unlimited-OCR` (HuggingFace model card) |
| **Context (8)** | artcraft, VoiceStudio, xtool, Motrix, dx-ball, sogen, hydra, Insomnia |
| **Pass (2)** | `akshaydeo/strip` (3★, no license), `storytold/wordcraft` |

**Tier-vs-license contradiction, resolved.** The docx tiers **`club-3090` as Integrate** while its own notes warn **"AGPL-3.0 copyleft … restrict usage strictly to internal inference backends."** The live repo shows **Apache-2.0**, so the docx **over-tightened on a wrong SPDX read** — Integrate is defensible, but only after `gh api` confirms. `context-mode` (ELv2) is Extract by design, which is consistent.

### The 20 entries

| # | Repo | What it does | Docx license | Verified | Revenue lens (docx) |
|---|------|--------------|--------------|----------|---------------------|
| 1 | `storytold/artcraft` | open 2D/3D "intentional crafting engine" routing across 62 generative models | MIT OR Apache-2.0 | ✓ | Basgiath promo media + Atto landing graphics (low, 90d) |
| 2 | `debpalash/VoiceStudio` | local voice cloning / TTS / dubbing | AGPL-3.0 | ✓ | Basgiath NPC dialogue (speculative) |
| 3 | `mksglu/context-mode` | sandboxes tool output (**~98% context reduction**), SQLite FTS5 session memory, MCP | ELv2 | ✓ | cut token + engineering cost across Atto / CeminiDFS / CeminiParlays (high, now) |
| 4 | `vercel-labs/skills` | `npx skills` CLI to install/symlink/update SKILL.md across Cursor / Claude Code / Codex | MIT | ✓ | standardize agent procedures (high, now) |
| 5 | `xtool-org/xtool` | cross-platform Xcode replacement (SwiftPM build/sign/deploy) | MIT | ✓ | none; speculative |
| 6 | `agalwood/Motrix` | aria2 download manager + headless server + CLI + QuickJS plugins | MIT | ✓ | dataset acquisition time (low, 90d) |
| 7 | `N0zoM1z0/dx-ball` | agentic decompilation showcase (Ghidra + REA MCP), DX-Ball byte-exact | MIT (recon source; assets excluded) | ✓ | none; speculative |
| 8 | `maziyarpanahi/openmed` | local clinical NER + HIPAA-grade PII de-identification (MLX/CoreML) | Apache-2.0 | ✓ | protect Atto kit privacy; stop living-person PII leaks (high, 30d) |
| 9 | `Cyan4973/xxHash` | non-cryptographic hash | BSD-2-Clause (lib) / GPL-2.0 (xxhsum) | ✓ | cut CeminiDFS lineup-sim + Atto dedup CPU (high, now) |
| 10 | `SaladDay/cc-switch-cli` | TUI/CLI manager for Claude Code / Codex / Gemini / OpenCode + MCP + SQLite provider config | MIT | ✓ | operator time (high, now) |
| 11 | `momo5502/sogen` | Windows/Linux userspace binary emulator | NOT FOUND | **GPL-2.0** | none; speculative |
| 12 | `akshaydeo/strip` | Go utility stripping function calls from builds | NOT FOUND | no license file | negligible; speculative — **3 stars, duplicates sed/awk/tr** |
| 13 | `noonghunna/club-3090` | Docker Compose LLM-serving recipes (vLLM/SGLang/llama.cpp) for RTX 3090/4090 | AGPL-3.0 | **Apache-2.0** | eliminate cloud LLM API cost (high, now) |
| 14 | `ja7ad/hydra` | multi-source download engine (range stealing, mirror failover) | GPL-3.0-or-later / MIT dual | GPL-3.0 + 2 others | minor OSINT-dump savings (low, 90d) |
| 15 | `kane50613/takumi` | render JSX/HTML/CSS to OG images + paged PDF in pure Rust (**no headless Chrome**) | MIT OR Apache-2.0 | ✓ | faster Atto client PDF binders (high, now) |
| 16 | `ARahim3/DigUp` | on-device macOS file search (EmbeddingGemma 2 + Apple Vision OCR + SQLite) | MIT | ✓ | Atto Concierge research hours (medium, 30d) |
| 17 | `baidu/Unlimited-OCR` | long-document OCR with flat KV cache (R-SWA) — **HuggingFace model card, not a repo** | Apache-2.0 / Open Weights | not re-verified | transcribe gazettes/registers (low, 90d) — blocked by Atto ban on unverified handwriting transcription |
| 18 | `wheresryan22/anatomy` | agent skill generating isometric SVG/WebGL system diagrams from prompts | MIT | ✓ | Atto landing-page conversion (high, now) |
| 19 | `storytold/wordcraft` | clean-room Microsoft Word reimplementation in pure Rust | Apache-2.0 | MIT OR Apache-2.0 | none; speculative (docx said 443 stars; actual **10.7k**) |
| 20 | `krishhgg/Insomnia` | macOS menu-bar utility preventing sleep during agent sessions | NOT FOUND | MIT | minor reliability (low, now) |

**Overlaps with existing pages:** `@entities/tools/cc-switch-cli.md` (entry 10 — already in the wiki), `@entities/tools/voxcpm.md` / `@entities/tools/omnivoice.md` (entry 2 voice), `@entities/tools/llmvault.md` (entry 8 privacy), `@entities/tools/mineru.md` / `@entities/tools/unlimited-ocr.md` (entry 17), `@entities/tools/t3code.md` (UI surfaces).

### Cross-wiki routing
- **Cyber:** `N0zoM1z0/dx-ball`, `momo5502/sogen` — dual-use reverse engineering. Reference only; **authorized lab; no PoC**.
- **CCC:** `vercel-labs/skills`, `mksglu/context-mode`, `SaladDay/cc-switch-cli`.
- **Image-gen / Basgiath:** `storytold/artcraft`, `debpalash/VoiceStudio`, `wheresryan22/anatomy`.

### Phase-0 status — RUN 2026-10-13
`bash scripts/adopt_k290_phase0.sh` ran in the Terminal panel. **`gh api` confirmed every licence against the live repo, and all 9 Integrate/Extract candidates were shallow-cloned** to `.local/adopts/k290/` — **411 MB of a 500 MB budget**. No clone failed.

**The docx licence errors are confirmed:**

| Repo | Docx said | `gh api` says |
|------|-----------|---------------|
| `noonghunna/club-3090` | AGPL-3.0 | **Apache-2.0** |
| `momo5502/sogen` | NOT FOUND | **GPL-2.0** |
| `krishhgg/Insomnia` | NOT FOUND | MIT |

**Two rows return `NOASSERTION`, and neither is a red flag.** `xxHash` carries a dual **BSD-2-Clause + GPL-2.0** split that GitHub's detector cannot express — the docx's split claim is substantively right. `context-mode` runs the **Elastic Licence 2.0**, which is not a licence GitHub recognises; that is the same reason it stays **Extract only**. `takumi` resolves to **Apache-2.0** from its dual, as expected.

**What this does and does not change.** Licence verification no longer blocks the six Integrate candidates, and `club-3090`'s copyleft caution is void — the repo is permissive. But **the workspace still holds 0 Integrate GO**: the clones are REFERENCE data under gitignored `.local/`, and adopting any of them into a product still needs its own brief.

## Snippets

> Batch theme: Developer Agent Tooling, Local Inference Engines, High-Performance Systems, and Media Generation Stack. [Source: Repository Revenue Opportunity Analysis.docx — header]

> Integrate 6, Extract 3, Watch 1, Context 8, Pass 2, UNAVAILABLE 0. [Source: Repository Revenue Opportunity Analysis.docx — aggregate summary]
