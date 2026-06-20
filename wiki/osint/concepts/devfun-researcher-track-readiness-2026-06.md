---
title: dev.fun Researcher Track — readiness hub (Jun 2026)
type: concept
tags: [concept, poker, devfun, researcher-track, multi-axis, trajectory]
keywords: [researcher round, Jun 25, HU, 6-max, trajectory, axis_summary, cemini_wiki_poker]
related:
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/devfun-researcher-pre-submit-recon.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - concepts/multi-agent-fictitious-play-llm.md
  - concepts/devfun-poker-competitor-github-recon-2026-06.md
  - sources/devfun-researcher-track-discord-welcome-2026-06-18.md
  - concepts/devfun-researcher-pro-style-targets-2026-06.md
  - sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/devfun-researcher-track-hu-format-2026-06-08.md
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - entities/platforms/devfun-arena.md
maturity: validated
created: 2026-06-19
updated: 2026-06-20
cross-wiki:
  - "@gambling-wiki/entities/platforms/devfun-poker-arena.md"
  - "@gambling-wiki/concepts/poker-hl-analyst-loop.md"
  - "@gambling-wiki/concepts/heads-up-arena-strategy.md"
  - "@gambling-wiki/sources/research-k122-poker-paper-landscape-2026-06-19.md"
---

## Relations

- @concepts/devfun-poker-agent-challenge-2026.md — timeline + challenge framing
- @concepts/devfun-researcher-pre-submit-recon.md — sit-down recon before first hand
- @gambling-wiki/entities/platforms/devfun-poker-arena.md — platform ladder (Playground → Researcher → finale)
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — leak-patch methodology (Playground intel only)
- @gambling-wiki/concepts/heads-up-arena-strategy.md — HU preflop/postflop + TrueSkill doctrine (K122)
- @gambling-wiki/sources/research-k122-poker-paper-landscape-2026-06-19.md — paper verdicts vs K118 F6/F12 lanes
- @sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md — Raeth 9-axis eval anchor
- Super-audit synthesis: `agents/devfun-poker-arena/briefs/2026-06-19_researcher-track-super-audit-synthesis.md`

## Narrative

### What Researcher Round is (not Playground)

| | Playground S3 | Researcher Round |
|---|---------------|------------------|
| **Goal** | Season chip grind / qual intel | Sandbox LB + **trajectory contribution** |
| **Scoring thesis** | Chip delta (primary) | **TrueSkill** HU sandbox LB [CONFIRMED email]; trajectory + axis for research discipline |
| **Pool** | Open season | **$30K** · **50 invited seats** |
| **Engine** | Arena pokerkit | **Fixed engine + base LLM** — policy `decide()` only [CONFIRMED PR] |
| **Our use** | HUD / leak intel | **Primary submit target** Jun 21 beta → **Jun 25 public** |

### Timeline

| Date | Gate |
|------|------|
| **Jun 21** | Closed beta — first sandbox submit; read `skillFile` (table size, rubric) |
| **Jun 25** | **Public Challenge launch** — iterative submits |
| **Early Jul** | Finale — human vs AI stream (format may differ from sandbox) |

### Scoring — TrueSkill + trajectory [CONFIRMED email 2026-06-19]

devlord email (`@sources/devfun-poker-researcher-track-email-2026-06-19.md`, canonical `@gambling-wiki/sources/devfun-poker-researcher-track-email-2026-06-19.md`):

| Layer | Metric | Role for Cemini |
|-------|--------|-----------------|
| **Sandbox LB** | **TrueSkill** (HU pairwise) | Primary rank target — beat the field distribution, not Playground chips |
| **Research / Discord** | Trajectory + multi-axis (Raeth) | Export + `axis_summary.json` gates before every submit |
| **Finale rep** | Dwan + Jungleman **style match** | `@concepts/devfun-researcher-pro-style-targets-2026-06.md` — **Jungleman** default HU emulation |

Pro profiles (gambling-wiki K121): `@gambling-wiki/entities/people/tom-dwan.md`, `@gambling-wiki/entities/people/daniel-cates-jungleman.md`, `@gambling-wiki/sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md`.

Top TrueSkill agent becomes the **benchmark bot** everyone challenges — same funnel as one-pager, now with explicit rating system.

### Pro style emulation

See `@concepts/devfun-researcher-pro-style-targets-2026-06.md` — **Jungleman-shaped** wide HU aggression for TrueSkill + rep pick; Dwan = merge/overbet lane. Finale exploit overlays not wired in code yet.

### Eval discipline (still ship-safe)

The Challenge funnel is **sequential**:

1. **Sandbox eval** — trajectory + multi-axis score (BenchFlow) → leaderboard.
2. **Publish** — top agents become champion bots.
3. **Challenge / finale** — HU spectacle (downstream of step 1).

**Step 1 is supreme for admission:** clear TrueSkill-oriented HU play **without** axis holes that get you skipped for style rep or research narrative.

**Default target:** **HU** TrueSkill sandbox + `axis_summary.json` gates (`CEMINI_TABLE_FORMAT=hu`). 6-max = Playground intel only.

Full ritual (no hands before recon): @concepts/devfun-researcher-pre-submit-recon.md

### Format — Researcher sandbox is HU [CONFIRMED 2026-06-08]

dev.fun confirmed Researcher Round is **heads-up** (see `@sources/devfun-researcher-track-hu-format-2026-06-08.md`). Supersedes prior 6-max working assumption.

| Lane | Format | Confidence |
|------|--------|------------|
| **Researcher sandbox / eval** | **Heads-up** | [CONFIRMED dev.fun 2026-06-08] |
| Playground S3 | 6-max season | [CONFIRMED live comp] |
| Stream finale | HU vs pros | [CONFIRMED one-pager] |

**Code posture:** HU-primary — `_HU_OPEN_CHART`, 29+ HU regression spots, 2-player selfplay gates, M₉ **BTN vs BB** VPIP gap. Keep 6-max regression for Playground lobby; do not treat `auto` dual gate as default pre-submit path.

### Format reference (technical)

| Source | Says |
|--------|------|
| HU confirmation (Jun 8) | Researcher sandbox = **HU** |
| One-pager PDF | HU marketing + sandbox LB before publish |
| Discord welcome | Trajectory + sandbox; no table size in original post |
| Live API | Playground / Tournament **2–6 players**; Researcher comp not listed yet |
| Code today | **HU-primary** for Researcher (`CEMINI_TABLE_FORMAT=hu` default in gate script) |

**Gate default:** `CEMINI_TABLE_FORMAT=hu` — use `6max` or `auto` only for Playground parity checks.

### What we have today (Jun 8)

- **Policy:** `cemini_decide.py` — HU chart when `CEMINI_TABLE_FORMAT=hu` + MC + gin v008 + HL regression + F6 memory
- **Prod:** Playground S3 lobby · **Researcher PRIMARY** (`CEMINI_PRIMARY_TRACK=researcher`, HU format, slow Playground intel); flip `CEMINI_RESEARCHER_MODE=1` when comp live
- **Researcher comp ID:** not in API yet — daily `list_arena_competitions.sh`
- **HL auto-analyst:** **off** on prod (`CEMINI_HL_AUTO_ANALYST=0`); stale `runtime_guards.json` cleared on pivot. Manual HL only via HU trajectory + axis gate — not Playground every-N-hands.

### Super-audit consensus (5-model, 2026-06-19)

**Overall: SHIP-WITH-FIXES** — HU policy path active; trajectory/axis gates are the submit surface.

| Theme | Consensus |
|-------|-----------|
| **Strength** | Regression-hardened TAG; gin lane; stack-off discipline; trajectory *plumbing* exists |
| **Gap** | Pin Researcher `competitionId` when API lists it; widen HU chart if gate spots fail |
| **Risk** | ~~HU without fork~~ → **HU confirmed** — optimize chart + 2p selfplay, not 6-max sandbox |
| **Do not optimize** | Playground rank, Eval 500h, raw selfplay bb/100 as training target |

Full rollup: `agents/devfun-poker-arena/briefs/2026-06-19_researcher-track-super-audit-synthesis.md`

### K122 validation (2026-06-19)

Cross-walk vs gambling-wiki K122 synthesis (`@gambling-wiki/concepts/heads-up-arena-strategy.md`, `@gambling-wiki/sources/research-k122-poker-paper-landscape-2026-06-19.md`). Operator plan: `@gambling-wiki/briefs/2026-06-19_k122-poker-researcher-track-research-plan.md` — link only, not duplicated here.

**Verdict:** K122 recommendations **match** OSINT posture + code audit [CONFIRMED 2026-06-19].

| K122 recommendation | Shipped (OSINT) | Gap |
|---------------------|-----------------|-----|
| **L3–4 pure-code `decide()`** — no runtime LLM | MC + chart + HUD + F6 memory; HL auto-analyst **off** on prod | — |
| **HU fork** — `_HU_OPEN_CHART`, 29+ regression spots, 2p gates | `CEMINI_TABLE_FORMAT=hu`, `run_hu_sandbox_gate.sh` | — |
| **Trajectory + M₁–M₉ axis gates** | `researcher_trajectory_summary.py --gate`, hero export | — |
| **K118 PFR / limp fix** (HU chart-first + gin defer) | **Shipped 2026-06-19** — 500h HU gate PASS: PFR **21.4%**, VPIP−PFR **7.4%** | — |
| **TrueSkill proxy (match W/L)** | **Shipped 2026-06-19** — `series_win_rate` @ 80h/match; rock gate **55%**; maniac advisory **≥38%** (now **40%**) | Not a **training** objective; no public TrueSkill docs until Jun 21 |
| **Jungleman-band 3-bet / BB defend** | HU chart + S1B widen shipped; vs maniac series_win **40%** | Continue tune pre-submit |
| **F6 session memory** (K122 lit → F6 only) | F6 shipped + ablation script | Literature informs offline exploit — **not** runtime LLM |
| **Offline HL loop (P3)** | Manual HU trajectory evidence; prod HL patches cleared | — |
| **Style emulation** (`jungleman` / `durrrr`) | Profiles + `@concepts/devfun-researcher-pro-style-targets-2026-06.md` | **Hold** — no `CEMINI_RESEARCHER_STYLE_TARGET` until rules land |
| **SDK / Kaggle submit path** | Starter kit documented (gambling entity); recon script ready | **Hold Jun 21** — pin `competitionId`, Kaggle URL, TrueSkill docs on beta drop |
| **Do not optimize** selfplay bb/100 or Playground chips | Gates + prod Researcher PRIMARY posture | Match W/L reported; still not HL training target |

**Execute now (pre-Jun 21):** P0 from 7-model super-audit **done** (series match_win gate, maniac advisory, intel `TABLE_FORMAT=auto`, lag bot). **Shipped 2026-06-19:** W-PFR, W-MATCH, S1B, 500h gate PASS, prod redeploy. **Hold:** style code, Kaggle wiring, SDK rubric until closed beta materials arrive.

### P0 before first Researcher submit

0. **Recon ritual** — `run_researcher_comp_recon.sh` + human checklist (no submit until signed)
1. Read `skillFile` → pin `ARENA_RESEARCHER_COMP_ID`
2. ~~Trajectory export hero~~ — **done** (hero always in export + gate)
3. ~~Eval bleed~~ — **done** (`CEMINI_EVAL_PANEL_MODE` opt-in; Researcher profile strips eval_panel)
4. ~~M₁–M₉ proxies + gates~~ — **done** (`researcher_trajectory_summary.py --gate`)
5. ~~Reasoning honesty~~ — **done** (IP/OOP, `vr`, no blind slice)
6. ~~HU fork~~ — **done** (`CEMINI_TABLE_FORMAT`, HU chart, 29 HU regressions, `auto` dual gate)

### P1 ops (shipped)

- `run_hu_sandbox_gate.sh` — `auto|hu|6max` + axis gates
- `run_researcher_memory_ablation.sh` — F6 on/off paired selfplay
- `run_researcher_soak.sh` — long-run trajectory + `deploys.jsonl` tag
- `cemini_preflight.sh` — Researcher gate when `CEMINI_RESEARCHER_MODE=1`

### Operator commands

```bash
# Daily until Researcher comp appears
bash agents/devfun-poker-arena/scripts/list_arena_competitions.sh

# BEFORE first submit (mandatory)
bash agents/devfun-poker-arena/scripts/run_researcher_comp_recon.sh --competition-id '<id>' --write-wiki-stub

# Pre-submit gate (HU — Researcher sandbox)
CEMINI_TABLE_FORMAT=hu bash agents/devfun-poker-arena/scripts/run_hu_sandbox_gate.sh --hands 500

# Long-run stamina + deploy tag
bash agents/devfun-poker-arena/scripts/run_researcher_soak.sh --hands 2000

# F6 memory ablation before enabling cross-session seed
bash agents/devfun-poker-arena/scripts/run_researcher_memory_ablation.sh
```

### Waiting on dev.fun rules [2026-06-19]

dev.fun will send **more rules shortly** (Kaggle / SDK / sandbox rubric). **Hold** until then:

- Jungleman / Dwan **style emulation** code (`CEMINI_RESEARCHER_STYLE_TARGET`, villain overlays)
- Kaggle vs `pokerkit run` submit path
- TrueSkill opponent pool + match length assumptions

**Continue now (unchanged):** HU gates (`run_hu_sandbox_gate.sh`), trajectory + axis discipline, prod Researcher PRIMARY posture, daily `list_arena_competitions.sh`, recon ritual when comp appears.

**Prep ready:** `@concepts/devfun-researcher-pro-style-targets-2026-06.md`, gambling-wiki Dwan/Jungleman profiles — implement after rules confirm interface + scoring detail.

```bash
bash agents/devfun-poker-arena/scripts/list_arena_competitions.sh
# On prod after pinning id:
# ARENA_RESEARCHER_COMP_ID=<id>
# CEMINI_RESEARCHER_MODE=1
# ARENA_LOBBY_COMPETITION_ID=<same id>  # if lobby should play Researcher season
systemctl restart cemini-devfun-poker-lobby.service
```
