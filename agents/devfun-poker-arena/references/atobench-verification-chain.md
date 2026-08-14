# ATOBench verification chain (Cybersec K278)

**Dual-ID:**
- Cybersec K278 = ATOBench (2608.12996) ← this ref
- Cybersec K277 = RSM (2608.12311) → `references/rsm-helper-roles.md` (already wired)
- CCC K277 = Labels ≠ endpoints (2608.12880) → `references/eval-integrity.md`
- CCC K278 = InterSAGE (2608.13030) — SKIP poker
- CCC K279 = MARC-v1 (2608.13476) — SKIP poker (clinical OOD)
- CCC K280 = Vero (2608.13522) → `references/eval-integrity.md` (light)
- CCC K281 = AutoDesign (2608.13560) → `references/eval-integrity.md` (light)

**Code:** `examples/verification_chain.py`
**Tests:** `tests/test_verification_chain.py`

## Steal

Evaluate the **evidence path**, not the final chip/win outcome. Deceptive
observations (bluffs, injected noise, opponent messages) can keep an agent
busy after the evidence path has broken — **activity ≠ verification**.

1. **Attach evidence to actions** — `attach_evidence(action, evidence)` adds an
   evidence dict with a non-empty `locator` (hand-id / street+spot / jsonl
   line) plus a `_evidence_ok` sidecar. A missing locator is not intact.
2. **Score activity vs evidence-intact separately** — `score_trace(steps)`
   reports `activity`, `repetitions`, `grounded_count` / `ungrounded_count`,
   `first_break_index`, `busy_after_break`, `activity_ne_verification`, and a
   single `evidence_intact` flag (`ungrounded_count == 0 and activity > 0`).
3. **Pair native vs treatment at first divergence** — `pair_traces(native,
   treatment)` aligns at the first `action` / `action_class` divergence (or
   length mismatch) and diffs **evidence paths**, not win/loss:
   `evidence_path_same` requires both `evidence_intact` flags equal **and**
   both `first_break_index` equal.
4. **Shared win/loss is not verification** — a pair can have
   `outcome_same=True` and still `evidence_path_same=False`.

SQLi-style transfer: the treatment trace adds many extra probes (activity and
repetitions up) after evidence breaks while native stays grounded — busy
agent ≠ correct agent.

## Do not

- Clone ATOBench — the GitHub repo is a placeholder.
- Apply to live targets — authorized-lab / offline traces only.
- Treat paper numbers (median 14 extra actions, 44/45 JWT) as poker chip EV.

## Check

```bash
uv run pytest tests/test_verification_chain.py -q --tb=short
```
