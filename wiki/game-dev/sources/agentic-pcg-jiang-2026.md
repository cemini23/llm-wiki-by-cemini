---
title: Jiang et al. — Agentic PCG via tool-using LLMs (2026)
type: source
tags: [source, pcg, research, llm, level-design]
keywords: [agentic-pcg, procedural, tool-using, jiang, sokoban, mario]
related:
  - concepts/agentic-pcg-level-design.md
read_status: read
source_type: paper
source_url: https://zehua-jiang.github.io/AgenticPCG/
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Raw Concept

**Agentic PCG** — wrap game level as interactive env; LLM agent perceives, reasons, plans, edits via tools with metric + simulation feedback.

## Narrative

### Loop [CONFIRMED]

Perceive state → reason → plan edits → apply tools → evaluate metrics (connectivity, path length) or simulated A* gameplay (SMB).

### Domains

Binary Maze/Door, Lode Runner, Zelda, Sokoban, Super Mario Bros — controllable metric targeting + natural language creative control.

### Tools

Primitives (place_tile) + classic algorithms (BSP, digger) + corridor rerouting.

### Implementation

GitHub: JiangZehua/AgenticPCG — SSRN preprint 6499021.

### Hobby takeaway

Use **tool loop + metrics** for dev-time map assist; ship static baked maps for Stronghold-like castle sim.

## Snippets

```bibtex
@article{jiang2026agentic,
  title={Agentic PCG: Procedural Content Generation via Tool-using LLMs},
  author={Jiang, Zehua and Earle, Sam and Khalifa, Ahmed and Togelius, Julian},
  year={2026}
}
```
