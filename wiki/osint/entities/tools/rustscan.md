---
title: "RustScan — fast port scanner (cyber recon, GPL-3.0)"
type: entity
tags: [tool, port-scan, recon, cyber, rust, k237]
keywords: [RustScan, port scanning, Nmap, scripting engine, GPL-3.0, recon]
related:
  - sources/eval-url-revenue-opportunity-2026-08-14.md
  - entities/tools/cyberscraper-2077.md
maturity: draft
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-14.md — K237 eval batch (Extract, cyber lab)
- @entities/tools/cyberscraper-2077.md — cyber-lab toolbelt sibling

## Raw Concept

What prompted this page: K237 eval tiers RustScan as **Extract** for the local abliterated / operator cyber lab (sub-2s recon). **License override: docx claimed MIT, gh api says GPL-3.0** — flagged on the eval source page. 14.5MB → cloned as reference to `.local/adopts/RustScan` (7MB).

## Narrative

The Modern Port Scanner: **all 65k ports in ~3 seconds** (async Rust), scripting engine (Python/Lua/Shell), adaptive-learning basic-math tuning, auto-pipes discovered open ports directly into targeted Nmap scans.

### Steal-for-cyber-lab (GPL-3.0 — pattern only)

- **Fast async port discovery → Nmap piping** cuts initial host recon from minutes to <3s, feeding automated whitehat perimeter audits.
- **Scripting engine** for post-scan automation.
- **Batch-size discipline required**: aggressive 3,000 ports/sec default can trigger firewall rate-limiting / service degradation on sensitive lab targets — enforce `-b 10 -T 5000` on sensitive hosts.
- **GPL-3.0** (not MIT as docx claimed): pattern extraction only; no linking into proprietary code. Install as standalone binary (`brew install rustscan` / `cargo install rustscan`).

Tier: `[TENTATIVE]`.
