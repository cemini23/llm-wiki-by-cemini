---
title: OSINT4ALL cyber / high-caution catalog
type: entity
tags: [osint4all, k241, cyber, caution]
keywords: [VirusTotal, Hybrid-Analysis, ANY.RUN, Malpedia, OTX, HIBP, Intelligence X, OFAC, GTD, SPLC, NSOPW, darknet, dump shops, malware corpora]
related:
  - entities/tools/osint4all.md
  - concepts/osint4all-catalog.md
  - sources/osint4all-startme-2026-08-18.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @entities/tools/osint4all.md — hub tool entity
- @concepts/osint4all-catalog.md — KEEP / CONTEXT / CAUTION filing rules
- @sources/osint4all-startme-2026-08-18.md — ingest source (K241)

## Raw Concept

OSINT4ALL group **07-cyber-caution** — threat-intel maps, malware sandboxes, hash-lookup sites, darknet indexes, dump shops, informant lists, public sex-offender registry locators, and extremist/sanctions archives from the L1rEYQ board (mirrored 2026-08-18). One catalog page; not a stub farm. **Majority CONTEXT by design.** Agents do not visit onion.pet, leak shops, darknet markets, or malware sample repos, and do not write exploits or dump-search playbooks.

| Field | Value |
|-------|--------|
| Board group | `07-cyber-caution` |
| Links (board) | 119 |
| Sections | 9 |
| Source JSON | `.local/osint4all/groups/07-cyber-caution.json` |
| Filing date | 2026-08-18 |

## Narrative

Public malware sandboxes and IOC corpora (VirusTotal, Hybrid-Analysis, ANY.RUN, Malpedia, AlienVault OTX) are **KEEP** with `wiki=cyber` — Cybersec wiki owns analysis runtime; this page is a locator only. Kaspersky and FireEye/Trellix threat maps, Have I Been Pwned, Intelligence X (public), OFAC sanctions search, START GTD, SPLC extremist-file profiles, and official sex-offender **registry locators** (NSOPW and peer government registers) are **KEEP** as public-record / public-intel locators. Public TI search portals (Pulsedive, Cisco Talos, ThreatMiner) are **KEEP** locators — “not in a named KEEP set” is not a filing criterion. Registry KEEP is locator-only: no targeting guidance.

Vendor threat-map copies, hash-recovery sites, Tor search locators, informant/snitch lists, chan/Parler research archives, and unofficial no-fly or “suspected terrorist” databases stay **CONTEXT** — know the board listed them; do not operationalize. Leak-dump shops (Scylla, Snusbase, leaked.site, DeHashed), DDoSecrets/Bloopbase dump indexes used as crimeware, ransomware onion.pet mirrors, darknet market/forum lists, theZoo / vx-underground sample repos, and exploitdb-bin-sploits are **CAUTION**: URL listed, **do not visit**, no payloads. Cymon and retired threat-map URLs are **DEAD-OUTDATED**.

## THREAT INTEL

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Threatbutt | https://threatbutt.com/map/ | — | CONTEXT | Parody threat map; not operational intel |
| Cyberthreat Real-Time Map | https://cybermap.kaspersky.com/ | cyber | KEEP | Kaspersky public threat map (named KEEP class) |
| Live Cyber Attack Threat Map | https://www.checkpoint.com/ThreatPortal/livemap.html | — | CONTEXT | Check Point vendor map; not in named KEEP set |
| Digital Attack Map | https://www.digitalattackmap.com/ | — | CONTEXT | Arbor/Google DDoS map; not in named KEEP set |
| Cyber Threat Map | https://www.fireeye.com/cyber-map/threat-map.html | cyber | KEEP | FireEye/Trellix public threat map (named KEEP class) |
| Bitdefender Threat Map | https://threatmap.bitdefender.com/ | — | CONTEXT | Vendor threat map; not in named KEEP set |
| Cyber Threat Intelligence | https://pulsedive.com/ | — | KEEP | Public TI search locator — not dump access |
| Cisco Talos Intelligence Group | https://talosintelligence.com/ | — | KEEP | Public vendor intel portal locator |
| Fortinet Threat Map | https://threatmap.fortiguard.com/ | — | CONTEXT | Vendor threat map; not a public IOC search |
| FortiGuard | http://www.fortiguard.com/ | — | CONTEXT | Vendor advisory portal |
| ThreatMiner | https://www.threatminer.org/ | — | KEEP | Public OSINT TI aggregator locator |
| cymon | https://cymon.io/ | — | DEAD-OUTDATED | Cymon discontinued (eSentire era); ignore |
| intelowlproject/IntelOwl | https://github.com/intelowlproject/IntelOwl | — | CONTEXT | Self-host TI aggregator (GitHub); not a public lookup |
| Visualizing Global Internet Performance | https://www.akamai.com/us/en/solutions/intelligent-platform/visualizing-akamai/real-time-web-monitor.jsp | — | DEAD-OUTDATED | Legacy Akamai Real-Time Web Monitor path; retired |
| THREAT MAP by LookingGlass | https://map.lookingglasscyber.com/ | — | DEAD-OUTDATED | LookingGlass map retired after acquisition |
| NETSCOUT Cyber Threat Horizon | https://horizon.netscout.com/ | — | CONTEXT | Vendor horizon dashboard; often login-gated |
| APTnotes | https://github.com/aptnotes/data | — | CONTEXT | Public APT-report index (PDFs, not samples) |

## MALWARE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Malpedia | https://malpedia.caad.fkie.fraunhofer.de/ | cyber | KEEP | KEEP cyber — public malware family/IOC corpus; Cybersec wiki owns analysis runtime |
| Interactive Online Malware Analysis Sandbox | https://app.any.run/ | cyber | KEEP | KEEP cyber — ANY.RUN public sandbox locator |
| Free Automated Malware Analysis Service | https://hybrid-analysis.com/ | cyber | KEEP | KEEP cyber — Hybrid-Analysis public sandbox locator |
| VirusTotal | https://www.virustotal.com/gui/ | cyber | KEEP | KEEP cyber — VT public multi-engine / IOC locator |
| Maltiverse | https://maltiverse.com/search | — | CONTEXT | IOC search; not in named KEEP sandbox set |
| Malware News Search | https://cse.google.com/cse?cx=003248445720253387346:turlh5vi4xc | — | CONTEXT | Google CSE over malware-news sites |
| AlienVault Open Threat Exchange | https://otx.alienvault.com/ | cyber | KEEP | KEEP cyber — OTX public pulse/IOC exchange |
| Jotti's malware scan | https://virusscan.jotti.org/ | — | CONTEXT | Public multi-AV scanner; not in named KEEP set |
| IObit Cloud | https://cloud.iobit.com/index.php | — | CONTEXT | Vendor cloud-scan portal; low-trust locator |
| theZoo | https://github.com/ytisf/theZoo | — | CAUTION | Live malware sample repo — list only; do not visit; no payloads |
| Vx-underground.org | https://vx-underground.org/ | — | CAUTION | Malware sample corpus — list only; do not visit; no payloads |
| VX Heaven | https://vx-underground.org/archive/VxHeaven/index.html | — | CAUTION | Historical malware archive via vx-underground — list only; do not visit |
| aptnotes/data | https://github.com/aptnotes/data | — | CONTEXT | Duplicate APT-report index (also under THREAT INTEL) |
| exploit-database-papers | https://github.com/offensive-security/exploitdb-papers | — | CONTEXT | Exploit-db papers (docs, not bins); not a PoC writeup |
| exploitdb-bin-sploits | https://github.com/offensive-security/exploitdb-bin-sploits | — | CAUTION | Binary exploit corpus — list only; do not visit; no payloads |

## HASH RECOVERY

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| CrackStation | https://crackstation.net | — | CONTEXT | Public unsalted-hash lookup; no cracking playbook; own-credential / authorized-lab only |
| Hashmob Community | https://hashmob.net/search | — | CONTEXT | Community hash-lookup locator; do not operationalize as a crack service |
| Hashes.com | https://hashes.com/en/decrypt/hash | — | CONTEXT | Commercial hash lookup; no playbook |
| Online Password Hash Crack | https://www.onlinehashcrack.com/ | — | CONTEXT | Paid hash-crack service; know it exists; do not operationalize |
| Md5 Decrypt & Encrypt | https://md5decrypt.net/en/ | — | CONTEXT | MD5 reverse-lookup locator; dual-use; no playbook |
| MD5 reverse lookup | https://md5.gromweb.com/ | — | CONTEXT | MD5 reverse-lookup locator; dual-use; no playbook |
| Ultimate Hashing | https://md5hashing.net/ | — | CONTEXT | Multi-algorithm hash lookup; dual-use; no playbook |
| Hashes.org | https://hashes.org/search.php | — | DEAD-OUTDATED | hashes.org seized/shut down; ignore |

## DARKNET

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Dark Tracer | https://darktracer.io/ | — | CONTEXT | Darkweb-monitoring claim; do not operationalize hidden-service access |
| ransomwatch | https://ransomwatch.telemetry.ltd/#/INDEX | — | CONTEXT | Ransomware leak-site tracker; do not visit listed onions |
| Ransomware Darknet websites | https://sizeof.cat/post/ransomware-darknet-websites/ | — | CAUTION | Ransomware onion directory — list only; do not visit |
| Ahmia — Search Tor Hidden Services | https://ahmia.fi/ | — | CONTEXT | Public Tor HS search locator; authorized research only; do not browse markets |
| Onion search engine | https://onionsearchengine.com/ | — | CONTEXT | Onion search locator; do not browse markets |
| onionsearch | https://pypi.org/project/onionsearch/ | — | CONTEXT | Tor-search CLI on PyPI; authorized-target only |
| Tor2Web: Tor Hidden Services Gateway | https://tor2web.onionsearchengine.com/ | — | CAUTION | Clearnet gateway onto hidden services — do not use for markets |
| Ransomware Group Sites | http://ransomwr3tsydeii4q43vazm7wofla5ujdajquitomtd47cxjtfgwyyd.onion.pet | — | CAUTION | Ransomware onion.pet — list only; do not visit |
| Blockpath.com | https://blockpath.com/ | — | CONTEXT | Blockchain path tool (misfiled in DARKNET) |
| LinkBaseORG | https://link-base.org/ | — | CAUTION | Darknet link directory — list only; do not visit |
| Onions - Darknetlive | https://darknetlive.com/onions/ | — | CAUTION | Darknet onion list — list only; do not visit |
| Darknet Market List | https://darknetlive.com/markets/ | — | CAUTION | Darknet market list — list only; do not visit |
| Darkweb Forums | https://darknetlive.com/forums/ | — | CAUTION | Darknet forum list — list only; do not visit |
| Raklet | http://iwr4usy33opfclmbyemzbmnwwnmmqpqltezpac7fyqqkdv3mabtm6kqd.onion.pet/ | — | CAUTION | onion.pet hidden-service mirror — list only; do not visit |
| Tool / path | https://learnmeabitcoin.com/tools/path/ | — | CONTEXT | Bitcoin tx-path visualizer (misfiled in DARKNET) |

## DATA DUMP

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Have I been pwned | https://haveibeenpwned.com/ | — | KEEP | Public breach-notification locator (named KEEP) |
| DeepSearch | http://xjypo5vzgmo7jca6b322dnqbsdnp3amd24ybx26x5nxbusccjkm4pwid.onion.pet/ | — | CAUTION | onion.pet dump search — list only; do not visit |
| Personal Data Leak Checker | https://cybernews.com/personal-data-leak-check/ | — | CONTEXT | Consumer leak-check (HIBP-adjacent); not in named KEEP set |
| Intelligence X | https://intelx.io/ | — | KEEP | Intelligence X public selector locator (named KEEP) |
| DDoSecrets | https://ddosecrets.com/wiki/Special:AllPages | — | CAUTION | DDoSecrets dump index used as crimeware — list only; do not visit |
| Bloopbase | https://bloopbase.keybase.pub/ | — | CAUTION | Keybase dump index — list only; do not visit |
| Scylla.so | https://scylla.so/ | — | CAUTION | Dump shop — list only; do not visit |
| Leakedpassword.com | https://leakedpassword.com/ | — | CAUTION | Leaked-password search — list only; do not visit |
| DeHashed | https://dehashed.com/ | — | CAUTION | Dump shop — list only; do not visit |
| Snusbase | https://www.snusbase.com/ | — | CAUTION | Dump shop — list only; do not visit |
| Leaked.site | https://www.leaked.site/ | — | CAUTION | Dump shop — list only; do not visit |
| Ashley Madison hacked email checker | https://ashley.cynic.al/ | — | CAUTION | Hacked-dataset search — list only; do not visit |
| Search Ashley Madison Leaked Data | http://checkashleymadison.com/ | — | CAUTION | Hacked-dataset search — list only; do not visit |
| Sony Archives | https://wikileaks.org/sony/emails/ | — | CONTEXT | Published WikiLeaks Sony archive; do not operationalize dump-search |
| Foodora | https://bloopbase.keybase.pub/POPPY/FOODORA/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |
| Liker | https://bloopbase.keybase.pub/POPPY/LIKER/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |
| Ledger | https://bloopbase.keybase.pub/POPPY/LEDGER/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |
| Slack | https://bloopbase.keybase.pub/SLACK/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |
| Weedmaps | https://bloopbase.keybase.pub/POPPY/WEEDMAPS/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |

## INFORMANT

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| WhosaRat.com | https://whosarat.com/ | — | CONTEXT | Vigilante informant list; do not operationalize; no targeting |
| Snitch List | https://web.archive.org/web/20200115091633/http://sniitch.com/all/ | — | CONTEXT | Archived vigilante snitch list; do not operationalize; no targeting |
| Goldensnitches | https://goldensnitches.com/ | — | CONTEXT | Vigilante informant list; do not operationalize; no targeting |

## SEX OFFENDER

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| OSINT list of public sex offenders registers – osintme.com | https://www.osintme.com/index.php/2021/08/31/osint-list-of-public-sex-offenders-registers/ | — | CONTEXT | Third-party blog index of registries; not an official locator |
| NSOPW | https://www.nsopw.gov/ | — | KEEP | US public-record registry locator only — no targeting guidance |
| Sex Offender Registry Websites | https://www.fbi.gov/scams-and-safety/sex-offender-registry | — | KEEP | FBI official registry-locator page — no targeting guidance |
| Sex Offender Korea | https://www.sexoffender.go.kr/indexN.nsc | — | KEEP | ROK official registry locator — no targeting guidance |
| Manitoba Sex Offender | https://www.gov.mb.ca/justice/commsafe/notification/index.html | — | KEEP | Manitoba official public-notification locator — no targeting guidance |
| Convicted Alberta Sex Offender | http://stoppedophiles.ca/convicted-AB.html | — | CONTEXT | Unofficial advocacy list; not a government registry |
| Convicted Sex Offenders List | https://www.ibbclaims.co.uk/site/services/child-abuse-and-trafficking/convicted-offenders/ | — | CONTEXT | UK law-firm marketing page; not a public registry |
| Family Watchdog | https://www.familywatchdog.us/ | — | CONTEXT | Commercial aggregator; not official NSOPW |
| Nigeria Sexual Offenders Registers | https://nsod.naptip.gov.ng/view_cases.php | — | KEEP | NAPTIP official register locator — no targeting guidance |
| Rejestr Sprawców Przestępstw na Tle Seksualnym | https://rps.ms.gov.pl/pl-PL/Public#/home | — | KEEP | Poland MS official registry locator — no targeting guidance |
| Maldives Sex Offender | http://www.offenders.mv/offenders/ | — | KEEP | Maldives official offenders locator — no targeting guidance |

## EXTREMIST / FAR-RIGHT

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Unicorn Riot: Discord Leaks | https://discordleaks.unicornriot.ninja/discord/ | — | CONTEXT | Journalistic Discord-leak archive; do not treat as dump-shop ops |
| Data / DDoSecrets Search | https://search.ddosecrets.com/data/ | — | CAUTION | DDoSecrets dump search — list only; do not visit |
| Parler Archive Search | https://parler.adatascienti.st/research | — | CONTEXT | Research archive of Parler posts |
| Parler Capitol Videos | https://projects.propublica.org/parler-capitol-videos/ | — | CONTEXT | ProPublica journalism project (public) |
| Project Whispers | https://whispers.ddosecrets.com/ | — | CAUTION | DDoSecrets whispers index — list only; do not visit |
| GiveSendGo | https://bloopbase.keybase.pub/LEFTHOOK/GiveSendGo/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |
| Gettr | https://bloopbase.keybase.pub/LEFTHOOK/Gettr/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |
| Utah Gun Exchange | https://bloopbase.keybase.pub/LEFTHOOK/UtahGunExchanges/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |
| 8chan | https://bloopbase.keybase.pub/LEFTHOOK/8chan/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |
| Iron March | https://bloopbase.keybase.pub/LEFTHOOK/IronMarch/index.html | — | CAUTION | Bloopbase dump slice — list only; do not visit |
| 4chansearch.org | https://4chansearch.org/ | — | CONTEXT | Imageboard search locator |
| archived.moe | https://archived.moe/ | — | CONTEXT | Chan archive locator |
| 8chan/8kun QResearch Board Search | https://qresear.ch/ | — | CONTEXT | QResearch board search; conspiracy archive locator |
| Extremist Profiles | https://www.splcenter.org/fighting-hate/extremist-files/individual | — | KEEP | SPLC individual extremist-file profiles (named KEEP) |
| Extremist Groups | https://www.splcenter.org/fighting-hate/extremist-files/groups | — | KEEP | SPLC group extremist-file profiles (named KEEP) |
| Database of suspected terrorists | https://www.nsatt.org/ | — | CONTEXT | Unofficial suspected-terrorist DB; quality unknown; not a gov list |
| TSA No-Fly List | https://www.no-fly-list.com/ | — | CONTEXT | Unofficial no-fly scrape; not TSA official |
| Terrorism Incidents Database | http://smapp.rand.org/rwtid/search_form.php | — | DEAD-OUTDATED | RAND RWTID search form retired; use GTD |
| Global Terrorism Database | https://www.start.umd.edu/gtd/access/ | — | KEEP | START GTD public terrorism-incident database (named KEEP) |
| Sanctions List Search | https://sanctionssearch.ofac.treas.gov/ | — | KEEP | OFAC official sanctions-list search (named KEEP) |
| Trump Twitter Archive | https://www.thetrumparchive.com/ | — | CONTEXT | Public tweet archive (not an extremist corpus) |
| OFAC Sanctioned Search Engine | https://cse.google.com/cse?cx=e96467889fb82b9b0 | — | KEEP | OFAC-oriented Google CSE (named KEEP class) |
| INFORMNAPALM | https://informnapalm.org/db/russian-aggression/#lang=en&page=m_unit | — | CONTEXT | Public RU-aggression OSINT database |
| gogettr | https://pypi.org/project/gogettr/ | — | CONTEXT | Gettr scraper (PyPI); ToS / authorized-target only |
| GUTTR | https://github.com/VVX7/GUTTR | — | CONTEXT | Gettr collection tool (GitHub); authorized-target only |
| FBI Most Wanted Search Engine | https://cse.google.com/cse?cx=1ee952e6584aa91f9 | — | KEEP | Public wanted-person CSE locator |
| Interpol Most Wanted Search Engine | https://cse.google.com/cse?cx=b1746754c83012613 | — | KEEP | Public wanted-person CSE locator |
| Europol Most Wanted Search Engine | https://cse.google.com/cse?cx=f08e8dc2172da1ba8 | — | KEEP | Public wanted-person CSE locator |
| Ironmarch.exposed | https://www.ironmarch.exposed/ | — | CONTEXT | Published Iron March leak site; do not treat as dump-shop ops |

## OTHER

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| cryptome.wikileaks.org | https://cryptome.wikileaks.org/ | — | CONTEXT | Cryptome-via-WikiLeaks document archive; do not operationalize dump-search |
| Nextstrain | https://nextstrain.org/ | — | CONTEXT | Pathogen genomic viz (OOD for this pack); public science locator |

## Counts

| Section | n |
|---------|---|
| THREAT INTEL | 17 |
| MALWARE | 15 |
| HASH RECOVERY | 8 |
| DARKNET | 15 |
| DATA DUMP | 19 |
| INFORMANT | 3 |
| SEX OFFENDER | 11 |
| EXTREMIST / FAR-RIGHT | 29 |
| OTHER | 2 |
| **Total rows** | **119** |

| Disposition | n |
|-------------|---|
| KEEP | 24 |
| CONTEXT | 56 |
| CAUTION | 34 |
| DEAD-OUTDATED | 5 |

Source JSON: `.local/osint4all/groups/07-cyber-caution.json` (`n_links=119`). Majority CONTEXT (56) is correct for this pack. Agents must not visit onion.pet, leak shops, darknet markets, or malware sample repos, and must not write exploits.
