# Status: DEFERRED — Pending Polymarket integration

**Decision date:** 2026-05-13
**Decision by:** Cemini operator (user)
**Closed phase:** Phase-2 Sprints 1+2+3+4 LANDED (105/105 tests pass)
**Deferred phase:** Sprint 5 (migration / rollout) + Task 1.3 (middleware wiring)

## Why deferred

This OpenSpec change specifies a reviewer-agent that gates the **XSP killer**
EMS tool surface — Robinhood `place_order` / `close_position` / `cancel_order`
on XSP long-call lanes A/B, plus `notify_operator` alerts and read-only
regime/quote tools (`get_regime_status`, `get_playbook_snapshot`, `get_price`).

The current production Conductor at `cemini-librarian:/opt/cemini/conductor/`
implements a **Q&A routing pipeline** (taxonomy → pool → cascade → tools →
response) whose `ToolOrchestrator.orchestrate()` dispatches exactly two
tools:

- `kb_search` — knowledge-base lookup (read-only)
- `stash_recall` — memory retrieval (read-only)

**No XSP EMS order-gating path exists in production reviewer wiring yet.** The bundled
`conductor/reviewer/policy.yaml` describes the XSP/Robinhood surface the
co-primary xsp-killer bot targets; Sprint 5 middleware is not live.
classifies every existing tool as `skip-review` → the reviewer fires zero
times in production → dead infrastructure plus a confidence trap (devs may
infer XSP orders are gated when no gate path is active).

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

## Vocabulary: Prebind Assurance (K155)

**Prebind Assurance** (CAGE-1, arXiv:2607.03510) — prove an agentic action is controlled **before** it becomes binding, effective, or operationally consequential. Actions may be admitted, held, narrowed, refused, escalated, quarantined, or made non-effective pre-consequence.

**Cemini mapping (K37 reviewer, pre-prod):**

| CAGE-1 posture | Reviewer implementation |
|----------------|-------------------------|
| Hold/refuse before bind | `refuse_only` on `place_order` / `close_position` / `cancel_order` — no `revise()` of order args |
| Prove control pre-LLM | `conductor.reviewer.lane_contract.validate_provisional_call()` — deterministic contract violations fail **before** the LLM reviewer runs |
| Policy gate | `trigger_policy` → `always-review` bucket on side-effecting EMS tools |
| Outer-loop accountability | Pair with Addy **Verdict** + **Answerability** — operator owns ship/block/redirect and can explain why (`@sources/substack-rss-addy-osmani-2026-07-09-own-the-outer-loop.md`) |

Cross-walk to passive-injection manifest slots: `wiki/concepts/reviewer-passive-injection-corpus.md` § CAGE-1 cross-walk.

## Re-open trigger

This change re-opens when an **XSP EMS integration** change lands in
`openspec/changes/` and a server-Claude install brief stages the
reviewer-agent into `/opt/cemini/conductor/reviewer/`. At that point:

1. Update `policy.yaml` to enumerate the actual Robinhood/EMS tool surface
   that landed (verify against `ToolOrchestrator._invoke` / EMS router
   dispatch at `/opt/cemini/conductor/tools.py` or EMS adapter table)
2. Rebuild passive-injection bundle: `bash scripts/build_reviewer_context.sh`
3. Enforce **lane_id contract** on all provisional order tools
   (`conductor.reviewer.lane_contract.validate_provisional_call`; hub:
   `wiki/concepts/reviewer-passive-injection-corpus.md` § Pre-prod gates)
4. Wire feature flag + middleware hook into `ToolOrchestrator.orchestrate`
   per Task 1.3
5. Generate ≥50 held-out correct trajectories from the new tool surface
6. Run Sprint 5 sequence (staging soak → audit → promote)

## Lessons recorded

The methodology gap surfaced by this exercise — OpenSpec produces
deterministic well-tested code but does NOT validate that the spec was
production-aligned — is captured in `LESSONS.md` 2026-05-13 entry
"OpenSpec spec-vs-production-alignment gap."

## Pointer to pilot deliverables

* Reviewer-agent v2 source: `conductor/reviewer/`
* Comparative bundle (Sonnet 4.6 vs Opus 4.7): `openspec/changes/reviewer-agent-selective-trigger-sonnet/`
* This (Opus 4.7) bundle remains the canonical spec for re-open work.
