---
title: "MyIP — IP Toolbox with WebRTC Leak Detection (jason5ng32)"
type: entity
tags: [osint, ip-geolocation, webrtc, proxy-detection, maxmind, vue, mit, steal-from-tier]
keywords: [myip, ip-toolbox, webrtc-leak, dns-leak-test, proxy-detection, maxmind-geolite2, stun]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations
- @cybersecurity-wiki/briefs/2026-05-15_myip-dns-leak-cybersec.md  (cross-wiki brief)

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Steal-from tier, OSINT wiki primary fit

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). MIT-licensed, 10.4k stars, sponsored by DigitalOcean and Cloudflare. Vue/Node.js IP toolbox with WebRTC local IP exposure detection, multi-source IPv4/IPv6 geolocation, and proxy rule testing.

## Narrative

MyIP implements WebRTC UDP leak detection via STUN servers, DNS exit endpoint identification using newly generated domain names, and MaxMind GeoLite2 database integration. These network utility functions should be extracted, decoupled from the Vue/Node.js frontend, and recoded in Python for the OSINT wiki's kb-server REST API to enhance threat-actor financial profiling.

**Tier: Steal-from** — extract the WebRTC leak detection logic and DNS leak test methodology; recode in Python. Do NOT deploy the full Vue/Node.js frontend (architectural bloat vs. /opt/cemini backend paradigm). MIT license is safe for extraction and proprietary modification. Cross-wiki routing: catalog DNS leak test endpoints and VPN infrastructure profiling methods in Cybersec wiki.
