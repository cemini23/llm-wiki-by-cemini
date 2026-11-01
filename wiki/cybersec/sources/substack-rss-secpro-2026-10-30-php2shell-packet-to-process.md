---
title: "PHP2Shell: packet-to-process evidence of code execution"
type: source
tags: [source, newsletter, php2shell, incident-response, detection]
related: []
maturity: draft
read_status: read
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | PHP2Shell, packet to process |
| Source | Packt SecPro (secpro) |
| File | `substack-rss-secpro-2026-10-30-php2shell-packet-to-process.md` |
| Retrieved | 2026-11-01 |
| URL | https://secpro.substack.com/p/php2shell-packet-to-process |
| Read status | read |

## Narrative

Packt SecPro frames PHP2Shell as a problem of evidence. A dashboard of suspicious requests, a vendor exploitation notice, and a proof of concept can merge into one settled story. This follow-up asks how a defender shows that an attacker executed code. The inbox file dates the post to 2026-10-30. The authors review published sources. They state that they did not reconstruct the full packet corpus.

The post cites Adel Karimi’s 24 October honeypot report, published as 0x4D31. That report links 35 execution-stage requests to 35 Apache-parented shell starts across three targets. The post calls this strong evidence of execution on those systems. It says the report supplies no estimate of compromise elsewhere. These counts come from that one cited report. This newsletter adds no independent count.

The post names two Critical issues. Each advisory rates the issue CVSS v4.0 9.2. CVE-2026-109618 concerns memory exhaustion that interrupts PHP while internal request structures are invalid. Request cleanup can then consume those structures. PHP identifies mod_php as the highest-risk deployment. CVE-2026-109619 concerns request-owned memory that persistent worker state still references after release. In one representative chain from the honeypot report, the decoded body sizes were 1,060,211; 33,128,677; 279,369; and 451,384 bytes. The post says these sizes are observed values from that chain. They are single-source figures from the cited report.

The post cites a Fastly sample. In that sampled hour, React2Shell accounted for 98.6% of matches to one circulating PHP2Shell signature and 99.9% of matches to another. The post says these rates describe Fastly’s sample. They are single-source sample figures, and the post does not present them as universal false-positive rates. The same honeypot report records 52 unusually large session cookies. Each cookie decodes to 819,200 bytes. The report confirms client acknowledgement for 51 complete responses. The post associates the observed chain with CVE-2026-109618. It says the report does not establish a distinct CVE-2026-109619 path. The cookie counts are single-source figures from that report.

The post calculates two intervals from the honeypot timestamps. The shell starts 0.435 seconds after the execution-stage request began. The segmentation fault follows 0.706 seconds after the shell start. The post says these intervals come from the report. They are single-source figures, and the post does not present them as independent performance measurements. On disclosure, the post reports attributed positions. Dan Lorenc says reports of exploitation informed his decision to publish fixed builds before the coordinated release. Nils Adermann says the coordination channel contained reports of probing and attempted exploitation, with no confirmed successful exploitation at release time. Marcus Hutchins criticises the unilateral embargo decision. PHP’s 21 October fixed releases are 8.2.35, 8.3.36, 8.4.27, and 8.5.12. A separate 23 October notice, CVE-2026-115560, does not establish another exploitation path in the honeypot dataset, according to the post.

A defensive reader can use the post as an evidence ladder. A captured request, a memory-pressure error, a disclosure response, and a process event answer different questions. The post says an exact final-payload match is fragile because execution-stage content varied by target and command. For an AI-safety reader, the post adds a check on public tools. A tool that needs a separate local file inclusion weakness is not, by the post’s claim, automatic evidence of PHP-engine exploitation. The post says responders should label a probe, an attempted exploit, a laboratory demonstration, and observed execution as separate facts. Containment of a dangerous exposure can proceed while the record states which decision is precautionary, which finding is established, and which question stays open.

## Snippets

> "This follow-up asks a narrower question: how do we establish that an attacker executed code? The starting point is Adel Karimi’s 24 October honeypot report, published as 0x4D31." [Source: https://secpro.substack.com/p/php2shell-packet-to-process (retrieved 2026-11-01)]
