---
title: Inbox arXiv reject batch — 2026-09-30 (8 ingests + 2 rejects)
type: source
tags: [source, triage, reject, arxiv, ingest]
keywords: [arxiv, triage, reject, digest, ad-hominem, matching]
related:
  - sources/inbox-arxiv-reject-batch-2026-09-24.md
  - sources/arxiv-2609.29228-bt-fsm-llm-conversion-2026-09-30.md
  - sources/arxiv-2609.29837-pubg-ally-embodied-teammate-2026-09-30.md
  - sources/arxiv-2609.31076-abstraction-ladder-code-skills-2026-09-30.md
  - sources/arxiv-2609.34214-glyphbench-rl-playground-2026-09-30.md
  - sources/arxiv-2609.34342-sage-strategic-reasoning-2026-09-30.md
  - sources/arxiv-2609.35928-prompted-identity-factionalism-2026-09-30.md
  - sources/arxiv-2609.37658-enterprisebench-strategic-agents-2026-09-30.md
  - sources/arxiv-2609.37853-anthrodial-social-npc-harness-2026-09-30.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
  - entities/tools/firmbench.md
  - entities/tools/codehack.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-09-30
updated: 2026-09-30
---

## Raw Concept

Ten PDFs from `2026-09-30-daily.md` and earlier sweeps. **8 ingest** (game AI, agent harness, agent evals, NPC guardrails); **2 reject** (political debate rhetoric; market-design simulation). Preingest: 10× NEW, 0 duplicates.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2609.29228 | LLM-driven BT↔FSM conversion | **Ingest** | @sources/arxiv-2609.29228-bt-fsm-llm-conversion-2026-09-30.md |
| 2609.29837 | PUBG Ally conversational teammate | **Ingest** | @sources/arxiv-2609.29837-pubg-ally-embodied-teammate-2026-09-30.md |
| 2609.31076 | Abstraction ladder, code-based skills | **Ingest** | @sources/arxiv-2609.31076-abstraction-ladder-code-skills-2026-09-30.md |
| 2609.34214 | GlyphBench RL playground | **Ingest** | @sources/arxiv-2609.34214-glyphbench-rl-playground-2026-09-30.md |
| 2609.34342 | SAGE strategic reasoning | **Ingest** | @sources/arxiv-2609.34342-sage-strategic-reasoning-2026-09-30.md |
| 2609.35928 | Prompted identity degrades cooperation | **Ingest** | @sources/arxiv-2609.35928-prompted-identity-factionalism-2026-09-30.md |
| 2609.37658 | EnterpriseBench strategic agents | **Ingest** | @sources/arxiv-2609.37658-enterprisebench-strategic-agents-2026-09-30.md |
| 2609.37853 | AnthroDial social-agent harness | **Ingest** | @sources/arxiv-2609.37853-anthrodial-social-npc-harness-2026-09-30.md |
| 2609.28673 | Argumentative behaviour / character attacks | **Reject** | cs.CL political debate rhetoric — @ccc-wiki |
| 2609.34679 | Preference to reciprocity, decentralized matching | **Reject** | cs.GT/ econ simulation — @osint-wiki |

**Reject reasons.**

- **2609.28673** — Benchmarks LLM defences against ad hominem attacks in political debate corpora. Findings on how safety fine-tuning narrows the strategic action space are interesting in principle, but the domain is persuasive political dialogue, not game NPCs. Marginal for the guardrail shelf. Route to @ccc-wiki if agent-persuasion eval is wanted.
- **2609.34679** — LLM-agent plus contextual-bandit model of decentralized bipartite matching, validated on a simulated marriage market. Computational social science and market design. No game-dev application. Route to @osint-wiki.

**Phase-0 audit results (2026-09-30):**

| Repo | From | Licence | Verdict |
|------|------|---------|---------|
| `github.com/chenzhwsysu57/SAGE` | 2609.34342 | none | **NO-GO clone** — STEAL-FROM (pattern only) |
| `github.com/zhoupeng-0425/FSM2BT` | 2609.29228 | none | **NO-GO clone** — STEAL-FROM |
| `github.com/NUDTQI/PartoPrey-BT-RL` | 2609.29228 | none | **NO-GO clone** — STEAL-FROM |
| `github.com/sduyangmin/FirmBench` | 2609.37658 | Apache-2.0 | **CONDITIONAL-GO** — see @entities/tools/firmbench.md |
| `github.com/BartekCupial/codehack` | 2609.31076 | MIT | **CONDITIONAL-GO** — see @entities/tools/codehack.md |

**Action:** Archived 10 PDFs; inbox cleared 2026-09-30.

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/` — remote sizes match the originals.

## Dead Ends

- Adding `ANDNOT cat:cs.CL.*` to the `llm-agent-game-paper` query. **Rejected 2026-09-30** — most wanted NPC and agent papers are cs.CL, so this would starve the feed. Accept the two rejects instead; the query already excludes astro-ph and UAV terms.
- Adding market-design / matching terms as exclusions — too narrow to be worth a config edit.
- Treating the FSM2BT / SAGE repos as adopted before a licence check.
