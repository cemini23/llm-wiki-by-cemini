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

**Verdict: Reject.** The main `mlfinlab` library's license is **unverified** in the retrieval data — and Hudson & Thames have historically gated mlfinlab behind a paid/subscription model rather than a permissive OSS license, so the burden of proof is high. (A secondary tutorial repo carries MIT, but that does not cover the core library.) Integrating these algorithms into the core financial suite without a definitively permissive license is an existential IP-sale risk → hard reject.

`[NEEDS VERIFICATION 2026-05-18]` — ascertain the precise licensing framework Hudson & Thames apply to the main `mlfinlab` library; a paid/commercial or copyleft result keeps this a permanent reject.
