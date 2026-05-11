---
title: Research-Paper-Writing-Skills — ML/CV/NLP Paper-Drafting Prompts (MIT)
type: entity
tags: [tool, prompt-engineering, mit-license, steal-from-tier, abandoned-project, claude-skill, adopted]
keywords: [research-paper-writing-skills, master-cai, claim-evidence-alignment, abstract-synthesis, claude-code-skill, prompt-pattern-library]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - entities/tools/codex-startup-pressure-test-skill.md
  - entities/tools/academic-paper-skills.md
  - entities/tools/obsidian-llm-wiki-local.md
maturity: validated
created: 2026-05-06
updated: 2026-05-10
adopted_as: scripts/skill_audit.py v0.4 (2026-05-10)
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

### Adoption status — ADOPTED into `scripts/skill_audit.py` v0.4 (2026-05-10)

**Phase 1 audit complete 2026-05-10**. Although the repo source files were not surfaced in DR (and `master-cai/Research-Paper-Writing-Skills` shows only 4 commits / 0 releases — abandoned-project profile), the **two domain-portable prompt patterns** named in the K32 DR brief have been distilled and ported as static-check primitives in `scripts/skill_audit.py` v0.4. This re-styles the prompts as deterministic Python checks rather than DeepSeek prompts — appropriate for a static-audit linter; LLM-as-judge dynamic checks remain deferred to a later sprint.

**Two new checks ported** (v0.4 adds these on top of v0.3's 10):

1. **`check_claim_evidence`** (weight 0.06) — claim-evidence alignment. Detects four claim labels in adoption-class briefs: license (`MIT`, `Apache-2.0`, `AGPL-3.0`, etc.), version (`vX.Y.Z`), stars (`N★`/`N stars`), and commits (`N commits`). Each claim must co-locate with a verification anchor within ±240 chars. Anchors: `VERIFIED YYYY-MM-DD`, `Phase-0 audit`, `audit ✓`, `[Source: ...]`, `[NEEDS VERIFICATION ...]`, `[CONFIRMED]`/`[TENTATIVE]`/`[RETRACTED]`. Same fact restated multiple times deduped via canonical-value grouping; claim anchored if **any** occurrence has anchor nearby. Coverage thresholds: ≥90% full credit, ≥70% (0.04), ≥50% (0.02), <50% (0.0).
2. **`check_abstract_synthesis`** (weight 0.04) — `## Summary` section quality. Three signals required: (a) length 50-400 words, (b) effort estimate present (e.g., `effort`, `**2-3 hr`, `~1 day`), (c) verdict-flavored opener (`Adopt`, `Steal-from`, `Reject`, `Reference`, `Defer`, `Install`, `GO`, `NO-GO`, `CONDITIONAL-GO`). 3/3 full credit, 2/3 (0.025), 1/3 (0.01), 0/3 (0.0).

**Weight rebalance**: 0.10 of headroom carved out of `check_citations` (0.15 → 0.10) and `check_prose_quality` (0.10 → 0.05). v0.4 still sums to 1.00 across 12 static checks.

**Adoption-class gate**: both new checks exempt ops/research briefs via `_is_adoption_brief()` — same gate already used by v0.3's `check_phasing`/`check_risk_discipline`/`check_brief_completeness`.

**Calibration verified 2026-05-10** against 7 representative briefs:
- K35 fresh adoption (aris, spec-kit, codeboarding, tech-debt): 99.5/100 PASS
- K35 with anchoring gaps (claude-mem 97.5 WARN — un-anchored `v13.0.1` mention outside Phase-0 context; revpdf 94.5 WARN — `Proprietary (free)` license string not co-located with verification)
- Older adoption briefs flagged with legitimate anchoring gaps: hftbacktest 90.5, polymarket-stack 90.5, picobot-prod 96.0, adala-prod 98.5, guidance-ai 94.5
- Ops/research briefs properly exempt: step81-sshd 85.0 N/A, polymarket-onchain 100/100 N/A

Both checks are signal-bearing, not noise — they catch real gaps in older briefs while preserving full scores on well-disciplined fresh briefs.

**Hierarchical section optimization** (third pattern named in DR) **NOT ported in v0.4**: structural-flow review requires LLM judgment; deferred to the dynamic-checks sprint pending `_llm_retry.py` from @entities/tools/obsidian-llm-wiki-local.md Phase 2.

## Snippets

### Scope (DR direct quote)

> "This repository functions as a curated 'skill package' containing highly structured agent metadata and instructional prompts tailored for AI coding assistants like Claude Code, Codex, and Gemini. It is architected specifically to aid researchers in structuring, drafting, and evaluating academic papers within the fields of Machine Learning (ML), Computer Vision (CV), and Natural Language Processing (NLP). The package consumes raw drafts or outlines and directs the LLM agent to execute complex editorial tasks, such as rewriting abstracts for academic rigor, rigorously aligning claims with presented evidence, and optimizing hierarchical section structuring." [Source: 5_6 links.docx URL 6]

### Why STEAL-FROM not ADOPT

> "Steal-from. Instead of blindly installing the entire repository into .claude/skills, selectively extract the logic pertaining to claim-evidence alignment and abstract synthesis. These specific analytical prompt patterns will dramatically improve the rigor of the briefs/ generated for production deployment without burdening the local environment with unnecessary CV/NLP boilerplate bloat." [Source: 5_6 links.docx URL 6]
