## Context

K37 reviewer-agent v1 (per `@concepts/reviewer-agent-inference-time-feedback.md`) implements the Apple "Reinforced Agent" pattern: a reasoning-class reviewer (DeepSeek-R1) evaluates a base agent's (DeepSeek-V3) provisional tool calls before execution. The paper reports a 6.2× single-turn latency penalty and 2.4× multi-turn amortization when every call is reviewed.

Cemini's tool surface is heterogeneous. Polymarket trading sessions interleave high-volume read-only queries (price, orderbook, news lookups) with low-volume side-effecting calls (place_order, withdraw). Uniformly reviewing all of them inflates total session latency without proportional safety benefit — read-only calls cannot mutate account state and produce no irreversible side effects.

Constraints: this change ships into a Conductor instance that already routes tool calls through a middleware-style execution pipeline. The reviewer-agent v1 hook is a known insertion point. We are adding a pre-reviewer classifier, not modifying the reviewer itself.

## Goals / Non-Goals

**Goals:**

- Recover most of the single-turn latency floor on read-only tool calls
- Preserve full reviewer gating on all side-effecting calls (no safety regression)
- Make the policy declarative (data, not code) so changes do not require redeploys
- Produce cost telemetry that supports a monthly spend estimate at trigger-gated volume
- Produce a harmfulness audit harness that quantifies over-cautious refusals as a distinct sub-class of degradation

**Non-Goals:**

- GEPA prompt-optimization layer (separate change)
- Replacing DeepSeek-V3 as the base agent
- Cross-broker generalization beyond Polymarket
- Reviewer model selection experimentation (DeepSeek-R1 stays)

## Decisions

### Decision 1: Three buckets, not two

Chose three buckets (`always-review`, `review-on-uncertainty`, `skip-review`) over a binary (review / skip).

- **Why**: Some tool surfaces are not cleanly side-effecting (e.g., `submit_research_query` to an external paid API). A uncertainty-gated middle bucket lets the policy author defer the decision to runtime confidence rather than forcing every tool into review/skip.
- **Alternative considered**: Binary classifier with a separate "uncertainty escalation" layer. Rejected — folds two concerns into one cleaner policy.

### Decision 2: Declarative YAML policy, fail-closed parse errors, fail-open absence

Chose YAML policy file. Parse errors abort startup; absent file falls back to v1 always-review.

- **Why**: Parse errors mean the operator intended a policy and got it wrong — safest action is to refuse to start. Absent file means the operator hasn't authored a policy yet — safest action is to behave like v1 (always review). Distinguishing these two states by behavior is load-bearing.
- **Alternative considered**: Hardcoded policy in Python. Rejected — defeats the declarative-data goal.

### Decision 3: Unclassified tools default to always-review

Chose safe default (`always-review`) for tools not enumerated in the policy file.

- **Why**: Operator may add a new tool surface and forget to update the policy. Failing toward review is non-regressive vs v1. Failing toward skip would silently bypass safety for unknown tools.
- **Alternative considered**: Hard error on unclassified tools. Rejected — too brittle; new tools land before policies update.

### Decision 4: Confidence-missing treated as low

When the `review-on-uncertainty` bucket is hit but the base agent didn't emit a confidence score, treat as below-threshold (escalate).

- **Why**: Same safe-default principle as Decision 3.
- **Alternative considered**: Skip review when confidence is missing. Rejected — silently weakens gating.

### Decision 5: Harmfulness audit harness separate from runtime

The audit harness is an offline tool that replays held-out trajectories. It is not a runtime component.

- **Why**: Harmfulness measurement is a slow batch operation; coupling it to runtime would hurt latency without benefit. Replaying held-out correct trajectories gives a clean signal.
- **Alternative considered**: Online harmfulness sampling at runtime. Rejected — measurement cost on critical path is unjustified.

## Risks / Trade-offs

- **Risk**: Policy file authoring becomes a new operational burden. → **Mitigation**: Ship a default policy file covering known Cemini tool surfaces; document additions in `CLAUDE.md` operational notes.
- **Risk**: Trigger-policy bypass introduces a class of vulnerabilities (operator misconfigures a side-effecting tool as skip-review). → **Mitigation**: Lint pass on the policy file that warns when a tool name matching known side-effecting patterns (`place_*`, `withdraw_*`, `cancel_*`) is classified as `skip-review`.
- **Risk**: Confidence-score semantics drift between base-agent versions. → **Mitigation**: Document the confidence-score contract in the policy file format. If the contract drifts, the audit harness will surface the regression as increased harmfulness.
- **Risk**: Telemetry overhead on the critical path. → **Mitigation**: Telemetry writes are async / buffered; reviewer-agent invocation already dominates the latency budget for reviewed calls.
- **Trade-off**: Three buckets is more cognitive load than two; some operators may default everything to `always-review` defeating the change. → **Mitigation**: Default policy ships pre-populated for the common Cemini tool surfaces.

## Migration Plan

1. Land the trigger-policy middleware in Conductor under a feature flag (`reviewer_v2_enabled=false` default)
2. Author + commit a default policy file covering current Polymarket tool surfaces
3. Run the harmfulness audit harness on a held-out trajectory sample (≥50 trajectories); confirm harmfulness rate ≤ v1 baseline
4. Flip feature flag to `true` in staging Cemini
5. Soak in staging for 1 week; monitor cost-telemetry monthly-spend estimate vs forecast
6. Promote to production
7. **Rollback**: flip feature flag to `false`; the system reverts to v1 always-review behavior without code change

## Open Questions

1. Per-tool uncertainty thresholds: default value 0.7 — needs empirical calibration on a representative trajectory sample. Should the harmfulness audit harness sweep thresholds and produce a per-tool optimum?
2. Should the policy file support tool-argument-conditional bucket assignment (e.g., `get_news` with `topic=politics` could escalate while `topic=weather` skips)? Adds expressive power but complicates the YAML schema. Defer to a future iteration?
3. Cost-telemetry aggregation cadence: daily roll-up vs on-demand. Daily produces a stable dashboard; on-demand is cheaper but less predictable. Pick one for v2 and revisit?
