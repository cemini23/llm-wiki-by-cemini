---
title: Italian regional genealogy — archive playbook (Abruzzo / Calabria / Trentino)
type: concept
tags: [genealogy, archival, italy, abruzzo, calabria, trentino, draft]
keywords: [copia integrale, PEC, Catasto Onciario, Cassa Sacra, Liste di Leva, NatiTrentino, Sellia, Colledimacine, Val di Non]
related:
  - sources/gemini-italian-ancestry-deep-research-2026-07-09.md
  - sources/gemini-automated-deep-genealogy-research-2026-07-09.md
  - sources/gemini-abruzzo-diaspora-genealogy-2026-07-12.md
  - sources/gemini-sellia-calabria-archive-routing-2026-07-11.md
  - concepts/computational-genealogy-archival-automation.md
  - entities/tools/nati-in-trentino.md
  - entities/tools/steve-morse-census-tools.md
  - entities/tools/italian-parish-records.md
  - entities/tools/gcerretani-antenati.md
maturity: draft
created: 2026-07-09
updated: 2026-07-12
---

## Relations

- @sources/gemini-italian-ancestry-deep-research-2026-07-09.md — primary synthesis (K154)
- @sources/gemini-automated-deep-genealogy-research-2026-07-09.md — K153 era ladder companion
- @concepts/computational-genealogy-archival-automation.md — IDE / HTR / IIIF stack
- @entities/tools/nati-in-trentino.md — Trentino baptism index
- @entities/tools/steve-morse-census-tools.md — US census ED targeting
- @entities/tools/italian-parish-records.md — parish digitization
- @sources/gemini-sellia-calabria-archive-routing-2026-07-11.md — K159 Sellia deep routing
- @entities/tools/gcerretani-antenati.md — Antenati IIIF pull

## Raw Concept

How to push Italian (and Trentino/Austrian-era) lines past short civil extracts: which archives, which false-match traps, and which free indexes unlock the next generation — without inventing ancestors.

## Narrative

### Geographic priors (~1550)

| Region | 16th-c frame | Typical parish / secular pivot |
|--------|--------------|--------------------------------|
| Abruzzo Citeriore (e.g. Colledimacine) | Kingdom of Naples; feudal transfers (e.g. Valignano era) | Parish San Nicola; later Catasto Onciario (1753) at Archivio di Stato di Chieti |
| Calabria Ulteriore (inland Sellia) | Spanish viceroyalty; hilltop defensive borghi | Diocese Catanzaro-Squillace; parish San Nicola di Bari; **Cassa Sacra** after 1783 quake as parish-gap bridge |
| Val di Non (Trentino) | Prince-Bishopric of Trento / Habsburg | Taufbuch / Trauungsbuch / Sterbebuch; Nati in Trentino 1815–1923; Tiroler Landesarchiv for AH army classes |

### *Copia integrale* vs *estratto*

For 20th-c *stato civile* still held at the *comune*, request the **integral act** (parental ages, grandparents when present, marginal notes). Short certificates are insufficient for Gen4. Privacy: records under 100 years need requester ID + proof of direct descent; Italian formal letter + PEC preferred where offered.

Example contact patterns (verify live on *comune* sites before send): Colledimacine PEC `comune.colledimacine@pec.it`; Sellia anagrafe `anagrafe@comune.sellia.cz.it` (+ secondary PEC). Always distinguish **Sellia** (inland) from **Sellia Marina**.

### Brick-wall bridges (pre-1809 / destroyed parish)

1. **Catasto Onciario** (1740s–50s) — hearth/*fuochi* tax census; Capofuochi names + ages bridge late 1600s → 1809 civil.
2. **Liste di Leva / Ruoli matricolari** — draft lists with parental names; Abruzzo/Calabria at provincial State Archives; Trentino split Italian AS Trento vs Innsbruck for AH service.
3. **Cassa Sacra** (Calabria post-1783) — secular property surveys when parish books burned.
4. **Capitoli matrimoniali** — notarial dowry contracts often name multiple generations for consanguinity clearance.

### Sellia (CZ) — K159 deep routing

| Resource | ID / route | Use |
|----------|------------|-----|
| Antenati Restoration | Sellia serie ~91 packs; **46 processetti** | Gen6–8 via parish extracts in marriage packets |
| FS Tribunale | **2043789** (1866–1910) | Unindexed Nati/Matrimoni/Morti browse — Gen4 births ~1895–1915 |
| FS State Archive | **726599** | Morti ~1867–1890 |
| Comune PEC | `anagrafe@comune.sellia.cz.it` | Post-1910 *copia integrale* (not on Antenati) |
| ASC Catanzaro Leva | `as-cz@pec.cultura.gov.it` | Liste di Leva backup if civil nati missing |

**Trap:** Sellia Marina (post-1956) ≠ inland Sellia — homonyms may trace to Simeri Crichi / Magisano. **Passante** surname endemic in modern Sellia; **Costantino** patronymic cluster — prove *comune* anchor before regional dragnet. Detail: `@sources/gemini-sellia-calabria-archive-routing-2026-07-11.md` (private names in `~/Desktop/family/research/`).

### Abruzzo Maiella — K160 diaspora routing (Colledimacine / Montenerodomo)

| Resource | Route | Use |
|----------|-------|-----|
| Comune Colledimacine | PEC `comune.colledimacine@pec.it` | Historic *stato di famiglia*; post-1920 *copia integrale* |
| ASC Chieti | Catasto Onciario (1753) | Pre-1809 hearth bridge |
| Diocesi Chieti-Vasto | Archivio storico | Secular priest *fascicolo personale* |
| Ministero della Difesa | Ordine di Vittorio Veneto roll | WWI *mutilato* matriculation + 1968+ honor lock |
| NAA RecordSearch | Alien + Naturalization | Australian diaspora — arrival year + birth year keys |
| NSW BDM | Historical death index | Spouse maiden via certificate order |
| ANMI (Rome) | Membership archives | Diaspora association president dossiers |
| *L'Araldo Abruzzese* | Bound 1974–1976 volumes | Clergy missionary departure notices |

**Diaspora traps:** obituary informant omissions when sibling count is large; homonym quarantine (guild presidents, other continents); Swiss guest-worker false positives without *comune* anchor; Italian cemetery concession expiry masquerading as negative death proof. Detail: `@sources/gemini-abruzzo-diaspora-genealogy-2026-07-12.md` (private sprint in `~/Desktop/family/research/`).

### US staging-ground tactics

- Post-1910 NYC births: NYC DOH (VitalChek) **long form**, not Municipal Archives open set.
- Address → Enumeration District: Steve Morse Unified Census ED Finder, then browse 1940/1950 images.
- Ellis Island / manifests: Trentino-born often coded **Austrian** nationality — search accordingly.
- Naturalizations (NARA EDNY/SDNY post-1906): birthplace + ship + spouse fields.

### Red flags

- Ubiquitous surnames (e.g. Rossi) outside the documented *comune* without a linking act.
- Coastal Sellia Marina acts for inland Sellia lines.
- Promoting feudal surname-origin stories (liege / fief nicknames) to genetic descent without parish proof.
- Treating LLM Deep Research footnotes as primary evidence — re-open the archive URL.

### Cemini rule

Personal pedigrees and DNA stay off this wiki. Use this page as the **archive routing table**; private trees live on the operator laptop.

## Snippets

> “A standard certificate (estratto) is insufficient; the request must explicitly demand the Copia Integrale…” [Source: @sources/gemini-italian-ancestry-deep-research-2026-07-09.md]

> Trentino on US paperwork ≈ “Austrian” label ≠ modern Austria geography. [Source: @sources/gemini-italian-ancestry-deep-research-2026-07-09.md]
