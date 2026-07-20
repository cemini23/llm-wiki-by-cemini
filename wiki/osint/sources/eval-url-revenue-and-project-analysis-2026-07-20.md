---
title: URL Revenue and Project Analysis.docx (20 URLs, 2026-07-20)
type: source
tags: [tool-evaluation, revenue, k175, docx, genealogy, journalism]
keywords: [tint, CodiceFiscaleJS, censusreporter, babynames, fivethirtyeight, beeswithmachineguns, Italian NLP, jure sanguinis]
related:
  - entities/tools/dhfbk-tint.md
  - entities/tools/codice-fiscale-js.md
  - entities/tools/censusreporter.md
  - entities/tools/timemagazine-babynames.md
  - entities/tools/fivethirtyeight-data.md
  - entities/tools/beeswithmachineguns.md
  - entities/tools/aztec-experiments.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/active-project-research-routing.md
maturity: draft
read_status: read
created: 2026-07-20
updated: 2026-07-20
clusters: [wiki-tooling, k175-ingest]
---

## Relations

- @entities/tools/dhfbk-tint.md — **Integrate** (family-tree Italian NLP; GPL-3.0 — Phase-0 before install)
- @entities/tools/codice-fiscale-js.md — **Extract** (comuni / soppressi matrix for regional playbook)
- @entities/tools/censusreporter.md — **Extract** (US census staging schemas)
- @entities/tools/timemagazine-babynames.md — **Extract** (SSA name-frequency priors for entity resolution)
- @entities/tools/fivethirtyeight-data.md — **Extract** (CeminiDFS + PM canary baselines)
- @entities/tools/beeswithmachineguns.md — **Watch** (pm-canary load test; aging AWS swarm)
- @entities/tools/aztec-experiments.md — **Watch** (PM on-chain privacy theory; no license SPDX)
- @concepts/computational-genealogy-archival-automation.md — K175 stack delta
- @concepts/italian-regional-genealogy-archive-playbook.md — CodiceFiscaleJS + Italian civic indexes
- @concepts/wiki-tooling-evaluation.md — revenue-eval batch
- @concepts/active-project-research-routing.md — family-tree + CeminiDFS routing

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | URL Revenue and Project Analysis |
| **Theme** | Journalistic data pipelines, Italian entity resolution, political context, network testing |
| **URLs** | 20 |
| **sha256** | `746c309cc4e947ca0deb2b552308079bcfe59429a49192001982633dd87e9cc4` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/URL Revenue and Project Analysis.docx` |
| **License report** | `.local/reports/license-spot-check-2026-07-20-0802.txt` |
| **Phase-0** | **Complete 2026-07-20** — `.local/reports/k175-phase0-2026-07-20.md` via `scripts/adopt_k175_phase0.sh` |
| **Distinct from** | K174 repository-revenue batch; K173 PostHog/ui-skills batch |

## Narrative

Gemini v10 revenue-first eval (Priority #1: XSP + TipDrop + family-tree + PM canary). Strong **genealogy** cluster this batch — Italian NLP + fiscal-code geo matrix + US census staging + SSA babynames — plus one CeminiDFS extract and two pm-canary Watch items.

| Tier | Items |
|------|-------|
| **Integrate (1)** | `dhfbk/tint` — Italian Stanford-CoreNLP pipeline (GPL-3.0; Java/RAM Phase-0) |
| **Extract (4)** | `fivethirtyeight/data` (CC-BY-4.0 → CeminiDFS); `censusreporter/censusreporter` (MIT); `TimeMagazineLabs/babynames` (MIT); `lucavandro/CodiceFiscaleJS` (CC-BY-SA-4.0 — sharealike if redistributed) |
| **Watch (2)** | `newsapps/beeswithmachineguns` (MIT); `vbuterin/aztec_experiments` (no SPDX) |
| **Context (7)** | datadesk/notebooks, propublica/guides, WTFJHT, awesome-italia-opensource, awesome-italian-public-datasets, openpolis/open_municipio (AGPL — wiki-only), anirudhology tokenization blog → CCC brief |
| **Pass (6)** | voxmedia/meme, nprapps/app-template, guardian/frontend, dukechronicle/chronline, BloombergGraphics/whatiscode, times/cardkit |

### License spot-check overrides (2026-07-20 `gh api`)

| Repo | Eval claim | SPDX confirmed |
|------|------------|----------------|
| fivethirtyeight/data | CC-BY-4.0 | CC-BY-4.0 |
| censusreporter/censusreporter | (implied OSS) | MIT |
| TimeMagazineLabs/babynames | (implied) | MIT |
| lucavandro/CodiceFiscaleJS | CC-BY-SA-4.0 | CC-BY-SA-4.0 |
| dhfbk/tint | GPL-3.0 | GPL-3.0 |
| newsapps/beeswithmachineguns | MIT (via Paramiko) | MIT |
| openpolis/open_municipio | NOT FOUND | **AGPL-3.0** — Context only; no product redistribute |
| vbuterin/aztec_experiments | NOT FOUND | null |
| guardian/frontend | Open Source | NOASSERTION |

**GPUOLOGY / family-tree product note:** CodiceFiscaleJS CC-BY-SA and Tint GPL-3.0 are fine for **private** research; shipping either inside a commercial kit requires license counsel / reimplementation of the geo matrix. Prefer *patterns* extract over vendoring into SaaS.

### Phase-0 complete (2026-07-20)

Shallow clones to `/tmp/k175-*-audit` only; no Desktop/family install; no npm/pip/brew from README (K173). Report: `.local/reports/k175-phase0-2026-07-20.md`.

| Repo | Verdict | Clone / size |
|------|---------|--------------|
| dhfbk/tint | **CONDITIONAL-GO** — private family only | `/tmp/k175-tint-audit` · 221 MB |
| lucavandro/CodiceFiscaleJS | **GO (extract)** | `/tmp/k175-codice-fiscale-js-audit` · 5 MB |
| censusreporter/censusreporter | **GO (extract)** | `/tmp/k175-censusreporter-audit` · 111 MB |
| TimeMagazineLabs/babynames | **GO (extract)** | `/tmp/k175-babynames-audit` · 169 MB |
| fivethirtyeight/data | **GO (extract)** | `/tmp/k175-fivethirtyeight-data-audit` · 422 MB |
| newsapps/beeswithmachineguns | **NO-GO install (Watch)** | metadata only |
| vbuterin/aztec_experiments | **NO-GO install (Watch)** | metadata only · no SPDX |

CCC Context brief (tokenization blog URL 19): `Cemini claude code CCC/briefs/2026-07-20_k175-tokenization-blog-context.md` (outside wiki path — not `@related`).

## Snippets

> Aggregate: Integrate tint; Extract 538 + censusreporter + babynames + CodiceFiscaleJS; Watch bees + aztec. [Source: URL Revenue and Project Analysis.docx]

> CodiceFiscaleJS: comuni soppressi matrix as regional playbook engine for jure sanguinis geo validation. [Source: same]
