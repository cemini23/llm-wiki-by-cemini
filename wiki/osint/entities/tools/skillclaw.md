---
title: SkillClaw — collective Hermes skill evolution
type: entity
tags: [tool, hermes, skills, continual-learning, k113]
keywords: [skillclaw, amap-ml, skill-dedup, hermes-skills]
related:
  - sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md
  - concepts/tool-evaluation-framework.md
  - concepts/llm-agent-systems.md
  - "@ccc-wiki/entities/tools/skillclaw.md"
maturity: draft
created: 2026-06-12
updated: 2026-06-12
license_verified: MIT
---

## Relations

- @sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md — K113 Adopt
- @concepts/llm-agent-systems.md — skill lifecycle adjacent to Muse/AutoSkill patterns
- @ccc-wiki/entities/tools/skillclaw.md — install handoff

## Raw Concept

- **Repo:** `github.com/AMAP-ML/SkillClaw`
- **Tier:** Adopt → **CONDITIONAL-GO** (laptop proxy; Hermes skill dir)
- **License:** MIT `[CONFIRMED]` 2026-06-12
- **Stars:** 1,880; pushed 2026-06-02

## Narrative

Post-task skill evolution for Hermes: deduplicate/merge `~/.hermes/skills` from real session payloads via proxy client intercept.

**Steal-from pattern:** collective skill distillation without manual SKILL.md editing — pairs with `@ccc-wiki/concepts/muse-autoskill-skill-lifecycle.md`.

**Risks:** skill pollution if evolution loop lacks human veto; isolate trial skills dir.

**Phase-0:** clone + README; no prod wiring.

### Laptop trial (2026-06-12)

| Check | Result |
|-------|--------|
| `pip install -e .` | PASS |
| `skillclaw --help` | PASS |
| `skillclaw doctor hermes` | BLOCKER — needs `skillclaw setup`; Hermes not installed |

Report: `.local/reports/k113-laptop-trial-2026-06-12.md`
