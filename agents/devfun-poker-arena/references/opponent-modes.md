# Opponent modes (best-response overlays)

Bounded **best-response** margins from K156 risk-spectrum tags. Not a copy of
frontier-LLM aggression spectra into `decide()`.

Flag: `CEMINI_OPPONENT_MODES=1` (harness `setdefault` for cemini engine).

## Mode map

| participation | proactiveness | mode |
|---------------|---------------|------|
| low | low / medium | `nit` |
| high | high | `lag` |
| high | low / medium | `wide_passive` |
| else | else | `balanced` |

Cold-start HUD or missing VPIP/PFR → `balanced` (no overlay).

## Deltas (each clamped ±0.06)

| mode | intent | deltas |
|------|--------|--------|
| `nit` | steal more, bluff more, fold to aggression | `bet_bar_delta` −0.04, `fold_slack_delta` +0.04, `preflop_fold_margin_delta` −0.03; fill `open_steal_equity=0.48` only if unset |
| `lag` | tighten calls, fewer bluffs | `bet_bar_delta` +0.04, `fold_slack_delta` −0.03, `call_margin_delta` +0.04 |
| `wide_passive` | value bet / iso more | `bet_bar_delta` −0.05, `call_margin_delta` −0.02 |
| `balanced` | zero | — |

Stacked **additively** on neutral / unknown HUD margins. When private HUD
already selected `rock` / `maniac` / `tight` (or similar), modes are **skipped**
so private exploit tables are not double-counted. Absolute keys such as
`open_steal_equity` are only filled by nit mode when unset.

## Code

- `examples/opponent_modes.py` — resolve + apply
- `examples/cemini_decide.py` — after HUD enrich, when flag on
- `examples/risk_spectrum.py` — participation / proactiveness bands
- Tests: `tests/test_opponent_modes.py`

## Related

- `references/risk-spectrum-tags.md` — tags only; modes are the BR layer
- Master plan: `briefs/2026-07-19_opponent-modes-deeper-bake-master-plan.md`
