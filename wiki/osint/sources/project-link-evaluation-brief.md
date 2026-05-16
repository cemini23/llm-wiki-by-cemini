---
title: "Project Link Evaluation Brief — 13-Tool Architecture & Compliance Audit"
type: source
tags: [tool-evaluation, architecture, licensing, workflow, cemini-stack]
keywords: [DeerFlow, DFlash, HTML-effectiveness, Anthropic Financial Services, Gemma, AlphaFold3, MuJoCo, Optax, ARIS, OpenHuman, Google Code Wiki]
related:
  - concepts/tool-evaluation-framework.md
  - entities/tools/deerflow.md
  - entities/tools/html-effectiveness-pattern.md
  - entities/tools/anthropics-financial-services.md
  - entities/tools/auto-claude-code-research-in-sleep.md
  - entities/tools/google-code-wiki.md
maturity: validated
read_status: deep-read
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@entities/tools/deerflow.md` — Steal-from: orchestration patterns for local agent sandbox
- `@entities/tools/html-effectiveness-pattern.md` — Steal-from: LLM-generates-HTML instead of Markdown
- `@entities/tools/anthropics-financial-services.md` — Steal-from: MCP schemas + prompt structures
- `@entities/tools/auto-claude-code-research-in-sleep.md` — Adopt: research automation skill framework
- `@entities/tools/google-code-wiki.md` — Defer: hosted code documentation, wait for local CLI
- `@concepts/tool-evaluation-framework.md` — three-surface evaluation methodology

## Raw Concept
- **Title**: Analysis and Evaluation of Technical Repositories for High-Performance Trading and Knowledge Infrastructures
- **Type**: Commissioned evaluation brief
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Project Link Evaluation Brief.docx`
- **Retrieved**: 2026-05-10
- **Format**: .docx, ~3.1MB, 348 paragraphs
- **Read status**: deep-read

## Narrative

Structured evaluation of 13 software repositories, platforms, and design patterns assessed against three Cemini deployment surfaces: (1) Cemini production stack (Hetzner, 7GB RAM, Docker Compose), (2) Wiki/librarian server (CPX21, 4GB RAM), (3) Solo-developer macOS laptop workflow.

Each tool scored on: concrete integration vector, RAM/disk/compute footprint, license compatibility against IP-sale-readiness requirements, and architectural fit.

### Summary verdicts

| Tier | Count | Tools |
|------|-------|-------|
| **Adopt** | 1 | ARIS (Auto-Research-In-Sleep) |
| **Steal-from** | 3 | DeerFlow, HTML-effectiveness pattern, Anthropic Financial Services |
| **Defer** | 1 | Google Code Wiki |
| **Reference-only** | 1 | Optax |
| **Reject** | 7 | DFlash, Gemma, AlphaFold3, MuJoCo Warp, Formal Conjectures, MuJoCo Playground, OpenHuman |

### Rejection patterns

- **Hardware incompatibility** (5): DFlash (GPU-only), Gemma (8-24GB VRAM), AlphaFold3 (GPU + Singularity containers), MuJoCo Warp (NVIDIA GPU), MuJoCo Playground (CUDA)
- **Domain mismatch** (2): Formal Conjectures (Lean 4 theorem proving), MuJoCo tools (robotics simulation)
- **License poison pill** (1): OpenHuman (GPL-3.0)
- **Note**: AlphaFold3 also rejected on non-commercial-use-only license terms

### Key adopt recommendation

**ARIS** (MIT license): Markdown-based research skill framework for Claude Code. Zero framework overhead, kilobytes not gigabytes. Installed via `git clone` into the Claude Code context directory. Enables structured ML research automation with /idea → /experiment → /paper workflow. See `@entities/tools/auto-claude-code-research-in-sleep.md`.

## Snippets

> "The localized research workflow on the laptop must extract and integrate [DeerFlow's] architectural patterns. Specifically, the strategy of organizing agent capabilities as isolated skill files and orchestrating them through a central message gateway." (URL 1, Steal-from rationale)

> "The explicit list of Python transitive dependencies pulled by the installation script to confirm the absolute absence of SSPL or PolyForm Noncommercial code logic." (URL 1, NEEDS VERIFICATION)

[Source: Project Link Evaluation Brief.docx]
