---
title: codex-startup-pressure-test-skill — Pressure-Test/MVP-Plan Prompt Patterns (MIT)
type: entity
tags: [tool, prompt-engineering, mit-license, steal-from-tier, abandoned-project, codex-skill]
keywords: [pressure-test, problem-validation, competition-map, mvp-plan, codex-skill, prompt-pattern-library, kappaemme-git]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - entities/tools/research-paper-writing-skills.md
  - entities/tools/academic-paper-skills.md
  - entities/tools/obsidian-llm-wiki-local.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 3, **STEAL-FROM** tier
- @concepts/cemini-license-posture.md — MIT-licensed, IP-clean
- @entities/tools/research-paper-writing-skills.md — sister STEAL-FROM in same K32 batch (academic paper editing prompts)
- @entities/tools/academic-paper-skills.md — sister STEAL-FROM in same K32 batch (35-point peer-review framework)
- @entities/tools/obsidian-llm-wiki-local.md — sister STEAL-FROM in same K32 batch (wiki maintenance code)

## Raw Concept

Kappaemme-git/codex-startup-pressure-test-skill is a specialized skill extension for the Codex CLI that pressure-tests startup concepts and infrastructure architectures via structured LLM prompts. Diagnostic modes: `pressure-test`, `problem-validation`, `competition-map`, `mvp-plan`. Outputs formatted markdown scorecards.

K32 DR verdict: **STEAL-FROM**. Don't install the JavaScript package (it's hardcoded for `.codex/skills/` directory structure, ecosystem-locked). Extract the underlying reasoning prompts and port them into Claude Code system-prompt templates.

## Narrative

- **URL**: `https://github.com/Kappaemme-git/codex-startup-pressure-test-skill` ✓ DR-cited
- **License**: MIT — clean, IP-sale safe
- **Stack**: JavaScript (npm package, hardcoded for Codex CLI's `.codex/skills/` layout)
- **Maturity**: 2 commits, 0 releases — **abandoned project status** per DR. Treat as static prompt artifact, not maintained software

### Four reasoning modes worth porting

DR identified four diagnostic prompt patterns embedded in the source:

| Mode | What it does | Cemini use case |
|------|--------------|-----------------|
| `pressure-test` | Identify fatal flaws in a proposed concept | New strategy idea cross-examination before brief drafting |
| `problem-validation` | Validate that the problem being solved is real | Pre-implementation sanity check on quant strategies |
| `competition-map` | Map competitive switching costs and moats | Competitive analysis for any new tool/library adoption |
| `mvp-plan` | Propose 2-week MVP plans for pressure-tested concepts | Time-bounded scoping for new Cemini features |

The first two are particularly aligned with the existing Phase-0 audit pattern (per `CLAUDE.md`): pressure-test catches "does this credible-looking tool actually fit our use case?" and problem-validation catches "is the problem we'd solve real?".

### Why STEAL-FROM not ADOPT

DR direct framing:

> "Do not execute the npm installation or integrate the JavaScript package into any environment. Instead, surgically extract the underlying reasoning modes (e.g., competition-map, mvp-plan, pressure-test) from the source code and translate these analytical frameworks into system prompt templates."

The JS package is hardcoded for Codex CLI's `.codex/skills/` directory structure — useless outside that environment. The **prompt content** is portable.

### Action plan

1. Phase 1: clone `github.com/Kappaemme-git/codex-startup-pressure-test-skill` to `/tmp/codex-pressure-test-audit/`
2. Phase 2: extract the four mode prompts (likely YAML or JS-string-literal source)
3. Phase 3: create `prompt-patterns/` directory at workspace root (or `.claude/skills/` if Claude Code skill-style is more appropriate)
4. Phase 4: install as Claude Code system-prompt templates with quant-finance domain re-styling

Estimated effort: 1-2 hours total. Low-priority but high-leverage.

### Risks (per DR)

> "The project exhibits clear signs of abandonment; with a total history of only 2 commits and 0 official releases, it is effectively a static proof-of-concept rather than maintained software. Furthermore, the tool's runtime is hardcoded to expect the .codex/skills/ directory structure, resulting in ecosystem lock-in that makes the executable portion useless outside of that specific, narrow CLI tool environment."

### Open questions

- ⚠ Exact instructional prompt texts — DR notes these were not visible in the evaluated surface context; manual repo inspection required
- ⚠ Are the prompts opinionated about specific stack assumptions (e.g., SaaS startup vs developer tool vs financial trading)? Re-styling cost depends on this

### Adoption status — STEAL-FROM, NOT INSTALLED

Phase-1 audit pending. No npm package installed.

## Snippets

### Operational scope

> "This repository contains a specialized skill extension designed specifically for the Codex CLI environment, structured to evaluate and pressure-test startup concepts and infrastructure architectures. It operates through various diagnostic modes, including pressure-test, problem-validation, competition-map, and mvp-plan. The tool consumes a user-provided text description of a business or technical concept and instructs an LLM to identify fatal flaws, map competitive switching costs, and propose concrete two-week Minimum Viable Product (MVP) plans, outputting the analysis as formatted markdown scorecards and verdicts." [Source: 5_6 links.docx URL 3]

### Why steal-from not adopt

> "Steal-from. Do not execute the npm installation or integrate the JavaScript package into any environment. Instead, surgically extract the underlying reasoning modes (e.g., competition-map, mvp-plan, pressure-test) from the source code and translate these analytical frameworks into system prompt templates." [Source: 5_6 links.docx URL 3]
