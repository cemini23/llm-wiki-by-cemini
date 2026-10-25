---
title: Letta (formerly MemGPT) — Stateful Agent Memory Framework
type: entity
tags: [tool, agent-memory, stateful-agents, memgpt-successor, steal-from-tier, architectural-reference]
keywords: [letta, memgpt, stateful-memory, memory-blocks, partition-paginate, context-window-bypass, agent-persistence]
related:
  - sources/5-5-moarrr-tool-eval.md
  - sources/alash3al-stash.md
  - concepts/agent-memory-critique.md
  - concepts/wiki-tooling-evaluation.md
  - sources/contextual-agentic-memory-critique-2604.27707.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-moarrr-tool-eval.md — origin source: K31 Gemini DR eval URL 18, **Steal-from** tier (extract architectural schemas; do NOT mount full Docker infra)
- @sources/alash3al-stash.md — Cemini's deployed episodic-memory layer (Wave 5 Adopt 2026-05-02). Letta is a competing framework — stays reference-only.
- @concepts/agent-memory-critique.md — academic critique of "agent memory" frameworks (vector stores / RAG / context-window are lookup, not memory). Both Letta and stash inherit this critique.
- @concepts/wiki-tooling-evaluation.md — librarian-tooling evaluation; if stash ever needs replacement, Letta joins the candidate list
- @sources/contextual-agentic-memory-critique-2604.27707.md — paper challenging the "memory" framing of these systems; useful counterpoint to Letta's marketing claims

## Raw Concept

Letta (formerly **MemGPT**) is an infrastructure platform for endowing autonomous AI agents with perpetual, stateful memory. Bypasses standard context-window limitations by fragmenting state across **memory blocks** with explicit partition + paginate logic. Identified as **Steal-from-tier** in the K31 Gemini DR eval (`@sources/5-5-moarrr-tool-eval.md` URL 18).

## Narrative

- **URL**: github.com/letta-ai/letta (per K31 eval URL 18)
- **License**: Apache-2.0 `[CONFIRMED 2026-10-25]` — the main repo and the MemGPT predecessor are both Apache-2.0; `letta-evals` is MIT. Verified against the GitHub org listing and three independent summaries.
- **Stack**: Docker-deployed infrastructure (LLM-agnostic), Python, Postgres + pgvector (similar to stash)
- **Origin**: research project from UC Berkeley → spinout

### Why Steal-from (not Adopt)

Cemini already has `alash3al/stash` deployed as the episodic-memory layer (per `@sources/alash3al-stash.md`, Wave 5 Phase 7 Adopt 2026-05-02). Both Letta and stash solve the same problem (stateful agent memory, Postgres + pgvector backend, MCP-accessible). Cemini chose stash 2026-05-02; that decision stands.

The K31 eval explicitly recommends:

> "The development team must absolutely avoid mounting the entire Letta Docker infrastructure onto the Hetzner server due to severe physical memory constraints. Instead, the developers should painstakingly extract the architectural schemas dictating how memory blocks are partitioned, pagina[ted]." [Source: 5_5 moarrr links.docx URL 18]

So: **read Letta's source code for architectural schema patterns; do NOT deploy Letta infrastructure.**

### What's worth lifting (architectural patterns)

If stash ever hits scale limits or needs schema evolution, Letta's design choices inform the migration:

1. **Memory block partition/paginate semantics** — how Letta divides agent state across context-fittable blocks
2. **Recall vs working memory tier separation** — Letta treats short-term and long-term memory differently; stash currently does this less explicitly
3. **MCP server tool surface** — Letta exposes memory operations via MCP; cross-reference against stash's MCP surface for gaps

### When Letta could re-enter consideration

NOT a current adoption candidate. Re-evaluation triggers:
- If stash hits operational limits (RAM, latency, schema-drift, etc.) and a more battle-tested alternative is needed
- If Letta ships a feature stash doesn't have and the gap becomes operationally load-bearing (e.g., sub-second multi-tier recall, structured memory-block typing, etc.)

Until then, Letta stays in the reference shelf alongside the K30 NO-GOs (SwarmVault, PageIndex, Claude-OSINT).

### Open questions [NEEDS VERIFICATION 2026-10-25] — re-dated; still open, not yet checked

- Exact GitHub URL + license + maturity
- Whether the MemGPT → Letta transition retained the Apache-2.0 license or moved to a more restrictive license (a common pattern when academic projects spin out)
- Stash vs Letta on observability + dashboard tooling — Letta's commercial backing may give it better operator UX, but Cemini doesn't currently need that
- Architectural-schema extraction effort estimate (1-2 days laptop-side reading?)

### Adoption status

**Reference-only.** No prod-side action. No brief. Add to `concepts/agent-memory-critique.md` cross-references if/when that page expands. Architectural-schema reading deferred until stash needs replacement.

## Snippets

- **Scope framing** (K31 eval): "Letta, previously known as the MemGPT framework, is an infrastructure platform engineered to endow autonomous artificial intelligence agents with perpetual, stateful memory. It achieves this structural persistence by bypassing standard context-window limitations. The architecture fragments system [state across memory blocks]." [Source: 5_5 moarrr links.docx URL 18]

- **Recommendation tier (Steal-from with explicit do-not-mount caveat)**: "The development team must absolutely avoid mounting the entire Letta Docker infrastructure onto the Hetzner server due to severe physical memory constraints. Instead, the developers should painstakingly extract the architectural schemas dictating how memory blocks are partitioned, pagina[ted]." [Source: 5_5 moarrr links.docx URL 18]
