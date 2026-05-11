---
title: "METATRON — AI Reconnaissance CLI"
type: entity
tags: [tool, recon, ollama, duckduckgo-scraper, steal-from, k38]
keywords: [metatron, recon, steal-from, three-surface-eval]
related:
  - sources/link-evaluation-brief-trading-stack.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@sources/link-evaluation-brief-trading-stack.md` — source evaluation brief (URL 23)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL**: `github.com/sooryathejas/METATRON`
- **Tier (per source brief)**: **Steal-from**
- **License**: [NEEDS VERIFICATION 2026-05-11] License needs verification — narrow scraper lift only.

## Narrative

AI-powered Python CLI reconnaissance tool. Orchestration loop: locally-running fine-tuned Ollama model (metatron-qwen / Qwen 3.5) → nmap, nikto, whatweb. MariaDB scan-history backend. DuckDuckGo scraper for CVE enrichment (no API key required).

### Integration vector

Steal-from: port the **`search.py` DuckDuckGo scraper** to Cemini's ingest layer for free real-time web context (alternative to expensive commercial search APIs). Discard everything else (local LLM + MariaDB = monolithic, too heavy for Cemini).

### Risks

Heavy local LLM + dedicated MariaDB = unfit full deployment. Scraper-only lift keeps risk minimal.

[Source: Link Evaluation Brief Trading Stack.docx, URL 23]
