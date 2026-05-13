## Why

The reviewer-agent v1 runs on every tool call, incurring a 6.2× single-turn latency penalty that is unjustifiable for read-only queries (e.g., `get_price`, `get_orderbook`). A selective-trigger policy recovers most of the latency floor while preserving gating benefit on the high-stakes minority of calls — specifically those that mutate account state or are issued under low base-agent confidence.

## What Changes

- Add a declarative YAML trigger-policy configuration evaluated by the Conductor middleware before the reviewer-agent stage is invoked.
- Introduce three routing buckets: `always-review` (side-effecting mutations), `review-on-uncertainty` (gated by a configurable confidence threshold), and `skip-review` (read-only queries).
- Emit cost-ceiling telemetry: track reviewer-agent invocation count and estimated DeepSeek-R1 token cost per session, with a configurable monthly ceiling that raises an alert when exceeded.
- Add a harmfulness audit harness: a test fixture that runs a representative sample of trajectories and reports the over-cautious-refusal rate for the `always-review` bucket.

## Capabilities

### New Capabilities

- `reviewer-agent-selective-trigger`: Declarative trigger-policy YAML evaluated at the Conductor middleware layer; three routing buckets (always-review / review-on-uncertainty / skip-review); cost-ceiling telemetry; harmfulness audit harness.

### Modified Capabilities

<!-- No existing spec-level behavior changes; v1 reviewer-agent has no existing spec file. -->

## Impact

- **Conductor middleware** (`conductor/mcp_server.py` or equivalent): insertion point for the trigger-policy evaluation step before `reviewer_agent.review()` is called.
- **Reviewer-agent configuration**: new `reviewer_policy.yaml` (or inline config block) defining bucket membership lists and the confidence threshold.
- **Telemetry module**: new session-scoped counter for reviewer invocations and token-cost estimate.
- **Audit harness**: new test script consuming a trajectory sample and computing helpfulness/harmfulness split for the `always-review` bucket.
- **No breaking changes** to existing base-agent or Conductor routing behavior; the trigger filter is additive. A missing or empty policy file degrades gracefully to v1 always-review behavior.
