---
title: Reviewer passive-injection corpus — K37 context bundle
type: concept
tags: [concept, conductor, reviewer-agent, passive-injection, k37, corpus, xsp]
keywords: [reviewer-agent, context-bundle, passive-injection, conductor-reviewer, xsp, robinhood, ems, harmfulness]
related:
  - concepts/reviewer-agent-inference-time-feedback.md
  - concepts/interaction-native-knowledge-harness.md
  - concepts/ems-execution-security-gaps.md
  - concepts/conductor-orchestrator.md
  - concepts/cemini-knowledge-application-architecture.md
  - concepts/context-fractured-decomposition-attacks.md
  - concepts/sae-execution-contract.md
  - concepts/mitre-atlas-taxonomy.md
  - concepts/rlhf-critic-bias.md
  - concepts/production-trading-blind-spots.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/macro-weather-regime.md
  - concepts/active-project-research-routing.md
  - "@cybersecurity-wiki/concepts/agent-runtime-guardrails.md"
  - "@cybersecurity-wiki/concepts/intent-governed-tool-authorization.md"
  - "@cybersecurity-wiki/concepts/mcp-execution-control-invariants.md"
  - concepts/kelly-sizing-quarter.md
  - sources/arxiv-cage1-enterprise-governance-2607.03510-2026-07-10.md
maturity: validated
created: 2026-07-08
updated: 2026-07-10
---

## Relations

- @concepts/reviewer-agent-inference-time-feedback.md — K37 reviewer pattern and trigger-policy design
- @concepts/interaction-native-knowledge-harness.md — passive injection vs query-time wiki-walk
- @concepts/ems-execution-security-gaps.md — P0 execution bypass catalog
- @concepts/conductor-orchestrator.md — orchestration layer; reviewer slots before `execute_tool`
- @concepts/cemini-knowledge-application-architecture.md — binding knowledge for prod gates
- @concepts/context-fractured-decomposition-attacks.md — cross-session provenance gap
- @concepts/sae-execution-contract.md — ALLOW/LIMIT/BLOCK at execution boundary
- @concepts/mitre-atlas-taxonomy.md — agent tool-invocation threat surface
- @concepts/rlhf-critic-bias.md — over-cautious refusal as harmfulness mode
- @concepts/production-trading-blind-spots.md — infra failures mistaken for alpha loss
- @concepts/xsp-lane-trading-framework.md — XSP killer lane map + Lane A/B rules
- @concepts/macro-weather-regime.md — Macro Weather for portfolio Kelly; XSP dip lanes are explicit exception
- @concepts/active-project-research-routing.md — xsp-killer co-primary brief routing
- @cybersecurity-wiki/concepts/agent-runtime-guardrails.md — tool-chain failure modes (cross-wiki corpus)
- @cybersecurity-wiki/concepts/intent-governed-tool-authorization.md — intent–tool consistency (cross-wiki corpus)
- @cybersecurity-wiki/concepts/mcp-execution-control-invariants.md — execution-control invariants (cross-wiki corpus)
- @concepts/kelly-sizing-quarter.md — fractional Kelly + hard position caps
- @sources/arxiv-cage1-enterprise-governance-2607.03510-2026-07-10.md — CAGE-1 Prebind Assurance vocabulary (K155)

## Raw Concept

Operator request (2026-07-08): curate a **tight reviewer corpus** for K37 `conductor/reviewer/` Phase 0 pilot — passive injection, not federation wiki or kb_search fan-out. **Retargeted same day** from Polymarket to **XSP killer bot** (Robinhood long-call lanes A/B). Authored on laptop; prod middleware wiring remains DEFERRED per `openspec/changes/reviewer-agent-selective-trigger/DEFERRED.md`.

## Narrative

### What this is

A **manifest-driven context bundle** for the K37 reviewer-agent, tuned for the **XSP killer bot** — Robinhood XSP long-call lanes A/B via EMS. At invocation time the reviewer receives a fixed, versioned markdown buffer compiled from binding wiki pages plus `policy.yaml` verbatim. Passive injection, not kb_search fan-out.

### Artifact locations

| Artifact | Path |
|----------|------|
| Manifest (source list) | `conductor/reviewer/corpus/manifest.yaml` |
| Build script | `conductor/reviewer/corpus/build_context_bundle.py` |
| Shell entry | `scripts/build_reviewer_context.sh` |
| Generated bundle | `conductor/reviewer/corpus/context_bundle.md` |
| Trigger policy (verbatim in bundle) | `conductor/reviewer/policy.yaml` |

Rebuild after any manifest or source page edit:

```bash
bash scripts/build_reviewer_context.sh
```

### Corpus entries (manifest v1 — XSP)

| ID | Source | Why reviewer needs it |
|----|--------|------------------------|
| `trigger_policy` | `policy.yaml` | EMS/Robinhood tool buckets (place_order, close_position, regime reads) |
| `reviewer_rubric` | @concepts/reviewer-agent-inference-time-feedback.md | Helpfulness/harmfulness + selective trigger |
| `ems_p0_gaps` | @concepts/ems-execution-security-gaps.md | Router bypass, PositionGate, RBAC fail-open |
| `sae_contract` | @concepts/sae-execution-contract.md | ALLOW/LIMIT/BLOCK at execution boundary |
| `mitre_atlas_surface` | @concepts/mitre-atlas-taxonomy.md | Tool-poisoning / agent-invocation threats |
| `rlhf_critic_guardrail` | @concepts/rlhf-critic-bias.md | Refusal-as-harmfulness guardrail |
| `inkh_passive_injection` | @concepts/interaction-native-knowledge-harness.md | Why not kb_search |
| `prod_blind_spots` | @concepts/production-trading-blind-spots.md | Infra failure checklist |
| `xsp_lane_framework` | @concepts/xsp-lane-trading-framework.md | Lane A/B rules, -$75 stop, 10:30 ET cut, LEAPS hedge |
| `xsp_regime_gate` | @concepts/macro-weather-regime.md | Macro Weather context; **not** universal GREEN-only entry for XSP dip lanes |
| `kelly_sizing_caps` | @concepts/kelly-sizing-quarter.md | Fractional Kelly + hard per-position caps |
| `igac_intent_scope` | @cybersecurity-wiki/concepts/intent-governed-tool-authorization.md | Intent must justify side-effecting call |
| `mcp_execution_invariants` | @cybersecurity-wiki/concepts/mcp-execution-control-invariants.md | Eight execution-control invariants |
| `agent_guardrail_failure_modes` | @cybersecurity-wiki/concepts/agent-runtime-guardrails.md | Authority confusion + permission laundering |
| `cfd_provenance` | @concepts/context-fractured-decomposition-attacks.md | Cross-session artifact trust |

### Deployment boundary

| Surface | Owner | Status |
|---------|-------|--------|
| Corpus curation + bundle build | **OSINT WORKSPACE (laptop)** | **Active** |
| Runtime injection + middleware | **cemini-prod `/opt/cemini`** | **DEFERRED** — re-opens when XSP EMS order path is reviewer-wired |

Prod promotion ships `conductor/reviewer/` + compiled `context_bundle.md` via server-Claude brief when Robinhood XSP `place_order` / `close_position` traverse the gated EMS path.

### Pre-prod gates (lane_id contract)

**Blocker before Sprint 5 / prod wiring.** Side-effecting order tools must carry `lane_id` so the reviewer does not cross-apply lane rules or second-guess strategy.

| Requirement | Detail |
|-------------|--------|
| **Required field** | `lane_id` on `place_order`, `close_position`, `cancel_order` (aliases: `strategy_track`, `lane`) |
| **Allowed values** | `lane_a`, `lane_b`, `lane_c`, `lane_d`, `manual`, `smb_put_credit`, `hl_shadow` |
| **v1 automation** | Lane A: **close only**; Lane B: **alerts + manual entry**; C/D/SMB/HL: **not automated** |
| **Reviewer verdict** | `refuse_only` on orders — no `revise()` of strikes/qty/side |
| **Reviewer mandate** | Hard limits + automation posture + EMS — **not** edge, timing, alpha, or universal GREEN entry |
| **Code validator** | `conductor.reviewer.lane_contract.validate_provisional_call()` |
| **Policy source** | `conductor/reviewer/policy.yaml` → `lane_id_contract` block |

```python
from conductor.reviewer.lane_contract import validate_provisional_call

validate_provisional_call("close_position", {"lane_id": "lane_a", ...})
```

Deterministic contract violations (e.g. automated `place_order` on `lane_a`) fail **before** the LLM reviewer runs. The LLM reviewer handles semantic checks (lane hard limits, sizing caps, intent) for calls that pass the contract. **Regime is advisory context** — dip-buying lanes (esp. Lane B) may add risk in YELLOW/RED; reviewer must not refuse solely on non-GREEN.

See @concepts/xsp-lane-trading-framework.md — do **not** merge SMB put-credit rules into long-call lane YAML; `smb_put_credit` is a separate `lane_id`.

### Prebind Assurance (K155)

**Prebind Assurance** (CAGE-1) — prove an agentic action is controlled before it becomes binding or operationally consequential. In the K37 reviewer stack this is implemented as: (1) `validate_provisional_call()` holding/refusing contract violations **before** the LLM reviewer; (2) `refuse_only` verdict mode on order tools so the reviewer cannot silently revise strikes/qty/side into a binding EMS call; (3) `always-review` trigger bucket on side-effecting tools. Pair with Addy outer-loop **Verdict** (ship/block/redirect) and **Answerability** (explain why) — `@sources/substack-rss-addy-osmani-2026-07-09-own-the-outer-loop.md`.

### CAGE-1 cross-walk

Maps CAGE-1 enterprise governance dimensions to existing manifest entry IDs (no new bundle slots in v1):

| CAGE-1 dimension | Manifest ID(s) | Coverage in bundle |
|------------------|----------------|--------------------|
| **Authority** | `igac_intent_scope`, `agent_guardrail_failure_modes` | Intent must justify side-effecting call; authority confusion + permission laundering |
| **Policy enforcement** | `trigger_policy`, `sae_contract`, `reviewer_rubric` | Three-bucket gating; ALLOW/LIMIT/BLOCK at execution boundary; helpfulness/harmfulness rubric |
| **Tool safety** | `ems_p0_gaps`, `mcp_execution_invariants`, `lane_id_contract` (policy.yaml) | P0 EMS bypass catalog; eight execution-control invariants; deterministic `validate_provisional_call` pre-LLM |
| **Auditability** | `mitre_atlas_surface`, `cfd_provenance` | Agent-invocation threat taxonomy; cross-session artifact provenance gap |

Secondary CAGE-1 dimensions (retrieval quality, memory integrity, human oversight, safe failure) partially covered by `cfd_provenance`, `prod_blind_spots`, and `notify_operator` always-review bucket — not dedicated manifest slots until XSP EMS wiring re-opens.

### What this is not

- Not Polymarket / CLOB tool semantics (PM bot is secondary per `active_project_brief_targets.yaml`)
- Not a ninth federation wiki
- Not kb_search retrieval
- Not live prod middleware (Phase 0 offline harness only)

## Snippets

> "Lane B: accumulate on dips — entries may target YELLOW/RED drawdown windows; reviewer must not refuse solely on non-GREEN regime."

> — @concepts/xsp-lane-trading-framework.md

> "Unknown tools default to `always-review` at classification time."

> — `conductor/reviewer/policy.yaml`
