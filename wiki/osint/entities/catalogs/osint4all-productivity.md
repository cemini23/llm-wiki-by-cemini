---
title: OSINT4ALL productivity / toolset catalog
type: entity
tags: [osint, catalog, osint4all, k241, productivity]
keywords: [OSINT4ALL, CyberChef, CryptPad, Wayback, theHarvester, block explorer, shadow library]
related:
  - sources/osint4all-startme-2026-08-18.md
  - entities/tools/osint4all.md
  - concepts/osint4all-catalog.md
  - entities/tools/cyberchef.md
  - sources/eval-multi-wiki-url-revenue-2026-08-18.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @sources/osint4all-startme-2026-08-18.md — ingest source (K241)
- @entities/tools/osint4all.md — hub entity
- @concepts/osint4all-catalog.md — KEEP / CONTEXT / DEAD filing rules
- @entities/tools/cyberchef.md — CyberChef entity (KEEP row below)

## Raw Concept

OSINT4ALL sections PRODUCTIVITY, FILE UPLOAD, TOOLSET, DOWNLOADER, and CRYPTOCURRENCY (123 mirrored links from group `08-productivity`). Filed as one locator catalog — not a stub farm. Shadow libraries stay CONTEXT (no copyrighted corpus ingest). Rainbow-table hash-recovery sites are not in this pack (see cyber-caution / HASH RECOVERY); if encountered, treat as CONTEXT analyst locators, not KEEP-as-attack. yt-dlp is not present in this JSON slice; KEEP it as a media-download locator when it appears on the live board.

## Narrative

**Counts:** KEEP 104 · DEAD-OUTDATED 13 · CONTEXT 6 · CAUTION 0 · NESTED-HUB 0 (total 123).

### PRODUCTIVITY

| Name | URL | Wiki | Disposition | Why |
| --- | --- | --- | --- | --- |
| unfurl | https://dfir.blog/unfurl/ | osint | KEEP | URL unfurl / metadata parser (DFIR) |
| Wolfram Alpha | https://www.wolframalpha.com/ | osint | KEEP | Computational knowledge engine |
| Cryptpad.fr | https://cryptpad.fr/ | osint | KEEP | E2EE collaborative docs/pads — productivity staple |
| Recontool.org | https://recontool.org/ | osint | DEAD-OUTDATED | Host unreachable (2026-08-18 probe) |
| MindMup 2 | https://app.mindmup.com/map/new | osint | KEEP | Browser mind-map editor |
| Dotspotter | https://www.forensicdots.de/ | osint | KEEP | Printer forensic tracking-dot decoder |
| Encrypted Pastebin | https://defuse.ca/pastebin.htm | osint | KEEP | Client-side encrypted paste (defuse.ca) |
| PrivateBin | https://privatebin.net/ | osint | KEEP | Self-destructing encrypted paste — share ephemeral notes |
| Bin.disroot.org | https://bin.disroot.org/ | osint | KEEP | Disroot PrivateBin instance |
| Framadrop | https://framadrop.org/en/ | osint | KEEP | Framasoft ephemeral file drop (Lufi) |
| Pad.riseup.net | https://pad.riseup.net/ | osint | KEEP | Riseup Etherpad |
| EtherCalc | https://ethercalc.net/ | osint | KEEP | Collaborative spreadsheet |
| Proofread Bot | https://proofreadbot.com/ | osint | KEEP | Grammar/proofreading helper |
| Write.as | https://write.as/ | osint | KEEP | Minimal blogging / paste writing |
| Cryptee | https://crypt.ee/ | osint | KEEP | Encrypted docs/photos suite |
| dudle | https://dudle.inf.tu-dresden.de/anonymous/ | osint | KEEP | Anonymous scheduling poll |
| Airborn.io | https://www.airborn.io/ | osint | DEAD-OUTDATED | Encrypted docs product abandoned; login stub only (2026-08-18 probe) |
| ZOOM URL Generator | https://skyzh.github.io/zoom-url-generator/ | osint | KEEP | Zoom meeting URL builder |
| Tor2web | https://www.tor2web.org/ | osint | DEAD-OUTDATED | Host unreachable; Tor2web gateways largely retired |
| archive.is | https://archive.is/ | osint | KEEP | On-demand page archive / permalink capture |
| Wayback Machine | https://web.archive.org/ | osint | KEEP | Internet Archive Wayback — historical page capture |
| waybackpy | https://pypi.org/project/waybackpy/ | osint | KEEP | Python Wayback Machine client library |
| CachedPages | http://www.cachedpages.com/ | osint | DEAD-OUTDATED | Parked lander redirect — not a cache viewer |
| Google Cached Pages of Any Website | https://cachedview.com/ | osint | KEEP | Cache-view helper (verify live; Google cache shrinking) |
| Oldweb.today | http://oldweb.today/ | osint | KEEP | Emulated old browsers against archives |
| Unpaywall | https://unpaywall.org/products/extension | osint | KEEP | Legal OA PDF finder browser extension |
| DeepL | https://www.deepl.com/translator | osint | KEEP | Machine translation |
| Project CSV | https://projectcsv.github.io/ | osint | KEEP | CSV viewer/tool |
| CSV to HTML | https://codepen.io/RYJASM/pen/LVEWgV | osint | KEEP | CSV→HTML CodePen utility |
| Monaco Editor | https://microsoft.github.io/monaco-editor/playground.html | osint | KEEP | VS Code editor playground |
| Online FlowChart Editor | https://mermaid-js.github.io/mermaid-live-editor/ | osint | KEEP | Mermaid live editor |
| Markdown Editor | https://markdown-editor.github.io/ | osint | KEEP | Browser markdown editor |
| SQL Editor | https://www.mycompiler.io/new/sql | osint | KEEP | Online SQL scratchpad |
| SQLite Viewer | https://inloop.github.io/sqlite-viewer/ | osint | KEEP | In-browser SQLite DB viewer |
| OCR Text Extractor | https://osint.sh/ocr/ | osint | KEEP | osint.sh OCR helper |
| Wetranscriber | https://www.wetranscriber.com/ | osint | KEEP | Audio transcription helper |
| Tophonetics.com | https://tophonetics.com/ | osint | KEEP | IPA phonetic transcription |
| Google Translate | https://translate.google.com/ | osint | KEEP | Machine translation |
| Multi Translate | https://translate.mix.pink/ | osint | DEAD-OUTDATED | Host unreachable (2026-08-18 probe) |
| Yandex.Translate | https://translate.yandex.com/ | osint | KEEP | Machine translation |
| Bing Microsoft Translator | https://www.bing.com/translator | osint | KEEP | Machine translation |
| Reverso | https://www.reverso.net/text_translation.aspx?lang=EN | osint | KEEP | Translation + conjugation |
| Translate | https://www.translatedict.com/ | osint | KEEP | Dictionary/translate utility |
| text to speech online | https://www.naturalreaders.com/online/ | osint | KEEP | TTS reader |
| TTSReader | https://ttsreader.com/ | osint | KEEP | TTS reader |
| Online Sequencer | https://onlinesequencer.net/ | osint | KEEP | Browser music sequencer |
| FetchRSS | https://fetchrss.com/ | osint | KEEP | RSS feed generator from pages |
| Sci-hub | https://sci-hub.st/ | osint | CONTEXT | Shadow library — do not ingest copyrighted corpora; locator only |
| Libgen.fun | https://libgen.fun/ | osint | CONTEXT | Shadow library — do not ingest copyrighted corpora; locator only |
| Z-lib.org | https://z-lib.org/ | osint | CONTEXT | Shadow library — do not ingest copyrighted corpora; locator only |
| PDF Drive | https://www.pdfdrive.com/ | osint | CONTEXT | Mass PDF mirror of unclear rights — do not ingest corpora; locator only |
| arXiv.org | https://arxiv.org/ | osint | KEEP | Open-access preprint server — legitimate literature |
| bioRxiv.org | https://www.biorxiv.org/ | osint | KEEP | Open-access biology preprints |
| Project Gutenberg | https://www.gutenberg.org/ | osint | KEEP | Public-domain ebook corpus |
| Trantor.is | https://trantor.is/ | osint | CONTEXT | Shadow-library style ebook mirror — CONTEXT; host also unreachable 2026-08-18 |
| Shadowlibraries.github.io | https://shadowlibraries.github.io/ | osint | CONTEXT | Shadow-library index — CONTEXT only; no corpus ingest |
| Editor.typely.com | https://editor.typely.com/ | osint | KEEP | Online text editor / proofreader |

### FILE UPLOAD

| Name | URL | Wiki | Disposition | Why |
| --- | --- | --- | --- | --- |
| MEGA | https://mega.io/ | osint | KEEP | Encrypted cloud storage |
| transfer.sh | https://transfer.sh/ | osint | KEEP | CLI/browser ephemeral file transfer |
| Upload (Disroot) | https://disroot.org/en/services/upload | osint | KEEP | Disroot upload service |
| Chibisafe.moe | https://chibisafe.moe/ | osint | KEEP | Self-hostable image/file host |
| Bunker.is | https://bunker.is | osint | DEAD-OUTDATED | Host unreachable (2026-08-18 probe) |
| Send | https://send.actionsack.com/ | osint | DEAD-OUTDATED | Firefox Send fork host unreachable (2026-08-18) |
| Zz.fo | https://zz.fo/ | osint | DEAD-OUTDATED | Host unreachable (2026-08-18 probe) |
| Upload files to IPFS from Browser | https://anarkrypto.github.io/upload-files-to-ipfs-from-browser-panel/public/ | osint | KEEP | Browser IPFS upload panel |
| BlackHole | https://blackhole.run/ | osint | DEAD-OUTDATED | Host unreachable (2026-08-18 probe) |

### TOOLSET

| Name | URL | Wiki | Disposition | Why |
| --- | --- | --- | --- | --- |
| CyberChef | https://gchq.github.io/CyberChef/ | osint | KEEP | @entities/tools/cyberchef.md — GCHQ encode/decode Swiss Army knife |
| mitaka | https://github.com/ninoseki/mitaka | osint | KEEP | Browser extension IOC lookup |
| Frack | https://github.com/sensepost/Frack | osint | KEEP | sensepost Frack framework (GitHub) |
| pywhat | https://pypi.org/project/pywhat/ | osint | KEEP | Identify mystery strings / artifacts |
| theHarvester | https://pypi.org/project/theHarvester/ | osint | KEEP | Email/subdomain/people recon CLI (authorized targets) |
| Online Tools | https://emn178.github.io/online-tools/ | osint | KEEP | Hash/encode/convert utility suite |
| Graphviz Online | https://dreampuf.github.io/GraphvizOnline/ | osint | KEEP | DOT graph renderer |
| CodePen | https://codepen.io/ | osint | KEEP | Front-end scratchpad |
| Diceware Generator | https://www.rempe.us/diceware/#eff | osint | KEEP | Passphrase generator (EFF wordlist) |
| Checkphish.ai | https://checkphish.ai/ | osint | KEEP | Phishing URL checker |
| x86 and x64 Intel Assembler | https://defuse.ca/online-x86-assembler.htm | osint | KEEP | Online assembler (defuse.ca) |
| Big Number Calculator | https://defuse.ca/big-number-calculator.htm | osint | KEEP | Arbitrary-precision calculator |
| Text and File Hash Calculator | https://defuse.ca/checksums.htm | osint | KEEP | Local hash checksum helper |
| HTML Sanitizer Tool | https://defuse.ca/html-sanitize.htm | osint | KEEP | HTML sanitize helper |
| URL Decoder/Encoder | https://meyerweb.com/eric/tools/dencoder/ | osint | KEEP | Percent-encode/decode |
| ODA - The Online Disassembler | https://onlinedisassembler.com/odaweb/ | osint | DEAD-OUTDATED | HTTP 502 — Online Disassembler down (2026-08-18) |
| Disasm.pro | https://disasm.pro/ | osint | KEEP | Online disassembler |
| Fotor | https://www.fotor.com/photo-editor-app/editor/basic | osint | KEEP | Photo editor |
| Decompiler.com | http://www.decompiler.com/ | osint | KEEP | Online decompiler portal |
| Google Colaboratory | https://colab.research.google.com/notebooks/intro.ipynb | osint | KEEP | Hosted Jupyter notebooks |
| Compiler Explorer | https://godbolt.org/ | osint | KEEP | Godbolt compiler explorer |
| HTML editor | https://onlinehtmleditor.dev/ | osint | KEEP | Online HTML editor |
| Online Color Picker | https://colorpicker.me/ | osint | KEEP | Color picker |
| Convert text to image file | https://text2image.com/en/ | osint | KEEP | Text→image utility |
| relational algebra calculator | https://dbis-uibk.github.io/relax/calc/local/uibk/local/0 | osint | KEEP | RelaX relational algebra calc |
| Data Structure : Infix Postfix Prefix - Converter & Evaluator | https://raj457036.github.io/Simple-Tools/prefixAndPostfixConvertor.html | osint | KEEP | Expression notation converter |
| RSA encryption, decryption and prime calculator | https://canihavesomecoffee.github.io/js-rsa-tool/ | osint | KEEP | Educational RSA calculator (analyst) |
| Tools.digitalmethods.net | https://tools.digitalmethods.net/beta/searchEngineScraper/ | osint | KEEP | DMI search-engine scraper toolkit |
| Steganography Online | https://stylesuxx.github.io/steganography/ | osint | KEEP | Image stego encode/decode demo |
| Torrent to Magnet | https://nutbread.github.io/t2m/ | osint | KEEP | Torrent→magnet converter — dual-use locator (authorized use only) |
| Anonymous YouTube Playlists | https://neverducky.github.io/anonymous-youtube-playlists/ | osint | KEEP | YT playlist without account |
| Vega Editor | https://vega.github.io/editor/#/ | osint | KEEP | Vega/Vega-Lite viz editor |
| DISA Code Template Generator | https://duncanford.github.io/disa-code-generator | osint | KEEP | DISA STIG code template helper |
| Canary Tokens | http://canarytokens.org/generate | osint | KEEP | Thinkst canary tokens — tripwire/beacon tradecraft |
| explainshell.com | https://explainshell.com/ | osint | KEEP | Shell command explainer — analyst helper |
| Google Colaboratory | https://colab.research.google.com/ | osint | KEEP | Duplicate Colab entry (root URL) — same KEEP as intro notebook |
| osint-cli-tool-skeleton | https://pypi.org/project/osint-cli-tool-skeleton/ | osint | KEEP | PyPI skeleton for OSINT CLIs |

### DOWNLOADER

| Name | URL | Wiki | Disposition | Why |
| --- | --- | --- | --- | --- |
| Media-downloader.net | https://media-downloader.net/ | osint | DEAD-OUTDATED | Host unreachable (2026-08-18 probe) |
| Imgur Album Downloader | https://dschep.github.io/imgur-album-downloader/#/ | osint | KEEP | Imgur album bulk save (authorized) |
| Export Comments | https://exportcomments.com/ | osint | KEEP | Social comment export locator |
| Image Extractor | https://extract.pics/ | osint | KEEP | Extract images from a page |
| Loader.to | https://loader.to/ | osint | KEEP | Media download helper (ToS/authorized) |
| Commentexporter.com | https://www.commentexporter.com/ | osint | KEEP | Comment export locator |
| Link Gopher | https://sites.google.com/site/linkgopher/ | osint | KEEP | Browser extension — extract page links |
| Page Links Extractor Tool | https://shadowcrypt.net/tools/pagelinks | osint | DEAD-OUTDATED | HTTP 404 — tool path gone |
| Online Tool to Extract Links from any Web Page | https://hackertarget.com/extract-links/ | osint | KEEP | HackerTarget link extractor |

### CRYPTOCURRENCY

| Name | URL | Wiki | Disposition | Why |
| --- | --- | --- | --- | --- |
| Cryptocurrency Alerting | https://cryptocurrencyalerting.com/ | osint | KEEP | Price/on-chain alert service |
| Bitcoin Explorer | https://blockchair.com/bitcoin | osint | KEEP | Bitcoin block explorer — tx/address locator |
| Ethereum Block Explorer | https://etherscan.io/ | osint | KEEP | Ethereum block explorer — tx/address locator |
| Flowscan.org | https://flowscan.org/ | osint | KEEP | Flow blockchain explorer |
| Bitcoin Forums Search Engine | https://cse.google.com/cse?cx=f49f9d5e679b15787 | osint | KEEP | Custom CSE over BTC forums |
| Blockchain Explorer | https://www.blockchain.com/explorer | osint | KEEP | Multi-chain block explorer locator |
| Blockcypher | https://live.blockcypher.com/ | osint | KEEP | BlockCypher live explorers |
| Addresschecker.eu | http://addresschecker.eu/ | osint | DEAD-OUTDATED | HTTP 410 Gone — crypto address checker dead |
| Coinwink.com | https://coinwink.com/ | osint | KEEP | Crypto price alerts |
| Cryptocurrency search tool | https://www.aware-online.com/en/osint-tools/cryptocurrency-search-tool/ | osint | KEEP | Aware Online crypto OSINT search |
| OSINT cryptocurrencies | https://www.aware-online.com/en/osint-tools/cryptocurrency-tools/ | osint | KEEP | Aware Online crypto OSINT tool index |

## Snippets

Source mirror: `.local/osint4all/groups/08-productivity.json` (123 links, 5 sections). Deadness probes 2026-08-18 (HTTP status / lander checks).
