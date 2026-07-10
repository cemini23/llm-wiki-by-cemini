## Target

dev.fun Poker Arena — researcher track eval primitives.

## Summary

K151 **steal-from** — FootsiesGym (2607.06514): 2p zero-sum **imperfect-information** fighting-game benchmark. Shared DNA with HU poker: hidden state, commitment timing, exploitability metrics. Use to stress-test nine-axis eval + trajectory logging outside pokerkit.

**Shipped (2026-07-09):** `references/footsiesgym-raeth-axis-map.md`; `exploitability_advisory` in `researcher_trajectory_summary.py` (CLI + tests); HU gate advisory echo for TEN/maniac_shark yardsticks; wiki source deepen + Raeth concept backlinks. **No** FootsiesGym install; **no** pokerkit replace; **no** ladder deploy.

## Body

Read:

- `@sources/arxiv-footsiesgym-2607.06514-2026-07-09.md`
- `@sources/arxiv-lightweight-game-agent-2607.06854-2026-07-09.md` (lightweight agent ablations)

**Arena actions:**

1. ~~Spike: map FootsiesGym observation/action API to Raeth rubric dimensions (information, commitment, exploitability).~~ **DONE** — `references/footsiesgym-raeth-axis-map.md`
2. ~~Compare lightweight-agent ablation lessons to `cemini_decide` compute budget on HU sandbox.~~ **DONE** — information-bound ceiling documented; prefer yardstick villains over MC capacity chase
3. **Out of scope:** Replacing pokerkit env; fighting game is eval sandbox only.

### Validation

```bash
uv run pytest tests/test_researcher_trajectory_summary.py -q
python3 scripts/skill_audit.py briefs/2026-07-09_k151-footsiesgym-benchmark-steal.md
```

## Sources

- `@sources/arxiv-footsiesgym-2607.06514-2026-07-09.md` [Source: https://arxiv.org/abs/2607.06514]
- `@sources/arxiv-lightweight-game-agent-2607.06854-2026-07-09.md` [Source: https://arxiv.org/abs/2607.06854]
- `references/footsiesgym-raeth-axis-map.md`
