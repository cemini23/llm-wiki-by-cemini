---
title: "CodeMimicry: safety generalization lag in code (2609.39902)"
type: source
tags: [source, k277, security, safety, threat-class]
keywords: [k277, codemimicry, safety-lag, mitigation, no-poc]
related:
  - concepts/k277-security-wave.md
maturity: draft
created: 2026-10-01
updated: 2026-10-01
read_status: skimmed
---

## Relations

- @concepts/k277-security-wave.md

## Raw Concept

| File | `arxiv-2609.39902-codemimicry-exploiting-safety-generalization-lag.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.39902-codemimicry-exploiting-safety-generalization-lag.pdf` |
| Archive | egress-fi 2026-10-01 |
| Retrieved | 2026-10-01 |
| Dual-ID | **OSINT K277** |
| sha256 | `24295d61ede94b2768549a0ec85b4fa4235328d35a23c44e4a404aa3727f5f8b` |
| arXiv | 2609.39902 |
| Authors | Zhen Liang, Hai Huang, Wentao Chen (Zhejiang Sci-Tech University; CAICT) |
| Repo | `https://github.com/lzzzr123/CodeMimicry` |

## Narrative

The paper names a failure mode: **safety generalization lag**. Safety alignment trains mostly on natural language, so it does not carry over to the code domain. That leaves a blind spot where harmful intent placed inside syntactically valid code does not trigger a refusal.

The authors test this with an automated black-box loop that wraps a harmful request inside object-oriented code, then presents it as an ordinary completion request. Reported success: 96.25% on one safety benchmark and 96.07% on another, across eight commercial models, in about 1.5 attempts on average.

The defensive half is the part worth keeping. Their measurements show prompt-level defences are weak here:

| Defence | Residual success |
|---------|-----------------|
| Llama Guard and perplexity filtering | 76% to 100% |
| Representation Bending | 38% |
| Circuit Breaker | 8% |
| SelfDefend | 4% to 14% |

Comment filtering substantially lowers success. The authors note the method depends on the target having strong code ability, and that it uses comments and docstrings as a side channel, which is why stripping them helps.

The defensive takeaway: prompt-level detection does not cover the code domain. Hidden-layer interventions and code-domain alignment do. This is a threat class and a mitigation table only. No payload, no step list, no working recipe on this page. **No PoC.**

Repo SPDX is **null**, 580 KB, 1 star (gh api 2026-10-01). A null SPDX records the pattern only. No clone. FILE only.
