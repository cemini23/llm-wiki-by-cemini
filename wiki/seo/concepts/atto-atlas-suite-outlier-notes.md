---
title: Atto — Outlier Weekly atlas + genealogy suite notes
type: concept
tags: [social, substack, outlier-weekly, atto, atlas, genealogy, youratto]
keywords: [atto, youratto, historical atlas, cognomi heatmap, parrocchie, ansc, caduti, outlier-weekly]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/atto-outlier-family-story-notes.md
  - concepts/guruwatcher-outlier-x-article-notes.md
  - concepts/outlier-weekly-issue3-world-cup-bot-notes.md
  - entities/tools/substack-publisher-mcp.md
  - "@osint-wiki/concepts/historical-jurisdiction-atlas.md"
  - "@osint-wiki/concepts/atto-macos-gtm-gumroad.md"
maturity: draft
created: 2026-10-25
updated: 2026-10-25
ship_draft: briefs/2026-10-25_outlier-weekly-atto-atlas-and-suite.md
draft_version: draft-v2
status: SCHEDULED — publishes 2026-10-26 at 09:00 ET
---

## Raw Concept

Second **Atto** Outlier Weekly issue. The first issue (2026-08-11) was the family story and the paperwork problem. This issue is the product update: five free tools that went live on 2026-10-25, plus three app releases since August. Full paste: `briefs/2026-10-25_outlier-weekly-atto-atlas-and-suite.md`.

## Narrative

### Lane

Builder product with a public free tier. The free atlas answers a question about a **place**. The paid app holds data about a **person**. Sell the split, and sell the refusal to guess. Do **not** sell eligibility, OCR magic, or archive access.

### Status

| Asset | Status |
|-------|--------|
| Marketing brief + paste body | `briefs/2026-10-25_outlier-weekly-atto-atlas-and-suite.md` — **draft-v2**, brief audit PASS 100/100 |
| Outlier | **SCHEDULED** — 2026-10-26 at 09:00 ET |
| X Article | **Deferred** (as with the first Atto issue) |
| Hero image | Atlas at 1861, regime colors on the province mesh |
| Publish window | 2026-10-26, 09:00 ET |
| Issue number | Confirm next free issue at paste time |

### Title locked for paste

| Surface | Title |
|---------|-------|
| Outlier | The Town Changed Its Name. The Map Should Not Guess. |
| Subtitle | Atto shipped a free historical atlas of 9,869 Italian places, four archival research tools, and three desktop releases. The rule behind all of it is simple: do not guess. |
| SEO slug | `italian-town-changed-name-historical-atlas` |
| Email subject | The map does not guess |

### Verified facts for paste

Every number below was checked against the built data or the repo on 2026-10-25. Do not round or inflate them.

| Claim | Value | Source |
|---|---|---|
| Places in the atlas | 9,869 | `comuni-index.json` `placeCount` |
| Year range | 1796 to 2026; date inside a year is 1 July | atlas page + README |
| Dioceses | 107 | `parrocchie-db.json` |
| PEC rows | 7,745 IndicePA + 2,120 pattern fallback = 9,865 comuni | `ansc-pec-db.json` |
| Surname regions (Phase 11) | Rossi to Emilia-Romagna, Ferrari to Lombardia, Barone to Campania | `cognomi-db.json` |
| Foundling surnames | Esposito Napoli, Innocenti Firenze, Proietti Roma, Colombo Milano (ambiguous) | `cognomi-db.json` |
| Sicily civil registration | 1 January 1820, Stato Civile Borbonico | `scripts/04_build_bundle.py` |
| Sardinia civil registration | 1838, Stato Civile Sabaudo, parish-kept | `scripts/04_build_bundle.py` |
| Chronicles | 5 (garibaldi-mille, dante-exile, sicily-to-ny, veneto-to-buenos-aires, lercara-new-york) | `routes.json` |
| Ports and crossings | 8 (Genova, Napoli, Palermo, Messina, Trieste, Livorno, Modane, Chiasso) | `routes.json` |
| Mac kit | 0.1.15 / build 25 | PROGRESS board |
| Windows kit | 0.1.14, Azure-signed | PROGRESS board |
| Linux desktop | 0.1.14, invite-only (AppImage + .deb) | PROGRESS board |
| Defects closed in 0.1.15 | 25 | K326 commit |
| Birth-act parser exact match | 13.56 percent at one worker | K325 measurement |
| Kraken vs Transkribus | NOT MEASURED | K280 decision |

### Revision v2 (2026-10-25)

Operator review produced four fixes. All four are applied in the paste body.

1. **Historical rules are authority, not apology.** The old "What is still not finished?" list is now "Historical rules the atlas enforces that naive tools miss". The Veneto 1871 gap, the island exemptions, and the ANSC paper rule now show domain modelling instead of incompleteness.
2. **Defensive disclaimers removed.** The surname section no longer opens with "the page I expect to get complaints about". It leads with the foundling hospital detector and the toponymic resolver. Phase 11 shipped the region coloring, so Rossi, Ferrari, and Barone now resolve to Emilia-Romagna, Lombardia, and Campania.
3. **The 13.56 percent figure is reframed.** It is now the proof against "1-click AI tree builders", followed by the page-type gate and review-gated extraction. It is no longer a standalone limit.
4. **Windows added to the CTA.** Subtitle, CTA row, and body all say Mac and Windows.

Fact corrections made during the rewrite:

- "7,900+ official IndicePA" was too high. The measured count is **7,745**, plus 2,120 fallback rows.
- "clean-room" was dropped. The jiangshan-map clone was read as a reference, so the honest term is "independent".
- "official ISTAT, ANPR, OpenPolis, IndicePA" became "public Italian datasets". OpenPolis is not an official body, and the comune data is ISTAT-derived via `matteocontrini/comuni-json`.

### Copy guardrails

- Lead with the atlas and the four tools. The app releases come third. Operator chose this order on 2026-10-25.
- One rule carries the issue: **do not guess**. Every section shows a refusal.
- The atlas never formats a coordinate. The agent passes `?year=&place=` only.
- The cognomi page is a **linguistic estimate, not a census**. Gray means no cluster. Do not call it a hotspot.
- jiangshan-map is GPL-3.0. Say "contract borrowed, code not". Never imply a code port.
- Do not claim handwriting OCR works. State that the head-to-head is not measured and why.
- Honest limits are a section, not a footnote. The list in the draft is the expected form.
- No em dashes in the paste body. Multi-sentence paragraphs. First person.
- No living-person PII, no Barone surname, no private `pages.dev` URLs.
- Free tier needs no account and no API key. Say that plainly.

### Why this issue exists

The first Atto issue sold a private vault and could not show the work, because the work is PII. The atlas is the first public surface that shows the method without showing a family. It converts the product rule into something a reader can test in ten seconds. That is the editorial reason to publish it now.

### Open decisions

- [ ] Confirm issue number at paste time
- [ ] Hero image yes/no
- [x] Publish day: 2026-10-26 at 09:00 ET
- [ ] Optional X Article after Outlier goes live
- [ ] Add the live Substack URL to this page and to the brief frontmatter

### After LIVE

1. Flip the status row and `status:` frontmatter to LIVE with the Substack URL
2. Add a row to `@concepts/x-account-voice-and-format.md` if the piece sets a new exemplar
3. Append the live line to `wiki/seo/log.md`
4. Record any reader corrections to the atlas data as a fix list
