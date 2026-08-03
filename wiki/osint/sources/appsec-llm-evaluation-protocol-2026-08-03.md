---
title: "AppSec LLM Evaluation Protocol (Local Authorized Assistants) 2026-08-03"
type: source
tags: [source, appsec, llm-eval, cybersec, k219]
keywords: [60GG-2, FS-815.06, OWASP, Inspect-AI, Juice-Shop, over-refusal, hallucination]
related:
  - concepts/cemini-license-posture.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
read_status: skimmed
---

## Relations

- @concepts/cemini-license-posture.md
- @concepts/wiki-tooling-evaluation.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | AppSec LLM Evaluation Protocol.docx |
| sha256 | `7523677ec8437b8f454a8792890bb973b1a044bf8e7c2e88ed576c8167362b10` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/AppSec LLM Evaluation Protocol.docx` |
| Framing | Florida 60GG-2 / FS 815.06 (authorized AppSec assistants only) |
| read_status | skimmed |

## Narrative

Local open-weight LLM eval protocol for **authorized** AppSec assistants — cloud models rejected on source/zero-day exfil risk. Frames Florida Cybersecurity Standards (60GG-2) + Computer Crimes Act (FS 815.06) as the legal boundary: no third-party exploitation tooling.

**Eight axes:** six technical proficiency scores (0–5) plus over-refusal and hallucination/unsafe-confidence penalties. Harness: OWASP-mapped prompt gauntlet, Inspect AI, Juice Shop labs. Goal = assist operators on owned systems with lab-only PoCs — not automated exploitation engines.

**Route → cybersec-wiki** (brief preferred over OSINT stub farm). OSINT keeps this source page + license/eval cross-links only.

## Snippets

> …adoption of local, open-weight LLMs is critical for maintaining data sovereignty… particularly pronounced under the State of Florida Cybersecurity Standards (Florida Administrative Code 60GG-2)… [Source: AppSec LLM Evaluation Protocol.docx]

> Highly aligned models often exhibit "exaggerated safety behaviors," leading to the over-refusal of legitimate, authorized security queries… heavily fine-tuned or "uncensored" models frequently suffer from dangerous overconfidence, hallucinating vulnerabilities… [Source: AppSec LLM Evaluation Protocol.docx]
