## ADDED Requirements

### Requirement: Trigger-policy classification

The system SHALL classify every provisional tool call into exactly one of three buckets — `always-review`, `review-on-uncertainty`, or `skip-review` — before any reviewer-agent invocation. Classification SHALL be deterministic given the tool name, the call arguments, and the active policy file.

#### Scenario: Side-effecting tool always reviewed

- **WHEN** Conductor receives a provisional call to `place_order(...)`, `withdraw(...)`, `close_position(...)`, or `cancel_order(...)`
- **THEN** the trigger-policy middleware MUST classify the call as `always-review`
- **AND** the reviewer-agent MUST be invoked before the call is dispatched to the underlying tool

#### Scenario: Read-only tool skipped

- **WHEN** Conductor receives a provisional call to `get_price(...)`, `get_orderbook(...)`, or `get_news(...)`
- **THEN** the trigger-policy middleware MUST classify the call as `skip-review`
- **AND** the call MUST be dispatched directly to the underlying tool without reviewer-agent invocation

#### Scenario: Unclassified tool defaults to always-review

- **WHEN** Conductor receives a provisional call to a tool not enumerated in the active policy file
- **THEN** the trigger-policy middleware MUST classify the call as `always-review`
- **AND** the reviewer-agent MUST be invoked (safe default — never silently skip an unknown tool)

### Requirement: Uncertainty-threshold gating

The system SHALL support a `review-on-uncertainty` bucket that escalates to the reviewer-agent only when the base agent's confidence score is below a configured threshold. The threshold SHALL be configurable per-tool in the policy file.

#### Scenario: Confidence above threshold skips review

- **WHEN** the trigger-policy middleware classifies a call as `review-on-uncertainty` AND the base agent's confidence is ≥ the per-tool threshold
- **THEN** the call MUST be dispatched directly without reviewer-agent invocation

#### Scenario: Confidence below threshold triggers review

- **WHEN** the trigger-policy middleware classifies a call as `review-on-uncertainty` AND the base agent's confidence is < the per-tool threshold
- **THEN** the reviewer-agent MUST be invoked before the call is dispatched

#### Scenario: Missing confidence score is treated as low

- **WHEN** the trigger-policy middleware classifies a call as `review-on-uncertainty` AND the base agent did not emit a confidence score
- **THEN** the call MUST be treated as below-threshold (escalate to reviewer-agent)

### Requirement: Declarative policy file

The policy SHALL be declarative data (YAML or equivalent), not code. The policy file SHALL list tool surfaces and their bucket assignment, plus per-tool uncertainty thresholds where applicable.

#### Scenario: Policy loaded at startup

- **WHEN** Conductor starts
- **THEN** the trigger-policy middleware MUST load the policy file from a configured path
- **AND** parse failures MUST cause Conductor startup to abort (fail-closed)

#### Scenario: Policy absent falls back to v1 behavior

- **WHEN** the policy file does not exist at the configured path
- **THEN** the trigger-policy middleware MUST default every call to `always-review`
- **AND** the system MUST log a single startup warning indicating fallback to v1 always-review behavior

### Requirement: Cost-ceiling telemetry

The system SHALL emit telemetry that allows monthly DeepSeek-R1 reviewer spend to be estimated from observed trigger-gated review volume.

#### Scenario: Per-call telemetry recorded

- **WHEN** the reviewer-agent is invoked for any provisional call
- **THEN** the system MUST record the tool name, the trigger bucket, the input-token count, and the output-token count to a structured log

#### Scenario: Monthly aggregation produced

- **WHEN** the cost-telemetry aggregator runs (daily or on-demand)
- **THEN** the system MUST produce a per-tool roll-up of review count and total tokens
- **AND** apply the configured DeepSeek-R1 per-token price to compute estimated monthly spend

### Requirement: Harmfulness audit harness

The system SHALL provide a harness that runs the reviewer-agent on a sample of trajectories where the v1 base agent's output was independently verified correct, and characterize any degradation introduced by reviewer intervention.

#### Scenario: Audit harness runs on sample

- **WHEN** the harness is invoked with a directory of trajectory JSON files known to be correct base-agent outputs
- **THEN** the system MUST replay each trajectory's tool call through the trigger-policy + reviewer stack
- **AND** produce a per-trajectory verdict: `unchanged`, `revised-still-correct`, `revised-now-incorrect`, or `refused`

#### Scenario: Harmfulness rate reported

- **WHEN** the audit harness finishes
- **THEN** the system MUST report the harmfulness rate as (count of `revised-now-incorrect` + count of `refused`) / total trajectories
- **AND** the system MUST report the over-cautious-refusal sub-rate separately
