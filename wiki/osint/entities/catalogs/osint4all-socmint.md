---
title: OSINT4ALL — SOCMINT catalog
type: entity
tags: [osint4all, k241, socmint, social-media]
keywords: [SOCMINT, Facebook, Twitter, X, YouTube, Reddit, LinkedIn, Instagram, Telegram, Snapchat, Discord, Twitch, Mastodon, TikTok, OnlyFans, nitter, OSINT4ALL]
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

OSINT4ALL group **04-socmint** — the nested SOCMINT board (start.me `Wp1kpe`) as mirrored in the L1rEYQ ingest (2026-08-18): social-media username/profile locators, platform-specific search tooling, bot/influence analysis, and news/analytics side-sections. One catalog page; not a stub farm. The SOCMINT start.me board itself is the **NESTED-HUB** — it is already mirrored in this pack, so it is not recursively scraped. **Wiki column = owning Cemini federation wiki** (`osint` default; `seo` for SEO-platform rows).

| Field | Value |
|-------|--------|
| Board group | `04-socmint` |
| Links (board) | 257 |
| Sections | 22 (1 empty on board) |
| Source JSON | `.local/osint4all/groups/04-socmint.json` |
| Filing date | 2026-08-18 |

## Narrative

SOCMINT locators are filed **KEEP** by default: username/social profile locators (social-searcher, RecruitEm x-ray), tweet search (X CSEs, Followerwonk bio search), Reddit search/archive tooling (reveddit, RedditMetis, comment search), LinkedIn x-ray (recruitin, LI boolean builders), Telegram search (tgstat, Lyzem, xtea), Instagram locators (instaloader, Osintgram, commentpicker ID tools), and IntelTechniques' social tool pages. Nitter/Invidious-style proxy instances are KEEP but **volatile** — each instance was probed at filing time; dead ones are marked DEAD-OUTDATED (nitter.it, teddit, libredd.it is 403 bot-gated, nitter.ca was responding 2026-08-18 despite earlier death reports). **CONTEXT**: the scraped/leaked Facebook dataset search (onion.pet) is listed for awareness only — never visited. **DEAD-OUTDATED**: Google+ rows, Clubhouse-era rows (platform defunct), twint (abandoned), plus ~50 tools that returned dead/squatted/parked/error responses at the 2026-08-18 probe (e.g. tweetbeaver, mentionmapp, mereku, redditsearch.io → spam; gramho, karmadecay, sleepingtime, socialbearing, trendsmap → no response; searcheddit, discordportal → parked-for-sale; skypli → gambling spam). OnlyFans profile searches and OSoMe bot/influence tools KEEP. News/fact-check rows KEEP (public-record verification); SEO-platform rows (Semrush, WordPress CSEs, SEO-resources CSE) tagged `seo` for the seo-wiki.

**Disposition totals:** KEEP 193 · DEAD-OUTDATED 62 · CONTEXT 1 · NESTED-HUB 1 · board rows 257 · unique hrefs 257.

## Catalog

### SOCIAL MEDIA

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| SOCMINT | https://start.me/p/Wp1kpe/socmint | osint | NESTED-HUB | nested SOCMINT board (Wp1kpe) — already mirrored in this pack; do not mass-scrape |
| Social Profiles Finder | https://www.social-searcher.com/search-users/ | osint | KEEP | multi-network username/profile locator — responds at probe |
| Who posted what? | https://whopostedwhat.com/ | osint | KEEP | FB/IG keyword search by author — responds at probe |
| VK Search Engine | https://cse.google.com/cse?cx=f5e7cd4c6e33954ec | osint | KEEP | VK profile CSE |
| Skype Search Engine | https://www.skypli.com/ | osint | DEAD-OUTDATED | domain squatted (gambling spam) at probe 2026-08-18; Skype-era locator |
| Vimeo search tool | https://www.aware-online.com/en/osint-tools/vimeo-search-tool/ | osint | KEEP | Vimeo keyword/location search methodology — responds at probe |
| Kribrum.io | https://kribrum.io/ | osint | KEEP | RU social-listening platform — no probe response (likely geo-block); company active |
| Graphtreon.com | https://graphtreon.com/ | osint | KEEP | Patreon earnings/rankings — responds at probe |
| Social Search Engine | https://www.socialsearchengine.org/ | osint | KEEP | social search aggregator — responds at probe |
| Instagram, Reddit & Snapchat | https://one-plus.github.io/Instagram | osint | KEEP | IG/Reddit/Snapchat OSINT toolkit — responds at probe |
| Google to search profiles on Dribbble | https://recruitin.net/dribbble.php | osint | KEEP | Dribbble profile x-ray via Google — responds at probe |
| Google to search profiles on Xing | https://recruitin.net/xing.php | osint | KEEP | Xing profile x-ray via Google — responds at probe |
| OSINT & SOCMINT Tooling | https://osint.support/chrome-extensions/2019/09/29/osint-socmint-tooling.html | osint | KEEP | OSINT/SOCMINT chrome-extension index — responds at probe |

### FACEBOOK

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| IntelTechniques Facebook | https://inteltechniques.com/tools/Facebook.html | osint | KEEP | core FB search toolkit (IntelTechniques) — responds at probe |
| Facebook Search Engine | https://cse.google.com/cse?cx=95ae46262a5f2958e | osint | KEEP | FB profile CSE |
| Facebook Photo Search Engine | https://cse.google.com/cse/publicurl?cx=013991603413798772546:jyvyp2ppxma | osint | KEEP | FB photo CSE |
| Facebook Scraped Data search | http://4wbwa6vcpvcr3vvf4qkhppgy56urmjcj2vagu2iqgp3z656xcmfdbiqd.onion.pet/ | osint | CONTEXT | scraped/leaked FB dataset search — do not visit; awareness only |
| Facebook Search | https://www.sowsearch.info/ | osint | KEEP | FB search — responds at probe 2026-08-18 |
| Facebook Search | https://www.social-searcher.com/facebook-search/ | osint | KEEP | FB keyword search — responds at probe |
| Facebook Video Downloader | https://fbdown.github.io/ | osint | KEEP | FB video downloader (github.io) |
| Facebook Search Tool | https://www.aware-online.com/osint-tools/facebook-search-tool/ | osint | KEEP | FB search methodology |
| Find My Facebook ID | https://commentpicker.com/find-facebook-id.php | osint | KEEP | FB numeric ID lookup — responds at probe |
| Facebook Geo | https://www.osintcombine.com/facebook-geo-pages | osint | DEAD-OUTDATED | 404 at probe; OSINT Combine geo tooling moved |
| Facebook Friends List Generator | https://osint.support/chrome-extensions/2019/10/20/facebook-friends-list-generator.html | osint | KEEP | FB friends-list extraction (chrome ext) |
| Facebook Entity Id Parser | https://osint.support/chrome-extensions/2019/09/08/facebook-entity-id-parser.html | osint | KEEP | FB entity ID parser (chrome ext) |
| Facebook Profile Id Grabber | https://osint.support/chrome-extensions/2019/09/01/facebook-profile-id-grabber.html | osint | KEEP | FB profile ID grabber (chrome ext) |
| Facebook Email Reverse Lookup | https://osint.support/chrome-extensions/2019/09/01/facebook-email-reverse-lookup.html | osint | KEEP | FB email reverse lookup (chrome ext) |
| Facebook Profile Directory | https://www.facebook.com/directory/ | osint | KEEP | official FB public profile directory |
| Have I Been Zucked? | https://haveibeenzucked.com/ | osint | KEEP | FB data-breach awareness — responds at probe |

### TWITTER

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| IntelTechniques Twitter | https://inteltechniques.com/tools/Twitter.html | osint | KEEP | core X search toolkit — responds at probe |
| Nitter.ca | https://nitter.ca/ | osint | KEEP | nitter instance — responding at probe 2026-08-18 (handoff flagged dead; treat as volatile) |
| Nitter.it | https://nitter.it | osint | DEAD-OUTDATED | nitter instance — no response at probe 2026-08-18 |
| BirdHunt | https://birdhunt.co/ | osint | KEEP | X posts-by-location search — responds at probe |
| Nitter Instances | https://xnaas.github.io/nitter-instances/ | osint | DEAD-OUTDATED | GitHub Pages 404 at probe — instance list moved (use community nitter instances) |
| twint | https://pypi.org/project/twint/ | osint | DEAD-OUTDATED | twint abandoned; X API changes broke it |
| Twitter Search Engine | https://cse.google.com/cse?cx=5857bab69c8b8e37e | osint | KEEP | X profile CSE |
| Tweet Finder | https://cse.google.com/cse/publicurl?cx=016621447308871563343:u4r_fupvs-e | osint | KEEP | X post CSE |
| Twitter Photo Search | https://cse.google.com/cse/publicurl?cx=006290531980334157382:_ltcjq0robu | osint | KEEP | X photo CSE |
| Tweet Archive Search | https://cse.google.com/cse/publicurl?cx=005797772976587943970:kffjgylvzwu | osint | KEEP | X archive CSE |
| Twitter Advanced Search | https://twitter.com/search-advanced | osint | KEEP | official X advanced search |
| Twitter / Profiles Directory | https://twitter.com/i/directory/ | osint | KEEP | official X profile directory |
| TweetBeaver | https://tweetbeaver.com/ | osint | DEAD-OUTDATED | domain squatted (casino spam) at probe 2026-08-18 |
| Twitter search tool | https://www.aware-online.com/en/osint-tools/twitter-search-tool/ | osint | KEEP | X search methodology |
| Google to search profiles on Twitter | https://recruitin.net/twitter.php | osint | KEEP | X profile x-ray via Google — responds at probe |
| Tweettioc.com | http://tweettioc.com/ | osint | DEAD-OUTDATED | legacy tweetstorm tool; redirects to unrelated content at probe |
| Search Twitter Bios and Profiles | https://followerwonk.com/bio | osint | KEEP | X bio search — responds at probe 2026-08-18 |
| The one million tweet map | https://onemilliontweetmap.com | osint | KEEP | geo tweet map — responds at probe (legacy viz) |
| Tweet Binder | https://www.tweetbinder.com/ | osint | KEEP | hashtag analytics — responds at probe |
| Twitter Search | https://one-plus.github.io/Twitter | osint | KEEP | X OSINT toolkit — responds at probe |
| Twitter Monitoring | https://one-plus.github.io/TwitterMonitor | osint | KEEP | X monitoring toolkit — responds at probe |
| Thread Reader | https://threadreaderapp.com/ | osint | KEEP | thread unroll/archive — responds at probe |
| Search Twitter Users | https://pushshift.io/twitter-user-search/ | osint | DEAD-OUTDATED | 404 at probe; Pushshift dropped X search |
| Find Twitter Followers | http://searchfortweets1.com/ | osint | DEAD-OUTDATED | legacy follower scraper; defunct |
| Getdewey.co | https://getdewey.co/ | osint | KEEP | X account intel — responds at probe |
| geosocial footprint | http://geosocialfootprint.com/ | osint | KEEP | geo-social footprint mapper — responds at probe |
| tweetmap | https://www.omnisci.com/demos/tweetmap | osint | DEAD-OUTDATED | no response at probe; OmniSci demo retired |
| DoesFollow | https://doesfollow.com/ | osint | KEEP | X follow-relationship checker — responds at probe |
| Sleeping Time | http://sleepingtime.org/ | osint | DEAD-OUTDATED | no response at probe; legacy sleep-time tool |
| Twitter Analytics | https://foller.me/ | osint | KEEP | X analytics — responds at probe 2026-08-18 |
| Tweet Topic Explorer | http://tweettopicexplorer.neoformix.com | osint | DEAD-OUTDATED | 2009-era visualization; defunct |
| TruthNest | https://app.truthnest.com/ | osint | KEEP | X analytics — responds at probe |
| getdaytrends | https://getdaytrends.com/ | osint | KEEP | X trends — responds at probe |
| Twitter Trending Hashtags and Topics | https://www.trendsmap.com/ | osint | DEAD-OUTDATED | no response at probe; last archive 2021 |
| Socialbearing | https://socialbearing.com/ | osint | DEAD-OUTDATED | no response at probe |
| Twiangulate: analyzing the connections between friends and followers | http://twiangulate.com/search/ | osint | KEEP | X network graph analysis — responds at probe |
| First Tweet | http://ctrlq.org/first/ | osint | DEAD-OUTDATED | 404 at probe; 'first tweet' tool gone |
| Twittertrails.com | http://twittertrails.com/ | osint | DEAD-OUTDATED | placeholder shell at probe; academic demo defunct |
| Download and Export Twitter Followers into Excel for Free | https://www.vicinitas.io/free-tools/download-twitter-followers | osint | DEAD-OUTDATED | 404 at probe; domain repurposed (FB68 spam) |

### YOUTUBE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Invidious Instances | https://docs.invidious.io/instances/ | osint | KEEP | canonical Invidious instance list — responds at probe |
| YouTube video upload time | https://www.aware-online.com/en/osint-tutorials/youtube-video-upload-time/ | osint | KEEP | upload-time estimation methodology |
| yt-dlp | https://pypi.org/project/yt-dlp/ | osint | KEEP | core downloader CLI |
| youtube-dl | https://ytdl.actionsack.com/ | osint | DEAD-OUTDATED | no response at probe; use yt-dlp |
| Location Search | https://mattw.io/youtube-geofind/location | osint | KEEP | geo-tagged video search — responds at probe |
| YouTube Metadata Bulk | https://mattw.io/youtube-metadata/bulk | osint | KEEP | channel metadata bulk export — responds at probe |
| Hadzy.com | https://hadzy.com/ | osint | KEEP | YT comment search — responds at probe |
| Youtube channel ID | https://commentpicker.com/youtube-channel-id.php | osint | KEEP | channel ID lookup — responds at probe |
| Extract Meta Data YouTube | https://citizenevidence.amnestyusa.org/ | osint | DEAD-OUTDATED | no response at probe; Amnesty Citizen Evidence Lab shuttered |
| Youtube Geo Search Tool | https://youtube.github.io/geo-search-tool/search.html | osint | KEEP | official YT geo-search demo |
| Youtube Channel Search | https://asif633.github.io/youtube-channel-search/ | osint | KEEP | channel search — responds at probe |
| YouTube search tool | https://www.aware-online.com/en/osint-tools/youtube-search-tool/ | osint | KEEP | YT search methodology |
| Yout | https://yout.com/ | osint | KEEP | YT clip/DVR — responds at probe |
| YouTube Comment Finder | https://ytcomment.kmcat.uk/ | osint | KEEP | YT comment finder — responds at probe |
| Youtube, Periscope, Twitch & Dailymotion | https://one-plus.github.io/Youtube | osint | KEEP | YT/Periscope/Twitch/Dailymotion toolkit — responds at probe |
| Unlistedvideos.com | https://unlistedvideos.com/ | osint | KEEP | unlisted-video index — responds at probe |
| Youtube Comments Downloader | https://youtubecommentsdownloader.com/ | osint | KEEP | comment export — responds at probe |

### REDDIT

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| teddit | https://teddit.net/ | osint | DEAD-OUTDATED | no response at probe; teddit unmaintained |
| Reddit Search | https://camas.unddit.com/ | osint | DEAD-OUTDATED | no response at probe 2026-08-18 (removeddit successor; down at filing) |
| Karma Decay | http://karmadecay.com/ | osint | DEAD-OUTDATED | no response at probe; image-repost search defunct |
| redditsfinder | https://pypi.org/project/redditsfinder/ | osint | KEEP | subreddit-discovery CLI |
| SocialGrep | https://www.socialgrep.com/search | osint | DEAD-OUTDATED | 523 origin unreachable at probe; Reddit API changes killed service |
| Reddit Search Tool | https://redditsearchtool.com/ | osint | KEEP | post/comment search — responds at probe |
| Search Reddit | https://bmai.dev/reddit/ | osint | KEEP | Reddit search — responds at probe |
| Reddit Archive | https://ihsoyct.github.io/ | osint | KEEP | Reddit archive — responds at probe |
| Chearch | https://adhesivecheese.github.io/chearch/ | osint | KEEP | Pushshift frontend — responds at probe |
| NY Dolls.org | https://nydolls.org/author | osint | DEAD-OUTDATED | 404 at probe; niche link gone |
| Reveddit.com | https://www.reveddit.com/ | osint | KEEP | removed-content viewer — responds at probe |
| Reddit Downloader | https://redditdownloader.github.io/ | osint | KEEP | post/media downloader — responds at probe |
| Redective | https://www.redective.com/ | osint | DEAD-OUTDATED | no response at probe |
| Reddit\_Persona | https://github.com/n2itn/reddit_persona | osint | KEEP | user persona analyzer (code) |
| Uncensor.cc | https://uncensor.cc/ | osint | DEAD-OUTDATED | no response at probe |
| Reddit Search Engine | https://cse.google.com/cse?cx=0728740ab68a619ba | osint | KEEP | Reddit CSE |
| Reddit Search Engine | https://cse.google.com/cse/publicurl?cx=017261104271573007538:bbzhlah6n4o | osint | KEEP | Reddit CSE |
| Reddit User Analyser | https://reddit-user-analyser.netlify.app/ | osint | KEEP | user stats analyzer — responds at probe |
| reddit search | https://www.redditsearch.io/ | osint | DEAD-OUTDATED | domain repurposed (vote-farming spam) at probe |
| Reddit search tool | https://www.aware-online.com/en/osint-tools/reddit-search-tool/ | osint | KEEP | Reddit search methodology |
| Pholder | https://pholder.com/ | osint | KEEP | subreddit image viewer — bot-gated at probe (403) |
| RedditMetis | https://redditmetis.com/ | osint | KEEP | user analysis — responds at probe |
| Search Reddit Comments by User | https://www.redditcommentsearch.com/ | osint | KEEP | comment-by-user search — responds at probe |
| Reddit Investigator | https://www.redditinvestigator.com/ | osint | DEAD-OUTDATED | 404 at probe |
| pushshift.io | https://pushshift.io | osint | KEEP | alive but signup-walled; API era largely over |
| Pushshift API Guide | https://github.com/pushshift/api | osint | KEEP | API docs archive (service wound down) |
| Searcheddit | http://searcheddit.com/ | osint | DEAD-OUTDATED | domain parked for sale at probe |
| Removeddit | https://removeddit.com/ | osint | DEAD-OUTDATED | defunct; use reveddit / unddit |
| Deaditarchive.netlify.app | https://deaditarchive.netlify.app/ | osint | KEEP | removeddit archive — responds at probe |
| Map of Reddit | https://anvaka.github.io/map-of-reddit/ | osint | KEEP | subreddit network viz — responds at probe |
| reddit visualization | https://yasiv.com/reddit | osint | KEEP | related-subreddit viz — responds at probe |
| ReSavr | https://www.resavr.com/ | osint | DEAD-OUTDATED | no response at probe |
| Redditle.com | https://redditle.com/ | osint | KEEP | Reddit-only search — responds at probe |
| Libredd.it | https://libredd.it/ | osint | KEEP | Reddit mirror — bot-gated at probe (403); instance volatile |

### LINKEDIN

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| LinkedIn Search | https://recruitin.net/ | osint | KEEP | LinkedIn x-ray via Google — responds at probe |
| LinkedIn X-Ray Search Tool | https://www.lisearcher.com/ | osint | KEEP | LI x-ray — 526 SSL error at probe; verify |
| LinkedProspect | https://linkedprospect.com/linkedin-boolean-search-tool/ | osint | KEEP | LI boolean search builder — responds at probe |
| LinkedIn Search Engine | https://cse.google.com/cse?cx=daaf18e804f81bed0 | osint | KEEP | LI profile CSE |
| LinkedIn Search Engine (with Images) | https://cse.google.com/cse?cx=40126f0af1aff84f8 | osint | KEEP | LI profile CSE (with images) |
| Chartloop | https://buildorgchart.herokuapp.com/ | osint | DEAD-OUTDATED | 404 'no such app'; Heroku free tier retired |
| Proxycurl | https://nubela.co/proxycurl/ | osint | KEEP | LI enrichment API — responds at probe |
| nqntnqnqmb | https://pypi.org/project/nqntnqnqmb/ | osint | KEEP | LI scraper library |
| LinkedIn Email Reverse Lookup | https://osint.support/chrome-extensions/2019/09/03/linkedin-email-reverse-lookup.html | osint | KEEP | LI email reverse lookup (chrome ext) |

### GOOGLE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Google+ Photo Custom Search | https://cse.google.com/cse/publicurl?cx=006205189065513216365:uo99tr1fxjq | osint | DEAD-OUTDATED | Google+ shut down 2019; CSE obsolete |
| GHunt | https://github.com/mxrch/GHunt | osint | KEEP | Google-account OSINT (code; maintained) |
| Google Social Search | https://www.social-searcher.com/google-social-search/ | osint | KEEP | Google social profile search — responds at probe |
| Google+ & LinkedIn | https://one-plus.github.io/G+Link | osint | DEAD-OUTDATED | Google+ dead; tool obsolete |

### DISCORD

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Discord User Search | https://discordhub.com/user/search | osint | KEEP | user search — responds at probe |
| Discord Me | https://discord.me/ | osint | KEEP | server/bot directory — responds at probe |
| Enlarge Discord avatars | https://discordzoom.com/en/ | osint | DEAD-OUTDATED | parked placeholder at probe |
| Discord History Tracker | https://dht.chylex.com/ | osint | KEEP | history tracker — responds at probe |
| DiscordOSINT | https://github.com/atoncehussein/DiscordOSINT | osint | KEEP | Discord intel tooling (code) |
| DiscordServers | https://discordservers.com/ | osint | KEEP | server directory — responds at probe |
| DISBOARD | https://disboard.org/ | osint | KEEP | server directory — bot-gated at probe (403) |
| Discord Servers Portal | https://www.discordportal.com/ | osint | DEAD-OUTDATED | domain parked for sale at probe |
| Discord ID Lookup | https://discord.id/ | osint | KEEP | ID lookup — responds at probe |
| Discord Center | https://discord.center/ | osint | DEAD-OUTDATED | 525 at probe |
| Discord Bots | https://discordbotlist.com/ | osint | KEEP | bot directory — responds at probe |
| Discord Bots | https://top.gg/ | osint | KEEP | bot directory — bot-gated at probe (403) |
| Discord Bots | https://discord.bots.gg/ | osint | KEEP | bot directory — responds at probe |

### TWITCH

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| TwitchTracker | https://twitchtracker.com/ | osint | KEEP | channel stats — responds at probe |
| Twitch.fckdmca.com | https://twitch.fckdmca.com/ | osint | DEAD-OUTDATED | no response at probe |
| Twitch Payout Search | https://sizeof.cat/project/twitch-payout-search/ | osint | DEAD-OUTDATED | no response at probe |
| Search for a Twitch channel | https://sullygnome.com/channelsearch | osint | KEEP | channel search — bot-gated at probe (403) |
| Searchstream.live | https://searchstream.live/ | osint | KEEP | live-stream filter — responds at probe |
| Twitch Tools | https://twitch-tools.rootonline.de/ | osint | KEEP | Twitch tools — responds at probe |
| Username Availability | https://cactus.tools/twitch/username | osint | KEEP | username availability — responds at probe |
| Check channel badges | https://cactus.tools/twitch/badges | osint | KEEP | channel-badge check |
| Check Twitch follow length | https://cactus.tools/twitch/followage | osint | KEEP | follow-length check |
| Twitch Following | https://cactus.tools/twitch/following | osint | KEEP | following list |
| All Twitch Streamers Search | https://twitchstats.net/allstreamers | osint | KEEP | streamer search — bot-gated at probe (403) |
| Twitchmetrics.net | https://www.twitchmetrics.net/ | osint | KEEP | streamer metrics — responds at probe |
| Twitch Username Search | https://twitchusernames.com/ | osint | DEAD-OUTDATED | no response at probe |

### INSTAGRAM

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Bibliogram.art | https://bibliogram.art/ | osint | DEAD-OUTDATED | Bibliogram project archived; frontend dead/redirecting |
| Bibliogram | https://bib.actionsack.com/ | osint | DEAD-OUTDATED | Bibliogram instance — no response at probe |
| InstaHunt | https://instahunt.co/ | osint | KEEP | location-based post search — responds at probe |
| Instagram Deep Photo Search Engine | https://cse.google.com/cse?cx=017261104271573007538:ffk_jpt64gy | osint | KEEP | IG photo CSE |
| Instagram analyzer and viewer | https://gramho.com/ | osint | DEAD-OUTDATED | no response at probe |
| Find Instagram User ID | https://codeofaninja.com/tools/find-instagram-user-id/ | osint | KEEP | IG numeric ID lookup — responds at probe |
| Instagram User ID | https://commentpicker.com/instagram-user-id.php | osint | KEEP | IG ID lookup — responds at probe |
| Searchmy.bio | https://www.searchmy.bio/ | osint | KEEP | IG bio search — responds at probe |
| Statflux | http://statflux.com/ | osint | KEEP | IG analytics — responds at probe (empty server-side title) |
| Gramsize.com | https://gramsize.com/ | osint | DEAD-OUTDATED | no response at probe |
| toutatis | https://pypi.org/project/toutatis/ | osint | KEEP | IG scraping library |
| instalooter | https://pypi.org/project/instalooter/ | osint | KEEP | IG downloader (unmaintained; prefer instaloader) |
| instaloader | https://pypi.org/project/instaloader/ | osint | KEEP | core IG downloader/archiver |
| chatter | https://github.com/visualbasic6/chatter | osint | KEEP | IG scraper (code) |
| osi.ig | https://github.com/th3unkn0n/osi.ig | osint | KEEP | IG recon (code) |
| Osintgram | https://github.com/Datalux/Osintgram | osint | KEEP | IG OSINT (code) |
| SoIG | https://github.com/yezz123/SoIG | osint | KEEP | IG OSINT CLI (code) |
| yesitsme | https://github.com/blackeko/yesitsme | osint | KEEP | IG account checker (code) |

### TELEGRAM

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Telegago | https://cse.google.com/cse?&cx=006368593537057042503:efxu7xprihg#gsc.tab=0 | osint | KEEP | TG channel/post CSE |
| Telegram Search | https://cse.google.com/cse?cx=004805129374225513871:p8lhfo0g3hg | osint | KEEP | TG CSE |
| Telegram Search. Search for posts | https://tgstat.com/search | osint | KEEP | post search + stats — responds at probe |
| Lyzem Blog | https://lyzem.com/ | osint | KEEP | TG search engine — responds at probe |
| Search.buzz.im | https://search.buzz.im/ | osint | DEAD-OUTDATED | no response at probe |
| Telegram Usernames Finder | https://socialfinder.app/list/Telegram | osint | DEAD-OUTDATED | 404 at probe |
| Telegram Channels List | https://tlgrm.eu/channels | osint | KEEP | channel directory — responds at probe |
| Readergram.com | https://readergram.com/ | osint | DEAD-OUTDATED | 500 at probe; unmaintained |
| Ixgram | https://www.telegramgroup1.com/ | osint | DEAD-OUTDATED | no response at probe (Ixgram) |
| Find Telegram Channels/Bots/Groups | https://xtea.io/ts_en.html | osint | KEEP | TG channel/group/bot search — responds at probe |
| Telegram Group: Find Telegram Channels, Bots & Groups | https://www.telegram-group.com/en/ | osint | KEEP | TG directory — responds at probe |
| TelegramDB.org | https://telegramdb.org/ | osint | KEEP | TG database — bot-gated at probe (403) |
| Global Telegram Database | https://t.me/s/privatelinks | osint | KEEP | official TG channel ('global TG database') |
| Telegram Search Engine | https://clickbee.me/Telegram-Search-Engine.html | osint | DEAD-OUTDATED | no response at probe |
| Nekogram X | https://f-droid.org/packages/nekox.messenger/ | osint | KEEP | open-source TG client (F-Droid) |

### SNAPCHAT

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Ghostcodes.com | https://www.ghostcodes.com/ | osint | DEAD-OUTDATED | 503 at probe; legacy Snapchat tool |
| Snap Map | https://map.snapchat.com/ | osint | KEEP | official Snap Map |
| Snapdex | https://snapdex.com/ | osint | DEAD-OUTDATED | no response at probe |
| SnapScraper | https://rhematt.github.io/Snap-Scraper/ | osint | KEEP | snapcode/profile scraper — responds at probe |
| snapmap-archiver | https://pypi.org/project/snapmap-archiver/ | osint | KEEP | Snap Map archive library |
| Snapchat User Search | https://sovip.io/ | osint | KEEP | Snapchat username search — responds at probe |
| SnapChat Search (ENTER-USERNAME-HERE) | https://feelinsonice.appspot.com/web/deeplink/snapcode?username=ENTER-USERNAME-HERE&size=400&type=SVG | osint | KEEP | official snapcode generator — responds at probe |

### MASTODON

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Search.noc.social | https://search.noc.social/ | osint | KEEP | federated search — responds at probe |
| Mastodon Search Engine | https://cse.google.com/cse?cx=334aec4c3c73ed945 | osint | KEEP | Mastodon CSE |

### TIKTOK

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| TIKTOK Search Engine | https://cse.google.com/cse?cx=011444696387487602669:aqf7d9w73om | osint | KEEP | TikTok CSE |
| TikTok User Search | https://vidnice.com/search/ | osint | DEAD-OUTDATED | no response at probe |
| TikTok downloader | https://tiktokd.com/ | osint | DEAD-OUTDATED | no response at probe |

### STEAM

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Steam Community :: Search | https://steamcommunity.com/search/users/ | osint | KEEP | official Steam user search |
| Steam ID Finder | https://steamidfinder.com/lookup/ | osint | KEEP | Steam ID lookup — bot-gated at probe (403) |
| steamdb.info/calculator | https://steamdb.info/calculator/ | osint | KEEP | account-value calculator (official) |

### CLUBHOUSE

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Clubhouse Database | https://clubhousedb.com/ | osint | DEAD-OUTDATED | Clubhouse original app shut down 2025; era tool dead |
| Rooms of Clubhouse | https://roomsofclubhouse.com/ | osint | DEAD-OUTDATED | Clubhouse original app shut down 2025; era tool dead |
| ClubSearch -- search Clubhouse rooms | https://clubsearch.io/ | osint | DEAD-OUTDATED | Clubhouse original app shut down 2025; era tool dead |

### ONLYFANS

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Onlysearch.co | https://onlysearch.co/ | osint | KEEP | OF profile search — responds at probe |
| OnlyFinder | https://onlyfinder.com/ | osint | KEEP | OF profile search — bot-gated at probe (403) |
| Search OnlyFans profiles | https://hubite.com/onlyfans-search/ | osint | KEEP | OF search — bot-gated at probe (403) |
| Fansmetrics.com | https://fansmetrics.com/ | osint | KEEP | OF stats — bot-gated at probe (403) |
| Findr.fans | https://findr.fans/ | osint | KEEP | OF search — responds at probe |
| SimilarFans | https://similarfans.com/ | osint | KEEP | OF similar-account search — redirects at probe; alive |

### BOT

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Bot Sentinel Dashboard ‹ Bot Sentinel | https://botsentinel.com | osint | KEEP | X bot/coordinated-account detection — bot-gated at probe (403) |
| Botometer by OSoMe | https://botometer.osome.iu.edu/ | osint | KEEP | X bot scoring — responds at probe |
| FollowerAudit | https://www.followeraudit.com/ | osint | KEEP | X follower-quality audit — responds at probe |
| Twitter Bot Checker | https://circleboom.com/twitter-management-tool/twitter-circle-tool/twitter-bot-checker | osint | KEEP | X bot checker — responds at probe |
| BotSlayer | https://osome.iu.edu/tools/botslayer | osint | KEEP | coordination detection (OSoMe) — responds at probe |

### BLOG

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Blogs Search Engine | https://cse.google.com/cse?cx=013991603413798772546:8c1g6f0frp8#gsc.tab=0 | osint | KEEP | blog CSE |
| WordPress Content Snatcher | https://cse.google.com/cse/publicurl?cx=011081986282915606282:w8bndhohpi0 | seo | KEEP | WordPress content CSE (seo-wiki) |
| WordPress Custom Search | https://cse.google.com/cse?cx=011081986282915606282:w8bndhohpi0 | seo | KEEP | WordPress CSE (seo-wiki) |
| OSINT Blogs Search Engine | https://cse.google.com/cse?cx=fd4729049350a76d0 | osint | KEEP | OSINT blog CSE |

### NEWS

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| News Search Engine | https://cse.google.com/cse?cx=013991603413798772546:fvmtax6anhd | osint | KEEP | news CSE |
| Mailing List Archives Search Engine | https://cse.google.com/cse/publicurl?cx=013991603413798772546:sipriovnbxq | osint | KEEP | mailing-list archives CSE |
| Google News | https://news.google.com/ | osint | KEEP | official Google News |
| News Search | https://upstract.com/search | osint | KEEP | news search — responds at probe |
| Newslookup.com | http://newslookup.com/ | osint | KEEP | news search — responds at probe |
| Welcome to Dealstrap! | http://correctsearch.com/ | osint | DEAD-OUTDATED | parked/placeholder at probe (title 'Welcome to Dealstrap!') |
| Beautiful News | https://informationisbeautiful.net/beautifulnews/ | osint | KEEP | positive-news viz — responds at probe |
| GoodGopher.com | https://goodgopher.com/ | osint | KEEP | privacy news search — responds at probe |
| Newsnow | https://www.newsnow.co.uk/ | osint | KEEP | UK news aggregator — responds at probe |
| Wintria | http://www.wintria.com/ | osint | KEEP | news aggregator — bot-gated at probe (403) |
| Mereku.com | https://mereku.com/ | osint | DEAD-OUTDATED | domain squatted (casino spam) at probe |
| Newspapers.com | https://www.newspapers.com/ | osint | KEEP | newspaper archive — responds at probe |
| Newspaper Archive | https://www.gastearsivi.com/en/ | osint | KEEP | Turkish newspaper archive — bot-gated at probe (403) |
| Talkwalker | https://www.talkwalker.com/alerts | osint | KEEP | social alerts — responds at probe |
| Google Alerts | https://www.google.com/alerts | osint | KEEP | official Google Alerts |
| Paperball.news | https://paperball.news/ | osint | DEAD-OUTDATED | no response at probe |
| Hoaxy: How claims spread online | https://hoaxy.osome.iu.edu/ | osint | KEEP | claim-spread viz — responds at probe |
| Snopes | https://www.snopes.com/?s= | osint | KEEP | fact-checking — official |
| ReviewMeta | https://reviewmeta.com/ | osint | KEEP | Amazon review analysis — bot-gated at probe (403) |
| Verification Handbook | https://datajournalism.com/read/handbook/verification-1 | osint | KEEP | verification handbook — responds at probe |
| Truth or Fiction | https://www.truthorfiction.com/ | osint | KEEP | fact-checking — responds at probe |
| Debunking False Stories Archives | https://www.factcheck.org/fake-news/ | osint | KEEP | fact-checking — responds at probe |
| Fact-Checking | https://reporterslab.org/fact-checking/ | osint | KEEP | fact-check directory — responds at probe |

### NEWS FROM REDDIT

*No links on board.*

### ANALYTICS

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| SEO Resources Search Engine | https://cse.google.com/cse/publicurl?cx=005797772976587943970:i7q6z1kjm1w | seo | KEEP | SEO resource CSE (seo-wiki) |
| Hashatit | https://www.hashatit.com/ | osint | DEAD-OUTDATED | no response at probe |
| Social Mentions | https://www.social-searcher.com/media-monitoring/ | osint | DEAD-OUTDATED | 404 at probe; vendor alive (sister pages live) |
| Social Trends | https://www.social-searcher.com/social-trends/ | osint | KEEP | social trends — responds at probe |
| Mentionmapp Analytics | https://mentionmapp.com/ | osint | DEAD-OUTDATED | domain repurposed (redirects to thulatula.com) at probe |
| Anonymous Ad Preview Tool | https://ads.google.com/anon/AdPreview | osint | KEEP | official anonymous ad preview — no probe response (Google-gated) |
| Semrush | https://www.semrush.com/ | seo | KEEP | SEO/competitor analytics (commercial; seo-wiki) |
| Network Tool | https://osome.iu.edu/tools/networks/#/ | osint | KEEP | network viz (OSoMe) — responds at probe |
| Trends Tool | https://osome.iu.edu/tools/trends/#/ | osint | KEEP | trends tool (OSoMe) — responds at probe |
| CoVaxxy | https://osome.iu.edu/tools/covaxxy | osint | KEEP | vaccine-claim misinformation tracker (OSoMe) — responds at probe |

## Snippets

> Group `04-socmint`: 257 links across 22 sections (SOCIAL MEDIA, FACEBOOK, TWITTER, YOUTUBE, REDDIT, LINKEDIN, GOOGLE, DISCORD, TWITCH, INSTAGRAM, TELEGRAM, SNAPCHAT, MASTODON, TIKTOK, STEAM, CLUBHOUSE, ONLYFANS, BOT, BLOG, NEWS, NEWS FROM REDDIT (empty), ANALYTICS). Nested hub: https://start.me/p/Wp1kpe/socmint. [Source: `.local/osint4all/groups/04-socmint.json` / OSINT4ALL start.me L1rEYQ (retrieved 2026-08-18)]

Liveness probe 2026-08-18: nitter/invidious-style instances and legacy X/IG-era tools are volatile — re-verify before operational use. Core KEEP anchors: IntelTechniques social tools, RecruitEm x-ray, X CSE suite, Followerwonk bio, reveddit/unddit-class Reddit tooling, tgstat/Lyzem/xtea (Telegram), instaloader/Osintgram (IG), OSoMe bot tools, OnlyFans search set.
