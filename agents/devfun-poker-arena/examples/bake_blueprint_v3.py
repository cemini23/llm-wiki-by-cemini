#!/usr/bin/env python3
"""Offline bake: TexasSolver dumps → research/postflop_hu_buckets_v3.json.

Per-combo → hand_bucket aggregation with separate FREE vs FACING keys.
Key: ``{street}|{line}|{role}|{texture}|{spr}|{node}|{hand_bucket}``

Bet sizes: 33%, 75%, allin; raise 60%, allin.
Solver: thread_num=1, use_isomorphism=0.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
import sys
import time
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any, Optional

_EXAMPLES = Path(__file__).resolve().parent
_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from bake_texassolver_buckets import (  # noqa: E402
    _board_cards,
    _iter_strategy_hands,
    classify_action,
    load_dump,
    parse_hand_combo,
    parse_board,
    player_to_role,
    resolve_solver_bin,
    run_solver,
)
from solver_policy_v3 import (  # noqa: E402
    FACING_ACTIONS,
    FREE_ACTIONS,
    HAND_BUCKETS,
    build_key,
    facing_node,
    hand_bucket,
)

DEFAULT_GRID = _ROOT / "research" / "texassolver_spot_grid_v3.json"
DEFAULT_OUT = _ROOT / "research" / "postflop_hu_buckets_v3.json"
DEFAULT_DUMP_DIR = Path("/tmp/cemini-texassolver-dumps-v3")

MIN_SUCCESSFUL = 4


def _log(msg: str) -> None:
    print(f"[bake-blueprint-v3] {msg}", flush=True)


def _bet_sizes_for_street(bet_sizes: list[str], street: str) -> list[str]:
    st = street.lower().strip()
    filtered = []
    for bs in bet_sizes:
        parts = [p.strip() for p in str(bs).split(",")]
        if len(parts) >= 2 and parts[1].lower() == st:
            filtered.append(bs)
    return filtered or list(bet_sizes)


def build_input_text(spot: dict, defaults: dict, dump_path: Path) -> str:
    pot = spot.get("pot", defaults.get("pot", 20))
    stack = spot.get("effective_stack", defaults.get("effective_stack", 80))
    board = spot["board"]
    board_s = ",".join(board) if isinstance(board, list) else str(board)
    range_ip = spot.get("range_ip", defaults["range_ip"])
    range_oop = spot.get("range_oop", defaults["range_oop"])
    street = str(spot.get("street") or "flop").lower()
    bet_sizes = _bet_sizes_for_street(
        list(spot.get("bet_sizes", defaults.get("bet_sizes") or [])),
        street,
    )
    accuracy = spot.get("accuracy", defaults.get("accuracy", 1.5))
    max_iter = spot.get("max_iteration", defaults.get("max_iteration", 60))
    dump_rounds = spot.get("dump_rounds", defaults.get("dump_rounds", 1))
    thread_num = int(spot.get("thread_num", defaults.get("thread_num", 1)))
    use_isomorphism = int(
        spot.get("use_isomorphism", defaults.get("use_isomorphism", 0))
    )
    allin = spot.get("allin_threshold", defaults.get("allin_threshold", 0.67))

    dump_abs = dump_path.resolve()
    if " " in str(dump_abs):
        raise ValueError(f"dump path has spaces: {dump_abs}")

    lines = [
        f"set_pot {pot}",
        f"set_effective_stack {stack}",
        f"set_board {board_s}",
        f"set_range_ip {range_ip}",
        f"set_range_oop {range_oop}",
    ]
    for bs in bet_sizes:
        lines.append(f"set_bet_sizes {bs}")
    lines += [
        f"set_allin_threshold {allin}",
        "build_tree",
        f"set_thread_num {max(1, thread_num)}",
        f"set_accuracy {accuracy}",
        f"set_max_iteration {max_iter}",
        "set_print_interval 40",
        f"set_use_isomorphism {use_isomorphism}",
        "start_solve",
        f"set_dump_rounds {dump_rounds}",
        f"dump_result {dump_abs}",
    ]
    return "\n".join(lines) + "\n"


def spot_cache_key(spot: dict, defaults: dict) -> str:
    street = str(spot.get("street") or "flop").lower()
    raw_sizes = list(spot.get("bet_sizes", defaults.get("bet_sizes") or []))
    payload = {
        "id": spot.get("id"),
        "board": spot.get("board"),
        "street": street,
        "pot": spot.get("pot", defaults.get("pot")),
        "stack": spot.get("effective_stack", defaults.get("effective_stack")),
        "spr": spot.get("spr"),
        "line": spot.get("line", defaults.get("line", "srp")),
        "bet_sizes": _bet_sizes_for_street(raw_sizes, street),
        "tree": "blueprint_v3",
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:16]


def map_bet_action(size: Optional[float], pot: float, *, is_raise: bool = False) -> str:
    if size is None or pot <= 0:
        return "allin"
    frac = float(size) / float(pot)
    if frac >= 0.85:
        return "allin"
    if is_raise:
        return "raise_060"
    if frac >= 0.55:
        return "bet_075"
    return "bet_033"


def _node_is_facing(actions: list[str]) -> bool:
    keys = {classify_action(a)[0] for a in actions}
    return bool(keys & {"fold", "call"})


def _node_is_free(actions: list[str]) -> bool:
    keys = {classify_action(a)[0] for a in actions}
    return bool(keys & {"check", "bet"}) and "fold" not in keys


def extract_v3_nodes(
    root: dict,
    *,
    pot: float,
) -> list[tuple[str, str, dict]]:
    """Return (role, node_label, node_dict)."""
    out: list[tuple[str, str, dict]] = []

    def walk(node: dict, path: list[tuple[str, Optional[float]]]) -> None:
        if not isinstance(node, dict):
            return
        actions, _ = _iter_strategy_hands(node)
        if actions and (node.get("strategy") or node.get("node_type") == "action_node"):
            role = player_to_role(node.get("player", 1))
            facing = _node_is_facing(actions)
            free = _node_is_free(actions)
            call_chips = 0.0
            vs_raise = False
            if facing:
                for label, amt in reversed(path):
                    act, _ = classify_action(label)
                    if act in ("bet", "raise"):
                        call_chips = float(amt or 0.0)
                        vs_raise = act == "raise"
                        break
                node_label = facing_node(call_chips, pot, vs_raise=vs_raise)
                out.append((role, node_label, node))
            elif free:
                out.append((role, "free", node))

        children = node.get("childrens") or node.get("children") or {}
        if not isinstance(children, dict):
            return
        for label, child in children.items():
            if not isinstance(child, dict) or child.get("node_type") == "chance_node":
                continue
            act, amt = classify_action(str(label))
            walk(child, path + [(str(label), amt)])

    walk(root, [])
    return out


def accumulate_v3_node(
    acc: dict[str, dict[str, float]],
    combo_acc: dict[str, int],
    mass_acc: dict[str, float],
    *,
    street: str,
    line: str,
    role: str,
    texture: str,
    spr: str,
    node: str,
    board: list[str],
    node_dict: dict,
    pot: float,
) -> int:
    actions, hands = _iter_strategy_hands(node_dict)
    if not actions or not hands:
        return 0
    mapped = [classify_action(a) for a in actions]
    facing = node != "free"
    n = 0
    for combo, probs in hands.items():
        if not isinstance(probs, (list, tuple)):
            continue
        parsed = parse_hand_combo(str(combo))
        if parsed is None:
            continue
        hole = list(parsed)
        hb = hand_bucket(hole, _board_cards(board))
        key = build_key(street, line, role, texture, spr, node, hb)
        bucket = acc.setdefault(
            key,
            {k: 0.0 for k in (FACING_ACTIONS if facing else FREE_ACTIONS)},
        )
        combo_acc[key] = combo_acc.get(key, 0) + 1
        row_mass = 0.0
        for i, (freq_key, size) in enumerate(mapped):
            if i >= len(probs):
                break
            p = float(probs[i])
            if p <= 0:
                continue
            if facing:
                if freq_key == "fold":
                    ak = "fold"
                elif freq_key == "call":
                    ak = "call"
                elif freq_key in ("raise", "bet"):
                    ak = map_bet_action(size, pot, is_raise=True)
                else:
                    continue
            else:
                if freq_key == "check":
                    ak = "check"
                elif freq_key in ("bet", "raise"):
                    ak = map_bet_action(size, pot, is_raise=False)
                else:
                    continue
            if ak in bucket:
                bucket[ak] += p
                row_mass += p
        mass_acc[key] = mass_acc.get(key, 0.0) + row_mass
        n += 1
    return n


def finalize_v3(
    acc: dict[str, dict[str, float]],
    combo_acc: dict[str, int],
    mass_acc: dict[str, float],
) -> dict[str, dict[str, Any]]:
    buckets: dict[str, dict[str, Any]] = {}
    for key, mass in acc.items():
        parts = key.split("|")
        if len(parts) != 7:
            continue
        node = parts[5]
        facing = node != "free"
        action_keys = FACING_ACTIONS if facing else FREE_ACTIONS
        total = sum(mass.get(k, 0.0) for k in action_keys)
        if total <= 1e-12:
            continue
        freqs = {k: mass.get(k, 0.0) / total for k in action_keys}
        combos = int(combo_acc.get(key, 0))
        buckets[key] = {
            "freqs": freqs,
            "node": node,
            "combos": combos,
            "weight": float(mass_acc.get(key, 0.0) / max(combos, 1)),
            "mass": float(mass_acc.get(key, 0.0)),
        }
    return buckets


def build_payload(
    buckets: dict[str, dict[str, Any]],
    *,
    spots_solved: int,
    spots_failed: list[str],
    grid_path: Path,
) -> dict[str, Any]:
    meta = {
        "generator": "texas_solver_blueprint_v3",
        "solver": "bupticybee/TexasSolver@v0.2.0",
        "spots_solved": spots_solved,
        "spots_failed": spots_failed,
        "key_count": len(buckets),
        "baked_at": date.today().isoformat(),
        "grid": str(grid_path.as_posix()),
        "hand_bucket_method": "made_hand_categories_per_combo",
        "key_schema": "{street}|{line}|{role}|{texture}|{spr}|{node}|{hand_bucket}",
        "spr_bins": ["le2", "2to5", "gt5"],
        "hand_buckets": list(HAND_BUCKETS),
        "thread_iso": "thread_num=1 use_isomorphism=0",
    }
    return {
        "schema": "postflop-hu-buckets-v3",
        "source": "examples/bake_blueprint_v3.py",
        "meta": meta,
        "buckets": buckets,
    }


def atomic_write_json(path: Path, payload: dict[str, Any]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + f".tmp.{secrets.token_hex(4)}")
    try:
        tmp.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass
    return path


def run_solver_v3(
    bin_path: Path,
    spot: dict,
    defaults: dict,
    dump_path: Path,
    *,
    timeout_s: int = 600,
) -> None:
    """Run v3 spot with thread=1 iso=0; retry once on abort."""
    last_err: Optional[Exception] = None
    for attempt in range(2):
        merged = {**defaults, **spot, "thread_num": 1, "use_isomorphism": 0}
        inp = build_input_text(merged, defaults, dump_path)
        try:
            if attempt:
                _log("  retry thread=1 iso=0")
            run_solver(bin_path, inp, dump_path, timeout_s=timeout_s)
            return
        except Exception as exc:
            last_err = exc
            _log(f"  solver attempt failed: {exc}")
    raise RuntimeError(f"all solver attempts failed: {last_err}")


def bake(
    *,
    grid_path: Path,
    out_path: Path,
    dump_dir: Path,
    bin_path: Path,
    max_spots: Optional[int] = None,
    min_successful: int = MIN_SUCCESSFUL,
    timeout_s: int = 600,
    skip_solve: bool = False,
) -> dict[str, Any]:
    grid = json.loads(Path(grid_path).read_text(encoding="utf-8"))
    defaults = grid.get("defaults") or {}
    spots = list(grid.get("spots") or [])
    if max_spots is not None and max_spots > 0:
        spots = spots[:max_spots]

    dump_dir = Path(dump_dir)
    dump_dir.mkdir(parents=True, exist_ok=True)

    acc: dict[str, dict[str, float]] = {}
    combo_acc: dict[str, int] = defaultdict(int)
    mass_acc: dict[str, float] = defaultdict(float)
    ok_ids: list[str] = []
    failed: list[str] = []

    for spot in spots:
        sid = str(spot.get("id") or spot.get("board"))
        street = str(spot.get("street") or "flop").lower()
        texture = str(spot.get("texture") or "dry").lower()
        line = str(spot.get("line") or defaults.get("line") or "srp").lower()
        spr = str(spot.get("spr") or "2to5").lower()
        board = parse_board(spot)
        pot = float(spot.get("pot", defaults.get("pot", 20)))
        ck = spot_cache_key(spot, defaults)
        dump_path = dump_dir / f"{sid}_{ck}.json"

        try:
            if dump_path.is_file() and dump_path.stat().st_size > 50:
                _log(f"cache hit {sid}")
                root = load_dump(dump_path)
            elif skip_solve:
                raise RuntimeError(f"no cache for {sid} and --skip-solve set")
            else:
                _log(f"solving {sid} board={','.join(board)} spr={spr} …")
                t0 = time.time()
                run_solver_v3(
                    bin_path,
                    spot,
                    defaults,
                    dump_path,
                    timeout_s=timeout_s,
                )
                root = load_dump(dump_path)
                _log(
                    f"  ok {sid} in {time.time() - t0:.1f}s "
                    f"({dump_path.stat().st_size} bytes)"
                )

            nodes = extract_v3_nodes(root, pot=pot)
            n_hands = 0
            for role, node_label, node_dict in nodes:
                n_hands += accumulate_v3_node(
                    acc,
                    combo_acc,
                    mass_acc,
                    street=street,
                    line=line,
                    role=role,
                    texture=texture,
                    spr=spr,
                    node=node_label,
                    board=board,
                    node_dict=node_dict,
                    pot=pot,
                )
            if n_hands <= 0:
                raise RuntimeError("no strategy hands extracted")
            ok_ids.append(sid)
            _log(f"  aggregated {sid}: {len(nodes)} nodes, {n_hands} hand rows")
        except Exception as exc:
            failed.append(f"{sid}: {exc}")
            _log(f"FAIL {sid}: {exc}")
            continue

    if len(ok_ids) < min_successful:
        raise SystemExit(
            f"Need ≥{min_successful} successful spots, got {len(ok_ids)}. "
            f"Failed: {failed[:5]}"
        )

    buckets = finalize_v3(acc, combo_acc, mass_acc)
    payload = build_payload(
        buckets,
        spots_solved=len(ok_ids),
        spots_failed=failed,
        grid_path=Path(grid_path),
    )
    atomic_write_json(out_path, payload)
    _log(
        f"wrote {out_path} keys={len(buckets)} "
        f"spots_ok={len(ok_ids)} failed={len(failed)}"
    )
    return payload


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Bake blueprint v3 from TexasSolver")
    ap.add_argument("--grid", type=Path, default=DEFAULT_GRID)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--dump-dir", type=Path, default=DEFAULT_DUMP_DIR)
    ap.add_argument("--bin", type=Path, default=None)
    ap.add_argument("--max-spots", type=int, default=0, help="Limit spots (smoke)")
    ap.add_argument("--min-successful", type=int, default=MIN_SUCCESSFUL)
    ap.add_argument(
        "--timeout",
        type=int,
        default=int(os.environ.get("CEMINI_TEXASSOLVER_TIMEOUT", "900")),
    )
    ap.add_argument("--skip-solve", action="store_true")
    args = ap.parse_args(argv)

    bin_path = Path(args.bin).resolve() if args.bin else resolve_solver_bin()
    max_spots = args.max_spots if args.max_spots > 0 else None
    min_ok = args.min_successful
    if max_spots:
        min_ok = min(min_ok, max_spots)

    payload = bake(
        grid_path=Path(args.grid),
        out_path=Path(args.out),
        dump_dir=Path(args.dump_dir),
        bin_path=bin_path,
        max_spots=max_spots,
        min_successful=min_ok,
        timeout_s=args.timeout,
        skip_solve=args.skip_solve,
    )
    meta = payload.get("meta") or {}
    assert meta.get("generator") == "texas_solver_blueprint_v3"
    assert int(meta.get("key_count") or 0) >= 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
