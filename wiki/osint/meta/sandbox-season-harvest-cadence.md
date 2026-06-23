---
title: Sandbox beta S1 season harvest cadence
type: concept
tags: [poker, arena, sandbox, researcher]
keywords: [sandbox, harvest, 10k, export, trajectory]
related:
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/garip-running-average-self-play.md
maturity: validated
created: 2026-06-08
updated: 2026-06-08
---

## Relations

- @concepts/devfun-poker-agent-challenge-2026.md
- @concepts/garip-running-average-self-play.md

## Raw Concept

Operator needs a single harvest when sandbox PvP completes ~10k hands so next-day tuning has arena exports + trajectory axes, not just leaderboard screenshots.

## Narrative

Competition: `[poker] heads-up sandbox — beta S1` `cmqqqs05i1u7ppnu7stqbw7d8`.

**Harvest script (laptop, credentials in `agents/devfun-poker-arena/.arena-credentials`):**

```bash
cd agents/devfun-poker-arena
bash scripts/run_sandbox_season_harvest.sh          # waits until 10k, then pulls all
bash scripts/run_sandbox_season_harvest.sh --now    # pull now (partial season OK)
bash scripts/run_sandbox_season_harvest.sh --poll-only
```

Output: `reports/sandbox-season/<compId>/<timestamp>/`

| Artifact | Use |
|----------|-----|
| `harvest_manifest.json` | Start here — counts + paths |
| `arena_snapshot.json` | Submission poll, leaderboard, `/agent/me` |
| `arena-export/` | `submissions.jsonl`, `agents.jsonl`, `replays.jsonl` |
| `trajectory-bundle/` | Axis M₁–M₉ summary from export |
| `local-gates/` | Today's `gate-hu-*` runs |

**Tomorrow workflow:** regression spots from worst `chipDelta` hands → patch `cemini_decide` / `s1b_exploit` → `run_hu_sandbox_gate.sh --hands 500` → resubmit when daily cap allows.

Poll single submission: `uv run python examples/submit_sandbox_pvp.py --poll <id>`

## Snippets

Tracked submission IDs (update in script or `SANDBOX_SUBMISSION_IDS` env):

- `59e6c951-95ac-44f2-92ae-2794b9ed08ab` — post super-audit bundle
- `1a945a9e-8140-45a9-9a27-fed6b46dd4a0` — prior Cemini bundle
- `308fdcbc-43b7-4ab2-ade7-0fb172e997f1` — always_fold smoke (ignore)
