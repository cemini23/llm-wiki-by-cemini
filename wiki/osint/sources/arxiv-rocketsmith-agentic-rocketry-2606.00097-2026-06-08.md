---
title: "RocketSmith — agentic system for high-powered rocket design and manufacturing (arXiv 2606.00097)"
type: source
tags: [paper, arxiv, llm-agents, agent-harness, mcp, physical-domain, additive-manufacturing, k105]
keywords: [rocketsmith, 2606.00097, openrocket, build123d, prusa-slicer, claude-code, gemini-cli, subagents, skills, cadsmith, high-power-rocketry]
clusters: [llm-agents, infrastructure]
related:
  - entities/tools/rocketsmith.md
  - concepts/code-as-agent-harness.md
  - concepts/llm-agent-systems.md
  - sources/agentic-harness-engineering.md
  - sources/arxiv-cli-anything-2606-03854-2026-06-03.md
  - concepts/high-signal-paper-patterns.md
  - sources/arxiv-agents-all-the-way-down-2606.11869-2026-06-16.md
  - concepts/agents-all-the-way-down-methodology.md
maturity: validated
read_status: read
created: 2026-06-08
updated: 2026-06-16
---

## Relations

- @entities/tools/rocketsmith.md — shipped plugin (MIT) for Claude Code + Gemini CLI
- @concepts/code-as-agent-harness.md — concrete **physical-domain** instance of harness-interface + tool-orchestration pattern
- @concepts/llm-agent-systems.md — cluster hub
- @sources/agentic-harness-engineering.md — complementary: AHE evolves harnesses automatically; RocketSmith is a **hand-authored** domain harness with skills/subagents
- @sources/arxiv-cli-anything-2606-03854-2026-06-03.md — sibling pattern: wrap domain software as CLI/MCP for agent control

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | RocketSmith: An Agentic System for High-Powered Rocket Design and Manufacturing |
| **Authors** | Peter Pak, Jesse Barkley, Rumi Loghmani, Ananya Pamal, Derek Baich (TRA), Amir Barati Farimani† (CMU) |
| **Type** | arXiv preprint (35 pages) |
| **arXiv ID** | 2606.00097v2 |
| **Submitted** | 2 June 2026 |
| **License** | arXiv non-exclusive (paper); code [CONFIRMED 2026-06-08: MIT] — `gh api repos/ppak10/RocketSmith` |
| **Code** | https://github.com/ppak10/RocketSmith |
| **PDF location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.00097-rocketsmith-an-agentic-system-for-high-powered-r.pdf` |
| **Read status** | read (full paper; flight-test tables + discussion deep-read) |

## Narrative

### What it claims

RocketSmith is a **domain harness** (not a new base model) that automates Class-2 high-power rocketry design → simulation → parametric CAD → slicer weight estimation → FDM print → flight test. Released as a **plugin** for Claude Code and Gemini CLI using MCP-standard tool calls.

**Architecture (6 subagents):** `rocketsmith` (orchestrator), `openrocket`, `cadsmith`, `prusaslicer`, `manufacturing`, `gui`. **7 skills:** `motor-selection`, `stability-analysis`, `design-for-additive-manufacturing`, `generate-structures`, `modify-structures`, `mass-calibration`, `print-preparation`.

**Tool chain (source of truth → downstream):**

1. **OpenRocket** + `orhelper` Python bindings — component tree, stability (Barrowman CP/CG), flight simulation (apogee, velocity)
2. **build123d** — parametric STEP generation (chosen over generative-3D for deterministic edits + programmatic mass/volume verification)
3. **PrusaSlicer** — weight estimation from sliced toolpaths; manual slicing kept outside agent for schedule risk

**GUI:** read-only web dashboard mirroring CLI state (component tree, simulations, CAD); local server bridges terminal harness ↔ browser.

### Empirical results (flight tests, 3 May 2026)

Four rockets manufactured from agent-generated designs; all achieved **stable launch**. Two of four recovered **reflyable** (High Power 3, 4).

| Rocket | Motor | Sim apogee | Measured apogee | Recovery |
|--------|-------|------------|-----------------|----------|
| HP1 | H100W | 338.8 m | 276 m (80%) | Structural failure (delayed ejection) |
| HP2 | H219T | 334 m | N/A | Recovery bay failed to separate |
| HP3 | H219T | — | visual ~sim | Reflyable (tree recovery) |
| HP4 | J425R | 570.1 m | 479 m (84%) | Reflyable |

**Aggregate simulation accuracy:** 84% measured vs simulated apogee on instrumented flights [Source: arxiv-2606.00097…pdf p.21–26].

### Human-in-the-loop reality

Authors stress zero-shot is feasible but **human-in-the-loop** preferred: motor covers and retainers designed outside RocketSmith; manual PrusaSlicer profiles; post-print epoxy for ABS cracking; ejection-charge timing not fully agent-controlled. Friction between OpenRocket ↔ CAD ↔ slicer is the problem the harness reduces, not eliminates.

### Cemini relevance — REFERENCE (not Adopt)

| Signal | Implication |
|--------|-------------|
| Skills + subagents + MCP on Claude Code/Gemini CLI | Validates Cemini's harness-first posture (conductor, lazy-tool, skills) for **non-coding** domains |
| build123d closed-loop verify (mass/volume vs manifest) | Pattern steal for any parametric artifact with programmatic oracles (backtests, conviction.yaml lint, spread tiers) |
| Subagent context isolation | Same rationale as scatter-gather / specialist agents in trading stack |
| Physical flight test as oracle | Analogue: shadow soak + replay gates before prod deploy |

**Not Adopt:** rocketry domain; no prod trading surface. **Steal:** skill-trigger workflow, subagent scoping table, "source of truth → downstream tools" pipeline discipline.

## Snippets

> "This work introduces RocketSmith, an agentic system composed of subagents, skills, and tool calling abilities developed to the standard of the Model Context Protocol (MCP) and released as a plugin for agent harnesses." [Source: arxiv-2606.00097…pdf p.4]

> "Code-based formulation is adopted over generative-3D approaches … the script is deterministic and parametric: identical inputs yield identical geometry, and the LLM can target a specific feature for adjustment … without regenerating the entire shape." [Source: arxiv-2606.00097…pdf p.10]

> "A zero-shot approach is feasible with RocketSmith, however there are many additional considerations during development that promote a human-in-the-loop utilization of this agentic system." [Source: arxiv-2606.00097…pdf p.24]
