---
title: dev.fun Heads-Up PvP S3 (Researcher sandbox candidate)
type: entity
tags: [entity, platform, poker, devfun, researcher-track, heads-up, k126]
keywords: [Heads-Up PvP S3, TrueSkill, eval-pvp, sandbox, competitionId, cmqnvili2002gwb82l1qba0gm]
related:
  - entities/platforms/devfun-arena.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/devfun-researcher-pre-submit-recon.md
  - concepts/kuhn-poker-sft-curriculum-reference.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
maturity: draft
created: 2026-06-22
updated: 2026-06-22
---

## Relations

- @entities/platforms/devfun-arena.md — platform ladder
- @concepts/devfun-researcher-track-readiness-2026-06.md — ops hub
- @concepts/devfun-researcher-pre-submit-recon.md — pre-submit ritual

## Raw Concept

What prompted this page: `list-active` surfaced **[Poker] Heads-Up PvP S3** as the likely Researcher Round HU sandbox target ahead of public announcement. Operator posture: **wait for official announce** before prod flip.

## Narrative

| Field | Value |
|-------|-------|
| **Name** | [Poker] Heads-Up PvP S3 |
| **competitionId** | `cmqnvili2002gwb82l1qba0gm` [OPEN QUESTION 2026-06-22] |
| **Format** | Heads-up PvP sandbox |
| **skillFile** | `eval-pvp.md` (server-hosted PvP sandbox) |
| **Scoring** | TrueSkill (HU pairwise) per Researcher track email |

**Prod pin (when live):**

```bash
ARENA_RESEARCHER_COMP_ID=cmqnvili2002gwb82l1qba0gm \
  bash scripts/researcher_jun21_beta_apply.sh --skip-checklist
```

**Submit path:** Discord [CONFIRMED 2026-06-20] bundle files → sandbox eval — not confirmed as lobby `texas/join` for this comp. Run `run_researcher_comp_recon.sh` on announce.

**Code defaults:** `pick_researcher_competition.py` prefers Heads-Up PvP over legacy beta sandbox; constant `HEADS_UP_PVP_S3_COMP_ID` in repo.

## Snippets

> "Pin when Heads-Up PvP S3 is publicly joinable" [Source: agents/devfun-poker-arena/examples/pick_researcher_competition.py (2026-06-22)]
