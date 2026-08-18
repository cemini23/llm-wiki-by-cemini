---
title: OSINT4ALL search / domain catalog
type: entity
tags: [osint, catalog, osint4all, k241, search, dorking]
keywords: [OSINT4ALL, search engines, Google CSE, Shodan, Censys, FOFA, crt.sh, SecurityTrails, dorking, public datasets, grep.app, WHOIS, DNS, GrayHatWarfare, onion.pet]
related:
  - sources/osint4all-startme-2026-08-18.md
  - entities/tools/osint4all.md
  - concepts/osint4all-catalog.md
  - entities/tools/mitaka.md
  - sources/eval-multi-wiki-url-revenue-2026-08-18.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @sources/osint4all-startme-2026-08-18.md — ingest source (K241)
- @entities/tools/osint4all.md — hub entity
- @concepts/osint4all-catalog.md — KEEP / CONTEXT / DEAD / NESTED-HUB filing rules

## Raw Concept

OSINT4ALL group **03-search-domain** — unified search, search engines, Google CSEs, dorking, open-directory, source-code, WHOIS, domain/IP/DNS, and public-dataset locators from the L1rEYQ board (mirrored 2026-08-18). One catalog page; not a stub farm. **Wiki column:** `—` = filed in osint-wiki; `cybersecurity-wiki` = shared-territory offense/vuln locator flagged for the cyber wiki.

| Field | Value |
|-------|--------|
| Board group | `03-search-domain` |
| Links (board) | 277 |
| Sections | 10 |
| Source JSON | `.local/osint4all/groups/03-search-domain.json` |
| Filing date | 2026-08-18 |

## Narrative

Search engines, Google CSEs, Shodan / Censys / FOFA / ZoomEye asset locators, crt.sh, SecurityTrails, dorking locators (GHDB + tooling), public datasets, grep.app and source-code search are **KEEP** — the working core of this catalog. **CONTEXT:** sploitus / vulmon / Rapid7 DB are vuln **locators**, never exploit how-to; the `recon…onion.pet` mirror is listed so the board contents are visible — **agents do not visit it**; libgen / megazsearch / btdig are shadow-library / piracy-adjacent (no copyrighted-corpus ingest); Internet Census 2012 has unauthorized-scan (Carna botnet) provenance — reference only. **DEAD-OUTDATED:** MIT PGP keyserver (post-2019 compromise), Alexa (retired 2022), PunkSPIDER (defunct). **NESTED-HUB:** 8 third-party start.me boards under RESOURCES — follow-on hubs, not mass-scrapes. GrayHatWarfare bucket + URL-shortener searches and all scanning / Nmap / secret-scraper rows are KEEP **with an authorized-target-only caveat**; no dump-search or exploit playbooks are written from this page.

## Unified Search

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| IntelTechniques OSINT | https://inteltechniques.com/tools/ | — | KEEP | Bazzell's OSINT toolkit directory — core |
| SynapsInt | https://synapsint.com/ | — | KEEP | Unified people/domain/link search |
| InfoTracer | https://infotracer.com/ | — | KEEP | US people-search (paid / ToS-gated) |
| MetaDefender | https://metadefender.opswat.com/ | — | KEEP | File/URL hash analysis (OPSWAT) |
| Username Search | https://usersearch.org/ | — | KEEP | Username search |
| SpyTox | https://www.spytox.com/ | — | KEEP | Phone/people lookup (paid) |
| Effect Group | https://effectgroup.io/ | — | KEEP | People lookup aggregator (status unverified) |
| osrframework | https://pypi.org/project/osrframework/ | — | KEEP | Python OSINT framework (osrframework) |
| Google Custom Search | https://cse.google.com/cse?cx=017648920863780530960:lddgpbzqgoi | — | KEEP | CSE — IntelTechniques google.com dork cx |
| OSINT Search Engine | https://cse.google.com/cse/publicurl?cx=006290531980334157382:qcaf4enph7i | — | KEEP | OSINT-focused CSE |
| LinkScope | https://github.com/AccentuSoft/LinkScope_Client | — | KEEP | Link-analysis client (GitHub) |
| IOA | https://www.io-archive.org/ | — | KEEP | Open-archive locator (status unverified) |
| Criminal IP | https://www.criminalip.io/ | — | KEEP | ASM / asset-intelligence search (Censys-class) |

## Search Engines

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| IntelTechniques Search Engine | https://inteltechniques.com/tools/Search.html | — | KEEP | Custom search tool page (Bazzell) |
| Google Advanced Search | https://www.google.com/advanced_search | — | KEEP | Advanced search params |
| Searx | https://searx.info/ | — | KEEP | Privacy metasearch |
| Bing | https://www.bing.com/ | — | KEEP | Web index |
| Yandex | https://yandex.com/ | — | KEEP | RU/CIS index |
| MetaGer: Privacy Protected Search | https://metager3.de/en/ | — | KEEP | Privacy metasearch (DE) |
| Duck Duck Go | https://duckduckgo.com/ | — | KEEP | Privacy metasearch |
| Search Engines Index | https://www.searchenginesindex.com/ | — | KEEP | Search-engine directory |
| carrot2 | https://search.carrot2.org/#/search/web | — | KEEP | Clustering search (Carrot2) |
| Qwant | https://www.qwant.com/ | — | KEEP | Privacy index (EU) |
| Startpage | https://startpage.com/ | — | KEEP | Google-proxy privacy search |
| Mailing List Search | https://cse.google.com/cse/publicurl?cx=013991603413798772546:sipriovnbxq | — | KEEP | Mailing-list dork CSE |
| swisscows | https://swisscows.com/ | — | KEEP | Family-safe privacy search |
| Crossref | https://search.crossref.org/ | — | KEEP | Scholarly metadata search |
| Brave Search | https://search.brave.com/ | — | KEEP | Privacy index (independent) |
| Mojeek | https://www.mojeek.com/ | — | KEEP | Independent-index search |
| Yahoo Search | https://search.yahoo.com/ | — | KEEP | Legacy web index |
| Baidu | https://www.baidu.com/ | — | KEEP | CN index |
| Ecosia | https://www.ecosia.org/ | — | KEEP | Bing-based green search |
| Dogpile | https://www.dogpile.com/ | — | KEEP | Metasearch aggregator |
| Zoo Search | https://www.metacrawler.com/ | — | KEEP | Metasearch (MetaCrawler) |
| App Store and iTunes search engine | https://fnd.io/ | — | KEEP | App Store / iTunes search |
| Ask | https://www.search.ask.com/ | — | KEEP | Legacy Q&A index |
| ZorexEye | http://zorexeye.com/ | — | KEEP | Legacy metasearch (availability unverified) |
| Yassen.com | http://yassen.com/ | — | KEEP | Legacy search (availability unverified) |
| Flippity | https://www.flippity.com/ | — | KEEP | Google-Sheets quiz/game generator (odd inclusion — misc utility) |
| keys.openpgp.org | https://keys.openpgp.org/ | — | KEEP | PGP key lookup (current) |
| MIT PGP Key Server | https://pgp.mit.edu/ | — | DEAD-OUTDATED | MIT PGP keyserver effectively decommissioned after 2019 compromise — use keys.openpgp.org |
| Ipse.io | https://www.ipse.io/ | cybersecurity-wiki | CONTEXT | IPFS/decentralized-content search (may surface dark-content links) — list-only |
| Ipfs-search.com | https://ipfs-search.com/#/search | — | KEEP | IPFS content search |
| Debate.cards | http://debate.cards/ | — | KEEP | Argument/debate search (status unverified) |
| Argumentsearch.com | http://argumentsearch.com/ | — | KEEP | Argument database search (status unverified) |
| Meganzsearch.com | https://www.meganzsearch.com/ | — | CONTEXT | Mega.nz file-link search — piracy-adjacent; list-only |
| Engine.presearch.org | https://engine.presearch.org/ | — | KEEP | Presearch metasearch |
| Blockscan.com | https://blockscan.com/ | — | KEEP | Blockchain address search |
| Publc.com | https://publc.com/ | — | KEEP | Public search locator (status unverified) |
| GoPit Search Engine - Home | https://www.gopit.com/socialsearch/index.php?type=Social | — | KEEP | Social search engine |
| The best document search engine | http://www.doc-txt.com/ | — | KEEP | Document search |
| CachedViews.com | https://cachedviews.com/ | — | KEEP | Cached-page viewer |
| MAC Address Lookup | https://maclookup.app/ | — | KEEP | MAC OUI vendor lookup |
| sploitus | https://sploitus.com/ | cybersecurity-wiki | CONTEXT | Vuln/exploit locator — not exploit how-to |
| https://vulmon.com/ | https://vulmon.com/ | cybersecurity-wiki | CONTEXT | Vuln locator — not exploit how-to |
| Vulnerability & Exploit Database | https://www.rapid7.com/db/ | cybersecurity-wiki | CONTEXT | Vuln/exploit locator (Rapid7 DB) — not exploit how-to |
| Recon | http://recon222tttn4ob7ujdhbn3s4gjre7netvzybuvbq2bcqwltkiqinhad.onion.pet/ | cybersecurity-wiki | CONTEXT | onion.pet mirror of a recon board — know it exists; do NOT visit |
| Google & Bing | https://one-plus.github.io/GoogleBing | — | KEEP | GitHub-hosted Google+Bing helper |
| Bookmarks | https://one-plus.github.io/Bookmarks | — | KEEP | GitHub-hosted bookmark tool |
| Boardreader - Forum Search | https://boardreader.com/ | — | KEEP | Forum search |
| Libgen.rs | http://libgen.rs/ | — | CONTEXT | Shadow library — do not ingest copyrighted corpora |
| Stacksearch | https://stacksear.ch/ | — | KEEP | Stack Exchange search |
| SearchTempest | https://www.searchtempest.com/ | — | KEEP | Craigslist/eBay multi-location search |
| 2lingual | https://2lingual.com/ | — | KEEP | Bilingual query search |
| SEQE - Search Engines Query Engine | https://seqe.me/ | — | KEEP | Multi-engine query aggregator |
| Milled | https://milled.com/search | — | KEEP | Email-marketing archive search |
| btdig | https://btdig.com/ | — | CONTEXT | Torrent index search — piracy-adjacent; list-only |
| Osint Open Source Projects | https://awesomeopensource.com/projects/osint | — | KEEP | OSINT project directory (also under RESOURCES) |
| Monster Crawler Search | http://monstercrawler.com/ | — | KEEP | Legacy metasearch (availability unverified) |
| Arabo.com | http://arabo.com/ | — | KEEP | Legacy search (availability unverified) |
| Google Scholar | https://scholar.google.com/ | — | KEEP | Scholarly search |
| Million Short | https://millionshort.com/ | — | KEEP | Search that strips top domains |
| BeVigil | https://bevigil.com/ | — | KEEP | Mobile-app asset/API-key search — authorized-target only |
| WordPress.com | https://en.search.wordpress.com/ | — | KEEP | WordPress content search |
| Octosearch.dootech.com | https://octosearch.dootech.com/ | — | KEEP | Site-asset search (status unverified) |
| Search craigslist | http://searchcraigslist.org/ | — | KEEP | Craigslist search helper |
| Public AWS S3 & Azure Search | https://buckets.grayhatwarfare.com/ | — | KEEP | Public S3/Azure bucket locator — authorized-target only |
| Public Buckets | https://osint.sh/buckets/ | — | KEEP | Public bucket locator — authorized-target only |
| URL Shorteners Search | https://shorteners.grayhatwarfare.com/ | — | KEEP | URL-shortener link locator |
| Mywoodle.com | https://mywoodle.com/ | — | KEEP | Web-tools locator (status unverified) |
| Search Atlas | https://searchatlas.org/ | — | KEEP | Search locator (status unverified) |
| Google to search profiles on Stack Overflow | https://recruitin.net/stackoverflow.php | — | KEEP | Google → StackOverflow profile search |
| Binparcel.com | https://binparcel.com/ | — | KEEP | Payment BIN lookup (card-forensics context) |

## Google CSE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Homepage Search Engine | https://cse.google.com/cse?cx=005797772976587943970:3tu7im1-rdg#gsc.tab=0 | — | KEEP | Homepage-index dork CSE |
| Amazon Cloud Search Engine | https://cse.google.com/cse?cx=005797772976587943970:g-6ohngosio#gsc.tab=0 | — | KEEP | Amazon/cloud dork CSE |
| Google CSE instances Search Engine | https://cse.google.com/cse?cx=009462381166450434430:vggeu3dhhgg#gsc.tab=0 | — | KEEP | CSE-instances dork CSE |
| Robots.txt Search Engine | https://cse.google.com/cse?cx=013991603413798772546:zu7epjqvunu | — | KEEP | robots.txt dork CSE |
| Short URL Search Engine | https://cse.google.com/cse?cx=017261104271573007538:magh-vr6t6g#gsc.tab=0 | — | KEEP | Short-URL dork CSE |
| Wikispaces Search Engine | https://cse.google.com/cse/publicurl?cx=005797772976587943970:afbre9pr2ly | — | KEEP | Wikispaces dork CSE (legacy) |
| Dog Bites Search Engine | https://cse.google.com/cse?cx=partner-pub-8216357153102971:3267723418 | — | KEEP | Dog-bites dork CSE |
| Google Domain Hacker | https://cse.google.com/cse/publicurl?cx=005797772976587943970:ca2hiy6hmri | — | KEEP | Domain-hacker dork CSE |
| Google Drive Folder Search Engine | https://cse.google.com/cse/publicurl?cx=013991603413798772546:nwzqlcysx_w | — | KEEP | Drive-folder dork CSE |
| Chrome Extension Archive Search Engine | https://cse.google.com/cse/publicurl?cx=000501358716561852263:h-5uyshsclq | — | KEEP | Chrome-extension archive CSE |
| Github with Awesome-List Search Engine | https://cse.google.com/cse/publicurl?cx=017261104271573007538:fqn_jyftcdq | — | KEEP | GitHub awesome-list CSE |
| Better Chrome Web Store Search Engine | https://cse.google.com/cse/publicurl?cx=006205189065513216365:pn3lumi80ne | — | KEEP | Chrome-Web-Store CSE |
| App Store Custom Search Engine | https://cse.google.com/cse/publicurl?cx=006205189065513216365:aqogom-kfne | — | KEEP | App Store CSE |
| \*.Google.com Hack Attack | https://cse.google.com/cse/publicurl?cx=017648920863780530960:lddgpbzqgoi | — | KEEP | google.com subdomain dork CSE |
| Search by FileType | https://cse.google.com/cse/publicurl?cx=013991603413798772546:mu-oio3a980 | — | KEEP | Filetype dork CSE |
| Search Engine Finder | https://cse.google.com/cse?cx=016621447308871563343:nyvaorurd5l | — | KEEP | CSE-finder dork CSE |
| Mindmap Search Engine | http://cse.google.com/cse?cx=013991603413798772546:gj6rx9spox8#gsc.tab=0 | — | KEEP | Mindmap dork CSE |
| Slack/Discord/Zoom Invites Search | https://cse.google.com/cse?cx=8e26eca532ec2cba3 | — | KEEP | Public invite-link dork CSE (Slack/Discord/Zoom) |
| Cloud Bucket Search Engine | https://cse.google.com/cse?cx=d80f8518b11b1438e | — | KEEP | Cloud-bucket dork CSE — authorized-target only |

## Resources

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| OH SHINT! Welcome Aboard | https://ohshint.gitbook.io/ | — | KEEP | OSINT gitbook hub |
| The Ultimate OSINT Collection | https://start.me/p/DPYPMz/the-ultimate-osint-collection | — | NESTED-HUB | Third-party start.me board — follow-on hub; not mass-scraped here |
| OSINT Resources in Canada | https://start.me/p/aLe0vp/osint-resources-in-canada | — | NESTED-HUB | Third-party start.me board — follow-on hub; not mass-scraped here |
| Nixintel's OSINT Resource List | https://start.me/p/rx6Qj8/nixintel-s-osint-resource-list | — | NESTED-HUB | Third-party start.me board — follow-on hub; not mass-scraped here |
| FAROS OSINT Resources | https://start.me/p/1kvvxN/faros-osint-resources | — | NESTED-HUB | Third-party start.me board — follow-on hub; not mass-scraped here |
| AML Toolbox | https://start.me/p/rxeRqr/aml-toolbox | — | NESTED-HUB | Third-party start.me board — follow-on hub; not mass-scraped here |
| TI | https://start.me/p/rxRbpo/ti | — | NESTED-HUB | Third-party start.me board — follow-on hub; not mass-scraped here |
| TOOLKIT | https://start.me/p/W1AXYo/toolkit | — | NESTED-HUB | Third-party start.me board — follow-on hub; not mass-scraped here |
| Trouble Fake | https://start.me/p/QRQb0O/trouble-fake | — | NESTED-HUB | Third-party start.me board — follow-on hub; not mass-scraped here |
| OSINT Is A State Of Mind | https://medium.com/secjuice/osint-as-a-mindset-7d42ad72113d | — | KEEP | OSINT mindset / tradecraft article (Secjuice) |
| sinwindie/OSINT | https://github.com/sinwindie/OSINT | — | KEEP | Curated OSINT list (sinwindie) |
| New Online Investigation (OSINT) Resources – IntelTechniques Blog | https://inteltechniques.com/blog/2019/04/09/new-online-investigation-osint-resources/ | — | KEEP | Bazzell OSINT-resource post |
| Technisette | https://www.technisette.com/p/home | — | KEEP | OSINT blog (Technisette) |
| OSINT Framework | https://osintframework.com/ | — | KEEP | Core OSINT framework tree |
| jivoi/awesome-osint | https://github.com/jivoi/awesome-osint | — | KEEP | Curated awesome-osint list |
| START CARING STOP SHARING | https://medium.com/@Dutchosintguy/start-caring-stop-sharing-9c108d957b2c | — | KEEP | OPSEC article (DutchOsintGuy) |
| Osint Curious OSINT Resource List | https://docs.google.com/document/d/14li22wAG2Wh2y0UhgBjbqEvZJCDsNZY8vpUAJ_jJ5X8/edit | — | KEEP | OsintCurious resource doc (Google Doc) |
| OSINT Tools | https://www.osinttechniques.com/osint-tools.html | — | KEEP | OSINT tool list (OSINTTechniques) |
| OSINT tools for investigating websites | https://www.aware-online.com/en/osint-tools/website-tools/ | — | KEEP | Website-investigation tool list |
| Shodan Cheat Sheet | https://thedarksource.com/shodan-cheat-sheet/ | — | KEEP | Shodan query cheat sheet |
| Week in OSINT | https://sector035.nl/articles/category:week-in-osint | — | KEEP | Weekly OSINT newsletter (Sector035) |
| Osint.team | https://osint.team/ | — | KEEP | OSINT team portal |
| QueryTool | https://github.com/oryon-osint/querytool | — | KEEP | OSINT query toolkit (QueryTool) |
| Investigating the source code of a website | https://www.aware-online.com/en/osint-tutorials/investigating-the-source-code-of-a-website/ | — | KEEP | Website source-code investigation tutorial |
| Find open FTP Servers | https://www.aware-online.com/en/osint-tutorials/find-open-ftp-servers/ | — | KEEP | Open-FTP finding tutorial — authorized-target only |
| Choose your wallet | https://bitcoin.org/en/choose-your-wallet | — | KEEP | Crypto wallet reference for blockchain OSINT |
| 10 Minute Tips | https://osintcurio.us/10-minute-tips/ | — | KEEP | OsintCurious 10-min tips |
| Webint Master | https://webintmaster.com/ | — | KEEP | Webint training/resources |
| DFIR Diva | https://dfirdiva.com/hooked-on-osint/ | — | KEEP | DFIR Diva OSINT series |
| Boolean Strings \\| Tools | https://booleanstrings.com/tools/ | — | KEEP | Boolean dorking tools (recruiting OSINT) |
| osintme.com | https://www.osintme.com/ | — | KEEP | OSINT blog (osintme) |
| Jake Creps | https://jakecreps.com/ | — | KEEP | OSINT blog (Jake Creps) |
| reKnowledge | https://www.reknowledge.tech/ | — | KEEP | OSINT reKnowledge portal (status unverified) |
| @Ivan30394639 OSINT tools collection | https://cipher387.github.io/osint_stuff_tool_collection/ | — | KEEP | cipher387 OSINT tool collection |
| The Top 132 Osint Open Source Projects | https://awesomeopensource.com/projects/osint | — | KEEP | OSINT project directory (also under RESOURCES) |
| 30 best OSINT extensions for Google Chrome – osintme.com | https://www.osintme.com/index.php/2021/06/30/30-best-osint-extensions-for-google-chrome/ | — | KEEP | Chrome OSINT extension roundup |
| Where Can I Find... - Free DFIR Related Training | https://freetraining.dfirdiva.com/where-can-i-find | — | KEEP | Free DFIR training locator |
| Awesome Deblurring | https://github.com/subeeshvasu/Awesome-Deblurring | — | KEEP | Image deblurring list (forensics) |
| OSINT.SH | https://osint.sh/ | — | KEEP | Core OSINT toolkit (OSINT.SH) |
| OSINT Techniques | https://www.osinttechniques.com/ | — | KEEP | OSINT Techniques site |
| OSINT aka Atvirųjų šaltinių žvalgyba | https://blog.parakomanai.lt/osint-387e80bdc901 | — | KEEP | LT-language OSINT writeup (parakomanai) |
| CTI & OSINT Online Resources | https://docs.google.com/spreadsheets/d/1klugQqw6POlBtuzon8S0b18-gpsDwX-5OYRrB7TyNEw/edit#gid=0 | — | KEEP | CTI & OSINT online resource sheet |
| Emsisoft Decryptor for Avaddon | https://www.emsisoft.com/ransomware-decryption-tools/avaddon | — | KEEP | Defensive ransomware decryptor (Emsisoft) |
| hwosint (@harrywald80) | https://twitter.com/harrywald80 | — | KEEP | Practitioner follow (hwosint) |
| Stefanie Proto 🔍 (@sprp77) | https://twitter.com/sprp77 | — | KEEP | Practitioner follow (sprp77, CSE builder) |
| Awesomelists.top | http://awesomelists.top/ | — | KEEP | Awesome-list search |
| GitHub Awesome Search | https://github.motakasoft.com/awesome/ | — | KEEP | GitHub awesome-list search |
| Ph055a OSINT\_Collection | https://github.com/Ph055a/OSINT_Collection | — | KEEP | OSINT collection repo (Ph055a) |
| MetaOSINT | https://metaosint.github.io/ | — | KEEP | MetaOSINT — opens a URL across many tools at once |
| Osint.support | https://osint.support/ | — | KEEP | OSINT support portal |
| Sprp77/My-Google-CSE | https://github.com/Sprp77/My-Google-CSE/blob/master/List%201 | — | KEEP | Sprp77 CSE / dork list |
| How to Build an OSINT Super Machine for People Surveillance and Sourcing | https://outline.com/GZbkZA | — | KEEP | People-surveillance / sourcing tradecraft article (Outline mirror) |
| How to find anyone with an advanced LinkedIn People Search | https://nubela.co/blog/how-to-find-anyone-with-an-advanced-linkedin-people-search/ | — | KEEP | LinkedIn people-search tradecraft — LinkedIn ToS caveat |

## Dorking

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Google Dork Cheatsheet | https://github.com/robyfirnandoyusuf/Google-Dork-Cheatsheet | — | KEEP | Google dork cheat sheet |
| Google Hacking Database | https://www.exploit-db.com/google-hacking-database | cybersecurity-wiki | KEEP | GHDB dork-query locator — dork locator, not payload |
| theHarvester | https://pypi.org/project/theHarvester/ | cybersecurity-wiki | KEEP | Email/subdomain gatherer — authorized-target only |
| metagoofil | https://github.com/opsdisk/metagoofil | cybersecurity-wiki | KEEP | Metadata extraction from public docs — authorized-target only |
| webdork | https://github.com/HACKE-RC/webdork | cybersecurity-wiki | KEEP | Dork automation — authorized-target only |
| ATSCAN | https://github.com/AlisamTechnology/ATSCAN | cybersecurity-wiki | KEEP | Dorking/scanner automation — authorized-target only |
| pagodo | https://github.com/opsdisk/pagodo | cybersecurity-wiki | KEEP | Google-dork pagination bot — authorized-target only |

## Open Directory

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| FilePhish | https://cartographia.github.io/FilePhish/ | — | KEEP | File-extension phishing-site builder (defensive / auth testing) |
| Open Directory Finder | https://odfinder.github.io/ | — | KEEP | Open-directory finder |
| Filetype search tool | https://www.aware-online.com/en/osint-tools/filetype-search-tool/ | — | KEEP | Filetype search tool |
| Opendirsearch.abifog.com | https://opendirsearch.abifog.com/ | — | KEEP | Open-directory search |
| Archive-it.org | https://archive-it.org/ | — | KEEP | Internet Archive web-archiving service |
| Odcrawler.xyz | https://odcrawler.xyz/ | — | KEEP | Open-directory crawler |
| Google Docs CSE | https://cse.google.com/cse/publicurl?cx=013991603413798772546:rse-4irjrn8#gsc.tab=0 | — | KEEP | Google-Docs dork CSE |
| Documents Search Engine | https://cse.google.com/cse?cx=e6756edc507bcfa91 | — | KEEP | Documents dork CSE |
| Cybersec Documents Search Engine | https://cse.google.com/cse?cx=013991603413798772546:ekjmizm8vus#gsc.tab=0 | — | KEEP | Cybersec-docs dork CSE |
| GoogleDrive Search Engine | https://cse.google.com/cse?cx=c64ba311eb8c31896 | — | KEEP | GoogleDrive dork CSE |
| SlideShare Search Engine | https://cse.google.com/cse?cx=465eeeb114c7f523f | — | KEEP | SlideShare dork CSE |
| Document Search | https://one-plus.github.io/DocumentSearch | — | KEEP | GitHub-hosted doc search |
| FONETASK | http://fonetask.com/ | — | KEEP | Document search (status unverified) |
| Web archive search tool | https://www.aware-online.com/osint-tools/web-archive-search-tool/ | — | KEEP | Web-archive search tool |
| Pdfsearch.io | https://www.pdfsearch.io/ | — | KEEP | PDF search |
| awesome-public-datasets | https://github.com/awesomedata/awesome-public-datasets | — | KEEP | Curated public datasets list |
| Drivesearch.kwebpia.net | http://drivesearch.kwebpia.net/ | — | KEEP | Public Drive search (status unverified) |
| Filepursuit.com | https://filepursuit.com/ | — | KEEP | Public file search |
| Filechef.com | https://www.filechef.com/ | — | KEEP | Public file search |
| Open Directory Search | http://eyeofjustice.com/od/ | — | KEEP | Open-directory search |
| Mamont's open FTP Index | https://www.mmnt.net/ | — | KEEP | Open FTP index locator — authorized-target only |
| LENDX | http://lendx.org/ | — | KEEP | Document-archive locator (status unverified) |
| Direct Download Almost Anything | https://ewasion.github.io/opendirectory-finder/ | — | KEEP | Open-directory finder (Ewasion) |

## Source Codes

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Pastes Search Engine | https://cse.google.com/cse?cx=661713d0371832a02 | — | KEEP | Pastes dork CSE |
| Pastes Search Engine 2 | https://cse.google.com/cse?cx=006896442834264595052:fawrl1rug9e | — | KEEP | Pastes dork CSE 2 |
| GitHub Search Engine | https://cse.google.com/cse?cx=1b053c8ec746d6611 | — | KEEP | GitHub dork CSE |
| Source Code Search Engine | https://publicwww.com/ | — | KEEP | HTML source / inline-string search |
| Google to search profiles on GitHub | https://recruitin.net/github.php | — | KEEP | Google → GitHub profile search |
| Grep.app | https://grep.app/ | — | KEEP | Code search — handoff-confirmed KEEP |
| NerdyData | https://www.nerdydata.com/ | — | KEEP | HTML-source search |
| Paste Search | https://psbdmp.ws/ | — | KEEP | Pastebin dump locator — may surface accidental leaks; authorized-target only |
| GitHub Code Search | https://github.com/search | — | KEEP | GitHub code search |
| Bitbucket Repo Search | https://bitbucket.org/repo/all/ | — | KEEP | Bitbucket repo search |
| Shhgit | https://github.com/eth0izzle/shhgit | cybersecurity-wiki | KEEP | GitHub secret scanner — authorized-target only |
| git-hound | https://github.com/tillson/git-hound | cybersecurity-wiki | KEEP | GitHub secret scanner — authorized-target only |
| Webfinery \\| Source Code Search | https://webfinery.com/search | — | KEEP | Source-code search (Webfinery) |
| Online IDE and Paste Search Engine | https://redhuntlabs.com/online-ide-search | — | KEEP | Online-IDE / paste search |
| searchcode | https://searchcode.com/ | — | KEEP | Source-code search |
| Sourcegraph | https://about.sourcegraph.com/ | — | KEEP | Code search platform |
| Awesome Open Source | https://awesomeopensource.com/ | — | KEEP | Open-source project directory |
| Awesome-indexed | http://awesome-indexed.mathew-davies.co.uk/ | — | KEEP | Awesome-list index |
| Awesomelists.top | http://dev.awesomelists.top/#/ | — | KEEP | Awesome-list search (dev) |
| Zen | https://github.com/s0md3v/Zen | — | KEEP | Email OSINT framework (s0md3v) |
| GitDorker | https://github.com/obheda12/GitDorker | cybersecurity-wiki | KEEP | GitHub dorking automation — authorized-target only |

## Whois

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| WHOIS Service | https://whoismind.com/ | — | KEEP | WHOIS search |
| Whois Search | https://webwhois.verisign.com/webwhois-ui/index.jsp?language=en_US | — | KEEP | Verisign WHOIS (registrar-official) |
| Who.is | https://who.is/ | — | KEEP | WHOIS + hostinfo |
| Whoxy | https://www.whoxy.com/ | — | KEEP | WHOIS + history (paid tiers) |
| Whois History | https://osint.sh/whoishistory/ | — | KEEP | WHOIS history lookup |

## Domain / IP / DNS

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| domainbigdata | https://domainbigdata.com/ | — | KEEP | Domain registration analytics |
| Domain Codex | https://www.domaincodex.com/search.php | — | KEEP | Domain WHOIS/expiry search (dup row) |
| dnslytics | https://dnslytics.com/ | — | KEEP | DNS/IP footprint search |
| SecurityTrails | https://securitytrails.com/ | — | KEEP | DNS/host history — handoff-confirmed KEEP |
| Shodan | https://shodan.io | — | KEEP | Internet device search — handoff-confirmed KEEP |
| Internetdb.shodan.io | https://internetdb.shodan.io/ | — | KEEP | Passive Shodan data API |
| GreyNoise Intelligence | https://www.greynoise.io/viz/ | — | KEEP | IP noise / scan classification |
| FOFA | https://fofa.so/ | — | KEEP | CN asset search (Censys-class) |
| zoomeye | https://www.zoomeye.org/ | — | KEEP | CN asset search (ZoomEye) |
| Censys | https://censys.io/domain | — | KEEP | Cert/device search (Censys) |
| ViewDNS.info | https://viewdns.info/ | — | KEEP | DNS / history toolkit (dup row) |
| Internet Census 2012 | http://census2012.sourceforge.net/paper.html | — | CONTEXT | Carna botnet-era dataset — unauthorized-scan provenance; reference only, do not operationalize |
| ONYPHE | https://www.onyphe.io/ | — | KEEP | Internet exposure data (ONYPHE) |
| IPLeak | https://ipleak.net/ | — | KEEP | IP / leak self-test |
| Censys Certificates | https://censys.io/certificates | — | KEEP | Certificate transparency search |
| Censys IPv4 | https://censys.io/ipv4 | — | KEEP | IPv4 device search |
| ViewDNS.info | https://viewdns.info/ | — | KEEP | DNS / history toolkit (dup row) |
| Robtex | https://www.robtex.com/ | — | KEEP | DNS/IP relationship graph |
| Website search tool | https://www.aware-online.com/en/osint-tools/website-search-tool/ | — | KEEP | Website search tool |
| Wappalyzer | https://www.wappalyzer.com/lookup/ | — | KEEP | Tech-stack fingerprint |
| photon | https://pypi.org/project/photon/ | — | KEEP | Fast web crawler lib (photon) |
| Technology Lookup | https://osint.sh/stack/ | — | KEEP | Tech-stack lookup |
| BuiltWith Technology Lookup | https://builtwith.com/ | — | KEEP | Tech-stack lookup (BuiltWith) |
| NMAP Online | https://osint.sh/nmap/ | — | KEEP | Nmap scan locator — authorized-target only |
| Nmap Checker Tool | https://shadowcrypt.net/tools/nmap | — | KEEP | Nmap scan locator — authorized-target only |
| Free online network tools | https://centralops.net/co/ | — | KEEP | Free online network tools |
| Google Transparency Report | https://transparencyreport.google.com/https/certificates | — | KEEP | Google CT-log search |
| Certificate Search | https://osint.sh/crt/ | — | KEEP | Certificate search |
| CRT | https://crt.sh/ | — | KEEP | Certificate transparency — handoff-confirmed KEEP |
| LeakIX | https://leakix.net/ | — | KEEP | Internet exposure / leak index — authorized-target assessment only |
| DomainWatch | https://domainwat.ch/ | — | KEEP | Domain cert / watch lookup |
| URL and website scanner | https://urlscan.io/ | — | KEEP | URL sandbox / scan |
| dnsdumpster | https://dnsdumpster.com/ | — | KEEP | DNS mapping / recon |
| Domain Codex | https://www.domaincodex.com/search.php | — | KEEP | Domain WHOIS/expiry search (dup row) |
| SimilarWeb | https://www.similarweb.com/ | — | KEEP | Traffic analytics |
| Alexa | https://www.alexa.com/siteinfo | — | DEAD-OUTDATED | Alexa Rank service retired May 2022 |
| Website Information | https://one-plus.github.io/WebsiteInformation | — | KEEP | GitHub-hosted site-info tool |
| IP search - Network Entity Reputation Database | https://nerd.cesnet.cz/nerd/ips/ | — | KEEP | Network entity reputation (CESNET NERD) |
| Reverse Domain | https://osint.sh/domain/ | — | KEEP | Reverse domain lookup |
| Poodle Check | https://osint.sh/poodle/ | — | KEEP | TLS POODLE check — authorized-target only |
| Heartbleed Check | https://osint.sh/heartbleed/ | — | KEEP | TLS Heartbleed check — authorized-target only |
| DNS History Lookup | https://osint.sh/dnshistory/ | — | KEEP | DNS history lookup |
| Subdomain Finder | https://osint.sh/subdomain/ | — | KEEP | Subdomain finder |
| Reverse IP Lookup | https://osint.sh/reverseip/ | — | KEEP | Reverse IP lookup |
| Reverse Google Adsense | https://osint.sh/adsense/ | — | KEEP | Reverse AdSense lookup (site-owner correlation) |
| Reverse Google Analytics | https://osint.sh/analytics/ | — | KEEP | Reverse Analytics lookup (site-owner correlation) |
| Reverse MX Record | https://osint.sh/reversemx/ | — | KEEP | Reverse MX lookup |
| IP GEO Location Lookup | https://osint.sh/ip/ | — | KEEP | IP geo lookup |
| IANA — Root Zone Database | https://www.iana.org/domains/root/db | — | KEEP | Root-zone registry (official) |
| Punkspider | https://punkspider.org/ | cybersecurity-wiki | DEAD-OUTDATED | Mass webapp vuln-scan project defunct (offline since ~2015) |
| metabigor | https://github.com/j3ssie/metabigor | — | KEEP | Recon CLI (metabigor) |
| Spyse | https://spyse.com/ | — | KEEP | Cybersec data search (status unverified) |

## Datasets

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Data Sets - OH SHINT | https://ohshint.gitbook.io/oh-shint-its-a-blog/osint-web-resources/data-sets | — | KEEP | OH SHINT dataset index |
| Datasetsearch.research.google.com | https://datasetsearch.research.google.com/ | — | KEEP | Google Dataset Search |
| Kaggle | https://www.kaggle.com/search?q= | — | KEEP | Kaggle dataset search |
| Databasd | https://databasd.com/ | — | KEEP | Database / dataset search |
| Data.gov | https://www.data.gov/ | — | KEEP | US open-data portal |
| data.world | https://data.world/ | — | KEEP | Open-data community |
| BigQuery public datasets | https://cloud.google.com/bigquery/public-data/ | — | KEEP | BigQuery public datasets |
| Ariadne2.isti.cnr.it | http://ariadne2.isti.cnr.it/ | — | KEEP | EU digital-library datasets (status unverified) |
| DSC Data Science Search Engine | https://www.datasciencecentral.com/page/search | — | KEEP | Data-science content search |
| Datasetlist.com | https://www.datasetlist.com/ | — | KEEP | Dataset directory |
| Search Datasets | https://datahub.io/search | — | KEEP | Open-data hub search |
| OpenData by Socrata | https://opendata.socrata.com/ | — | KEEP | Socrata open-data portal |
| Opensanctions.org | https://opensanctions.org/ | — | KEEP | Sanctions / ownership dataset — core for AML |
| FiveThirtyEight | https://fivethirtyeight.com/?s= | — | KEEP | Data-journalism datasets (FiveThirtyEight) |

## Counts

| Section | n |
|---------|---|
| Unified Search | 13 |
| Search Engines | 70 |
| Google CSE | 19 |
| Resources | 53 |
| Dorking | 7 |
| Open Directory | 23 |
| Source Codes | 21 |
| Whois | 5 |
| Domain / IP / DNS | 52 |
| Datasets | 14 |
| **Total rows** | **277** |

| Disposition | n |
|-------------|---|
| KEEP | 257 |
| CONTEXT | 9 |
| NESTED-HUB | 8 |
| CAUTION | 0 |
| DEAD-OUTDATED | 3 |

## Snippets

> Group `03-search-domain`: 277 links across 10 sections (UNIFIED SEARCH, SEARCH ENGINES, GOOGLE CSE, RESOURCES, DORKING, OPEN DIRECTORY, SOURCE CODES, WHOIS, DOMAIN / IP / DNS, DATASET). [Source: `.local/osint4all/groups/03-search-domain.json` / OSINT4ALL start.me L1rEYQ (retrieved 2026-08-18)]

Agents must not visit the `recon…onion.pet` link and must not write exploit or dump-search playbooks from this page. GrayHatWarfare / bucket / Nmap / secret-scanner rows are authorized-target-only locators.
