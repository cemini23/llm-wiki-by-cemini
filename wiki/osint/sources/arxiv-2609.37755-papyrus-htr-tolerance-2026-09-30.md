---
title: "Which papyrus HTR is good enough? (2609.37755)"
type: source
tags: [source, k276, atto, htr, error-tolerance]
keywords: [k276, papyri, cer, tolerance, mit, no-clone]
related:
  - concepts/k276-atto-htr-wave.md
maturity: draft
created: 2026-09-30
updated: 2026-09-30
read_status: skimmed
---

## Relations

- @concepts/k276-atto-htr-wave.md

## Raw Concept

| File | `arxiv-2609.37755-which-papyrus-htr-is-good-enough-character-error.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.37755-which-papyrus-htr-is-good-enough-character-error.pdf` |
| Archive | egress-fi 2026-09-30 |
| Retrieved | 2026-09-30 |
| Dual-ID | **OSINT K276** |
| sha256 | `2654750668b46036d1437e10dc15316d32e6407a80eb450b63b4173115298dc5` |
| arXiv | 2609.37755 |
| Authors | Anton Repushko (independent), Elena Chepel (University of Vienna) |
| Repo | `https://github.com/repushko/good_enough_papyrus_htr` |

## Narrative

The question is: how much character error can a downstream task survive? The authors build a letters-only perfect text from 63,846 Greek editions in papyri.info. They degrade it to exact character-error rates from 1% to 50%. Then they train small task models on the noisy text.

The 90%-retention thresholds differ by task. Documentary-versus-literary survives 20% error. Document type survives 7.5% to 12.5% as-is, and 15% after retraining. Search ranking needs 5%. Dating needs 3%.

Two findings transfer to any archive. First, retraining on noisy text removes the collapse: document-type macro-F1 rises from 0.163 to 0.703 at 30% error. Second, lost lines are expensive: losing 30% of lines costs about as much as 5% character error.

Dating never reaches the 50-year bar, even on clean text. The best clean mean absolute error is 55 years.

The authors admit the noise is simulated. Merged lines, split lines, and wrong reading order are not modelled. Greek only.

Result for Atto: not applicable as an HTR engine. It is a task-tolerance study, with no recogniser of its own. The seal idea is reusable: set a per-task error budget before you buy a transcription model. Treat it as a FILING note, not a wire. Repo license is MIT, 23 KB, 0 stars (gh api 2026-09-30). No clone.
