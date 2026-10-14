---
title: Inbox arXiv batch — 2026-10-07 (6 ingests, 0 rejects)
type: source
tags: [source, triage, arxiv, ingest, agents, harness]
keywords: [arxiv, triage, digest, masbench, learn2play, speedrunbench, mafia, world-solver, social-deduction]
related:
  - sources/inbox-arxiv-reject-batch-2026-10-05.md
  - sources/arxiv-2610.04672-masbench-partial-observability-2026-10-07.md
  - sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md
  - sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md
  - sources/arxiv-2610.08076-speedrunbench-strategy-formation-2026-10-07.md
  - sources/arxiv-2610.04261-social-deduction-rft-2026-10-07.md
  - sources/arxiv-2610.08720-worldsolver-visual-fidelity-2026-10-07.md
  - sources/cross-wiki-routed-briefs-2026-10-05.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
  - sources/inbox-arxiv-reject-batch-2026-10-09.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-10-07
updated: 2026-10-07
---

## Raw Concept

Six PDFs from the `2026-10-06` and `2026-10-07` digests. **6 ingest, 0 reject** — the first all-ingest batch in this wiki. Every paper is an LLM-agent study with a game environment or a game-adjacent task, which is exactly the wiki's agent-harness lane. Preingest: 6× NEW, 0 duplicates.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2610.04672 | MASBench — multi-agent collab under partial observability | **Ingest** | @sources/arxiv-2610.04672-masbench-partial-observability-2026-10-07.md |
| 2610.08215 | Learn2Play Bench — learning from experience | **Ingest** | @sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md |
| 2610.05041 | Communication shapes collective inference (Mafia) | **Ingest** | @sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md |
| 2610.08076 | SpeedrunBench — strategy formation via speedrunning | **Ingest** | @sources/arxiv-2610.08076-speedrunbench-strategy-formation-2026-10-07.md |
| 2610.04261 | RFT and social behaviour in hidden-role games | **Ingest** | @sources/arxiv-2610.04261-social-deduction-rft-2026-10-07.md |
| 2610.08720 | WorldSolver — solver generation and visual fidelity | **Ingest** | @sources/arxiv-2610.08720-worldsolver-visual-fidelity-2026-10-07.md |

### Why nothing was rejected

The `llm-agent-game-paper` query is doing what it was tuned to do. Five of the six are direct harness or game-agent work. WorldSolver is the one marginal case — its domain is graphics-research physics simulation, not games — but it was kept for its **evaluation design**: it is the first bench in this wiki's ladder to score **visual fidelity** of rendered output, which is a real acceptance axis for a 3D castle sim. That is recorded explicitly on its page, with the physics content marked as non-transferable.

### The connecting thread

Three of the six converge on the same question from different angles: **what should an agent carry forward from past attempts?**

- Cogentic (rule H3) says promote only **verified** results into a durable ledger.
- Learn2Play finds **complete raw records** beat summaries as a learning substrate.
- The Mafia study finds an **inherited notes corpus can actively harm** — sixty generations of self-written notes scored below no notes at all.

Read together, they argue for a small verified ledger **plus** a complete raw log, with inherited derived notes treated as a re-validation risk rather than an asset. That tension is the most useful thing in this batch and is reflected in the harness concept.

### Phase-0

One repo: `github.com/BUPT-GAMMA/MASBench` — **MIT** (`LICENSE` at root). **CONDITIONAL-GO** on licence, **STEAL-FROM** in practice. No other paper ships a resolvable repository.

**Action:** Archive 6 PDFs; clear inbox.

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/` (per archived filename).

## Dead Ends

- Treating this batch as a sign the query needs no further tuning. It is one good window, not proof.
- Adopting MASBench code for a Godot project. It targets multi-agent LLM systems.
