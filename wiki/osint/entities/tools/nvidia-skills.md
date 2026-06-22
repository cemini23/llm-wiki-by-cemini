---
title: NVIDIA Skills — signed agent skill distribution
type: entity
tags: [entity, tool, agent-skills, nvidia, ccc-wiki, k126]
keywords: [nvidia-skills, skill-md, model-signing, skill-supply-chain, cursor-skills]
related:
  - sources/links-6-22-tool-eval.md
  - entities/tools/nvidia-skillspector.md
  - concepts/claude-code-skills-md-workflow.md
  - concepts/wiki-tooling-evaluation.md
  - "@ccc-wiki/entities/tools/nvidia-skills.md"
maturity: draft
created: 2026-06-22
updated: 2026-06-22
---

## Relations

- @sources/links-6-22-tool-eval.md — K126 URL 61; docx Adopt → **CONDITIONAL-GO** after license re-check
- @entities/tools/nvidia-skillspector.md — complementary static scanner (K88); SkillSpector audits supply chain, this repo distributes skills
- @concepts/claude-code-skills-md-workflow.md — SKILL.md protocol target
- @ccc-wiki/entities/tools/nvidia-skills.md — CCC routing stub (create on cross-wiki pass if missing)

## Raw Concept

What prompted this page: K126 links.docx Adopt-tier evaluation of `github.com/nvidia/skills` — NVIDIA-backed SKILL.md distribution with signing/verification flows.

## Narrative

**Repository:** [nvidia/skills](https://github.com/nvidia/skills) — agent skill packages (YAML/Markdown) with cryptographic signing and model-signing verification hooks.

**Phase-0 license (2026-06-22):** Docx claimed MIT; LICENSE file reads **Apache-2.0 AND CC-BY-4.0** dual license. GitHub API reports `NOASSERTION` SPDX (multi-license). **Posture: CONDITIONAL-GO** — safe for reference install + attribution; require legal review before bundling into IP-sale artifacts.

**Stars / activity:** ~1.6k★, pushed 2026-06-22, not archived.

**Steal targets:**

- Signed skill distribution pattern for federation hub skill supply
- Pair with SkillSpector pre-commit gate on `.cursor/skills/` and `.claude/skills/`

**Reject for:** Direct merge into CeminiSuite prod trading paths — skills are dev-harness scope only.

## Snippets

> "SPDX-License-Identifier: Apache-2.0 AND CC-BY-4.0" [Source: nvidia/skills LICENSE file, retrieved 2026-06-22]

> "This ecosystem actively sets the standard for securely distributing and verifying the SKILL.md format protocol." [Source: links.docx URL 61]
