---
title: OSINT4ALL identity / anonymity catalog
type: entity
tags: [osint, catalog, osint4all, k241]
keywords: [OSINT4ALL, throwaway email, alias email, fake identity, emulator, privacy guides, Signal, Tor, ProtonVPN, K241]
related:
  - sources/osint4all-startme-2026-08-18.md
  - entities/tools/osint4all.md
  - concepts/osint4all-catalog.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @sources/osint4all-startme-2026-08-18.md — ingest source (K241)
- @entities/tools/osint4all.md — hub entity
- @concepts/osint4all-catalog.md — KEEP / DEAD / CONTEXT / CAUTION filing rules

## Raw Concept

OSINT4ALL group `01-identity-anon` (97 links, 5 sections: throwaway contact, ID generator, sandbox/emulator, privacy/security, secure communication) from the L1rEYQ start.me board, mirrored 2026-08-18. One catalog page — not a stub farm. Public privacy and sockpuppet-tradecraft locators stay KEEP; fake-ID / SSN generators stay KEEP with a dual-use caveat (locator, not a crime how-to); known-dead P2P desks and the 2021 Threader.app corpse are DEAD-OUTDATED. No leak, darknet, or malware URLs in this pack.

## Narrative

File this board as locators for authorized OSINT tradecraft: disposable contact, synthetic personas, Android sandboxes, OpSec guides, and E2EE / anonymity clients. Do not treat generators as a document-fraud playbook. Nested start.me hubs: **none** in this group.

### THROWAWAY CONTACT

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| 10minutemail.com | https://10minutemail.com/ | osint | KEEP | Classic disposable inbox for throwaway signups |
| AnonAddy | https://anonaddy.com/ | osint | KEEP | Alias email (rebranded addy.io); inbox isolation |
| SimpleLogin | https://simplelogin.io/ | osint | KEEP | Alias email (Proton-owned); inbox isolation |
| MailDrop | https://maildrop.cc/ | osint | KEEP | No-account disposable inbox |
| Send text free | https://globfone.com/send-text/ | osint | KEEP | Browser SMS/call without a SIM |
| SendaText | https://www.sendatext.co/ | osint | KEEP | Browser SMS without a SIM |
| Free Fax | https://faxzero.com/ | osint | KEEP | Free web fax (ad cover page) |
| Receive SMS Online | http://receive-sms-online.com/ | osint | KEEP | Public shared SMS inbox; numbers recycle |
| Receive-sms-now.com | http://receive-sms-now.com/ | osint | KEEP | Public shared SMS inbox; numbers recycle |
| Receive SMS Online | https://hs3x.com/ | osint | KEEP | Public shared SMS inbox; numbers recycle |
| Receive SMS Online for FREE | http://freesmsverification.com/ | osint | KEEP | Public shared SMS inbox; numbers recycle |
| Smstome.com | https://smstome.com | osint | KEEP | Public shared SMS inbox; numbers recycle |
| Amazon SNS | https://aws.amazon.com/sns/ | osint | KEEP | Commercial SMS/push API — not a public inbox |
| Twilio | https://www.twilio.com/ | osint | KEEP | Commercial programmable SMS/voice API |
| One-time Mobile by @OsintStash | https://threader.app/thread/1199785692274077696 | skip | DEAD-OUTDATED | Threader.app shut down Dec 2021 (Twitter acquisition); 2019 thread corpse |

### ID GENERATOR

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Username Generator | https://www.lastpass.com/features/username-generator | osint | KEEP | Random username for sockpuppet handles |
| Fake Name Generator | https://www.fakenamegenerator.com/ | osint | KEEP | Synthetic persona (name/address/profile) |
| Resume Generator | https://thisresumedoesnotexist.com/ | osint | KEEP | AI/GAN fake-resume locator |
| International Name Generator | https://www.behindthename.com/random/ | osint | KEEP | Culture-accurate random given names |
| Windows Phone IMEI Generator | https://wpimeigenerator.github.io/ | osint | KEEP | IMEI Luhn toy (Windows Phone-era) |
| IMEI Number Generator | https://dyrk.org/tools/imei/ | osint | KEEP | IMEI checksum generator |
| US SSN / Driver License / State ID / Passport / Tax ID Generator | https://www.elfqrin.com/usssndriverlicenseidgen.php | osint | KEEP | Synthetic ID locator; dual-use — tradecraft, not a crime how-to |
| Washington State Driver's License Generator | https://mmarvick.github.io/wa-drivers-license/ | osint | KEEP | WA DL number algorithm locator; dual-use — not a crime how-to |
| Fake Drivers License Generator | https://fakeinfo.net/drivers-license-generator | osint | KEEP | Synthetic DL locator; dual-use — not a crime how-to |
| This Rental Does Not Exist | https://thisrentaldoesnotexist.com/ | osint | KEEP | GAN fake rental listing (cover-story photos) |
| Face Photo Generator | https://thispersondoesnotexist.com/ | osint | KEEP | StyleGAN face for sockpuppets |
| Random Face Generator | https://fakeinfo.net/random-face-generator | osint | KEEP | Synthetic face photos |
| Credit Card Generator | https://www.fakenamegenerator.com/credit-card-validator.php | osint | KEEP | Luhn test-card locator; dual-use — not payment fraud |
| PIC/CIC Code Database | https://www.allredtech.com/ | osint | KEEP | Telecom PIC/CIC carrier-code lookup |
| SIN Generator | https://www.fakenamegenerator.com/social-insurance-number.php | osint | KEEP | Canadian SIN locator; dual-use — not a crime how-to |
| ABA Generator | https://www.fakenamegenerator.com/aba-validator.php | osint | KEEP | ABA routing-number locator; dual-use — not a crime how-to |
| VIN Generator | https://www.fakenamegenerator.com/vehicle-identification-number.php | osint | KEEP | VIN checksum locator; dual-use — not a crime how-to |
| NINO Generator | https://www.fakenamegenerator.com/national-insurance-number.php | osint | KEEP | UK NINO locator; dual-use — not a crime how-to |
| SSN Generator | https://www.fakenamegenerator.com/social-security-number.php | osint | KEEP | US SSN locator; dual-use — not a crime how-to |
| IID Generator by Georgy Bunin | https://georgybu.github.io/IID_Generator/ | osint | KEEP | Israeli ID checksum locator; dual-use — not a crime how-to |
| GUID/UUID and short GUID generator | https://richardkundl.github.io/shortguid/ | osint | KEEP | UUID / short-GUID mint |
| Nano ID CC | https://zelark.github.io/nano-id-cc/ | osint | KEEP | Nano ID collision-odds calculator |
| Generate SA ID Numbers | https://chris927.github.io/generate-sa-idnumbers/ | osint | KEEP | South African ID locator; dual-use — not a crime how-to |
| Decoding Social Security Numbers | https://stevemorse.org/ssn/ssn.html | osint | KEEP | SSN area/group decode (Steve Morse One-Step) |
| Encoding and Decoding Driver's License Numbers | https://stevemorse.org/dl/dl.html | osint | KEEP | State DL algorithm decode (Steve Morse One-Step) |
| Dating Profile Generator | https://www.dating-profile-generator.org.uk/ | osint | KEEP | Synthetic dating-bio text |
| Fake Identity ID Random Name Generator | https://www.elfqrin.com/fakeid.php | osint | KEEP | Synthetic persona bundle; dual-use — not a crime how-to |
| Fake Company Name Generator | https://fakeinfo.net/company-name-generator | osint | KEEP | Synthetic company-name locator |
| Twitter Profile Generator | https://fakeinfo.net/fake-twitter-profile-generator | osint | KEEP | Synthetic X/Twitter profile kit |
| Fake Tiktok Profile Generator | https://fakeinfo.net/fake-tiktok-profile-gererator | osint | KEEP | Synthetic TikTok profile kit (board URL has a typo) |
| Fake Youtube Channel Generator | https://fakeinfo.net/fake-youtube-channel-generator | osint | KEEP | Synthetic YouTube channel kit |
| Resume Builder | https://vinaysomawat.github.io/Resume-Builder/ | osint | KEEP | GitHub Pages resume builder (not a fake-ID mill) |
| Fake Generator Tools | https://fauxid.com/tools | osint | KEEP | Fake-ID tool index; dual-use — locators, not a crime how-to |

### SANDBOX / EMULATOR

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Kasm | https://kasmweb.com/ | osint | KEEP | Isolated browser/desktop streaming for investigation sandboxes |
| Bluestacks | https://www.bluestacks.com/ | osint | KEEP | Android emulator for app / SOCMINT work |
| Genymotion | https://www.genymotion.com/ | osint | KEEP | Android emulator (dev / investigation) |
| PrimeOS | https://www.primeos.in/ | osint | KEEP | Android-x86 OS for PC (x86 builds poorly maintained) |
| BigNox | https://www.bignox.com/ | osint | KEEP | NoxPlayer Android emulator |
| Memuplay.com | https://www.memuplay.com/ | osint | KEEP | MEmu Android emulator |
| Ldplayer.net | https://www.ldplayer.net/ | osint | KEEP | LDPlayer Android emulator |

### PRIVACY / SECURITY

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Privacy Services by Michael Bazzell | https://inteltechniques.com/workbook.html | osint | KEEP | IntelTechniques privacy workbook |
| Privacy Guides | https://privacyguides.org/ | osint | KEEP | Independent privacy-tool recommendations hub |
| Surveillance Self-Defense | https://ssd.eff.org/ | osint | KEEP | EFF Surveillance Self-Defense |
| gofoss.net | https://gofoss.net/ | osint | KEEP | FOSS privacy / self-hosting guides |
| Consumer Reports Security Planner | https://securityplanner.consumerreports.org/ | osint | KEEP | Consumer Reports personal-security planner |
| Security in a Box | https://securityinabox.org/en/ | osint | KEEP | Tactical Tech digital-security kits |
| Counter-OSINT guide for Russians | https://github.com/soxoj/counter-osint-guide-ru | osint | KEEP | soxoj counter-OSINT playbook (RU; defensive) |
| PRISM Break | https://prism-break.org/en/ | osint | KEEP | Anti-surveillance software directory (stale but live) |
| Security First - Umbrella | https://secfirst.org/umbrella/ | osint | KEEP | Field digital/physical-security handbook app |
| Matweb.info | https://matweb.info/ | osint | KEEP | Online metadata stripper |
| Metacleaner.com | https://metacleaner.com/ | osint | KEEP | Online metadata stripper |
| Image Scrubber | https://everestpipkin.github.io/image-scrubber/ | osint | KEEP | Client-side protest-photo EXIF / blur scrubber |
| View Exif data online, remove Exif online | http://www.verexif.com/en/ | osint | KEEP | Browser EXIF view / strip |
| Bitcoinprivacy.guide | https://bitcoinprivacy.guide/ | osint | KEEP | Bitcoin privacy primer |
| LocalBitcoins | https://localbitcoins.com/ | skip | DEAD-OUTDATED | P2P BTC marketplace shut down Feb 2023 |
| Localmonero.co | https://localmonero.co/ | skip | DEAD-OUTDATED | P2P XMR marketplace wound down 2024 (site gone by Nov 2024) |
| Bitonic | https://bitonic.nl/en/ | osint | KEEP | Dutch BTC broker (KYC; still operating) |
| Paxful | https://paxful.com/ | skip | DEAD-OUTDATED | P2P marketplace wound down 1 Nov 2025 |
| Speech Jammer | https://mynoise.net/NoiseMachines/audioJammerNoiseGenerator.php | osint | KEEP | Delayed-audio jammer (in-person) |
| Stutterbox | https://www.stutterbox.co.uk/ | osint | KEEP | Delayed-audio speech jammer |
| StegOnline | https://stegonline.georgeom.net/upload | osint | KEEP | Browser steganography analyze / embed |
| The Hitchhiker’s Guide to Online Anonymity | https://anonymousplanet.org/guide.html | osint | KEEP | Long-form anonymity / OpSec guide |

### SECURE COMMUNICATION

| Name | URL | Wiki | Disposition | Why |
|------|-----|------|-------------|-----|
| Signal | https://signal.org/ | osint | KEEP | Default E2EE messenger |
| Element | https://element.io/ | osint | KEEP | Matrix client |
| Briar | https://briarproject.org/ | osint | KEEP | Peer-to-peer messenger (no central server) |
| Jami.net | https://jami.net/ | osint | KEEP | Distributed messenger / SIP |
| Jitsi Meet | https://meet.jit.si/ | osint | KEEP | Browser video conference |
| Rocket.Chat | https://rocket.chat/ | osint | KEEP | Self-hostable team chat |
| Wire | https://wire.com/en/ | osint | KEEP | E2EE messenger (enterprise option) |
| Nekogram.app | https://nekogram.app/ | osint | KEEP | Unofficial Telegram Android fork |
| Telegram | https://www.telegram.org/ | osint | KEEP | Cloud messenger (secret chats optional) |
| Brave Talk | https://talk.brave.com/ | osint | KEEP | Browser video via Brave |
| The Tor Project | https://www.torproject.org/download/ | osint | KEEP | Tor Browser download |
| Brave Browser | https://brave.com/ | osint | KEEP | Chromium + shields |
| Psiphon | https://www.psiphon.ca/ | osint | KEEP | Censorship circumvention (VPN / SSH / obfs) |
| ProtonVPN | https://protonvpn.com/ | osint | KEEP | Proton VPN |
| hide.me VPN | https://hide.me/en/ | osint | KEEP | Commercial VPN |
| AdGuard VPN | https://adguard-vpn.com/en/welcome.html | osint | KEEP | Commercial VPN |
| I2P | https://geti2p.net/en/download | osint | KEEP | Invisible Internet Project (anonymity network) |
| VPN Services | https://privacyguides.org/providers/vpn/ | osint | KEEP | Privacy Guides VPN-provider recommendations |
| Browser Recommendations | https://privacyguides.org/browsers/ | osint | KEEP | Privacy Guides browser recommendations |
| Getsession.org | https://getsession.org/ | osint | KEEP | Session messenger (Oxen) |

## Counts

| Disposition | n |
|-------------|---|
| KEEP | 93 |
| DEAD-OUTDATED | 4 |
| CONTEXT | 0 |
| CAUTION | 0 |
| NESTED-HUB | 0 |
| **Rows** | **97** |

| Section | n |
|---------|---|
| THROWAWAY CONTACT | 15 |
| ID GENERATOR | 33 |
| SANDBOX / EMULATOR | 7 |
| PRIVACY / SECURITY | 22 |
| SECURE COMMUNICATION | 20 |

Source JSON: `.local/osint4all/groups/01-identity-anon.json` (`n_links=97`). Nested start.me hubs: none.
