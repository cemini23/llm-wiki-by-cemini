"""Solver provenance stamping and guarded diff for equilibrium baselines.

K136 P0 — Nash-solver provenance vocabulary and cross-profile diff guards.
Implements arXiv 2606.28308 solver-family selection semantics:
- Charts/baselines from different solver families are NOT directly comparable
  without explicit disclosure of Nash-polytope asymmetry.
- Profiles with known non-singleton Nash sets (nash_set_singleton=False)
  require disclosure even within the same family (cross-member ambiguity).

All functions are pure (no side effects) except CLI file writes (--apply).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


SOLVER_FAMILIES = frozenset({
    "cfr",            # vanilla counterfactual regret minimization (time average)
    "cfr_plus",       # CFR+ (time average, regret-matching+)
    "fictitious_play",# FP (time average)
    "rnad",           # R-NaD / regularized last-iterate (max-entropy member)
    "ped",            # projected exploitability descent (last iterate)
    "fp_ped",         # FP burn-in -> PED refinement hybrid
    "exploitability_descent",  # ED (tabular, last iterate)
    "mafp",           # K124 multi-agent fictitious play (stance FP in chart space)
    "static_chart",   # hand-authored / heuristic chart (no solver)
    "unknown",        # provenance not recorded
})

EQUILIBRIUM_SELECTION = frozenset({
    "time_average", "last_iterate", "max_entropy", "heuristic", "unknown",
})

PROVENANCE_SCHEMA = "solver-provenance-v1"


class SolverProvenanceError(Exception):
    """Raised when diffing profiles with incompatible solver provenance."""
    pass


def normalize_family(name: str | None) -> str:
    """Normalize solver family name to canonical vocabulary.

    Maps common aliases:
        "cfr+" -> "cfr_plus"
        "r-nad", "rnad" -> "rnad"
        "fp" -> "fictitious_play"
        "", None -> "unknown"

    Returns "unknown" for any token not in SOLVER_FAMILIES.
    """
    if name is None:
        return "unknown"
    token = name.lower().strip()
    if token in ("", "unknown"):
        return "unknown"
    # Aliases
    if token in ("cfr+", "cfr-plus"):
        return "cfr_plus"
    if token in ("r-nad", "rnad"):
        return "rnad"
    if token == "fp":
        return "fictitious_play"
    if token == "ed":
        return "exploitability_descent"
    if token in SOLVER_FAMILIES:
        return token
    return "unknown"


def solver_provenance(
    family: str,
    *,
    version: str = "1",
    equilibrium_selection: str = "unknown",
    nash_set_singleton: bool | None = None,
    notes: str = "",
) -> dict[str, Any]:
    """Build a provenance block for stamping onto chart/baseline JSON.

    Args:
        family: Solver family (normalized via normalize_family)
        version: Solver version string
        equilibrium_selection: One of EQUILIBRIUM_SELECTION
        nash_set_singleton: True/False/None (None = not analyzed)
        notes: Human-readable context

    Returns:
        Dict with schema, normalized family, stamped_at UTC ISO, and fields above.

    Raises:
        ValueError: If equilibrium_selection not in EQUILIBRIUM_SELECTION.
    """
    if equilibrium_selection not in EQUILIBRIUM_SELECTION:
        raise ValueError(
            f"Invalid equilibrium_selection '{equilibrium_selection}'. "
            f"Must be one of: {EQUILIBRIUM_SELECTION}"
        )
    return {
        "schema": PROVENANCE_SCHEMA,
        "solver_family": normalize_family(family),
        "solver_version": str(version),
        "equilibrium_selection": equilibrium_selection,
        "nash_set_singleton": nash_set_singleton,
        "stamped_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "notes": notes,
    }


def stamp_chart_provenance(payload: dict[str, Any], provenance: dict[str, Any]) -> dict[str, Any]:
    """Return a shallow copy of payload with solver_provenance key set.

    Does NOT mutate the input payload (deep copy of top-level dict only).
    """
    out = dict(payload)
    out["solver_provenance"] = deepcopy(provenance)
    return out


def read_chart_provenance(payload: dict[str, Any] | None) -> dict[str, Any] | None:
    """Return payload.get('solver_provenance') or None.

    Never raises; safe for pre-K136 payloads without the key.
    """
    if payload is None:
        return None
    return payload.get("solver_provenance")


def read_chart_file_provenance(path: str | Path) -> dict[str, Any] | None:
    """Load JSON file and return its provenance block (or None if absent/unparseable)."""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return None
    return read_chart_provenance(data)


def family_of(payload_or_prov: dict[str, Any] | None) -> str:
    """Extract normalized solver family from a payload or provenance dict directly.

    Returns "unknown" if absent or input is None.
    """
    if payload_or_prov is None:
        return "unknown"
    # If it's a provenance block directly
    if "solver_family" in payload_or_prov:
        return normalize_family(payload_or_prov.get("solver_family"))
    # If it's a payload with solver_provenance nested
    prov = payload_or_prov.get("solver_provenance")
    if prov is None:
        return "unknown"
    return normalize_family(prov.get("solver_family"))


def same_family(a: dict[str, Any] | None, b: dict[str, Any] | None) -> bool:
    """True if family_of(a) == family_of(b) AND both != "unknown"."""
    fa = family_of(a)
    fb = family_of(b)
    if fa == "unknown" or fb == "unknown":
        return False
    return fa == fb


def provenance_fingerprint(provenance: dict[str, Any]) -> str:
    """SHA256 hash of core provenance fields (family, version, selection, singleton).

    Used for change detection / cache invalidation.
    """
    core = {
        "family": provenance.get("solver_family"),
        "version": provenance.get("solver_version"),
        "equilibrium_selection": provenance.get("equilibrium_selection"),
        "nash_set_singleton": provenance.get("nash_set_singleton"),
    }
    payload = json.dumps(core, sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()


def assert_diffable(
    prov_a: dict[str, Any] | None,
    prov_b: dict[str, Any] | None,
    *,
    disclose: bool = False,
) -> dict[str, Any]:
    """Guard: raise SolverProvenanceError if profiles are not safely diffable.

    Logic (fail-closed):
    1. If disclose=True, always returns a disclosure record (no raise).
    2. If same_family is False (different families or any side unknown), raises.
    3. If either side has nash_set_singleton=False (known non-singleton) and
       disclose=False, raises (cross-member ambiguity within same family).

    Returns:
        Disclosure record dict with:
        - diffable: True (caller may proceed)
        - same_family: bool
        - disclosed: bool (whether disclose flag was used to bypass)
        - family_a, family_b: str
        - nash_set_singleton_a, nash_set_singleton_b: bool|None
        - reason: str

    Raises:
        SolverProvenanceError: If guard conditions fail and disclose=False.
    """
    fa = family_of(prov_a)
    fb = family_of(prov_b)
    sf = same_family(prov_a, prov_b)

    def singleton_flag(p: dict[str, Any] | None) -> bool | None:
        if p is None:
            return None
        # Handle both provenance block and payload-with-nested-provenance
        prov = p.get("solver_provenance") if "solver_provenance" in p else p
        if prov is None:
            return None
        return prov.get("nash_set_singleton")

    sa = singleton_flag(prov_a)
    sb = singleton_flag(prov_b)

    # Build reasons
    reasons: list[str] = []
    if not sf:
        reasons.append(f"cross-family: {fa} vs {fb}")
    if sa is False:
        reasons.append("side_a known non-singleton")
    if sb is False:
        reasons.append("side_b known non-singleton")

    record: dict[str, Any] = {
        "diffable": True,
        "same_family": sf,
        "disclosed": disclose,
        "family_a": fa,
        "family_b": fb,
        "nash_set_singleton_a": sa,
        "nash_set_singleton_b": sb,
        "reason": "; ".join(reasons) if reasons else "same family, singleton status ok",
    }

    if disclose:
        return record

    if not sf:
        raise SolverProvenanceError(
            f"Cannot diff charts from different solver families ({fa} vs {fb}) without --disclose"
        )
    if sa is False or sb is False:
        raise SolverProvenanceError(
            f"Cannot diff charts with known non-singleton Nash set without --disclose "
            f"(a={sa}, b={sb})"
        )
    return record


def diff_charts(
    payload_a: dict[str, Any],
    payload_b: dict[str, Any],
    *,
    disclose: bool = False,
) -> dict[str, Any]:
    """Guarded diff of two chart payloads.

    Steps:
    1. assert_diffable(read_chart_provenance(a), read_chart_provenance(b), disclose=disclose)
    2. Diff the 'ranges' dicts per-position {hand: action}:
       - Hands in A not B -> removed
       - Hands in B not A -> added
       - Action mismatch -> changed

    Returns:
        {"disclosure": <record>, "added": [...], "removed": [...],
         "changed": [{position, hand, from, to}], "n_changed": int}
    """
    prov_a = read_chart_provenance(payload_a)
    prov_b = read_chart_provenance(payload_b)
    disclosure = assert_diffable(prov_a, prov_b, disclose=disclose)

    ranges_a = payload_a.get("ranges") if isinstance(payload_a.get("ranges"), dict) else {}
    ranges_b = payload_b.get("ranges") if isinstance(payload_b.get("ranges"), dict) else {}

    added: list[dict[str, str]] = []
    removed: list[dict[str, str]] = []
    changed: list[dict[str, str]] = []

    all_positions = set(ranges_a.keys()) | set(ranges_b.keys())

    for pos in all_positions:
        hands_a = ranges_a.get(pos, {})
        hands_b = ranges_b.get(pos, {})
        all_hands = set(hands_a.keys()) | set(hands_b.keys())

        for hand in all_hands:
            action_a = hands_a.get(hand)
            action_b = hands_b.get(hand)
            if action_a is None and action_b is not None:
                added.append({"position": pos, "hand": hand, "to": action_b})
            elif action_a is not None and action_b is None:
                removed.append({"position": pos, "hand": hand, "from": action_a})
            elif action_a is not None and action_b is not None and action_a != action_b:
                changed.append({"position": pos, "hand": hand, "from": action_a, "to": action_b})

    return {
        "disclosure": disclosure,
        "added": added,
        "removed": removed,
        "changed": changed,
        "n_changed": len(changed),
    }


def _cli_print(args: argparse.Namespace) -> int:
    """Print provenance block from a chart file (or 'unknown' if absent)."""
    path = Path(args.file)
    prov = read_chart_file_provenance(path)
    if prov is None:
        print("unknown")
    else:
        print(json.dumps(prov, indent=2))
    return 0


def _cli_stamp(args: argparse.Namespace) -> int:
    """Stamp provenance onto a chart file (--apply to rewrite)."""
    path = Path(args.file)
    singleton_val: bool | None = None
    if args.singleton is not None:
        if args.singleton.lower() in ("true", "1", "yes"):
            singleton_val = True
        elif args.singleton.lower() in ("false", "0", "no"):
            singleton_val = False
        # else remain None

    prov = solver_provenance(
        family=args.family,
        version=args.version,
        equilibrium_selection=args.selection,
        nash_set_singleton=singleton_val,
        notes=args.notes or "",
    )

    # Show the would-be stamped provenance
    print(json.dumps(prov, indent=2))

    if not args.apply:
        print("\n(Dry-run: use --apply to rewrite file atomically)")
        return 0

    # Read existing payload, stamp, atomic write
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        return 1

    new_payload = stamp_chart_provenance(payload, prov)
    tmp = path.with_suffix(path.suffix + ".tmp")
    try:
        tmp.write_text(json.dumps(new_payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        Path(tmp).replace(path)
        print(f"\nStamped -> {path}")
    except Exception as e:
        print(f"Error writing {path}: {e}", file=sys.stderr)
        return 1
    return 0


def _cli_diff(args: argparse.Namespace) -> int:
    """Guarded diff of two chart files."""
    path_a = Path(args.file_a)
    path_b = Path(args.file_b)

    try:
        payload_a = json.loads(path_a.read_text(encoding="utf-8"))
        payload_b = json.loads(path_b.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading files: {e}", file=sys.stderr)
        return 1

    disclose_flag: bool = bool(getattr(args, "disclose", False))

    try:
        result = diff_charts(payload_a, payload_b, disclose=disclose_flag)
    except SolverProvenanceError as e:
        print(f"SolverProvenanceError: {e}", file=sys.stderr)
        return 3

    print(json.dumps(result, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Solver provenance CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    # Print command
    p_print = sub.add_parser("print", help="Print provenance from a chart JSON")
    p_print.add_argument("file", help="Path to chart JSON")

    # Stamp command
    p_stamp = sub.add_parser("stamp", help="Stamp provenance onto a chart JSON")
    p_stamp.add_argument("file", help="Path to chart JSON")
    p_stamp.add_argument("--family", required=True, help="Solver family")
    p_stamp.add_argument("--version", default="1", help="Solver version")
    p_stamp.add_argument("--selection", default="unknown", help="Equilibrium selection")
    p_stamp.add_argument("--singleton", default=None, help="Nash set singleton (true/false/unknown)")
    p_stamp.add_argument("--notes", default="", help="Notes")
    p_stamp.add_argument("--apply", action="store_true", help="Apply the stamp (rewrite file)")

    # Diff command
    p_diff = sub.add_parser("diff", help="Diff two chart JSONs with provenance guard")
    p_diff.add_argument("file_a", help="First chart JSON")
    p_diff.add_argument("file_b", help="Second chart JSON")
    p_diff.add_argument("--disclose", action="store_true", help="Allow cross-family diff with disclosure")

    args = p.parse_args(argv)

    if args.cmd == "print":
        return _cli_print(args)
    if args.cmd == "stamp":
        return _cli_stamp(args)
    if args.cmd == "diff":
        return _cli_diff(args)

    return 1


if __name__ == "__main__":
    sys.exit(main())
