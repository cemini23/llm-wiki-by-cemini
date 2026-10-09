---
title: Agent harness — castle sim project
type: concept
tags: [concept, agents, harness, codex, opus, fable]
keywords: [agent-swarm, codex, opus, fable, planner, executor, milestone-gates]
related:
  - concepts/game-dev-wiki-scope.md
  - concepts/vertical-slice-v0.md
  - concepts/indie-kingdom-builder-lessons.md
  - concepts/ai-assisted-game-dev-workflows.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/ccgs-workflow-extraction.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - entities/tools/godot-stagehand.md
  - entities/tools/gamedevbench.md
  - sources/gamedevbench-phase-0-audit-2026-06-21.md
  - entities/tools/claude-code-game-studios.md
  - entities/tools/godot-mcp-landscape.md
  - meta/sibling-wiki-inventory.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
  - entities/projects/castle-sim.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md
  - entities/tools/hi-godot-ai.md
  - entities/tools/ziva-godot-agent.md
  - sources/ziva-godot-agent-phase-0-audit-2026-06-21.md
  - sources/inbox-arxiv-reject-batch-2026-06-30.md
  - sources/protocolbench-llm-multiagent-protocol-shelf-2026-06-24.md
  - sources/godot-engine-ai-contribution-policy-2026-07-01.md
  - sources/arxiv-2606.29932-saga-civrealm-strategy-agents-2026-07-05.md
  - entities/engines/godot-4.md
  - concepts/tycho-arc-agi-active-abstraction-stub.md
  - sources/arxiv-2607.03525-gameenginebench-harness-2026-08-15.md
  - sources/inbox-arxiv-reject-batch-2026-09-19.md
  - concepts/twin-test-time-world-model-stub.md
  - concepts/vibeworlding-3d-agent-stub.md
  - sources/arxiv-2609.21562-gamelogicbench-runtime-logic-2026-09-24.md
  - entities/tools/gamelogicbench.md
  - sources/arxiv-2609.23142-craftbench-ue-deterministic-eval-2026-09-24.md
  - sources/arxiv-2609.27606-state-grounded-conditioning-2026-09-24.md
  - sources/inbox-arxiv-reject-batch-2026-09-24.md
  - sources/arxiv-2609.31076-abstraction-ladder-code-skills-2026-09-30.md
  - sources/arxiv-2609.34214-glyphbench-rl-playground-2026-09-30.md
  - sources/arxiv-2609.35928-prompted-identity-factionalism-2026-09-30.md
  - sources/arxiv-2609.37658-enterprisebench-strategic-agents-2026-09-30.md
  - entities/tools/codehack.md
  - entities/tools/firmbench.md
  - sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md
  - sources/arxiv-2610.01514-audit-rule-faithful-explanations-2026-10-03.md
  - sources/inbox-arxiv-reject-batch-2026-10-03.md
  - concepts/minecraft-agent-harness-shelf.md
  - entities/tools/mineflayer.md
  - entities/tools/minecraft-agent-mcp-shelf.md
  - sources/minecraft-modding-deep-research-2026-10-05.md
  - sources/arxiv-2610.03695-queen-chess-explains-moves-2026-10-05.md
  - sources/arxiv-2610.03253-default-following-collective-action-2026-10-05.md
  - sources/inbox-arxiv-reject-batch-2026-10-05.md
  - sources/cross-wiki-routed-briefs-2026-10-05.md
  - sources/arxiv-2610.04672-masbench-partial-observability-2026-10-07.md
  - sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md
  - sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md
  - sources/arxiv-2610.08076-speedrunbench-strategy-formation-2026-10-07.md
  - sources/arxiv-2610.08720-worldsolver-visual-fidelity-2026-10-07.md
  - sources/inbox-arxiv-reject-batch-2026-10-07.md
  - sources/arxiv-2610.11464-who-verifies-the-verifier-2026-10-09.md
  - sources/arxiv-2610.09371-confidence-game-delegation-2026-10-09.md
  - sources/arxiv-2610.09683-system-switch-fast-slow-gate-2026-10-09.md
  - sources/arxiv-2610.11794-memento-3-reflective-rulebooks-2026-10-09.md
  - sources/inbox-arxiv-reject-batch-2026-10-09.md
maturity: draft
created: 2026-06-13
updated: 2026-10-03
wire_status: policy_wired
wire_target: briefs/W2-harness-kickoff.md
---

## Relations

- @concepts/ai-assisted-game-dev-workflows.md — **general** AI game dev patterns (any project)
- @concepts/ai-game-dev-tool-stack-2026.md — MCP, automation, CCGS catalog
- @ccc-wiki/entities/tools/claude-code-game-studios.md — role graph steal-from
- @ccc-wiki/concepts/ship-subagent-writer-reviewer-tester.md — writer + tester → reviewer gate
- @ccc-wiki/concepts/agent-completion-verification-gates.md — done = tests + playtest
- @ccc-wiki/entities/patterns/scatter-gather.md — parallel Godot subsystems
- @ccc-wiki/concepts/skill-vetting.md — before untrusted skills
- @cybersecurity-wiki/concepts/mcp-security-posture.md — MCP admission (W2+)
- @cybersecurity-wiki/concepts/agent-skill-injection.md — SKILL.md poisoning
- @meta/sibling-wiki-inventory.md — full cross-wiki map

## Raw Concept

Model matrix and milestone gates for agent-assisted hobby game dev. Research phase uses wiki; execution phase uses per-slice Codex swarms.

## Narrative

### Roles

| Role | Model (2026-06-13) | Fallback when Fable returns |
|------|-------------------|----------------------------|
| **Planner / designer** | `claude-opus-4-8-thinking-high` | `claude-fable-5-thinking-high` |
| **Implementer swarm** | `gpt-5.3-codex` | same |
| **Third lens** | `gemini-3.1-pro` | art/spec review |

Fable withdrawn from Cursor subagents 2026-06-13 — Opus is default planner. [CONFIRMED — @ccc-wiki cursor-audit reference]

### Per-milestone workflow

1. **Research** — ingest sources into this wiki; update slice spec
2. **Plan** — Opus writes task breakdown in `briefs/` (gitignored) from wiki spec — use CCGS P0 skills as checklist (@concepts/ccgs-workflow-extraction.md)
3. **Execute** — Codex subagents implement **one subsystem** in `castle-sim` repo (`/dev-story` equivalent)
4. **Verify** — operator playtest + automated lint/tests; `PROCEED/PIVOT/KILL` on M0/M1 (@concepts/vertical-slice-v0.md)
5. **Promote** — update concept maturity when slice criteria pass

### Anti-patterns

- One prompt → full RTS
- Executor agents changing scope without planner pass
- Skipping playtest gate

### Steal-from

`Donchitos/Claude-Code-Game-Studios` — planner / implementer / reviewer edges only (`@entities/tools/claude-code-game-studios.md`).

GameDevBench (Godot task zips) vs GameEngineBench (UE5 paper rubric, no pin): @entities/tools/gamedevbench.md · @sources/arxiv-2607.03525-gameenginebench-harness-2026-08-15.md. Tycho / Twin / VibeWorlding harness depth stays CCC-primary (@concepts/tycho-arc-agi-active-abstraction-stub.md · @concepts/twin-test-time-world-model-stub.md · @concepts/vibeworlding-3d-agent-stub.md).

### W2 MCP policy (Phase-1 wired)

| Tool | wire_status | Rule |
|------|-------------|------|
| godot-stagehand | policy_wired | L0 smoke only — story-004 pattern |
| hi-godot-ai | policy_wired | Sandbox clone; read-only MCP first; no writes until operator OK |
| sods2-godot-mcp | policy_wired | Alt if Node/debugger needed — pick one MCP stack |
| hera-agent-godot | policy_wired | Godot 4.7+ pin gate; low-token CLI adjunct — not default executor |
| ziva-godot-agent | deferred | Proprietary Asset Store — eval only |
| SerpentAI / CCGS full | wont_wire | STEAL-FROM patterns in WORKFLOW.md — no install |
| GameLogicBench | policy_wired | Tick-level runtime assertions — steal pattern; **NO-GO clone** (no LICENSE) |
| CraftBench-UE | wont_wire | MIT UE reference only — deterministic eval shape for Godot stories |

Canon table: `briefs/W2-harness-kickoff.md` § MCP admission.

### Eval bench ladder (2026-09-24) [CONFIRMED]

| Bench | Engine | Verdict | castle-sim use |
|-------|--------|---------|----------------|
| GameDevBench | Godot | STEAL-FROM | Task zips + validate_tasks |
| GameLogicBench | Agnostic | STEAL-FROM (no SPDX) | Mid-run rule asserts |
| CraftBench-UE | UE | extract-only MIT | Fresh-project deterministic checks |
| GameEngineBench | UE paper | citation only | Taxonomy tags for `*_3d_test` |
| FirmBench / EnterpriseBench | Agnostic | **CONDITIONAL-GO** Apache-2.0 | Beer-Game delayed-feedback lens — deferred |
| GlyphBench | Agnostic | citation only (no repo pinned) | Unicode-grid state rendering hint |
| CodeHack | NetHack | **CONDITIONAL-GO** MIT | Skill-vs-primitive design pattern |
| MASBench | Agnostic | CONDITIONAL-GO MIT (1★) | Collaboration taxonomy: Protocol / Memory / Routing + **communication cost** |
| Learn2Play | Text games | citation only | **Complete records beat summaries** — learning substrate |
| SpeedrunBench | 9 games | citation only | Self-improvement measurement shape |
| WorldSolver | Graphics sim | citation only | **Visual fidelity** as a verification axis |

### Phase-1 wires (2026-09-30)

Two new policy rules for the W2 swarm, from this batch.

**Rule H1 — name high-level operations, keep primitive fallback** [CONFIRMED — arXiv 2609.31076]

Give executor agents named operations (build wall segment, place granary, run smoke scene) instead of raw editor calls. Measured effect in NetHack: ~3x progression and 86% lower inference cost per episode. Keep a primitive path for cases the skill library does not cover. See @entities/tools/codehack.md.

**Rule H2 — withhold model-family identity from cooperative agents** [CONFIRMED — arXiv 2609.35928]

Do not put "you are model X" metadata into shared multi-agent context. In cooperative tasks, visible family labels split the group into factions and cost 55% more tokens and 30% more rounds, with success falling from 96% to 81%. See @sources/arxiv-2609.35928-prompted-identity-factionalism-2026-09-30.md.

### Phase-1 wires (2026-10-03)

Two more policy rules, from the Cogentic and audit-rule papers.

**Rule H3 — promote only confirmed results into a durable ledger** [CONFIRMED — arXiv 2609.40324]

Cogentic's strongest transferable idea. Each round writes two artifacts: a **record** of attempts and why they failed, and a **verified ledger** of confirmed intermediate results that the next round starts from. Map to castle-sim: a broken build or failed story writes the failure reason to the record; only playtest-passed state is promoted into the durable artifact later stories build on. This stops each session re-deriving state. Verifiers act adversarially — they assume the work is wrong until it survives. See @sources/arxiv-2609.40324-cogentic-proof-harness-2026-10-03.md.

**Rule H4 — audit something the executor did not nominate** [CONFIRMED — arXiv 2610.01514]

Report-dependent verification creates a suppression incentive: what the worker reports as important is what gets checked, so under-reporting escapes scrutiny. The fix is a report-independent audit floor. In the W2 verify gate this means the verifier must sample checks the executor did not flag, not only the items the executor listed as risky. See @sources/arxiv-2610.01514-audit-rule-faithful-explanations-2026-10-03.md.

### Phase-1 wires (2026-10-05)

**Rule H5 — do not pre-fill a value where the design wants a neutral choice** [CONFIRMED — arXiv 2610.03253]

Pre-filled defaults pull an LLM's choice toward the default, and the pull depends on wording — permission-style wording cuts it, and coarse action spaces reduce it. For any handoff or in-game advisor prompt, do not pre-fill a recommended action. This also reinforces **H1**: an agent given a few high-level verbs is less swayed by a supplied default than one given a fine-grained list. See @sources/arxiv-2610.03253-default-following-collective-action-2026-10-05.md.

**Rule H6 — let the expert policy decide, and a language model explain** [TENTATIVE — arXiv 2610.03695]

QUEEN pairs a silent expert encoder with a language model that is trained only to interpret the expert's state and explain it. Applied to castle-sim: keep the JSON-weighted lord director authoritative, and treat any language model as an **explainer** over the director's state, not a decision-maker. The missing piece is that the recipe needs a strong expert to exist first — so this is a Phase E+ note, not a W2 action. See @sources/arxiv-2610.03695-queen-chess-explains-moves-2026-10-05.md.

### Phase-1 wires (2026-10-07)

**Rule H7 — keep the complete raw record; do not compress history into rules too early** [CONFIRMED — arXiv 2610.08215]

Learn2Play Bench finds that retaining **complete records of actions and feedback** supports better learning than summarizing them into rules or strategies. For the W2 harness this argues for keeping the raw action-and-feedback log retrievable, and against handing the next agent only a tidy rule list. Note the pairing with **H3**: H3 governs what gets *promoted* into the verified ledger; H7 says the underlying raw record must still be kept. Also from the same bench: with the backbone model fixed, changing the **harness** can improve performance while lowering estimated inference cost. See @sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md.

**Rule H8 — re-validate inherited notes; an accumulating corpus can harm** [CONFIRMED — arXiv 2610.05041]

The strongest counterweight to H3 in this wiki. In the Mafia study, societies that carried **sixty generations of their own inherited strategy notes scored below societies with none**, and adaptation destroyed the signalling it depended on. A durable ledger is not automatically an asset — it can encode a stale or self-defeating convention. Practical rule for castle-sim: keep the ledger **small and verified**, and treat inherited derived notes as a **re-validation risk** rather than accumulated wisdom. See @sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md.

**Rule H9 — measure coordination cost, not just outcome** [CONFIRMED — arXiv 2610.04672]

MASBench scores multi-agent collaboration on performance **and** on communication cost and efficiency. The castle-sim harness currently measures outcomes only. A planner-plus-swarm plus verifiers spends real tokens on coordination, and that overhead is invisible today. Add a token-cost column to the per-milestone record. See @sources/arxiv-2610.04672-masbench-partial-observability-2026-10-07.md.

**Rule H10 — add a visual-fidelity check for 3D acceptance** [TENTATIVE — arXiv 2610.08720]

Every bench in the ladder above checks logic, ticks, or task completion. None verifies that rendered output *looks* right — which for a 3D castle sim is a real acceptance axis. WorldSolver scores visual fidelity as one of three evaluation dimensions. The cheap version for this project: render the scene headlessly and judge with an image diff or a VLM. See @sources/arxiv-2610.08720-worldsolver-visual-fidelity-2026-10-07.md.

### Phase-1 wires (2026-10-09) — the verification doctrine

Four rules from the verification cluster. Together they answer one question: **how do you know an agent's claim about its own work is true?**

**Rule H11 — certify a verifier with an external anchored reference set, never the task score** [CONFIRMED — arXiv 2610.11464]

A verifier that evolves alongside the agent can **collapse into a vacuous always-pass grader while still training skills just as well** — so a passing milestone does not prove the gate still works. Keep a small fixed set of tasks with known-good verdicts and re-check the gate against it whenever the gate itself changes. Read with **H4**: H4 says audit what the executor did not nominate; H11 says you cannot validate the auditor by the thing it audits. See @sources/arxiv-2610.11464-who-verifies-the-verifier-2026-10-09.md.

**Rule H12 — do not trust self-reported confidence when the reporter has a stake** [CONFIRMED — arXiv 2610.09371]

An LLM given its own true success probability still **claimed high confidence on 56% of tasks it had been told it would probably fail**. Honest reporting was not an equilibrium. The W2 verify gate must never rest on an executor's confidence claim, and no in-game advisor gets an engagement-shaped incentive. This is the incentive-side companion to **H4** (audit-rule) — one shows *suppression* pressure, the other shows *inflation*. See @sources/arxiv-2610.09371-confidence-game-delegation-2026-10-09.md.

**Rule H13 — escalate on sensitivity, not accuracy** [CONFIRMED — arXiv 2610.09683]

Accuracy, calibration, and sensitivity are distinct. Models with similar accuracy differ widely in **AUROC**, and deferring the **least-confident fraction** to the slow model gains in proportion to AUROC. Choose which cheap model to run, and when to escalate to the expensive one, on **sensitivity** — not on a benchmark accuracy score. See @sources/arxiv-2610.09683-system-switch-fast-slow-gate-2026-10-09.md.

**Rule H14 — a revisable rulebook plus a deterministic replay gate** [TENTATIVE — arXiv 2610.11794]

MEMENTO 3 keeps a natural-language rulebook as persistent memory with **unknown aspects deliberately underspecified**, compiles it to executable code, and **admits an update only when the code is judged faithful to the rulebook AND cell-exact replay reproduces the observed transitions**. This is the concrete shape for **H3**'s "promote only confirmed results": a change is admitted on a deterministic replay, not a judgement call. It also resolves the tension between **H7** (keep complete raw records) and **H8** (inherited notes can harm) — keep the raw transitions, derive a revisable summary, accept edits only on replay. See @sources/arxiv-2610.11794-memento-3-reflective-rulebooks-2026-10-09.md.

### Minecraft agent literature (2026-10-05) [CONFIRMED]

The Minecraft ecosystem is the largest live agent-tooling laboratory, and its mechanisms match rules H1–H4 above. Mineflayer (MIT, active) exposes small composable verbs with machine-checkable results; Voyager's skill library is executable code indexed for reuse, not prompt text; and its verifier feeds back execution errors rather than prose.

Two additions worth carrying forward:

- **Version-pin before generating.** One Minecraft tool reads the pack format file first, because models "get Minecraft syntax wrong confidently." Pin the Godot version and API in context before any agent writes code.
- **Human judgment for fuzzy goals.** The BASALT benchmark's four "fuzzy" tasks were never solved robustly by any team — scalar rewards fail on aesthetic goals. Keep a person or a rubric in the loop.

Full detail: @concepts/minecraft-agent-harness-shelf.md · @entities/tools/mineflayer.md · @entities/tools/minecraft-agent-mcp-shelf.md

## Snippets

> OMC-style game-dev case study pattern: Sonnet/Opus logic + Gemini art — validated for narrow vertical slices, not full Stronghold. [TENTATIVE — @osint-wiki/sources/omc-talent-container-paper.md]
