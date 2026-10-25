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
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/agents-last-exam-benchmark.md
  - concepts/ems-execution-security-gaps.md
  - sources/cemini-external-code-audit-errors-2026-06-03.md
  - concepts/interaction-native-knowledge-harness.md
  - sources/arxiv-interaction-native-knowledge-harness-2606.01886.md
  - concepts/reviewer-passive-injection-corpus.md
maturity: validated
created: 2026-05-31
updated: 2026-10-25
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
- @concepts/cemini-wiki-ingest-workflow.md — four-phase ingest pipeline; briefs + ROADMAP step after wiki commit
- @concepts/interaction-native-knowledge-harness.md — passive injection still needs lesson-registry for prod actions (K99)

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
| **Production `/opt/cemini`** | K89 Wave 1 report | **Complete** — Wave 2–3 **DONE**; R08 brain-only → **Wave 3b staged** |

Symmetry: laptop clean; prod had same `DOCUMENTED-ONLY` pattern at scale. **Wave 2 briefs staged** to close the enforcement loop.

### Wave 1 findings (2026-05-31) [CONFIRMED — prod audit report]

**Report:** `cemini-prod:/opt/cemini/briefs/2026-05-31_cemini-knowledge-application-audit-report.md`  
**Git SHA at audit:** `bb629289a4bc06a69924d0ecf7d5261182f15a20`  
**Gap JSON:** `briefs/artifacts/knowledge-audit-2026-05-31.json`

| Metric | Value |
|--------|-------|
| Containers probed | 44 up, 0 unhealthy |
| Layer rows APPLIED | 14 |
| PARTIAL | 16 |
| DOCUMENTED-ONLY | 5 |
| CONTRADICTED | 0 |
| Brief backlog (May 25–31) | ~11/20 implemented, 6 partial/deferred, 2 not started |
| 90-day brief completion artifact | ~60% **UNKNOWN** |

**Headline answers (confirmed):**

| Question | Wave 1 answer |
|----------|---------------|
| Self-learn? | **No** — operator-driven registry bumps only |
| Self-heal? | **Minimal** — fail-open + kill switch, not replan taxonomy |
| Strategies accurate? | **Mixed** — pm_lp live; pm_weather HOLD (falsification INSUFFICIENT_DATA); btc shadow-gated |
| Bootstrap debt? | **`agents/orchestrator.py`** — logic_version yes; kb/stash no |
| Wiki → brain? | **Analyst only** (`llm_analyst` → `fetch_wiki_context`); orchestrator does not query kb |

**Top PnL-risk gaps:**

1. Orchestrator without kb/stash (G01)
2. No lesson registry (G02)
3. pm_lp live vs pm_weather HOLD — asymmetric promotion (document or gate)
4. Brief completion tracking ad hoc (G08)
5. Swap **78%** on 7.6 GB RAM — OOM risk (ops)

**Top retrofit queue (Wave 2 targets first 3):**

| Rank | Item | Wave 2 brief |
|------|------|--------------|
| 1 | kb hook in orchestrator (visibility v1) | `2026-05-31_k89-wave2-brain-kb-context-hook-cemini.md` |
| 2 | `wiki-lesson-registry.yaml` bootstrap | `2026-05-31_k89-wave2-wiki-lesson-registry-bootstrap-cemini.md` |
| 3 | Brief completion template + lint | `2026-05-31_k89-wave2-brief-completion-template-cemini.md` |

Deferred P2: stash on prod, self-healing taxonomy, SkillSpector wire, 30s vs 30min reconcile cadence.

**Stash transport fix (2026-05-31):** Wave 4 `core/stash_remember.py` and `wiki_enforcement._stash_recall` incorrectly POSTed/GETed REST `/api/v1/remember|recall` on `:9090` (metrics-only). Fixed on prod via **`core/stash_mcp_client.py`** — MCP SSE `http://10.0.0.2:8080/sse` (`remember` / `recall` tools). `scripts/check_stash_remember_ready.py` now probes MCP and **PASS**. Env: `STASH_MCP_URL` (not `STASH_BASE_URL`). Enable `STASH_REMEMBER_ENABLED=true` when operator ready for automated F04 remember.

### Wave 3 — accuracy, healing, enforcement (**DONE** 2026-05-31)

**Principle:** shadow/paper first; **`pm_lp_rewards` never auto-blocked** in kb/stash v1.

| Brief | Purpose | Live lp touch | Status |
|-------|---------|---------------|--------|
| promotion-sop-unified | One checklist + readiness script | Reconcile waivers | **DONE** |
| failure-taxonomy-corrective-actions | Taxonomy + daily rollup + shadow auto-correct | Alert-only on lp | **DONE** |
| prod-memory-swap-mitigation | Swap alert + budget doc | Ops; upgrade rec | **DONE** (swap still ~80%) |
| kb-stash-behavior-enforcement | Registry + kb gates | **`log_only` denylist** | **DONE** (brain path only) |

**Wave 3 verify caveat:** `check_wiki_enforcement` wired on **`brain_equity` orchestrator only** — PM executors pending Wave 3b.

### Wave 3b — PM/WC executor wiring (**STAGED**)

| Brief | Purpose |
|-------|---------|
| `k89-wave3b-pm-executor-wiki-enforcement` | `pm_btc_updown`, `pm_weather`, WC shadow — **not live lp** |

**Recommended prod order:** Wave 3b → then Wave 4 (lp warn-only, stash auto).

### Roadmap to target state (summary)

| Phase | Outcome |
|-------|---------|
| Wave 2 | Visible + tracked lessons |
| Wave 3 | Accurate promotion, shadow healing, kb/stash **binds shadow trades** |
| Wave 4 (future) | pm_lp observe → warn on CONTRADICTED; prod stash remember on incidents (**MCP client wired 2026-05-31; flag still off**) |
| Wave 5 (future) | Rule/threshold learning on shadow metrics only |

### Wave 2 — enforcement loop (**DONE** 2026-05-31, operator confirmed)

| Brief | Purpose | Expected outcome |
|-------|---------|------------------|
| wiki-lesson-registry-bootstrap | `docs/wiki-lesson-registry.yaml` + smoke script | Answer "is lesson X applied?" in one grep |
| brief-completion-template | `BRIEF_TEMPLATE.md` + backfill 10 May briefs | Close brief→code verification gap |
| brain-kb-context-hook | Orchestrator pre-cycle kb fetch, log-only v1 | Habitual wiki lookup at decision time |

**Implementation order on prod:** registry bootstrap → completion template (dogfoods status block) → kb hook (updates G01 registry row).

### Intent registry (meta — prevents scope drop)

**Program tracker (prod canonical):** `cemini-prod:/opt/cemini/briefs/2026-05-31_k89-master-roadmap-cemini.md`

Operator initial K89 intent named **self-learning, self-healing, accurate strategies, wiki enforcement, bootstrap debt retrofit** — Wave 1–2 alone did not satisfy that scope; Wave 3+ staged after explicit re-prompt (same failure mode this program fixes).

| Rule | Enforcement |
|------|-------------|
| Every K89 brief cites capability id `R##` from master roadmap matrix | Brief authoring SOP in meta brief |
| Program not closed until R01–R10 DONE; R11–R14 DONE or DEFERRED with date | Matrix in master roadmap |
| New operator capability words → same session brief batch or **INTENT GAP** flag | `hot.md` + session summary |
| Live lp never auto-skip until Wave 4 + operator GO | Program invariant in master roadmap |

Capability matrix (abbreviated):

| R## | Capability | Wave | Status |
|-----|------------|------|--------|
| R01–R02 | Audit + prompt | 1 | DONE |
| R03–R05 | Registry, brief template, kb log-only | 2 | DONE |
| R06–R07, R09 | Promotion SOP, failure taxonomy, memory | 3 | DONE |
| R08 | kb/stash enforce (brain) | 3 | PARTIAL → APPLIED after 3b |
| R08b | PM/WC executors | 3b | STAGED |
| R10 | Master roadmap | meta | DONE |
| R11–R14 | Self-learn, lp warn, stash auto, bootstrap | 4–6 | OPEN |

Full matrix: master roadmap brief on prod.

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
| **Wave 1 report** | `cemini-prod:/opt/cemini/briefs/2026-05-31_cemini-knowledge-application-audit-report.md` |
| Gap JSON | `cemini-prod:/opt/cemini/briefs/artifacts/knowledge-audit-2026-05-31.json` |
| Wave 2 briefs (3) | `cemini-prod:/opt/cemini/briefs/2026-05-31_k89-wave2-*.md` |
| Wave 3 briefs (4) | `cemini-prod:/opt/cemini/briefs/2026-05-31_k89-wave3-*.md` |
| **Master roadmap (R## matrix)** | `cemini-prod:/opt/cemini/briefs/2026-05-31_k89-master-roadmap-cemini.md` |
| Wave 3b brief | `cemini-prod:/opt/cemini/briefs/2026-05-31_k89-wave3b-pm-executor-wiki-enforcement-cemini.md` |

Laptop copies: `briefs/` mirror (gitignored).

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

### What agents do and do not do [CONFIRMED — Wave 1 2026-05-31]

| Question | Answer |
|----------|--------|
| Self-learn (weights/rules from outcomes)? | **No** — RL retrain brief exists, not enabled; coach_analyzer has no verified write-back |
| Self-heal (failure detect + replan)? | **Minimal** — fail-open wiki timeout; KillSwitch halt; not arXiv 2605.06737 taxonomy |
| Remember across sessions? | **stash/kb on librarian** — prod MCP client wired (`stash_mcp_client.py`); auto-remember gated on `STASH_REMEMBER_ENABLED` |
| Apply wiki at build time? | **Inconsistent** — orchestrator hot path has no kb hook (Wave 2 fixes visibility) |

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
