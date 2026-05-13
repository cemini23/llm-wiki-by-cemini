---
title: "NVIDIA OpenShell — Containerized Agent Sandbox Runtime (GO 2026-05-12: policy-schema extraction approved)"
type: entity
tags: [tool, agent-sandbox, container, security, nvidia, steal-from, k39, phase-0-go]
keywords: [nvidia openshell, agent sandbox, docker policy, network isolation, declarative policy, apache-2.0, landlock, regorus]
related:
  - sources/evaluating-project-links-stacks.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-12
phase_0_audit: GO 2026-05-12 — Apache-2.0 verified (NVIDIA org owner, LICENSE file confirmed); policy schemas standalone-portable to FastMCP Python hardening
license_verified: Apache-2.0 (gh api confirmed)
---

## Relations
- `@sources/evaluating-project-links-stacks.md` — source evaluation brief (URL 4)
- `@concepts/tool-evaluation-framework.md` — three-surface methodology applied
- `@concepts/cemini-license-posture.md` — license posture context

## Raw Concept

- **Repo / URL** (per source brief): `github.com/NVIDIA/OpenShell` (release v0.0.37)
- **Tier (per source brief)**: **Steal-from**
- **License** (per source brief): Apache-2.0
- **Stack**: Python CLI (`uv tool install openshell`), Docker container runtime, declarative YAML policies, optional NVIDIA GPU acceleration
- **Maturity** (per source brief): v0.0.37; Copyright 2025-2026 NVIDIA Corporation

## Narrative

Containerized runtime for safely executing autonomous AI agents in restricted, transient sandboxes. Declarative YAML policies restrict file access, network egress, and outbound API activity. Predefined sandboxes (Ollama, OpenClaw, base). Apache-2.0 with explicit patent retaliation clauses (favorable for enterprise acquirers).

### Integration vector

**Steal-from**: extract the declarative-policy schemas (file-access + network-egress rules) and manually port to harden existing FastMCP Python Docker containers. **Do not deploy** OpenShell wholesale — Docker-in-Docker abstraction is too fragile for 24/7 trading; 40-container Hetzner host already at file-descriptor / inode pressure.

### NEEDS VERIFICATION

- Confirm this is the real NVIDIA-published repo (v0.0.37 only — verify on `github.com/NVIDIA/OpenShell` directly)
- Execution-latency overhead per FastMCP tool call when wrapped in a transient OpenShell sandbox
- Whether declarative-policy schemas can be lifted standalone without the runtime

### Phase-0 audit status

**GO 2026-05-12** — Apache-2.0 + NVIDIA-owned + policy schemas standalone-portable.

## Phase-0 audit findings (2026-05-12)

**Repo verified**: `github.com/NVIDIA/OpenShell` — owner=`NVIDIA` (real org, not typosquat) / 5,852★ / Apache-2.0 confirmed via `gh api license.spdx_id` / default branch `main` / last push 2026-05-13 (active daily). No patent retaliation clauses beyond standard Apache-2.0 §3.

**Policy schema files (standalone-portable)**:

1. **`crates/openshell-policy/src/lib.rs`** (380 lines) — Serde types for YAML parsing: `PolicyFile`, `FilesystemDef`, `NetworkPolicyRuleDef`. Bidirectional YAML ↔ protobuf conversion. Pure parsing library — no gRPC, no OPA engine dependency. Translatable to Python Pydantic models or dataclasses.
2. **`proto/sandbox.proto`** — protobuf schema definitions for `SandboxPolicy`, `FilesystemPolicy`, `NetworkPolicyRule`. Cemini can implement a Python reader that consumes the same protobuf OR YAML directly (no proto needed if Pydantic models suffice).
3. **Example policies (test fixtures)**:
   - `crates/openshell-sandbox/testdata/sandbox-policy.yaml` — comprehensive fixture
   - `examples/sandbox-policy-quickstart/policy.yaml` — minimal REST-only (curl → api.github.com)
   - `examples/local-inference/sandbox-policy.yaml` — PyPI + NVIDIA API access (strip NVIDIA endpoints)
   - `examples/policy-advisor/sandbox-policy.yaml` — restrictive (Anthropic API only; closest template for hardening a FastMCP Claude container)

**Schema dimensions constrained**:
- **Filesystem**: `read_only` paths (glob), `read_write` paths, `include_workdir` (bool)
- **Process**: `run_as_user`, `run_as_group` (strings)
- **Landlock** (Linux LSM): `compatibility` mode (`best_effort` | `hard_requirement`)
- **Network** (L4 + L7): per-policy rules with `endpoints` (host:port), `binaries` (path globs), L7 enforcement (`rest`/`websocket`/`graphql`/`sql`), HTTP method/path allow-lists, credential rewriting, deny rules

**Steal-readiness**: schemas decoupled from OpenShell runtime evaluator. OPA evaluation (`regorus` Rust interpreter) is a runtime detail; the YAML → proto translation is schema-only. No Docker-in-Docker lock-in (policies don't reference container images, Docker sockets, kernel versions). The `policy-advisor` example is the closest match for FastMCP Python container hardening.

**Red flags (none critical)**:
- GPU/CUDA dependencies — none. Works on Linux + macOS + Windows-WSL.
- NVIDIA inference API endpoints in `examples/local-inference/sandbox-policy.yaml` — strip when porting; policies themselves are agnostic.
- `examples/openclaw.md` references NVIDIA's proprietary OpenClaw framework. **Do not extract OpenClaw image**; policy syntax is universal.
- Patent retaliation: standard Apache-2.0 §3 (sue for infringement → license terminates). Applies to all licensees; does not single-out IP-sale risk for Cemini.

### Extraction plan (Cemini-side, queued for separate FastMCP-hardening brief)

1. Port `openshell-policy/src/lib.rs` Serde types → Python Pydantic models. Keep YAML as the configuration surface.
2. Use the `policy-advisor` example as the FastMCP Claude container template (restrictive, Anthropic-only network egress).
3. Implement enforcement: Linux seccomp/landlock for filesystem rules; proxy-based interception (LD_PRELOAD or unshare network namespace + iptables) for network egress.
4. Test fixtures: lift the 4 example YAML files verbatim as the Python module's test corpus.

Out of scope for this audit: the actual port. Brief to be staged under `briefs/2026-MM-DD_fastmcp-policy-hardening.md` once Cemini-prod is ready (currently EMS/Redis-blocked on Step 82).

### Verdict

**GO — extract policy schemas**. Apache-2.0 + NVIDIA-owned + standalone YAML/protobuf with no runtime coupling. License clean for IP-sale posture. First **non-mischaracterized, non-rejected** Steal-from in the K39 batch (deepseek-tui + obscura + mac-code + meridian + gabagool all NO-GO).

[Source: Evaluating Project Links for Stacks.docx URL 4; retrieved 2026-05-11; Phase-0 audit 2026-05-12]
