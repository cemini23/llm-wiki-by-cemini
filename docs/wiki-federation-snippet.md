<!-- Canonical federation block — copy into each repo README; set **This wiki** row per repo. -->

## Cemini wiki federation

**Eight** interlinked markdown wikis plus the **Cemini Financial Suite** production trading stack (not a wiki). Page bodies cross-link with `@<alias>/path/to/page.md` (aliases in each repo's `CLAUDE.md`).

| Alias | Repository | Visibility | Focus |
|-------|------------|------------|--------|
| `osint-wiki` | `llm-wiki-by-cemini` *(private repository)* | **Private** | Financial / quant / prediction-market automation; librarian + CeminiSuite integration |
| `gambling-wiki` | [Gambling-wiki](https://github.com/cemini23/Gambling-wiki) | **Public** | Sports betting, casino, poker, DFS, best ball; PM/Kalshi retail strategy |
| `game-dev-wiki` | [Game-Dev-wiki](https://github.com/cemini23/Game-Dev-wiki) | **Public** | Hobby game dev — castle/RTS research, engine evals, agent-assisted slices |
| `ccc-wiki` | [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC) | **Public** | Cursor / Claude Code workflow, MCP, skills, multi-wiki eval prompts |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | Public | Image / video / voice generation, ComfyUI, persona ops |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Public | Local SEO, GBP, GEO/AEO, creator marketing |
| `3d-printing-wiki` | [3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) | Public | FDM/FFF, Bambu, slicers, print farms |
| `cybersecurity-wiki` | [Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki) | Public | Pentest, red team, SOC, certifications |
| *Cemini Financial Suite* | `Cemini-Financial-Suite` *(private — IP-sensitive trading stack)* | **Private** | Dockerized trading stack; consumes OSINT wiki via briefs |

**This wiki:** `REPLACE_ALIAS` — REPLACE_ONE_LINER.

**Privacy:** Only **`osint-wiki`** and **Cemini Financial Suite** are treated as private operational projects (sensitive research + production trading). **`ccc-wiki`** and the **six public domain wikis** (including `gambling-wiki`, `game-dev-wiki`) are **public** on GitHub. Cross-wiki `@osint-wiki/...` links resolve on maintainer machines only; public clones should not expect OSINT or prod secrets in-repo.

**Librarian:** `osint-wiki`, `ccc-wiki`, `gambling-wiki`, `game-dev-wiki`, and all public domain wikis sync via OSINT `scripts/sync_wiki_to_librarian.sh` → `cemini-librarian:/opt/cemini-wiki/<alias>/wiki/`.

**Eval prompt:** `@ccc-wiki/prompts/deep-research-multi-wiki-eval-v7-2026-06-13.md` — nine surfaces (includes `game-dev-wiki` as surface 9).
