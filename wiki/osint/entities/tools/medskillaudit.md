---
title: MedSkillAudit — LLM-Skill Validation Veto-Gate Framework (MIT)
type: entity
tags: [llm-agents, skill-validation, audit-framework, prompt-validation, mit, steal-from, healthcare-prediction-markets]
keywords: [medskillaudit, veto-gates, llm-skill-validation, static-dynamic-scoring, prompt-quality-audit, biotech-prediction]
related:
  - sources/5-4-links-tool-eval.md
  - sources/gemini-sci-research-2602-03837.md
  - entities/tools/financetoolkit.md
maturity: validated
created: 2026-05-04
updated: 2026-05-04
---

## Workspace-side port — deployed 2026-05-04

`scripts/skill_audit.py` ships a clean-room re-implementation of the MedSkillAudit veto-gate framework, scoped to brief / skill / prompt validation. Stdlib-only (no external deps); matches the style of `scripts/wiki_lint.py`.

### Implemented checks (Static phase, 40% of design weight)

| # | Check | Weight | Behavior |
|---|-------|--------|----------|
| 1 | required_sections | 0.30 | VETO if `## Target` or `## Summary` missing; WARN if no `## Sources`/`## References` |
| 2 | crosslinks | 0.20 | VETO if any `@path/to/page.md` doesn't resolve to a real file (tries both wiki-relative + repo-relative — briefs use `@wiki/...`, wiki pages use `@concepts/...`) |
| 3 | citations | 0.15 | PASS if `## Sources` section exists OR ≥1 inline `[Source: ...]` tag; WARN if both absent |
| 4 | needs_verification_freshness | 0.10 | WARN if any `[NEEDS VERIFICATION YYYY-MM-DD]` tag is older than `--nv-age-days` (default 30) |
| 5 | prose_quality | 0.15 | WARN if emoji or TODO/FIXME/XXX markers present (technical Unicode arrows / check-marks deliberately allowed) |
| 6 | frontmatter | 0.10 | PASS if absent (briefs typical) or well-formed YAML block |

### Deferred to v0.2 (Dynamic phase, 60% of design weight)

Requires a sandboxed LLM API endpoint (Conductor or DeepSeek). Tests:
- N-trial output reproducibility
- Structured-output schema-compliance rate
- Hallucinated-citation detection
- Factual-accuracy on known-answer queries

### Veto gates wired

- **Operational Stability** — file parses + required sections present
- **Scientific Integrity** — every cross-link / citation tag resolves (no orphans)

### CLI

```
python3 scripts/skill_audit.py briefs/2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md
python3 scripts/skill_audit.py --json briefs/some.md       # machine-readable
python3 scripts/skill_audit.py --strict briefs/some.md     # warnings → veto
python3 scripts/skill_audit.py --nv-age-days 7 briefs/...  # tighter NV freshness gate
```

Exit codes: 0 PASS / 1 WARN / 2 REJECT / 3 ERROR.

### Smoke test (2026-05-04)

All 4 K28 briefs pass at 100.0/100:
- `2026-05-04_klaassen-magnus-elo-cemini-fastmcp.md` ✓
- `2026-05-04_quant-libs-fastmcp-integration.md` ✓
- `2026-05-04_autoresearch-conductor-evolution.md` ✓
- `2026-05-04_probablyprofit-pattern-extraction.md` ✓

Veto-gate behavior verified earlier in iteration: deliberately-malformed cross-links triggered REJECT correctly.

### Adoption status

- Workspace-side port (this script) ✅ shipped 2026-05-04
- Healthcare-equity / prediction-market skill-content adoption: deferred until those verticals open
- Dynamic phase (60% weight): v0.2, requires sandboxed LLM endpoint

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
