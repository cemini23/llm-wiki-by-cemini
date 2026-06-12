#!/usr/bin/env python3
"""Multi-competition oracle — S1 tournament (primary) + S2 playground (intel only).

Appends read-only snapshots to reports/hl-loop/multi_comp_timeseries.jsonl.
Does not auto-deploy; S1 tournament is the only comp that should drive patches.

Usage:
  uv run python examples/multi_comp_registry.py init-config
  uv run python examples/multi_comp_registry.py discover
  uv run python examples/multi_comp_registry.py snapshot
  uv run python examples/multi_comp_registry.py snapshot --export
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv

_EXAMPLES = Path(__file__).resolve().parent
_AGENT_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from analyze import _fetch_replays  # noqa: E402
from arena_client import ArenaClient, ArenaError, CREDS_PATH, DEFAULT_BASE  # noqa: E402
from arena_monitor import _fetch_active_competitions  # noqa: E402
from cemini_hl_hand_count import fetch_hand_count, _load_agent_id  # noqa: E402
from export_competition_hands import (  # noqa: E402
    export_competition,
    leaderboard_adjusted_bb100,
)

CONFIG_SCHEMA = "devfun.multi_comp_config.v1"
TIMESERIES_SCHEMA = "devfun.multi_comp_timeseries.v1"

_DEFAULT_S2 = "cmq57o53r0bhw18g23qkydb08"
_DEFAULT_S1_PLAYGROUND = "cmpy2qy65002ud9ej6b7jjq0l"


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def hl_dir() -> Path:
    raw = os.environ.get("CEMINI_HL_REPORTS_DIR", "").strip()
    return Path(raw) if raw else _AGENT_ROOT / "reports" / "hl-loop"


def config_path() -> Path:
    raw = os.environ.get("CEMINI_MULTI_COMP_CONFIG", "").strip()
    return Path(raw) if raw else hl_dir() / "multi_comp_config.json"


def timeseries_path() -> Path:
    raw = os.environ.get("CEMINI_MULTI_COMP_TIMESERIES", "").strip()
    return Path(raw) if raw else hl_dir() / "multi_comp_timeseries.jsonl"


def _git_commit_short() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=_AGENT_ROOT,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return None


def _load_api_key() -> str | None:
    raw = os.environ.get("ARENA_API_KEY")
    if raw and raw.strip():
        return raw.strip()
    for path in (CREDS_PATH, _AGENT_ROOT / ".arena-credentials"):
        if path.is_file():
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("apiKey"):
                return data["apiKey"]
    return None


def default_config() -> dict[str, Any]:
    lobby = (
        os.environ.get("ARENA_LOBBY_COMPETITION_ID", "").strip()
        or _DEFAULT_S2
    )
    s1 = os.environ.get("S1_TOURNAMENT_COMP", "").strip()
    return {
        "schema": CONFIG_SCHEMA,
        "updated": _utc_now(),
        "primary": {
            "role": "s1_tournament",
            "label": "Tournament S1",
            "competition_id": s1,
            "priority": 1,
            "drives_deploy": True,
            "export_dir": "reports/exports/s1-tournament-live",
        },
        "secondary": [
            {
                "role": "s2_playground",
                "label": "Playground S2",
                "competition_id": os.environ.get(
                    "S2_PLAYGROUND_COMP", _DEFAULT_S2
                ).strip() or _DEFAULT_S2,
                "priority": 2,
                "drives_deploy": False,
                "export_dir": "reports/exports/s2-playground-live",
            },
        ],
        "lobby_competition_id": lobby,
        "notes": "primary=S1 tournament patches; secondary=S2 field intel only",
    }


def load_config() -> dict[str, Any]:
    path = config_path()
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except Exception:
            pass
    return default_config()


def write_config(cfg: dict[str, Any]) -> Path:
    cfg["updated"] = _utc_now()
    path = config_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cfg, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def init_config() -> Path:
    return write_config(default_config())


def _is_tournament_s1(comp: dict) -> bool:
    name = (comp.get("name") or comp.get("title") or "").lower()
    if "tournament" not in name:
        return False
    return "s1" in name or "season 1" in name or re.search(r"\bs1\b", name)


def discover_s1_tournament(client: ArenaClient) -> Optional[dict]:
    for comp in _fetch_active_competitions(client):
        if _is_tournament_s1(comp):
            return comp
    return None


def discover_and_update_config(client: ArenaClient) -> dict[str, Any]:
    cfg = load_config()
    found = discover_s1_tournament(client)
    if found and found.get("id"):
        cfg.setdefault("primary", {})
        cfg["primary"]["competition_id"] = found["id"]
        cfg["primary"]["label"] = found.get("name") or cfg["primary"].get("label")
        cfg["primary"]["discovered_at"] = _utc_now()
    write_config(cfg)
    return cfg


def primary_competition_id(cfg: Optional[dict] = None) -> str:
    cfg = cfg or load_config()
    primary = cfg.get("primary") or {}
    cid = (primary.get("competition_id") or "").strip()
    if cid:
        return cid
    for key in ("S1_TOURNAMENT_COMP", "CEMINI_HL_PRIMARY_COMP", "ARENA_LOBBY_COMPETITION_ID"):
        env = os.environ.get(key, "").strip()
        if env:
            return env
    return ""


def all_comp_entries(cfg: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    primary = cfg.get("primary")
    if isinstance(primary, dict) and primary.get("competition_id"):
        rows.append(primary)
    for sec in cfg.get("secondary") or []:
        if isinstance(sec, dict) and sec.get("competition_id"):
            rows.append(sec)
    return rows


def snapshot_competition(
    client: ArenaClient,
    entry: dict[str, Any],
    *,
    agent_id: str | None,
    lobby_competition_id: str | None,
) -> dict[str, Any]:
    comp_id = str(entry.get("competition_id") or "")
    role = str(entry.get("role") or "unknown")
    priority = int(entry.get("priority") or 99)
    drives_deploy = bool(entry.get("drives_deploy"))

    hand_info = fetch_hand_count(client, comp_id, agent_id=agent_id)
    hands = int(hand_info.get("hands") or 0)
    rank = hand_info.get("rank")
    chips = hand_info.get("chips")

    adj_bb100: float | None = None
    try:
        from export_competition_hands import fetch_leaderboard  # noqa: WPS433

        for row in fetch_leaderboard(client, comp_id):
            ag = row.get("agent") or {}
            if agent_id and ag.get("id") == agent_id:
                adj_bb100 = leaderboard_adjusted_bb100(row)
                break
            if hand_info.get("handle") and ag.get("handle") == hand_info.get("handle"):
                adj_bb100 = leaderboard_adjusted_bb100(row)
                break
    except ArenaError:
        pass

    replay_delta_sum: int | None = None
    replay_delta_n = 0
    replay_delta_avg: float | None = None
    if agent_id:
        replays = _fetch_replays(
            client, agent_id, limit=50, competition_id=comp_id
        )
        if replays:
            vals = list(replays.values())
            replay_delta_sum = sum(vals)
            replay_delta_n = len(vals)
            replay_delta_avg = round(replay_delta_sum / replay_delta_n, 2)

    commit = _git_commit_short()
    agent_version = os.environ.get("AGENT_VERSION", "").strip()

    row: dict[str, Any] = {
        "schema": TIMESERIES_SCHEMA,
        "ts": _utc_now(),
        "role": role,
        "label": entry.get("label"),
        "priority": priority,
        "drives_deploy": drives_deploy,
        "competition_id": comp_id,
        "hands": hands,
        "hand_count_source": hand_info.get("source"),
        "rank": rank,
        "chips": chips,
        "adjusted_bb100": adj_bb100,
        "replay_chip_delta_sum": replay_delta_sum,
        "replay_chip_delta_n": replay_delta_n,
        "replay_chip_delta_avg": replay_delta_avg,
        "lobby_active": bool(lobby_competition_id and comp_id == lobby_competition_id),
        "agent_id": agent_id,
        "handle": hand_info.get("handle"),
    }
    if commit:
        row["commit"] = commit
    if agent_version:
        row["agent_version"] = agent_version
    return row


def append_timeseries_row(row: dict[str, Any]) -> Path:
    path = timeseries_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, separators=(",", ":")) + "\n")
    return path


def _export_int_env(name: str, default: int) -> int:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        return max(0, int(raw))
    except ValueError:
        return default


def run_export_append(
    client: ArenaClient,
    entry: dict[str, Any],
    *,
    hero_agent_id: str | None,
) -> int:
    comp_id = str(entry.get("competition_id") or "")
    export_dir = entry.get("export_dir") or f"reports/exports/{comp_id}"
    out = Path(_AGENT_ROOT) / export_dir
    top_agents = _export_int_env("CEMINI_EXPORT_TOP_AGENTS", 200)
    stats_top = _export_int_env("CEMINI_EXPORT_STATS_TOP", 200)
    replays_top = _export_int_env("CEMINI_EXPORT_REPLAYS_TOP", 50)
    data = export_competition(
        client,
        comp_id,
        mode="recent",
        top_agents=top_agents,
        fetch_stats=True,
        stats_top=stats_top,
        with_replays=True,
        replays_top_agents=replays_top,
        hero_agent_id=hero_agent_id,
    )
    from export_competition_hands import _append_jsonl  # noqa: WPS433

    from export_competition_hands import _append_chip_delta_sidecar  # noqa: WPS433

    n_tables = _append_jsonl(out / "tables.jsonl", data["tables"], "table_id")
    n_subs = _append_jsonl(out / "submissions.jsonl", data["submissions"], "submission_id")
    n_delta = _append_chip_delta_sidecar(out, data["submissions"])
    (out / "agents.jsonl").write_text(
        "\n".join(json.dumps(r, sort_keys=True) for r in data["agents"]) + "\n",
        encoding="utf-8",
    )
    (out / "summary.json").write_text(
        json.dumps(data["summary"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return n_tables + n_subs + n_delta


def run_snapshot(
    client: ArenaClient,
    *,
    export: bool = False,
    discover: bool = True,
) -> list[dict[str, Any]]:
    cfg = discover_and_update_config(client) if discover else load_config()
    agent_id = _load_agent_id()
    lobby = (cfg.get("lobby_competition_id") or "").strip()
    if not lobby:
        lobby = os.environ.get("ARENA_LOBBY_COMPETITION_ID", "").strip()

    rows: list[dict[str, Any]] = []
    for entry in all_comp_entries(cfg):
        comp_id = entry.get("competition_id")
        if not comp_id:
            continue
        row = snapshot_competition(
            client, entry, agent_id=agent_id, lobby_competition_id=lobby or None
        )
        append_timeseries_row(row)
        rows.append(row)
        tag = "PRIMARY" if row.get("drives_deploy") else "intel"
        print(
            f"[multi-comp] {tag} {row.get('label')} {comp_id}: "
            f"hands={row.get('hands')} rank={row.get('rank')} "
            f"replay_avg={row.get('replay_chip_delta_avg')}"
        )
        if export:
            if row.get("drives_deploy"):
                n = run_export_append(client, entry, hero_agent_id=agent_id)
                print(f"[multi-comp] export primary → {entry.get('export_dir')} (+{n} rows)")
            else:
                print(f"[multi-comp] skip export for {row.get('role')} (intel only)")

    return rows


def latest_primary_snapshot() -> dict[str, Any] | None:
    path = timeseries_path()
    if not path.is_file():
        return None
    last: dict[str, Any] | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get("drives_deploy") or row.get("role") == "s1_tournament":
            last = row
    return last


def deploy_allowed_from_oracle(min_primary_hands: int = 80) -> tuple[bool, str]:
    """S1 tournament must have enough hands; S2 never authorizes deploy."""
    primary = latest_primary_snapshot()
    if not primary:
        return False, "no primary snapshot — run multi_comp snapshot"
    hands = int(primary.get("hands") or 0)
    if hands < min_primary_hands:
        return False, f"S1 hands={hands} < {min_primary_hands} (need more tournament data)"
    return True, f"S1 primary OK hands={hands} — patch/deploy from S1 analyze only"


def main(argv: Optional[list[str]] = None) -> int:
    load_dotenv(_AGENT_ROOT / ".env")
    p = argparse.ArgumentParser(description="Multi-comp oracle (S1 primary)")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init-config", help="Write default multi_comp_config.json")

    sub.add_parser("discover", help="Discover S1 tournament in list-active")

    snap = sub.add_parser("snapshot", help="Append oracle row per configured comp")
    snap.add_argument("--export", action="store_true", help="Append export for primary only")
    snap.add_argument("--no-discover", action="store_true")

    gate = sub.add_parser("deploy-gate", help="Check S1 hands threshold for HL deploy")
    gate.add_argument("--min-hands", type=int, default=80)

    args = p.parse_args(argv)

    if args.cmd == "init-config":
        path = init_config()
        print(f"multi_comp_config → {path}")
        return 0

    key = _load_api_key()
    if not key:
        print("ERROR: ARENA_API_KEY or .arena-credentials required", file=sys.stderr)
        return 2

    client = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=key)
    try:
        if args.cmd == "discover":
            cfg = discover_and_update_config(client)
            cid = (cfg.get("primary") or {}).get("competition_id")
            print(f"primary competition_id={cid or 'NOT FOUND'}")
            return 0 if cid else 1

        if args.cmd == "snapshot":
            run_snapshot(
                client,
                export=args.export,
                discover=not args.no_discover,
            )
            return 0

        if args.cmd == "deploy-gate":
            ok, msg = deploy_allowed_from_oracle(min_primary_hands=args.min_hands)
            print(msg)
            return 0 if ok else 1
    finally:
        client.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
