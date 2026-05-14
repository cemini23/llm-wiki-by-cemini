---
title: "awesome-osint-arsenal (rawfilejson) — Kali-Linux OSINT toolkit installer collection [REJECTED]"
type: entity
category: tool
tags: [entity, tool, awesome-list, osint-tools, kali-linux, k44, reject, no-license, ip-sale-poison]
keywords: [awesome-osint-arsenal, rawfilejson, no-license, kali-linux, blueteam-script, forensics-script, ip-sale-reject]
related:
  - sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md
  - concepts/cemini-license-posture.md
maturity: rejected
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (REJECT verdict)
- @concepts/cemini-license-posture.md — no-license = hard-reject under IP-sale posture

## Raw Concept

A shell-script aggregator (100% Shell) that installs 100+ intelligence-gathering utilities on Kali Linux platforms. Includes `osint.sh`, `blueteam.sh`, `forensics.sh`. **422 stars but NO LICENSE FOUND** per K44 doc-level eval. Verdict: **Reject**.

## Narrative

K44 thematic fit: OSINT-wiki. Cross-routing: none.

**Why rejected**: The total absence of a license declaration places this asset outside Cemini's IP-sale posture (per `@concepts/cemini-license-posture.md`). Executing or embedding unlicensed shell scripts into proprietary infrastructure introduces legal vulnerability to the impending suite transfer. No pattern extraction either — "Steal-from" still requires a permissive license on what's being stolen.

**Reconsideration trigger**: only if upstream maintainer adds an MIT/Apache-2.0 LICENSE file in the future. Until then, this is a hard dead-end.

## Dead Ends

- **K44 considered topical alignment with OSINT-wiki but rejected on license discipline alone.** Same posture as awesome-prediction-market-tools and Awesome-Prediction-Market-Tools-aarora4 — the "no LICENSE file" reject pattern applies uniformly.
