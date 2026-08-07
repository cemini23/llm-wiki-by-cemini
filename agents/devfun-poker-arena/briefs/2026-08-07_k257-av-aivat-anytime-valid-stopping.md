---
title: CCC→Poker K257 — AV-AIVAT anytime-valid agent eval stopping
type: brief
tags: [brief, poker, k257, evaluation]
created: 2026-08-07
---

## Target

`agents/devfun-poker-arena/` — Poker Arena

## Summary

When comparing LLM poker agents, stop as soon as evidence suffices under anytime-valid confidence sequences + AIVAT-style variance reduction. Paper reports median **74×** fewer HUNL hands vs raw outcomes at ±1 BB (AsympCS). No public code — method only.

## Regime disclosure

Paper metrics are not Arena EV. Apply inside existing HU Researcher / Playground eval regimes only.

## Steal

1. Prefer variance-reduced payoffs + CS stopping over fixed hand budgets.
2. Do not stop early with an ordinary CI (invalidates coverage).
3. Online value model must not peek at the current hand.
4. Keep paired logs + stop metadata so a third party can recheck.

## Light peers

- K256 TrajDebug: on failed long Arena sessions, attribute earliest wrong commitment with evidence.
- K258 PTC: if Arena helpers call tools via code stubs, prefer that for fan-out when sandboxed.

## Skip

- Hardware keystore HSM stack (cybersec).
- READ financial-doc MCP (wiki ingest).
- TrajDebug / AV-AIVAT / PTC installs (no usable public code for poker).

## Filed (2026-08-07)

- `references/anytime-valid-agent-eval-stopping.md`
- `examples/eval_stop_metadata.py`
- `tests/test_eval_stop_metadata.py`

## Sources

- `@concepts/anytime-valid-agent-eval-iigames.md`
- `@sources/arxiv-2608.06362-av-aivat-2026-08-07.md`
- arXiv 2608.06362
- Arena ref: `references/anytime-valid-agent-eval-stopping.md`
