## 1. Trigger-policy middleware

- [x] 1.1 Create `conductor/reviewer/trigger_policy.py` with a `classify(tool_name, tool_args, policy, base_agent_confidence) -> Bucket` function returning one of `Bucket.ALWAYS_REVIEW`, `Bucket.REVIEW_ON_UNCERTAINTY`, `Bucket.SKIP_REVIEW`  *(landed 2026-05-13; `Bucket`/`Policy`/`ToolEntry` dataclasses; pure function, no I/O)*
- [x] 1.2 Implement the three bucket-routing rules per spec Requirements 1-3 (side-effecting → always; read-only → skip; unclassified → always; confidence-missing → escalate)  *(landed 2026-05-13; 4 rules + misconfig guard for ROU-without-threshold)*
- [ ] 1.3 Wire the classifier into Conductor's pre-reviewer middleware stage behind a `reviewer_v2_enabled` feature flag (default false)  *(deferred to Sprint 2; depends on Task 2.x policy YAML loader + location decision for production conductor at `/opt/cemini/conductor/`)*
- [x] 1.4 Add unit tests covering all 6 scenarios from the trigger-policy spec requirements  *(landed 2026-05-13; `test_trigger_policy.py` — 20 tests pass: 14 scenario tests covering all 6 scenarios incl. boundary cases + 6 defensive invariants; never-returns-ROU, args-no-op, ROU-without-threshold-escalates, empty-policy-fallback, enum-yaml-round-trip)*

## 2. Declarative policy file

- [x] 2.1 Define the YAML policy-file schema: top-level `tools` map with `bucket`, `uncertainty_threshold` (optional), and `notes` (optional) per tool  *(landed 2026-05-13; `policy_loader.py` validates schema; rejects unknown fields, non-string keys, missing required `bucket`, invalid bucket values, ROU without threshold, threshold ∉ [0,1], non-numeric thresholds incl. bool, non-string notes)*
- [x] 2.2 Author `conductor/reviewer/policy.yaml` with default classifications for current Polymarket tool surfaces (place_order, withdraw, close_position, cancel_order → always-review; get_price, get_orderbook, get_news → skip-review; remainder → review-on-uncertainty with threshold 0.7)  *(landed 2026-05-13; 8 tools enumerated with notes; bundled policy passes load + lint integration test)*
- [x] 2.3 Add a lint pass that warns when a tool matching side-effecting naming patterns (`place_*`, `withdraw_*`, `cancel_*`, `close_*`) is classified as `skip-review`  *(landed 2026-05-13; `lint_policy()` returns list of warning strings; non-fatal; 6 lint tests pass incl. all 4 patterns + 3 negative cases)*
- [x] 2.4 Implement load-on-startup behavior: parse error → fail-closed; absent file → fail-open to v1 always-review with single startup warning  *(landed 2026-05-13; `load_policy()` raises `PolicyParseError` on schema/YAML violations, `FileNotFoundError` on missing file; `load_policy_or_default()` swallows missing-file + emits single WARNING + returns empty Policy; 2 fail-closed tests + 1 fail-open test pass)*

## 3. Cost-ceiling telemetry

- [x] 3.1 Create `conductor/reviewer/cost_telemetry.py` with a `record(tool_name, bucket, input_tokens, output_tokens)` function writing structured log entries (async/buffered)  *(landed 2026-05-13; `TelemetryWriter` class — buffered NDJSON, `threading.Lock`-guarded, context-manager protocol, auto-flush at `buffer_size` threshold; default path `~/.cemini/reviewer_telemetry.ndjson`; module-level `record()` one-shot convenience wrapper; 11 tests pass incl. NDJSON compact-format invariant, append-no-overwrite, parent-dir creation, buffer-threshold semantics)*
- [x] 3.2 Implement the daily aggregator that produces per-tool roll-ups of review count and total tokens  *(landed 2026-05-13; `cost_aggregator.aggregate(log_path) -> Dict` — pure NDJSON reader; sorted deterministic per-tool dict for diff-friendly output; period bounds + workspace-wide total; malformed-JSON / missing-tool-field raise `ValueError` with line number; missing log file yields zero report — fresh deployments aren't errors; 14 tests pass)*
- [x] 3.3 Apply the configured DeepSeek-R1 per-token price to compute estimated monthly spend; emit as a dashboard-ready JSON artifact  *(landed 2026-05-13; DeepSeek-R1 2025-Q1 public pricing baked in as defaults — $0.55/M input, $2.19/M output — operator-overridable via kwargs or CLI flags; `monthly_estimate_usd` extrapolates observed cost to 30-day window with 1-hour duration floor to avoid inflating estimates from short bursts; `pricing` block in every report surfaces active prices + source string so dashboards can audit; CLI entry `python -m conductor.reviewer.cost_aggregator <log> [-o out.json]` with output-dir auto-creation; smoke-test verified end-to-end: 4 records → 3-tool roll-up → $0.004 observed → $2.89 monthly extrapolation correctly applies 720x scaling via 1hr floor)*

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
