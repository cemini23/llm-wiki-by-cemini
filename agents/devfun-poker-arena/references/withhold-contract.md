# Withhold contract (Cybersec K276)

**Dual-ID:**
- Cybersec K276 = withhold contract (2608.12292) ← this ref
- Cybersec K277 = RSM (same 2608.12311) → `references/rsm-helper-roles.md`
- CCC K274 = CDH (2608.12273) → `references/cdh-skill-budget.md`
- CCC K275 = VAKRA (2608.12282) → `references/vakra-eval-axes.md`
- CCC K276 = RSM (2608.12311) → `references/rsm-helper-roles.md`

**Code:** `examples/withhold_contract.py`
**Wire:** `examples/output_sanitize.py` (`maybe_sanitize_action(hole_cards=..., hand_class=...)`)
**Tests:** `tests/test_withhold_contract.py`

## Steal

Enforce "withhold what must not be revealed" as a per-turn machine-checkable
contract, not a prompt line:

1. **Non-LLM policy core fed only trusted state** — hole cards (and optional
   `hand_class`) come from decide, never from table chat / `tool_result`.
   The API raises `ValueError` on `hole_source="observation"` instead of
   trusting the fake list.
2. **Deterministic detector outranks the model** — rank-suit tokens in common
   Arena forms (`Ah`, `AH`, `A♥`, `Ace of hearts`, `AhKd`) plus the
   hand-class shorthand (`AKo` when it is the current hand class) are
   matched by regex, not by an LLM judgment call.
3. **Revise over block** — redacted text (`[HOLE]` / `[HAND]`) is returned;
   over-blocking is a measured failure (users route around friction).
   Empty/None text is never a leak.
4. Board cards are not secrets — the caller simply never passes them as
   `hole_cards`.

## Env gate

`CEMINI_WITHHOLD_CONTRACT` defaults **on** (`1`). At `0`, `detect_leak` still
works but `check_outbound_action` is a no-op passthrough.

## Do not

- Feed observation / tool_result hole lists into the detector — untrusted
  channel as hole source is rejected.
- Raise on a detected leak — revise over block.
- Treat board cards as secrets.

## Check

```bash
uv run pytest tests/test_withhold_contract.py tests/test_anti_profiling.py -q --tb=short
```
