---
title: Computational genealogy — archival ladder + IDE automation
type: concept
tags: [genealogy, archival, automation, italy, antenati, draft]
keywords: [stato civile, parish, Trent 1563, notarial, IIIF, HTR, GEDCOM, Double Metaphone, kinship graph]
related:
  - sources/eval-github-repo-revenue-evaluation-2026-07-15.md
  - entities/tools/espanso.md
  - sources/arxiv-2607.09324-letting-data-speak-keyword-extraction-crowdsourced-2026-07-15.md
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
  - sources/gemini-italian-ancestry-deep-research-2026-07-09.md
  - sources/gemini-sellia-calabria-archive-routing-2026-07-11.md
  - sources/gemini-abruzzo-diaspora-genealogy-2026-07-12.md
  - sources/eval-multi-wiki-link-evaluation-genealogy-agent-2026-07-10.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - entities/tools/gcerretani-antenati.md
  - entities/tools/transkribus.md
  - entities/tools/familysearch-platform-api.md
  - entities/tools/nati-in-trentino.md
  - entities/tools/autoresearch-genealogy.md
  - entities/tools/topola-viewer.md
  - entities/tools/liberu-genealogy-laravel.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/active-project-research-routing.md
  - "@ccc-wiki/concepts/deep-research-evaluation-prompt.md"
maturity: draft
created: 2026-07-09
updated: 2026-07-15
---

## Relations

- @sources/gemini-automated-deep-genealogy-research-2026-07-09.md — primary synthesis source (Gemini roadmap docx)
- @sources/gemini-italian-ancestry-deep-research-2026-07-09.md — K154 regional archive playbook companion
- @sources/gemini-abruzzo-diaspora-genealogy-2026-07-12.md — K160 Abruzzo diaspora offline pivot
- @concepts/italian-regional-genealogy-archive-playbook.md — Abruzzo/Calabria/Trentino contacts + red flags
- @entities/tools/gcerretani-antenati.md — Antenati IIIF downloader
- @entities/tools/transkribus.md — handwriting recognition for Latin/cursive acts
- @entities/tools/familysearch-platform-api.md — catalog/tree API alternative to UI scrape
- @entities/tools/nati-in-trentino.md — Trentino baptism index before parish travel
- @entities/tools/autoresearch-genealogy.md — K157 Claude Code vault + archival agent prompts (Integrate)
- @entities/tools/topola-viewer.md — K157 static GEDCOM fan/hourglass charts (Extract)
- @entities/tools/liberu-genealogy-laravel.md — K157 php-dna triangulation extract (optional)
- @sources/eval-multi-wiki-link-evaluation-genealogy-agent-2026-07-10.md — K157 eval batch
- @concepts/cemini-wiki-ingest-workflow.md — parallel “don’t invent Tier-3 autonomy” discipline for personal archives
- @concepts/active-project-research-routing.md — K156 co-primary family-tree routing

## Raw Concept

How to structure a **software-assisted** deep genealogy project (target ~1500s–present Europe, Italy as the worked example) without confusing methodology with unverified pedigree claims.

## Narrative

### Three archival eras (Italy-centric)

| Horizon | Primary sources | Custodian | Schema |
|---------|-----------------|-----------|--------|
| ~1809–present | *Stato civile* (birth/marriage/death) | Comune / Archivio di Stato; Portale Antenati | Structured forms; grandparents often on full acts |
| ~1563–1809 | Parish baptisms, marriages, burials | Local *parrocchia* / diocese | Semi-structured Latin narrative; godparents/witnesses as soft kinship |
| Pre-~1563 / gaps | *Atti notarili*, tax rolls (*catasto* / *onciario*), feudal | State / district archives | Legal prose; generational IDs when property parties named |

Council of Trent (~1545–1563) mandated systematic baptism/marriage registers — the usual European “paper trail” start for Catholic areas. Before that, expect sparse vitals and heavier notarial/tax reliance. Reformation-era migration can break geographic continuity (*cuius regio, eius religio*).

Realistic depth: **civil alone** often reaches early 1800s; **parish** can push mid–late 1500s *if* registers survive; **continuous 500 years** is project-dependent, not guaranteed.

### IDE stack (from roadmap — adopt selectively)

1. **Truth layer first** — official *copia integrale* / imaged civil acts for Gen N before automation.
2. **FamilySearch Platform API** — person/parents/matches/places over UI scrapes.
3. **GEDCOM 5.5.1 / 7** — interchange; Gramps or similar as human UI.
4. **Kinship store** — SQLite + recursive CTEs (lightweight) or Neo4j Person/Union graph (heavier).
5. **IIIF pull** — download Antenati (and other IIIF) registries for offline review (`gcerretani/antenati`).
6. **HTR** — Transkribus models or multimodal LLM on page images (ceremonial Latin abbreviations).
7. **Entity resolution** — Double Metaphone (+ edit distance) for Latinization / dialect spelling drift.
8. **Reverse genealogy** — collateral godparent/witness graphs when the direct line vanishes.
9. **Agent research loops (K157)** — `mattprusak/autoresearch-genealogy` vault templates for timeline-gap runs; human-verify every imported fact before GEDCOM merge.
10. **Visualization (K157)** — `PeWu/topola-viewer` on exported GEDCOM for fan/hourglass dead-end discovery (static, no server DB).

### Cemini operating rules

- Treat Gemini/LLM roadmaps as **hypotheses + tool pointers**, not licenses or Phase-0 GO.
- Prefer official API / IIIF endpoints over Terms-of-Service-violating scrapes. [TENTATIVE] always re-check Antenati/FS ToS before bulk download.
- Personal pedigrees and DNA stay **out of this wiki** (laptop private folders only).
- Do not build Neo4j/HTR pipelines before Gen3 dates and Gen4 names exist for the towns under study.

## Snippets

> Era ladder: stato civile → parish (post-Trent) → notarial/tax for brick walls. [Source: @sources/gemini-automated-deep-genealogy-research-2026-07-09.md]

> Prefer Double Metaphone primary+secondary hashes over pure Levenshtein for cross-century Italian/Latin name drift. [Source: @sources/gemini-automated-deep-genealogy-research-2026-07-09.md]
