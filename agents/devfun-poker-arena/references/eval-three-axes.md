# Three-axis eval — WC2026-Agents steal (K160)

HL / sandbox preflight only. **Not** runtime LLM reflection in `decide()`.

## Axes

| Axis | Question | Poker analog |
|------|----------|--------------|
| **Calibration** | Are beliefs right? | Equity / pot-odds / HUD accuracy vs realized |
| **Decision quality** | Does policy profit vs hard baseline? | bb/100 vs rock/TAG/self-play gate / prior shipped decide |
| **Self-knowledge** | Does reflection match reality? | Trajectory admit-wrong / gate honesty — deploy fingerprint only |

Accuracy-only or pick-agreement boards can be a **null** when agents share a retrieval surface.

## Hard baseline required

Pair every agent/variant score with a **non-LLM** baseline: rock/TAG charts, sandbox self-play gate, or prior shipped `decide()` — never LLM-vs-LLM only.

## Do not

- Port WC search–act–reflect into the Arena hand loop
- Use reflection honesty as a runtime decide() feature
- Treat forecasting +ROI as poker alpha

Helper: `examples/eval_three_axes.py`.
