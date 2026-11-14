---
title: Federation wiki — catalog index
type: concept
related:
  - osint/index.md
  - ccc/index.md
  - cybersec/index.md
  - seo/index.md
  - image-gen/index.md
  - gambling/index.md
  - game-dev/index.md
  - 3d-printing/index.md
updated: 2026-11-14
---

# Federation wiki — catalog index

Read this file first, then the domain's own catalog. Each domain catalog is hand-curated and
updated on ingest; this page is only a map of them.

The eight domains merged into this one repository on **2026-10-14**, so the entity vocabulary of
the old sibling wikis applies unchanged: a page lives at `wiki/<domain>/<category>/<slug>.md`,
and `@<alias>/<path>` resolves to `wiki/<domain>/<path>`.

| Domain | Alias | Pages | Sources | Entities | Concepts | Sweeps | Catalog |
|---|---|---|---|---|---|---|---|
| osint | `osint-wiki` | 4,228 | 2,126 | 1,103 | 749 | 176 | [catalog](osint/index.md) |
| ccc | `ccc-wiki` | 1,655 | 618 | 313 | 469 | 162 | [catalog](ccc/index.md) |
| cybersec | `cybersecurity-wiki` | 1,475 | 748 | 192 | 365 | 167 | [catalog](cybersec/index.md) |
| image-gen | `image-gen-wiki` | 1,318 | 643 | 311 | 187 | 167 | [catalog](image-gen/index.md) |
| gambling | `gambling-wiki` | 647 | 328 | 57 | 84 | 169 | [catalog](gambling/index.md) |
| seo | `seo-wiki` | 567 | 239 | 68 | 91 | 166 | [catalog](seo/index.md) |
| game-dev | `game-dev-wiki` | 472 | 216 | 37 | 58 | 156 | [catalog](game-dev/index.md) |
| 3d-printing | `3d-printing-wiki` | 349 | 121 | 24 | 35 | 166 | [catalog](3d-printing/index.md) |

## Which domain holds what

- **osint** — financial research, quant finance, prediction markets, CeminiSuite, RL for trading.
- **cybersec** — offensive security (pentest / red team / bug bounty / exploit dev), defensive operations (SOC / IR / threat hunting), careers, threat actors. Shares OSINT tradecraft with osint.
- **ccc** — Cursor + Claude Code meta-work: workflow, subagents, MCP, hooks, skills, slash commands.
- **image-gen** — uncensored image generation, model cataloging, ComfyUI, LoRA, persona ops.
- **seo** — local SEO, GBP optimization, GEO/AEO, web design, social media, creator marketing.
- **gambling** — sports betting, casino, poker, DFS, prediction-market wagering (retail/strategy). osint keeps the bots.
- **game-dev** — hobby game dev: castle/RTS research, engine evals, agent-assisted slices.
- **3d-printing** — FDM/FFF printing, Bambu, materials, slicers, print farms, store ops.

## Notes

- A page that resolves to **no** domain catalog is either new since the last catalog update or a stub.
- `wiki/osint/index.md` is the largest catalog at 4,694 lines; it absorbed the pre-merge OSINT catalog.
- Cross-domain pages are not duplicated. A topic is reconciled into one domain and linked with `@<alias>/…`.
- The seven absorbed repositories are archived, not deleted — they are the rollback. See
  `briefs/2026-10-14_federation-wiki-merge-plan.md` §5.7.
