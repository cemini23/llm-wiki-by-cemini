#!/usr/bin/env python3
"""Apply Playground chip-qual .env keys (not ladder HU).

Usage (on prod or local):
  python3 scripts/playground_chip_qual_apply_env.py \\
    --season 10 \\
    --comp cms0bwufmf3n8kyykdpxi6d2i \\
    --export playground-s10-live \\
    --env-path .env
"""
from __future__ import annotations

import argparse
from pathlib import Path

DEFAULT_COMPS = {
    9: "cmrt1wzu40jm911suskj9qebe",
    10: "cms0bwufmf3n8kyykdpxi6d2i",
}


def build_kv(season: int, comp: str, export_slug: str) -> dict[str, str]:
    label = f"Playground_S{season}"
    role = f"s{season}_playground"
    return {
        "ARENA_LOBBY_COMPETITION_ID": comp,
        f"S{season}_PLAYGROUND_COMP": comp,
        "CEMINI_LOBBY_LABEL": label,
        "CEMINI_LOBBY_ROLE": role,
        "CEMINI_PRIMARY": "lobby",
        "CEMINI_PRIMARY_TRACK": "playground",
        "ARENA_RESEARCHER_COMP_ID": "",
        "CEMINI_SANDBOX_PVP_SUBMIT_ONLY": "0",
        "CEMINI_TABLE_FORMAT": "6max",
        "CEMINI_RESEARCHER_MODE": "0",
        "CEMINI_TOURNAMENT_MODE": "0",
        "CEMINI_EVAL_PANEL_GATE": "0",
        "CEMINI_EVAL_PANEL_MODE": "0",
        "CEMINI_EVAL_CRUSH": "0",
        "CEMINI_ARENA_PROFILE": "",
        "CEMINI_PLACEMENT_CHASE": "0",
        "CEMINI_PACE_PHASE": "volume",
        "CEMINI_JOIN_RETRY_S": "12",
        "CEMINI_IN_QUEUE_RETRY_S": "25",
        "CEMINI_LOW_STACK_JOIN_RETRY_S": "15",
        "CEMINI_QUAL_CUTOFF_RANK": "20",
        "CEMINI_PRIZE_CUTOFF_RANK": "20",
        # Dynamic protect — real buffers (999999 disables protect)
        "CEMINI_QUAL_BUFFER_CHIPS": "1000",
        "CEMINI_LEAD_BUFFER_CHIPS": "3000",
        "CEMINI_LEAD_RANK": "5",
        "CEMINI_FIRST_RANK": "1",
        "CEMINI_FIRST_JOIN_RETRY_S": "1800",
        # Fresh-board survival (S1a premium synthesis)
        "CEMINI_COLD_START_NO_STEAL": "1",
        "CEMINI_KO_SURVIVAL": "1",
        "CEMINI_KO_SURVIVAL_HANDS": "200",
        "CEMINI_KO_SURVIVAL_MIN_STACK": "2000",
        "CEMINI_STAGGER_LOCKS": "1",
        "CEMINI_NUTS_DETECT": "1",
        "CEMINI_SANITIZE_OUTPUT": "1",
        "CEMINI_MIX_POSTFLOP": "1",
        "CEMINI_PLAYGROUND_TIMESERIES": "1",
        # S1B / nemesis (gated exploit; tighten-first early)
        "CEMINI_S1B_EXPLOIT": "1",
        "CEMINI_S1B_MIN_STACK_BB": "60",
        "CEMINI_NEMESIS_EXPLOIT": "1",
        "CEMINI_NEMESIS_TIGHT": "1",
        "CEMINI_NEMESIS_HANDLES": "hunterguy102,thaddius,v_16,0xjeff_ai,jagoan_neon",
        "CEMINI_ISO_PASSIVE_LP": "1",
        "CEMINI_NEMESIS_WIDE_PASSIVE": "1",
        "CEMINI_NEMESIS_LINEAR_AGGRO": "1",
        # Ladder / gin / solver OFF for Playground chip qual
        "CEMINI_GIN_STYLE": "0",
        "CEMINI_GIN_STYLE_PREFLOP": "0",
        "CEMINI_GIN_STYLE_POSTFLOP": "0",
        "CEMINI_GIN_STYLE_GATE": "0",
        "CEMINI_GIN_V008": "0",
        "CEMINI_GIN_V2_EXPLOITS": "0",
        "CEMINI_MAFP_CHART": "0",
        "CEMINI_SOLVER_V3": "0",
        "CEMINI_SOLVER_HARD": "0",
        "CEMINI_TRAJECTORY_BOUND": "0",
        "CEMINI_VERIFIER_BON": "0",
        "CEMINI_POSTFLOP_BUCKETS": "0",
        # Jackpots — leave off until API shows slots for this season
        "JACKPOT_ROYAL_ENABLED": "0",
        "JACKPOT_ROYAL_SHOWDOWN": "0",
        "JACKPOT_27_HUNT_ENABLED": "0",
        "CEMINI_HL_PRIMARY_COMP": comp,
        "CEMINI_EXPORT_DIR": f"reports/exports/{export_slug}",
        "CEMINI_FIELD_EXPORT_DIR": f"reports/exports/{export_slug}",
        "AGENT_VERSION": f"playground-s{season}.qual.2026-07-25",
        "ARENA_NO_AUTO_REGISTER": "1",
    }


def apply_env(path: Path, kv: dict[str, str]) -> None:
    lines: list[str] = []
    seen: set[str] = set()
    text = path.read_text() if path.exists() else ""
    for line in text.splitlines():
        if "=" in line and not line.strip().startswith("#"):
            key = line.split("=", 1)[0]
            if key in kv:
                lines.append(f"{key}={kv[key]}")
                seen.add(key)
                continue
        lines.append(line)
    for key, value in kv.items():
        if key not in seen:
            lines.append(f"{key}={value}")
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--season", type=int, default=10)
    ap.add_argument("--comp", default="")
    ap.add_argument("--export", default="")
    ap.add_argument("--env-path", default=".env")
    args = ap.parse_args()
    season = args.season
    comp = args.comp or DEFAULT_COMPS.get(season, "")
    if not comp:
        raise SystemExit(f"Need --comp for season {season}")
    export_slug = args.export or f"playground-s{season}-live"
    path = Path(args.env_path)
    kv = build_kv(season, comp, export_slug)
    apply_env(path, kv)
    print(f"Playground S{season} chip-qual env applied")
    show = (
        "ARENA_LOBBY_COMPETITION_ID",
        "CEMINI_LOBBY_ROLE",
        "CEMINI_TABLE_FORMAT",
        "CEMINI_GIN_STYLE",
        "CEMINI_STAGGER_LOCKS",
        "CEMINI_QUAL_BUFFER_CHIPS",
        "CEMINI_LEAD_BUFFER_CHIPS",
        "CEMINI_NEMESIS_TIGHT",
        "CEMINI_NEMESIS_HANDLES",
        "CEMINI_PRIMARY_TRACK",
        "CEMINI_KO_SURVIVAL_HANDS",
        "CEMINI_SANDBOX_PVP_SUBMIT_ONLY",
        "AGENT_VERSION",
    )
    text = path.read_text()
    for key in show:
        for line in text.splitlines():
            if line.startswith(key + "="):
                print(line)
                break


if __name__ == "__main__":
    main()
