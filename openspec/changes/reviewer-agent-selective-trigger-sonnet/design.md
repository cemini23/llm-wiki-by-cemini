## Context

The Cemini Conductor orchestrates tool calls across the trading stack (Polymarket, Kalshi, IBKR). Reviewer-agent v1 — prototyped in K37 — interposes a DeepSeek-R1 reviewer between `propose_call` and `execute_tool` on **every** call. This produces a 6.2× single-turn latency penalty (Apple arXiv 2604.27233v1) that is acceptable for multi-turn long-horizon sessions but unjustifiable for read-only lookups. The Conductor's orchestrator node is already the natural interception layer; the trigger-policy filter inserts there without touching the base agent or the reviewer model itself.

Current state: v1 reviewer always fires. No routing logic. No cost instrumentation. No audit fixture for characterising over-cautious refusals.

Stakeholders: Cemini trading session runtime; DeepSeek-R1 cost budget; K37 implementation sprint.

## Goals / Non-Goals

**Goals:**

- Introduce a declarative YAML policy evaluated at Conductor middleware that routes each tool call to one of three buckets: `always-review`, `review-on-uncertainty`, `skip-review`.
- Gate reviewer invocation at the middleware layer, leaving the reviewer model and base agent untouched.
- Emit per-session cost-ceiling telemetry (invocation count + estimated DeepSeek-R1 token cost) with a configurable monthly ceiling and alert threshold.
- Ship a harmfulness audit harness that runs a representative Polymarket trajectory sample and reports the over-cautious-refusal rate for the `always-review` bucket.

**Non-Goals:**

- GEPA prompt-optimization of the reviewer prompt (separate workstream; +1.5–2.8% gain is a Phase 2 ROI question).
- Replacing DeepSeek-V3 as base agent (model selection is frozen for this pilot).
- Cross-broker trajectory generalization beyond Polymarket (Kalshi/IBKR samples are out of scope for the audit harness pilot).
- Modifying the reviewer model's internal rubric or scoring logic.

## Decisions

### Decision 1: YAML policy file as the trigger contract

**Choice**: Declarative `reviewer_policy.yaml` listing tool-name sets for each bucket, plus a numeric `uncertainty_threshold` field.

**Rationale**: Operators can change routing without touching Python. The policy file is version-controlled alongside the Conductor config, not baked into middleware code. Alternative (enum annotations in tool descriptors) was rejected because it requires touching every tool definition and doesn't support threshold tuning at runtime.

**Fallback**: A missing or empty policy file silently degrades to v1 always-review, preserving backward compatibility.

### Decision 2: Confidence score sourced from base-agent output metadata

**Choice**: The `review-on-uncertainty` bucket checks a `confidence` field emitted by the base agent in its provisional call output. If the field is absent, the call defaults to `skip-review` (conservative: treat absence of uncertainty signal as confidence).

**Rationale**: Avoids a separate uncertainty-estimation model. DeepSeek-V3 already emits token-level logprobs that can be reduced to a scalar confidence proxy. Alternative (heuristic keyword matching on tool arguments) was rejected as too brittle for finance-domain tool surfaces.

### Decision 3: Cost telemetry as session-scoped counters, not persistent store

**Choice**: In-memory counters reset per session; a rolling monthly accumulator is written to a lightweight local file (e.g., `~/.cemini/reviewer_cost.json`).

**Rationale**: Session counters are cheap and always accurate. The monthly accumulator covers the cost-ceiling alert use case without needing a database. Alternative (full observability pipeline) is over-engineered for the pilot stage.

### Decision 4: Audit harness as a standalone script, not integrated test

**Choice**: `scripts/reviewer_audit.py` consuming a pre-recorded Polymarket trajectory sample (JSON fixture), running each call through the trigger-policy and reviewer, outputting helpfulness/harmfulness metrics.

**Rationale**: Decoupled from the live Conductor so it can run offline against a frozen fixture. Makes the audit reproducible. Alternative (live integration test against Polymarket sandbox) introduces network dependency and nondeterminism.

## Risks / Trade-offs

- **Confidence signal reliability** → Base agent may emit unreliable or absent confidence scores for some tool surfaces. Mitigation: default-to-skip-review on absence; monitor `review-on-uncertainty` miss rate in telemetry.
- **Policy file drift** → As new tools are added, the YAML bucket lists go stale. Mitigation: add a lint step that warns on tool names present in Conductor but absent from all three buckets.
- **Harmfulness audit fixture staleness** → A frozen Polymarket trajectory sample becomes unrepresentative as market conditions change. Mitigation: document fixture vintage; re-record quarterly.
- **Monthly cost-ceiling accuracy** → Token-cost estimate uses a static price-per-token constant. If DeepSeek-R1 pricing changes, estimates drift. Mitigation: make price constant a config field; emit a "estimated, verify against invoice" disclaimer in telemetry output.

## Migration Plan

1. Deploy `reviewer_policy.yaml` with all existing tool calls mapped (write a migration helper that generates the YAML from Conductor tool registry, defaulting everything to `always-review`).
2. Update Conductor middleware to load the policy file and evaluate it before the reviewer stage. If file is absent, log a warning and continue with always-review.
3. Enable cost telemetry; let it accumulate for one week before setting a ceiling threshold.
4. Run `scripts/reviewer_audit.py` against the Polymarket fixture; review harmfulness report before promoting the selective-trigger policy to production traffic.
5. Rollback: remove the policy file → Conductor reverts to v1 always-review behavior automatically (no code change needed).

## Open Questions

1. **Confidence threshold calibration**: what numeric threshold maps to "base agent is uncertain" on Cemini's finance tool surfaces? Needs empirical calibration on recorded trajectories before setting the default.
2. **Monthly ceiling value**: what is the acceptable DeepSeek-R1 spend ceiling per month for the reviewer? Cost model depends on trigger rate, which depends on traffic — needs one week of telemetry data before setting.
3. **Fixture curation**: who owns the Polymarket trajectory sample for the audit harness? Needs a human-reviewed slice of trajectories with known-correct outcomes to score helpfulness/harmfulness accurately.
