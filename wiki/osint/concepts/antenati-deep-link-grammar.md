---
title: Antenati deep-link grammar — search-registry + ARK
type: concept
tags: [concept, genealogy, antenati, deep-link, k180, draft]
keywords: [search-registry, localita, tipologia, anno, ARK, lang=it, dual-original, find plan]
related:
  - sources/gemini-portale-antenati-research-guide-2026-07-21.md
  - sources/gemini-italian-civil-register-extraction-2026-07-21.md
  - sources/gemini-italian-genealogy-research-tools-2026-07-21.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/us-italy-hometown-reveal-ladder.md
  - entities/tools/gcerretani-antenati.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- @sources/gemini-portale-antenati-research-guide-2026-07-21.md — primary DR (K180)
- @sources/gemini-italian-civil-register-extraction-2026-07-21.md — ARK + act-number citation
- @sources/gemini-italian-genealogy-research-tools-2026-07-21.md — WAF / IIIF ops context
- @concepts/us-italy-hometown-reveal-ladder.md — supplies exact comune before these links help
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

### Cite with ARK

When the researcher lands on a volume/page, log the ARK URL (`/ark:/12657/…`), register year, typology, and *numero dell'atto* — not `detail-registry/?s_id=`.

### Checklist deltas (vs name-only search)

1. Resolve exact comune (US ladder / place engine) first.
2. Open `search-registry` for Nati ±1–2 years (then Matrimoni/Morti).
3. If nominative index empty → still browse volumes + annual/decennial indices.
4. If no volume → dual-original: write Comune for *copia integrale*; Antenati printouts are not legal certificates.
5. Save act image to local vault; candidate packet only — human Approve merges.

### Ops constraints

AWS WAF on image tiles; IIIF manifests may be inspectable but bulk download is operator-local / Watch tooling only. Authenticated Ministry download area (announced) may change third-party CLI economics — Atto stays browser-first.
