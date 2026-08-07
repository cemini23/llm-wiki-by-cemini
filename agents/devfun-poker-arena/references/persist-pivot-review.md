# Verification-gated persist/pivot review (K253)

Long Arena sessions must separate execution from review: an independent
reviewer admits memories/skills/new procedures only after checking the
evidence. State persists while evidence holds and pivots on measured
failure.

## Steal

1. Keep execute vs independent review as separate roles — the executor
   does not admit its own procedures.
2. Persist while evidence still supports the line (durable project state
   across sessions).
3. Pivot on measured failure — when street/evidence falsifies the line,
   change course instead of accumulating.
4. Gate persistence on `review_ok AND evidence_ok`
   (`examples/persist_pivot.should_persist`); pivot when
   `evidence_ok` fails.

## Do not

- Pivot on preference or vibes — require measured evidence failure.
- Install Argus (lbx154/Argus) until a real SPDX LICENSE exists
  (pyproject MIT claim insufficient; NO-GO clone).

## Sources

- Phase-1 policy wire `cemini-phase1-policy-wires.mdc` (K253)
- `briefs/2026-08-06_k250-k253-steal.md`
- `examples/persist_pivot.py`
