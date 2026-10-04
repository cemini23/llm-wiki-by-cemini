---
title: K280 Atto HTR Wave (Oct 2026)
type: concept
tags: [atto, htr, genealogy, k280]
keywords: [k280, kraken, catmus, transkribus, posture-change]
related:
  - concepts/k281-basgiath-wave.md
  - concepts/k278-atto-htr-wave.md
  - sources/eval-htr-repos-2026-10-03.md
maturity: draft
created: 2026-10-03
updated: 2026-10-04
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @concepts/k281-basgiath-wave.md
- @concepts/k278-atto-htr-wave.md
- @sources/eval-htr-repos-2026-10-03.md

## Raw Concept

K280 Atto cluster hub for the **Atto** workstream (priority #1). Dual-ID **OSINT K280**. Prior @concepts/k278-atto-htr-wave.md.

## Narrative

**Posture change.** Across every prior wave, this wiki carried the line *"Transkribus stays the only product HTR."* The operator has now said: **do not stay on Transkribus by precedent; if there is a better solution, adopt it.**

That is correct, and it is recorded as the new posture. The old line rested on a real observation — no evaluated alternative had beaten Transkribus on a measured task — but "nothing has beaten it yet" is not "nothing can."

**Transkribus is now the incumbent with a challenger. It is not the fixed answer.**

### The challenger

`mittagessen/kraken`. Apache-2.0, 1,079 stars, last push 2026-09-24. A real engine — trainable layout analysis, reading order, recognition — CPU-capable, no GPU needed, about 16 MB per model, exports ALTO and PageXML.

Its partner model is **CATMuS Medieval**, which names **Latin, Old French, Middle French, Old Spanish, and Italian** as its languages. Over 160,000 training lines, CC-BY-4.0. That is the first released historical-script model in any wave that names Italian.

### The two things standing in the way

1. **Domain gap.** CATMuS is medieval bookscript. Our records are 19th-century Italian cursive. Fine-tuning on our own labelled pages is required, and no off-the-shelf Kraken model exists for Italian civil registers.
2. **No head-to-head number.** The audit could not find a direct Kraken-versus-Transkribus character-error comparison on a Latin historical benchmark. Two relevant papers sit behind a publisher anti-bot block. **That gap is the thing to close first.**

### The decision procedure

Do not switch on enthusiasm and do not refuse on precedent. Measure.

| Step | What it settles |
|------|-----------------|
| 1 | Transkribus against Kraken+CATMuS on the **same** pages, same ground truth, line CER each. This number decides |
| 2 | If Kraken is within a few points before fine-tuning, label a few thousand lines from one comune and fine-tune |
| 3 | Re-measure. Adopt only on a win |

**The operational argument already favours Kraken.** It is permissive, local-only, and CPU-capable — which fits the Atto no-cloud-HTR constraint rather than merely tolerating it. But an operational advantage is not an accuracy result, and the accuracy result is what is missing.

### A real error caught

The eval docx rated `githubharald/HTRPipeline` **Integrate** and claimed **MIT**. The live API returns `spdx_id: null` — **no licence at all**, all rights reserved — and the repo has been stale since July 2023. A no-licence repo cannot be vendored into a proprietary product.

This is the one narrow case where the licence check still pays: **the eval recommended vendoring an unlicensed repo.** Note it, do not ritualise it.

### What did not qualify

`SimpleHTR` is MIT but an English IAM toy. `PreprocessingHTR` is a preprocessing helper with no model. `cremma-medieval` is Old French data, no Latin and no Italian. Three of the eight rows have no licence at all.

### Boundary

**No clone. Nothing vendored. Transkribus remains the running engine until a measurement says otherwise.** No `truth.ged` merge. No Barone PII.

**Cemini posture:** FILE. **0 product Integrate GO** — with an open evaluation, not a closed one.
