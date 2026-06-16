# Game Dev Wiki — Operations Log

Append-only chronological log.

---

## [2026-06-16] ingest | Phase-0 closeout + inbox triage + brief sync

- Phase-0 audits: @sources/stronghold2-analyse-hub-phase-0-audit-2026-06-13.md, @sources/stronghold2-mp-ai-patch-phase-0-audit-2026-06-13.md, @sources/gamedev-resources-phase-0-audit-2026-06-13.md
- Inbox: 7 arXiv PDFs rejected (robotics/sports/AV) → @sources/inbox-arxiv-reject-batch-2026-06-16.md; archived to egress
- Tool Evaluation docx duplicate — skipped (already @sources/tool-evaluation-cross-wiki-routing-2026-06-13.md)
- Briefs: `sh2-mp-ai-patch-install.md`, `sh2-analyse-hub-install.md`, `story-011-tier2-hunters-meat.md` → rsync to `castle-sim/briefs/`
- Entity maturity bumps: stronghold2-analyse-hub → validated

---

## [2026-06-13] research | GitHub Stronghold 2 ecosystem scan

- Swept GitHub for SH2 patches, trainers, S2M tools; no Crusader-scale UCP equivalent
- MIT adopt: MP-AI patch (Jpnock), AnalyseHub (crycodebaby); entity pages added
- Reference-only: Eren121 SiegeExporter (.s2m), Ald0s trainer (player struct offsets)
- New: @concepts/stronghold-2-github-ecosystem-shelf.md, @sources/github-stronghold-2-scan-2026-06-13.md
- Cross-linked @concepts/stronghold-modding-ecosystem-shelf.md (Crusader vs SH2 split)

---

## [2026-06-13] ingest | SH2 targeted mechanics (parallel play session)

- Scraped SH2 Heaven: popularity, resources, cservices1–3, industry1–3, civilian1–2, FAQ gameplay
- New concepts: popularity model, crime/punishment loop, economy chains, architect controls
- Source: @sources/stronghold-2-heaven-targeted-2026-06-13.md
- Playtest checklist: `briefs/research/sh2-playsession-checklist.md` (gitignored)
- Parent @concepts/stronghold-2-systems-inventory.md cross-linked; index updated
- Deferred: military unit stat pages, castle structure 404s

---

## [2026-06-13] implement | story-005 M0.3D architect spike (Fork B)

- Scope pivot: story-005 = Godot 3D SH2 architect camera + wall paint + peasant path
- `scenes/game_3d/architect_test.tscn` now main scene; 2D `game.tscn` = logic lab
- `architect_3d_test` PASS; 2D regression via explicit scene paths
- D-024 logged; operator manual 5m @ 60fps still open

---

## [2026-06-13] implement | story-010 Tier 2 bread chain

- Wheat farm → stockpile → mill → flour → bakery → granary bread
- D-019 stub removed; D-023 SH1/SH2 food north star logged
- `food_test` updated for full chain (50s); v0/lord regression PASS
- Next: story-011 hunters + meat

---

## [2026-06-13] implement | story-009 Tier 2 simplified AI lord

- Enemy keep east; lord builds westward walls + escalates raid waves
- Archers siege `EnemyKeep`; HUD shows lord name / HP / walls
- `lord_test` PASS; raid + v0 regression unchanged
- Tier 2 core slices complete — next: food chain (D-019) or barracks roster

---

## [2026-06-13] implement | story-008 Tier 2 wave raids

- `RaidDirector` timer waves from west; raiders path to keep; archers engage `CombatTarget`
- HUD: wave / live raiders / kills / breaches; raids start on keep placement
- `raid_test` PASS; Tier 1 + food + stone regression unchanged
- Next Tier 2: food chain (wheat/mill), barracks roster, or simplified AI lord

---

## [2026-06-13] implement | story-007 Tier 2 stone / quarry

- Stone deposits on map, quarry placement, miners → stockpile stone counter
- `stone_test` PASS; food + Tier 1 regression unchanged
- Deferred: wheat→mill→bread chain (D-019)

---

## [2026-06-13] implement | story-006 Tier 2 food + popularity

- Granary, Farm (apple), Bakery (bread), farmer job loop, popularity-driven immigration
- `food_test` headless PASS; Tier 1 regression unchanged
- Next Tier 2: stone/quarry or wave raids (operator pick)

---

## [2026-06-13] implement | story-005 placeholder art

- Kenney-style 32×32 PNGs in `castle-sim/assets/placeholders/` (generator: `tools/art/generate_placeholders.py`)
- `PlaceholderArt` autoload; procedural `_draw()` wired to textures; peasant 4-frame walk
- Wiki checklist in `art-pipeline-v0-requirements.md` marked complete
- All headless tests PASS; isometric TileMap still W3

---

## [2026-06-13] implement | story-004 stagehand L0 smoke

- godot-stagehand addon pinned (`9a6ce19`) in castle-sim `addons/stagehand/`
- L0 script: `scripts/ci/stagehand_l0_smoke.sh` — TIME_FPS ≥ 55 × 30s on pathfinding spike
- Two consecutive local runs PASS; headless CLI tests unchanged
- Next W2 item: optional L1 UI clicks or story-005 art

---

## [2026-06-13] implement | story-003 Tier 1 close-out

- Audit P0/P1 fixes merged in castle-sim; `labor_contention_test` added (wood cap regression)
- Wiki: `vertical-slice-v0.md` § Tier 1 rendering — top-down accepted for Tier 1 (D-014)
- `entities/projects/castle-sim.md` — Tier 1 close-out done; next: story-004 stagehand L0

---

## [2026-06-13] decision | Fork B — Godot 3D SH2 clone

- Operator locked **Fork B** (3D); 2D rejected as wrong product feel
- New: `concepts/godot-3d-sh2-architect-spike-plan.md`, `briefs/story-005-3d-architect-spike.md`
- D4 closed; Mac SH2 reference via CrossOver Steam Edition
- Next implementation gate: M0.3D architect camera + wall paint + one peasant

---

## [2026-06-13] research | Stronghold 2 personal clone — operator north star

- Operator intent: personal SH2 copy (no sale/redistribution); supersedes SH1-only wiki default
- New: `concepts/stronghold-2-systems-inventory.md` (honour, crime, kingmaker ranks, popularity)
- New: `concepts/operator-vision-sh2-personal-clone.md` (Fork A/B/C, legal boundary)
- Sources: SH2 Heaven gameinfo, MobyGames snapshot; linked GameSpy Bradbury Q&A
- Brief: `briefs/GDD-sh2-personal-clone.md` — phased clone ladder aligned to Kingmaker ranks
- Open: **D4** 2D mechanics vs Godot 3D rebuild

---

## [2026-06-13] phase-0 | SerpentAI + Airtest + UCP2 audits + W2 briefs

- Phase-0 clones: SerpentAI (STEAL-FROM/NO-GO install), Airtest (CONDITIONAL-GO @ccc), UCP2 (STEAL-FROM study)
- Sources: serpent-ai, airtest, unofficial-crusader-patch2 phase-0 audits
- Briefs (local): W2-harness-kickoff, story-003 tier1-closeout, story-004 stagehand L0, systems/aiv-design-notes
- Entity pages updated; WORKFLOW story index extended

---

## [2026-06-13] ingest | Tool Evaluation cross-wiki batch — 56 targets

- Source: `research to be indexed/Tool Evaluation and Wiki Fit.docx` → `sources/tool-evaluation-cross-wiki-routing-2026-06-13.md`
- Concepts: tool-evaluation-cross-wiki-batch, stronghold-modding-ecosystem-shelf, deferred-engine-candidates
- Entities: serpent-ai, airtest (CCC primary), unofficial-crusader-patch2, gamedev-resources
- Post-ingest gh api: OpenSHC GPL-3.0, Path-Creator MIT, AI-Aimbot GPL-3.0
- Cross-wiki stubs queued: CCC (SerpentAI, Airtest, AITradeGame), cybersec (UCP2, AI-Aimbot), image-gen (GameDev-Resources)
- Aggregate: 1 Adopt, 5 Steal-from, 2 Defer, 2 Reference, 37 Reject, 9 UNAVAILABLE

---

## [2026-06-13] implement | castle-sim M0–M1.5 + v0 playtest PROCEED

- M0 pathfinding spike PROCEED; M1 vertical slice v0 operator playtest steps 1–5 passed (~10m @ 60fps)
- story-002 labor delegation complete (Keep, hovel, JobAssigner, no P-spawn)
- Refactor: generic peasant loop + `JobBehavior` / `WoodcutterJobBehavior` (D-012, D-013)
- Implementation log: `castle-sim/docs/PROJECT_LOG.md` (decision register + session history)
- Headless regression: `spike_test`, `v0_test`, `labor_test`, `archer_stress`
- Tier 1 still open: placeholder art, isometric TileMap (or documented top-down exception)
- Tier 2 (food, popularity, stone) explicitly deferred pending operator GO + wiki plan

---

- `briefs/WORKFLOW.md` — CCGS P0 skills port (local gitignored)
- Shaggydev: tactics engine + UDD navigation sources → godot-pathfinding-patterns Pattern 7
- papierkorp: grid tactical movement tutorial (UI/range reference)
- GDC Total War siege AI ingested (GDC blurb + TW forum recap); rts-siege-ai-reference validated
- godot-stagehand CI smoke plan + eval source (W2 execute in castle-sim)
- ROADMAP W4 devlog/GDC/stagehand items closed

---

## [2026-06-13] ingest | Phase-0 tool audits + CI lint fix

- Phase-0: hi-godot-ai, sods2-godot-mcp, godot-stagehand, godot-ai-playtest, CCGS (steal-from)
- Fixed `@wiki/index.md` body mentions → backtick paths (wiki_lint --fail-on-dangling)
- Entity verdicts updated; godot-mcp-landscape Phase-0 table complete

---

## [2026-06-13] ingest | Exa NPC + PCG + CCGS — 11 clusters, 82 URLs

- Three-lane pass: runtime LLM NPCs, agentic PCG, CCGS deep extraction
- New concepts: llm-npc-runtime-ai-shelf, agentic-npc-design-guardrails, agentic-pcg-level-design, ccgs-workflow-extraction
- New sources: Ubisoft Teammates, NVIDIA ACE Qwen3, iXie guardrails, AgenticPCG, CCGS workflow catalog, Starlog review, LLMUnity/morganpage stubs
- Updated: claude-code-game-studios entity, agent-harness-castle-project, scope-tiers Tier 3 cuts

---

## [2026-06-13] ingest | Exa AI game-dev tools — 10 clusters, 81 URLs

- Broad AI gamedev research (not castle-specific) → `wiki/sweeps/2026-06-13-exa-ai-gamedev-tools-batch.json`
- New concepts: ai-assisted-game-dev-workflows, ai-game-dev-tool-stack-2026
- New entities: hi-godot-ai, godot-stagehand, godot-ai-playtest
- New sources: Catvivors/Claude Code, Shin KoiKoi, Lava Leap, Void Balls, Luden GDD prototype, Exa batch meta
- Updated: claude-code-game-studios, godot-mcp-landscape, agent-harness-castle-project

---

## [2026-06-13] ingest | Exa flow-fields + Firefly batch — 8 clusters, 68 URLs

- Second Exa pass → `wiki/sweeps/2026-06-13-exa-flowfields-firefly-batch.json`
- **No Firefly/Stronghold GDC postmortem found** — ingested Bradbury GameSpy SH2 Q&A + adjacent sources instead
- New concept: `flow-field-pathfinding` (cost/integration/flow, Emerson tiles, Tier 2 gate)
- New sources: Emerson Game AI Pro, Leif Node, Vav Labs Godot, Red Blob Games, GameSpy SH2, Firefly about-us, Legends making-of stub
- Updated: rts-pathfinding-approaches, godot-pathfinding-patterns, indie-kingdom-builder-lessons

---

## [2026-06-13] ingest | Exa deep batch — 10 clusters, 71 URLs

- Ran automated digest + custom Exa deep batch → `wiki/sweeps/2026-06-13-exa-deep-batch.json`
- New concepts: rts-pathfinding-approaches, godot-pathfinding-patterns, indie-kingdom-builder-lessons, medieval-sim-fun-vs-accuracy, rts-networking-deferred, rts-siege-ai-reference
- New sources: GDC K&C, Bradbury SH3 interview, Northgard case study, Leiden accuracy essay, Liquid Fire pathfinding, lockstep paper, Exa batch meta
- New entity: godot-mcp-landscape (WATCH)
- Tightened `daily_research_config.yaml` paper queries (filter UAV noise)

---

## [2026-06-13] ingest | Stronghold franchise + sibling scan + castle-sim scaffold

- Deep research: `concepts/stronghold-systems-inventory.md` (SH1 buildings/units/economy, Crusader/SH2+ deltas)
- Updated `entities/games/stronghold-series.md` (engines, timeline, modes)
- Sources: `stronghold-hd-manual-2001.md`, `stronghold-series-wikipedia-2026-06-13.md`
- Meta: `meta/sibling-wiki-inventory.md` — ccc / image-gen / cybersec / osint map
- Concept: `art-pipeline-v0-requirements.md` → @image-gen-wiki
- Entity: `entities/projects/castle-sim.md`
- Vertical slice v0 tightened (spike gate, SH1 mapping, playtest script)
- Harness: CCC ship/verify/scatter-gather + cybersec MCP links
- Implementation: `/Users/claudiobarone/Desktop/projects/castle-sim/` (Godot 4.5 scaffold)
- ROADMAP W1 marked complete

---

## [2026-06-13] ingest | Godot 4 Phase-0 audit

- Deep-read: license (MIT), Mac universal editor 4.5.2 smoke test, grid-kit scan (MarkoDM GDS), pathfinding (`AStarGrid2D` vs navmesh)
- Verdict **CONDITIONAL-GO** on `entities/engines/godot-4.md` — unblocks `castle-sim` repo
- Source: `sources/godot-4-phase-0-audit-2026-06-13.md`
- ROADMAP W1: Phase-0 checkbox closed

---

## [2026-06-13] bootstrap | K115 — game-dev-wiki federation

- Created repo from Cemini federation template (Gambling-wiki / Cybersecurity-wiki pattern)
- `CLAUDE.md` — scope: hobby castle/RTS research + agent harness; code in separate repos
- Seed **5 concept** pages, **3 entity** pages, **1 source**, **2 meta** pages
- Federation alias: `game-dev-wiki` (public)
- Cross-wiki: `@osint-wiki/concepts/game-dev-wiki-federation.md` pointer hub
- Daily digest: federated install `game-dev` wiki-id; LaunchAgent staggered
- GitHub: `cemini23/Game-Dev-wiki`
- CCC eval v7 — surface 9
