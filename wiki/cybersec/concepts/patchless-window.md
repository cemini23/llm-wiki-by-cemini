---
title: "The patchless window: public fix before public CVE"
type: concept
related:
  - sources/newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md
  - concepts/software-maintenance-institutional-insecurity.md
  - concepts/responsible-disclosure.md
  - concepts/llm-vulnerability-discovery.md
  - sources/substack-rss-secpro-2026-11-06-five-issues-the-php-crisis-has-brought-into-view.md
updated: 2026-11-14
---

## Raw Concept

Question: **how long does a defender have between a public open-source fix and the CVE that triggers a scanner?** From Second Security research, reported in tl;dr sec #354.

## Narrative

Open-source fixes land in public commits. A CVE usually follows later. Between those two events there is a window where the vulnerability is patchable and invisible to vulnerability management. The window has a name in the source material, and it has a measured trend.

### The measurement

| Month (2026) | Median gap, public fix to CVE publication |
|---|---|
| January | 5.1 days |
| August | 39.2 days |

The sample is 18,594 CVEs. Exploit publication does not wait for the CVE. Public exploits appeared within hours of the fix. The fastest cases were 4–16 hours. The fastest tenth of all public exploits arrived within 1.8 days.

`[TENTATIVE]` — single-source reporting. `[NEEDS VERIFICATION 2026-11-14]` against the primary study.

### Why the window exists

- A fix commit is a diff. A diff is a description of the bug.
- A CVE identifier requires coordination, an assigner, a description and a publication step.
- Scanners and vulnerability feeds key on the CVE identifier, not on the commit.

AI lowers the cost of reading a diff and writing a proof of concept. The window therefore matters more than it did, because the attacker side of it is now fast and cheap.

### The defender's control set

| Control | Effect |
|---|---|
| Track upstream commits, not only CVE feeds | Closes the visibility gap |
| Watch security-relevant commits in dependencies | Detects fixes before the advisory |
| Enable dependency-diff or lockfile review in CI | Surfaces version moves early |
| Coordinate backports to the deployed branch | Converts the upstream fix into protection |
| Measure deployed version, not "available" | Distinguishes patch available from service fixed |

The last row repeats the lesson from the PHP2Shell disclosure wave: "patched in main" is not "users are protected."

### Backport debt makes the window permanent

Upstream stable branches carry large known-unfixed sets. Reported figures `[TENTATIVE]`:

| Target | Unfixed CVEs |
|---|---|
| Ubuntu 26.04 | 770 across 1,028 packages, 43.5% high or critical |
| Debian 13 | 4,562 across 1,128 packages, 39.9% high or critical |
| Stable kernel 5.10.y | more than 2,000 |

An AI-assisted backport effort produced 142 fixes for 90 CVEs in stable kernel trees, which shows the work is automatable. The debt remains a standing exposure surface for any long-term-support user.

### Detection and monitoring ideas

- Alert on a new CVE that names a package version already deployed, and note the fix commit date if available.
- Track the publication lag as a metric. A rising lag means more time spent exposed.
- Include commit-level monitoring for the small set of components that carry the most risk.

## Snippets

> "The gap between when an open source vulnerability fix becomes public and when its CVE is published, finding it grew from 5.1 days in January 2026 to 39.2 days in August across 18,594 CVEs." [Source: newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md]

> "Public exploits appeared within hours of fixes (fastest examples: 4-16 hours), while the fastest tenth of all public exploits arrived in just 1.8 days." [Source: newsletter-rss-tldrsec-2026-11-12-tldr-sec-354---artex-agentic-hacking-in-the-wild.md]
