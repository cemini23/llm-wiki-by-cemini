---
title: "Wu Blockchain — Coldcard RNG vulnerability (2026-08-05)"
type: source
tags: [crypto, coldcard, cyber, k223]
keywords: [Coinkite, Galaxy Research, Mk3, firmware 4.0.1-4.1.9]
related:
  - sources/substack-rss-wublock-2026-08-04-july-blockchain-tech.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
read_status: read
---

## Relations

- @sources/substack-rss-wublock-2026-08-04-july-blockchain-tech.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Coldcard's Five-Year Vulnerability: RNG Failure, Four Suspected Attack Waves |
| URL | https://wublock.substack.com/p/coldcards-five-year-vulnerability |
| sha256 | `be81d0662dc901fff5e952554d435f26f8f2748b83f78c102f9b1d3e7078555c` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-wublock-2026-08-05-coldcards-five-year-vulnerability-rng-failure-fo.md` |
| read_status | read |

## Narrative

2021 firmware path used software PRNG instead of hardware RNG for some Coldcard seeds (Mk2/Mk3 fw 4.0.1–4.1.9). Galaxy: four suspected sweep waves; combined on-chain pattern totals ~1,816 BTC / 5,294 addrs — **not** individually verified victims. Firmware update does **not** fix old seeds — generate new + move funds. AI-found-the-bug claims unverified. **cybersec brief + wiki** — not GuruWatcher arms; not HL concentration.
