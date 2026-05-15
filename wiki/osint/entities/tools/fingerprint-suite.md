---
title: "fingerprint-suite — browser fingerprint generation + injection"
type: entity
tags: [tool, scraping, browser-fingerprint, anti-bot, opsec, playwright, puppeteer, adopt]
keywords: [fingerprint-suite, apify, header-generator, fingerprint-generator, fingerprint-injector, bayesian-network, bot-detection, apache-2.0, adopt]
related:
  - sources/tool-evaluation-wiki-fit-2026-05-15.md
  - entities/tools/obscura-headless-browser.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
phase_0_verdict: ADOPT 2026-05-15 (Apache-2.0 verified, locally installed)
---

## Relations

- @sources/tool-evaluation-wiki-fit-2026-05-15.md — evaluated in the 52-URL eval (Adopt tier, OSINT primary fit)
- @entities/tools/obscura-headless-browser.md — sibling OSINT-collection tooling (headless browsing); fingerprint-suite supplies the stealth layer

## Raw Concept

Promoted from the 2026-05-15 "Tool Evaluation and Wiki Fit" 52-URL eval. Tier: **Adopt**. Primary fit: OSINT-wiki. Cross-route: Cybersec wiki (red-team evasion).

- URL: https://github.com/apify/fingerprint-suite
- License: **Apache-2.0** — verified via GitHub API 2026-05-15 (matches report)
- Stars: 2,214 | Last push: 2026-05-11 | Open issues: 12 | Stack: TypeScript

## Narrative

A modular TypeScript toolkit (Apify) that generates and injects realistic browser fingerprints so automated collection bypasses bot-detection. The monorepo splits cleanly into composable packages:

- **`header-generator`** — realistic HTTP header sets
- **`fingerprint-generator`** — full browser fingerprints (screen, navigator, WebGL, fonts) via a Bayesian generative network trained on real-world data
- **`fingerprint-injector`** — applies a generated fingerprint into a Playwright / Puppeteer browser context
- **`generative-bayesian-network`** — the underlying model

**OSINT relevance**: maintains operational security during web collection — threat-actor profiling, infrastructure tracking, and financial-source scraping all benefit from not presenting an obviously-automated fingerprint and tripping CAPTCHAs or behavioral blocks. It is the stealth layer beneath a headless-browser collection pipeline, not a scraper itself.

**Scope discipline**: this is a legitimate anti-detection tool for authorized OSINT collection. It is not, and should not be used as, a tool for evading detection in any unauthorized context.

## Local adoption (2026-05-15)

Installed laptop-side to `~/tools/fingerprint-suite/` as npm packages (it is a library, not a CLI). Status: **working**.

- Packages: `fingerprint-generator`, `fingerprint-injector`, `header-generator` — all at v2.1.82
- 21 packages added, `npm audit`: 0 vulnerabilities
- Node v24.13.0 / npm 11.14.0
- Smoke test passed: generated a Chrome/macOS fingerprint (userAgent + 1920x1080 screen + 13 HTTP headers)

License re-verified at adoption: Apache-2.0 (GitHub API). No IP-sale concern.

## Snippets

```bash
# Install (2026-05-15)
mkdir -p ~/tools/fingerprint-suite && cd ~/tools/fingerprint-suite
npm install fingerprint-generator fingerprint-injector header-generator

# Smoke test
node -e "
const { FingerprintGenerator } = require('fingerprint-generator');
const gen = new FingerprintGenerator();
const fp = gen.getFingerprint({ browsers:['chrome'], operatingSystems:['macos'] });
console.log(fp.fingerprint.navigator.userAgent, fp.fingerprint.screen);
"
# → Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ... { width: 1920, height: 1080 }
```

Usage pattern: pair `fingerprint-injector` with a Playwright/Puppeteer browser context to apply a generated fingerprint before navigation.

