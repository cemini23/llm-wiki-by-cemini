---
title: OSINT4ALL — public records / government catalog
type: entity
tags: [osint4all, k241, records, genealogy]
keywords: [PACER, CourtListener, OpenCorporates, ICIJ, Companies House, SEDAR, MuckRock, LittleSis, OCCRP, FamilySearch, SSDI, voter rolls, BlueLeaks]
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
- @concepts/osint4all-catalog.md — KEEP / CONTEXT filing rules
- @sources/osint4all-startme-2026-08-18.md — start.me ingest (K241)

## Raw Concept

OSINT4ALL group **06-records-gov** — public-records, government, Canadian gov/corp, voter databases, business, finance, and police/LE locator bookmarks from the L1rEYQ board (mirrored 2026-08-18). One catalog page; not a stub farm. **No private Barone pedigree** anywhere. Atto methodology uses public genealogy/registry locators only.

| Field | Value |
|-------|--------|
| Board group | `06-records-gov` |
| Links (board) | 241 |
| Sections | 9 |
| Source JSON | `.local/osint4all/groups/06-records-gov.json` |
| Filing date | 2026-08-18 |

## Narrative

Freedom-of-information and public-registry locators (courts, corporations, FOIA desks, genealogy indexes, Canadian ATI/open data) are **KEEP** for authorized OSINT / Atto methodology. Voter custom-search engines and state voter-lookup sites are **KEEP as public-record locators with a hard caveat** — they are not a voter-harassment playbook. Police-misconduct databases and transparency projects are **CONTEXT** (journalistic public records); leak dumps (**BlueLeaks**, WikiLeaks email/ICE mirrors, Keybase ACAB dump mirrors) are **CONTEXT** — listed so the operator can see what the board contained; agents do not open dumps and do not write targeting or dump-search how-to. No Italian archive URLs appear in this group; Canadian corporate + LAC/BAnQ stay **KEEP (atto+osint)**.

**Disposition totals:** KEEP 186 · CONTEXT 55 · board rows 241 · unique hrefs 239.

## Catalog

### PUBLIC RECORDS

| Tool | URL | Disposition | Note |
|------|-----|-------------|------|
| JudyRecords | https://www.judyrecords.com/ | KEEP | core public-records / corporate / FOIA locator |
| CourtListener | https://www.courtlistener.com/ | KEEP | core public-records / corporate / FOIA locator |
| Public Access to Court Electronic Records | https://pacer.uscourts.gov/ | KEEP | core public-records / corporate / FOIA locator |
| Parallelsearch case law | https://parallelsearch.casetext.com/ | KEEP | public-records / gov / business locator |
| Canadian Legal Information Institute | https://www.canlii.org/en/ | KEEP | core public-records / corporate / FOIA locator |
| Supreme Court of Canada - Cases | https://www.scc-csc.ca/case-dossier/index-eng.aspx | KEEP | public-records / gov / business locator |
| Offender Tracking Information System (OTIS) | https://mdocweb.state.mi.us/OTIS2/otis2.aspx | KEEP | public-records / gov / business locator |
| New York State Prison Records | https://stevemorse.org/prison/prison.html | KEEP | public-records / gov / business locator |
| Texas Public Records Search | https://publicrecords.searchsystems.net/United_States_Free_Public_Records_by_State/Texas_Public_Records/ | KEEP | public-records / gov / business locator |
| Arrest Bookings Search and Report | https://b2.caspio.com/dp/a1a3100009b7083c53a9405f8c6b | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Credibly Accused | https://projects.propublica.org/credibly-accused/ | KEEP | public-records / gov / business locator |
| Sortedbybirthdate | https://sortedbybirthdate.com/ | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| NJParcels.com | http://njparcels.com/property/ | KEEP | public-records / gov / business locator |
| Social Security Death Master File | https://ssdmf.info/ | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| SortedByName.com | https://sortedbyname.com/ | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Sortedbybirthdate.com | https://sortedbybirthdate.com/ | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree); duplicate href also under «PUBLIC RECORDS» |
| Cemetery.directory | https://cemetery.directory/ | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Social Security Death Index | https://stevemorse.org/ssdi/ssdi.html | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| FamilySearch's United States Record Collections | https://stevemorse.org/fhl/websitesunitedstates.html | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Chicago Cook County Genealogy | https://stevemorse.org/vital/cook.html | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| BoatInfoWorld | https://www.boatinfoworld.com/ | KEEP | public-records / gov / business locator |
| 51,000 University of Michigan employee salaries | https://www.mlive.com/news/ann-arbor/2020/12/see-the-2020-salaries-for-all-45000-university-of-michigan-employees.html | KEEP | public-records / gov / business locator |
| Street Name Changes | https://stevemorse.org/census/changes.html | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Brooklyn Genealogy | http://bklyn-genealogy-info.stevemorse.org/index.html | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Little Rock AR Crime Search | https://b2.caspio.com/dp.asp?AppKey=88321000961d92fc4ed343f38a0e | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| New England Facts | https://newenglandfacts.com/ | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Michigan State Records | https://michigan.staterecords.org/ | KEEP | public-records / gov / business locator |
| Cancelthesefunerals.com | http://cancelthesefunerals.com/ | KEEP | public-records / gov / business locator |
| Independent fundamental Baptist sexual misconduct database | https://datawrapper.dwcdn.net/UyECh/20/ | KEEP | public-records / gov / business locator |
| York County PA 2017 Write in Report | https://b2.caspio.com/dp/0a9210000bece9f2f50642ff9cac | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| PA teacher salary average | https://b2.caspio.com/dp/0a921000a059622d4771466aab79 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| High schools that received NRA grants 2010-2016 | https://b4.caspio.com/dp/55073000c492127ebd8d4a03a06a | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Corrections Books Approval Search | https://b2.caspio.com/dp/0a921000cae47f9702f44d2bb94b | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Wisconsin Fox River Veterans' Grave Registration Database | https://c3cqk813.caspio.com/dp/b201500011643c5f4c7f4bfba7d1 | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| OH marijuana docs | https://c0eru132.caspio.com/dp/95d310003d6c2e38182a48ef9bb2 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| FAFSA Search and Report | https://c0dcb948.caspio.com/dp/726780004ccd83a96316450caead | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| AL Local Surety Association Directory | https://c0gaf106.caspio.com/dp/2d4e1000c7506b7686a540d3b10f | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Ohio obituaries, death & marriage Search | https://c0abe732.caspio.com/dp/679e5000cbc8c6a587bb42efa9ef | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| SECO Verification of Course Attendance 2018 | https://c0esh132.caspio.com/dp/9040200005c29c35a74342e2b357 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| IUS The Horizon Search and Report | https://c0acy802.caspio.com/dp/cf3b6000f61f1e0724984cb28f5c | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Katrina Spending Search | https://b2.caspio.com/dp/a4321000cb4905373d1946e5b33f | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| AR College University 2017 Salaries | https://b2.caspio.com/dp.asp?AppKey=883210005c5e51279b424364aab2 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| The Weapons ID Database | http://www.smallarmssurvey.org/weapons-and-markets/tools/weapons-id-database.html | KEEP | public-records / gov / business locator |
| Yearbooks | https://www.e-yearbook.com/ | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Yearbooks \/ High School Yearbooks \/ Ancestry | https://www.ancestry.com/search/collections/1265/ | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Yearbooks - MyHeritage | https://www.myheritage.com/research/category-10010/yearbooks | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |

### GOVERNMENT

| Tool | URL | Disposition | Note |
|------|-----|-------------|------|
| data.occrp.org | https://data.occrp.org/ | KEEP | core public-records / corporate / FOIA locator |
| The Pegasus Project \/ OCCRP | https://cdn.occrp.org/projects/project-p/#/ | KEEP | core public-records / corporate / FOIA locator |
| COP26 registered attendees | https://datawrapper.dwcdn.net/UCUWs/3/ | KEEP | public-records / gov / business locator |
| MuckRock | https://www.muckrock.com/ | KEEP | core public-records / corporate / FOIA locator |
| GovSalaries | https://govsalaries.com/ | KEEP | public-records / gov / business locator |
| Openpayrolls.com | https://openpayrolls.com/ | KEEP | public-records / gov / business locator |
| SeeThroughNY :: Pensions | https://www.seethroughny.net/pensions | KEEP | public-records / gov / business locator |
| Scotussearch.com | https://www.scotussearch.com/ | KEEP | public-records / gov / business locator |
| Nonprofit Explorer | https://projects.propublica.org/nonprofits/ | KEEP | public-records / gov / business locator |
| Coronavirus Bailouts | https://projects.propublica.org/coronavirus/bailouts/ | KEEP | public-records / gov / business locator |
| Nursing Home Inspect | https://projects.propublica.org/nursing-homes/ | KEEP | public-records / gov / business locator |
| Macron Campaign Emails | https://wikileaks.org//macron-emails/ | CONTEXT | WikiLeaks dump / mirror — journalistic awareness only; no dump-search playbook |
| DNC email database | https://wikileaks.org//dnc-emails/ | CONTEXT | WikiLeaks dump / mirror — journalistic awareness only; no dump-search playbook |
| GI Files | https://search.wikileaks.org/gifiles/ | CONTEXT | WikiLeaks dump / mirror — journalistic awareness only; no dump-search playbook |
| AKP email database | https://wikileaks.org//akp-emails/ | CONTEXT | WikiLeaks dump / mirror — journalistic awareness only; no dump-search playbook |
| LittleSis | https://littlesis.org/ | KEEP | core public-records / corporate / FOIA locator |
| Lexington KY Employee Salaries 2021 | https://c0ect130.caspio.com/dp/c852100055664d756c6e441aa963 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Greater Sacramento Area Public Salaries | https://b2.caspio.com/dp/c48210000605c38aa22f4080a1be | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Illinois Public Salaries | https://c0ctb111.caspio.com/dp/1a7210001e4dbabdb7204962bc03 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| St. Louis County salaries fiscal 2020 | https://c0bkr141.caspio.com/dp/936b1000d0c132c8cbbb4f0c8c1f | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Milwaukee Wisconsin City Employee Salaries 2019 | https://c0ebl104.caspio.com/dp/eab010008ed5ca97d7404269bf89 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Texas Local Superintendent Salaries Search and Report | https://b3.caspio.com/dp/5a5b1000b41b35162a3844b4b7ec | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Baytown TX Employee Directory | https://c0ctb134.caspio.com/dp/c5f5200097e7aef4edb54e09bd5e | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| MA Middlesex County City employee salary 2019 | https://c0eib112.caspio.com/dp/6ee01000497ba7e2d63b46229a99 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| KY State Salary 2019 | https://c0ect130.caspio.com/dp/c8521000065e102da08c40e696ad | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| UKY Salaries 2019 | https://c0ect130.caspio.com/dp/c8521000eca729c2125e46c487fd | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Mobile AL Salaries Search and Report | https://b2.caspio.com/dp/362210004ae292fb5cf34f0fb079 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| NC State Government Salaries Search and Report | https://b2.caspio.com/dp/96073000345d59bc5b1744109afe | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| NC State Employee Overtime 2018 Search and Report | https://c0eib112.caspio.com/dp/6ee01000325ae85bbfe24ade9bea | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| PA 2017 Certificate Actions (Education) | https://b2.caspio.com/dp/0a9210006dbe656876084f9b9f59 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| First Philadelphia Preparatory Charter School Staff Public Release 2017 | https://b2.caspio.com/dp/0a921000842668d3d3e644d2bd8f | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| PA School Districts Deeds user-facing web search | https://b2.caspio.com/dp/0a92100000938817df46468fa2a0 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| PA Perry County 2017 Compensation Search and Report | https://b2.caspio.com/dp/0a921000e05cf4b592b245aeae20 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Gettysburg PA Adams County 2017 Payroll Search and Report | https://b2.caspio.com/dp/0a9210006f0ddf22afd8417f9711 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Lebanon County PA 2017 Search and Report | https://b2.caspio.com/dp/0a9210001cc98f2f21004ce4a3d4 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Dauphin County PA 2017 Compensation | https://b2.caspio.com/dp/0a921000a2f20d556db84221a92c | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| York City PA Compensation | https://b2.caspio.com/dp/0a92100001903125816c4d34a37a | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| York County VA 2017 Public Salaries | https://b2.caspio.com/dp/0a921000b12e238357df42e7affc | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| OH Court Costs | https://b2.caspio.com/dp/95d31000da9841d5980644c98761 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| German Gov Employee Database (Unknown) | https://c0acz339.caspio.com/dp/E171600054612b9f79fb4ddf8f2b | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Brazillian Address CEP Search and Report | https://c2abn462.caspio.com/dp/6c2d80006c6adb825b3b45079cb8 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Darpan NGO Search | https://c7ect427.caspio.com/dp/c45e900062d54a7f263942979465 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| UNC System employees with the biggest paychecks | https://c0dzk127.caspio.com/dp/b95b1000e0821c125a8a43cd9cc1 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| HEALTHCARE EDUCATION PROVIDERS | https://c3dug085.caspio.com/dp/1fec4000740ace75fdb94ec5bca5 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Cal Poly Email Search | https://c0acw966.caspio.com/dp/5dbe60009c7190a3b0bb407eaea0 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Dutchess and Ulster bridge safety ratings 2015 | https://b2.caspio.com/dp.asp?AppKey=996f1000109b0cd3b24b408daf60 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Lou Barletta 2017 Donors | https://b2.caspio.com/dp/0a9210001cdd2eaac90941488478 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Worcester MA Employee Gross Pay | https://c0acu481.caspio.com/dp/e0536000108787410ed749fdb240 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |

### [CAN] GOVERNMENT

| Tool | URL | Disposition | Note |
|------|-----|-------------|------|
| Advanced Registry Search | https://lobbycanada.gc.ca/app/secure/ocl/lrs/do/advSrch?lang=eng | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Statistics Canada | https://www150.statcan.gc.ca/n1/en/type/data?HPA=1 | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Canada Gazette | https://www.gazette.gc.ca/accueil-home-eng.html | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Completed Access to Information Requests | https://open.canada.ca/en/search/ati | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Canadian Importers Database | https://strategis.ic.gc.ca/eic/site/cid-dic.nsf/eng/home | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Canadian Institute for Health Information | https://www.cihi.ca/en | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Association-assq.qc.ca | https://www.association-assq.qc.ca/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Trouver une décision | http://citoyens.soquij.qc.ca/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Regional Municipality of Durham | https://opendata.durham.ca/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Find a Teacher | https://www.oct.ca/Home/FindATeacher | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| www.infogo.gov.on.ca/infogo/home.html | https://www.infogo.gov.on.ca/infogo/home.html | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Employee Contact Directory Search \/ novascotia.ca | https://novascotia.ca/psc/geds/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Search for Open Information Documents | https://www2.gov.bc.ca/gov/search?id=0882CD53C45A4AE1A42D5E22D8712AD8 | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Search the Open Information Catalogue | https://www2.gov.bc.ca/gov/search?id=9199E7BC9682482EB9EA0B6D6B8D386C | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Registrant directory | https://www.cpsbc.ca/public/registrant-directory | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Government staff directory | https://www.alberta.ca/staff-directory.cfm | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Canadian Intellectual Property Office | https://www.ic.gc.ca/eic/site/cipointernet-internetopic.nsf/eng/Home | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Gouvernement du Québec | https://www.donneesquebec.ca/organisation/gouvernement-du-quebec/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Library and Archives Canada (LAC) | https://www.bac-lac.gc.ca/eng/Pages/home.aspx | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Montreal Council of Social Agencies Database | http://www.archives.mcgill.ca/resources/db/mcsasearch.htm | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Media Room & Blue Book | https://media.utoronto.ca/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Resources.library.ubc.ca | https://resources.library.ubc.ca/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Security Licence Status Verification | https://justice.gov.bc.ca/security/utilities/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |

### [CAN] CORPORATION

| Tool | URL | Disposition | Note |
|------|-----|-------------|------|
| RJSC Connect | https://rjsc.novascotia.ca/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Search for a Federal Corporation | https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/fdrlCrpSrch.html?locale=en_CA | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| FederalCorporation | https://federalcorporation.ca/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Corporate Affairs Registry Database | https://www.pxw2.snb.ca/card_online/cardsearch.aspx | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| MRAS Business Registry Search | https://beta.canadasbusinessregistries.ca/search | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Alberta Business Search | https://albertacorporations.com/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| LeoList | https://www.leolist.cc/ | CONTEXT | classifieds board (not a corporate registry); locator only — no ops |
| Toronto Star | https://misc.thestar.com/interactivegraphic/2019/07-july/25-housing-complaints-database/index.html | KEEP | public Canadian housing/open-data locator |
| Rental in Canada | https://www.n49.com/search/rental/1/canada/ | KEEP | public Canadian housing/open-data locator |
| Manitoba Assessment Online | https://www.gov.mb.ca/mao/public/search_select.aspx | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Search for Company Documents | https://www.sedar.com/search/search_form_pc_en.htm | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Business Directory \/ OCC | https://occ.ca/business-directory/ | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Rechercher par entreprise | https://www.pes.rbq.gouv.qc.ca/RegistreLicences/Recherche?mode=Entreprise | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Rechercher par répondant | https://www.pes.rbq.gouv.qc.ca/RegistreLicences/Recherche?mode=Repondant | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Rechercher par région ou type de travaux | https://www.pes.rbq.gouv.qc.ca/RegistreLicences/Recherche?mode=RegionTypeTravaux | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Services en ligne | https://www.pes.ctq.gouv.qc.ca/pes/faces/dossierclient/recherche.jsp | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Alcool - Régie des alcools, des courses et des jeux (RACJ) | https://www.racj.gouv.qc.ca/en/registres-publics/alcool.html | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| BAnQ numérique | https://numerique.banq.qc.ca/resultats | KEEP | atto+osint — genealogy / vital / archive locator (no private pedigree) |
| Online Services PEI Business / Corporate Registry | https://www.princeedwardisland.ca/en/feature/pei-business-corporate-registry-original#/service/LegacyBusiness/LegacyBusinessSearch | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| XBRL Voluntary Filing Program | https://www.sedar.com/issuers/issuers_en.htm | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |
| Registrant Lookup | https://www.cdsbc.org/home/registrant-lookup#/lookup/dentists | KEEP | atto+osint — Canadian public registry / ATI / open-gov locator |

### VOTER DATABASES

| Tool | URL | Disposition | Note |
|------|-----|-------------|------|
| Search for US Voters with Custom Search Engines #OSINT \/ Boolean Strings | https://booleanstrings.com/2021/07/15/search-for-us-voters-with-custom-search-engines-osint/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Washington State Voter Database | http://www.soundpolitics.com/voterlookup.html | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Arkvoters.com | https://arkvoters.com/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Coloradovoters.info | https://coloradovoters.info/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Delawarevoters.info | http://delawarevoters.info/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Flvoters.com | https://flvoters.com/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Georgia-voters.com | https://georgia-voters.com/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Connvoters.com | https://connvoters.com/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Michiganvoters.info | https://michiganvoters.info/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Ohiovoters.us | http://ohiovoters.us/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Oklavoters.com | http://oklavoters.com/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Rivoters.com | https://rivoters.com/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Wiscvoters.com | https://wiscvoters.com/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Utvoters.com | http://utvoters.com/ | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| Oklahoma Voters Search | http://oklahomadata.com/voters.asp | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| New Jersey Voter Records | https://stevemorse.org/njvoters/njvoters.html | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |
| New York State Voter Records | https://stevemorse.org/nysvoters/nysvoters.html | KEEP | public voter-roll locator / CSE — authorized OSINT locator only; not a harassment playbook |

### BUSINESS

| Tool | URL | Disposition | Note |
|------|-----|-------------|------|
| Companies & Orgs Search Engine | https://cse.google.com/cse?cx=72ea9d8cfefc142d3 | KEEP | public-records / gov / business locator |
| WhaleSlide | https://whaleslide.com/ | KEEP | public-records / gov / business locator |
| AllPeople | https://allpeople.com/ | KEEP | public-records / gov / business locator |
| Corporation Wiki | https://www.corporationwiki.com/ | KEEP | public-records / gov / business locator |
| PA PPP Database | https://public.flourish.studio/visualisation/3105919/ | KEEP | public-records / gov / business locator |
| Michigan PPP loans | https://c0eib122.caspio.com/dp/74321000d4c16abc2baf480b8934 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Companies House | https://www.gov.uk/government/organisations/companies-house | KEEP | core public-records / corporate / FOIA locator |
| Global Brownbook | https://www.brownbook.net/ | KEEP | public-records / gov / business locator |
| list-org | https://www.list-org.com/ | KEEP | public-records / gov / business locator |
| OpenCorporates | https://opencorporates.com/ | KEEP | core public-records / corporate / FOIA locator |
| ICIJ Offshore Leaks Database | https://offshoreleaks.icij.org/ | KEEP | core public-records / corporate / FOIA locator |
| Home Comptroller.Texas.Gov | https://comptroller.texas.gov/ | KEEP | public-records / gov / business locator |
| Company search tool | https://www.aware-online.com/en/osint-tools/company-search-tool/ | KEEP | public-records / gov / business locator |
| XRefer | https://www.xrefer.com/ | KEEP | public-records / gov / business locator |
| Ttabcenter.com | https://ttabcenter.com/ | KEEP | public-records / gov / business locator |
| First Search | https://search.firstround.com/ | KEEP | public-records / gov / business locator |
| Findingstartups.com | https://findingstartups.com/ | KEEP | public-records / gov / business locator |
| Startup Tracker | https://startuptracker.io/home | KEEP | public-records / gov / business locator |
| Shopsearchengine.com | http://shopsearchengine.com/ | KEEP | public-records / gov / business locator |
| Covidbailouttracker.com | https://covidbailouttracker.com/ | KEEP | public-records / gov / business locator |
| Coronavirus Bailouts: Search Every Company Approved for Federal Loans Over $150k | https://projects.propublica.org/coronavirus/bailouts/ | KEEP | public-records / gov / business locator; duplicate href also under «GOVERNMENT» |
| LA County CA Restaurant Health Violations | https://b2.caspio.com/dp.asp?AppKey=22341000af0b9c98ebf047f1b9f2 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Kansas Restaurant Inspections | https://b2.caspio.com/dp/a1a31000af3bac4c5e434987a857 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Lexington-Fayette County KY Health Department Restaurant Inspections | https://b2.caspio.com/dp.asp?AppKey=c8521000c641ab80b6d2448e89d9 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| FL Energy Money in Politics | https://b2.caspio.com/dp.asp?AppKey=c73210001174b8c2a8d444768f5c | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| ValidFleetList (unknown Sail Boat database) | https://c0eru285.caspio.com/dp/0dc330002829dcc1ad864b5bb094 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |
| Viking Rifle Series Shooter Live Results | https://vikingrifleseries.caspio.com/dp/c8ac5000f29041f935cf42b6a641 | KEEP | Caspio-hosted public search UI (often one-off FOIA dumps) — locator only |

### FINANCE

| Tool | URL | Disposition | Note |
|------|-----|-------------|------|
| Greylist Trace | https://greylisttrace.com/ | KEEP | public-records / gov / business locator |
| analytics-engine | https://github.com/mashiox/analytics-engine | KEEP | public-records / gov / business locator |
| Tradint Research Tool | https://tradint.io/ | KEEP | public-records / gov / business locator |
| Ppp.adatascienti.st | https://ppp.adatascienti.st/ | KEEP | public-records / gov / business locator |
| CoVi Analytics | https://www.covianalytics.com/ | KEEP | public-records / gov / business locator |
| Search Our PPP Loan Database | https://ppp.directory/search | KEEP | public-records / gov / business locator |
| TMX | https://www.m-x.ca/en/trading/data/quotes?symbol= | KEEP | public-records / gov / business locator |
| TMX TSX | https://www.tsx.com/listings/listing-with-us/listed-company-directory | KEEP | public-records / gov / business locator |
| Search for Investment Fund Documents | https://www.sedar.com/search/search_form_mf_en.htm | KEEP | core public-records / corporate / FOIA locator |

### POLICE / LE / FED

| Tool | URL | Disposition | Note |
|------|-----|-------------|------|
| Openoversight | https://openoversight.com/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Criminal Cop Database Lookup | https://extras.mercurynews.com/criminalcops/database/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Police1 | https://bloopbase.keybase.pub/ACAB/POLICEONE/index.html | CONTEXT | third-party LE dump mirror — CONTEXT; not an authorized FOIA portal |
| The Philadelphia Police Misconduct Database | https://datawrapper.dwcdn.net/3GbVI/1/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| NYPD Misconduct Complaint Database | https://nyclu.shinyapps.io/CCRB_combo/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| NYPD Officer Profile | https://nypdonline.org/link/2 | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Maine County Law Enforcement Discipline Chart | https://public.flourish.studio/visualisation/4443849/?utm_source=showcase&utm_campaign=visualisation/4443849 | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Arizona LE Database - ABC15 | https://datawrapper.dwcdn.net/kkg90/6/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Police Complaint Lookup | http://complaints.cuapb.org/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Boston Police Internal Affairs Cases, 2010-2020 | https://apps.bostonglobe.com/graphics/2020/law-enforcement/index.html?initialWidth=1029&childId=police-embed&parentTitle=Database%3A%20Search%2010%20years%27%20worth%20of%20Boston%20Police%20Department%20disciplinary%20action&parentUrl=https%3A%2F%2Fwww.bostonglobe.com%2F2020%2F11%2F24%2Fmetro%2Fheres-searchable-database-boston-police-department-internal-investigations-disciplinary-actions-more%2F | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Police Decertifcations Search and Report | https://c0acu882.caspio.com/dp/07da6000e467ebc2a444430c9c1d | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| San Francisco CopWatch Database | https://airtable.com/embed/shreS9yA6eWiJAmHZ/tbl0A1AfPBOaPNBhH?backgroundColor=blue | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| NJ Police and Fire FY 2011 Pension contribution | https://b2.caspio.com/dp.asp?AppKey=c43d100007eedbb0f0e740188660 | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| EFF Atlas of Surveillance | https://atlasofsurveillance.org/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Clearview AI US taxpayer-funded entities | https://datawrapper.dwcdn.net/VOOIE/16/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Oregon DPSST Professional Standards Cases Database | https://www.oregon.gov/dpsst/CJ/Pages/Cases.aspx | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| PA Forfeiture 2010-2016 Search | https://b2.caspio.com/dp/0a921000328dc970793c4364bb2a | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| BlueLeaks | https://blueleaks.io/index.html | CONTEXT | leak dump (BlueLeaks) — know it exists; do not operationalize / no dump playbook |
| Plain View Project | https://www.plainviewproject.org/data | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| ICE Patrol | https://ice.wikileaks.org/search | CONTEXT | WikiLeaks dump / mirror — journalistic awareness only; no dump-search playbook |
| Policecrime.bgsu.edu | https://policecrime.bgsu.edu/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| CAPstat.nyc | https://www.capstat.nyc/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Citizens Police Data Project | https://beta.cpdp.co/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Fatal Encounters | https://fatalencounters.org/people-search/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| The NYPD Files | https://projects.propublica.org/nypd-ccrb/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Open Data Policing | https://opendatapolicing.com/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Police Surveillance in Chicago | https://redshiftzero.github.io/policesurveillance/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Mappingpoliceviolence.org | https://mappingpoliceviolence.org/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Police Protest Videos | https://projects.propublica.org/protest-police-videos/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| GeorgeFloyd Protest police brutality videos | https://docs.google.com/spreadsheets/u/1/d/1YmZeSxpz52qT-10tkCjWOwOGkQqle7Wd1P7ZM1wMW0E/htmlview?pru=AAABcql6DI8*mIHYeMnoj9XWUp3Svb_KZA# | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Police Body-Worn Camera Footage Access Map | https://www.rcfp.org/resources/bodycams/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Policebrutalitydatabase.org | https://www.policebrutalitydatabase.org/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Civilian Office of Police Accountability | https://www.chicagocopa.org/data-cases/case-portal/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Coplookup.com | https://coplookup.com/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| How many untested rape kits does your city police department or county sheriff's office have? | https://datawrapper.dwcdn.net/uOdaT/4/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Gun Dealer Inspections \/ The Trace | https://projects.thetrace.org/inspections/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Secret Surveillance Catalogue | https://theintercept.com/surveillance-catalogue/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Chicago Police Department Demographics | https://public.flourish.studio/visualisation/1089756/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| George Floyd - Where black people are most disproportionately killed by police | https://public.flourish.studio/visualisation/2646234/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Iowa Cities police budgets | https://public.flourish.studio/visualisation/3168834/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| TGCG Members Page | https://c2ffn114.caspio.com/dp/e6a74000833e44e23c324a10987c | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Buffalo Police | https://airtable.com/embed/shra4F3cAE7H2PV5m?backgroundColor=gray&amp;viewControls=on | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| postcert | https://post.coag.gov/s/?tabset-1eada=4b5ff | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |

### [CAN] POLICE

| Tool | URL | Disposition | Note |
|------|-----|-------------|------|
| Alberta Police Misconduct Database | https://www.policemisconductdatabase.ca/database/ | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| Toronto Police Service | https://bloopbase.keybase.pub/ACAB/TPS/index.html | CONTEXT | third-party LE dump mirror — CONTEXT; not an authorized FOIA portal |
| Royal Canadian Mounted Police | https://bloopbase.keybase.pub/ACAB/RCMP/index.html | CONTEXT | third-party LE dump mirror — CONTEXT; not an authorized FOIA portal |
| Ontario Provincial Police | https://bloopbase.keybase.pub/ACAB/OPP/index.html | CONTEXT | third-party LE dump mirror — CONTEXT; not an authorized FOIA portal |
| RCMP Death Search | https://c0cqk108.caspio.com/dp/9156100036f195cdf0934662917c | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| RCMP Death Search 2 | https://c0cqk108.caspio.com/dp/915610007f161cceda514e33a0b7 | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |
| RCMP Death Search 3 | https://b2.caspio.com/dp/91561000c38ca49de99e4ecf9619 | CONTEXT | LE misconduct / transparency locator (journalistic public records) — CONTEXT, not targeting how-to |

## Snippets

> Group `06-records-gov`: 241 links across 9 sections (PUBLIC RECORDS, GOVERNMENT, [CAN] GOVERNMENT, [CAN] CORPORATION, VOTER DATABASES, BUSINESS, FINANCE, POLICE / LE / FED, [CAN] POLICE). [Source: `.local/osint4all/groups/06-records-gov.json` / OSINT4ALL start.me L1rEYQ (retrieved 2026-08-18)]

Core KEEP anchors: PACER, CourtListener, OpenCorporates, ICIJ Offshore Leaks, Companies House, Canadian corporate registries + SEDAR, FamilySearch/SSDI/cemetery genealogy locators, MuckRock, LittleSis, OCCRP data. BlueLeaks + WikiLeaks/ICE dump mirrors = CONTEXT.
