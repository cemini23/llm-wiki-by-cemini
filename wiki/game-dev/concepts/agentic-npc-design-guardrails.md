---
title: Agentic NPC design — guardrails and balance
type: concept
tags: [concept, npc, llm, design, guardrails, balance]
keywords: [agentic-npc, guardrails, memory, lore, balance]
related:
  - concepts/llm-npc-runtime-ai-shelf.md
  - sources/ixie-agentic-npc-balance-2026.md
  - sources/ubisoft-teammates-ai-experiment-2025.md
  - sources/exa-npc-pcg-ccgs-batch-2026-06-13.md
  - sources/morganpage-local-npc-dialogue-2026.md
  - sources/36kr-ai-game-story-gameplay-guardrails-2026-06-30.md
  - sources/arxiv-2609.18935-long-lived-characters-local-inference-2026-09-19.md
  - sources/arxiv-2609.23043-narrative-reliability-detective-games-2026-09-24.md
  - sources/arxiv-2609.27606-state-grounded-conditioning-2026-09-24.md
  - sources/arxiv-2609.26629-personaweaver-procedural-characters-2026-09-24.md
maturity: validated
created: 2026-06-13
updated: 2026-09-24
wire_status: policy_wired
wire_target: concepts/agentic-npc-design-guardrails.md
---

## Relations

- @sources/ubisoft-teammates-ai-experiment-2025.md — "fences" metaphor for writer control

## Raw Concept

Design framework for **adaptive NPCs** that do not break game balance, lore, or economy — synthesized from iXie (2026) + Ubisoft Teammates research.

## Narrative

### Core thesis [CONFIRMED — iXie 2026]

> Scripted NPCs are **content**. Agentic NPCs are **systems**.

Systems need policy, telemetry, replay, regression harnesses — not line-by-line script review.

36Kr expert roundtable [@sources/36kr-ai-game-story-gameplay-guardrails-2026-06-30.md] adds a narrative-design warning: generic "in-game Siri" NPCs often reduce authorial intent. Runtime AI should either be a bounded component in an AI-native loop or stay out of the shipped feature set.

### Failure modes

| Failure | Player perception | Example |
|---------|-------------------|---------|
| Social unpredictability | "Bugged" | Guard calm then hostile without clear cause |
| Exploit surfaces | Meta degeneracy | Herding NPCs to block doors |
| Tone/lore drift | Immersion break | Grim merchant sounds like customer support bot |
| Economy manipulation | Unfair | Dynamic merchant prices gamed by buy/dump |

### Control framework

**1. Narrow goals** — per-scene, role-bound, fail-soft. Not "maximize profit."

**2. Explicit constraints** — hard walls:
- Forbidden actions (never kill quest givers)
- Immutable beliefs (faction loyalty)
- Tone rules (no modern slang, no out-of-world refs)

**3. Authorial fences** [CONFIRMED — Ubisoft Mosser]

Writers set personality + lore boundaries; NPCs **improvise inside fences**, not rewrite canon.

**4. Curated memory** — remember:
- Quest flags, reputation **tiers**, short-term context

**4b. Incremental inference state** [CONFIRMED — arXiv 2609.18935]

For **local** LLM NPCs, memory is not only text — KV prefix + recurrent state are maintained resources. Patch at **true sequence tail** when facts change; do not replay the character's full life before every line. Dialogue that contradicts authoritative game state (ownership, transfers, stockpile) must be blocked **before** it reaches deterministic rules (@sources/arxiv-2609.18935-long-lived-characters-local-inference-2026-09-19.md).

**4c. State-Grounded Conditioning (SGC)** [CONFIRMED — arXiv 2609.27606]

**Direction drift** — fluent replies that ignore live session/game state. Use rule kernels + structured state slices (perception / grounding / interaction wrappers) so NPC-facing agents cannot pick valid-sounding but state-wrong actions.

**4d. Epistemic pacing (narrative)** [CONFIRMED — arXiv 2609.23043]

For story-heavy modes, gate what NPCs may reveal via structured knowledge trees — detective-game pattern; prevents premature clues and fabricated facts in open dialogue.

Do **not** remember:
- Exact phrasing, petty crimes, misclick experiments

Memory needs **decay** + chapter resets.

**5. Guardrail layers** — model output never raw:
- Safety/content filters
- Lore consistency check
- Economy clamps (price bands, progression gates)

**6. Testing** — seeds, input logs, replay, behavior snapshot tests (variance bounds not "IQ")

**7. LiveOps cost** — cap turns/length, cache barks, agentic mode for VIP NPCs only

### castle-sim implication

Even Tier 3 "advisor" NPC must not:
- Alter tax/popularity mechanics via free-form chat
- Gate wall-building unpredictably
- Replace Stronghold-style **readable** economy feedback

Use agentic dialogue for **flavor** only until full guardrail stack exists.

## Snippets

Fence pattern (design doc):

```markdown
## NPC: Steward
May improvise: ration advice, morale quips, siege rumors
Must never: change tax rates, spawn units, alter wall rules
Memory: last 3 player decisions (decay after session)
```

## Dead Ends

- "Smarter NPCs" as marketing goal — believable **consistency** is the shipped bar
