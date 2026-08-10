---
title: Qwen-MM-Plugins — multimodal harness plugins (Integrate core → Atto)
type: entity
tags: [tool, k230, phase-0, atto, multimodal, apache]
keywords: [qwen-mm-plugins, vision, ocr, dashscope, mcp]
related:
  - sources/eval-github-repository-evaluation-plan-2026-08-10.md
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/active-project-research-routing.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/computational-genealogy-archival-automation.md
maturity: draft
created: 2026-08-10
updated: 2026-08-10
---

## Relations

- @sources/eval-github-repository-evaluation-plan-2026-08-10.md — K230 UNAVAILABLE→GO after live gh check
- @concepts/cemini-license-posture.md
- @concepts/wiki-tooling-evaluation.md
- @concepts/active-project-research-routing.md
- @concepts/gpuology-genealogy-agent-kit.md
- @concepts/computational-genealogy-archival-automation.md

## Raw Concept

K230 eval URL 20 was UNAVAILABLE (missing research context). Live probe 2026-08-10: repo exists, Apache-2.0. Phase-0 clone under OSINT `.local/adopts/Qwen-MM-Plugins` (~74MB shallow).

## Narrative

- **URL:** https://github.com/QwenLM/Qwen-MM-Plugins
- **License:** Apache-2.0 (LICENSE + gh SPDX)
- **Size / clone:** ~74MB shallow
- **Fit:** Atto vault screenshot/PDF assist; CCC optional
- **Verdict:** **GO Integrate `core` only** — not into `/route` skill

Skills + MCP that make a harness multimodal-native (vision / OCR / grounding / optional video). **Do not** wire into `route-task` / OpenRouter easy lane.

### Cemini constraints

1. Install **only** `qwen-mm-plugins-core` capability — skip blender/freecad/video-edit/edu-agent unless a dedicated brief.
2. **No** `curl | bash install.sh` — register skill/MCP via harness-native commands after supply-chain review (`agent-setup-supply-chain`, AgentBaiting).
3. Cloud OCR/vision (`DASHSCOPE_API_KEY`) = human-gated; **strip PII** before any vault blob leaves the laptop; Magika sniff first.
4. **Transkribus remains sole product HTR** — Qwen OCR is assistive read of screenshots/PDFs, not genealogy HTR replace.
5. Not a `/route` lane upgrade — optional executor capability when tasks cite images/PDFs.

[Source: https://github.com/QwenLM/Qwen-MM-Plugins (retrieved 2026-08-10)]
