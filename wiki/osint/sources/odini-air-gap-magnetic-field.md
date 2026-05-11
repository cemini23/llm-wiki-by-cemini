---
title: "ODINI — Escaping Sensitive Data from Faraday-Caged, Air-Gapped Computers via Magnetic Fields"
type: source
tags: [source, air-gap, covert-channel, apt, electromagnetic-emanation, defensive-security, ben-gurion]
keywords: [air-gap, Faraday cage, CPU magnetic field, covert channel, ODINI, APT, magnetic exfiltration, signal jamming, Mordechai Guri]
related:
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@concepts/cemini-license-posture.md` — IP-sale-ready stack threat model includes covert-exfiltration vectors

## Raw Concept

- **Title**: ODINI: Escaping Sensitive Data from Faraday-Caged, Air-Gapped Computers via Magnetic Fields
- **Authors**: Mordechai Guri, Boris Zadov, Andrey Daidakulov, Yuval Elovici (Ben-Gurion University of the Negev, Cyber Security Research Center)
- **Type**: Academic paper, defensive cybersecurity / red-team research
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/ODINI - Escaping Sensitive Data from Faraday-Caged, Air-Gapped Computers via Magnetic Fields.pdf`
- **arXiv**: [1802.02700v1](https://arxiv.org/abs/1802.02700) (cs.CR, 8 Feb 2018)
- **sha256**: `c75703a763546140…` (preingest verdict: NEW)
- **Pages**: 18
- **Read-status**: deep-read

## Narrative

Demonstrates a covert channel that defeats Faraday-cage isolation by modulating low-frequency magnetic fields from CPU core load. Unlike electromagnetic radiation (EMR), low-frequency magnetic emanation propagates through metal shielding — the authors note compasses still function inside Faraday cages, exploiting the same physics.

**Mechanism (`ODINI` malware prototype)**:
- Modulates CPU core load (multi-thread workload regulation) to control magnetic emission amplitude
- Receiver is a magnetic field "bug" placed in physical proximity (the paper evaluates ranges up to ~100 cm through 1mm steel + air-gap)
- Works from user-space; no root required; survives inside a VM
- Encoding/modulation schemes evaluated (OOK / B-FSK / B-PSK); achieves transmission rates of single bits/sec at relevant ranges

**Threats covered**:
- Insider physically plants a magnetic-bug receiver near the air-gapped machine
- Once an APT compromises the air-gapped network (e.g., via supply chain or sneakernet), this covert channel becomes the egress path

**Defensive countermeasures discussed**:
- Signal detection (anomalous magnetic-field telemetry monitors near sensitive equipment)
- Signal jamming (active magnetic-field generators to drown the covert signal)
- Mu-metal shielding active compensation (cost-prohibitive for routine deployments)
- Physical zoning (minimum standoff distance between sensitive machines and any unauthorized object)

### Cemini significance

**Reference-only** — not a tool to adopt. Cemini's prod stack is connected (Hetzner internet-facing), so air-gap covert channels are not in the active threat model today. The paper matters for:

1. **IP-sale-readiness posture**: If Cemini's proprietary algorithms ever require air-gap isolation for institutional buyer due-diligence, the threat surface includes more than just network and EMR — magnetic covert channels are real and unmitigated by standard Faraday cages.
2. **Threat-modeling discipline**: Reinforces "trust the physics, not the cage" — defensive posture must include every emanation channel, not just the ones built into the threat model.
3. **Companion paper** to Guri's broader BGU air-gap research corpus (other covert channels: thermal, acoustic, optical, electromagnetic, power-line). Worth bookmarking the [BGU air-gap research index](https://cyber.bgu.ac.il/advanced-cyber/airgap) for future threat-modeling sessions.

### Snippets

> "Unlike electromagnetic radiation (EMR), low frequency magnetic radiation propagates though the air, penetrating metal shielding such as Faraday cages (e.g., compass still works inside Faraday cages). Since the CPU is an essential part of any computer, our covert channel is relevant to virtually any device with a CPU: desktop PCs, servers, laptops, embedded systems and Internet of Things (IoT) devices." [Source: ODINI.pdf p.1 (Abstract)]

> "We also show that the malicious code does not require special privileges (e.g., root) and can successfully operate from within isolated virtual machines (VMs) as well." [Source: ODINI.pdf p.1 (Abstract)]

[Source: ODINI - Escaping Sensitive Data from Faraday-Caged, Air-Gapped Computers via Magnetic Fields.pdf, arXiv:1802.02700]
