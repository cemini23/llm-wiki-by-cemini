---
title: sentrux/sentrux — Real-time AST Architectural Sensor (Rust, MIT)
type: source
tags: [llm-tooling, code-quality, ast, tree-sitter, mcp, rust, claude-code, workflow-adopt, ip-sale-clean]
keywords: [sentrux, tree-sitter, ast-analysis, code-quality-score, mcp-server, hard-quality-gate, modularity, acyclicity, depth, equality, redundancy, architectural-boundary, claude-plugin, langgraph-refactoring]
related:
  - sources/gemini-dr-link-eval-2026-04-28.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/ip-sale-readiness.md
  - entities/frameworks/langgraph.md
  - entities/frameworks/fastmcp.md
maturity: validated
created: 2026-04-28
updated: 2026-04-28
clusters: [llm-agents, dev-tooling]
---

## Relations

- @sources/gemini-dr-link-eval-2026-04-28.md — parent canonical Gemini DR source; sentrux is one of 7 Adopt-for-Workflow recommendations
- @concepts/wiki-tooling-evaluation.md — Wave 2 evaluation parent
- @concepts/ip-sale-readiness.md — MIT license clears IP-sale checks (Exa-verified 2026-04-28: 808 ★)
- @entities/frameworks/langgraph.md — sentrux's hard architectural boundary governor protects LangGraph state-machine code from "god file" generation during Claude Code refactoring sessions
- @entities/frameworks/fastmcp.md — sentrux ships an MCP server mode; could attach to Cemini's FastMCP layer (lower priority than core Workflow use case)

## Raw Concept

- **URL**: https://github.com/sentrux/sentrux
- **Type**: Open-source repository / Rust CLI + MCP server
- **License**: MIT (Exa-verified 2026-04-28)
- **Stars / Forks (Exa-verified 2026-04-28)**: 808 ★ / 75 forks / 11 open issues
- **Stack**: Rust 87.4%, HTML 7.2%, Tree-sitter Query 5.2%, Shell 0.1%, GDScript
- **Org**: sentrux (Cemini-relevant primary contributors: v1b3coder, sentrux, trevorsilence)
- **Created**: 2026-03-11; **Last push**: 2026-03-19; **Latest release**: v0.5.7 (2026-03-18)
- **Releases**: 37 published — high velocity in March 2026
- **Topics**: agentharness, architecture, cobol, cobol-language, code-quality, developer-tools, harnessengineering, mcp, rust, static-analysis, treemap, visualization
- **Homepage**: https://sentrux.dev

## Narrative

### What it does
Real-time architectural sensor and code-quality governor designed to mitigate structural degradation introduced by autonomous AI coding agents. Processes codebases via tree-sitter AST plugins to compute a deterministic 0–10000 quality score across five root-cause architectural metrics: modularity, acyclicity, depth, equality, and redundancy. Visualises code dependencies as an interactive treemap and enforces architectural boundaries defined in `.sentrux/rules.toml`. Functions as both an MCP server (continuous agent feedback) and a hard quality gate within CI/CD pipelines.

### Why Adopt-for-Workflow

Direct match for the Cemini development workflow's biggest implicit risk: autonomous Claude Code sessions generating monolithic "god files" during complex LangGraph + FastAPI refactoring. Reasoning:

1. **Compiled Rust binary** — negligible local overhead, no JVM/Node.js runtime cost. Easy to install (`cargo install` or pre-built binary).
2. **Deterministic 0–10000 scoring** — no probabilistic noise. Quality regressions are detected reliably across sessions.
3. **MCP server mode** — Claude Code (and any other MCP-compatible LLM) can query the sensor in real-time during refactoring, getting immediate architectural feedback rather than waiting for a CI run.
4. **CI/CD hard gate** — pre-commit hook or GitHub Actions stage to block architectural regressions on Cemini's Python+LangGraph codebase.
5. **MIT license** — clears all IP-sale-readiness gates.

### Where it falls short

1. **Wiki / librarian server fit: ❌** — AST analysis offers no value for a Markdown-based knowledge compiler. Don't deploy on the librarian server.
2. **Cemini production stack fit: ⚠️** — runs at CI/dev-time, not at runtime. Useful as a pre-commit hook protecting the Python orchestration codebase, not as a deployed runtime container on the Hetzner production server.
3. **Headless rendering caveat** — sentrux's interactive treemap visualizations rely on Vulkan/OpenGL backends. In headless environments (CI, server), sentrux must correctly identify the lack of display server and gracefully degrade to its CLI-only fallback. **[NEEDS VERIFICATION 2026-04-29]**: confirm CLI-only mode works on the laptop and CI environments before adopting as a hard gate.
4. **Dynamic-language probabilistic accuracy** — deep architectural analysis in Python is inherently more probabilistic than statically-typed languages. False positives during FastMCP dependency checks possible. **[NEEDS VERIFICATION 2026-04-29]**: empirical false-positive rate on Cemini's existing codebase before declaring it a hard gate.

### Integration vector

**Local laptop deploy:**
1. Install sentrux binary (Cargo or release tarball).
2. Initialise `.sentrux/rules.toml` in Cemini repo root with rules constraining LangGraph state-machine boundaries (e.g., max-depth, max-fan-in for orchestrator nodes).
3. Configure the Claude Code `.claude-plugin` to query sentrux via its MCP server during refactoring.
4. Add a pre-commit hook: `sentrux check --hard-gate` to block commits that drop the quality score below threshold.

**Future CI deploy:**
1. GitHub Actions stage running sentrux's CLI-only mode.
2. Block PRs that regress the quality score below the main-branch baseline.

### Risks & open questions

1. **Memory footprint when parsing complex LangGraph graphs** [NEEDS VERIFICATION 2026-04-29] — what is the resident memory of sentrux when parsing a state machine with hundreds of nodes? Per Gemini's evaluation, this requires verification before relying on it as a hard CI gate.
2. **Sustainability** — only 3 contributors (v1b3coder, sentrux, trevorsilence). High release velocity (37 releases in 8 days March 11–19) but sole-author projects sometimes go dormant. Track upstream activity quarterly.
3. **Accuracy on Python vs statically-typed languages** [NEEDS VERIFICATION 2026-04-29] — file false-positive issues upstream if encountered; consider configurable suppression rules in `.sentrux/rules.toml`.

## Snippets

> "Real-time architectural sensor that helps AI agents close the feedback loop, enabling recursive self-improvement of code quality. Pure Rust." [Source: GitHub repo description, retrieved via Exa crawling_exa 2026-04-28]

> "Adopt for Workflow. Integrating the .claude-plugin locally creates an immediate safeguard against the generation of monolithic 'god files' during complex LangGraph and FastAPI refactoring sessions for the Cemini repository." [Source: Gemini DR report, URL 2]
