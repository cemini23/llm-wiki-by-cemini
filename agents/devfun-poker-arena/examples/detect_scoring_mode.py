#!/usr/bin/env python3
"""Detect playground scoring mode (chips vs adjustedBbPer100 / V2/V3)."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from arena_client import ArenaClient, CREDS_PATH, DEFAULT_BASE  # noqa: E402
from export_competition_hands import fetch_leaderboard, leaderboard_adjusted_bb100  # noqa: E402
from export_bundle import load_bb100_snapshot  # noqa: E402


def _snapshot_overlay(export_dir: Path | None) -> dict | None:
    if export_dir is None:
        return None
    snap = load_bb100_snapshot(export_dir)
    if not snap:
        return None
    hero = snap.get("hero_analysis") or {}
    return {
        "source": "ui_snapshot_file",
        "schema": snap.get("schema"),
        "captured_at": snap.get("captured_at"),
        "bb100_sortable": snap.get("bb100_sortable"),
        "field_ranked_total": snap.get("field_ranked_total"),
        "agents_logged": len(snap.get("agents") or []),
        "hero_analysis": hero,
        "note": snap.get("capture_note"),
    }


def detect(client: ArenaClient, competition_id: str, export_dir: Path | None = None) -> dict:
    out: dict = {
        "competition_id": competition_id,
        "scoring_mode": "unknown",
        "adjusted_bb100_visible": False,
        "participant_fields": [],
        "match_fields": [],
        "recommendation": "",
    }
    try:
        body = client.get(f"/texas/benchmark/status?competitionId={competition_id}")
    except Exception as e:
        out["error"] = str(e)
        out["recommendation"] = "Could not reach status API — assume chip rank until verified."
        return out

    participant = body.get("participant") or {}
    match = body.get("match") or {}
    out["participant_fields"] = sorted(participant.keys()) if isinstance(participant, dict) else []
    out["match_fields"] = sorted(match.keys()) if isinstance(match, dict) else []

    for key in ("adjustedBbPer100", "rawChipDelta", "allInEvBbPer100", "aivatBbPer100"):
        if isinstance(match, dict) and key in match:
            out["adjusted_bb100_visible"] = True
            out["scoring_mode"] = "eval_style"
            out[key] = match.get(key)
            break
        if isinstance(participant, dict) and key in participant:
            out["adjusted_bb100_visible"] = True
            out["scoring_mode"] = "eval_style"
            out[key] = participant.get(key)
            break

    if out["scoring_mode"] != "eval_style":
        out["scoring_mode"] = "chip_accumulation"
        out["total_chips"] = participant.get("totalChips")
        out["total_hands"] = participant.get("totalHands")
        # UI may expose adjusted bb/100 on leaderboard before status/match fields do.
        try:
            lb_rows = fetch_leaderboard(client, competition_id)
            bb_samples = [
                v for r in lb_rows[:50]
                if (v := leaderboard_adjusted_bb100(r)) is not None
            ]
            if bb_samples:
                out["adjusted_bb100_visible"] = True
                out["scoring_mode"] = "eval_style_leaderboard"
                out["leaderboard_agents_with_bb100"] = len(bb_samples)
                out["hero_adjusted_bb100"] = leaderboard_adjusted_bb100(
                    next(
                        (r for r in lb_rows
                         if (r.get("agent") or {}).get("handle") == "cemini_wiki_poker"),
                        lb_rows[0] if lb_rows else {},
                    )
                )
                out["recommendation"] = (
                    "Leaderboard shows adjustedBbPer100 — track chip rank AND EV rank; "
                    "chip #1 can trail EV leaders (e.g. 0xJeff_ai). Keep first_protect."
                )
                return out
        except Exception as e:
            out["leaderboard_probe_error"] = str(e)
        snap_meta = _snapshot_overlay(export_dir)
        if snap_meta:
            out["adjusted_bb100_visible"] = True
            out["scoring_mode"] = "ui_snapshot_only"
            out["ui_snapshot"] = snap_meta
            out["hero_adjusted_bb100"] = (snap_meta.get("hero_analysis") or {}).get("adjusted_bb100")
            out["recommendation"] = (
                "API still chip-only; UI briefly showed Adjusted BB/100 (not sortable, removed). "
                "Use bb100_ui_snapshot.json + import_bb100_snapshot.py until API or next UI test. "
                "Chip #1 can trail EV leaders — keep first_protect."
            )
            return out
        out["recommendation"] = (
            "Playground ranks on totalChips — preserve first_protect; "
            "track participant totals; do not trust chip-proxy as EV bb/100."
        )
    else:
        out["recommendation"] = (
            "V2/V3-style metrics visible — optimize for adjustedBbPer100; "
            "run competition_metrics_report after each export."
        )
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Detect arena scoring mode for a competition")
    p.add_argument("--match", default=None, help="competitionId")
    p.add_argument("--json-out", type=Path, default=None)
    p.add_argument(
        "--export-dir",
        type=Path,
        default=None,
        help="Check bb100_ui_snapshot.json when API lacks adjustedBbPer100",
    )
    args = p.parse_args(argv)

    load_dotenv()
    api_key = None
    if CREDS_PATH.exists():
        api_key = json.loads(CREDS_PATH.read_text()).get("apiKey")
    api_key = api_key or os.environ.get("ARENA_API_KEY")
    if not api_key:
        print("ERROR: need API key", file=sys.stderr)
        return 2

    competition_id = (
        args.match
        or os.environ.get("ARENA_LOBBY_COMPETITION_ID")
        or "cmpy2qy65002ud9ej6b7jjq0l"
    )
    client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=api_key)
    try:
        report = detect(client, competition_id, export_dir=args.export_dir)
    finally:
        client.close()

    print(json.dumps(report, indent=2, sort_keys=True))
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
