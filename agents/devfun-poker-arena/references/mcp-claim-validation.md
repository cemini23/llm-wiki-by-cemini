# MCP claim validation + parameter grounding (K259)

When Arena helpers surface solver/tool reports, catalog membership ("looks
like a known line") is **not** the same as validating the directional claim
the agent will repeat. Validate the direction; refuse ambiguous NL -> tool
args instead of silent-defaulting.

## Steal

1. `membership_match(report|line_id, catalog)` separates catalog membership
   from claim truth. A known-looking report only tags `membership="match"` —
   it never sets `repeat_ok` by itself.
2. `validate_directional_claim(claim, report)` compares the directional
   assertion (action / EV / line direction) the agent would repeat against
   the report's own directional fields. `repeat_ok=True` only when
   `claim_status="validated"`. Missing or malformed evidence ->
   `unvalidated`/`skipped`, never a crash.
3. `ground_tool_args(raw)` resolves informal seat/street/solver-id names via
   **server-side code alias maps** (never raw model strings). Ambiguous or
   unknown args -> `clarify`/`refuse`, fields stay `None`. Prefer skip over
   inventing — no silent default to seat 1 / preflop / `static_chart`.
4. `tag_solver_context_claims(ctx)` is the light wire for
   `cemini_decide.retrieve_solver_context`: tags a directional assertion as
   `unvalidated` when no independent evidence exists, tags membership-only
   reports, and grounds `ctx["tool_args"]` when present. Fail-open — decide
   never crashes on claim-validation weirdness.

## Do not

- Treat a catalog match ("looks like a known line") as claim validation.
- Silent-default ambiguous seat/street/solver id — refuse or skip.
- Trust raw model strings for informal names; resolve through code alias maps.
- Install CASCADE / genomics runtime — this is a light steal, pattern only.
- Treat a `claim_validation` skip/tag as an EV claim (advisory for the
  compare harness, not a decision).
- Duplicate `assert_solver_grounded` (K199) — numbers stay K199; K259
  validates direction/membership and arg grounding, not float provenance.

## Sources

- `briefs/2026-08-08_k259-cascade-claim-validation-steal.md`
- CCC wiki `concepts/mcp-claim-validation-and-parameter-grounding.md`
- `examples/claim_validation.py`
- Related: `examples/solver_preflight.py` (K244),
  `examples/canary_tool_diagnosis.py` (K250),
  `examples/solver_context_prune.py` (K199)
