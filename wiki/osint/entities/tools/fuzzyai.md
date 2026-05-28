---
title: FuzzyAI — Adversarial prompt patterns (PAIR/Crescendo) (Adopt-tier)
type: entity
tags: [tool, adversarial, prompt-injection, PAIR, Crescendo, adopt-tier, cybersec-cross-route, news-rewriter-defense]
keywords: [fuzzyai, prompt injection, adversarial prompts, PAIR, Crescendo, news rewriter, financial news robustness]
related:
  - sources/evaluating-urls-cemini-project-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/verbalized-sampling-llm-diversity.md
maturity: draft
created: 2026-05-13
updated: 2026-05-28
---

## Relations

- `@sources/evaluating-urls-cemini-project-2026-05-13.md` — origin source (Doc 1, K42), Adopt-tier
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/verbalized-sampling-llm-diversity.md` — Vector 5 (news-feed adversarial robustness testing) directly intersects FuzzyAI's PAIR/Crescendo prompt patterns

## Raw Concept

Stub created from Doc 1 K42 eval (2026-05-13). Adopt-tier; cross-routed to OSINT-wiki (financial-news adversarial detection) + Cybersec-wiki (prompt-injection defensive ops).

## Narrative

- **Eval claim**: PAIR and Crescendo prompt structures for adversarial LLM manipulation testing.
- **Cemini use case**: defensive layer on the news-rewriter / sentiment-classifier path — catalog known prompt-injection patterns to harden against adversarial financial-news inputs.
- **Intersects K39 VS Vector 5**: generate diverse sentiment-shifted rewrites for testing robustness; FuzzyAI provides the adversarial input vocabulary.

### Phase-0 audit (2026-05-28)

Repo: `cyberark/FuzzyAI` — **Apache-2.0**, ~1.4k★, active, tests present.

**Verdict: CONDITIONAL-GO (cybersec / defensive testing)** — use for adversarial prompt-pattern catalogs in security workflows; not a Cemini trading-runtime component.

[Source: Evaluating URLs for Cemini Project.docx (retrieved 2026-05-13)]
