---
title: VIR-5500 Equity Research Dossier (Gemini Deep Research)
type: source
tags: [source, docx, gemini-deep-research, biotech, VIR, VIR-5500, prostate, oncology, k179]
keywords: [VIR-5500, AMX-500, PRO-XTEN, Astellas, JANX007, Pluvicto, NCT05997615, ECLIPSE, mCRPC]
clusters: [k179-ingest]
related:
  - entities/tickers/vir.md
  - sources/gemini-vir-5500-commercial-strategy-dossier-2026-07-21.md
maturity: draft
read_status: read
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- @entities/tickers/vir.md — ticker synthesis page (VIR-5500 primary thesis)
- @sources/gemini-vir-5500-commercial-strategy-dossier-2026-07-21.md — Gemini DR v2 commercial/demand sister dossier (K181)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | VIR-5500 Deep-Research Dossier: Validating the Prostate Cancer Re-Rating Thesis |
| **Author / origin** | Gemini Deep Research (operator prompt `briefs/2026-07-21_vir-5500-gemini-deep-research-prompt.md` → inbox) |
| **Type** | Word docx — equity research dossier |
| **Filename** | `VIR-5500 Equity Research Dossier.docx` |
| **sha256** | `f42a557b8ef3d5f216a08d1b44ace507f44239e7e24330cd3e31d7fb73a77fa3` |
| **Size** | 35,523 bytes |
| **Retrieved** | 2026-07-21 (inbox) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/VIR-5500 Equity Research Dossier.docx` |
| **read_status** | read |
| **Extract** | `.local/reports/2026-07-21_vir-5500-gemini-dossier-extract.md` (gitignored local) |

## Narrative

Gemini Deep Research dossier commissioned 2026-07-21 to stress-test the **VIR-5500** (PSMA dual-masked TCE) prostate thesis for Vir Biotechnology (NASDAQ: VIR). Primary framing matches operator redirect: oncology first, HDV/ECLIPSE secondary.

**What the dossier gets right (keep):**
- Strict **cutoff discipline** — discard ASCO GU abstract #17 Sep 23, 2025 (n≈51) headlines; use Jan 9, 2026 IR/ASCO oral cut (n=58) as expansion baseline.
- Efficacy table at ≥3000 µg/kg Q3W: PSA50 82% (14/17), PSA90 53%, ORR 45% (5/11), DCR ~64%, 0 DLTs.
- Step-up expansion dose **800 / 2000 / 3500 µg/kg Q3W** motivated by **blurred vision at 4000 µg/kg**.
- Astellas economics: $335M near-term; ≤$1.37B milestones; DevEx 40/60; US 50/50; runway into 2H 2028.
- Competitive framing vs **JANX007** (QW/Q2W, single-mask, mitigation protocols) and **Pluvicto** (logistics + salivary/marrow toxicity).
- Explicit expansion success / equivocal / kill bars (useful as working hypothesis, not gospel).

**Useful additions vs prior laptop brief:**
- Astellas $335M breakdown claim: **$240M cash + $75M equity @ ~50% premium + $20M near-term milestone** — **`[CONFIRMED]`** vs Feb 2026 8-K / IR (lock pack 2026-07-21). $20M is manufacturing tech-transfer MS anticipated **Q2/Q3 2027**, not immediate cash.
- Illustrative ASCO case studies (incl. post–Ac-225 patient with deep response) — anecdotal, not cohort stats.
- **Pasritamig** (J&J KLK2 TCE) added to competitive matrix — Ph3 **KLK2-comPAS** confirmed in lock pack.
- ECLIPSE 1/2/3 NCT IDs named (06903338 / 07128550 / 07142811).

**Conflicts / demote before promoting maturity (lock pack 2026-07-21):**
| Claim | Gemini | Prior / check | Status after lock |
|-------|--------|---------------|-------------------|
| Sanofi skim | “typically 3–8%”; exact % redacted | Prior brief **~20%** | **Still open** — Amunix §6.6 fully `[***]` redacted; 8-K says only “a portion” |
| Trial planned N | ~**215** | CT.gov ~**437** | **CT.gov wins** — API v2 est. **437** RECRUITING (2026-07-21) |
| Gr≥3 CRS | **0%** stated flatly | IR thin | **Partial** — **0** at ≥3000 Q3W (N=22); **1** low-dose event on N=58 → reject blanket 0% |
| Next expansion data | ESMO Q3 2026 **“Confirmed Window”** | Operator: **undated** | **Still undated** — no IR confirmation |
| ECLIPSE topline | Q1 2027 | Prior: primary completion Q4 2026 → topline soon after | Timing nuance OK if labeled |

**Source quality:** Primary IR / CT.gov / ASCO PDF / Janux IR are usable. Demote Reddit, Seeking Alpha narrative, GFCT blog for efficacy claims. Dossier tone is bullish; wiki keeps neutral synthesis on `@entities/tickers/vir.md`.

## Snippets

> VIR-5500 presents a highly investable profile on a 12-to-18-month horizon, provided the asset maintains a >50% PSA90 rate and <10% Grade 3+ CRS rate at the go-forward 3500 µg/kg Q3W expansion dose. [Source: VIR-5500 Equity Research Dossier.docx §1]

> These figures must be discarded. The clinical truth set … is derived from the finalized ASCO GU 2026 oral presentation, featuring a mature data cut of January 9, 2026, encompassing 58 heavily pretreated patients. [Source: VIR-5500 Equity Research Dossier.docx §2.2]

> At the 4000 µg/kg dose, two events of blurred vision were recorded … step-up dosing … 800 / 2000 / 3500 µg/kg Q3W. [Source: VIR-5500 Equity Research Dossier.docx §2.4]

> Near-Term Capital Injection: … $240 million in direct cash, a $75 million equity investment (priced favorably at a 50% premium …), and a near-term $20 million milestone. [Source: VIR-5500 Equity Research Dossier.docx §6.1] `[CONFIRMED]` vs 8-K/IR lock pack 2026-07-21
