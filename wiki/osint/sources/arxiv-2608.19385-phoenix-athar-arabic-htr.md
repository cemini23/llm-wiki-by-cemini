---
title: Phoenix + Athar — compact Arabic manuscript HTR with evidence-aware review
type: source
tags: [htr, arabic, manuscripts, continual-learning, atto]
keywords: [phoenix, athar, CNN-BiLSTM-CTC, CER, greedy_text, unique-ambiguous-abstain, CC-BY-NC-SA, factlogic]
related:
  - concepts/arabic-htr-evidence-review.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
read_status: skimmed
---

## Relations
- @concepts/arabic-htr-evidence-review.md
- @concepts/computational-genealogy-archival-automation.md
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept
- **title:** Phoenix and Athar: Compact Multi-Domain HTR with Evidence-Aware Review for Arabic Manuscripts
- **author:** Abdullah Ahmed Ali Mohammed, Thamer Abdulhadi, Ali Haider, Safaa Dhulfiqar Mahdi Wadi (University of Technology, Baghdad; Hugging Face factlogic)
- **type:** arXiv paper + Hugging Face model card
- **location:** research to be indexed/arxiv-2608.19385-phoenix-athar-arabic-htr.pdf
- **retrieved:** 2026-08-21
- **pages:** arXiv HTML (full skim of abstract, system, sealed eval, oracle gap, Athar workflow, licence)
- **read-status:** skimmed

## Narrative
Phoenix is a 4.99M-parameter (19.94 MB) CNN–BiLSTM–CTC line recognizer with an 81-symbol codec. Athar is the evidence-aware review layer around it. The paper’s claim is not “better OCR”; it is that scholarly HTR is auditable evidence management, not silent text replacement.

Sealed, frozen, greedy, raw-reference eval on 22,278 large-set lines (Agapet 10,594 + Omar 11,684) dropped character-weighted CER from 19.98% to 14.93% (25.3% relative). Agapet 22.12%→17.86%; Omar 17.72%→11.84%. A 164-line TariMa set *regressed* 10.39%→10.72% and is reported, not hidden. Domain specialists added only 0.07–0.44 pp CER, so they kept one unified model. Replay + forgetting guards (mean ≥0.1 pp gain, ≤0.1 pp single-guard regression, ≤0.5 pp vs prior release) selected the checkpoint.

The steal is the candidate-selection bottleneck. On a 250-line five-domain diagnostic, beam 7.97% CER vs Oracle@25 5.82% — a 2.15 CER oracle gap. Neural rerankers, MBR, CTC-posterior QE, and pre-CTC hidden-state QE recover <4% of that gap. Therefore Athar: (1) preserves greedy visual reading (`greedy_text`) even when an LM suggestion is accepted; (2) retrieval states unique / ambiguous / abstain, never unique-from-a-truncated-list; (3) default training export is human-approved GT only; (4) replay + forgetting guards; (5) domain-conditioned LMs are evidence, not overwrite (mismatched general LM *raised* archival CER 11.52%→14.78%). Model licence: CC BY-NC-SA 2.0. Hugging Face: factlogic/phoenix-arabic-manuscript-htr. Do not silently LM-correct Atto lines.

## Snippets
> Historical Arabic manuscript transcription is not only a recognition problem. A usable scholarly system must … preserve uncertain readings, distinguish visual evidence from linguistic plausibility … and record the researcher’s final decision. [Source: arxiv-2608.19385-phoenix-athar-arabic-htr.pdf p.1]

> Because automated sequence selection fails to reliably bridge this oracle headroom, Athar preserves the visual reading, exposes bounded alternatives, … retrieves parallels with explicit unique/ambiguous/abstain states, and exports auditable TEI and PAGE-XML records. [Source: arxiv-2608.19385-phoenix-athar-arabic-htr.pdf p.1]

> The work demonstrates that manuscript HTR should be evaluated and deployed as auditable evidence management rather than silent text replacement. [Source: arxiv-2608.19385-phoenix-athar-arabic-htr.pdf p.1]

> Across the two large held-out sets, character-weighted CER fell from 19.98% to 14.93% … An N-best diagnostic … reveals … an oracle gap of 2.15 CER points (Beam 7.97% vs. Oracle@25 5.82%). [Source: arxiv-2608.19385-phoenix-athar-arabic-htr.pdf p.1]

Phoenix checkpoint exp9 SHA-256 prefix `2896fef9d9665cbb`. Licence CC BY-NC-SA 2.0. [Source: https://huggingface.co/factlogic/phoenix-arabic-manuscript-htr (retrieved 2026-08-21)]
