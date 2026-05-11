---
title: "google-research / google-research (monorepo)"
type: entity
tags: [tool, ml-monorepo, academic-research, google, steal-from, k38]
keywords: [google, research, monorepo, steal-from, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 2)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/google-research/google-research`
- **Tier (per source brief)**: **Steal-from**
- **License**: Apache-2.0 (Google standard)

## Narrative

Google's official archival monorepo: ML models, algorithms, research utilities. ALBERT, BERT Seq2Seq, adaptive learning-rate tuners, feature engineering utilities. Library of academic + experimental codebases — not a deployable product.

### Integration vector

Steal-from: identify + mathematically study specific numerical algorithms, feature-engineering scripts, and learning-rate tuning methodologies; reimplement within Cemini's quant analysis modules. Do NOT adopt the monorepo wholesale.

### Risks

Academic 'publish and abandon' lifecycle — many subdirs rely on deprecated TF/PyTorch/Python; refactoring required for integration with FastAPI/Polars.

[Source: Link Evaluation Brief Trading Stack.docx, URL 2]
