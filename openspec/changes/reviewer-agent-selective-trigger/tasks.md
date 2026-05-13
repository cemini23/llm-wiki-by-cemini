## 1. Trigger-policy middleware

- [ ] 1.1 Create `conductor/reviewer/trigger_policy.py` with a `classify(tool_name, tool_args, policy, base_agent_confidence) -> Bucket` function returning one of `Bucket.ALWAYS_REVIEW`, `Bucket.REVIEW_ON_UNCERTAINTY`, `Bucket.SKIP_REVIEW`
- [ ] 1.2 Implement the three bucket-routing rules per spec Requirements 1-3 (side-effecting → always; read-only → skip; unclassified → always; confidence-missing → escalate)
- [ ] 1.3 Wire the classifier into Conductor's pre-reviewer middleware stage behind a `reviewer_v2_enabled` feature flag (default false)
- [ ] 1.4 Add unit tests covering all 6 scenarios from the trigger-policy spec requirements

## 2. Declarative policy file

- [ ] 2.1 Define the YAML policy-file schema: top-level `tools` map with `bucket`, `uncertainty_threshold` (optional), and `notes` (optional) per tool
- [ ] 2.2 Author `conductor/reviewer/policy.yaml` with default classifications for current Polymarket tool surfaces (place_order, withdraw, close_position, cancel_order → always-review; get_price, get_orderbook, get_news → skip-review; remainder → review-on-uncertainty with threshold 0.7)
- [ ] 2.3 Add a lint pass that warns when a tool matching side-effecting naming patterns (`place_*`, `withdraw_*`, `cancel_*`, `close_*`) is classified as `skip-review`
- [ ] 2.4 Implement load-on-startup behavior: parse error → fail-closed; absent file → fail-open to v1 always-review with single startup warning

## 3. Cost-ceiling telemetry

- [ ] 3.1 Create `conductor/reviewer/cost_telemetry.py` with a `record(tool_name, bucket, input_tokens, output_tokens)` function writing structured log entries (async/buffered)
- [ ] 3.2 Implement the daily aggregator that produces per-tool roll-ups of review count and total tokens
- [ ] 3.3 Apply the configured DeepSeek-R1 per-token price to compute estimated monthly spend; emit as a dashboard-ready JSON artifact

## 4. Harmfulness audit harness

- [ ] 4.1 Create `conductor/reviewer/harmfulness_audit.py` as an offline CLI tool taking a directory of trajectory JSON files
- [ ] 4.2 For each trajectory: replay the tool call through trigger-policy + reviewer; classify outcome as `unchanged`, `revised-still-correct`, `revised-now-incorrect`, or `refused`
- [ ] 4.3 Emit per-trajectory verdicts and an aggregate report showing harmfulness rate + over-cautious-refusal sub-rate
- [ ] 4.4 Validation gate: harness reports harmfulness rate ≤ v1 baseline on ≥50 held-out correct trajectories before promotion

## 5. Migration + rollout

- [ ] 5.1 Land all of (1)-(4) behind the `reviewer_v2_enabled` feature flag
- [ ] 5.2 Flip flag to `true` in staging Cemini; run harmfulness audit; soak for 7 days
- [ ] 5.3 Monitor cost-telemetry monthly-spend estimate vs pre-rollout forecast; abort and rollback if delta > 30%
- [ ] 5.4 Promote to production; document rollback procedure (flip flag to false) in operational runbook
- [ ] 5.5 Archive this change via `openspec archive reviewer-agent-selective-trigger` after production promotion
