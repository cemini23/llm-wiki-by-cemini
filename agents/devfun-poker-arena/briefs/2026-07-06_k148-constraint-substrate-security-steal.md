## Target

`agents/devfun-poker-arena/` — sandbox bundle harness + HL patch security posture.

## Summary

K148 steals: **constraint substrate** (2607.02389) for auditable agent code; **cognitive security** literacy (2606.30587); **Ganzfried QP** exact-NE anchor (2509.25618) — theory only.

## Body

### Constraint substrate (02389) — P0 adoption

| Control | Implement |
|---------|-----------|
| Linters + type hints | Fail bundle CI on lint before MCP eval |
| Layered docs CLI | ~200 LoC module index for small reviewer / human audit |
| Allow-list actions | Match K120 — outcomes shaped in code not prompts |
| MCP discipline | No raw payload dumps saturating context |

Backdoor-detection experiment: recall **54.5% → 90.9%** with substrate vs unconstrained agent.

### Cognitive security (30587)

- LLM vuln triage on `analyze` briefs can flip on **comment framing** alone (97% suppression PoC)
- **Rule:** `cemini_preflight.sh` + regression spots gate deploy; LLM review is advisory

### Ganzfried QP (25618)

- Exact multiplayer imperfect-info NE via QCQP — complements K131 VBT + K134 PED
- **Not** a Playground qualification metric — toy games only

## Sources

- [Source: arXiv:2607.02389, 2606.30587, 2509.25618 (retrieved 2026-07-06)]
- `@sources/arxiv-steerability-constraints-2607.02389-2026-07-05.md`
- `@concepts/coding-agent-substrate-steerability.md`
