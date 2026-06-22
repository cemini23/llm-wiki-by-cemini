---
title: dev.fun Researcher — pre-submit recon ritual
type: concept
tags: [concept, poker, devfun, researcher-track, evaluation, ops]
keywords: [skillFile, BenchFlow, trajectory, recon, before submit, optimization target]
related:
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - sources/devfun-poker-agent-challenge-onepager-2026-06-18.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - sources/devfun-researcher-track-hu-format-2026-06-08.md
  - sources/devfun-researcher-track-discord-welcome-2026-06-18.md
  - entities/platforms/devfun-arena.md
  - entities/platforms/devfun-heads-up-pvp-s3.md
maturity: validated
created: 2026-06-19
updated: 2026-06-20
---

## Relations

- @concepts/devfun-researcher-track-readiness-2026-06.md — readiness hub + gates
- @concepts/poker-arena-multi-axis-cognitive-profile.md — what “eval” measures (M₁–M₉)
- @sources/devfun-poker-agent-challenge-onepager-2026-06-18.md — funnel wording (sandbox → champions → finale)

## Narrative

### Eval is the gate

The public Challenge funnel is **sequential**, not a menu of equal options:

1. **Sandbox eval** — submit agent, score on leaderboard (**trajectory + multi-axis**; BenchFlow on rails).
2. **Publish** — top agents become **champion bots** others challenge.
3. **Finale** — top LB vs Dwan/Jungleman (HU stream).

Steps 2 and 3 are **rewards for clearing step 1**. Optimizing Playground S3 rank, Eval S1 500h bb/100, or local selfplay bb/100 **without** trajectory/axis discipline is optimizing the wrong game.

Raeth (2606.13815) reinforces this: **#1 chips ≠ #1 mean axis score**. Researcher eval is likely to punish **salient axis holes** (bet sizing, positional spread, reasoning hallucination) even when chip delta is acceptable.

**Default optimization target:** **HU** sandbox **trajectory + axis gates** + leak discipline (`CEMINI_TABLE_FORMAT=hu`, 2-player selfplay). 6-max = Playground intel only.

**Table format is confirmed** [CONFIRMED 2026-06-08] — see `@sources/devfun-researcher-track-hu-format-2026-06-08.md`. Still read `skillFile` for rubric, hand count, and economics.

### Sit-down rule — no hands before recon

Do **not** run `pokerkit run`, flip prod lobby, or burn buy-in until this ritual completes and operator signs the decision block.

| Phase | When | Output |
|-------|------|--------|
| **A. Discover** | Daily from Jun 18 → comp appears | `list_arena_competitions.sh` |
| **B. Recon** | First sight of Researcher comp + **before every format change** | `run_researcher_comp_recon.sh` |
| **C. Decide** | Human reads report + skillFile | Filled checklist below |
| **D. Gate** | After decisions locked | `run_hu_sandbox_gate.sh --hands 500` with `CEMINI_TABLE_FORMAT=hu` |
| **E. Submit** | Gate PASS | smoke `pokerkit run --max-hands 50` → season → trajectory export |

### Phase B — automated recon

```bash
cd agents/devfun-poker-arena

# Daily until candidate appears
bash scripts/list_arena_competitions.sh

# When Researcher comp id known
bash scripts/run_researcher_comp_recon.sh --competition-id '<id>' --write-wiki-stub
```

Writes `reports/researcher-round/recon-<ts>/`:

- `recon-<ts>.md` — human-readable report + optimization matrix
- `introspection.json` — live API schema
- `skillFile.md` — fetched when API provides URL
- `competition_candidates.json` / `target_competition.json`

Manual supplements (automation does not replace):

- Read Discord `#researcher-track` + any BenchFlow / Daytona docs linked at launch
- Open https://b-arena.dev.fun/skills/ if skill path is non-obvious
- Compare one-pager finale (HU) vs sandbox skill (table size, hand count, rubric)

### Phase C — operator decision checklist

Copy into recon report or brief; **all boxes** before first submit:

- [ ] **Competition id** pinned → `ARENA_RESEARCHER_COMP_ID`
- [ ] **Table format** — **HU** [CONFIRMED 2026-06-08] — cite skillFile for any override
- [ ] **Scoring rubric** — **TrueSkill** LB [CONFIRMED email]; trajectory / axis weights from skillFile
- [ ] **Submission surface** — Kaggle vs `pokerkit run` vs SDK-only (cite email / rules URL)
- [ ] **Style rep criterion** — Dwan/Jungleman style-match overlays if aiming for pro representation
- [ ] **Match cadence** — smoke N hands vs multi-day season vs 500h reset panel
- [ ] **Economics** — entry fee, rebuy, stack reset rules
- [ ] **Reasoning policy** — sanitize off on submit (`CEMINI_SANITIZE_OUTPUT=0` + Researcher mode)
- [ ] **Memory** — F6 on/off per ablation if skill mentions session memory
- [ ] **Optimization target sentence** — one line: “We are optimizing for X because skillFile says Y”
- [ ] **Regression scope** — HU full (`test_hu_regression`) + 500h 2p selfplay gate
- [ ] **Prod flip** — `CEMINI_RESEARCHER_MODE=1`, lobby comp id, `AGENT_VERSION` bump

### What to optimize (decision matrix)

| If skillFile emphasizes… | Optimize for… | De-prioritize… |
|--------------------------|---------------|----------------|
| Trajectory / action logs | Export + M₈/M₉ gates every run | Raw Playground rank |
| Multi-axis / cognitive profile | Cross-axis consistency (M₁,M₇,M₉ floor) | Single-axis aggression |
| **TrueSkill HU sandbox** | Win rate vs SDK opponent mix + axis gates | Playground chip rank |
| 6-max Playground | `CEMINI_TABLE_FORMAT=6max`, gin + seat matrix | Confusing Playground rank with Researcher eval |
| BenchFlow / fixed panel | Panel-shaped opponents + stamina | Tournament survival lanes |
| Published champions | Eval admission (step 1) | Stream HU prep until published |

### Phase E — submit bundle

**Interface [CONFIRMED Discord 2026-06-20]:** builders upload **agent bundle files** to sandbox (heuristic / LLM / weights / solver). Full layout **pending** — see `@sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md`. Until spec drops:

```bash
export ARENA_RESEARCHER_COMP_ID='<id>'
CEMINI_TABLE_FORMAT=hu bash scripts/run_hu_sandbox_gate.sh --hands 500
./pokerkit run --agent examples/cemini_decide.py --max-hands 50   # smoke
./scripts/export_researcher_trajectory.sh --competition-id "$ARENA_RESEARCHER_COMP_ID"
```

**Do not** pivot to runtime LLM submit — devs recommend pure-code agents for sandbox cost/quality.

Post `axis_summary.json` + link to trajectory bundle in researcher channel per Discord norms.

## Snippets

> "Top agents go live as champion agents that everyone else can come and challenge." [Source: devfun-poker-agent-challenge-onepager-2026-06-18.md]

> "Tournament chips and aggregate axis score order the field differently." [Source: arXiv:2606.13815 — see @sources/arxiv-poker-arena-multi-axis-2606-13815-2026-06-18.md]
