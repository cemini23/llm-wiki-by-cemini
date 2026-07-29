# K148 cognitive security — deploy discipline

From arXiv:2606.30587 — LLM vulnerability triage can flip on **comment framing** alone (97% suppression PoC in paper).

## Arena rule

| Layer | Role |
|-------|------|
| **pytest + regression spots** | **Gate** — blocks deploy via `cemini_preflight.sh` |
| **substrate gate** | **Gate** — AST + ruff + forbidden calls before sandbox submit |
| **HL / analyze LLM** | **Advisory** — proposes patches; never sole deploy authority |
| **substrate reviewer pilot** | **Advisory** — topology-only Gemma-class WARN/BLOCK hints |

## Operator checklist

1. Patch `cemini_decide.py` from replay data or approved STRATEGY translation.
2. Run `./scripts/cemini_preflight.sh` (or `--full` before ladder replace).
3. For Researcher submit: `./scripts/run_hu_sandbox_gate.sh`.
4. Treat any LLM "looks good" without green preflight as **non-binding**.
5. Eval claim ceiling (K220) — modest clean boards do not license rare-leak
   absence: `references/eval-claim-ceiling.md`.
6. LIVE vs sandbox containment (K222): `references/sandbox-live-containment.md`.
