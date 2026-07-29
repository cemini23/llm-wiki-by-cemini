# Risk-spectrum tags (K156)

Operator tags for AI / sandbox foe cards. Source: AgentTexasPoker / arXiv
**2607.10251** — stable VPIP/PFR risk spectra. **Tags only** — do not copy
frontier-LLM aggression into `decide()`.

## Schema

```json
"risk_spectrum": {
  "participation": "high|medium|low",
  "proactiveness": "high|medium|low",
  "vpip": 0.516,
  "pfr": 0.0,
  "source": "arena_stats|heuristic"
}
```

| Axis | Stat | Meaning |
|------|------|---------|
| `participation` | VPIP | Willingness to enter uncertain pots |
| `proactiveness` | PFR | Preflop escalation |

## Bands

| Band | VPIP | PFR |
|------|------|-----|
| high | ≥ 0.45 | ≥ 0.15 |
| medium | ≥ 0.25 | ≥ 0.05 |
| low | else | else |

Implemented in `examples/risk_spectrum.py` (`VPIP_HIGH`, `VPIP_MEDIUM`,
`PFR_HIGH`, `PFR_MEDIUM`).

## Where used

- `research/opponents/*-profile.json` nemesis cards
- Optional HUD enrich via `attach_risk_spectrum_to_hud` (exploit selection /
  HL notes — not forced into every decide)

## Best-response modes (allowed)

Risk-spectrum tags may drive **bounded best-response overlays**
(`nit` / `lag` / `wide_passive` / `balanced`) via `examples/opponent_modes.py`
when `CEMINI_OPPONENT_MODES=1`. That is still **not** “copy GPT VPIP into
aggression” — modes only stack small margin deltas (±0.06) against tagged
foes. See `references/opponent-modes.md`.

## Related

- `briefs/2026-07-15_k156-agenttexaspoker-risk-spectrum-steal.md`
- `references/opponent-modes.md`

