---
title: Fara — scalable learning environments for computer-use agents
type: concept
tags: [concept, computer-use, browser-agents, agent-training, k129]
keywords: [Fara, Fara-1.5, FaraGen, Microsoft, computer use, web automation, training pipeline]
related:
  - sources/arxiv-fara-1-5-computer-use-2606.20785-2026-06-25.md
  - concepts/code-as-agent-harness.md
  - concepts/agentic-navigation-memory-strategy.md
  - sources/playwright-mcp-microsoft.md
  - entities/tools/playwright-mcp.md
maturity: draft
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- @sources/arxiv-fara-1-5-computer-use-2606.20785-2026-06-25.md — primary source (arXiv 2606.20785)
- @sources/playwright-mcp-microsoft.md — sibling Microsoft browser-automation stack
- @concepts/code-as-agent-harness.md — training-environment vs runtime harness distinction

## Raw Concept

Prompted by arXiv **2606.20785** (K129). **Fara-1.5** describes scalable **learning environments** for computer-use agents via the **FaraGen** data-generation pipeline (Microsoft; repo `microsoft/fara`).

## Narrative

Computer-use agents (GUI/web automation) need diverse, executable training environments at scale. FaraGen synthesizes tasks + verifiable outcomes for agent policy learning — complementary to runtime MCP/browser harnesses (Playwright MCP, Cursor built-in browser).

**Cemini reference posture (not prod trading):**

| Surface | Use |
|---------|-----|
| poker-arena / castle-sim agent dev | Benchmark **browser-based** eval loops (Arena UI, Godot export smoke) |
| OSINT research sessions | Pattern reference for Cursor built-in browser + Stagehand parity tests |
| CeminiSuite prod | **No route** — training infra, not order egress |

**Limitations [TENTATIVE]:** Industrial Microsoft stack; license/deploy boundary unverified for Cemini prod; prefer **REFERENCE** until Phase-0 on `microsoft/fara` repo completes.

## Snippets

> "Fara-1.5: Scalable Learning Environments for Computer Use Agents" [Source: arXiv:2606.20785 title (retrieved 2026-06-25)]

> "Repo: https://github.com/microsoft/fara" [Source: wiki/sweeps/2026-06-25-daily.md preingest (retrieved 2026-06-25)]
