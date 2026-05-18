---
title: "mlfinlab (Hudson & Thames)"
type: entity
tags: [tool, machine-learning, quant-finance, backtesting, reject, license-unverified, k51]
keywords: [mlfinlab, hudson-and-thames, financial-machine-learning, quant-research, cemini-financial]
related:
  - sources/multi-wiki-tool-eval-prompt-2026-05-18.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/multi-wiki-tool-eval-prompt-2026-05-18.md — K51 multi-wiki tool-eval; Reject verdict, Cemini-financial primary fit
- @concepts/cemini-license-posture.md — license-unverified → reject under the IP-sale posture

## Raw Concept

What prompted this page: K51 multi-wiki tool-eval (`@sources/multi-wiki-tool-eval-prompt-2026-05-18.md`) URL 32. Reject, Cemini-financial primary.

## Narrative

`hudson-and-thames/mlfinlab` — a comprehensive machine-learning-for-finance toolbox from the Hudson & Thames quantitative research group: reproducible, interpretable tooling for portfolio managers and traders. 4.7k★, institutional pedigree. Directly augments the `/opt/cemini` algorithmic-trading stack and strategy backtesting.

**Verdict: Reject — confirmed.** License check 2026-05-18 (GitHub API): the repo ships a `LICENSE.txt`, but GitHub classifies it as **"Other" / `NOASSERTION`** — i.e. not a recognised OSS license. This is consistent with Hudson & Thames' known commercial posture (mlfinlab is gated behind a paid subscription, not released under a permissive OSS license). A non-standard, non-permissive license is unusable in the IP-sale-bound `/opt/cemini` stack → **hard Reject, verified** `[CONFIRMED: non-OSS license]`.

Cemini takeaway: mlfinlab implements published financial-ML techniques (mostly from López de Prado's *Advances in Financial Machine Learning*). If those methods are wanted, work from the book / papers directly — do not depend on this commercially-licensed library.
