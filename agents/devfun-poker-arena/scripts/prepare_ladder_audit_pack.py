#!/usr/bin/env python3
"""Build audit pack for S1 heads-up ladder premium gap audit."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPT = ROOT / "prompts" / "s1_ladder_gap_audit.md"
DEFAULT_AUDIT = ROOT / "reports/researcher-round/s1-ladder-audit-20260703T2024Z"
DEFAULT_ANALYZE = ROOT / "reports/researcher-round/ladder-analyze-20260705.txt"
DEFAULT_OUT = ROOT / "reports/gap-audit/pack-ladder-s1"


def _load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def _worst_clusters(replays: list[dict], analyze_text: str) -> str:
    buckets: Counter[str] = Counter()
    for r in replays:
        d = int(r.get("chipDelta") or 0)
        if d >= -20:
            continue
        if d <= -500:
            buckets["catastrophic_stackoff"] += 1
        elif d <= -100:
            buckets["large_loss"] += 1
        else:
            buckets["medium_loss"] += 1
    villains = Counter(r.get("winnerHandle") or "?" for r in replays if int(r.get("chipDelta") or 0) < 0)
    lines = [
        f"catastrophic (≤-500): {buckets['catastrophic_stackoff']}",
        f"large (-100..-500): {buckets['large_loss']}",
        f"medium (-20..-100): {buckets['medium_loss']}",
        "",
        "Villains on losing replays:",
    ]
    for v, n in villains.most_common(8):
        lines.append(f"  {v}: {n}")
    lines.append("")
    if "delta=-1000" in analyze_text:
        lines.append("Fresh analyze: multiple -1000 SB/BTN stackoffs vs Caravan (JJ set/straight, weak pairs).")
    if "delta=-950" in analyze_text or "delta=-940" in analyze_text:
        lines.append("Prior audit: A6o/A2s preflop pot-committed folds (patched).")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--audit-dir", type=Path, default=DEFAULT_AUDIT)
    p.add_argument("--analyze", type=Path, default=DEFAULT_ANALYZE)
    p.add_argument("--out", type=Path, default=DEFAULT_OUT)
    p.add_argument(
        "--live-posture",
        type=str,
        default=(
            '{"submission":"cef05ccb","hands":3600,"rank":"100/130",'
            '"trueskillScore":-84,"adjBbPer100":44.1,"mu":-56,"sigma":9.4}'
        ),
    )
    args = p.parse_args(argv)

    audit_dir = args.audit_dir.resolve()
    analyze_text = args.analyze.read_text(encoding="utf-8") if args.analyze.is_file() else ""
    replays = _load_jsonl(audit_dir / "cemini_wiki_poker/replays.jsonl")
    stats_path = audit_dir / "cemini_wiki_poker/agent-stats.json"
    hero_stats = json.loads(stats_path.read_text()) if stats_path.is_file() else {}

    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    (out / "replays.json").write_text(json.dumps(replays, indent=2) + "\n", encoding="utf-8")
    (out / "failure_analyze.txt").write_text(analyze_text, encoding="utf-8")
    (out / "hero_stats.json").write_text(json.dumps(hero_stats, indent=2) + "\n", encoding="utf-8")

    template = PROMPT.read_text(encoding="utf-8")
    prompt = (
        template.replace("{live_posture}", args.live_posture)
        .replace("{hero_stats}", json.dumps(hero_stats, indent=2))
        .replace("{failure_analyze}", analyze_text[:12000])
        .replace("{replays}", json.dumps(replays[:50], indent=2))
        .replace("{worst_clusters}", _worst_clusters(replays, analyze_text))
    )
    (out / "audit_prompt.md").write_text(prompt, encoding="utf-8")

    meta = {
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "audit_dir": str(audit_dir),
        "replay_count": len(replays),
        "prompt_chars": len(prompt),
    }
    (out / "manifest.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
