## ADDED Requirements

### Requirement: Trigger-policy middleware evaluates each tool call before reviewer invocation
The Conductor middleware SHALL evaluate a declarative YAML trigger-policy file for every provisional tool call and route the call to exactly one of three buckets — `always-review`, `review-on-uncertainty`, or `skip-review` — before deciding whether to invoke the reviewer agent. The policy evaluation MUST complete before `reviewer_agent.review()` is called.

#### Scenario: Side-effecting call routed to always-review
- **WHEN** the base agent proposes a tool call whose name appears in the `always-review` list in `reviewer_policy.yaml`
- **THEN** the Conductor middleware MUST invoke the reviewer agent before executing the tool call
- **AND** the reviewer's approve/revise decision MUST be applied before execution proceeds

#### Scenario: Read-only call routed to skip-review
- **WHEN** the base agent proposes a tool call whose name appears in the `skip-review` list in `reviewer_policy.yaml`
- **THEN** the Conductor middleware MUST execute the tool call directly without invoking the reviewer agent
- **AND** no reviewer latency penalty SHALL be incurred

#### Scenario: Policy file absent — graceful degradation
- **WHEN** `reviewer_policy.yaml` is missing or empty
- **THEN** the Conductor middleware MUST log a warning and fall back to always-review behavior for all tool calls
- **AND** no exception or crash SHALL propagate to the calling session

### Requirement: Declarative YAML trigger-policy file defines bucket membership
The system SHALL support a `reviewer_policy.yaml` configuration file that declares three named lists — `always_review`, `review_on_uncertainty`, and `skip_review` — each containing zero or more tool-name strings, plus a numeric `uncertainty_threshold` field (0.0–1.0). Tool names MUST be kebab-case strings matching Conductor tool registry names exactly.

#### Scenario: Valid policy file loaded
- **WHEN** `reviewer_policy.yaml` exists and contains valid YAML with at least one non-empty bucket list
- **THEN** the Conductor middleware MUST load the policy at startup (or on first call after file change)
- **AND** all tool calls MUST be routed according to the declared bucket membership

#### Scenario: Tool name absent from all buckets
- **WHEN** a provisional tool call's name does not appear in any bucket list
- **THEN** the middleware MUST default to `always-review` for that call
- **AND** a warning MUST be emitted to the session log identifying the unclassified tool name

### Requirement: Uncertainty-gated review for low-confidence base-agent calls
The middleware SHALL invoke the reviewer agent for calls in the `review-on-uncertainty` bucket if and only if the base agent's provisional call output includes a `confidence` field whose numeric value is strictly less than the `uncertainty_threshold` configured in `reviewer_policy.yaml`. If the `confidence` field is absent, the call SHALL be treated as `skip-review`.

#### Scenario: Low-confidence call triggers review
- **WHEN** the base agent proposes a tool call in the `review_on_uncertainty` list
- **AND** the provisional call output includes `confidence: 0.6` and `uncertainty_threshold` is `0.75`
- **THEN** the middleware MUST invoke the reviewer agent before executing the call

#### Scenario: Absent confidence field skips review
- **WHEN** the base agent proposes a tool call in the `review_on_uncertainty` list
- **AND** the provisional call output does not include a `confidence` field
- **THEN** the middleware MUST skip the reviewer and execute the call directly
- **AND** a debug log entry MUST record that confidence was absent

### Requirement: Per-session cost-ceiling telemetry
The system SHALL maintain per-session in-memory counters tracking reviewer-agent invocation count and an estimated DeepSeek-R1 token cost for that session. At session end, the system MUST append the session totals to a rolling monthly accumulator file (`~/.cemini/reviewer_cost.json`). When the rolling monthly total exceeds a configurable `monthly_ceiling_usd` value, the system MUST emit a cost-ceiling alert to the session log.

#### Scenario: Session telemetry accumulates per invocation
- **WHEN** the middleware invokes the reviewer agent for a tool call
- **THEN** the session invocation counter MUST increment by 1
- **AND** the estimated token cost for that invocation MUST be added to the session cost accumulator

#### Scenario: Monthly ceiling alert fires
- **WHEN** the rolling monthly total from `reviewer_cost.json` plus the current session cost exceeds `monthly_ceiling_usd`
- **THEN** the system MUST emit a cost-ceiling alert message to the session log
- **AND** the alert MUST include the current estimated total and the configured ceiling

#### Scenario: Missing accumulator file
- **WHEN** `~/.cemini/reviewer_cost.json` does not exist at session start
- **THEN** the system MUST create it with an empty monthly record for the current month
- **AND** session telemetry MUST proceed normally without error

### Requirement: Harmfulness audit harness for always-review bucket
The system SHALL include a standalone audit script (`scripts/reviewer_audit.py`) that accepts a path to a pre-recorded trajectory fixture (JSON), runs each tool call through the trigger-policy middleware and reviewer agent in offline mode, and outputs a harmfulness report including: total calls evaluated, helpfulness rate (fraction of base-agent errors corrected), harmfulness rate (fraction of correct outputs degraded), and over-cautious-refusal count.

#### Scenario: Audit harness runs against Polymarket fixture
- **WHEN** `scripts/reviewer_audit.py --fixture trajectories/polymarket_sample.json` is executed
- **THEN** the script MUST process all tool calls in the fixture through the always-review bucket logic
- **AND** output a report containing helpfulness rate, harmfulness rate, and over-cautious-refusal count

#### Scenario: Audit harness offline mode — no live API calls
- **WHEN** the audit harness runs
- **THEN** it MUST NOT make live API calls to Polymarket, Kalshi, or any external broker
- **AND** all tool execution MUST be stubbed using recorded fixture responses

#### Scenario: Audit report format
- **WHEN** the audit completes successfully
- **THEN** the report MUST be emitted to stdout in a human-readable format
- **AND** a machine-readable JSON version MUST be written to `reports/reviewer_audit_<timestamp>.json`
