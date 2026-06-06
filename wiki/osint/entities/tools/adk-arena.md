---
title: ADK Arena — agent framework benchmark runner
type: entity
tags: [entity, tool, agent-harness, evaluation, phase-0, k101]
keywords: [adk-arena, 2606.05548, llm-as-a-developer, mcp-atlas, docker, phase-0]
related:
  - sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md
  - concepts/adk-arena-framework-evaluation.md
  - concepts/mcp-tool-calling-eval-scaffold.md
  - concepts/system-scaling-harness-evaluation.md
  - concepts/wiki-tooling-evaluation.md
  - entities/tools/lazy-tool.md
  - "@ccc-wiki/concepts/adk-arena-agent-framework-benchmark.md"
maturity: validated
created: 2026-06-06
updated: 2026-06-06
phase_0_verdict: NO-GO
license_verified: MIT
repo: https://github.com/jintao-h/ADK-Arena
---

## Relations

- @sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md — arXiv 2606.05548 source page
- @concepts/adk-arena-framework-evaluation.md — OSINT synthesis (REFERENCE posture)
- @entities/tools/lazy-tool.md — production MCP proxy; **not** in ADK Arena eval scope
- @concepts/mcp-tool-calling-eval-scaffold.md — steal MCP-Atlas GTFA scoring pattern here

## Raw Concept

**Phase-0 audit** 2026-06-06 — cloned `/tmp/adk-arena-audit/`; `gh api` license spot-check; compared to lazy-tool + MAVEN smoke matrix + existing wiki discipline.

**Verdict: NO-GO (Adopt)** · **Steal-from: CONDITIONAL-GO**

## Narrative

Microsoft / Ohio State research pipeline that benchmarks **51 Python Agent Development Kits** via **LLM-as-a-Developer** — one coding agent learns each framework API, generates `solve(problem_statement, workdir)` agents, runs SWE-bench / Terminal-Bench / τ²-bench / **MCP-Atlas** in Docker.

### License [CONFIRMED]

| Check | Result |
|-------|--------|
| `LICENSE` | MIT (Copyright 2026 The ADK Arena Authors) |
| GitHub API | `"license": "MIT"` |
| Root `requirements.txt` | numpy, pandas, matplotlib, scipy, httpx — permissive |

Full pipeline pulls **51 framework Docker images** + benchmark clones (MCP-Atlas, τ²-bench, SWE-bench) — transitive license surface is large; eval *targets* are third-party repos.

### Maturity [CONFIRMED — immature repo]

| Signal | Value |
|--------|-------|
| Stars | 1 |
| Commits (shallow clone) | 1 |
| Last push | 2026-06-06 |
| Unit tests | None (`tests/` absent, no CI) |
| Paper | arXiv 2606.05548 — methodology validated; **repo ≠ paper maturity** |

### Failure mode — harness benchmark class

| Risk | Finding |
|------|---------|
| Hardcoded layout | Rigid `data/`, `resources/`, 51× `docker/generation/install/{fw}.sh` — not plug-in for lazy-tool / Cursor |
| Docker mandatory | ~50 GB disk; MCP-Atlas built `linux/amd64` — Apple Silicon emulation |
| Eval surface | Python ADK `solve()` only; **conductor excluded** from framework collector |
| MCP-Atlas ≠ prod MCP | HTTP `agent-environment` sandbox; not stdio lazy-tool path |
| Cost | Paper: $0.6–$3.4 per generated agent × 204 pairs — research budget |

### Overlap with Cemini [CONFIRMED — duplicate discipline]

- **lazy-tool** (GO) — token proxy; ADK Arena cannot score it.
- **MAVEN / mcp-tool-calling-eval-scaffold** — manual smoke matrix already covers MCP discipline; ADK Arena duplicates MCP-Atlas slice at 100× infra.
- **adk-arena-framework-evaluation** concept — already REFERENCE; this entity locks NO-GO.

### Steal-from (no install)

1. In-container **token proxy** + cost metrics (`src/arena/proxy/token_proxy.py`)
2. **MCP HTTP → stdio bridge** (`mcp_stdio_bridge.py`) for smoke tests
3. **Three-level generation feedback** — static → mock LLM → real task (mirrors `skill_audit` + `ingest_session_gate`)
4. **MCP-Atlas GTFA** claim-coverage scoring — extend MAVEN smoke step (2)
5. Pipeline flags: `--skip-existing`, `--smoke-test`, `--aggregate --eval`
6. Paper finding: framework choice ≈ model choice; generation cost as API-complexity proxy

### Do not adopt

- 51-framework Docker factory on laptop
- Full 204-pair shootout
- LLM-as-a-Developer as default Phase-0 workflow (cost + non-determinism)

## Snippets

> "Evaluating all 51 popular Python ADK frameworks (204 agent–benchmark pairs)… no single framework dominates."

> — [Source: arxiv-2606.05548-adk-arena-evaluating-agent-development-kits-via.pdf abstract, retrieved 2026-06-06]

## Dead Ends

- **Replicating ADK Arena to rank lazy-tool vs conductor** — wrong interface; collector explicitly skips `conductor`.
- **Installing for quarterly cadence** — ~50 GB + frontier LLM spend incompatible with solo Mac Studio operator model.
