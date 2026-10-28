---
title: "Trojan threats in the LLM activation-steering supply chain"
type: source
tags: [source, arxiv, supply-chain, llm-security]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Steering for Safety, Hijacking for Profit: Trojan Threats in the LLM Activation Steering Supply Chain |
| Authors | Yu Yan (Information Engineering University), Jiahao Chen (Zhejiang University), Siqi Lu, Yongjuan Wang, Ziming Zhao, Zhaoxuan Li, Qingjun Yuan |
| arXiv | 2610.35043 |
| File | `arxiv-2610.35043-steering-for-safety-hijacking-for-profit-trojan.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.35043 |
| Read status | skimmed (abstract + intro) |

## Narrative

Steering vectors change model behaviour by intervening in internal representations. Users
install them as third-party plugins, the same way they install other model customisations.
The paper treats that plugin ecosystem as a supply chain, and audits it.

The threat model is a malicious plugin. It presents a legitimate function. It then quietly
shifts the model's output, while keeping measured model performance close to normal. A user
sees no obvious drop in quality.

The authors audit **eight mainstream open-source Steering plugin libraries**. They report
three structural vulnerabilities:

- **Insufficient distribution integrity verification.** A user cannot confirm that the
  vector they install is the vector that was published.
- **Excessive plugin privileges.** A plugin holds more access than its stated function needs.
- **Missing runtime monitoring.** No component observes what a loaded steering vector does to
  live output.

Defensive implication: treat a steering vector as executable third-party code, not as a
configuration value. Apply the controls a team already uses for package supply chains —
pinning, provenance, least privilege, and runtime observation. The audit covers eight
libraries, so the finding is a class-level observation, not a per-library disclosure. Treat
the specific counts as single-source.

## Snippets

> "This paper audits eight mainstream open-source Steering plugin libraries and reveals three structural vulnerabilities: insufficient distribution integrity verification, excessive plugin privileges, and missing runtime monitoring." [Source: `arxiv-2610.35043-steering-for-safety-hijacking-for-profit-trojan.pdf` p.1 (arXiv 2610.35043), retrieved 2026-10-27]
