---
title: "tl;dr sec #353 — A thousand fewer paths to root, Kubernetes security logging, post-AI security floor"
type: source
related:
  - concepts/cloud-llm-service-quarantine-coverage-gap.md
  - concepts/llm-vulnerability-discovery.md
  - concepts/siem.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [tl;dr sec] #353 - A Thousand Fewer Paths to Root, Kubernetes Security Logging, Post-AI Security Floor |
| Author | Clint Gibler (tl;dr sec) |
| Type | newsletter (RSS) |
| URL | https://tldrsec.com/p/tldr-sec-353 |
| Feed | tldrsec (https://rss.beehiiv.com/feeds/xgTKUmMmUm.xml) |
| Retrieved | 2026-11-05 |
| File | `newsletter-rss-tldrsec-2026-11-05-tldr-sec-353---a-thousand-fewer-paths-to-root-ku.md` |
| Read status | read |

## Narrative

This issue carries one headline result and five smaller items that matter to a defensive team.

### A thousand fewer paths to root

OpenAI describes an autonomous vulnerability discovery, exploitation and patching pipeline. In one run with an upcoming cyber model, it validated and generated patches for **948 local privilege escalation (LPE) vulnerabilities in Linux**. The API cost was **$1.2 million**, about **$1,279 per LPE**. The agents discovered and used at least **10 novel Linux exploitation techniques**. Kyle Zeng built the pipeline. The work is framed as critical-software defence, not product.

### Bedrock Mantle escapes quarantine

Plerion's Daniel Grzelak shows that the AWS policy `AWSCompromisedKeyQuarantineV3` fails to block LLM inference through the newer `bedrock-mantle` service. The quarantine blocks `bedrock:InvokeModel`. The new service uses `bedrock-mantle:CreateInference`. An attacker with a quarantined key can still run DeepSeek, Qwen and 36 other open-weight models through the Mantle endpoint. The calls appear only as CloudTrail **data events**, which most accounts disable by default. Recommended controls are to enable CloudTrail data events for `AWS::BedrockMantle::Project`, use a service control policy to deny the service when unused, or wait for AWS to extend the quarantine.

The general lesson is that a deny-list is reactive. A cloud provider keeps shipping new surfaces, so exposure exists until the list catches up.

### Kubernetes security logging

Marco Lancini describes a logging platform for Kubernetes clusters. Collect audit logs from `kube-apiserver`, control-plane logs, node and container logs (Fluent Bit, Vector or the OpenTelemetry Collector as DaemonSets), runtime events (Falco, Tetragon, or managed services such as GuardDuty EKS Protection and GKE Security Command Center), network flows, and Kubernetes Events. Feed everything through Kinesis or Pub/Sub into immutable S3 or GCS buckets with Object Lock, then into a SIEM. High-value detection targets are `system:anonymous` requests, `cluster-admin` bindings, `pods/exec` commands, and privileged pod creation.

### Two open-source SOC tools

`depalmar/ai-dfir-toolkit` ships 161 vendor-neutral Sigma, YARA and Suricata signatures for AI and ML attacks. The nine categories are prompt injection, MCP attacks, model supply chain, AI infrastructure, copilot abuse, RAG and vector database, runtime AI malware, agentic orchestration, and agent memory poisoning. The rules map to MITRE ATLAS and OWASP LLM/Agentic 2026. The package also carries a machine-readable artefact catalogue with KAPE, Velociraptor and osquery exports, 22 case studies, 221 indicators and 20 actor profiles.

`thomasunise/argus` is a self-hosted security operations platform with eight specialist AI agents that use read-only tools. Its autonomous response playbooks start in shadow mode with hourly caps and blast-radius limits. It ships 12 canary types, four of which target AI agents, including fake MCP servers and planted prompt injections.

### Risk-adaptive security review

Postman's Anurag Mewar describes a move from manual AppSec sign-off on every release to risk-adaptive routing. Mandatory triage questionnaires at release and pull-request level feed a VAPT ticket. Low and medium severity services with no security-sensitive change auto-close. High and critical services always get manual review. Auto-closed releases still pass SAST, SCA, secret detection and infrastructure policy. AppSec audits the automated decisions monthly. So far **25% of releases auto-unblock** and the team reclaimed three business weeks of AppSec capacity per half-year.

### AI-assisted attack tooling and the post-AI floor

The PHP2Shell coverage reports evidence of AI-assisted tooling in the attack infrastructure: Claude Code, an offensive security platform called `aiscan` configured with DeepSeek and Kimi, and API keys for the Chinese reconnaissance platform FOFA. The chained exploit reached root on 25 servers, including US government hosts, through a PAN-OS management web server in a single unauthenticated HTTP request.

Daniel Miessler's "Post-AI Security Floor" gives three priorities: build an inventory of every internet-facing asset in a simple format, remove as much public exposure as possible with tunnels, and reduce dependence on small security vendors that hold credentials.

Other items: 42 compromised GitHub repositories with malicious payloads in ~13 MB files that exceed GitHub search and indexing limits, carrying execution hooks for AI coding assistants. Chrome Enhanced Protection gains a two-tier suspicious/dangerous taxonomy, a server-side Gemini classifier, and ClickFix detection that scrubs the clipboard before analysis.

## Snippets

> "In one run with an upcoming cyber model, it validated and generated patches for 948 local privilege escalation vulnerabilities in Linux at an API cost of $1.2 million, ~$1,279 per LPE. During the run, the agents in this pipeline discovered and used at least 10 novel Linux exploitation techniques." [Source: newsletter-rss-tldrsec-2026-11-05-tldr-sec-353---a-thousand-fewer-paths-to-root-ku.md]

> "Attacks can still run DeepSeek, Qwen, and 36 other open-weight models through the Mantle endpoint even after quarantine is applied, with these calls only visible as CloudTrail data events that are disabled by default in most accounts." [Source: newsletter-rss-tldrsec-2026-11-05-tldr-sec-353---a-thousand-fewer-paths-to-root-ku.md]

> "Auto-closed releases still pass through SAST, SCA, secret detection, and infrastructure policy enforcement, with AppSec auditing them monthly to validate triage accuracy. So far 25% of releases auto-unblock and the team has reclaimed 3 full business weeks of AppSec capacity per half-year." [Source: newsletter-rss-tldrsec-2026-11-05-tldr-sec-353---a-thousand-fewer-paths-to-root-ku.md]

> "Tool that ships 161 vendor-neutral Sigma, YARA, and Suricata signatures for detecting AI/ML attacks across nine categories ... mapped to MITRE ATLAS and OWASP LLM/Agentic 2026." [Source: newsletter-rss-tldrsec-2026-11-05-tldr-sec-353---a-thousand-fewer-paths-to-root-ku.md]
