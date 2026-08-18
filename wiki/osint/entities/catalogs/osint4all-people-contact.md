---
title: OSINT4ALL — people / contact catalog
type: entity
tags: [osint, catalog, osint4all, k241, people]
keywords: [people search, username, email, phone, identity resolution, FamilyTreeNow, WhatsMyName, sherlock, maigret, holehe, Epieos, Hunter, PhoneInfoga, OpenCelliD, leaked.site]
related:
  - entities/tools/osint4all.md
  - concepts/osint4all-catalog.md
  - sources/osint4all-startme-2026-08-18.md
  - entities/tools/sherlock.md
  - entities/tools/mitaka.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @entities/tools/osint4all.md — hub tool entity
- @concepts/osint4all-catalog.md — KEEP / CONTEXT / CAUTION filing rules
- @sources/osint4all-startme-2026-08-18.md — start.me ingest (K241)
- @entities/tools/sherlock.md — username footprint (K227 Extract)

## Raw Concept

OSINT4ALL group **02-people-contact** — people search, username, email, phone, identity-resolution heading, resident databases, and “resolver” bookmarks from the L1rEYQ board (mirrored 2026-08-18). One catalog page; not a stub farm. **No private Barone pedigree.** FamilyTreeNow stays KEEP toward Atto / OSINT methodology only.

| Field | Value |
|-------|--------|
| Board group | `02-people-contact` |
| Links (board) | 110 |
| Sections | 7 (IDENTITY RESOLUTION = 0 links) |
| Source JSON | `.local/osint4all/groups/02-people-contact.json` |
| Filing date | 2026-08-18 |

## Narrative

Public people locators, username checkers (WhatsMyName, sherlock, maigret), email enrichment (Epieos, holehe, Hunter), and phone/cell-tower tools (PhoneInfoga, OpenCelliD) are **KEEP** for authorized OSINT. FamilyTreeNow is **KEEP (atto/osint)** — public US relatives/records locator, never private vitals. State “resident database” clones are KEEP as people-search locators, not a scrape playbook. Keybase.pub-hosted Pipl/CANRES mirrors are **DEAD-OUTDATED** (keybase.pub hosting ended 2023). Classic dead people-search clones (iTools meta-search, Yasni) are **DEAD-OUTDATED**. Discord/Skype IP resolvers on leaked.site and credential-style PSN/Xbox resolvers are **CAUTION** rows — listed so the board contents are visible; **do not visit leaked.site**; no IP-dox or dump-search playbook. Shadowcrypt Cloudflare origin lookup is **CONTEXT** (technique locator, not a leak forum). `h8mail` and WhatBreach are **CONTEXT** breach-correlation locators — listed-only; not a dump playbook (Sol audit 2026-08-18).

**Disposition totals:** KEEP 98 · DEAD-OUTDATED 4 · CONTEXT 3 · CAUTION 5 · NESTED-HUB 0 · board rows 110.

## PEOPLE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| IDCrawl | https://www.idcrawl.com/ | — | KEEP | Name / username / phone people-search hub |
| WebMii | https://webmii.com/ | — | KEEP | Public-web people search |
| Tools | https://intelx.io/tools?tab=person | — | KEEP | Intelligence X person-tab locator |
| TruePeopleSearch | https://www.truepeoplesearch.com/ | — | KEEP | US public-records people search |
| Free People Search | https://www.peoplefinder.com/ | — | KEEP | Commercial people-finder locator |
| fastpeoplesearch | https://fastpeoplesearch.com/ | — | KEEP | US name / phone / address locator |
| Yandex People Search | https://yandex.ru/people | — | KEEP | RU/CIS people locator (yandex.ru/people) |
| FamilyTree | https://www.familytreenow.com/ | @concepts/computational-genealogy-archival-automation.md | KEEP | Atto/OSINT — US relatives + public records; no private pedigree |
| People Search | http://itools.com/search/people-search | — | DEAD-OUTDATED | 2000s meta-search wrapping defunct locators (Wink, Yahoo People) |
| People Search Engine | https://cse.google.com/cse?cx=14db36e158cd791c0 | — | KEEP | Google CSE over people-search sites |
| Dating Sites Search Engine | https://cse.google.com/cse?cx=c7b340447e1e12653 | — | KEEP | Google CSE over dating-profile surfaces |
| 192 | https://www.192.com/ | — | KEEP | UK directory / people locator |
| International | https://www.infobel.com/ | — | KEEP | International directory locator |
| People search Tool | https://www.aware-online.com/en/osint-tools/people-search-tool/ | — | KEEP | Aware Online people-search launcher |
| PeekYou | https://www.peekyou.com/ | — | KEEP | People / username aggregator |
| White Pages | https://www.whitepages.com/ | — | KEEP | US whitepages locator |
| New Canada 411 | https://www.canada411.ca/ | — | KEEP | Canadian directory locator |
| 411 | http://411.com/ | — | KEEP | US 411 directory locator |
| TruthFinder | https://www.truthfinder.com/ | — | KEEP | Paywalled people-search locator |
| zaba search | https://www.zabasearch.com/ | — | KEEP | US people-search locator |
| Thats them | https://thatsthem.com/ | — | KEEP | Name / email / phone / address locator |
| People search | https://radaris.com/ | — | KEEP | People-search aggregator |
| No.1 Free People Search | http://www.yasni.com/ | — | DEAD-OUTDATED | Classic people-search clone; long a parked/spam aggregator |
| Gofindwho.com | https://gofindwho.com/ | — | KEEP | OSINT people-search form launcher |
| xlek | https://xlek.com/ | — | KEEP | People-search aggregator locator |
| Ufind.name | https://ufind.name/ | — | KEEP | People-search engine locator |

## USERNAME

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| WhatsMyName Web | https://whatsmyname.app/ | — | KEEP | Username → site hits (web) |
| Username Checker | https://analyzeid.com/username/ | — | KEEP | Username availability / footprint |
| Username Search | https://www.idcrawl.com/username | — | KEEP | IDCrawl username tab |
| Tools | https://intelx.io/tools?tab=username | — | KEEP | Intelligence X username-tab locator |
| maigret | https://pypi.org/project/maigret/ | — | KEEP | Username OSINT CLI (PyPI) |
| sherlock | https://github.com/sherlock-project/sherlock | @entities/tools/sherlock.md | KEEP | Username social footprint — Atto FIND Extract; human-gated |
| socialscan | https://pypi.org/project/socialscan/ | — | KEEP | Email/username existence checker (PyPI) |
| socid-extractor | https://pypi.org/project/socid-extractor/ | — | KEEP | Extract IDs from social profile pages |
| social-analyzer | https://pypi.org/project/social-analyzer/ | — | KEEP | Username / profile analyzer (PyPI) |
| KnowEm | https://knowem.com/ | — | KEEP | Username availability across networks |
| Check Usernames | https://checkusernames.com/ | — | KEEP | Username checker locator |
| Username Checker | https://checkuser.org/ | — | KEEP | Username checker locator |
| Namechk | https://namechk.com/ | — | KEEP | Username / domain name checker |
| Lullar Com | https://com.lullar.com/ | — | KEEP | Legacy people/username search locator |
| SearchPOF.com | https://searchpof.com/ | — | KEEP | Plenty of Fish username search |
| OSINT Toolkit | https://one-plus.github.io/EmailUsername | — | KEEP | Email/username dork launcher |
| Username search tool | https://www.aware-online.com/en/osint-tools/username-search-tool/ | — | KEEP | Aware Online username launcher |
| snoop | https://github.com/snooppr/snoop | — | KEEP | Username search CLI |
| quidam | https://pypi.org/project/quidam/ | — | KEEP | Username OSINT (PyPI) |

## EMAIL

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Epieos Email Lookup | https://epieos.com/ | — | KEEP | Email → accounts / Google footprint |
| Intelligence X | https://intelx.io/tools?tab=email | — | KEEP | Intelligence X email-tab locator |
| holehe | https://pypi.org/project/holehe/ | — | KEEP | Email → registered sites (PyPI) |
| Infoga | http://github.com/m4ll0k/Infoga | — | KEEP | Email OSINT CLI |
| email2phonenumber | https://github.com/martinvigo/email2phonenumber | — | KEEP | Email → linked phone OSINT (authorized-target) |
| Trumail | https://trumail.io/ | — | KEEP | Email verification API locator (Emailable rebrand) |
| Email Verifier | https://hunter.io/email-verifier | — | KEEP | Hunter.io verifier locator |
| Verify Email | https://verify-email.org/ | — | KEEP | SMTP/MX email verifier |
| Reverse Whois | https://osint.sh/reversewhois/ | — | KEEP | Reverse-whois email/domain locator |
| Email Dossier | https://centralops.net/co/emaildossier.aspx | — | KEEP | Header / DNS email dossier |
| Email Format | https://www.email-format.com/ | — | KEEP | Corporate email-pattern locator |
| Email Header Analyzer | https://mxtoolbox.com/EmailHeaders.aspx | — | KEEP | Header analysis (MXToolbox) |
| E-mail search tool | https://www.aware-online.com/osint-tools/e-mail-search-tool/ | — | KEEP | Aware Online email launcher |
| Proofy | https://proofy.io/ | — | KEEP | Email verification locator |
| Email Permutator | http://metricsparrow.com/toolkit/email-permutator/ | — | KEEP | Name+domain permutation generator |
| Phonebook.cz | https://phonebook.cz/ | — | KEEP | Intelligence X phonebook (email/domain) |
| Email Breach Analysis | https://www.hotsheet.com/inoitsu/ | — | KEEP | HIBP-style checker; authorized-target only — not a dump playbook |
| Emailrep.io | https://emailrep.io/ | — | KEEP | Email reputation API locator |
| Email Finder | https://osint.sh/email/ | — | KEEP | osint.sh email finder |
| EmailHarvester | https://pypi.org/project/EmailHarvester/ | — | KEEP | Public-page email harvest CLI; authorized-target only |
| h8mail | https://pypi.org/project/h8mail/ | — | CONTEXT | Breach-correlation CLI — listed-only; not a dump playbook |
| WhatBreach | https://github.com/Ekultek/WhatBreach | — | CONTEXT | Breach-search CLI — listed-only; not a dump playbook |
| buster | https://github.com/sham00n/buster | — | KEEP | Email OSINT / account-recovery locator |
| Anymailfinder.com | https://anymailfinder.com/ | — | KEEP | Email finder locator |
| ProtOSINT | https://github.com/pixelbubble/ProtOSINT | — | KEEP | ProtonMail OSINT CLI |

## PHONE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| IntelTechniques Telephone | https://inteltechniques.com/tools/Telephone.html | — | KEEP | Bazzell telephone-tool launcher |
| Phonerator | https://www.martinvigo.com/tools/phonerator/ | — | KEEP | Phone-number permutation generator |
| PhoneInfoga | https://demo.phoneinfoga.crvx.fr | — | KEEP | PhoneInfoga public demo (may flake) |
| Reverse Phone Lookup | https://www.idcrawl.com/phone | — | KEEP | IDCrawl reverse-phone tab |
| ignorant | https://pypi.org/project/ignorant/ | — | KEEP | Phone → registered sites (PyPI) |
| PhoneInfoga | https://github.com/sundowndev/PhoneInfoga | — | KEEP | Phone OSINT scanner (GitHub) |
| Moriarty-Project | https://github.com/AzizKpln/Moriarty-Project | — | KEEP | Phone/username OSINT toolkit |
| collector | https://github.com/galihap76/collector | — | KEEP | Phone OSINT collector CLI |
| Truecaller Search Engine | https://cse.google.com/cse?cx=c46b76bce1848d976 | — | KEEP | Google CSE over Truecaller-index pages |
| Nuwber | https://nuwber.com/ | — | KEEP | People / reverse-phone locator |
| Who Called Me | https://www.whocalledme.com/ | — | KEEP | Crowd reverse-phone comments |
| Phone number search Tool | https://www.aware-online.com/en/osint-tools/phone-number-search-tool/ | — | KEEP | Aware Online phone launcher |
| Validnumber.com | https://validnumber.com/ | — | KEEP | Number validation / line-type locator |
| Reverse Phone Lookup | https://www.zlookup.com/ | — | KEEP | Reverse-phone locator |
| Reverse Phone Lookup | https://www.reversephonecheck.com/ | — | KEEP | Reverse-phone locator |
| Truecaller | https://www.truecaller.com/ | — | KEEP | Caller-ID / reverse-phone locator |
| Phone Number Lookup Tool | https://shadowcrypt.net/tools/phone | — | KEEP | Reverse-phone tool page |
| SYNC.me | https://sync.me/ | — | KEEP | Caller-ID / reverse-phone locator |
| OpenCelliD | https://opencellid.org/ | — | KEEP | Cell-tower geolocation (MCC/MNC/LAC/CID) |
| CellTower Locator | http://www.cell2gps.com/ | — | KEEP | Cell-ID → approximate GPS |
| Find GSM base stations cell id coordinates | https://cellidfinder.com/ | — | KEEP | GSM cell-ID coordinate lookup |
| Phone Scoop | https://www.phonescoop.com/phones/ | — | KEEP | Handset / FCC device database |
| GSM Arena | https://www.gsmarena.com/ | — | KEEP | Handset specs locator |
| Fcc.io | http://fcc.io/ | — | KEEP | FCC ID lookup |
| Oldphonebook.com | http://www.oldphonebook.com/ | — | KEEP | Historical US phone-book locator |
| carrier lookup | https://www.carrierlookup.com/ | — | KEEP | Number → carrier / line type |
| Free Reverse Phone Lookup | https://spydialer.com/default.aspx | — | KEEP | Reverse-phone locator |

## IDENTITY RESOLUTION

Board heading present in the 2026-08-18 dump; **0 links**. No nested hub to follow.

## RESIDENT DATABASE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Michigan Resident Database | https://www.michiganresidentdatabase.com/ | — | KEEP | State-branded people-search locator (not a scrape playbook) |
| Ohio Resident Database | https://www.ohioresidentdatabase.com/ | — | KEEP | State-branded people-search locator |
| Florida Residents Directory | https://www.floridaresidentsdirectory.com/ | — | KEEP | State-branded people-search locator |
| North Carolina Resident Database | https://northcarolinaresidentdatabase.com/ | — | KEEP | State-branded people-search locator |
| NY Rent Regulated Building Search | https://apps.hcr.ny.gov/BuildingSearch/ | — | KEEP | Official NY HCR rent-regulated building search |
| Canadian Resident Database (warning: slow) | https://bloopbase.keybase.pub/POPPY/CANRES/index.html | — | DEAD-OUTDATED | keybase.pub hosting shut down 2023; do not chase the mirror |
| Pipl US (warning: slow) | https://bloopbase.keybase.pub/POPPY/PIPL/index.html | — | DEAD-OUTDATED | keybase.pub hosting shut down 2023; do not chase the mirror |

## RESOLVERS

Credential-style and leak-forum IP “resolvers.” Rows exist so the board contents are visible. **Do not visit leaked.site.** No IP-dox, dump-search, or credential-stuffing playbook.

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Skype Resolver | http://www.skypeipresolver.net/index.php | — | CAUTION | Skype IP resolver (protocol long dead); credential/IP-dox adjacent — listed only |
| PSN Resolver | https://playstationresolver.xyz/ | — | CAUTION | Credential-style PSN resolver — listed only; do not operationalize |
| Cloudflare Resolver | http://www.skypeipresolver.net/cloudflare.php | — | CAUTION | Same skypeipresolver.net family — listed only |
| Cloudflare Resolver Tool | https://shadowcrypt.net/tools/cloudflare | — | CONTEXT | CF origin-IP technique locator (not a leak forum); know it exists |
| Discord Resolver | https://www.leaked.site/index.php?resolver/discord.0/ | — | CAUTION | leaked.site Discord IP resolver — **do not visit**; listed only |
| Xboxresolver.com | https://xboxresolver.com/ | — | CAUTION | Credential-style Xbox resolver — listed only; do not operationalize |

## Snippets

> Group `02-people-contact`: 110 links across 7 sections (PEOPLE, USERNAME, EMAIL, PHONE, IDENTITY RESOLUTION, RESIDENT DATABASE, RESOLVERS). IDENTITY RESOLUTION had 0 URLs. [Source: `.local/osint4all/groups/02-people-contact.json` / OSINT4ALL start.me L1rEYQ (retrieved 2026-08-18)]

| Section | n |
|---------|---|
| PEOPLE | 26 |
| USERNAME | 19 |
| EMAIL | 25 |
| PHONE | 27 |
| IDENTITY RESOLUTION | 0 |
| RESIDENT DATABASE | 7 |
| RESOLVERS | 6 |
| **Total rows** | **110** |

| Disposition | n |
|-------------|---|
| KEEP | 100 |
| DEAD-OUTDATED | 4 |
| CONTEXT | 1 |
| CAUTION | 5 |
| NESTED-HUB | 0 |

Core KEEP anchors: FamilyTreeNow (atto/osint), WhatsMyName, sherlock (@entities/tools/sherlock.md), maigret, Epieos, holehe, Hunter, PhoneInfoga, OpenCelliD. leaked.site Discord + Skype/PSN/Xbox resolvers = CAUTION (not visited).
