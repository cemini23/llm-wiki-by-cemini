---
title: AI-Research-SKILLs — Orchestra Research skill library
type: entity
tags: [tool, skills, mlops, research-engineering, k113]
keywords: [orchestra-research, ai-research-skills, peft, rlhf, skill-audit]
related:
  - sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md
  - concepts/tool-evaluation-framework.md
  - "@ccc-wiki/entities/tools/ai-research-skills.md"
  - "@cybersecurity-wiki/briefs/2026-06-12_k113-cybersec-ai-research-skills-from-osint.md"
  - "@cybersecurity-wiki/entities/tools/ai-research-skills.md"
maturity: draft
created: 2026-06-12
updated: 2026-06-12
license_verified: MIT
---

## Relations

- @sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md — K113 Adopt
- @cybersecurity-wiki/briefs/2026-06-12_k113-cybersec-ai-research-skills-from-osint.md — ML security skills subset
- @cybersecurity-wiki/entities/tools/ai-research-skills.md — cybersec cherry-pick entity
- @ccc-wiki/entities/tools/ai-research-skills.md — CCC install notes

## Raw Concept

- **Repo:** `github.com/Orchestra-Research/AI-Research-SKILLs`
- **Tier:** Adopt → **CONDITIONAL-GO** (laptop skill install; audit before prod-adjacent use)
- **License:** MIT `[CONFIRMED]` 2026-06-12
- **Stars:** 9,613

## Narrative

~83 specialized ML research engineering skills (PEFT, distributed training, RLHF, MLOps observability). Installer: `npx @orchestra-research/ai-research-skills` (verify package name at install time).

**CCC fit:** enrich Claude Code harness for quant/ML prototyping sessions.

**Cybersec fit:** fine-tuning / MLOps modules relevant to offensive ML eval — track in `skill_audit.py` if adopted.

**NO-GO:** blind install into prod agents without skill_audit PASS per skill file.

### Laptop trial (2026-06-12)

98 `SKILL.md` files inventoried; cybersec cherry-pick folders documented on `@cybersecurity-wiki/entities/tools/ai-research-skills.md`. Category `npx` install not run (operator-gated).
