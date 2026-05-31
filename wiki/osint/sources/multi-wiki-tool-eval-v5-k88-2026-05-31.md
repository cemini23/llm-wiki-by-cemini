---
title: "Multi-Wiki Tool Evaluation (v5 prompt, K88 batch — 29 URLs)"
type: source
tags: [source, gemini-deep-research, tool-eval, v5-prompt, license-corrections, k88]
keywords: [skillspector, openosint, webwright, skill-seekers, skillnet, finance-skills, machine-learning-for-trading, graph-r1]
related:
  - sources/multi-wiki-tool-eval-v4-k84-2026-05-30.md
  - sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md
  - concepts/cemini-license-posture.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/openosint.md
  - entities/tools/microsoft-webwright.md
  - entities/tools/skill-seekers.md
  - entities/tools/finance-skills.md
  - entities/tools/book-to-skill.md
  - entities/tools/skillnet.md
maturity: draft
read_status: deep-read
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @sources/multi-wiki-tool-eval-v4-k84-2026-05-30.md — prior v4 batch; v5 prompt frozen at `Cemini claude code CCC/prompts/deep-research-multi-wiki-eval-v5-2026-05-30.md`
- @concepts/cemini-license-posture.md — NO LICENSE false-negative pattern continues
- @entities/tools/finance-skills.md — Gemini Reject overturned (MIT on GitHub API 2026-05-31)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Multi-Wiki Link Evaluation Report (Batch v5, May 2026) |
| **Author** | Gemini Deep Research (v5 multi-wiki eval prompt) |
| **Type** | docx |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/multi-wiki-tool-eval-v5-k88-2026-05-31.docx` |
| **Retrieved** | 2026-05-31 |
| **URLs** | 29 evaluated |
| **Read status** | deep-read + `gh api` license spot-check (12 NO LICENSE rows) |

## Narrative

K88 v5 batch: agent skills registries, MCP bridges, OSINT dashboard, browser automation harness, quant reference repos. **Prompt improvement landed:** v5 references **world-cup-bot** public OSS — evals avoid greenfield PM bot Adopts. **Residual gap:** Gemini still marks **NO LICENSE FOUND** on repos with SPDX on GitHub (~40% false-negative rate on checked rows).

### Gemini aggregate (as reported)

| Tier | Count | Headlines |
|------|-------|-----------|
| Adopt | 9 | SkillSpector, Webwright, book-to-skill, OpenOSINT, cc-thinking-skills, SkillNet, alirezarezvani/claude-skills, Skill_Seekers, claude-skill-registry |
| Steal-from | 4 | OpenWA, stefan-jansen/MLFT, jezweb/claude-skills |
| Defer | 3 | ai-labs-claude-skills, seo-geo-claude-skills, agentwasp |
| Reference-only | 10 | learnGitBranching, ml-systems-papers, train-llm-from-scratch, ML-Master, awesome-* lists |
| Reject | 3 | Graph-R1 (CC-BY-NC-SA), linux-basics notes, finance-skills |
| UNAVAILABLE | 2 | smavg, dev-commands-cheatsheet |

### License corrections after `gh api` [CONFIRMED 2026-05-31]

| URL | Gemini | Verified | Action |
|-----|--------|----------|--------|
| ailabs-393/ai-labs-claude-skills | NO LICENSE | **MIT** | Defer → Reference-only |
| aaron-he-zhu/seo-geo-claude-skills | NO LICENSE | **Apache-2.0** | Defer → SEO-wiki steal-from |
| tjboudreaux/cc-thinking-skills | NO LICENSE | **MIT** | Adopt upheld |
| agentwasp/agentwasp | NO LICENSE | **Apache-2.0** | Defer upheld |
| himself65/finance-skills | Reject | **MIT** | **Reject overturned** — operator stack already installed; close issue #64 if LICENSE file present |
| byungsoo-oh/ml-systems-papers | NO LICENSE | **null** | Reference-only; still no LICENSE file |
| ahegazy0/linux-basics-for-hackers-notes | Reject | **null** | Reject upheld (notes-only, no LICENSE) |
| sjtu-sai-agents/ML-Master | NO LICENSE | **null** | Reference-only academic |
| AmberLJC/LLMSys-PaperList | NO LICENSE | **null** | Reference-only |
| travisvn/awesome-claude-skills | NO LICENSE | **null** | Curated list — no LICENSE file |
| BehiSecc/awesome-claude-skills | NO LICENSE | **null** | Same |
| aradotso/trending-skills | NO LICENSE | **null** | Low-star index |

### OSINT-priority outcomes

1. **NVIDIA SkillSpector (Adopt)** — wire into `scripts/skill_audit.py` / preingest skill scanning; Phase-0 audit queued.
2. **OpenOSINT (Adopt)** — Palantir-style OSINT dashboard; Phase-0 vs existing librarian/conductor stack.
3. **OpenWA (Steal-from)** — webhook/session patterns for world-cup-bot alert channel (module 6), not full gateway adopt.
4. **stefan-jansen/MLFT (Steal-from)** — corroborates Wave-3 steal-from; strip-mine alpha factors only.
5. **Graph-R1 (Reject)** — CC-BY-NC-SA 4.0 poison pill for IP-sale surfaces.

### Cross-wiki routing (not duplicated as OSINT entity bodies)

| Target | Items |
|--------|-------|
| **ccc-wiki** | Webwright, book-to-skill, SkillNet, cc-thinking-skills, alirezarezvani/claude-skills, Skill_Seekers, claude-skill-registry, learnGitBranching | Brief: `Cemini claude code CCC/briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md` |
| **seo-wiki** | aaron-he-zhu/seo-geo-claude-skills (Apache-2.0) | Brief: `SEO:GEO B&M Business/briefs/2026-05-31_k88-seo-geo-claude-skills-from-osint.md` |
| **cybersec-wiki** | SkillSpector primary fit; linux-basics notes Reject | Brief: `Cybersecurity wiki/briefs/2026-05-31_k88-skillspector-cybersec-from-osint.md` |

## Snippets

> "v5 protocol strictly enforces inline license verification via the GitHub API … rendering heuristic or metadata-based license assumptions obsolete." [Source: multi-wiki-tool-eval-v5-k88-2026-05-31.docx]

> "The active deployment of the public open-source world-cup-bot inventory across modules one through seven necessitates that any incoming prediction market or sports-liquidity tools be evaluated strictly for gap-filling capabilities." [Source: multi-wiki-tool-eval-v5-k88-2026-05-31.docx]
