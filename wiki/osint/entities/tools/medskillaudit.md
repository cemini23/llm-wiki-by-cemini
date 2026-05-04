---
title: MedSkillAudit — LLM-Skill Validation Veto-Gate Framework (MIT)
type: entity
tags: [llm-agents, skill-validation, audit-framework, prompt-validation, mit, steal-from, healthcare-prediction-markets]
keywords: [medskillaudit, veto-gates, llm-skill-validation, static-dynamic-scoring, prompt-quality-audit, biotech-prediction]
related:
  - sources/5-4-links-tool-eval.md
  - sources/gemini-sci-research-2602-03837.md
  - entities/tools/financetoolkit.md
maturity: draft
created: 2026-05-04
updated: 2026-05-04
---

## Relations

- @sources/5-4-links-tool-eval.md — origin source: 2026-05-04 Gemini DR eval, URL 9 (`aipoch/medical-research-skills`), **Steal-from** tier verdict
- @sources/gemini-sci-research-2602-03837.md — Gemini paper §2.7 ("Optimizing Context") + §2.4 ("Formalization & Rigor Checks") establish the same kind of pre-deployment validation principles MedSkillAudit operationalizes
- @entities/tools/financetoolkit.md — pairs with FinanceToolkit for healthcare/biotech prediction-market analysis: MedSkillAudit validates the medical-research prompts; FinanceToolkit provides corporate fundamentals on the same biotech tickers

## Raw Concept

LLM-skill validation framework bundled with `aipoch/medical-research-skills` repo. Implements a two-stage scoring system (40% Static + 60% Dynamic) and explicit "Veto Gates" (Operational Stability, Scientific Integrity) that gate skill deployment. Identified as **Steal-from-tier** in the 2026-05-04 Gemini DR eval — extract framework, reject domain-specific medical content for trading-stack use, but **the medical-research content is directly relevant for biotech prediction-market analysis** (per user note 2026-05-04).

## Narrative

- **Container repo URL**: https://github.com/aipoch/medical-research-skills
- **License**: MIT (clean for IP-sale)
- **Stack**: Python 89.8%, TeX 6.3%, designed for OpenClaw / Claude Code / Hermes Agent compatibility
- **Maturity**: 175 commits, 478 stars, 39 forks, 6 organized releases

### The framework (load-bearing content)

MedSkillAudit gates skill deployment via:

1. **Static checks (40% weight)** — pre-runtime: prompt structure, format compliance, constraint coverage, declared input/output contracts
2. **Dynamic checks (60% weight)** — runtime: actual LLM output against expected outcomes on test cases
3. **Veto Gates** — categorical pass/fail (any veto = deployment blocked):
   - **Operational Stability** — does the skill execute deterministically across N test runs?
   - **Scientific Integrity** — does it produce outputs consistent with domain ground truth?

### Why Steal-from for Cemini

Direct adaptation: refactor MedSkillAudit into `wiki_lint.py` + a new `prompt_lint.py` script that validates financial-reasoning prompts before they're staged via `briefs/` → `/opt/cemini/briefs/`. The static / dynamic / veto-gate structure maps cleanly:

| MedSkillAudit gate | Cemini equivalent |
|--------------------|-------------------|
| Static — Operational | Static — JSON-schema output, deterministic-output check |
| Static — Scientific Integrity | Static — citation completeness, frontmatter conformance |
| Dynamic — Operational Stability | Dynamic — N-trial output reproducibility |
| Dynamic — Scientific Integrity | Dynamic — backtest agreement, factual accuracy on known queries |

### Direct in-domain use for healthcare equities AND prediction markets

Per user notes 2026-05-04: medical-research content applies to **both halves** of Cemini's market scope:

1. **Healthcare equities** — biotech/pharma tickers (MRNA, NVAX, BIIB, large-cap pharma, small-cap biotechs awaiting catalysts) are core healthcare-investing territory. The skill library's clinical-experimental-design + statistical-data-analysis + evidence-insight modules apply directly to ticker-research workflow: drug-trial outcome assessment, FDA approval probability estimation, clinical-paper interpretation feeding equity decisions.
2. **Prediction markets** — Kalshi + Polymarket healthcare contracts (FDA approval markets, drug-trial outcomes, public-health policy contracts). Same medical-research skills feed Brier-score-optimized prediction-market positions.

Both use cases share the same upstream analytical work — clinical-trial outcomes inform both the equity position on the biotech ticker and the prediction-market position on the FDA approval contract. The MedSkillAudit framework + skill library is general-purpose enough to feed either trade-execution destination.

This reframes the original Gemini DR verdict ("medical domain orthogonal to trading"): MedSkillAudit is general-purpose **and** the medical content has direct relevance to healthcare equities + prediction markets.

### Adaptation work

1. **Generic veto-gate framework** → port to Python module under `scripts/skill_audit.py`
2. **Financial-domain veto criteria** → write Cemini-specific dynamic checks (backtest agreement, JSON-schema compliance, factual accuracy on known queries)
3. **Healthcare-domain veto criteria** (deferred) → if/when Cemini opens healthcare prediction-market depth, the original medical skills + audit checks transfer near-directly

## Snippets

- **Framework composition**: "embedded auditing framework called 'MedSkillAudit,' which performs rigorous static and dynamic quality checks—utilizing a network of 'Veto Gates'—before any generated skill is deployed to an agent." [Source: 5_4 links.docx URL 9]

- **Scoring split**: "two-stage scoring system (40% Static, 60% Dynamic) and strict 'Veto Gates' (checking Operational Stability, Scientific Integrity)." [Source: 5_4 links.docx URL 9]

- **Recommendation tier**: "Steal-from. Reject the medical and bioinformatics content entirely. However, extract the MedSkillAudit Python testing framework and the conceptual Veto Gate architecture. Refactor these methodologies to audit the financial reasoning, strict output formatting, and prompt-injection resilience of the deepseek-v4-pro model within the Cemini repository." [Source: 5_4 links.docx URL 9]
  - **NOTE 2026-05-04**: per user note, "Reject the medical content entirely" verdict is too strong — medical content is directly applicable for healthcare/biotech prediction-market analysis on Kalshi/Polymarket. Updated verdict: **adopt framework now, defer medical-content adoption until prediction-market healthcare depth becomes priority.**
