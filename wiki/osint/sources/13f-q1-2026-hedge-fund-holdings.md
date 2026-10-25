---
title: "13F Hedge-Fund Holdings — Q1 2026 (filed May 2026)"
type: source
tags: [source, 13f, hedge-funds, holdings, smart-money, sec-filings, equity-positioning, k48]
keywords: [13f-hr, q1-2026-13f, hedge-fund-holdings, berkshire, pershing-square, gates-foundation, tiger-global, greenlight, tci, appaloosa, fairfax, baupost, smart-money-positioning]
related:
  - concepts/q1-2026-13f-smart-money-positioning.md
  - entities/companies/berkshire-hathaway.md
  - entities/companies/pershing-square.md
  - entities/companies/gates-foundation-trust.md
  - entities/companies/tiger-global-management.md
  - entities/companies/greenlight-capital.md
  - entities/companies/tci-fund-management.md
  - entities/companies/appaloosa-management.md
  - entities/companies/fairfax-financial.md
  - entities/companies/baupost-group.md
maturity: validated
read_status: deep-read
created: 2026-05-15
updated: 2026-05-15
clusters: [13f, smart-money]
---

## Relations

- @concepts/q1-2026-13f-smart-money-positioning.md — cross-fund synthesis built from this source
- @entities/companies/berkshire-hathaway.md — Warren Buffett
- @entities/companies/pershing-square.md — Bill Ackman
- @entities/companies/gates-foundation-trust.md — Bill & Melinda Gates Foundation Trust
- @entities/companies/tiger-global-management.md — Chase Coleman
- @entities/companies/greenlight-capital.md — David Einhorn
- @entities/companies/tci-fund-management.md — Chris Hohn
- @entities/companies/appaloosa-management.md — David Tepper
- @entities/companies/fairfax-financial.md — Prem Watsa
- @entities/companies/baupost-group.md — Seth Klarman

## Raw Concept

- **Type**: SEC Form 13F-HR holdings, captured as screenshots from a 13F-tracking site (History / Stock / % of Portfolio / Recent Activity layout — the dataroma.com presentation).
- **Reporting period**: quarter ended **2026-03-31** (Q1 2026).
- **Filed**: by the SEC 13F deadline, **~2026-05-15** (45 days after quarter-end).
- **Retrieved**: 2026-05-15.
- **Files**: 11 `.jpeg` screenshots provided; **9 distinct funds** usable (see below).
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/` (9 images: `buffet holdings.jpeg`, `ackaman holdings.jpeg`, `bill gates holdings.jpeg`, `chase coleman holdings.jpeg`, `einhorn holdings.jpeg`, `hohn holdings.jpeg`, `tepper holdings.jpeg`, `watsa holdings.jpeg`, `loeb holdings.jpeg`).

### Coverage and known gaps

| Fund | Manager | Source file |
|------|---------|-------------|
| Berkshire Hathaway | Warren Buffett | `buffet holdings.jpeg` |
| Pershing Square | Bill Ackman | `ackaman holdings.jpeg` |
| Gates Foundation Trust | (Bill Gates) | `bill gates holdings.jpeg` |
| Tiger Global Management | Chase Coleman | `chase coleman holdings.jpeg` |
| Greenlight Capital | David Einhorn | `einhorn holdings.jpeg` |
| TCI Fund Management | Chris Hohn | `hohn holdings.jpeg` |
| Appaloosa Management | David Tepper | `tepper holdings.jpeg` |
| Fairfax Financial | Prem Watsa | `watsa holdings.jpeg` |
| Baupost Group | Seth Klarman | `loeb holdings.jpeg` (see note) |

- **`loeb holdings.jpeg` is mislabeled** — it shows the **Baupost Group (Klarman)** portfolio, identical to `klarman holdings.jpeg` (which is a cropped copy with the Recent Activity column missing). There is **no Third Point / Daniel Loeb data** in this upload. [OPEN QUESTION 2026-05-15] — a real Third Point 13F was not supplied.
- **`tepper 2.jpeg` not ingested** — a distinct portfolio (AMZN 19%, TDS 13%, CRH, Carpenter Technology, MasTec, APi Group; near-universal position reductions; SPAC warrants) that does **not** match Appaloosa's book. Manager unidentified; left in the inbox pending confirmation (user decision 2026-05-15).

## Narrative

Form 13F-HR is the quarterly SEC filing every institutional manager with >$100M in 13(f)-eligible securities must submit within 45 days of quarter-end. It is the standard "smart money" window — but a **lagged and partial** one:

- **As-of 2026-03-31, disclosed ~2026-05-15** — positions are six weeks stale at publication.
- **Long US-listed equity only** — no short positions, cash, bonds, commodities, non-US-listed equity, or most derivatives. A 13F is not a full picture of a fund's risk.
- **"% of Portfolio"** here is the percentage of the *13F-reported* book, not of total fund AUM.
- **"Recent Activity"** ("Add x%", "Reduce x%", "Buy") is the quarter-over-quarter change in share count for that position.

Per-fund holdings tables and notable moves live on the nine `entities/companies/` pages. Cross-fund patterns — shared convictions, contested names, the Q1 2026 Alphabet story — are synthesized in `@concepts/q1-2026-13f-smart-money-positioning.md`.

### Headline observations

- **Alphabet was the quarter's most-contested name.** Buffett's Berkshire opened/expanded GOOGL by **+204%** to a 5.9% position; Tiger Global holds GOOGL as its **single largest** position (13.4%); TCI added GOOG. Against that, Pershing Square cut both GOOG and GOOGL ~95% and TCI's MSFT was cut 84% — share-class consolidation and rotation muddy the simple read.
- **Microsoft split the room** — Ackman initiated MSFT (new Buy, 15% position); Tiger Global cut it 54%; TCI cut it 84%; Appaloosa cut it 82%.
- **Amazon is the broadest consensus long** — a top-3 position for Pershing Square, Appaloosa, and Baupost, and a top-10 for Tiger Global; Baupost added +47%, Appaloosa +98%.
- **Restaurant Brands (QSR)** appears as a ~12% position in *both* Pershing Square and Baupost.

## Snippets

Per-fund verbatim holdings tables are reproduced on each fund's entity page (`## Snippets`). Source images are the canonical record. [Sources: buffet holdings.jpeg, ackaman holdings.jpeg, bill gates holdings.jpeg, chase coleman holdings.jpeg, einhorn holdings.jpeg, hohn holdings.jpeg, tepper holdings.jpeg, watsa holdings.jpeg, loeb holdings.jpeg]

## Dead Ends

- **Third Point / Daniel Loeb** — intended for this batch but the supplied `loeb holdings.jpeg` was a duplicate of the Baupost portfolio. No Third Point page created; gap noted for a future upload.
- **`tepper 2.jpeg`** — unidentified manager; not ingested. If identified later, it is a clean stand-alone add.
