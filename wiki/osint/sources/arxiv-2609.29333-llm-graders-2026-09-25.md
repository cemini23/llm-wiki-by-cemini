---
title: "Where LLM Graders Succeed and Break"
type: source
tags: [arxiv, source, k272, harness]
keywords: [k272, LLM-graders, exam, preamble, 404]
related:
  - concepts/k272-harness-evolution-wave.md
maturity: validated
created: 2026-09-25
updated: 2026-09-25
read_status: deep-read
---

## Relations

- @concepts/k272-harness-evolution-wave.md

## Raw Concept

| Paper | arXiv:2609.29333 |
| File | `arxiv-2609.29333-where-llm-graders-succeed-and-break-evidence-fro.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.29333-where-llm-graders-succeed-and-break-evidence-fro.pdf` |
| Archive | egress-fi 2026-09-25 |
| Authors | Ali Habibullah, Yazan Alshoibi, Mohammad Alshiekh, Salman Khan, Naeemullah Khan (KAUST; Oxford Brookes) |
| Retrieved | 2026-09-25 |
| Pages | 38 |
| Dual-ID | **OSINT K272** |
| sha256 | `07690023c4437d0316a4cfccc261dd775f034eb28abec6696bdc1f65bd4395af` |
| Code | KAUST graders repo 404 on 2026-09-25 |

## Narrative

The paper grades one computer-vision exam (570 dual-graded students) under 171 model settings. The best mean absolute error is 1.64/35. Two human graders differ by 2.61/35 against each other. A short "strict grader" preamble pushes 14 of 17 open-weight models out of the graded band (MAE ≥ 8), and three models stop grading altogether. The damage traces to the preamble's two credit-withholding sentences, not to tone or model scale; one sentence, "never give partial credit," alone makes two of three probed models stop grading. Closed flagship models from three vendors shift calibration under the preamble but stay in the band. A replication on a second independent Machine Learning exam (1,038 dual-graded students) under 162 configurations worsens ten models, moving three out of the band into collapse and one into refusal, yet improves seven whose neutral prompts over-mark. The vulnerability replicates but its direction is exam-specific. Light LoRA fine-tuning on the pooled ~3,900 graded examples brings five small open models to parity or better with a human grader and nearly eliminates sensitivity to the three harsh personas (≤0.32 MAE). The KAUST graders repo returned **404** on 2026-09-25. No clone.

**Cemini posture:** FILE. No clone. **0 product Integrate GO.** Do not install a grader. Never auto-evolve skills.

## Snippets

> "A short 'strict grader' preamble drives 14 of 17 open-weights models out of the graded band (MAE ≥ 8), three stopping grading altogether." [Source: https://arxiv.org/html/2609.29333 (retrieved 2026-09-25)]

> "Light LoRA fine-tuning on the two exams' pooled ~3,900 examples brings five small open models to parity or better with a human grader and nearly eliminates sensitivity to the three harsh personas (≤0.32 MAE)." [Source: https://arxiv.org/html/2609.29333 (retrieved 2026-09-25)]