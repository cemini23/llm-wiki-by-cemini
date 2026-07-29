# HL session trail (K159 — Aleena decision continuity)

**arXiv pattern:** [2607.08043](https://arxiv.org/abs/2607.08043) (Aleena — lifecycle alignment agents; schema only)  
**Brief:** `briefs/2026-07-18_k159-aleena-decision-continuity-steal.md`  
**Shelf date:** 2026-07-18

## Steal (pattern only)

After each analyze → patch → preflight cycle, leave a **structured session
trail** so decisions, risks, and open questions survive chat context loss.
Steal the field names and discipline — **not** Aleena's web/Pixi stack, and
not a runtime LLM in `decide()`.

## When to write

- End of an HL patch session (local analyze → code/doc change → preflight)
- Before handoff to another agent or human
- When a heuristic name / Arena term is redefined across sessions

Do **not** invent facts from chat. If a field has no concrete content, write
`none` or leave a one-line blocker — never fabricate spot names, μ, or pins.

## Required headings (use these exact names)

Copy the block below into the session note (brief, escalate, or HL log).

```markdown
## summary
<!-- 1–3 sentences: what was attempted and what landed. Concrete only. -->

## decisions
<!-- What we chose (and what we explicitly did not). Pin IDs, gate outcomes, replace posture. -->

## action_items
<!-- Next concrete steps: owner + verb + artifact. Code-shaped items stay human-gated. -->

## risks
<!-- What can go wrong if we ship / replace / rename now. -->

## open_questions
<!-- Unresolved blockers. Prefer named spots, tests, or API unknowns. -->
```

### Field rules

| Field | Rule |
|-------|------|
| **summary** | Concrete spot names, blockers, next steps only. No invented μ / hand counts / pins. |
| **decisions** | Record replace posture (`NO_REPLACE` / replace planned), pin strings, engine flags **as known**. |
| **action_items** | Actionable; draft PR/patch only when code-shaped; human review + merge. |
| **risks** | Supply-chain, TrueSkill reset, vocabulary conflict, gate miss — only if evidenced this session. |
| **open_questions** | Prefer named fixtures / boards / API gaps. Never invent unanswered facts to fill the box. |

## Vocabulary-conflict check (P1)

Before shipping a heuristic rename or redefinition of Arena terms:

1. Search existing `references/`, `STRATEGY.md`, charts, and recent briefs for the old term.
2. Flag **conflict** (two live meanings) vs **duplicate** (same meaning, two names).
3. Do not ship the rename until the conflict is resolved or explicitly accepted in **decisions**.

Example conflict classes: street labels, strength bins, gate class names
(transition vs play), engine env vars (`CEMINI_SANDBOX_ENGINE` values).

## Human-gated code changes (P2)

- Session trail alone is not a merge. Runtime `decide()` stays zero LLM.
- Draft patch / PR only when an **action_item** is code-shaped; human review + merge.

## Out of scope

- Running Aleena / Pixi in the arena loop
- Vendoring `uw-ssec/Aleena` while LICENSE TBD
- Memory-scarcity / infra-macro papers (CCC lane, not this repo)

## Related

- Researcher sandbox ops: `references/researcher-track-sandbox.md`
- Play-adequacy gates: `references/play-adequacy-gates.md`
- Pre-install gate (bake deps): `references/preinstall-gate.md`
- Heuristic learning loop: `references/heuristic-learning.md`

## Check

```bash
test -f references/hl-session-trail.md
rg -n "summary|decisions|action_items|risks|open_questions" references/hl-session-trail.md
```
