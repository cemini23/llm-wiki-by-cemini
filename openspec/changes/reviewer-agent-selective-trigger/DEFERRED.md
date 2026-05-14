# Status: DEFERRED — Pending Polymarket integration

**Decision date:** 2026-05-13
**Decision by:** Cemini operator (user)
**Closed phase:** Phase-2 Sprints 1+2+3+4 LANDED (105/105 tests pass)
**Deferred phase:** Sprint 5 (migration / rollout) + Task 1.3 (middleware wiring)

## Why deferred

This OpenSpec change specifies a reviewer-agent that gates the Polymarket
trading tool surface — `place_order`, `withdraw`, `close_position`,
`cancel_order`, `submit_research_query`, plus read-only quote tools.

The current production Conductor at `cemini-librarian:/opt/cemini/conductor/`
implements a **Q&A routing pipeline** (taxonomy → pool → cascade → tools →
response) whose `ToolOrchestrator.orchestrate()` dispatches exactly two
tools:

- `kb_search` — knowledge-base lookup (read-only)
- `stash_recall` — memory retrieval (read-only)

**No Polymarket tool surface exists in production yet.** The bundled
`conductor/reviewer/policy.yaml` describes a hypothetical tool surface that
hasn't been built. Deploying Sprint 5 today would land middleware that
classifies every existing tool as `skip-review` → the reviewer fires zero
times in production → dead infrastructure plus a confidence trap (devs may
infer trading is gated when no gate path is active).

## What remains valid

* **Sprints 1-4 code at `conductor/reviewer/`** — fully tested, spec-validated.
  Stays in the laptop workspace as a pilot deliverable. NOT shipped to
  `/opt/cemini/`.
* **OpenSpec pilot measurement** — Phase-1 + Phase-2 succeeded at the
  load-bearing objective (Opus + Sonnet bundles both validated; 105 tests
  pass end-to-end against the locked spec). The pilot proved spec-driven
  development is viable in this workspace.
* **The architectural design** — three-bucket gating, declarative YAML
  policy, NDJSON telemetry, harmfulness-audit harness with ≥50-trajectory
  validation gate. All re-usable when the Polymarket integration lands.

## What's blocked

* **Sprint 5 tasks (5.1-5.5)** — feature flag, staging soak, cost
  monitoring, production promotion, archive. All require a real
  production tool surface to gate.
* **Task 1.3** — Conductor middleware wiring. Same blocker.

## Re-open trigger

This change re-opens when a Polymarket-integration change lands in
`openspec/changes/` and a server-Claude install brief stages the
reviewer-agent into `/opt/cemini/conductor/reviewer/`. At that point:

1. Update `policy.yaml` to enumerate the actual Polymarket tool surface
   that landed (verify against the actual `ToolOrchestrator._invoke`
   dispatch table at `/opt/cemini/conductor/tools.py`)
2. Wire feature flag + middleware hook into `ToolOrchestrator.orchestrate`
   per Task 1.3
3. Generate ≥50 held-out correct trajectories from the new tool surface
4. Run Sprint 5 sequence (staging soak → audit → promote)

## Lessons recorded

The methodology gap surfaced by this exercise — OpenSpec produces
deterministic well-tested code but does NOT validate that the spec was
production-aligned — is captured in `LESSONS.md` 2026-05-13 entry
"OpenSpec spec-vs-production-alignment gap."

## Pointer to pilot deliverables

* Reviewer-agent v2 source: `conductor/reviewer/`
* Comparative bundle (Sonnet 4.6 vs Opus 4.7): `openspec/changes/reviewer-agent-selective-trigger-sonnet/`
* This (Opus 4.7) bundle remains the canonical spec for re-open work.
