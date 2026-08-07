# Canary tool selection (K250)

When Arena helpers pick the wrong tool/solver, classify *why* instead of
stopping at "wrong tool." Plant diagnostic canary tools during MCP /
solver-selection audits and measure how often the model falls for each
trap class.

## Trap taxonomy

1. **semantic decoy** — a tool whose name/description resembles the right
   one but is a different capability.
2. **parameter trap** — the right tool, configured with the wrong
   parameters.
3. **capability mirage** — "advanced"/premium-looking capability that
   overclaims; strong models are not immune.
4. **prerequisite blindness** — a tool that needs setup/dependencies the
   picker never checks.
5. **temporal decoy** — stale/outdated variant chosen over the current
   one.
6. **granularity trap** — right family, wrong resolution/level for the
   spot.

## Steal

1. Label a wrong pick with its trap class before deciding whether the
   tool or the routing is the problem.
2. Measure canary susceptibility rate (CSR) = fraction of planted canary
   traps the model picks over the task-matched tool. Report CSR when
   auditing tool selection — capability tier != safety.
3. Prefer task-matched specificity over capability-looking generality.

## Do not

- Stop at "wrong tool" without a trap class (loses the fix signal).
- Claim a public canary framework exists — taxonomy only, no artifact
  install.

## Sources

- Phase-1 policy wire `cemini-phase1-policy-wires.mdc` (K250)
- `briefs/2026-08-06_k250-k253-steal.md`
- `examples/canary_tool_diagnosis.py`
