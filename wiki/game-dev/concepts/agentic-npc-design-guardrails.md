---
title: Agentic NPC design — guardrails and balance
type: concept
tags: [concept, npc, llm, design, guardrails, balance]
keywords: [agentic-npc, guardrails, memory, lore, balance]
related:
  - concepts/llm-npc-runtime-ai-shelf.md
  - sources/ixie-agentic-npc-balance-2026.md
  - sources/ubisoft-teammates-ai-experiment-2025.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @sources/ubisoft-teammates-ai-experiment-2025.md — "fences" metaphor for writer control

## Raw Concept

Design framework for **adaptive NPCs** that do not break game balance, lore, or economy — synthesized from iXie (2026) + Ubisoft Teammates research.

## Narrative

### Core thesis [CONFIRMED — iXie 2026]

> Scripted NPCs are **content**. Agentic NPCs are **systems**.

Systems need policy, telemetry, replay, regression harnesses — not line-by-line script review.

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
