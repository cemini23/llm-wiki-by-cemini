---
title: "HTR repository Phase-0 audit — 8 rows (2026-10-03)"
type: source
tags: [source, k280, atto, htr, eval]
keywords: [k280, kraken, catmus, transkribus, phase0]
related:
  - concepts/k280-atto-htr-wave.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
read_status: skimmed
---

## Relations

- @concepts/k280-atto-htr-wave.md

## Raw Concept

| File | `Revenue Opportunity Repository Evaluation.docx` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Revenue Opportunity Repository Evaluation.docx` |
| Archive | egress-fi 2026-10-03 |
| Retrieved | 2026-10-03 |
| Dual-ID | **OSINT K280** |
| sha256 | see the archive record |
| Method | Phase-0 audit. Live GitHub REST API, raw READMEs, and publisher records. Direct clone was blocked by this session's network policy, so every figure below comes from the API or a cited source, not from a checkout |

## Narrative

Eight HTR rows. The operator asked a direct question: is anything here better than Transkribus, and should we stop treating Transkribus as fixed?

**The answer is: one candidate is viable, and it needs work we have not scoped.**

### `mittagessen/kraken` — the only real engine

| Signal | Value |
|--------|-------|
| License | **Apache-2.0** |
| Stars / forks | 1,079 / 176 |
| Last push | **2026-09-24** (9 days before this audit) |
| What it is | A full OCR/HTR **engine**: trainable layout analysis, reading order, recognition. CLI plus Python API. Exports ALTO, PageXML, hOCR |
| Models | None bundled. Fetched from a public Zenodo repository |
| GPU | **Not required.** CPU-capable |
| Model size | About 16 MB per model |

**The model that matters: CATMuS Medieval.** It explicitly lists **Latin, Old French, Middle French, Old Spanish, and Italian** among its languages (Zenodo record 10.5281/zenodo.15030337, CC-BY-4.0). Its training corpus is Latin-script, over 160,000 lines, and includes both Italian and Latin.

That is the first time in any wave we have found a released historical-script model that names Italian.

### The honest caveat

**CATMuS is medieval bookscript. Italian civil registers are 19th-century cursive hands.** A model trained on medieval manuscripts is not a finished answer for civil records. Domain fine-tuning on our own labelled pages is required, and the audit found **no off-the-shelf Kraken model for 19th-century Italian civil registers.**

Fine-tuning needs a labelled corpus. The README states no volume; realistically a few thousand labelled lines to adapt CATMuS to civil-register hands.

### Accuracy evidence found

| Setting | Reported |
|---------|----------|
| Kraken pipeline, medieval French | **6.0% line CER**; 15.2% on an unseen manuscript, against 15.3% for a TrOCR+LoRA baseline |
| CATMuS-Medieval, unseen 17th-c Spanish and Hokkien | About 10.0% to 11.4% CER, against about 7.7% to 8.1% for a PyLaia baseline |

**A direct Kraken-versus-Transkribus head-to-head CER was not found.** The two most relevant papers sit behind an anti-bot block on their publisher site. The audit says so rather than guessing. That gap is the single most important thing to close before any switch.

### The docx got one row badly wrong

The docx rated `githubharald/HTRPipeline` **Integrate** and claimed **MIT**. The live API returns **`spdx_id: null`** — **no licence at all**, which means all rights reserved. It was also last pushed in July 2023 with four commits, and its weights come from a Dropbox link of unknown provenance.

**A no-licence repo cannot be vendored into a proprietary product.** The docx recommended exactly that. This is the one place where the licence call still earns its keep, and it caught a real error.

### The rest

| Repo | Verdict | Why |
|------|---------|-----|
| `githubharald/SimpleHTR` | Not a candidate | MIT, but a minimal CTC model trained on **IAM English** handwriting. About 10% CER on IAM. **No evidence of historical, Romance, or Italian fit** |
| `KadenMc/PreprocessingHTR` | Not a candidate | MIT, preprocessing only — crop, deskew, binarize, line clustering. Ships no model. Superseded by Kraken's own segmenter |
| `HTR-United/cremma-medieval` | Useful data, not an engine | CC-BY-4.0, 15 Old French manuscripts, 22,662 lines, three Kraken models. **Old French only — no Latin, no Italian.** Its descendant CATMuS is the one that adds both |
| `Intellindust-AI-Lab/HTR-VT` | Watch | Vision transformer. No licence found, no pretrained Italian weights |
| `raphael-baena/DTLR` | Watch | Polygon line detection. No licence found |
| `him4318/Transformer-ocr` | Context | No licence found, no evidence shown |

**Read the Watch and Context rows for what they are: unlicensed experiments.** Three of the eight have no licence at all.

## The recommendation

**Do not switch yet. Do not dismiss either.**

The path, in order:

1. **Close the evidence gap.** Run a head-to-head on our own pages: Transkribus against Kraken plus CATMuS, same pages, same ground truth, line CER each. That number decides it.
2. **If Kraken is within a few points before fine-tuning, fine-tune.** Label a few thousand lines from one comune, adapt CATMuS, and re-measure.
3. **Adopt only on a measured win.** Transkribus is a paid managed service; Kraken is Apache-2.0, CPU-capable, and runs locally. Local-only is already an Atto hard ban we satisfy, so the operational argument favours Kraken — but the accuracy argument is unproven.

**Transkribus is no longer the fixed answer. It is now the incumbent with a challenger.** That is a real change in posture, and it is recorded as such.

**No clone. Nothing vendored. 0 product Integrate GO.**
