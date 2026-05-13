## Why

The K37 reviewer-agent v1 design (per `@concepts/reviewer-agent-inference-time-feedback.md`) reviews every provisional tool call, inheriting a 6.2× single-turn latency penalty from the source Apple paper. For Cemini's mixed workload (read-only quotes mixed with side-effecting orders), uniform review is wasteful on the read-only majority and tolerable only on the side-effecting minority. We need a **trigger filter** that gates review by call category before the reviewer is invoked, preserving the gating benefit on high-stakes calls while recovering most of the latency floor on routine ones. This is also the pilot capability for the OpenSpec spec-driven development workflow per `@briefs/2026-05-13_openspec-spec-driven-pilot.md`.

## What Changes

- Add a **trigger-policy middleware** stage to Conductor that classifies each provisional tool call into one of three buckets before reviewer-agent invocation: `always-review`, `review-on-uncertainty`, `skip-review`
- Author a **declarative trigger policy** (data, not code) listing which tool surfaces fall into each bucket — e.g., `place_order` → always-review, `get_price` → skip-review
- Add an **uncertainty threshold** parameter for the middle bucket: when the base agent's confidence is below threshold, escalate to the reviewer
- Add a **cost-ceiling telemetry** hook that estimates monthly DeepSeek-R1 spend from observed trigger-gated review volume
- Author a **harmfulness audit harness** that runs the reviewer on a held-out sample of correct base-agent trajectories and characterizes any degradation (over-cautious refusals vs false negatives)
- **NON-BREAKING**: v1 always-review behavior remains the default if the policy file is absent

## Capabilities

### New Capabilities

- `reviewer-agent-selective-trigger`: trigger-policy middleware that classifies provisional tool calls and routes them to (skip|review-on-uncertainty|always-review) buckets before reviewer-agent invocation, with cost-ceiling telemetry and harmfulness audit harness

### Modified Capabilities

(None — v1 reviewer-agent has no existing OpenSpec spec; v1 is wiki-documented only at `@concepts/reviewer-agent-inference-time-feedback.md`.)

## Impact

- **Affected code (anticipated)**:
  - `conductor/reviewer/` — new `trigger_policy.py` middleware module
  - `conductor/reviewer/policy.yaml` — declarative tool-class buckets (new file)
  - `conductor/reviewer/cost_telemetry.py` — DeepSeek-R1 monthly spend estimator (new file)
  - `conductor/reviewer/harmfulness_audit.py` — held-out trajectory audit harness (new file)
- **Affected APIs**:
  - Conductor MCP orchestrator gains a new pre-execute middleware hook (backward-compatible; no signature change for existing tool calls)
- **Affected dependencies**:
  - No new runtime deps; uses existing DeepSeek-R1 client + Conductor middleware machinery
- **Affected systems**:
  - DeepSeek-R1 spend pattern shifts from per-call to per-high-stakes-call (downward direction)
  - Tool-call latency distribution bimodal: skip-review calls return at base-agent latency; always-review calls retain v1 latency
- **Out-of-scope for this change**:
  - GEPA prompt-optimization layer (deferred to a separate change)
  - Cross-broker generalization beyond Polymarket (pilot scope limited)
  - Base model replacement (DeepSeek-V3 stays as base agent)
