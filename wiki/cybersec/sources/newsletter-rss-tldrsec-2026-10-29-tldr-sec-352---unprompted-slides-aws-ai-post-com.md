---
title: "tl;dr sec #352 — Unprompted talks, AWS LLM post-compromise, malicious routers"
type: source
tags: [source, newsletter, ai-security, cloud-security, llm-supply-chain]
related: []
maturity: draft
read_status: read
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [tl;dr sec] #352 - Unprompted Slides, AWS AI Post-compromise Trends, Malicious LLM API Routers |
| Source | tl;dr sec |
| File | `newsletter-rss-tldrsec-2026-10-29-tldr-sec-352---unprompted-slides-aws-ai-post-com.md` |
| Retrieved | 2026-11-01 |
| URL | https://tldrsec.com/p/tldr-sec-352 |
| Read status | read |

## Narrative

This issue is tl;dr sec #352. The file header dates it 2026-10-29. Clint wrote it while he was at [un]prompted, an AI and security conference that Gadi Evron and a CFP crew organize. He says the conference CTF encourages AI use, and perhaps requires it. He says the videos and slides will be released later, and he links a few talks before that release.

Tim de Waal's talk walks through an AI-assisted patch of a command injection and an SQL injection in ASUS router firmware. The newsletter says he used GPT-5.6 Sol and Daybreak Blue on a personal account, and that the work used 7% of a weekly Pro allowance. Kat Traxler's talk reports about 100 design-flaw bugs in cloud providers. She defined a Security Constitution of principles. Models generate hypotheses from those principles and then try to validate or disprove them. One principle is that authorization exists at every trust boundary. After the system finds one vulnerability, it abstracts a shape and looks for that shape at other cloud providers. The bug count and the allowance figure are single-source claims in this newsletter.

Binary Security's Haakon Wik Gulbrandsrud describes four more critical vulnerabilities in Azure API Connections, a part of Azure Logic Apps. The newsletter says the bugs allowed cross-tenant compromise of Key Vaults, SQL databases, and other connected services, and that they earned $200,000 in bug bounties. Azure checks that the caller can use their own connection. He then redirected the later privileged request to another person's connection, for example with path traversal, and used the stored credentials. The newsletter says Microsoft's fixes were bypassed through path normalization timing issues and undocumented API endpoints. The same issue links KillaBoi/StealMyBitcoin-PoC and says that tool gets remote code execution on Alpine PHP 8.4.26 and lands about seven out of ten local lab runs, depending on which worker handles each pipelined request. It also links rikugan, which embeds a multi-provider LLM in IDA Pro and Binary Ninja and uses profiles to limit tool access and data visibility. The bounty figure and the lab success rate are single-source claims here.

Adan Alvarez tested 14 LLMs across 13 post-compromise AWS scenarios, with 20 responses each, and mapped the proposed commands to CloudTrail events. The newsletter gives these results: 12 of 14 models opened with GetCallerIdentity; creating IAM users was the preferred persistence method (63/113 persistence attempts); models read secrets 87% of the time when the scenario said a secret existed; DeepSeek V4 proposed account modifications 72% of the time; Grok refused to help 98% of the time; only 1% of answers proposed evasion when the scenario did not mention defenses; around a third proposed tampering with CloudTrail or GuardDuty when the next action would be logged or GuardDuty had already flagged them. The newsletter says none of the tradecraft is new. It says detections that teams already run will catch LLM-driven post-compromise the same way they catch an attacker who does the same actions. The full dataset is at llms.traildiscover.cloud, with reproduction code on GitHub. Every percentage and count in this test is a single-source claim from this issue.

Hanzhi Liu and co-authors formalize malicious LLM API routers. They define two core attack classes: payload injection and secret exfiltration. Across 28 paid routers bought from Taobao, Xianyu, and Shopify-hosted storefronts, and 400 free routers from public communities, they found 1 paid router and 8 free routers that actively inject malicious code, 2 routers that deploy adaptive evasion triggers, 17 routers that touch researcher-owned AWS canary credentials, and 1 router that drains ETH from a researcher-owned private key. The newsletter quotes two further poisoning studies. A leaked OpenAI key generates 100M GPT-5.4 tokens and more than seven Codex sessions. Weakly configured decoys yield 2B billed tokens, 99 credentials across 440 Codex sessions, and 401 sessions already running in autonomous YOLO mode. The authors built Mine, a research proxy that implements all four attack classes against four public agent frameworks. They use Mine to evaluate three client-side defenses: a fail-closed policy gate, response-side anomaly screening, and append-only transparency logging. Clint states that an LLM API router has full plaintext access to everything a client sends. These router counts are single-source as summarized here.

Datadog Security Labs' Nick Frichette and Feras Al-Kassar report a counterfeit-policy attack on TypeSafe AI's Jev classifier. Adversarial instructions in untrusted content redefine attack categories and supply the desired answers, and those instructions override the model's security classifications. On four prompt-injection datasets (12,295 samples total), a prepended counterfeit policy dropped Jev's recall from 82.90% to 3.88% on the binary detection question and from 85.46% to 9.69% on the category classification question. The newsletter says traditional prompt-injection payloads had no effect. The authors placed a counterfeit policy in a user-editable profile description and used it against LangChain's tool-risk gating. The policy redefined is_risky so that a call blocked by the tool's own preconditions counted as safe. The newsletter says TypeSafe's documentation notes that injected instructions, misleading framing, and text that argues for its own classification can influence Jev's answers. A linked note says a JavaScript fingerprinting file uses descriptions of harmful acts to stop LLM analysis. A sponsor block in the same issue claims that 1.7 billion credentials were stolen in the first six months of 2026, and that 19% of the 21,667 vulnerabilities disclosed in H1 2026 shipped with ready-made, functional exploit code. The recall figures and the sponsor figures are single-source claims in this issue.

## Snippets

> "Testing across four prompt injection datasets (12,295 samples total), prepending a counterfeit policy dropped Jev's recall from 82.90% to 3.88% on its binary detection question and from 85.46% to 9.69% on its category classification question. Traditional prompt injection payloads had no effect." [Source: https://tldrsec.com/p/tldr-sec-352 (retrieved 2026-11-01)]
