## Target

dev.fun Poker Arena — researcher track eval primitives.

## Summary

K151 **steal-from** — FootsiesGym (2607.06514): 2p zero-sum **imperfect-information** fighting-game benchmark. Shared DNA with HU poker: hidden state, commitment timing, exploitability metrics. Use to stress-test nine-axis eval + trajectory logging outside pokerkit.

## Body

Read:

- `@sources/arxiv-footsiesgym-2607.06514-2026-07-09.md`
- `@sources/arxiv-lightweight-game-agent-2607.06854-2026-07-09.md` (lightweight agent ablations)

**Arena actions:**

1. Spike: map FootsiesGym observation/action API to Raeth rubric dimensions (information, commitment, exploitability).
2. Compare lightweight-agent ablation lessons to `cemini_decide` compute budget on HU sandbox.
3. **Out of scope:** Replacing pokerkit env; fighting game is eval sandbox only.

## Sources

- `@sources/arxiv-footsiesgym-2607.06514-2026-07-09.md` [Source: https://arxiv.org/abs/2607.06514]
