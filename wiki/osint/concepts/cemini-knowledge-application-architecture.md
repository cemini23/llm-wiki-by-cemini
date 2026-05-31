---
title: Cemini knowledge-application architecture — closing the wiki→prod loop
type: concept
tags: [concept, architecture, knowledge-management, audit, cemini-prod, workflow, k89]
keywords: [knowledge-application, lesson-registry, brief-completion, wiki-to-prod, knowledge-drift, retrofit, DOCUMENTED-ONLY, stash, kb-server]
related:
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - concepts/agent-memory-critique.md
  - concepts/librarian-server-architecture.md
  - concepts/production-trading-blind-spots.md
  - concepts/pnl-attribution-versioning.md
  - concepts/exploration-graph-dead-ends.md
  - entities/infrastructure/cemini-stack.md
  - entities/tools/world-cup-bot.md
  - sources/arxiv-self-healing-llm-agents-2605.06737.md
  - meta/wiki-gap-detect-cadence.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/cemini-workflow-tooling-audit-2026-05-30.md — laptop-side mirror audit (K84); same failure mode, different surface
- @concepts/agent-memory-critique.md — kb-server + stash are **lookup**, not enforcement; sets expectations for this architecture
- @concepts/librarian-server-architecture.md — two-layer memory (static wiki + episodic stash) that prod under-consumes
- @concepts/production-trading-blind-spots.md — exemplar lessons that sat in wiki while prod repeated mistakes for months
- @concepts/pnl-attribution-versioning.md — canonical retrofit case (`logic_version` after prolonged mixed PnL)
- @concepts/exploration-graph-dead-ends.md — preserve abandoned paths so agents don't re-try them
- @entities/tools/world-cup-bot.md — repeat-lesson motivator (build loop rediscovered solved problems)
- @meta/wiki-gap-detect-cadence.md — wiki-side stale-claim detection; complementary, not substitute for prod retrofit

## Raw Concept

What prompted this page: operator observed a **systemic pattern** — ingested knowledge (X posts, arXiv, tool evals, Gemini DR, prior briefs) exists in the wiki, yet agents and prod code **re-learn the same mistakes**. K84 closed laptop workflow gaps only after an explicit audit; prod was hypothesized to have the same `DOCUMENTED-ONLY` debt at larger scale. K89 ships a prod audit brief + reusable prompt; this page defines the **wiki-side architecture** for closing the loop.

## Narrative

### The failure mode

| Symptom | Mechanism | Example |
|---------|-----------|---------|
| Repeat prompts for solved problems | No **enforcement** — RAG is optional lookup | World-cup-bot: calendar guard, negative filters, reconciliation — wiki had answers |
| Ingested tooling unused for months | No **adoption gate** after ingest | K84: Obsidian/kepano/cadences documented; deployed only after audit |
| Old code never retrofitted | **Greenfield bias** — new modules get doctrine; bootstrap doesn't | K75: `logic_version` added months after PnL confusion |
| Briefs orphaned | No **completion verification** | `/opt/cemini/briefs/` grows; implementation status unknown |

**Root cause (synthesized):** Cemini treats knowledge as **retrievable** (kb-server, stash, wiki grep) but not **binding**. Agents do not self-learn production weights; stash consolidates episodes but does not block bad deploys. See @concepts/agent-memory-critique.md — calling lookup "memory" overstates what the stack guarantees.

### Intended loop (target architecture)

```
Raw source → ingest → wiki page(s)
                ↓
         brief (if prod-touching)
                ↓
    prod implement + verify + registry bump
                ↓
         completion report → stash failure/success episode
                ↓
    quarterly audit (laptop workflow + prod knowledge-application)
```

Each arrow needs an **artifact** and a **verification step** — not just habit.

### Two surfaces, one problem

| Surface | Audit | Status (2026-05-31) |
|---------|-------|---------------------|
| **Laptop / OSINT workspace** | @concepts/cemini-workflow-tooling-audit-2026-05-30.md | Gaps **closed** (Obsidian, cadences, v5 prompt, LaunchAgents) |
| **Production `/opt/cemini`** | Prod brief + prompt (K89) | **Wave 1 pending** — server-Claude off-hours |

Symmetry matters: fixing laptop workflow without prod audit leaves **half the system** in `DOCUMENTED-ONLY` state.

### Wiki-side mechanisms (proposed)

| Mechanism | Owner | Purpose |
|-----------|-------|---------|
| **Lesson registry** (YAML on prod; wiki mirror concept) | prod + OSINT | Map `@concepts/*` or `@sources/*` → prod module → status (`APPLIED` / `PARTIAL` / `DOCUMENTED-ONLY`) → `last_verified` |
| **Brief completion report** | prod server-Claude | Every shipped brief ends with `## Implementation status` + git SHA + probe date |
| **Post-incident stash episode** | operator | After prod incident: `remember` failure pattern + wiki `@concepts/exploration-graph-dead-ends.md` if abandoned |
| **Pre-promotion checklist** | prod SOP | Shadow + registry bump + @concepts/production-trading-blind-spots.md scan — no live without row |
| **mem-search / wiki grep ritual** | agents (CCC rule) | Before re-Adopt or greenfield build: "Did we already solve this?" |
| **Wiki gap detect Tier 1** | laptop weekly | Stale `[NEEDS VERIFICATION]` — wiki truth drift |
| **Knowledge-application audit** | prod quarterly | Prompt at `/opt/cemini/prompts/cemini-knowledge-application-audit-v1-2026-05-31.md` |

**Registry location (prod canonical):** `/opt/cemini/docs/wiki-lesson-registry.yaml` — create on first audit Wave 1 completion. Wiki holds **concept-level** status summaries only (no prod secrets).

### Prod audit (K89) — shipped artifacts

| Artifact | Location |
|----------|----------|
| Handoff brief | `cemini-prod:/opt/cemini/briefs/2026-05-31_cemini-knowledge-application-audit-cemini.md` |
| Reusable prompt | `cemini-prod:/opt/cemini/prompts/cemini-knowledge-application-audit-v1-2026-05-31.md` |
| Wave 1 report (pending) | `cemini-prod:/opt/cemini/briefs/YYYY-MM-DD_cemini-knowledge-application-audit-report.md` |

Laptop copies: `briefs/2026-05-31_cemini-knowledge-application-audit-cemini.md`, `briefs/prompts/cemini-knowledge-application-audit-v1-2026-05-31.md`.

**Seven audit layers** (prod prompt): knowledge plumbing → agent cognition → strategy versioning → execution plumbing → data fidelity → infrastructure debt → per-strategy vertical.

### Scoring vocabulary (shared laptop + prod)

Use consistently in audits and registry rows:

| Status | Meaning |
|--------|---------|
| `APPLIED` | Wiki lesson has named prod file/config/container proof |
| `PARTIAL` | Some paths comply; others don't |
| `DOCUMENTED-ONLY` | Wiki/brief exists; prod unchanged |
| `CONTRADICTED` | Prod behavior violates documented lesson |
| `UNKNOWN` | Not probed this cycle |

K84 laptop audit used the same pattern informally; K89 formalizes it for prod.

### What agents do and do not do [TENTATIVE until Wave 1 report]

| Question | Expected answer (pre-audit) |
|----------|----------------------------|
| Self-learn (weights/rules from outcomes)? | **No** automatic loop in prod; coach/reviewer may suggest config changes |
| Self-heal (failure detect + replan)? | **Partial** — compare to @sources/arxiv-self-healing-llm-agents-2605.06737.md; mostly try/except, not taxonomy-driven recovery |
| Remember across sessions? | **stash/kb on librarian** — available, not mandatory in brain hot path |
| Apply wiki at build time? | **Inconsistent** — depends on operator/agent discipline, not pipeline gate |

Wave 1 prod report must confirm or revise each row with evidence.

### Retrofit priority (wiki guidance for prod queue)

When prod audit produces a retrofit queue, sort by:

1. **Live capital exposure** — strategies posting real orders
2. **Silent failure risk** — wrong PnL, phantom fills, stale ticks (see blind-spot catalog)
3. **Brief backlog** — shipped >30d, no implementation proof
4. **IP-sale / diligence visibility** — undocumented debt, license drift

Greenfield modules (world-cup-bot, recent K76 diagnostics) are not exempt — they still need registry rows.

### Relationship to other wiki concepts

- **Dead ends** (@concepts/exploration-graph-dead-ends.md) — prevent re-trying abandoned approaches; complements lesson registry
- **Blind spots** (@concepts/production-trading-blind-spots.md) — the *content* of many lessons; registry tracks *application*
- **Workflow audit** (@concepts/cemini-workflow-tooling-audit-2026-05-30.md) — laptop harness; run both audits on similar cadence
- **Gap detect** (@meta/wiki-gap-detect-cadence.md) — wiki claim freshness; does not check prod code

## Snippets

> "Current agent memory systems are lookup mechanisms (memos), not memory." — @concepts/agent-memory-critique.md

> "For bot: the edge is in the plumbing, not the algorithm." — @concepts/production-trading-blind-spots.md [Source: Posts 2.docx — @MatiasScalbi]

> "NPX install path is one command" — K84 closed laptop gaps only after explicit audit proved ingested knowledge was DOCUMENTED-ONLY. — @concepts/cemini-workflow-tooling-audit-2026-05-30.md

## Dead Ends

- **Expecting kb-server alone to prevent repeat mistakes** — retrieval without enforcement does not change prod behavior; registry + completion reports required.
- **Full-repo `/tech-debt-audit` on prod host** — parallel subagents destabilize CPU during trading; run debt quant from laptop git export (@entities/tools/tech-debt-skill.md).
- **Wiki-only fix without prod audit** — K84 proved laptop can be clean while prod still drifts; both surfaces need periodic audit.
