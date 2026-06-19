#!/usr/bin/env python3
"""Self-play KPI audit for cemini decide() — catches VPIP / EP leaks pytest misses.

The starter kit tests `examples/agent.py` (skeleton), not your custom decide(),
and HU scenarios hide 6-max position + HUD paths. This script runs offline
6-max self-play with `--training-hud`, records hero decisions, and optionally
**gates** deploy when KPIs drift.

Usage:
    uv run python examples/cemini_selfplay_audit.py
    uv run python examples/cemini_selfplay_audit.py --gate
    uv run python examples/cemini_selfplay_audit.py --hands 800 --seed 42 --gate

Exit 0 = pass (or report-only). Exit 1 = gate failed.
"""
from __future__ import annotations

import argparse
import os
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional

_EXAMPLES = Path(__file__).resolve().parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from position_utils import hero_position_label  # noqa: E402
from selfplay import run_selfplay, _load_decide_from_path  # noqa: E402


@dataclass
class HeroAudit:
    preflop_seen: int = 0
    vpip: int = 0
    pfr: int = 0
    ep_opportunities: int = 0
    ep_trash_raises: int = 0
    by_position: Counter = field(default_factory=Counter)
    vpip_by_position: Counter = field(default_factory=Counter)
    trash_hands_opened: list[str] = field(default_factory=list)
    _vpip_hands: set[str] = field(default_factory=set)
    _pfr_hands: set[str] = field(default_factory=set)
    _counted_hands: set[str] = field(default_factory=set)
    _ep_opp_hands: set[str] = field(default_factory=set)

    _TRASH = frozenset({
        "72o", "73o", "74o", "75o", "76o", "82o", "83o", "84o", "85o",
        "92o", "93o", "94o", "95o", "96o", "J2o", "J3o", "J4o", "Q2o",
        "K2o", "K3o", "K4o", "T2o", "T3o", "32o", "42o", "52o", "62o",
    })

    def record(self, table: dict, action: dict) -> None:
        street = (table.get("street") or "").lower()
        if street != "preflop":
            return

        hand_key = str(table.get("tableId") or table.get("id") or "")
        if not hand_key:
            return

        act = (action.get("action") or "").lower()
        pos = hero_position_label(table)
        allowed = table.get("allowedActions") or {}
        call_chips = int(allowed.get("callChips") or 0)
        bb = int(table.get("bigBlindChips") or 20)
        sb = int(table.get("smallBlindChips") or 10)
        facing_raise = call_chips > bb

        # One VPIP/PFR sample per hand (first hero preflop decision).
        if hand_key in self._counted_hands:
            return

        self._counted_hands.add(hand_key)
        self.preflop_seen += 1
        self.by_position[pos] += 1

        seats = table.get("seats") or []
        sn = table.get("selfSeatNumber")
        hero = next((s for s in seats if s.get("seatNumber") == sn), {})
        hole = hero.get("holeCards") or []
        if len(hole) == 2:
            from agent import _hand_class  # noqa: WPS433

            hc = _hand_class(list(hole)) or ""
        else:
            hc = ""

        if act in ("bet", "raise", "all-in"):
            self._vpip_hands.add(hand_key)
            self.vpip += 1
            self.vpip_by_position[pos] += 1
            if not facing_raise:
                self._pfr_hands.add(hand_key)
                self.pfr += 1
                if pos in ("UTG", "MP") and hc in self._TRASH:
                    self.ep_trash_raises += 1
                    self.trash_hands_opened.append(f"{hc}@{pos}")
        elif act == "call":
            # BB check behind unopened pot is not VPIP; SB complete is.
            is_bb_free = pos == "BB" and call_chips == 0
            if not is_bb_free:
                self._vpip_hands.add(hand_key)
                self.vpip += 1
                self.vpip_by_position[pos] += 1

        if pos in ("UTG", "MP") and not facing_raise and hand_key not in self._ep_opp_hands:
            self._ep_opp_hands.add(hand_key)
            self.ep_opportunities += 1


def _wrap_decide(fn: Callable, audit: HeroAudit) -> Callable:
    def wrapped(table: dict, **kwargs: Any) -> dict:
        action = fn(table, **kwargs)
        if isinstance(action, dict):
            audit.record(table, action)
        return action

    return wrapped


@dataclass(frozen=True)
class GateThresholds:
    max_ep_vpip: float = 0.22
    max_ep_trash_raises: int = 0
    min_bb_per_100_rock: float = -25.0
    min_bb_per_100_maniac: float = -40.0
    min_vpip: float = 0.0
    min_pfr: float = 0.06  # rock selfplay floor; live S2 ~11% PFR (K118 gate vs 2.2% passive)
    max_vpip_pfr_gap: float = 0.06
    min_match_win_rate: float = 0.0
    min_match_win_rate_maniac: float = 0.0
    min_match_win_rate_lag: float = 0.0
    gate_bb_maniac: bool = False  # advisory by default (negatively correlated w/ match-win)


def _rate(num: int, den: int) -> float:
    return num / den if den else 0.0


def _series_or_hand_mwr(run: dict) -> Optional[float]:
    if run.get("match_hands") and run.get("match_win_rate") is not None:
        return float(run["match_win_rate"])
    return run.get("hand_match_win_rate") or run.get("match_win_rate")


def _run_profile(
    raw_decide: Any,
    *,
    label: str,
    hands: int,
    players: int,
    seed: Optional[int],
    match_hands: Optional[int],
) -> tuple[dict, HeroAudit]:
    audit = HeroAudit()
    decide_fn = _wrap_decide(raw_decide, audit)
    os.environ["TRAINING_OPPONENT_MODE"] = label
    n_matches: Optional[int] = None
    n_hands = hands
    mh = match_hands if players == 2 and match_hands else None
    if mh:
        n_matches = max(1, hands // mh)
        n_hands = mh * n_matches
    stats = run_selfplay(
        decide_fn=decide_fn,
        n_hands=n_hands,
        opponent_label=label,
        n_players=players,
        starting_stack=500,
        small_blind=10,
        big_blind=20,
        seed=seed,
        training_hud=True,
        match_hands=mh,
        n_matches=n_matches,
    )
    return stats, audit


def run_audit(
    *,
    hands: int,
    players: int,
    seed: Optional[int],
    gate: bool,
    thresholds: GateThresholds,
    match_hands: Optional[int] = None,
) -> int:
    decide_path = _EXAMPLES / "cemini_decide.py"
    raw_decide = _load_decide_from_path(str(decide_path))

    hu_mode = players == 2
    profiles = ("rock", "maniac", "lag") if hu_mode else ("rock", "maniac")
    mh = match_hands if hu_mode else None
    if hu_mode and mh is None:
        mh = 80

    runs: dict[str, dict] = {}
    audits: list[HeroAudit] = []
    for i, label in enumerate(profiles):
        s, a = _run_profile(
            raw_decide,
            label=label,
            hands=hands,
            players=players,
            seed=(seed + i) if seed is not None else None,
            match_hands=mh,
        )
        runs[label] = s
        audits.append(a)

    rock = runs["rock"]
    maniac = runs["maniac"]
    lag = runs.get("lag")

    by_pos: Counter = Counter()
    vpip_pos: Counter = Counter()
    trash: list[str] = []
    for a in audits:
        by_pos.update(a.by_position)
        vpip_pos.update(a.vpip_by_position)
        trash.extend(a.trash_hands_opened)

    merged = HeroAudit(
        preflop_seen=sum(a.preflop_seen for a in audits),
        vpip=sum(a.vpip for a in audits),
        pfr=sum(a.pfr for a in audits),
        ep_opportunities=sum(a.ep_opportunities for a in audits),
        ep_trash_raises=sum(a.ep_trash_raises for a in audits),
        by_position=by_pos,
        vpip_by_position=vpip_pos,
        trash_hands_opened=trash,
    )

    vpip_rate = _rate(merged.vpip, merged.preflop_seen)
    pfr_rate = _rate(merged.pfr, merged.preflop_seen)
    vpip_pfr_gap = vpip_rate - pfr_rate
    ep_seen = merged.by_position.get("UTG", 0) + merged.by_position.get("MP", 0)
    ep_vpip = merged.vpip_by_position.get("UTG", 0) + merged.vpip_by_position.get("MP", 0)
    ep_vpip_rate = _rate(ep_vpip, ep_seen)

    sep = "─" * 58
    print(sep)
    profile_label = "rock + maniac + lag" if lag else "rock + maniac"
    print(f"  cemini self-play audit  ({hands} hands × {profile_label}, {players}-max)")
    if mh:
        print(f"  match series: {mh} hands/match  (TrueSkill proxy)")
    print(f"  seed={seed}  training-hud=ON")
    print(sep)
    print(f"  VPIP (all)  : {vpip_rate:.1%}  ({merged.vpip}/{merged.preflop_seen})")
    print(f"  VPIP (EP)   : {ep_vpip_rate:.1%}  ({ep_vpip}/{ep_seen})  ← gate metric")
    print(f"  PFR         : {pfr_rate:.1%}  ({merged.pfr}/{merged.preflop_seen})")
    print(f"  VPIP − PFR  : {vpip_pfr_gap:.1%}  ← passive-limp gate")
    print(f"  EP trash opens: {merged.ep_trash_raises}  {merged.trash_hands_opened[:5]}")
    print(f"  bb/100 rock : {rock['bb_per_100']:+.1f}")
    print(f"  bb/100 maniac: {maniac['bb_per_100']:+.1f}  (advisory — not gated)")
    if lag:
        print(f"  bb/100 lag   : {lag['bb_per_100']:+.1f}  (advisory)")
    if players == 2:
        for label, run in runs.items():
            hw = run.get("hand_match_win_rate")
            if hw is not None:
                w, l = run["wins"], run["losses"]
                print(f"  hand_win_rate ({label}): {hw:.1%}  ({w}/{w + l})")
            swr = _series_or_hand_mwr(run)
            if swr is not None and run.get("match_hands"):
                mw, ml = run.get("match_wins", 0), run.get("match_losses", 0)
                print(
                    f"  series_win_rate ({label}): {swr:.1%}  "
                    f"({mw}/{mw + ml} matches, {run.get('match_hands')}h)"
                )
    print("  VPIP by seat:")
    for pos in ("UTG", "MP", "CO", "BTN", "SB", "BB"):
        seen = merged.by_position.get(pos, 0)
        vp = merged.vpip_by_position.get(pos, 0)
        if seen:
            print(f"    {pos:3s}  {_rate(vp, seen):.1%}  ({vp}/{seen})")
    print(sep)

    failures: list[str] = []
    if ep_vpip_rate > thresholds.max_ep_vpip:
        failures.append(
            f"EP VPIP {ep_vpip_rate:.1%} > max {thresholds.max_ep_vpip:.1%}"
        )
    if merged.ep_trash_raises > thresholds.max_ep_trash_raises:
        failures.append(
            f"EP trash opens {merged.ep_trash_raises} > {thresholds.max_ep_trash_raises}"
        )
    if rock["bb_per_100"] < thresholds.min_bb_per_100_rock:
        failures.append(
            f"bb/100 vs rock {rock['bb_per_100']:+.1f} < {thresholds.min_bb_per_100_rock:+.1f}"
        )
    if thresholds.gate_bb_maniac and maniac["bb_per_100"] < thresholds.min_bb_per_100_maniac:
        failures.append(
            f"bb/100 vs maniac {maniac['bb_per_100']:+.1f} < "
            f"{thresholds.min_bb_per_100_maniac:+.1f}"
        )
    if thresholds.min_vpip > 0 and vpip_rate < thresholds.min_vpip:
        failures.append(
            f"VPIP {vpip_rate:.1%} < min {thresholds.min_vpip:.1%}"
        )
    if thresholds.min_pfr > 0 and pfr_rate < thresholds.min_pfr:
        failures.append(
            f"PFR {pfr_rate:.1%} < min {thresholds.min_pfr:.1%}"
        )
    if thresholds.max_vpip_pfr_gap > 0 and vpip_pfr_gap > thresholds.max_vpip_pfr_gap:
        failures.append(
            f"VPIP−PFR gap {vpip_pfr_gap:.1%} > max {thresholds.max_vpip_pfr_gap:.1%}"
        )
    if players == 2 and thresholds.min_match_win_rate > 0:
        mwr = _series_or_hand_mwr(rock)
        if mwr is None or mwr < thresholds.min_match_win_rate:
            shown = f"{mwr:.1%}" if mwr is not None else "n/a"
            failures.append(
                f"series_win_rate vs rock {shown} < "
                f"{thresholds.min_match_win_rate:.1%}"
            )
    if players == 2 and thresholds.min_match_win_rate_maniac > 0:
        mwr = _series_or_hand_mwr(maniac)
        if mwr is None or mwr < thresholds.min_match_win_rate_maniac:
            shown = f"{mwr:.1%}" if mwr is not None else "n/a"
            failures.append(
                f"series_win_rate vs maniac {shown} < "
                f"{thresholds.min_match_win_rate_maniac:.1%}"
            )
    if players == 2 and lag and thresholds.min_match_win_rate_lag > 0:
        mwr = _series_or_hand_mwr(lag)
        if mwr is None or mwr < thresholds.min_match_win_rate_lag:
            shown = f"{mwr:.1%}" if mwr is not None else "n/a"
            failures.append(
                f"series_win_rate vs lag {shown} < "
                f"{thresholds.min_match_win_rate_lag:.1%}"
            )

    if failures:
        print("  GATE FAIL:")
        for f in failures:
            print(f"    • {f}")
        if gate:
            return 1
    elif gate:
        print("  GATE PASS")
    else:
        print("  (report only — pass `--gate` to enforce thresholds on deploy)")

    return 0


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Cemini self-play KPI audit")
    p.add_argument("--hands", type=int, default=400, help="Hands per opponent profile")
    p.add_argument("--players", type=int, default=6)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gate", action="store_true", help="Exit 1 if KPI thresholds fail")
    p.add_argument("--max-ep-vpip", type=float, default=GateThresholds.max_ep_vpip)
    p.add_argument("--min-bb-rock", type=float, default=GateThresholds.min_bb_per_100_rock)
    p.add_argument("--min-bb-maniac", type=float, default=GateThresholds.min_bb_per_100_maniac)
    p.add_argument("--min-pfr", type=float, default=None,
                   help="Min PFR rate (default 0.12 HU / 0.06 6-max)")
    p.add_argument("--max-vpip-pfr-gap", type=float, default=None,
                   help="Max VPIP−PFR gap (default 0.10 HU / 0.06 6-max)")
    p.add_argument("--min-match-win-rate", type=float,
                   default=GateThresholds.min_match_win_rate,
                   help="HU only: min win rate vs rock; 0 disables")
    p.add_argument("--min-match-win-maniac", type=float,
                   default=GateThresholds.min_match_win_rate_maniac,
                   help="HU only: min win rate vs maniac; 0 disables")
    p.add_argument("--min-match-win-lag", type=float,
                   default=GateThresholds.min_match_win_rate_lag,
                   help="HU only: min series win rate vs lag; 0 disables")
    p.add_argument("--match-hands", type=int, default=None,
                   help="HU: hands per TrueSkill-style match series (default 80)")
    p.add_argument("--gate-bb-maniac", action="store_true",
                   help="Gate on bb/100 vs maniac (default off — advisory)")
    args = p.parse_args(argv)

    hu_mode = (
        args.players == 2
        or os.environ.get("CEMINI_TABLE_FORMAT", "").strip().lower() in (
            "hu", "heads-up", "headsup", "2max", "2-max",
        )
    )
    min_pfr = args.min_pfr if args.min_pfr is not None else (
        0.12 if hu_mode else GateThresholds.min_pfr
    )
    max_vpip_pfr_gap = (
        args.max_vpip_pfr_gap if args.max_vpip_pfr_gap is not None else (
            0.10 if hu_mode else GateThresholds.max_vpip_pfr_gap
        )
    )

    min_vpip = 0.18 if os.environ.get("CEMINI_GIN_STYLE", "").strip().lower() in (
        "1", "true", "yes", "on",
    ) else 0.0
    match_hands = args.match_hands
    if hu_mode and match_hands is None:
        match_hands = 80
    min_match_rock = args.min_match_win_rate
    if hu_mode and args.gate and min_match_rock == 0:
        min_match_rock = 0.55
    th = GateThresholds(
        max_ep_vpip=args.max_ep_vpip,
        min_bb_per_100_rock=args.min_bb_rock,
        min_bb_per_100_maniac=args.min_bb_maniac,
        min_vpip=min_vpip,
        min_pfr=min_pfr,
        max_vpip_pfr_gap=max_vpip_pfr_gap,
        min_match_win_rate=min_match_rock,
        min_match_win_rate_maniac=args.min_match_win_maniac,
        min_match_win_rate_lag=args.min_match_win_lag,
        gate_bb_maniac=args.gate_bb_maniac,
    )
    return run_audit(
        hands=args.hands,
        players=args.players,
        seed=args.seed,
        gate=args.gate,
        thresholds=th,
        match_hands=match_hands,
    )


if __name__ == "__main__":
    sys.exit(main())
