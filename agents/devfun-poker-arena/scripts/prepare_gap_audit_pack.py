#!/usr/bin/env python3
"""Build self-contained audit pack for S1a gap premium audit (3-model cursor-audit).

Writes reports/gap-audit/pack/ with metrics, field report, hero samples, manifest.

Usage:
  uv run python scripts/prepare_gap_audit_pack.py reports/exports/playground-s1-live/
  uv run python scripts/prepare_gap_audit_pack.py reports/exports/playground-s1-live/ \\
      --hero cemini_wiki_poker --out reports/gap-audit/pack
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
PROMPT_TEMPLATE = ROOT / "prompts" / "s1a_gap_retrospective_audit.md"
if str(EXAMPLES) not in sys.path:
    sys.path.insert(0, str(EXAMPLES))

from export_bundle import crawl_progress, load_export_agents_with_bb100, load_export_submissions, load_bb100_snapshot  # noqa: E402


def _hero_variance_bootstrap(
    submissions: list[dict],
    hero_handle: str,
    *,
    initial_chips: int = 1000,
    big_blind: int = 20,
    n_boot: int = 500,
) -> dict:
    """Bootstrap chip-proxy bb/100 from hero submission rows (pot-win proxy, not EV)."""
    rows = [r for r in submissions if r.get("agent_handle") == hero_handle]
    if len(rows) < 50:
        return {"note": "insufficient hero rows", "n": len(rows)}

    payouts = [int(r.get("payout_chips") or 0) for r in rows]
    pot_win_rate = sum(1 for p in payouts if p > 0) / len(rows)
    # Rough per-hand chip proxy: treat pot win as +pot, loss as -bb (conservative)
    deltas = []
    for p in payouts:
        if p > 0:
            deltas.append(p * 0.35)
        else:
            deltas.append(-big_blind * 0.5)
    mean_bb100 = (sum(deltas) / big_blind) / len(deltas) * 100

    import random

    rng = random.Random(42)
    samples = []
    for _ in range(n_boot):
        pick = [deltas[rng.randrange(len(deltas))] for _ in range(len(deltas))]
        s = sum(pick)
        samples.append((s / big_blind) / len(pick) * 100)
    samples.sort()
    lo = samples[int(n_boot * 0.025)]
    hi = samples[int(n_boot * 0.975)]
    return {
        "hero_submission_rows": len(rows),
        "pot_win_rate": round(pot_win_rate, 4),
        "bb100_chip_proxy_point": round(mean_bb100, 2),
        "bb100_bootstrap_95ci": [round(lo, 2), round(hi, 2)],
        "note": "NOT all-in EV — submission payout_chips ≥ 0 only; use for de-luck sanity check",
    }


def _position_breakdown(submissions: list[dict], hero_handle: str) -> str:
    rows = [r for r in submissions if r.get("agent_handle") == hero_handle]
    by_pos: dict[str, list[int]] = defaultdict(list)
    for r in rows:
        pos = str(r.get("position") or r.get("seat") or "?")
        by_pos[pos].append(int(r.get("payout_chips") or 0))
    lines = ["| Position | Hands | Pot wins | Win rate |", "|----------|-------|----------|----------|"]
    for pos in sorted(by_pos.keys()):
        vals = by_pos[pos]
        wins = sum(1 for v in vals if v > 0)
        lines.append(f"| {pos} | {len(vals)} | {wins} | {wins / max(len(vals), 1):.1%} |")
    return "\n".join(lines)


def _villain_showdown_sample(submissions: list[dict], hero_handle: str, limit: int = 40) -> str:
    """Sample hero rows with board + hole cards for structural leak review."""
    rows = [r for r in submissions if r.get("agent_handle") == hero_handle]
    rows.sort(key=lambda r: int(r.get("payout_chips") or 0))
    lines = []
    for r in rows[:limit]:
        lines.append(
            f"payout={r.get('payout_chips')} pos={r.get('position')} "
            f"hole={r.get('hole_cards')} board={r.get('board_cards')} "
            f"table={r.get('table_id', '?')[:12]}"
        )
    return "\n".join(lines)


def _style_distribution(agents: list[dict]) -> str:
    styles = Counter((a.get("stats") or {}).get("playing_style") or "?" for a in agents)
    lines = ["| Style | Count |", "|-------|-------|"]
    for style, n in styles.most_common(15):
        lines.append(f"| {style} | {n} |")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Prepare S1a gap audit pack")
    p.add_argument("export_dir", type=Path)
    p.add_argument("--hero", default="cemini_wiki_poker")
    p.add_argument("--out", type=Path, default=ROOT / "reports/gap-audit/pack")
    p.add_argument("--initial-chips", type=int, default=1000)
    args = p.parse_args(argv)

    export_dir = args.export_dir.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    agents = load_export_agents_with_bb100(export_dir)
    submissions = load_export_submissions(export_dir)
    bb_snap = load_bb100_snapshot(export_dir)
    crawl = crawl_progress(export_dir)

    hero = next((a for a in agents if a.get("handle") == args.hero), None)
    if not hero:
        print(f"WARN: hero {args.hero} not in export", file=sys.stderr)

    metrics_py = EXAMPLES / "competition_metrics_report.py"
    subprocess.run(
        [sys.executable, str(metrics_py), str(export_dir), "--hero", args.hero],
        check=False,
    )
    field_report = subprocess.run(
        [sys.executable, str(EXAMPLES / "competition_field_report.py"), str(export_dir),
         "--hero", args.hero, "--top", "25"],
        capture_output=True,
        text=True,
    )
    (out / "field_report.txt").write_text(field_report.stdout or field_report.stderr, encoding="utf-8")

    metrics_path = export_dir / "metrics_report.json"
    metrics = json.loads(metrics_path.read_text()) if metrics_path.is_file() else {}

    variance = _hero_variance_bootstrap(submissions, args.hero, initial_chips=args.initial_chips)
    (out / "hero_variance.json").write_text(json.dumps(variance, indent=2) + "\n", encoding="utf-8")
    (out / "position_breakdown.md").write_text(_position_breakdown(submissions, args.hero), encoding="utf-8")
    (out / "worst_hero_hands.txt").write_text(
        _villain_showdown_sample(submissions, args.hero, limit=50), encoding="utf-8"
    )
    (out / "field_style_distribution.md").write_text(_style_distribution(agents), encoding="utf-8")

    hl_analyze = ROOT / "reports/hl-loop/latest_analyze.txt"
    if hl_analyze.is_file():
        (out / "hl_analyze.txt").write_text(hl_analyze.read_text(encoding="utf-8"), encoding="utf-8")

    if bb_snap:
        (out / "bb100_ui_snapshot.json").write_text(
            json.dumps(bb_snap, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        hero_ev = bb_snap.get("hero_analysis") or {}
        (out / "bb100_hero_analysis.md").write_text(
            "## Hero EV vs chip rank (UI snapshot)\n\n"
            + json.dumps(hero_ev, indent=2)
            + "\n",
            encoding="utf-8",
        )

    manifest = {
        "built_at": datetime.now(timezone.utc).isoformat(),
        "export_dir": str(export_dir),
        "competition_id": os.environ.get("ARENA_LOBBY_COMPETITION_ID", "cmpy2qy65002ud9ej6b7jjq0l"),
        "hero": args.hero,
        "agents": len(agents),
        "submission_rows": len(submissions),
        "crawl": crawl,
        "hero_rank": hero.get("rank") if hero else None,
        "hero_chips": hero.get("chips") if hero else None,
        "hero_hands": hero.get("hands") if hero else None,
        "metrics_summary": {
            k: metrics.get(k)
            for k in ("rank", "chips", "hands", "vpip", "pfr", "chip_accumulation_proxy", "v2_v3_readiness")
        },
        "variance": variance,
        "files": [],
    }

    for name in out.iterdir():
        if name.is_file():
            manifest["files"].append(name.name)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if PROMPT_TEMPLATE.is_file():
        template = PROMPT_TEMPLATE.read_text(encoding="utf-8")
        filled = template.format(
            export_dir=str(export_dir),
            hero=args.hero,
            manifest=json.dumps(manifest, indent=2),
            field_report=field_report.stdout or "",
            metrics=json.dumps(metrics, indent=2),
            variance=json.dumps(variance, indent=2),
            position_breakdown=(out / "position_breakdown.md").read_text(encoding="utf-8"),
            worst_hands=(out / "worst_hero_hands.txt").read_text(encoding="utf-8"),
            style_distribution=(out / "field_style_distribution.md").read_text(encoding="utf-8"),
            hl_analyze=(out / "hl_analyze.txt").read_text(encoding="utf-8") if (out / "hl_analyze.txt").is_file() else "(not available)",
            bb100_snapshot=json.dumps(bb_snap.get("hero_analysis") or bb_snap, indent=2) if bb_snap else "(not available — see briefs/2026-06-08_s1a-adjusted-bb100-ui-snapshot.md)",
            crawl=json.dumps(crawl, indent=2),
        )
        (out / "audit_prompt.md").write_text(filled, encoding="utf-8")

    print(f"Audit pack → {out}")
    print(f"  agents={len(agents)} submissions={len(submissions)} crawl={len(crawl.get('completed_agent_ids') or [])}/{crawl.get('leaderboard_total', '?')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
