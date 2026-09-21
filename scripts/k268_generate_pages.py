#!/usr/bin/env python3
"""K268 ingest page generator — self-contained (no external JSON).

Dual-ID: OSINT K268. TODAY=2026-09-21.
0 product Integrate GO. FILE only. Transkribus sole HTR.
Skip substack-rss-secpro (K265).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "research to be indexed"
WIKI = ROOT / "wiki"
TODAY = "2026-09-21"

ARXIV_META: dict[str, dict[str, str]] = {
    "2609.21177": {
        "title": (
            "CRAFT HTR2: Polarimetry of 64 non-repeating fast radio bursts "
            "from the updated CRAFT catalogue"
        ),
        "summary": (
            "We present high-time resolution spectro-polarimetric data for 34 new "
            "fast radio bursts (FRBs) discovered by the Commensal Real-time Fast "
            "Transients (CRAFT) survey on ASKAP. This doubles the CRAFT HTR "
            "catalogue and probes a fainter FRB population. Astronomy FRB "
            "polarimetry — not handwriting recognition."
        ),
    },
    "2609.21291": {
        "title": (
            "Efficient simulation schemes for pricing options under the "
            "Ornstein--Uhlenbeck driven stochastic volatility model"
        ),
        "summary": (
            "Operator-splitting Monte Carlo for OU-driven stochastic volatility "
            "option pricing. Analytic sub-steps; avoids conditional integrated "
            "variance sampling. Competes with Hilbert / Karhunen-Loève / IG "
            "moment-matching schemes, especially path-dependent options."
        ),
    },
    "2609.21301": {
        "title": "Simulation of stochastic volatility models via operator splitting schemes",
        "summary": (
            "Strang operator-splitting framework for SV option pricing (Heston, "
            "lifted Heston, Hull-White, BNS). Circumvents conditional integrated "
            "variance evaluation. Second-order convergence proof. Wiki-only "
            "vol-quant FILE."
        ),
    },
    "2609.21554": {
        "title": (
            "MIRAGE: Multi-Perspective Creative Language Model Reasoning "
            "with Reinforcement Learning Guidance"
        ),
        "summary": (
            "MIRAGE: Selector + Reasoner multi-perspective inference-time "
            "framework. Outperforms CoT / ensembles on GSM8K, MATH500, "
            "MMLU-Pro, Game-of-24. CCC harness FILE; do not swap /route."
        ),
    },
    "2609.21684": {
        "title": "Equilibrium prices under hidden Markov fundamentals",
        "summary": (
            "Epstein-Zin economy with hidden finite-state Markov drift. "
            "Belief-Markovian prices; two-state existence/uniqueness; "
            "belief-dependent stock vol and short-maturity skewness expansion. "
            "Wiki-only vol-quant FILE."
        ),
    },
    "2609.21942": {
        "title": (
            "When Should a Failing Robot Ask? Initiating Corrective "
            "Human-Robot Dialogue from Audited Sensor Evidence"
        ),
        "summary": (
            "HITL ask gate: act on own diagnosis, consult another sensor, or "
            "interrupt a person. Audited sensor evidence; VLMs track prompt "
            "surface not evidence. Harness FILE — pairs Atto/GW HITL gates."
        ),
    },
    "2609.22000": {
        "title": (
            "RecreationWorld: Scalable and Verifiable Environments "
            "for Hybrid Computer-Use Agents"
        ),
        "summary": (
            "Five-platform hybrid CUA env: agents interleave GUI explore, "
            "code, and visual verify. RecreationWorld FILE entity; route "
            "game-dev-wiki brief; no local wire."
        ),
    },
    "2609.22068": {
        "title": "CodeMidas: Scaling Agentic Coding RL Environments from Code Itself",
        "summary": (
            "Agentic pipeline turns implemented codebase functionality into "
            "executable RL coding envs without relying only on issues/commits. "
            "CodeMidas FILE entity; paper repo unverified; 0 Integrate GO."
        ),
    },
}

FILE_MAP: list[tuple[str, str, str]] = [
    ("Jev Trading Research Paper", "jev-trading-research-paper", "k268-harness-evolution-wave"),
    ("arxiv-2609.21177", "arxiv-2609.21177-craft-frb-polarimetry", "k268-ood-stub-wave"),
    ("arxiv-2609.21291", "arxiv-2609.21291-ou-stoch-vol-options", "k268-vol-quant-wave"),
    ("arxiv-2609.21301", "arxiv-2609.21301-operator-splitting-sv", "k268-vol-quant-wave"),
    ("arxiv-2609.21554", "arxiv-2609.21554-mirage-creative-reasoning", "k268-harness-evolution-wave"),
    ("arxiv-2609.21684", "arxiv-2609.21684-hmm-equilibrium-prices", "k268-vol-quant-wave"),
    ("arxiv-2609.21942", "arxiv-2609.21942-failing-robot-ask", "k268-harness-evolution-wave"),
    ("arxiv-2609.22000", "arxiv-2609.22000-recreationworld", "k268-game-dev-wave"),
    ("arxiv-2609.22068", "arxiv-2609.22068-codemidas", "k268-harness-evolution-wave"),
    (
        "substack-rss-capital-flows-2026-09-20",
        "substack-rss-capital-flows-2026-09-20-credit-fueled-growth",
        "k268-newsletter-macro-wave",
    ),
    (
        "substack-rss-event-horizon-2026-09-21",
        "substack-rss-event-horizon-2026-09-21-ep33-prediction-markets",
        "k268-gambling-pm-wave",
    ),
    (
        "substack-rss-glitchspx-2026-09-20",
        "substack-rss-glitchspx-2026-09-20-talon-weekly-sep21",
        "k268-xsp-signal-wave",
    ),
    (
        "substack-rss-klement-2026-09-21",
        "substack-rss-klement-2026-09-21-heating-hammer",
        "k268-newsletter-macro-wave",
    ),
    (
        "substack-rss-moontower-2026-09-20-blindsided",
        "substack-rss-moontower-2026-09-20-blindsided",
        "k268-vol-quant-wave",
    ),
    (
        "substack-rss-moontower-2026-09-20-end-behavior",
        "substack-rss-moontower-2026-09-20-end-behavior",
        "k268-vol-quant-wave",
    ),
    (
        "substack-rss-moontower-2026-09-20-moontower-328",
        "substack-rss-moontower-2026-09-20-moontower-328",
        "k268-vol-quant-wave",
    ),
    (
        "substack-rss-outlier-weekly-2026-09-21",
        "substack-rss-outlier-weekly-2026-09-21-parlay-submit-screen",
        "k268-gambling-pm-wave",
    ),
    (
        "substack-rss-wublock-2026-09-21",
        "substack-rss-wublock-2026-09-21-weekly-outlook",
        "k268-newsletter-macro-wave",
    ),
]

HUBS: dict[str, dict] = {
    "k268-vol-quant-wave": {
        "title": "K268 Vol Quant Wave (Sep 2026)",
        "tags": "vol, options, quant, k268",
        "keywords": "OU-SV, operator-splitting, HMM-equilibrium, Moontower",
        "prior": "k256-vol-quant-wave",
        "narrative": (
            "K268 vol-quant cluster — OU stochastic-vol option simulation "
            "(2609.21291 / 2609.21301), HMM equilibrium prices (2609.21684), "
            "Moontower blindsided / end-behavior / #328. **Wiki-only. No xsp scp. "
            "0 product Integrate GO. FILE only.**"
        ),
    },
    "k268-harness-evolution-wave": {
        "title": "K268 Harness Evolution Wave (Sep 2026)",
        "tags": "agents, harness, k268, ccc",
        "keywords": "CodeMidas, MIRAGE, failing-robot-ask, Jev-trading-paper",
        "prior": "k267-ccc-jev-wave",
        "narrative": (
            "K268 harness cluster — **CodeMidas** agentic coding RL envs "
            "(2609.22068); **failing-robot-ask** HITL dialogue gate (2609.21942); "
            "**MIRAGE** multi-perspective reasoning (2609.21554); **Jev Trading "
            "Research Paper** image-only unread-stub. Entity `codemidas` FILE. "
            "Pairs SHE / harness-evolution canon. **0 Integrate GO. Do not swap "
            "`/route`. jev-mcp WIRE unchanged. No skill auto-evolve.**"
        ),
    },
    "k268-ood-stub-wave": {
        "title": "K268 OOD Stub Wave (Sep 2026)",
        "tags": "ood, stub, k268, astronomy",
        "keywords": "CRAFT, FRB, polarimetry, NOT-Atto-HTR",
        "prior": "k267-ood-stub-wave",
        "narrative": (
            "K268 OOD — **CRAFT HTR2** FRB polarimetry (2609.21177). Filename "
            "contains `htr` but this is **fast radio burst astronomy**, **NOT** "
            "handwriting recognition for Atto. **Transkribus remains sole product "
            "HTR.** Do not confuse with PP-OCR genealogy bait."
        ),
    },
    "k268-game-dev-wave": {
        "title": "K268 Game Dev Wave (Sep 2026)",
        "tags": "game-dev, agents, k268",
        "keywords": "RecreationWorld, hybrid-CUA, verifiable-envs",
        "prior": "k266-ccc-jev-x-wave",
        "narrative": (
            "K268 game-dev — **RecreationWorld** hybrid computer-use agent envs "
            "(2609.22000). Entity `recreationworld` FILE. Route game-dev-wiki "
            "brief; **no local wire. 0 Integrate GO.**"
        ),
    },
    "k268-newsletter-macro-wave": {
        "title": "K268 Newsletter Macro Wave (Sep 2026)",
        "tags": "macro, newsletter, k268, guruwatcher",
        "keywords": "Capital-Flows, WuBlock, Klement, heating-hammer",
        "prior": "k267-newsletter-macro-wave",
        "narrative": (
            "K268 macro newsletters — Capital Flows credit-fueled cycle; WuBlock "
            "weekly outlook (US–China); Klement heating hammer (Germany GEG). "
            "GW alert-only FILE. **Never auto-arm. Never watches.json. No LIVE "
            "Discord. No xsp/pm scp.**"
        ),
    },
    "k268-gambling-pm-wave": {
        "title": "K268 Gambling / PM Wave (Sep 2026)",
        "tags": "prediction-markets, gambling, k268",
        "keywords": "Event-Horizon, Herrisson, Outlier, parlay-submit-screen",
        "prior": "k256-gambling-pm-wave",
        "narrative": (
            "K268 PM/gambling — Event Horizon ep33 Herrisson hedging via "
            "prediction markets; Outlier Weekly parlay submit-screen pricing. "
            "Awareness only. **No pm scp. No book submit. No LIVE Discord.**"
        ),
    },
    "k268-xsp-signal-wave": {
        "title": "K268 XSP Signal Wave (Sep 2026)",
        "tags": "xsp, options, k268, glitchspx",
        "keywords": "Talon, GlitchSPX, sector-watchlist, Sep21-25",
        "prior": "k256-vol-quant-wave",
        "narrative": (
            "K268 XSP signal — GlitchSPX Talon weekly Sep 21–25 sector "
            "watchlist. Wiki FILE + xsp brief. **No xsp scp. No auto-arm. "
            "No LIVE Discord.**"
        ),
    },
    "k268-cybersec-wave": {
        "title": "K268 Cybersec Wave (Sep 2026)",
        "tags": "cybersec, k268, file",
        "keywords": "SecPro-skipped, no-PoC, thin-FILE",
        "prior": "k267-cybersec-wave",
        "narrative": (
            "K268 cyber — thin FILE hub. No inbox sources this wave. Leftover "
            "SecPro skipped (already K265). **No PoC. Authorized lab assist "
            "only.**"
        ),
    },
}

HUB_ENTITIES: dict[str, list[str]] = {
    "k268-harness-evolution-wave": ["entities/tools/codemidas.md"],
    "k268-game-dev-wave": ["entities/tools/recreationworld.md"],
}

NARRATIVES: dict[str, str] = {
    "jev-trading-research-paper": (
        "Jev Trading Research Paper PDF — **image-only** (no extractable text). "
        "`read_status: unread-stub`. Not Atto product HTR. Not a live trading "
        "path. FILE mention on harness hub. **0 Integrate GO. Never auto-arm. "
        "Transkribus remains sole product HTR.**"
    ),
    "arxiv-2609.21177-craft-frb-polarimetry": (
        "**TRAP AVOID:** CRAFT **HTR2** = high-time-resolution **fast radio "
        "burst** polarimetry (astronomy). **NOT** handwriting / OCR / Atto HTR. "
        "Filename `htr` is astronomy jargon. **Transkribus remains sole product "
        "HTR.** OOD stub only."
    ),
    "arxiv-2609.21291-ou-stoch-vol-options": (
        "OU-driven SV option pricing via operator splitting. Wiki vol-quant "
        "FILE. No xsp scp. No desk wire."
    ),
    "arxiv-2609.21301-operator-splitting-sv": (
        "Strang operator-splitting SV simulation (Heston family + BNS). Wiki "
        "vol-quant FILE. Complements 21291. No xsp scp."
    ),
    "arxiv-2609.21554-mirage-creative-reasoning": (
        "MIRAGE multi-perspective inference-time reasoning. CCC harness FILE. "
        "**Do not swap `/route`. No skill auto-evolve. 0 Integrate GO.**"
    ),
    "arxiv-2609.21684-hmm-equilibrium-prices": (
        "Hidden-Markov fundamentals → belief-Markovian equilibrium prices. "
        "Wiki vol-quant FILE. No xsp scp."
    ),
    "arxiv-2609.21942-failing-robot-ask": (
        "When should a failing agent ask a human? Audited sensor evidence + "
        "HITL interrupt gate. Pairs Atto/GW claim-ledger HITL. FILE only — "
        "do not auto-interrupt prod paths."
    ),
    "arxiv-2609.22000-recreationworld": (
        "RecreationWorld hybrid CUA benchmark. Entity stub FILE; paper repo "
        "unverified; no Phase-0 clone. Route game-dev-wiki. **0 Integrate GO.**"
    ),
    "arxiv-2609.22068-codemidas": (
        "CodeMidas scales agentic coding RL envs from code itself. Entity stub "
        "FILE; paper repo unverified; no Phase-0 clone. CCC harness FILE. "
        "**Do not swap `/route`.**"
    ),
    "substack-rss-capital-flows-2026-09-20-credit-fueled-growth": (
        "Capital Flows — credit-fueled growth / yield-curve bear flattening. "
        "GW macro FILE. **Never auto-arm.**"
    ),
    "substack-rss-event-horizon-2026-09-21-ep33-prediction-markets": (
        "Event Horizon ep33 — Herrisson hedging / insurance via prediction "
        "markets (Will Brooke). Awareness FILE. **No pm scp.**"
    ),
    "substack-rss-glitchspx-2026-09-20-talon-weekly-sep21": (
        "GlitchSPX Talon weekly Sep 21–25 sector watchlist. XSP brief FILE. "
        "**No xsp scp. No auto-arm.**"
    ),
    "substack-rss-klement-2026-09-21-heating-hammer": (
        "Klement — Germany 'heating hammer' media campaign vs GEG reform. "
        "Macro / narrative FILE. GW alert-only. **Never auto-arm.**"
    ),
    "substack-rss-moontower-2026-09-20-blindsided": (
        "Moontower Meta — blindsided. Vol/trading newsletter FILE. No xsp scp."
    ),
    "substack-rss-moontower-2026-09-20-end-behavior": (
        "Moontower Meta — end behavior. Options-trader prompt FILE. No xsp scp."
    ),
    "substack-rss-moontower-2026-09-20-moontower-328": (
        "Moontower #328 index (blindsided + end behavior). Vol-quant FILE."
    ),
    "substack-rss-outlier-weekly-2026-09-21-parlay-submit-screen": (
        "Outlier Weekly — parlay price is the submit-screen American (already "
        "correlation-adjusted). CeminiParlays / gambling awareness. **No pm "
        "scp. No book submit.**"
    ),
    "substack-rss-wublock-2026-09-21-weekly-outlook": (
        "WuBlock weekly outlook — US–China meeting / tech restrictions. Macro "
        "FILE. **No xsp/pm scp. Never auto-arm.**"
    ),
}


def yaml_title(s: str) -> str:
    return s.replace('"', "'")


def snippet(text: str, n: int = 280) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > n:
        return text[:n].rsplit(" ", 1)[0] + "…"
    return text


def parse_md_title(text: str) -> str:
    m = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", text, re.M)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else "Untitled"


def match_inbox(name: str) -> tuple[str, str] | None:
    if "secpro" in name.lower():
        return None
    stem = Path(name).stem
    for prefix, slug, hub in FILE_MAP:
        if stem.startswith(prefix) or name.startswith(prefix):
            return slug, hub
    return None


def write_source(
    slug: str,
    hub: str,
    inbox_name: str,
    title: str,
    body: str,
    is_pdf: bool,
    *,
    unread_stub: bool = False,
) -> None:
    path = WIKI / "sources" / f"{slug}-{TODAY}.md"
    arxiv = None
    m = re.search(r"arxiv-(\d+\.\d+)", inbox_name)
    if m:
        arxiv = m.group(1)
    related = [f"  - concepts/{hub}.md"]
    relations = [f"- @concepts/{hub}.md"]
    if slug == "arxiv-2609.22068-codemidas":
        related.append("  - entities/tools/codemidas.md")
        relations.append("- @entities/tools/codemidas.md")
    if slug == "arxiv-2609.22000-recreationworld":
        related.append("  - entities/tools/recreationworld.md")
        relations.append("- @entities/tools/recreationworld.md")
    loc = f"cemini-egress-fi:/opt/cemini-bulk/research/osint/{inbox_name}"
    raw = []
    if arxiv:
        raw.append(f"| Paper | arXiv:{arxiv} |")
    raw += [
        f"| File | `{inbox_name}` |",
        f"| Location | `{loc}` |",
        f"| Retrieved | {TODAY} |",
        "| Dual-ID | **OSINT K268** |",
    ]
    snip_src = body
    if arxiv and arxiv in ARXIV_META:
        snip_src = ARXIV_META[arxiv]["summary"]
    if unread_stub:
        read_status = "unread-stub"
        tags = "arxiv, source, k268, unread-stub, image-only"
    elif is_pdf:
        read_status = "skimmed"
        tags = "arxiv, source, k268"
    else:
        read_status = "read"
        tags = "source, k268"
    path.write_text(
        "\n".join(
            [
                "---",
                f'title: "{yaml_title(title)}"',
                "type: source",
                f"tags: [{tags}]",
                "keywords: [k268]",
                "related:",
                *related,
                "maturity: draft",
                f"created: {TODAY}",
                f"updated: {TODAY}",
                f"read_status: {read_status}",
                "---",
                "",
                "## Relations",
                "",
                *relations,
                "",
                "## Raw Concept",
                "",
                *raw,
                "",
                "## Narrative",
                "",
                body,
                "",
                "## Snippets",
                "",
                f'> "{snippet(snip_src)}" [Source: {inbox_name}]',
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_hub(slug: str, meta: dict, sources: list[str], extra_entities: list[str]) -> None:
    path = WIKI / "concepts" / f"{slug}.md"
    prior = meta["prior"]
    related = [f"  - concepts/{prior}.md"]
    relations = [f"- @concepts/{prior}.md"]
    for s in sources:
        related.append(f"  - sources/{s}-{TODAY}.md")
        relations.append(f"- @sources/{s}-{TODAY}.md")
    for e in extra_entities:
        related.append(f"  - {e}")
        relations.append(f"- @{e}")
    path.write_text(
        "\n".join(
            [
                "---",
                f"title: {meta['title']}",
                "type: concept",
                f"tags: [{meta['tags']}]",
                f"keywords: [{meta['keywords']}]",
                "related:",
                *related,
                "maturity: draft",
                f"created: {TODAY}",
                f"updated: {TODAY}",
                "harness_verb: FILE",
                "---",
                "",
                "## Relations",
                "",
                *relations,
                "",
                "## Raw Concept",
                "",
                "K268 cluster hub. Dual-ID **OSINT K268**.",
                "",
                "## Narrative",
                "",
                meta["narrative"],
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_entity_stub(
    slug: str,
    title: str,
    hub: str,
    source_slug: str,
    narrative: str,
) -> None:
    path = WIKI / "entities" / "tools" / f"{slug}.md"
    src = f"sources/{source_slug}-{TODAY}.md"
    path.write_text(
        "\n".join(
            [
                "---",
                f"title: {title}",
                "type: entity",
                f"tags: [tool, k268, file]",
                f"keywords: [{slug}, paper, unverified-repo]",
                "related:",
                f"  - concepts/{hub}.md",
                f"  - {src}",
                "maturity: draft",
                f"created: {TODAY}",
                f"updated: {TODAY}",
                "phase_0_verdict: FILE NO-CLONE",
                "harness_verb: FILE",
                "wire_status: wont_wire",
                "wire_note: Paper repo unverified. FILE stub only. 0 product Integrate GO.",
                "---",
                "",
                "## Relations",
                "",
                f"- @concepts/{hub}.md",
                f"- @{src}",
                "",
                "## Raw Concept",
                "",
                f"K268 Phase-0 — no clone. Paper-linked tool `{slug}`.",
                "",
                "## Narrative",
                "",
                narrative,
                "",
            ]
        ),
        encoding="utf-8",
    )


def add_related(path: Path, entries: list[str]) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    for entry in entries:
        rel_line = f"  - {entry}"
        at_line = f"- @{entry}"
        if rel_line not in text:
            text = re.sub(
                r"(related:\n(?:  - .+\n)*)",
                lambda m, line=rel_line: m.group(1) + line + "\n",
                text,
                count=1,
            )
        if at_line not in text:
            text = re.sub(
                r"(## Relations\n\n(?:- .+\n)*)",
                lambda m, line=at_line: m.group(1) + line + "\n",
                text,
                count=1,
            )
    text = re.sub(r"^updated: \d{4}-\d{2}-\d{2}$", f"updated: {TODAY}", text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8")


def insert_index(rows: list[str], blurb: str) -> None:
    index = WIKI / "index.md"
    text = index.read_text(encoding="utf-8")
    if "### K268 ingest" in text:
        return
    block = (
        f"### K268 ingest ({TODAY})\n"
        f"{blurb}\n\n"
        "| Page | Summary | Maturity |\n"
        "|------|---------|----------|\n"
        + "\n".join(rows)
        + "\n\n"
    )
    marker = "### K267 ingest (2026-09-20)"
    if marker not in text:
        raise SystemExit("index.md marker missing: ### K267 ingest (2026-09-20)")
    index.write_text(text.replace(marker, block + marker, 1), encoding="utf-8")


def main() -> None:
    hub_sources: dict[str, list[str]] = {k: [] for k in HUBS}
    index_rows: list[str] = []
    for inbox_path in sorted(INBOX.iterdir()):
        if inbox_path.name.startswith("."):
            continue
        matched = match_inbox(inbox_path.name)
        if not matched:
            print(f"SKIP unmapped: {inbox_path.name}")
            continue
        slug, hub = matched
        is_pdf = inbox_path.suffix.lower() == ".pdf"
        arxiv = None
        m = re.search(r"arxiv-(\d+\.\d+)", inbox_path.name)
        if m:
            arxiv = m.group(1)
        unread_stub = slug == "jev-trading-research-paper"
        if is_pdf and arxiv and arxiv in ARXIV_META:
            title = ARXIV_META[arxiv]["title"]
        elif unread_stub:
            title = "Jev Trading Research Paper (image-only unread-stub)"
        elif inbox_path.suffix.lower() == ".md":
            title = parse_md_title(inbox_path.read_text(encoding="utf-8", errors="replace"))
        else:
            title = inbox_path.stem.replace("-", " ")
        body = NARRATIVES.get(slug, "K268 wiki ingest. FILE only. 0 Integrate GO.")
        write_source(slug, hub, inbox_path.name, title, body, is_pdf, unread_stub=unread_stub)
        hub_sources[hub].append(slug)
        index_rows.append(
            f"| [{slug}](sources/{slug}-{TODAY}.md) | {yaml_title(title)[:70]} | draft |"
        )
        print(f"OK source: {slug}")

    write_entity_stub(
        "codemidas",
        "CodeMidas — agentic coding RL envs (FILE)",
        "k268-harness-evolution-wave",
        "arxiv-2609.22068-codemidas",
        (
            "| Field | Value |\n"
            "|-------|-------|\n"
            "| **Paper** | arXiv:2609.22068 |\n"
            "| **License / repo** | unverified at Phase-0 |\n"
            "| **Local** | none — no clone |\n"
            "| **Verdict** | **FILE NO-CLONE**. CCC harness awareness. "
            "**0 product Integrate GO. Do not swap `/route`.** |"
        ),
    )
    print("OK entity: codemidas")
    write_entity_stub(
        "recreationworld",
        "RecreationWorld — hybrid CUA envs (FILE)",
        "k268-game-dev-wave",
        "arxiv-2609.22000-recreationworld",
        (
            "| Field | Value |\n"
            "|-------|-------|\n"
            "| **Paper** | arXiv:2609.22000 |\n"
            "| **License / repo** | unverified at Phase-0 |\n"
            "| **Local** | none — no clone |\n"
            "| **Verdict** | **FILE NO-CLONE**. Route game-dev-wiki. "
            "**0 product Integrate GO. No local wire.** |"
        ),
    )
    print("OK entity: recreationworld")

    hub_index: list[str] = []
    for hub_slug, meta in HUBS.items():
        srcs = hub_sources.get(hub_slug, [])
        write_hub(hub_slug, meta, srcs, HUB_ENTITIES.get(hub_slug, []))
        hub_index.append(f"| [{hub_slug}](concepts/{hub_slug}.md) | {meta['title']} | draft |")
        print(f"OK hub: {hub_slug} ({len(srcs)} sources)")

    hub_index.append(
        "| [codemidas](entities/tools/codemidas.md) | CodeMidas FILE NO-CLONE | draft |"
    )
    hub_index.append(
        "| [recreationworld](entities/tools/recreationworld.md) | "
        "RecreationWorld FILE NO-CLONE | draft |"
    )

    add_related(
        WIKI / "concepts" / "k267-ccc-jev-wave.md",
        ["concepts/k268-harness-evolution-wave.md"],
    )
    add_related(
        WIKI / "concepts" / "k267-ood-stub-wave.md",
        ["concepts/k268-ood-stub-wave.md"],
    )
    add_related(
        WIKI / "concepts" / "k267-newsletter-macro-wave.md",
        ["concepts/k268-newsletter-macro-wave.md"],
    )
    add_related(
        WIKI / "concepts" / "k267-cybersec-wave.md",
        ["concepts/k268-cybersec-wave.md"],
    )
    add_related(
        WIKI / "concepts" / "k256-vol-quant-wave.md",
        ["concepts/k268-vol-quant-wave.md", "concepts/k268-xsp-signal-wave.md"],
    )
    add_related(
        WIKI / "concepts" / "k256-gambling-pm-wave.md",
        ["concepts/k268-gambling-pm-wave.md"],
    )
    add_related(
        WIKI / "concepts" / "k266-ccc-jev-x-wave.md",
        ["concepts/k268-game-dev-wave.md"],
    )

    blurb = (
        "OSINT K268: 18 inbox (9 PDF + 9 newsletters; leftover SecPro skipped = K265). "
        "Phase-0 **no clones** (paper repos unverified). Entities: codemidas + "
        "recreationworld FILE. **0 product Integrate GO. FILE only. Transkribus "
        "sole HTR. Do not swap `/route`. No xsp/pm scp. No skill auto-evolve. "
        "No LIVE Discord. Never `npx github:`. Never auto-arm. 21177 = FRB "
        "astronomy NOT Atto HTR.**"
    )
    insert_index(hub_index + index_rows, blurb)
    print(
        f"Done — {sum(len(v) for v in hub_sources.values())} sources, "
        f"{len(HUBS)} hubs, 2 entities"
    )


if __name__ == "__main__":
    main()
