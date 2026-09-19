---
title: Inbox arXiv reject batch — 2026-09-19 (3 rejects + 1 ingest)
type: source
tags: [source, triage, reject, arxiv, ingest]
keywords: [arxiv, triage, reject, digest, llm-agent, uav, clue, logn-questions]
related:
  - sources/inbox-arxiv-reject-batch-2026-08-15.md
  - sources/arxiv-2609.18935-long-lived-characters-local-inference-2026-09-19.md
  - concepts/llm-npc-runtime-ai-shelf.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-09-19
updated: 2026-09-19
---

## Raw Concept

Four PDFs from `2026-09-17-daily.md` … `2026-09-18-daily.md` (`llm-agent-game-paper` arXiv-API cluster). **1 ingest** (game NPC memory); **3 reject** (Clue deductive-reasoning eval, log(N)-Questions comms benchmark, UAV LAWN networking). Preingest: 4× NEW.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2609.18935 | Long-Lived Characters, Local Inference: Incremental Memory Maintenance for Game NPCs | **Ingest** | @sources/arxiv-2609.18935-long-lived-characters-local-inference-2026-09-19.md |
| 2609.18736 | Clueing up LLMs with Tool-Augmented Deductive Reasoning | **Reject** | cs.AI — Clue board-game multi-agent deductive reasoning eval; harness depth → @ccc-wiki |
| 2609.19113 | Playing log(N)-Questions over Wikipedia Abstracts | **Reject** | cs.CL — paired-frontier comms-efficiency benchmark; eval depth → @ccc-wiki |
| 2609.19538 | Agentic AI Networking for Heterogeneous Unmanned Aerial Systems in LAWNs | **Reject** | cs.AI/cs.MA — UAV low-altitude wireless networking; `llm-agent-game-paper` false positive (same class as 2608.10309 UAV noise) |

**Phase-0:** none on rejects. Ingest paper is **shelf / STEAL-FROM pattern** only — local Qwen hybrid RNN-attention; no repo pin until SPDX + Godot bridge exists.

**Briefs:** none prod-touching. Optional castle-sim Tier 3+ shelf note only (local LLM NPC memory — defer).

**Action:** Archive 4 PDFs to egress; clear inbox. Tighten `llm-agent-game-paper` `arxiv_query`: add `ANDNOT` UAV / UAS / drone / aerial / LAWN / unmanned.

**Location:** [NEEDS VERIFICATION 2026-09-26] egress archive failed 2026-09-19 (SSH reset to cemini-egress-fi) — PDFs remain in `research to be indexed/` until tunnel retry succeeds

## Snippets

```
python3 scripts/preingest_check.py → 4 NEW, 0 LIKELY, 0 DUPLICATES
Digest cluster: llm-agent-game-paper (arXiv API; fetched 2026-09-17…18)
2609.19538 abstract cue: "Low-altitude wireless networks (LAWNs) … unmanned aerial systems"
2609.18736 abstract cue: "text-based, multi-agent version of the classic board game Clue"
```

## Dead Ends

- Phase-0 on UAV LAWN agentic networking for castle-sim / Godot harness
- Deep Clue deductive-reasoning eval pages in game-dev-wiki (CCC-primary)
- Treating log(N)-Questions Wikipedia benchmark as NPC/playtest adopt target
