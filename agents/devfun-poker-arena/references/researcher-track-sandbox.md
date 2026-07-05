# Researcher track — sandbox recon (Cemini)

Operator: **cemini_wiki_poker** · **Researcher Round** (50 seats) · **heads-up** sandbox LB + trajectory contribution.

Official guide: https://docs.dev.fun/arena/poker-arena-and-prize/the-sandbox-researcher-guide

## Format [CONFIRMED 2026-06-08]

Researcher sandbox is **HU** (2-player NLHE). Source: `@wiki/sources/devfun-researcher-track-hu-format-2026-06-08.md`.

6-max gates remain for **Playground S3** intel only — not the Researcher optimization target.

## Sandbox PvP submit (static-agent) [CONFIRMED 2026-06-26]

Researcher **heads-up sandbox** uses **static-agent bundle** + scheduler PvP — **not** `pokerkit run` on that comp (403 `sandbox_submission_required`) and **not** `texas/join` lobby (409 `benchmark_lobby_unavailable`).

```bash
export ARENA_RESEARCHER_COMP_ID='<researcher-comp-id>'   # e.g. cmqqqs05i1u7ppnu7stqbw7d8

# Local gates first
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 200
bash scripts/verify_sandbox_bundle_layout.sh

# Build + submit (replace unfinished active bot)
uv run python examples/submit_sandbox_pvp.py --build --replace --competition-id "$ARENA_RESEARCHER_COMP_ID"

# Poll
uv run python examples/submit_sandbox_pvp.py --poll '<submissionId>'

# Clear active slot (fold placeholder) before a fresh submit if needed
uv run python examples/submit_sandbox_pvp.py --discard-active --competition-id "$ARENA_RESEARCHER_COMP_ID"
```

**Bundle layout** (zip root → Daytona `/app/workspace`):

| Path | Contents |
|------|----------|
| `harness/strategy.py` | `choose_action(table)` → `gin_hu004_bridge` or `cemini_decide` per `CEMINI_SANDBOX_ENGINE` |
| `assets/cemini_decide.py` | **Live default** — K131b stack (`CEMINI_SANDBOX_ENGINE=cemini`) |
| `assets/gin_hu004_bridge.py` | Option A — vendored gin v3 `hu004` (superseded for live; retained for local gate) |
| `assets/_vendor/gin_hu004/hu004.py` | Full HU brain (~290KB); sync `scripts/sync_gin_hu004.sh`; omitted from bundle when engine=cemini |
| `skills/` | Optional — **omit from zip** (Arena rejects `skills/` in bundle) |

**Reasoning:** harness defaults `CEMINI_SANITIZE_OUTPUT=0` — Arena rejects generic reasoning on trajectory. Playground lobby may keep `CEMINI_SANITIZE_OUTPUT=1`.

**Leaderboard:** ranks **best finalized** bot (TrueSkill μ−σ). Replace does not reset LB until new bot finishes a season.

**S2 public LB visibility [SUPERSEDED on public ladder]:** `headsup-ladder.md` — listed once `pvp.status=Active`; no hidden-until-20k gate. The **20k-hand** mark is a **representative-bot** preference (longest sample wins on agent page), not LB visibility. Legacy beta S2 Discord note may still apply to `cmr0jmqlt` only.

**Arena onboarding (canonical):** `https://arena.dev.fun/skills/arena.md` → Step 0 returning player; competition skill `headsup-ladder.md` for submit/poll loop (no `/texas/*`).

**Active engine (2026-07-05):** `CEMINI_SANDBOX_ENGINE=cemini`. Pin: comp **`cmr3n8tft01nilecm1u5jlny7`**, submission **`ef651e76`** (`pvp: Active`, continuous) after premium audit HU upgrade (wide open/defend + postflop stack-off guards). Prior **`cef05ccb`** replaced. Legacy S2 `f8d4f05f` on `cmr0jmqlt` — separate track. **Claim:** `GET /auth/claim/status` (`@Cemini23`, Active).

**Prod auto-submit:** `cemini-researcher-sandbox-submit.timer` (00/06/12/18:12 UTC) → `scripts/run_researcher_sandbox_auto_submit.sh` → `examples/researcher_sandbox_auto_submit.py`: try `--replace`; on `sandbox_agent_already_running` **wait for active PvP to finish**, then submit **fresh** bundle (no replace). Pin: `config/researcher_sandbox_submit.pin.json`.


## Working assumptions

| Item | Posture |
|------|---------|
| **Table size** | **Heads-up** [CONFIRMED dev.fun 2026-06-08] |
| **Match length** | Multi-day PvP season (~10k hands per finalized bot) |
| **Submit cadence** | Bundle submit + poll; daily limit via `/submissions/settings` |
| **Engine + LLM** | **Fixed** per PR [CONFIRMED per PR] — policy `decide()` layer only |

Still read `skillFile` for hand count, rubric weights, and economics when API ships (Jun 21).

## Challenge funnel (one-pager)

1. Submit → **sandbox LB** (trajectory + multi-axis — BenchFlow eval partner).
2. Top agents → **published champion bots** (“everyone else can come and challenge”).
3. Finale → HU vs Dwan/Jungleman on stream.

**Before first submit:** `bash scripts/run_researcher_comp_recon.sh --competition-id '<id>'` — see `wiki/concepts/devfun-researcher-pre-submit-recon.md`.

## Discord welcome [CONFIRMED 2026-06-18]

Channel: `#researcher-track` — $30K · 50 seats · Jun 21 · trajectory export · how-not-only-win eval.

Wiki: `wiki/sources/devfun-researcher-track-discord-welcome-2026-06-18.md`

## API recon

`scripts/list_arena_competitions.sh` — daily until Researcher comp appears.

| competitionId | name | notes |
|---------------|------|-------|
| `cmqf827h30u7dfca3x2aqvzjv` | Playground S3 | 6-max PVP — optional HUD intel |
| `cmqqqs05i1u7ppnu7stqbw7d8` | Researcher HU sandbox (S1) | static-agent PvP submit |
| `cmr3n8tft01nilecm1u5jlny7` | **[poker] heads-up ladder S1** | **current** submit target (`headsup-ladder.md`) |
| `cmr0jmqlt08bi13n8neory9xb` | Researcher HU sandbox — beta **S2** | legacy — hero still on LB; not public ladder |
| `seed_poker_eval_s1` | Eval S1 | PVE 500h panel — **wrong cadence** for Researcher |

## Local gates (before each submit)

```bash
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh --hands 500
./scripts/export_researcher_trajectory.sh --competition-id "$ARENA_RESEARCHER_COMP_ID"
bash scripts/verify_sandbox_bundle_layout.sh
```

`CEMINI_TABLE_FORMAT` controls the local gate shape:

- `hu` (default) — HU regression + 2-player selfplay (Researcher sandbox)
- `6max` — 6-max regression + selfplay (Playground parity)
- `auto` — both bundles merged for combined gate

Current M8/M9 submit thresholds from `examples/researcher_trajectory_summary.py`:

- `M8_hallucination_rate <= 0.05`
- `M8_hole_leak_rate <= 0.02`
- `M9_positional vpip gap >= -0.20` (6-max: BTN–UTG; HU: BTN–BB)

## arena-tool vs static-agent

The official guide documents **arena-tool MCP** (`join_pve`, `submit_action` with `reasoning_text`) for LLM agents in Daytona. Cemini uses the **static-agent** path: BenchFlow calls `harness/strategy.choose_action(table)` — no direct Arena HTTP from the sandbox. Both require hand-specific reasoning, not generic placeholders.

## Competitor OSINT

See `wiki/concepts/devfun-poker-competitor-github-recon-2026-06.md` — **gin/poker-bot** v008 in `gin_style.py` (`CEMINI_GIN_V008=1`); **full HU stack** vendored as `hu004` for optional local gate (`CEMINI_SANDBOX_ENGINE=gin_hu004`). Live sandbox reverted to cemini 2026-07-02. Ship brief: `briefs/2026-07-01_k139-gin-hu004-option-a-sandbox-ship.md`.

## Prod posture

- **Researcher Round** — **primary** optimization target (HU gates, trajectory, axis discipline).
- **Playground S3** — optional **background intel** only (`CEMINI_PACE_PHASE=intel`, ~1h join cadence); parallel S3 volume service **disabled** on prod prep apply.
- Ship **`cemini_decide.py`** via **bundle submit** for Researcher; 6-max gin lane for incidental Playground hands only.
