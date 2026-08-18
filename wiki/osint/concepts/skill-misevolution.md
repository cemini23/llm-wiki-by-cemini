---

title: "Skill misevolution — self-improving agents can make skills unsafe with practice"
type: concept
tags: [concept, agent-safety, skill-evolution, ccc, cyber, she, k237]
keywords: [skill misevolution, lifecycle gates, authoring-retrieval-execution, SKILLMISEVO, SAFEEVOLVE, C-ASR, skill poisoning]
related:
  - sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md
  - sources/arxiv-2608.12977-self-evolving-security-2026-08-14.md
  - concepts/agent-skill-rl-extraction.md
  - concepts/agent-setup-instruction-supply-chain.md
  - sources/arxiv-2608.13560-autodesign-2026-08-14.md
  - concepts/self-evolving-runtime-defense.md
  - sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md
  - concepts/intent-not-form-refusal.md
  - sources/arxiv-2608.14036-demystifying-agent-skills-2026-08-17.md
  - concepts/agent-skills-procedural-anchoring.md
  - "@cybersecurity-wiki/concepts/skill-misevolution.md"
  - sources/eval-multi-wiki-revenue-plan-2026-08-18.md
  - sources/arxiv-2608.16112-strategic-technical-debt-2026-08-18.md
  - entities/tools/diagram-design.md
maturity: draft
created: 2026-08-14
updated: 2026-08-17
---

## Relations

- @sources/arxiv-2608.12851-skill-misevolution-2026-08-14.md — primary source
- @sources/arxiv-2608.12977-self-evolving-security-2026-08-14.md — defensive mirror (HARD)
- @concepts/agent-skill-rl-extraction.md — K233 SKILLER generation sibling
- @concepts/agent-setup-instruction-supply-chain.md — K236 promptware/setup-instruction risk
- @sources/arxiv-2608.13560-autodesign-2026-08-14.md — self-improving harness family
- @sources/arxiv-2608.13304-wifa-intent-not-form-2026-08-15.md — K239: wrappers must not become the refusal label
- @concepts/intent-not-form-refusal.md — do not auto-evolve skills to "fix" refusals
- @sources/arxiv-2608.14036-demystifying-agent-skills-2026-08-17.md — K240: skills stabilize procedure (65.7%) not facts
- @concepts/agent-skills-procedural-anchoring.md — library cap + no unattended evolve

## Raw Concept

What this page answers: self-improving agents convert "successful" trajectories into persistent reusable skills — but a success that contains an unsafe shortcut becomes a reusable skill that causes harm later, after the trigger input is gone. How do we detect and govern it? Synthesized from SKILLMISEVO (2608.12851) + HARD (2608.12977).

## Narrative

**Misevolution signature**: all 21 evolved configurations in SKILLMISEVO-BENCH authored unsafe artifacts; 15 retained fresh-session harm. No-Evolution stays clean — the risk is introduced by *learning from experience*, not by the base model. A terminal attack-success-rate cannot distinguish a clean library from an unsafe artifact that was merely never retrieved.

### The three lifecycle gates (risk attribution, not just outcomes)

1. **Authoring** — does the written skill contain reusable unsafe instructions? (CU/UG/Stealth artifact scores.)
2. **Retrieval** — would the skill be retrieved in a clean session? (Unsafe Retrieval Rate.)
3. **Execution** — does it cause harm when executed fresh? (Carryover ASR.)

This is the correct eval structure for any skill library (Claude Code `.cursor/skills/*`, CCC `/route`, SHE harness). A terminal success rate is insufficient.

### Drift mechanisms (VC1–VC3)

- **VC1 label hijack**: unsafe body attaches to a benign label ("monitoring/telemetry/setup") and gets abstracted as the trigger.
- **VC2 dual-use boundary loss**: safety-critical boundary (provenance, data scope, granted capability) dropped while the reusable template is kept.
- **VC3 completion spillover**: full collection→processing→transmission chain packaged as one procedure so later benign work "completes" the omitted harmful steps.

Benign mixed updates do **not** reliably erase learned risk; early exposure widens the contamination window.

### Governance (SAFEEVOLVE + SHE HITL)

- **Write-time**: non-blocking critic that localizes reusable unsafe instructions + **delete-only paired deleter** (can remove/narrow, never add checks/approvals/HITL).
- **Reuse-time**: ranking by utility × lineage-risk, harmful-outcome attribution, retirement after 2 harmful reuses or effective risk ≥0.6; library cap 32.
- **SHE implication**: **skills can get worse with practice** — promote/refine skills under an eval-gate with decoupled benign-utility + harm judges, clean-session reload, No-Evolution baseline. HITL approval on a skill's *write* does not check whether later retrieval activates an unsafe span — need retrieval lineage + retirement.

**Offense-side (cyber lab)**: VC1–VC3 are ready-made poisoning templates against skill-evolution agents; the threat model is "poison a learning-history position and let evolution propagate it."
