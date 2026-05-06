---
title: Research-Paper-Writing-Skills — ML/CV/NLP Paper-Drafting Prompts (MIT)
type: entity
tags: [tool, prompt-engineering, mit-license, steal-from-tier, abandoned-project, claude-skill]
keywords: [research-paper-writing-skills, master-cai, claim-evidence-alignment, abstract-synthesis, claude-code-skill, prompt-pattern-library]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - entities/tools/codex-startup-pressure-test-skill.md
  - entities/tools/academic-paper-skills.md
  - entities/tools/obsidian-llm-wiki-local.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 6, **STEAL-FROM** tier
- @concepts/cemini-license-posture.md — MIT-licensed, IP-clean
- @entities/tools/codex-startup-pressure-test-skill.md — sister STEAL-FROM in same K32 batch (different prompt domain)
- @entities/tools/academic-paper-skills.md — sister STEAL-FROM in same K32 batch (peer-review framework, complementary)
- @entities/tools/obsidian-llm-wiki-local.md — sister STEAL-FROM in same K32 batch (wiki maintenance code)

## Raw Concept

Master-cai/Research-Paper-Writing-Skills is a curated "skill package" of agent metadata and instructional prompts tailored for Claude Code, Codex, and Gemini. Specifically designed for ML/CV/NLP academic paper drafting, editing, and evaluation.

K32 DR verdict: **STEAL-FROM**. Don't install the entire repository wholesale. Surgically extract the prompts pertaining to **claim-evidence alignment** and **abstract synthesis** — these patterns are domain-portable to Cemini's brief-drafting workflow.

## Narrative

- **URL**: `https://github.com/Master-cai/Research-Paper-Writing-Skills` ✓ DR-cited
- **License**: MIT — clean, IP-sale safe
- **Stack**: YAML agent metadata + Markdown instructional prompts; designed for `.claude/skills` directory drop-in
- **Maturity**: 4 commits, 0 releases — abandoned per DR. Treat as static prompt artifact

### Domain mismatch and what to extract

The package is heavily tuned for ML/CV/NLP academic conventions. **Most of it doesn't apply to Cemini's quant-finance domain.** Don't bulk-install.

What's worth extracting:

| Pattern | Why it transfers to quant-finance |
|---------|-----------------------------------|
| Claim-evidence alignment | Briefs to claude.ai or CeminiSuite have claims; alignment with cited sources is a quality bar |
| Abstract synthesis | Briefs benefit from "TL;DR / Summary / Body" structure; the prompts here can guide tighter executive summaries |
| Hierarchical section optimization | Briefs and concept pages benefit from section-flow review |

What to leave behind:

- ML/CV/NLP-specific stylistic conventions
- Conference-template formatting
- Reviewer-response templates (academic specific)

### Action plan

1. Phase 1: clone `github.com/Master-cai/Research-Paper-Writing-Skills` to `/tmp/research-paper-skills-audit/`
2. Phase 2: extract claim-evidence alignment prompts + abstract synthesis prompts
3. Phase 3: re-style for quant-finance domain (drop ML jargon, add finance-domain examples)
4. Phase 4: install as Claude Code skills OR add to `prompt-patterns/` (per parallel work for codex-startup-pressure-test-skill)

Estimated effort: 2-3 hours total. Could be bundled with codex-startup-pressure-test-skill extraction for combined ROI.

### Risk

> "The primary limitation is domain specificity. The prompts are heavily tuned to expect the stylistic conventions of ML/CV/NLP academic formats. They will require significant semantic modification to handle the stylistic expectations of quantitative finance models or macroeconomic reporting effectively. Additionally, with a history of only 4 commits and 0 releases, the repository appears to be a static collection of personal configurations rather than a continuously maintained, evolving community framework."

### Open questions

- ⚠ Exact prompt content (DR didn't surface)
- ⚠ Are the prompts standalone-runnable or do they assume specific Claude Code skill scaffolding?
- ⚠ Does the package include the agent-coordination logic (Strategist + Composer phases mentioned in academic-paper-skills sister project) or just the prompts?

### Adoption status — STEAL-FROM, NOT INSTALLED

Phase-1 audit pending. Bundle with sister STEAL-FROM extractions.

## Snippets

### Scope (DR direct quote)

> "This repository functions as a curated 'skill package' containing highly structured agent metadata and instructional prompts tailored for AI coding assistants like Claude Code, Codex, and Gemini. It is architected specifically to aid researchers in structuring, drafting, and evaluating academic papers within the fields of Machine Learning (ML), Computer Vision (CV), and Natural Language Processing (NLP). The package consumes raw drafts or outlines and directs the LLM agent to execute complex editorial tasks, such as rewriting abstracts for academic rigor, rigorously aligning claims with presented evidence, and optimizing hierarchical section structuring." [Source: 5_6 links.docx URL 6]

### Why STEAL-FROM not ADOPT

> "Steal-from. Instead of blindly installing the entire repository into .claude/skills, selectively extract the logic pertaining to claim-evidence alignment and abstract synthesis. These specific analytical prompt patterns will dramatically improve the rigor of the briefs/ generated for production deployment without burdening the local environment with unnecessary CV/NLP boilerplate bloat." [Source: 5_6 links.docx URL 6]
