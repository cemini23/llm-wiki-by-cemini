## 1. Policy File Schema

- [ ] 1.1 Define `reviewer_policy.yaml` schema: `always_review`, `review_on_uncertainty`, `skip_review` lists plus `uncertainty_threshold` (float 0.0–1.0) and `monthly_ceiling_usd` (float) fields
- [ ] 1.2 Write YAML schema validation (pydantic model or equivalent) that rejects malformed policy files with a clear error message
- [ ] 1.3 Create a migration helper script that reads the Conductor tool registry and generates a starter `reviewer_policy.yaml` with all tools defaulting to `always_review`
- [ ] 1.4 Add a lint step that warns when a tool name present in the Conductor tool registry is absent from all three bucket lists

## 2. Conductor Middleware — Trigger-Policy Evaluation

- [ ] 2.1 Add a `TriggerPolicyMiddleware` class (or equivalent function) to `conductor/mcp_server.py` that loads `reviewer_policy.yaml` at startup
- [ ] 2.2 Implement `evaluate_trigger(tool_name, call_metadata) -> Bucket` returning one of `ALWAYS_REVIEW | REVIEW_ON_UNCERTAINTY | SKIP_REVIEW`
- [ ] 2.3 Handle unclassified tool names: default to `ALWAYS_REVIEW` and emit a warning log entry with the tool name
- [ ] 2.4 Implement graceful degradation: if policy file is missing or empty, log a warning and behave as v1 always-review
- [ ] 2.5 Wire middleware into Conductor's pre-reviewer hook so `TriggerPolicyMiddleware.evaluate_trigger()` is called before `reviewer_agent.review()`

## 3. Uncertainty-Gated Routing

- [ ] 3.1 Parse the `confidence` field from base-agent provisional call output metadata; handle absent field by routing to `SKIP_REVIEW` with a debug log entry
- [ ] 3.2 Implement threshold comparison: invoke reviewer iff `confidence < uncertainty_threshold`; document the strict-less-than semantics in code comment

## 4. Cost-Ceiling Telemetry

- [ ] 4.1 Create `CostTelemetry` session-scoped class with `invocation_count` and `estimated_cost_usd` in-memory accumulators
- [ ] 4.2 Implement `record_invocation(token_count)` that increments counters using a configurable price-per-token constant (make constant a config field, not hardcoded)
- [ ] 4.3 Implement monthly accumulator read/write against `~/.cemini/reviewer_cost.json`; create file with empty monthly record if absent
- [ ] 4.4 Implement cost-ceiling alert: compare rolling monthly total + current session cost against `monthly_ceiling_usd`; emit alert to session log when exceeded
- [ ] 4.5 Call `CostTelemetry.flush()` at session end to append session totals to the monthly accumulator

## 5. Harmfulness Audit Harness

- [ ] 5.1 Create `scripts/reviewer_audit.py` with CLI interface: `--fixture <path>` (required), `--output-dir <path>` (optional, defaults to `reports/`)
- [ ] 5.2 Implement fixture loader that reads a JSON trajectory file and yields individual tool calls with their expected outcomes
- [ ] 5.3 Stub all external broker API calls (Polymarket, Kalshi, IBKR) in offline mode; raise error if live call is attempted
- [ ] 5.4 Run each call through the `always-review` bucket logic using the production trigger-policy middleware in test mode
- [ ] 5.5 Compute helpfulness rate, harmfulness rate, and over-cautious-refusal count from reviewer decisions vs expected outcomes
- [ ] 5.6 Emit human-readable report to stdout and write machine-readable JSON to `reports/reviewer_audit_<timestamp>.json`
- [ ] 5.7 Record a representative Polymarket trajectory fixture (`trajectories/polymarket_sample.json`) with known-correct outcomes for use by the harness

## 6. Validation & Integration

- [ ] 6.1 Write unit tests for `TriggerPolicyMiddleware.evaluate_trigger()` covering all three buckets, the unclassified-tool default, and the missing-file fallback
- [ ] 6.2 Write unit tests for `CostTelemetry`: accumulation, monthly file creation, ceiling alert trigger
- [ ] 6.3 Run `scripts/reviewer_audit.py` against `trajectories/polymarket_sample.json`; review harmfulness report and confirm over-cautious-refusal rate is within acceptable range before promoting to production
- [ ] 6.4 Verify `reviewer_policy.yaml` lint step fires correctly when a new tool is added to the Conductor registry without a bucket assignment
- [ ] 6.5 Smoke-test the full Conductor flow with the policy file present (verify always-review calls go to reviewer, skip-review calls bypass it, missing-file falls back gracefully)
