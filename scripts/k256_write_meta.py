#!/usr/bin/env python3
"""Index entity rows, log prepend, ROADMAP current state."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
TODAY = "2026-09-07"

# entity index rows
idx = WIKI / "index.md"
text = idx.read_text(encoding="utf-8")
rows = [
    "| [magnitude](entities/tools/magnitude.md) | Magnitude Apache-2.0 GO REFERENCE (K256) | draft |",
    "| [refactor-platform](entities/tools/refactor-platform.md) | RefactorPlatform MIT GO REFERENCE (K256) | draft |",
    "| [trailofbits-skills](entities/tools/trailofbits-skills.md) | trailofbits/skills CC-BY-SA-4.0 EXTRACT-ONLY (K256) | draft |",
    "| [cve-mcp-server](entities/tools/cve-mcp-server.md) | cve-mcp-server Apache-2.0 GO REFERENCE (K256) | draft |",
]
if "entities/tools/magnitude.md" not in text.split("### Desk pack")[0]:
    text = text.replace(
        "| [outlier-tungsten-furnace]",
        "\n".join(rows) + "\n| [outlier-tungsten-furnace]",
        1,
    )
    idx.write_text(text, encoding="utf-8")
    print("index entities added")
else:
    print("index entities already present")

log = WIKI / "log.md"
old = log.read_text(encoding="utf-8")
entry = """## [2026-09-07] ingest | K256 wave

- **Inbox:** 24 files (13 arXiv incl. 2 skipped-cap fetched + 2 eval docx + 9 newsletters). Preingest: all NEW.
- **Sources:** AlcaTRAz; Beyond Shallow Alignment; FiMI OOD; Matched Starts; AutoLR; world-acting systems; RefactorPlatform; Gatheral; TIER; WeAgent-MMGenEdit; uncensored redistribution; BUGSTONE-E2E CVE history; Latent Space Grok Bot vs OpenClaw; Capital Flows x2; Klement organic; Wu Kalshi ban / Asia TOP10 / VC / outlook; Outlier tungsten LIVE; 2 eval docx.
- **Concepts:** 10 k256-* hubs. Bumps: k255 priors, grok-bot, grok-bot-operator-patterns, openai-codex-security, addyosmani-agent-skills, western-tungsten, ALM.
- **Phase-0:** `adopt_k256_phase0.sh` — magnitude Apache-2.0 (~55MB), refactor-platform MIT (~18MB), cve-mcp-server Apache-2.0 (~12MB), trailofbits-skills CC-BY-SA-4.0 EXTRACT-ONLY (~14MB). **0 Integrate GO.**
- **Routing:** CCC harness + Grok Bot FILE. Cyber jailbreak/refusal/uncensored/CVE. GW Capital Flows + Wu outlook alert-only. Gambling Kalshi lifetime ban **no pm scp**. Atto matched-starts method, no Barone PII. Image-gen WeAgent brief. SEO open-seo + tungsten notes. **No xsp/pm scp.**
- **Briefs:** `briefs/2026-09-07_k256-*` + sibling copies. **No LIVE Discord.**
- **Archive:** inbox → egress-fi.

## [2026-09-07] phase-0 | K256 Grok audits

- **magnitude** (`magnitudedev/magnitude`) — Apache-2.0 `[CONFIRMED]` gh api; 3934★; push 2026-09-07; ~55MB. **GO REFERENCE** FILE. Entity: `entities/tools/magnitude.md`.
- **RefactorPlatform** (`PiSchool/refactor-platform`) — MIT `[CONFIRMED]`; 2★; push 2026-09-07; ~18MB. **GO REFERENCE** FILE. Entity: `entities/tools/refactor-platform.md`.
- **cve-mcp-server** (`mukul975/cve-mcp-server`) — Apache-2.0 `[CONFIRMED]`; 1459★; ~12MB. **GO REFERENCE** FILE. Ask before MCP install. Entity: `entities/tools/cve-mcp-server.md`.
- **trailofbits/skills** — CC-BY-SA-4.0 `[CONFIRMED]`; 6998★; ~14MB. **EXTRACT-ONLY** (NO-GO Integrate). Entity: `entities/tools/trailofbits-skills.md`.
- **Skip:** Beyond-Shallow-Alignment null SPDX; awesome-mcp-servers ~215MB catalog; miles GRPO; virtual.attack no PoC; ponytail/addyosmani/codex-security already FILE.
- **Committed** with parent lint-commit-push. **0 Integrate GO.**

"""
if "## [2026-09-07] ingest | K256 wave" not in old:
    log.write_text(entry + old, encoding="utf-8")
    print("log prepended")
else:
    print("log already has K256")

rm = ROOT / "ROADMAP.md"
rt = rm.read_text(encoding="utf-8")
block = """## Current state (2026-09-07 — K256 ingest)

- **K256 ingest** — 24 inbox (13 arXiv incl. 2 skipped-cap fetched + 2 eval + 9 newsletters). 24 source pages + 10 concept hubs + 4 new entities. Raws to egress-fi. **No xsp/pm scp.**
- **Phase-0** — `adopt_k256_phase0.sh`: magnitude + RefactorPlatform + cve-mcp-server REFERENCE. trailofbits/skills EXTRACT-ONLY. **0 Integrate GO.**
- **Routing** — CCC AutoLR/RefactorPlatform/world-acting + Grok Bot FILE. Cyber AlcaTRAz/TIER/uncensored/CVE. GW CF + Wu outlook alert-only. Gambling Kalshi lifetime ban. Atto matched-starts. Outlier tungsten LIVE bump. **No LIVE Discord.**
- **Briefs** — `briefs/2026-09-07_k256-*` → CCC/cyber/GW/gambling/atto/SEO/image-gen siblings.
- **Open:** Atto P0 kit fixes; GW High-finding regressions; cursor-route 0.1.14 OR ranker; Grok Bot §9–§16 paste; HL funding / Kalshi LP / equity-signal / cross-venue backtests overdue.

"""
if "Current state (2026-09-07 — K256 ingest)" not in rt:
    # insert after Vision/Active workstreams header area — after first Current state
    needle = "## Current state (2026-09-04 — desk pack ingest)"
    if needle in rt:
        rt = rt.replace(needle, block + needle, 1)
        rm.write_text(rt, encoding="utf-8")
        print("ROADMAP updated")
    else:
        print("ROADMAP needle missing")
else:
    print("ROADMAP already has K256")

# briefs
BR = ROOT / "briefs"
BR.mkdir(exist_ok=True)
ccc = BR / "2026-09-07_k256-ccc-harness.md"
if not ccc.exists():
    ccc.write_text(
        "## Target\n\nCCC wiki + route skill backlog (claude.ai)\n\n"
        "## Summary\n\nK256 harness: AutoLR, RefactorPlatform MIT GO REFERENCE, "
        "world-acting justified-delegation. Grok Bot FILE. Do not swap /route. "
        "0 Integrate GO.\n\n"
        "## Body\n\n- AutoLR HITL. Deterministic controllers own execution.\n"
        "- RefactorPlatform FILE yardstick at .local/adopts/refactor-platform.\n"
        "- Shared Grok Bot VM is not a security boundary.\n\n"
        "## Sources\n\n- @osint-wiki/concepts/k256-harness-evolution-wave.md\n"
        "- @osint-wiki/entities/tools/refactor-platform.md\n"
        "- @osint-wiki/entities/tools/grok-bot.md\n",
        encoding="utf-8",
    )
    print("wrote ccc brief")

def write_brief(name: str, body: str, sibling: str | None) -> None:
    dest = BR / name
    dest.write_text(body, encoding="utf-8")
    print("wrote", dest)
    if sibling:
        sib = ROOT.parent / sibling / "briefs" / name
        sib.parent.mkdir(parents=True, exist_ok=True)
        sib.write_text(body, encoding="utf-8")
        print("copied", sib)

write_brief(
    "2026-09-07_k256-cyber-lab.md",
    "## Target\n\nCybersecurity wiki briefs (local abliterated lab)\n\n"
    "## Summary\n\nAlcaTRAz FILE. Beyond Shallow Alignment null SPDX no clone. "
    "TIER plus refusal-steering fetched. Uncensored redistribution: do not pull weights. "
    "cve-mcp-server Apache-2.0 GO REFERENCE. trailofbits/skills CC-BY-SA-4.0 EXTRACT-ONLY. "
    "Authorized targets only. No PoC.\n\n"
    "## Body\n\n- No uncensored-weight install.\n"
    "- No federation import of trailofbits/skills.\n"
    "- Ask before MCP install of cve-mcp-server.\n"
    "- magnitude GO REFERENCE for local GGUF.\n\n"
    "## Sources\n\n- @osint-wiki/concepts/k256-cybersec-wave.md\n"
    "- @osint-wiki/concepts/k256-abliterated-lab-wave.md\n"
    "- @osint-wiki/entities/tools/cve-mcp-server.md\n",
    "Cybersecurity wiki",
)
write_brief(
    "2026-09-07_k256-guruwatcher-macro.md",
    "## Target\n\nGuruWatcher (alert-only)\n\n"
    "## Summary\n\nCapital Flows low-vol bond complacency plus sovereign-risk 30y vs 2 percent inflation. "
    "Wu outlook: ECB 10 Sep, US Aug PPI, Oracle/Adobe, US Aug CPI 11 Sep. "
    "Alert-only. No named RSS levels so no auto-arm. Never place orders.\n\n"
    "## Body\n\n- CF strategy body is paywalled.\n"
    "- Klement organic farming is wiki-only.\n"
    "- Wu Asia TOP10 and August VC are wiki-only.\n\n"
    "## Sources\n\n- @osint-wiki/concepts/k256-newsletter-macro-wave.md\n",
    "GuruWatcher",
)
write_brief(
    "2026-09-07_k256-gambling-kalshi-ban.md",
    "## Target\n\nGambling wiki (awareness). No pm scp.\n\n"
    "## Summary\n\nKalshi first lifetime trading ban (George Santos, SOTU-attendance manipulation). "
    "Polymarket perps up to 20x. Hyperliquid xStocks RFQ. Awareness only. No LIVE Discord.\n\n"
    "## Body\n\n- Do not copy enforcement policy into Cemini bots.\n"
    "- No pm scp.\n\n"
    "## Sources\n\n- @osint-wiki/concepts/k256-gambling-pm-wave.md\n",
    "Gambling wiki",
)
write_brief(
    "2026-09-07_k256-atto-matched-starts.md",
    "## Target\n\nAtto briefs (productizable method only)\n\n"
    "## Summary\n\nMatched Starts (2609.04542): same frozen problem yields different research objects. "
    "Steal: branch-isolated FIND trajectories and HITL object lock. No Barone PII. No Atto fixtures from this paper.\n\n"
    "## Body\n\n- Lock the research object before long FIND runs.\n"
    "- Transkribus remains sole product HTR. Magnitude is lab-side only.\n\n"
    "## Sources\n\n- @osint-wiki/concepts/k256-atto-collab-wave.md\n",
    "atto",
)
write_brief(
    "2026-09-07_k256-seo-open-seo-tungsten.md",
    "## Target\n\nSEO:GEO wiki briefs\n\n"
    "## Summary\n\nevery-app/open-seo MIT FILE, no OSINT clone. Outlier Weekly 7 Sep tungsten letter LIVE: "
    "APT chemistry choke, China 79 percent mine, APT-to-Japan zero since Jan, DFARS 1 Jan 2027. "
    "Append metals-tungsten-ptpd-outlier-notes. No live prices.\n\n"
    "## Body\n\n- Four products: concentrate / APT / powder / carbide.\n"
    "- ALM/ELMT mentions, not the lead.\n\n"
    "## Sources\n\n- @osint-wiki/sources/substack-rss-outlier-weekly-2026-09-07-tungsten-furnace-2026-09-07.md\n"
    "- @osint-wiki/concepts/western-tungsten-supply-thesis.md\n",
    "SEO:GEO B&M Business",
)
write_brief(
    "2026-09-07_k256-image-gen-weagent.md",
    "## Target\n\nImage-gen wiki brief. No local image-gen wire.\n\n"
    "## Summary\n\nWeAgent-MMGenEdit (2609.05171) multimodal harness plus WeBench. OSINT OOD stub only.\n\n"
    "## Body\n\n- Do not clone the 50MB PDF runtime into Image-gen local wires.\n"
    "- FILE for recipe/benchmark awareness.\n\n"
    "## Sources\n\n- @osint-wiki/concepts/k256-ood-stub-wave.md\n",
    "Image gen",
)
# also copy CCC brief
sib = ROOT.parent / "Cemini claude code CCC" / "briefs" / "2026-09-07_k256-ccc-harness.md"
if ccc.exists() and sib.parent.is_dir():
    sib.write_text(ccc.read_text(encoding="utf-8"), encoding="utf-8")
    print("copied CCC brief")

rules = ROOT / ".cursor" / "rules" / "osint-phase1-adopt-wires.mdc"
rtxt = rules.read_text(encoding="utf-8")
if "OSINT K256" not in rtxt:
    insert = (
        "\n## OSINT K256 — 2026-09-07\n\n"
        "Dual-ID: OSINT K256 = 7 Sep 2026 inbox. FILE only. 0 Integrate GO.\n\n"
        "- Harness: AutoLR / RefactorPlatform MIT GO REFERENCE / world-acting justified-delegation. Do not swap /route. Grok Bot FILE.\n"
        "- Eval SPDX via gh api: magnitude Apache-2.0 GO REFERENCE; cve-mcp-server Apache-2.0 GO REFERENCE; trailofbits/skills CC-BY-SA-4.0 EXTRACT-ONLY.\n"
        "- Lab: no uncensored-weight pull; Beyond-Shallow-Alignment null SPDX no clone.\n"
        "- GW alert-only no auto-arm. Gambling Kalshi ban no pm scp. Atto matched-starts no Barone PII.\n"
        "- Verify: bash scripts/adopt_k256_phase1.sh. No skill auto-evolve. No LIVE Discord.\n\n"
    )
    needle = "## OSINT K246–K253 routing index"
    if needle in rtxt:
        rules.write_text(rtxt.replace(needle, insert + needle, 1), encoding="utf-8")
        print("phase1 section inserted")
    else:
        print("phase1 needle missing")
else:
    print("phase1 already has K256")
