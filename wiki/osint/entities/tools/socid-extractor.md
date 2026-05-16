---
title: "socid-extractor — cross-platform social-account identifier extraction"
type: entity
tags: [tool, osint, social-media-intelligence, entity-resolution, scraping, adopt, locally-installed, k49]
keywords: [socid-extractor, soxoj, stable-internal-identifiers, gaia-id, facebook-uid, instagram-pk, 130-platforms, http-only, no-headless-browser, entity-resolution, mit-license]
related:
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
  - entities/tools/fingerprint-suite.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
phase_0_verdict: ADOPT 2026-05-16 — MIT (per report); installed locally (laptop ~/tools + cemini-librarian) this ingest
---

## Relations

- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — evaluated in the v3-iteration eval (Adopt tier, OSINT primary fit)
- @entities/tools/fingerprint-suite.md — sibling OSINT-collection tooling; fingerprint-suite supplies stealth, socid-extractor supplies entity extraction
- @cybersecurity-wiki/concepts/osint-for-cybersecurity.md — cross-wiki: stable-identifier extraction enables threat-actor correlation across platform redesigns

## Raw Concept

Promoted from the 2026-05-16 "Tool Evaluation and Wiki Fit v3 Iteration" 46-repo eval. Tier: **Adopt**. Primary fit: OSINT-wiki. Cross-route: cybersecurity-wiki (OSINT-for-cybersecurity / threat-actor correlation). **Adopted locally** this ingest.

- URL: https://github.com/soxoj/socid-extractor
- License: **MIT** (per report)
- Stars / last commit / open issues: 975 / 2026-04-09 / 1
- Stack: Python

## Narrative

**socid-extractor** is a Python library that resolves a persistent OSINT friction point: **entity continuity across constantly-evolving social-media architectures**. It operates entirely via standard HTTP requests — no headless browser, no compute overhead — and parses structured data from **130+ platforms** into normalized ontologies (standardizing fields like `fullname`, `created_at`).

Its core innovation is extraction of **stable internal identifiers** — Google **GAIA IDs**, Facebook **UIDs**, Instagram **`pk`** values. These immutable IDs let analysts track a target continuously even when usernames change or a platform redesigns its frontend DOM. Output normalization means unstructured social intelligence can pipe directly into a database for cross-referencing.

**Cemini fit**: directly serves the OSINT-wiki / librarian kb-server workflow — pure-Python, no browser latency, ingests and normalizes public profile data programmatically. The stable-identifier extraction is the tracking primitive for threat-actor financial profiling (cross-routed to cybersec). MIT clears the IP sale.

**Adoption (2026-05-16)**: installed via `pip` on the laptop (`~/tools/`) and on cemini-librarian — a workspace/curation-side OSINT tool, consistent with the deployment boundary (curation tooling on laptop+librarian; financial tooling on cemini-prod).

- `[NEEDS VERIFICATION 2026-05-16]` Parser resilience against emerging anti-scraping defenses (e.g. Cloudflare Turnstile on TikTok).

## Snippets

> "The core innovation is its extraction of 'stable internal identifiers' — such as Google GAIA IDs, Facebook UIDs, and Instagram pk values ... These immutable identifiers allow OSINT analysts to track threat actors continuously, even when the target attempts to evade detection by altering usernames." [Source: Tool Evaluation and Wiki Fit Analysis.docx — URL 10]
