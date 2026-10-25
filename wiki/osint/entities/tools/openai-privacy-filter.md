---
title: "openai/privacy-filter — Apache-2.0 PII filter (Atto Extract, K239)"
type: entity
tags: [tool, atto, pii, k239, phase-0]
keywords: [openai, privacy-filter, PII, NER, codice-fiscale, fixtures]
related:
  - sources/eval-url-revenue-opportunity-2026-08-15.md
  - entities/tools/privacy-filter.md
  - concepts/atto-genealogy-agent-kit.md
  - entities/tools/fclones.md
maturity: draft
created: 2026-08-15
updated: 2026-08-15
harness_verb: FILE
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-15.md — K239 eval (GO Extract)
- @entities/tools/privacy-filter.md — **name collision**: packyme/privacy-filter (K215, MIT)
- @concepts/atto-genealogy-agent-kit.md — vault sanitization + synthetic fixtures
- @entities/tools/fclones.md — archive hygiene sibling

## Raw Concept

What prompted this page: K239 eval URL 17. Docx said Apache/MIT; **gh api = Apache-2.0**. Cloned `.local/adopts/openai-privacy-filter` (1MB). Distinct from `@entities/tools/privacy-filter.md` (`packyme/privacy-filter`, K215).

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/openai/privacy-filter |
| License | **Apache-2.0** |
| Local | `.local/adopts/openai-privacy-filter` (1MB) |
| Verdict | **GO Extract** — regex/NER rule lists into Atto vault/privacy.py; do not pull live Barone records through it into git |

Python regex + NER rule engine for redacting PII in prompts, eval traces, and fixtures. Steal: deterministic patterns for SSN-class IDs, plus a place to hang **codice fiscale / passport / living-relative contact** rules before any MCP/LLM hop.

### Steal-for-Atto

- Fail-closed strip before any outbound model call or public fixture.
- Do **not** over-redact historical commune/province names (false-positive risk on Italian archives) `[OPEN QUESTION 2026-08-15]`.
- Synthetic Rossi / 900-series SSN fixtures only. **Never** living-person vitals in git or Atto kit fixtures.

Tier: `[TENTATIVE]`.
