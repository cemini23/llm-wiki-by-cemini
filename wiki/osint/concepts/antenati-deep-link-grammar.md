---
title: Antenati deep-link grammar — search-registry + ARK
type: concept
tags: [concept, genealogy, antenati, deep-link, k180, draft]
keywords: [search-registry, localita, tipologia, anno, ARK, lang=it, dual-original, find plan]
related:
  - sources/gemini-portale-antenati-research-guide-2026-07-21.md
  - sources/gemini-italian-civil-register-extraction-2026-07-21.md
  - sources/gemini-italian-genealogy-research-tools-2026-07-21.md
  - sources/gemini-italian-civil-genealogy-find-playbook-2026-07-22.md
  - sources/gemini-italian-citizenship-software-map-2026-07-22.md
  - sources/gemini-italian-citizenship-document-pipelines-2026-07-22.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/us-italy-hometown-reveal-ladder.md
  - concepts/italian-citizenship-pathways-document-pipelines.md
  - entities/tools/gcerretani-antenati.md
maturity: draft
created: 2026-07-21
updated: 2026-07-22
---

## Relations

- @sources/gemini-portale-antenati-research-guide-2026-07-21.md — primary DR (K180)
- @sources/gemini-italian-civil-genealogy-find-playbook-2026-07-22.md — K185 FIND pipeline + templates + do-not-automate
- @sources/gemini-italian-citizenship-software-map-2026-07-22.md — K185 research vs filing; pathway triage after FIND
- @sources/gemini-italian-civil-register-extraction-2026-07-21.md — ARK + act-number citation
- @sources/gemini-italian-genealogy-research-tools-2026-07-21.md — WAF / IIIF ops context
- @concepts/us-italy-hometown-reveal-ladder.md — supplies exact comune before these links help
- @concepts/italian-citizenship-pathways-document-pipelines.md — K183: deep links find acts; Comune issues filing copies
- @sources/gemini-italian-citizenship-document-pipelines-2026-07-22.md — research vs *copia integrale*
- @concepts/computational-genealogy-archival-automation.md — civil era hub
- @concepts/italian-regional-genealogy-archive-playbook.md — when Antenati volume missing → regional/Comune pivot
- @concepts/gpuology-genealogy-agent-kit.md — Atto find.plan pointer surface
- @entities/tools/gcerretani-antenati.md — bulk IIIF after human browse (Watch)

## Raw Concept

Operator-openable HTTPS patterns for Portale Antenati that beat coarse fulltext `q=` — for Atto `find plan` / pointer builders. **No scrape, no CDN upload.**

## Narrative

### Prefer browse deep links

```
https://antenati.cultura.gov.it/search-registry/?localita={comune}&tipologia={Nati|Matrimoni|Morti}&anno={YYYY}&lang=it
```

Optional filters when known: `archivio`, `fondo`, `serie`, `descrizione`. Always pass `lang=it`.

Nominative (secondary / low-yield framing from K185):

```
https://antenati.cultura.gov.it/search-nominative/?cognome={SURNAME}&nome={GIVEN_NAME}
```

FamilySearch durable catalog (film):

```
https://www.familysearch.org/search/catalog/results?q.filmNumber={FILM_NUM}
```

### Cite with ARK

When the researcher lands on a volume/page, log the ARK URL (`/ark:/12657/…`), register year, typology, and *numero dell'atto* — not `detail-registry/?s_id=`.

### FIND.md emission pipeline (K185)

1. Geographic normalize (Belfiore / ISTAT; frazione → administrative comune; historical name for query, modern Archivio for custody).
2. Nominative deep links — framed as rapid-pass only.
3. Registry browse deep links — primary.
4. Military backdoor if male ~1850–1920 (*Liste di Leva* / *Ruoli Matricolari*); Albo d'Oro often search-UI only.
5. Optional cassette / local HTR prep — never server scrape.
6. Emit `FIND.md` checklist for human execution — never write `truth.ged` without Approve.

### Checklist deltas (vs name-only search)

1. Resolve exact comune (US ladder / place engine) first.
2. Open `search-registry` for Nati ±1–2 years (then Matrimoni/Morti).
3. If nominative index empty → still browse volumes + annual/decennial indices.
4. If no volume → dual-original: write Comune for *copia integrale*; Antenati printouts are not legal certificates.
5. Save act image to local vault; candidate packet only — human Approve merges.
6. Soft-prior checks: frazione vs comune · temporal merger validity · civil vs baptism · 70-year privacy closure.

### Ops constraints / do-not-automate

AWS WAF on image tiles; IIIF manifests may be inspectable but bulk download is operator-local / Watch tooling only. Authenticated Ministry download area (announced) may change third-party CLI economics — Atto stays browser-first.

**Forbidden:** Antenati CDN scrape · auto tree merge · unauthorized server HTR on scraped images · bypass Comune/Archivio paywalls · blind POST into portal forms.
