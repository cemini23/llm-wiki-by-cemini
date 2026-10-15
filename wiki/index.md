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
updated: 2026-10-14
---

# Federation wiki — catalog index

Read this file first, then the domain's own catalog. Each domain catalog is hand-curated and
updated on ingest; this page is only a map of them.

The eight domains merged into this one repository on **2026-10-14**, so the entity vocabulary of
the old sibling wikis applies unchanged: a page lives at `wiki/<domain>/<category>/<slug>.md`,
and `@<alias>/<path>` resolves to `wiki/<domain>/<path>`.

| Domain | Alias | Pages | Sources | Entities | Concepts | Sweeps | Catalog |
|---|---|---|---|---|---|---|---|
| osint | `osint-wiki` | 3,998 | 1,989 | 1,072 | 719 | 145 | [catalog](osint/index.md) |
| ccc | `ccc-wiki` | 1,419 | 475 | 282 | 437 | 132 | [catalog](ccc/index.md) |
| cybersec | `cybersecurity-wiki` | 1,366 | 694 | 185 | 348 | 136 | [catalog](cybersec/index.md) |
| image-gen | `image-gen-wiki` | 1,234 | 605 | 310 | 171 | 139 | [catalog](image-gen/index.md) |
| gambling | `gambling-wiki` | 596 | 311 | 57 | 81 | 138 | [catalog](gambling/index.md) |
| seo | `seo-wiki` | 494 | 203 | 68 | 85 | 135 | [catalog](seo/index.md) |
| game-dev | `game-dev-wiki` | 425 | 207 | 34 | 54 | 125 | [catalog](game-dev/index.md) |
| 3d-printing | `3d-printing-wiki` | 288 | 97 | 23 | 28 | 137 | [catalog](3d-printing/index.md) |

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
