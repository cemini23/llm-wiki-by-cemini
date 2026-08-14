---
title: "CyberScraper-2077 — AI-powered web scraper (anti-bot, LLM extraction)"
type: entity
tags: [tool, scraper, osint, cyber, playwright, k237]
keywords: [CyberScraper-2077, Playwright, stealth, Tor, captcha, LLM extraction, Streamlit, Patchright]
related:
  - sources/eval-url-revenue-opportunity-2026-08-14.md
  - concepts/self-evolving-runtime-defense.md
  - entities/tools/rustscan.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14

---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-14.md — K237 eval batch (**Integrate**, cyber lab)
- @concepts/self-evolving-runtime-defense.md — cyber lab harness guardrails context

## Raw Concept

What prompted this page: K237 eval tiers CyberScraper-2077 as the batch's only **Integrate** (docx routed it to GuruWatcher paywall scraping; re-routed to the **cyber / local-abliterated lab** per operator priority — no GuruWatcher brief because it's a scraping tool, not a price-watch source). Verified via gh api: **MIT**, 0.4MB → cloned to `.local/adopts/CyberScraper-2077` (1MB on disk).

## Narrative

AI-powered web scraper (Python 3.10+, Streamlit GUI) using OpenAI / Gemini / Ollama for structured LLM extraction into JSON/CSV/HTML/SQL/Excel. Key mechanisms (verified in cloned source):

- **Current-browser stealth**: attaches to a local Chrome instance via **CDP (`connect_over_cdp` on localhost:9222)** using Patchright (stealth Playwright fork) — the "bypass 99% of bot detection" claim; requires an active browser session.
- **Tor routing** for .onion scraping; captcha-bypass parameter; multi-page navigation (BETA); LRU content + query caching; Google Sheets upload.
- Anti-bot resilience via local browser instance hijacking; **needs headless fallback for unattended cron runs**.

### Decision

**GO Integrate (cyber lab, authorized research only)** — MIT, tiny footprint. Constraints:
- Authorized-target-only (local lab evaluations, whitehat perimeter audits, newsletter/substack polling the operator already has rights to).
- **Headless fallback required** for unattended runs (README documents active-session requirement for stealth mode).
- Playwright memory-leak watch during multi-hour polling loops (`[NEEDS VERIFICATION 2026-08-14]`).

Phase-1 wire appended (cyber-lab scraping guardrails). **No GuruWatcher prod brief** this batch (no price-watch content).
