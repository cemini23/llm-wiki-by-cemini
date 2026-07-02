---
title: dev.fun Researcher — pro style targets (Dwan vs Jungleman)
type: concept
tags: [concept, poker, devfun, researcher-track, heads-up, villain-profile]
keywords: [tom-dwan, jungleman, style-emulation, TrueSkill, HU, nemesis, durrrr]
related:
  - concepts/devfun-researcher-track-readiness-2026-06.md
  - concepts/devfun-poker-agent-challenge-2026.md
  - concepts/poker-arena-multi-axis-cognitive-profile.md
  - sources/devfun-poker-researcher-track-email-2026-06-19.md
  - sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md
maturity: validated
created: 2026-06-19
updated: 2026-06-08
cross-wiki:
  - "@gambling-wiki/entities/people/tom-dwan.md"
  - "@gambling-wiki/entities/people/daniel-cates-jungleman.md"
  - "@gambling-wiki/sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md"
  - "@gambling-wiki/entities/bots/cemini-devfun-poker-agent.md"
  - "@gambling-wiki/sources/research-k122-poker-paper-landscape-2026-06-19.md"
---

## Relations

- @gambling-wiki/entities/people/tom-dwan.md — `durrrr` archetype (image + merge + pressure)
- @gambling-wiki/entities/people/daniel-cates-jungleman.md — `jungleman` archetype (HU frequency + balance)
- @gambling-wiki/sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md — synthesis source
- @concepts/devfun-researcher-track-readiness-2026-06.md — TrueSkill + trajectory gates

## Narrative

### Why this matters now

Researcher email: Dwan + Jungleman **pick bots that play most like them** — not only TrueSkill #1. Two **different** style targets; merging them loses fidelity.

| Track | Use profiles |
|-------|----------------|
| **Researcher HU sandbox** | **Emulate** Jungleman-shaped aggression for TrueSkill + rep; optional Dwan merge lane |
| **Pro Table Finale** | **Exploit** overlays when `villain_id` known |
| **Playground 6-max** | **Do not load** — wrong format |

### Archetype contrast [CONFIRMED gambling-wiki profiles]

| Dimension | **Tom Dwan (`durrrr`)** | **Daniel Cates (`jungleman`)** |
|-----------|-------------------------|--------------------------------|
| **Core edge** | Image, fear, oversized pressure, range merge | HU pot frequency, structural 3-bet, decision-tree balance |
| **Preflop** | Trash 4-bets, wide deep opens | High 3-bet (~20–25%+ HU peak) [TENTATIVE]; 56s > QTs as 3-bet bluff |
| **Postflop** | Overbets, multi-street bluffs, turns value into bluffs | Small-ball probes, thin HU value, semi-bluff CR |
| **Durrrr Challenge** | Lost ~$1.2–1.5M over ~20k HU hands | Won via **light call-down + merge** vs Dwan bluffs |
| **Rep pick read** | “Plays like Dwan” = pressure + merge theatrics | “Plays like Jungleman” = **wide HU fight + balanced aggression** |

**Cemini default emulation target:** **Jungleman** — aligns with HU TrueSkill (win pots, defend wide, sufficient PFR). Dwan lane is higher-variance merge/overbet — secondary A/B for rep selection.

### Agent play style (TrueSkill + rep)

What `cemini_wiki_poker` should **look like** in HU sandbox trajectory:

| Knob | Anti-pattern (K118 / Playground nit) | **Jungleman-shaped target** |
|------|--------------------------------------|-----------------------------|
| **VPIP / PFR** | ~9% / ~1% tournament nit | **Wide HU** — fight for blinds, probe small pots |
| **3-bet** | Chart-tight only | **Structural high** — suited connectors as bluff 3-bets |
| **Blind defense** | Over-fold | **Defend wide**; raise vs small probes |
| **Passivity** | Bleeds vs Jungleman archetype | **Raise** when opponent auto-check-folds |
| **Bluffing** | Obvious air | **Selective** — merge on credible stories |
| **Axis gates** | M₇ entropy floor, M₉ BTN–BB spread | Still required — aggression must stay **consistent** in trajectory |

Dwan emulation adds: larger sizing, more merge lines, thinner value — risks M₈ reasoning leaks if reasoning doesn’t match action mix.

### Finale exploit overlays (when seated vs human)

Not implemented in `cemini_decide.py` yet (`durrrr` / `jungleman` not in `nemesis_seed` / `villain_archetype`).

**Update 2026-06-08:** Finale exploit overlay **shipped** as separate lane — `CEMINI_FINALE_EXPLOIT=1` + `CEMINI_FINALE_VILLAIN=durrrr|jungleman`; default ladder bundle **excludes** `finale_*.py`. See `agents/devfun-poker-arena/briefs/2026-06-08_human-table-exploit-layer-brief.md`.

| vs | Exploit direction |
|----|-------------------|
| **Dwan** | Call wider vs bombs; thinner value; **fewer** bluffs into call-down |
| **Jungleman** | Wide defend; **raise** probes; fix passive PFR; selective bluffs vs merged lines |

Gambling-wiki entity tables: `@gambling-wiki/entities/people/tom-dwan.md` § Bot counter-strategy, `@gambling-wiki/entities/people/daniel-cates-jungleman.md` § Bot counter-strategy.

### Code backlog (private repo)

1. `CEMINI_RESEARCHER_STYLE_TARGET=jungleman|dwan|balanced` — HU sandbox **emulation** profile (ladder grind; separate from finale exploit) — **open**
2. **`CEMINI_FINALE_VILLAIN` + `villain_id` HUD** — **shipped 2026-06-08** (`finale_villain.py`, `opponent_hud_stub.py`; excluded from default sandbox bundle)
3. HU selfplay **`durrrr_bomb` / `jungleman_calldown`** bots + `run_hu_sandbox_gate.sh --finale` — **shipped 2026-06-08**
4. Trajectory **`export_researcher_trajectory.sh --tag finale-*`** — **shipped 2026-06-08**; operator review before stream still required

**Do not** wire Dwan/Jungleman overlays into Playground `CEMINI_NEMESIS_HANDLES` — those handles are arena bot names, not pro profiles.

### K122 literature → F6 only (no runtime LLM)

K122 paper landscape (`@gambling-wiki/sources/research-k122-poker-paper-landscape-2026-06-19.md`) maps 2024–2026 poker-agent lit to **pure-code** HU posture. Actionable lanes:

| Literature lane | Maps to | Not in prod `decide()` |
|-----------------|---------|------------------------|
| AlphaExploitem, StratFormer, Readable Minds | **F6** session / showdown memory | — |
| ToolPoker, PokerSkill | **F12–F13** offline solver patches (HL loop) | Runtime solver |
| SpinGPT, SPIRAL | — | **REJECT** — runtime LLM training paths |

**Rule:** K122 literature informs **F6 memory + offline HL** only. No runtime LLM in `decide()`; no `CEMINI_RESEARCHER_STYLE_TARGET` overlays until Jun 21 rules confirm interface. Dwan/Jungleman **profiles** stay study targets — see `@gambling-wiki/concepts/heads-up-arena-strategy.md`.

### Study sources

- HSP tape: `@gambling-wiki/sources/youtube-pokergo-dwan-hsp-mega-compilation-2026-06-03.md`
- Web synthesis: `@gambling-wiki/sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md`
- K122 papers: `@gambling-wiki/sources/research-k122-poker-paper-landscape-2026-06-19.md`

## Dead Ends

- **One LAG profile for both pros** — wrong for rep fidelity
- **HSP 2008 frequencies as exact 2026 targets** — both evolved (GTO Wizard era)
- **Playground nemesis tight vs Dwan bombs** — opposite of correct finale defense
