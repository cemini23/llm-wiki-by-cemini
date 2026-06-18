# Researcher track — sandbox recon (Cemini)

Operator: **cemini_wiki_poker** · **Researcher Round** (50 seats) · Target: sandbox LB + trajectory contribution.

## Discord welcome [CONFIRMED 2026-06-18]

Channel: `#researcher-track`

| Item | Detail |
|------|--------|
| Name | **Researcher Round** (next Poker Arena phase) |
| Pool | **$30,000** |
| Seats | **50** — invited researchers only |
| Closed beta | **June 21** |
| Eval thesis | How agents **play**, not only whether they **win** |
| Data | Submit → arena run → **full trajectory pull** |
| Meta | Input shapes **next agent-eval version** |

Wiki: `wiki/sources/devfun-researcher-track-discord-welcome-2026-06-18.md`

**Cemini angle:** export trajectories with `reasoning` + sizing buckets; cite multi-axis proxy metrics (2606.13815) when engaging in channel.

## API recon (2026-06-18)

`scripts/list_arena_competitions.sh` — re-run daily until Jun 21.

| competitionId | name | notes |
|---------------|------|-------|
| `cmqggiv9k37am11ydmppz466e` | [Poker] Tournament S2 | 6-max MTT — busted stack (~1.26 MON rebuy) |
| `cmqf827h30u7dfca3x2aqvzjv` | [Poker] Playground S3 | 6-max PVP — HUD intel only |
| `seed_poker_eval_s1` | [Poker] Eval S1 | PVE 500h vs reference panel — **not HU Challenge** |

**No Challenge / researcher / HU competition in `list-active` yet.** Expect new `competitionId` + `skillFile` on or before **2026-06-21** closed beta. Check researcher Discord + BenchFlow onboarding pack in parallel.

## Confirmed constraints [NEEDS VERIFICATION 2026-06-18]

From [PR Newswire launch](https://www.prnewswire.com/news-releases/devfun-launches-poker-arena-the-first-public-benchmark-for-ai-agent-reasoning-302804245.html):

- Researcher track may **fix engine + underlying LLM** — compete on poker skill layer only.
- BenchFlow contributing to eval design.
- Sample data ~41k decisions / ~2.6k hands on Hugging Face.

## Local gates (before each sandbox submit)

```bash
./scripts/run_hu_sandbox_gate.sh              # regression + selfplay + trajectory bundle
./scripts/run_hu_sandbox_gate.sh --hands 500
./scripts/export_researcher_trajectory.sh --competition-id <compId>  # after Arena run
```

Bundle output: `reports/researcher-round/<timestamp>/` — `selfplay_trajectory.jsonl`, `axis_summary.json`, optional `arena-export/`.

```bash
uv run pytest tests/test_cemini_regression.py tests/test_hu_regression.py -q
```

Arena eval (when comp live):

```bash
ARENA_COMPETITION_ID=<challenge_id> ./pokerkit run --agent examples/cemini_decide.py --max-hands 50
```

Use `GET /api/arena/__introspection` once per session; pin `competitionId` in `.arena-poker-state`.

## Skill files

| Surface | URL |
|---------|-----|
| Index | https://arena.dev.fun/skills/arena.md |
| Poker Eval PVE | https://arena.dev.fun/skills/poker-eval.md |
| Texas lobby | https://arena.dev.fun/skills/texas-holdem.md |

Challenge-specific skill likely ships with new competition `skillFile` field.

## Prod posture

- **Playground S3** — keep single lobby service for field intel; do not chase top-20 qual.
- **No prod rsync** to Challenge comp until sandbox submit path confirmed on laptop.
