---
title: "Jev Trading Research Paper — One-Person HFT on System One (TypeSafe field report)"
type: source
tags: [source, k268, jev, typesafe, hft, image-ocr]
keywords: [k268, Jev, System One, RLCD, AgenKit, market making]
related:
  - sources/newsletter-rss-latent-space-2026-09-21-jev-diogo-2026-09-22.md
  - concepts/k269-jev-system-one-wave.md
  - concepts/k268-harness-evolution-wave.md
  - concepts/k268-jev-trading-wave.md
  - entities/tools/jev-mcp.md
  - entities/tools/jev-trader.md
maturity: draft
created: 2026-09-21
updated: 2026-09-22
read_status: read
---

## Relations

- @sources/newsletter-rss-latent-space-2026-09-21-jev-diogo-2026-09-22.md
- @concepts/k269-jev-system-one-wave.md
- @concepts/k268-harness-evolution-wave.md
- @concepts/k268-jev-trading-wave.md
- @entities/tools/jev-mcp.md
- @entities/tools/jev-trader.md

## Raw Concept

| File | `Jev Trading Research Paper.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Jev Trading Research Paper.pdf` |
| Local OCR | `.local/ocr/jev-trading-research-paper.txt` (8 pages, vision OCR 2026-09-21) |
| Retrieved | 2026-09-21 |
| Dual-ID | **OSINT K268** |
| Pages | 8 (image-only PDF; no text layer) |

## Narrative

8-page TypeSafe **field report** (not peer-reviewed arXiv): *How to Build a One-Person HFT Hedge Fund on Jev…* Describes splitting trading into **deterministic code** (state engine, Avellaneda–Stoikov quotes, hard risk vetoes) and **Jev System One** probabilistic judgments (Noull / Choice / Score battery, RLCD-calibrated confidence, fractional Kelly sizing). Claims **70–500 ms** latency and **$0.042/M input tokens**; cites TypeSafe release **2026-09-15** and **AgenKit** (`agenkit.xyz`) build harness.

**Cemini posture — FILE only:** This is vendor architecture marketing + reference design, **not** a Cemini live trading path. **0 product Integrate GO.** Never auto-arm. Never `npx github:`. Laptop **`jev-mcp`** WIRE unchanged. **GW:** claim-check / HITL ledger analog only. **Not Atto HTR** — Transkribus remains sole product HTR. Reference to **jev-trader** (Monad MM) is a named live-trading demo — out of scope.

Claim hygiene: latency/cost figures are **TypeSafe vendor claims** `[TENTATIVE]` until independently measured. OCR via vision pass — verify formulas against PDF if citing in briefs.

## Snippets

> "Jev returns calibrated probabilities in 70 to 500 milliseconds at a cost of $0.042 per million input tokens." [Source: Jev Trading Research Paper.pdf p.1] `[TENTATIVE]` vendor claim

> "Under RLCD, events the model tags at eighty percent occur, in aggregate, approximately eighty percent of the time." [Source: Jev Trading Research Paper.pdf p.2] `[TENTATIVE]`

> "Jev does not replace market-data infrastructure, exchange connectivity, or deterministic risk engines." [Source: Jev Trading Research Paper.pdf p.8]
