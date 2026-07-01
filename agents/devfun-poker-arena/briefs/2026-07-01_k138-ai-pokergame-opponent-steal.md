## Target

`agents/devfun-poker-arena/` — sandbox villain / chart opponent modeling.

## Summary

Steal K138 eval **PENEEEEE732/AI_pokergame** (MIT per gh): Hard-tier pot-odds, implied-odds, semi-bluff heuristics as **reference villains** — read-only extraction, no Flask server merge.

## Body

### Preconditions

- MIT license confirmed `gh api` 2026-07-01 (docx had NOT FOUND).
- Audit extracted functions for side effects / network calls before copy.

### P0 — heuristic inventory

1. Map Hard AI decision tree: preflop range buckets, postflop pot-odds thresholds, semi-bluff frequency params.
2. Document as YAML villain profile (`villain_ai_pokergame_hard.yaml`) — no code merge yet.

### P1 — sandbox villain spike

1. Implement thin adapter wrapping extracted heuristics as `decide()` opponent in HU toy env (not full NLHE).
2. Run nine-axis eval vs random + one chart baseline; log exploitability of **us** vs this villain.

### Out of scope

- Socket.IO server deployment
- Claiming Hard AI is balanced GTO

## Sources

- @wiki/entities/tools/ai-pokergame.md
- @wiki/sources/eval-github-repo-plan-dfs-marl-poker-osint-2026-07-01.md
