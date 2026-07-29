---
title: Italian citizenship pathways — document pipelines for Atto
type: concept
tags: [concept, genealogy, citizenship, jure-sanguinis, k183, atto, draft]
keywords: [JS_ADMIN_CONSULATE, copia integrale, apostille, Tajani, Minor Issue, 1948, Prenot@Mi, concierge]
related:
  - sources/gemini-italian-citizenship-document-pipelines-2026-07-22.md
  - sources/gemini-italian-citizenship-software-map-2026-07-22.md
  - sources/gemini-atto-macos-gtm-2026-07-22.md
  - sources/italian-citizenship-primary-law-lock-2026-07-22.md
  - sources/cassazione-minor-issue-pdf-pack-2026-07-28.md
  - sources/interno-circolari-law74-2026-07-22.md
  - sources/maeci-consular-js-law11-2026-07-22.md
  - concepts/italian-citizenship-primary-law-lock.md
  - concepts/gpuology-genealogy-agent-kit.md
  - concepts/atto-macos-gtm-gumroad.md
  - concepts/antenati-deep-link-grammar.md
  - concepts/us-italy-hometown-reveal-ladder.md
  - concepts/computational-genealogy-archival-automation.md
  - concepts/italian-regional-genealogy-archive-playbook.md
  - sources/gemini-portale-antenati-research-guide-2026-07-21.md
  - sources/gemini-italian-civil-register-extraction-2026-07-21.md
  - sources/gemini-italian-american-genealogy-sources-2026-07-21.md
  - sources/youtube-italian-citizenship-channels-2026-07-22.md
  - concepts/italian-citizenship-youtube-soft-flags.md
maturity: validated
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- @sources/gemini-italian-citizenship-document-pipelines-2026-07-22.md — primary DR (K183)
- @sources/gemini-italian-citizenship-software-map-2026-07-22.md — K185 decision tree + status vocab + proposed ID renames
- @sources/italian-citizenship-primary-law-lock-2026-07-22.md — K187 statute/court lock
- @sources/interno-circolari-law74-2026-07-22.md — K188 Interno operational circulars
- @sources/maeci-consular-js-law11-2026-07-22.md — K189 Prenot@Mi a-bis + L. 11 central venue
- @concepts/italian-citizenship-primary-law-lock.md — soft-flag ship posture
- @sources/youtube-italian-citizenship-channels-2026-07-22.md — K186 ICA/IDCA deep watch
- @concepts/italian-citizenship-youtube-soft-flags.md — appointment evidence + court soft-flags
- @concepts/gpuology-genealogy-agent-kit.md — product: vault + checklist + optional concierge (not auto-file)
- @concepts/atto-macos-gtm-gumroad.md — listing must use safe status language
- @sources/gemini-atto-macos-gtm-2026-07-22.md — DIY persona / fee-risk framing for GTM
- @concepts/us-italy-hometown-reveal-ladder.md — Stage 0 research before Italian *copie*
- @concepts/antenati-deep-link-grammar.md — find acts; then order filing-grade copies from Comune
- @concepts/computational-genealogy-archival-automation.md — lineage evidence packets feed citizenship pack
- @concepts/italian-regional-genealogy-archive-playbook.md — PEC / *copia integrale* requests
- @sources/gemini-italian-civil-register-extraction-2026-07-21.md — why marginalia matter
- @sources/gemini-portale-antenati-research-guide-2026-07-21.md — dual-original; portal ≠ certificate
- @sources/gemini-italian-american-genealogy-sources-2026-07-21.md — US long-form / naturalization proofs

## Raw Concept

How Atto should model **citizenship document pipelines**: pathway triage → required document types → apostille/translation rules → venue — without giving legal advice or auto-filing.

**Not legal advice.** K187 courts/statute · K188 Interno · K189 MAECI/consular + L. 11 GU. Mantova/Campobasso Cost. merits + Sezioni Unite written still open.

## Narrative

### Path classes (software IDs)

| ID | Meaning | Typical venue |
|----|---------|---------------|
| `BIRTH_REG_ABROAD` | Child of **already recognized** Italian parent — register foreign birth | Consulate vital stats / AIRE |
| `JS_ADMIN_CONSULATE` | Jure sanguinis admin recognition (meets current generational rules) | Consulate + Prenot@Mi |
| `JS_ADMIN_COMUNE` | Same claim filed in Italy after real residency | Comune + *permesso attesa cittadinanza* |
| `JS_JUDICIAL_1948` | Maternal transmission / pre-1948 (or analogous equality) cases | Tribunale |
| `JS_JUDICIAL_MINOR` | Parental naturalization while next gen was minor cohabitant | Tribunale |
| `JS_JUDICIAL_TAJANI` | Blocked by Law 74/2025-style generational limits; challenge retroactivity | Tribunale |
| `NAT_MARRIAGE` | Spouse naturalization | Prefettura / consulate / Portale Servizi |
| `NAT_RESIDENCY` | Residency naturalization (years vary) | Prefettura |

### Stage machine (US → consulate baseline)

0. **Triage** — naturalization-before-birth? minor-at-naturalization? pre-1948 maternal? Tajani parent/grandparent exclusive-Italian test? intake date vs 27 Mar 2025 grandfather?
1. **Italian root** — *copia integrale* (not Antenati scan; not *estratto*)
2. **US chain** — long-form vitals each generation + naturalization **or** USCIS/NARA/local no-record letters
3. **Apostille** — by issuing jurisdiction (state SoS vs federal State Dept chain)
4. **Translate** — consular certified vs Italian *asseverata* (venue fork)
5. **Forms + appointment** — consulate Forms 1–4 class; jurisdiction proof; Prenot@Mi; fee
6. **After** — transcription at ancestral comune, AIRE, codice fiscale, passport; vault “citizenship evidence pack”

### Atto product rules

- Research images → FIND / vault intake; **filing-grade** docs tracked as separate checklist items.
- Red-flag triage **halts** admin checklist and surfaces “consult citizenship counsel / judicial path” — never invents eligibility.
- Concierge pack (`atto concierge`) can export the evidence vault; humans still apostille, translate, and file.
- Watch calendar: Constitutional Court / Cassazione outcomes may flip routing — keep pathway rules data-driven.

### K185 software-map deltas (pending product GO)

Proposed ID renames from @sources/gemini-italian-citizenship-software-map-2026-07-22.md — **do not rename shipped enums without an Atto brief:**

| Current (K183) | Proposed | Why (per DR) |
|----------------|----------|--------------|
| `BIRTH_REG_ABROAD` | `JS_BENEFICIO_MINORE` | Law 74/2025 affirmative declaration framing |
| `JS_JUDICIAL_TAJANI` | `JS_JUDICIAL_PRE_2025_SAFE` | Safe-harbor / equivocal-intent litigation path |
| `NAT_MARRIAGE` | `JM_MARRIAGE_ART5` | Art. 5 Law 91/1992 |
| `NAT_RESIDENCY` | `NAT_RESIDENCY_ART9` | Art. 9 Law 91/1992 |

**UI status vocab (safe):** Identified · Requested · Received · Checklist Complete · Appointment Pending · Under Consular Review · Recognized. Avoid “Ready to File / Submitted / Approved / You are eligible.”

**Soft-flags only:** post-1992 bipolidi Minor Issue; pre-27 Mar 2025 “clear intent” definition; consulate-variable name OATS.

### K186 YouTube deep-watch deltas

From @concepts/italian-citizenship-youtube-soft-flags.md (ICA/IDCA transcripts):

- **Appointment evidence pack** — Prenot@Mi unavailability series, account emails, consulate correspondence, wait-list proofs (counsel export; never “grandfathered”).
- **Venue soft-flag** — current = consulate of residence through **2028**; **MAECI central from 1 Jan 2029** (L. 11/2026) — soft-flag long-horizon abroad applicants.
- **Doc matrix (ICA claim)** — for applicants who meet *new* rules, vital/naturalization docs “have not changed”; eligibility triage changed.
- **Alt path label** — Italian parent/grandparent + ~2y legal Italy residency → residency-naturalization / art. 3-bis letter-d *research* track when JS chain broken.
- **Court glossary** — Costituzionale vs Cassazione; Cass. **13818/2026** interest-to-sue when filing blocked — **[CONFIRMED]**; Cost. **63/2026** left reform standing — **[CONFIRMED]**; Mantova/Campobasso + Sezioni Unite written — still open (K187).

### K187 primary-law lock

See @concepts/italian-citizenship-primary-law-lock.md — statute GU, Cost. 63, Cass. 13818, L. 11/2026 venue date locked; open watch list for post–Jun-9 Cost. sentenza + Sezioni Unite deposit.

### K188 Interno circolari

See @sources/interno-circolari-law74-2026-07-22.md — art. 3-bis a/a-bis = **comune** domanda / municipal appointment; letter d + art. 14 residency clocks; beneficio €250; riacquisto 2025–2027; beneficio minor declaration soft deadline **31 May 2029** (Circ. 19951).

### K189 MAECI / Law 11

See @sources/maeci-consular-js-law11-2026-07-22.md — consular a-bis = Prenot@Mi / section email; €600; L. 11 GU: **2029** postal central MAECI; through 2028 annual consular **cap** (≥100).

### Glossary (operator-facing)

*Copia integrale* · *Estratto* · AIRE · Apostille · *Traduzione asseverata* · Prenot@Mi · *Permesso di soggiorno per attesa cittadinanza* · 1948 rule · Minor Issue · Tajani / Law 74/2025 · *beneficio di legge* · Corte Costituzionale · Corte di Cassazione · *Sezioni Unite*
