---
title: Agent memory cross-scenario generality (AutoMEM / 2606.04315)
type: concept
tags: [concept, agent-memory, evaluation, stash, conductor, k100, reference]
keywords: [2606.04315, automem, cross-scenario, stash, conductor, inkh, five-scenario-matrix]
related:
  - sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md
  - concepts/agent-memory-critique.md
  - concepts/interaction-native-knowledge-harness.md
  - concepts/agent-memory-pipeline-eval-rubric.md
  - concepts/conductor-orchestrator.md
  - concepts/librarian-server-architecture.md
  - entities/tools/claude-mem.md
  - "@ccc-wiki/concepts/agentic-memory-cross-scenario-generality.md"
  - "@ccc-wiki/concepts/failed-trajectory-harness-repair.md"
  - sources/arxiv-harnessfix-trace-repair-2606.06324-2026-06-16.md
maturity: validated
created: 2026-06-05
updated: 2026-06-16
cross-wiki-source: "@ccc-wiki/concepts/agentic-memory-cross-scenario-generality.md"
---

## Relations

- @sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md — arXiv 2606.04315
- @concepts/interaction-native-knowledge-harness.md — InKH temporal graph vs tool-managed flat files
- @concepts/agent-memory-critique.md — lookup vs true memory; representation/retrieval failure lens
- @concepts/conductor-orchestrator.md — federation query fan-out vs agent-controlled recall
- @ccc-wiki/concepts/failed-trajectory-harness-repair.md — HarnessFix repairs harness; this paper optimizes **what to remember**
- @sources/arxiv-harnessfix-trace-repair-2606.06324-2026-06-16.md — K119 OSINT source (Tier-2 sweep)

## Raw Concept

OSINT deep pass 2026-06-05 from prod brief `2026-06-05_automem-memory-cross-scenario-osint-handoff.md` + CCC K100 stub. Synthesizes Chen et al. (2606.04315) for Cemini memory-stack evaluation.

## Narrative

### Paper claim (steal-from, not AutoMEM install)

Passive memory pipelines tuned for chat-QA **underperform on agentic work** because agents need **active control** over what gets written and retrieved. Cross-scenario benchmarks are mandatory — optimizing for one scenario mis-ranks systems used across ingest, federation query, and PM bot context.

### Five-scenario matrix → Cemini analogues

| Paper scenario | Cemini stack probe |
|----------------|-------------------|
| Single-turn QA | kb-server `kb_search` one-shot |
| Multi-session chat | stash episodic + `hot.md` session cache |
| Agentic-trajectory QA | conductor federation query after multi-tool ingest |
| Memory stress tests | K-batch ingest (15 PDFs) + lint gate without context loss |
| Long-horizon tasks | PM bot / HL loop across days with claude-mem observations |

### OSINT eval answers (draft)

| Question | Posture |
|----------|---------|
| **stash + conductor** — passive or agent-controlled? | **Hybrid passive store + agent-triggered recall.** Stash `remember`/`recall` is agent-initiated; conductor fan-out is **passive RAG routing** unless the agent explicitly selects tools. On agentic-trajectory tasks, risk of **retrieval failure** (evidence in wiki/stash but not surfaced) matches paper diagnostic `[TENTATIVE]`. |
| **InKH vs AutoMEM** | InKH is **domain temporal graph + governance** (K99), not a general cross-scenario harness. Closer to structured representation than AutoMEM flat tool-managed files; still needs five-scenario audit before prod temporal-graph writes `[OPEN QUESTION 2026-06-05]`. |
| **Prod episodic memory scored without new infra?** | **CONDITIONAL-GO** — reuse `@concepts/agent-memory-pipeline-eval-rubric.md` stages + this five-scenario checklist on existing stash/kb/conductor; no AutoMEM install. Token/latency already tracked via token-economics pages. |

### Steal-from (no AutoMEM install)

| Paper insight | Cemini action |
|---------------|---------------|
| Agent-controlled read/write beats passive pipeline on agentic work | Prefer explicit stash writes + conductor retrieval over summarization-only context |
| Cross-scenario eval required | Don't judge memory on chat-QA alone — run ingest + federation + PM contexts |
| Token/latency with accuracy | Align quarterly memory-stack review with existing cost pages |

### vs HarnessFix (2606.06324)

| Paper | Focus |
|-------|-------|
| **2606.04315** | What to remember and retrieve across scenarios |
| **2606.06324** | How to diagnose/repair harness flaws from failed trajectories |

### Verdict

**REFERENCE** — methodology for memory eval harness design. **CONDITIONAL-GO** for lightweight five-scenario audit of stash/conductor/InKH before AutoMEM-style tooling investment.

## Snippets

> "Memory performance hinges on giving the agent active control over storage and retrieval rather than on a passive store behind a fixed pipeline."

> — [Source: arxiv-2606.04315 abstract, retrieved 2026-06-05]
