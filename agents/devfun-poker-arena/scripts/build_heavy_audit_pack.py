#!/usr/bin/env python3
"""Build heavy gap-audit pack: full-export aggregates + top-rival samples (no 287k row dump).

Usage:
  uv run python scripts/build_heavy_audit_pack.py reports/exports/s2-audit-pack \\
      --hero cemini_wiki_poker --out reports/gap-audit/pack-s2-heavy
"""
from __future__ import annotations

import argparse
import json
import random
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
if str(EXAMPLES) not in sys.path:
    sys.path.insert(0, str(EXAMPLES))

from export_bundle import (  # noqa: E402
    crawl_progress,
    load_bb100_snapshot,
    load_export_agents_with_bb100,
    load_export_submissions,
)

PROMPT_TEMPLATE = ROOT / "prompts" / "s2_gap_retrospective_audit.md"
HERO_DEFAULT = "cemini_wiki_poker"
# Fallback if export has no 200h rivals yet
TOP_RIVALS_FALLBACK = (
    "0xJeff_ai",
    "fefou_v2",
    "phoenix-rises-nrkdhd-v10",
    "float_engine",
    "crypto-bro-agent",
    "alnitak",
    "einstein",
    "poker_brat_n9dl",
    "wemby_guy_v2",
    "long_tu",
)


def _select_rivals(
    agents: list[dict],
    hero: str,
    *,
    min_hands: int,
    max_rivals: int,
) -> list[str]:
    """Top rivals by chip rank with at least min_hands (exclude hero)."""
    pool = [
        a for a in agents
        if (a.get("handle") or "") != hero and int(a.get("hands") or 0) >= min_hands
    ]
    pool.sort(key=lambda a: (a.get("rank") or 9999, -(a.get("chips") or 0)))
    handles = [str(a["handle"]) for a in pool[:max_rivals] if a.get("handle")]
    return handles or list(TOP_RIVALS_FALLBACK)


def _rivals_200plus_table(agents: list[dict], hero: str, *, min_hands: int = 200) -> str:
    pool = [
        a for a in agents
        if (a.get("handle") or "") != hero and int(a.get("hands") or 0) >= min_hands
    ]
    pool.sort(key=lambda a: (a.get("rank") or 9999))
    lines = [
        f"Agents with ≥{min_hands} hands (excl hero): **{len(pool)}**",
        "",
        "| Rank | Handle | Hands | Chips | Style | VPIP | PFR | Sub rows |",
        "|------|--------|-------|-------|-------|------|-----|----------|",
    ]
    for a in pool[:60]:
        st = a.get("stats") or {}
        vpip = st.get("vpip")
        pfr = st.get("pfr")
        vp = f"{vpip:.1%}" if isinstance(vpip, (int, float)) else "?"
        pf = f"{pfr:.1%}" if isinstance(pfr, (int, float)) else "?"
        lines.append(
            f"| {a.get('rank', '?')} | {a.get('handle', '?')} | {a.get('hands', '?')} "
            f"| {a.get('chips', '?')} | {st.get('playing_style', '?')} | {vp} | {pf} "
            f"| {a.get('submission_rows', '?')} |"
        )
    if len(pool) > 60:
        lines.append(f"\n(... {len(pool) - 60} more in export — see rival_samples/)")
    return "\n".join(lines)


def _hero_variance_bootstrap(submissions: list[dict], hero: str, *, n_boot: int = 500) -> dict:
    rows = [r for r in submissions if r.get("agent_handle") == hero]
    if len(rows) < 50:
        return {"note": "insufficient hero rows", "n": len(rows)}
    big_blind = 20
    payouts = [int(r.get("payout_chips") or 0) for r in rows]
    pot_win_rate = sum(1 for p in payouts if p > 0) / len(rows)
    deltas = [(p * 0.35 if p > 0 else -big_blind * 0.5) for p in payouts]
    mean_bb100 = (sum(deltas) / big_blind) / len(deltas) * 100
    rng = random.Random(42)
    samples = sorted(
        (sum(deltas[rng.randrange(len(deltas))] for _ in range(len(deltas))) / big_blind)
        / len(deltas)
        * 100
        for _ in range(n_boot)
    )
    lo, hi = samples[int(n_boot * 0.025)], samples[int(n_boot * 0.975)]
    return {
        "hero_submission_rows": len(rows),
        "pot_win_rate": round(pot_win_rate, 4),
        "bb100_chip_proxy_point": round(mean_bb100, 2),
        "bb100_bootstrap_95ci": [round(lo, 2), round(hi, 2)],
        "note": "NOT all-in EV — payout_chips ≥ 0 only",
    }


def _position_stats(submissions: list[dict], hero: str) -> str:
    rows = [r for r in submissions if r.get("agent_handle") == hero]
    by_pos: dict[str, list[int]] = defaultdict(list)
    for r in rows:
        pos = str(r.get("position") or r.get("seat") or "?")
        by_pos[pos].append(int(r.get("payout_chips") or 0))
    lines = [
        "| Position | Hands | Pot wins | Win rate | Avg payout |",
        "|----------|-------|----------|----------|------------|",
    ]
    for pos in sorted(by_pos.keys(), key=lambda p: (p.isdigit(), p)):
        vals = by_pos[pos]
        wins = sum(1 for v in vals if v > 0)
        lines.append(
            f"| {pos} | {len(vals)} | {wins} | {wins / max(len(vals), 1):.1%} "
            f"| {mean(vals):.1f} |"
        )
    return "\n".join(lines)


def _payout_histogram(submissions: list[dict], hero: str) -> dict:
    rows = [int(r.get("payout_chips") or 0) for r in submissions if r.get("agent_handle") == hero]
    if not rows:
        return {}
    buckets = Counter()
    for p in rows:
        if p <= 0:
            buckets["0"] += 1
        elif p < 50:
            buckets["1-49"] += 1
        elif p < 200:
            buckets["50-199"] += 1
        elif p < 500:
            buckets["200-499"] += 1
        else:
            buckets["500+"] += 1
    return dict(buckets)


def _rival_samples(
    submissions: list[dict],
    handle: str,
    *,
    limit: int = 25,
    agent_row: dict | None = None,
) -> str:
    rows = [r for r in submissions if (r.get("agent_handle") or "").lower() == handle.lower()]
    if not rows:
        return f"(no rows for {handle})"
    win_n, loss_n = (15, 15) if len(rows) >= 200 else (10, 10)
    wins = sorted(rows, key=lambda r: int(r.get("payout_chips") or 0), reverse=True)[:win_n]
    losses = sorted(rows, key=lambda r: int(r.get("payout_chips") or 0))[:loss_n]
    lines = [f"## {handle} — {len(rows)} submission rows"]
    if agent_row:
        st = agent_row.get("stats") or {}
        lines.append(
            f"rank={agent_row.get('rank')} chips={agent_row.get('chips')} hands={agent_row.get('hands')} "
            f"style={st.get('playing_style')} vpip={st.get('vpip')} pfr={st.get('pfr')}"
        )
        pot_wins = sum(1 for r in rows if int(r.get("payout_chips") or 0) > 0)
        lines.append(f"pot_win_rate={pot_wins / len(rows):.1%} avg_payout={mean(int(r.get('payout_chips') or 0) for r in rows):.1f}")
    lines.append("### Top pot wins")
    for r in wins:
        lines.append(
            f"payout={r.get('payout_chips')} pos={r.get('position')} "
            f"hole={r.get('hole_cards')} board={r.get('board_cards')}"
        )
    lines.append("### Lowest payouts")
    for r in losses:
        lines.append(
            f"payout={r.get('payout_chips')} pos={r.get('position')} "
            f"hole={r.get('hole_cards')} board={r.get('board_cards')}"
        )
    return "\n".join(lines)


def _hero_vs_rival_tables(submissions: list[dict], hero: str, rivals: list[str]) -> str:
    """Table co-occurrence proxy via shared table_id in submission rows."""
    hero_tables: dict[str, int] = Counter()
    rival_tables: dict[str, dict[str, int]] = {h: Counter() for h in rivals}
    for r in submissions:
        tid = r.get("table_id")
        if not tid:
            continue
        h = r.get("agent_handle") or ""
        if h == hero:
            hero_tables[tid] += 1
        for rival in rivals:
            if h.lower() == rival.lower():
                rival_tables[rival][tid] += 1
    lines = ["| Rival | Shared tables (proxy) | Rival rows |", "|-------|----------------------|------------|"]
    for rival in rivals:
        shared = len(set(hero_tables) & set(rival_tables[rival]))
        lines.append(f"| {rival} | {shared} | {sum(rival_tables[rival].values())} |")
    return "\n".join(lines)


def _field_style_summary(agents: list[dict], top_n: int = 50) -> str:
    styles = Counter((a.get("stats") or {}).get("playing_style") or "?" for a in agents[:top_n])
    lines = ["| Style (top agents) | Count |", "|--------------------|-------|"]
    for style, n in styles.most_common(15):
        lines.append(f"| {style} | {n} |")
    vpip_vals = [(a.get("stats") or {}).get("vpip") for a in agents[:top_n]]
    pfr_vals = [(a.get("stats") or {}).get("pfr") for a in agents[:top_n]]
    vpip_nums = [v for v in vpip_vals if isinstance(v, (int, float))]
    pfr_nums = [v for v in pfr_vals if isinstance(v, (int, float))]
    if vpip_nums:
        lines.append(f"\nTop-{top_n} avg VPIP {mean(vpip_nums):.1%}, PFR {mean(pfr_nums):.1%}")
    return "\n".join(lines)


def _worst_hero_hands(submissions: list[dict], hero: str, limit: int = 80) -> str:
    rows = [r for r in submissions if r.get("agent_handle") == hero]
    rows.sort(key=lambda r: int(r.get("payout_chips") or 0))
    lines = []
    for r in rows[:limit]:
        lines.append(
            f"payout={r.get('payout_chips')} pos={r.get('position')} "
            f"hole={r.get('hole_cards')} board={r.get('board_cards')} "
            f"table={str(r.get('table_id', ''))[:16]}"
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build heavy S1/S2 gap audit pack")
    p.add_argument("export_dir", type=Path)
    p.add_argument("--hero", default=HERO_DEFAULT)
    p.add_argument("--out", type=Path, default=ROOT / "reports/gap-audit/pack-s2-heavy")
    p.add_argument("--min-hands", type=int, default=200, help="Min hands for rival sampling")
    p.add_argument("--max-rivals", type=int, default=15, help="Max rival profiles in pack")
    args = p.parse_args(argv)

    export_dir = args.export_dir.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    print(f"Loading export from {export_dir}...", file=sys.stderr)
    agents = load_export_agents_with_bb100(export_dir)
    submissions = load_export_submissions(export_dir)
    bb_snap = load_bb100_snapshot(export_dir)
    crawl = crawl_progress(export_dir)
    hero_row = next((a for a in agents if a.get("handle") == args.hero), None)

    print(f"  agents={len(agents)} submissions={len(submissions)}", file=sys.stderr)

    top_rivals = _select_rivals(
        agents, args.hero, min_hands=args.min_hands, max_rivals=args.max_rivals
    )
    agents_by_handle = {a.get("handle"): a for a in agents if a.get("handle")}
    print(f"  rivals (≥{args.min_hands}h, max {args.max_rivals}): {top_rivals}", file=sys.stderr)

    metrics_py = EXAMPLES / "competition_metrics_report.py"
    subprocess.run(
        [sys.executable, str(metrics_py), str(export_dir), "--hero", args.hero],
        check=False,
    )
    field_report = subprocess.run(
        [sys.executable, str(EXAMPLES / "competition_field_report.py"), str(export_dir),
         "--hero", args.hero, "--top", "30"],
        capture_output=True,
        text=True,
    )

    variance = _hero_variance_bootstrap(submissions, args.hero)
    hist = _payout_histogram(submissions, args.hero)
    metrics_path = export_dir / "metrics_report.json"
    metrics = json.loads(metrics_path.read_text()) if metrics_path.is_file() else {}

    (out / "hero_variance.json").write_text(json.dumps(variance, indent=2) + "\n", encoding="utf-8")
    (out / "hero_payout_histogram.json").write_text(json.dumps(hist, indent=2) + "\n", encoding="utf-8")
    (out / "position_breakdown.md").write_text(_position_stats(submissions, args.hero), encoding="utf-8")
    (out / "field_report.txt").write_text(field_report.stdout or field_report.stderr, encoding="utf-8")
    (out / "field_style_distribution.md").write_text(_field_style_summary(agents), encoding="utf-8")
    (out / "worst_hero_hands.txt").write_text(_worst_hero_hands(submissions, args.hero, 80), encoding="utf-8")
    rivals_table = _rivals_200plus_table(agents, args.hero, min_hands=args.min_hands)
    (out / "rivals_200plus.md").write_text(rivals_table, encoding="utf-8")
    (out / "hero_vs_rivals.md").write_text(
        _hero_vs_rival_tables(submissions, args.hero, top_rivals), encoding="utf-8"
    )

    rival_dir = out / "rival_samples"
    rival_dir.mkdir(exist_ok=True)
    rival_blocks = []
    for rival in top_rivals:
        text = _rival_samples(
            submissions,
            rival,
            limit=40,
            agent_row=agents_by_handle.get(rival),
        )
        (rival_dir / f"{rival.replace('/', '_')}.md").write_text(text, encoding="utf-8")
        rival_blocks.append(text)

    hl = ROOT / "reports/hl-loop/latest_analyze.txt"
    if hl.is_file():
        (out / "hl_analyze.txt").write_text(hl.read_text(encoding="utf-8"), encoding="utf-8")

    if bb_snap:
        (out / "bb100_ui_snapshot.json").write_text(json.dumps(bb_snap, indent=2) + "\n", encoding="utf-8")

    # Trimmed manifest — NO completed_agent_ids bloat
    manifest = {
        "built_at": datetime.now(timezone.utc).isoformat(),
        "pack_type": "heavy_aggregate",
        "export_dir": str(export_dir),
        "competition_id": metrics.get("competition_id", "cmpy2qy65002ud9ej6b7jjq0l"),
        "hero": args.hero,
        "agents_in_export": len(agents),
        "submission_rows_scanned": len(submissions),
        "crawl_summary": {
            k: crawl.get(k)
            for k in ("leaderboard_total", "cycles", "agent_offset")
            if k in crawl
        },
        "crawl_completed_count": len(crawl.get("completed_agent_ids") or []),
        "hero_rank": hero_row.get("rank") if hero_row else None,
        "hero_chips": hero_row.get("chips") if hero_row else None,
        "hero_hands": hero_row.get("hands") if hero_row else None,
        "hero_adjusted_bb100": hero_row.get("adjusted_bb100") if hero_row else None,
        "variance": variance,
        "payout_histogram": hist,
        "rival_handles_sampled": top_rivals,
        "rivals_200plus_count": sum(
            1 for a in agents
            if (a.get("handle") or "") != args.hero and int(a.get("hands") or 0) >= args.min_hands
        ),
        "min_hands_rival_gate": args.min_hands,
        "data_note": (
            f"Full export aggregated in Python; models receive stats + 80 worst hero hands "
            f"+ {len(top_rivals)} rival profiles (40 showdown rows each for ≥{args.min_hands}h), "
            "not raw jsonl."
        ),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    aggregate_block = f"""
## Heavy aggregate (full export scan)

Submission rows scanned: **{len(submissions):,}**
Hero submission rows: **{variance.get('hero_submission_rows', '?')}**
Pot win rate: **{variance.get('pot_win_rate', '?')}**
Chip-proxy bb/100 point: **{variance.get('bb100_chip_proxy_point', '?')}**
Bootstrap 95% CI: **{variance.get('bb100_bootstrap_95ci', '?')}**
Payout histogram (hero): {json.dumps(hist)}

### Hero vs top rivals (table co-occurrence)
{_hero_vs_rival_tables(submissions, args.hero, top_rivals)}

### Top rival showdown samples (full export slice)
{chr(10).join(rival_blocks[:4])}

(... {max(0, len(top_rivals) - 4)} more rivals in rival_samples/ — see pack directory)
"""

    if PROMPT_TEMPLATE.is_file():
        template = PROMPT_TEMPLATE.read_text(encoding="utf-8")
        crawl_trim = {k: crawl.get(k) for k in ("leaderboard_total", "cycles", "agent_offset")}
        crawl_trim["completed_agent_count"] = len(crawl.get("completed_agent_ids") or [])
        filled = template.format(
            export_dir=str(export_dir),
            hero=args.hero,
            manifest=json.dumps(manifest, indent=2),
            field_report=(field_report.stdout or "") + aggregate_block,
            metrics=json.dumps(metrics, indent=2),
            variance=json.dumps(variance, indent=2),
            position_breakdown=(out / "position_breakdown.md").read_text(encoding="utf-8"),
            worst_hands=(out / "worst_hero_hands.txt").read_text(encoding="utf-8"),
            style_distribution=(out / "field_style_distribution.md").read_text(encoding="utf-8"),
            hl_analyze=(out / "hl_analyze.txt").read_text(encoding="utf-8")
            if (out / "hl_analyze.txt").is_file()
            else "(not available)",
            bb100_snapshot=json.dumps(bb_snap.get("hero_analysis") or bb_snap, indent=2)
            if bb_snap
            else "(not available)",
            rivals_200plus=rivals_table,
            crawl=json.dumps(crawl_trim, indent=2),
        )
        (out / "audit_prompt.md").write_text(filled, encoding="utf-8")

    (out / "AUDIT_README.md").write_text(
        f"# Heavy audit pack\n\nBuilt: {manifest['built_at']}\n\n"
        f"- Scanned {len(submissions):,} submission rows locally\n"
        f"- 80 worst hero hands, {len(top_rivals)} rival profiles (≥{args.min_hands}h)\n"
        f"- {manifest.get('rivals_200plus_count', '?')} agents with ≥{args.min_hands} hands in field\n"
        f"- Use with cursor-audit (3 parallel subagents) or run_gap_premium_audit.py\n",
        encoding="utf-8",
    )

    print(f"Heavy pack → {out}")
    print(f"  prompt_chars={(out / 'audit_prompt.md').stat().st_size if (out / 'audit_prompt.md').is_file() else 0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
