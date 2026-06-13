# Game Dev Wiki — Operations Log

Append-only chronological log.

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
