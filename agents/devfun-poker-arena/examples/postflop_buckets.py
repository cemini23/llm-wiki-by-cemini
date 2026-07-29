"""HU postflop bucket frequency table — O(1) lookup for solver bake v1.

Schema key: ``{street}|{role}|{texture}|{strength_bin}``
  street ∈ flop, turn, river
  role ∈ ip, oop
  texture ∈ dry, wet, paired
  strength_bin ∈ air, weak, medium, strong, nuts

Values: bet/check/call/fold/raise frequencies + size_pot_frac.

Runtime: pure dict lookup, fail-open, bundle-aware path resolution.
Generation: equity-vs-pot-odds heuristics (heuristic_bucket_v1) — not a
tabular solver export.
"""
from __future__ import annotations

import json
import os
import secrets
from pathlib import Path
from typing import Any, Optional

STREETS = ("flop", "turn", "river")
ROLES = ("ip", "oop")
TEXTURES = ("dry", "wet", "paired")
STRENGTH_BINS = ("air", "weak", "medium", "strong", "nuts")

# Equity thresholds for strength bins (left-open intervals except air).
_STRENGTH_CUTS = (
    ("air", 0.0, 0.35),
    ("weak", 0.35, 0.50),
    ("medium", 0.50, 0.65),
    ("strong", 0.65, 0.85),
    ("nuts", 0.85, 1.01),
)

_FREQ_KEYS = ("bet", "check", "call", "fold", "raise")

_bucket_cache: Optional[dict[str, Any]] = None
_bucket_cache_key: Optional[tuple[Optional[str], Optional[float]]] = None


def _env_truthy(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in ("1", "true", "yes", "on")


def postflop_buckets_enabled() -> bool:
    return _env_truthy("CEMINI_POSTFLOP_BUCKETS")


def deepcfr_enabled() -> bool:
    """Prefer DeepCFR-lite bake when flag on (still requires POSTFLOP_BUCKETS)."""
    return _env_truthy("CEMINI_DEEPCFR")


def solver_hard_enabled() -> bool:
    """When on, sample actions from bake freqs instead of soft equity-bar bias."""
    return _env_truthy("CEMINI_SOLVER_HARD")


def spr_bin(effective_stack: float, pot: float) -> str:
    """Coarse SPR bucket for denser v2 keys (backward-compatible helper)."""
    pot_f = max(float(pot), 1e-9)
    spr = max(0.0, float(effective_stack) / pot_f)
    if spr < 3.5:
        return "spr2"
    if spr < 7.5:
        return "spr5"
    if spr < 15.0:
        return "spr10"
    return "spr20"


def sample_action_from_freqs(
    freqs: dict[str, float],
    *,
    facing_bet: bool,
    available: list[str],
    rng: Any,
) -> Optional[tuple[str, Optional[float]]]:
    """Sample a legal action from bake freqs. Returns (action, size_pot_frac) or None.

    Free spot uses bet/check mass; facing uses fold/call/raise. Illegal actions
    are dropped and the remainder re-normalized. Empty support → None (fail-open).
    """
    if not freqs or not available:
        return None
    avail = {str(a).lower() for a in available}
    size = float(freqs.get("size_pot_frac", 0.5) or 0.5)
    size = max(0.25, min(1.0, size))

    if facing_bet:
        # Map raise→raise/bet/all-in preference
        cand = {
            "fold": float(freqs.get("fold", 0.0) or 0.0),
            "call": float(freqs.get("call", 0.0) or 0.0),
            "raise": float(freqs.get("raise", 0.0) or 0.0),
        }
        weights: list[tuple[str, float]] = []
        for action, w in cand.items():
            if w <= 0:
                continue
            if action == "fold" and "fold" in avail:
                weights.append(("fold", w))
            elif action == "call" and "call" in avail:
                weights.append(("call", w))
            elif action == "raise":
                if "raise" in avail:
                    weights.append(("raise", w))
                elif "bet" in avail:
                    weights.append(("bet", w))
                elif "all-in" in avail:
                    weights.append(("all-in", w))
                elif "allin" in avail:
                    weights.append(("allin", w))
    else:
        cand = {
            "bet": float(freqs.get("bet", 0.0) or 0.0),
            "check": float(freqs.get("check", 0.0) or 0.0),
        }
        weights = []
        for action, w in cand.items():
            if w <= 0:
                continue
            if action == "check" and "check" in avail:
                weights.append(("check", w))
            elif action == "bet":
                if "bet" in avail:
                    weights.append(("bet", w))
                elif "raise" in avail:
                    weights.append(("raise", w))
                elif "all-in" in avail:
                    weights.append(("all-in", w))
                elif "allin" in avail:
                    weights.append(("allin", w))

    if not weights:
        return None
    total = sum(w for _, w in weights)
    if total <= 1e-12:
        return None
    pick = float(rng.random()) * total
    acc = 0.0
    chosen = weights[-1][0]
    for action, w in weights:
        acc += w
        if pick <= acc:
            chosen = action
            break
    if chosen in ("check", "fold", "call"):
        return chosen, None
    return chosen, size


def strength_bin(equity: float) -> str:
    """Map equity in [0,1] to strength_bin label."""
    eq = max(0.0, min(1.0, float(equity)))
    for name, lo, hi in _STRENGTH_CUTS:
        if lo <= eq < hi:
            return name
    return "nuts"


def classify_board_texture(board: list[str]) -> str:
    """Classify board as dry / wet / paired (paired takes priority)."""
    if not board or len(board) < 3:
        return "dry"
    ranks = [c[0].upper() for c in board if c]
    suits = [c[-1].lower() for c in board if c]
    if len(ranks) < 3:
        return "dry"

    if len(set(ranks)) < len(ranks):
        return "paired"

    rank_order = "23456789TJQKA"
    idxs = sorted(rank_order.index(r) for r in ranks if r in rank_order)
    monotone = len(set(suits)) == 1
    two_tone = len(set(suits)) == 2 and max(suits.count(s) for s in set(suits)) >= 2
    connected = (max(idxs) - min(idxs)) <= 4 if len(idxs) >= 2 else False
    if monotone or (two_tone and connected) or (connected and len(idxs) >= 3):
        return "wet"
    return "dry"


def bucket_key(street: str, role: str, texture: str, strength: str) -> str:
    return f"{street}|{role}|{texture}|{strength}"


def resolve_deepcfr_buckets_path() -> Optional[Path]:
    """Bundle-aware DeepCFR-lite path: env → assets/research → repo research."""
    override = os.environ.get("CEMINI_DEEPCFR_PATH", "").strip()
    if override:
        return Path(override)

    module_dir = Path(__file__).resolve().parent
    candidates = (
        module_dir / "research" / "deepcfr_hu_buckets.json",
        module_dir.parent / "assets" / "research" / "deepcfr_hu_buckets.json",
        module_dir.parent / "research" / "deepcfr_hu_buckets.json",
    )
    for p in candidates:
        if p.is_file():
            return p
    return None


def resolve_postflop_buckets_path() -> Optional[Path]:
    """Bundle-aware path: DeepCFR (if flagged) → env → assets/research → repo."""
    if deepcfr_enabled():
        deep = resolve_deepcfr_buckets_path()
        if deep is not None:
            return deep

    override = os.environ.get("CEMINI_POSTFLOP_BUCKETS_PATH", "").strip()
    if override:
        return Path(override)

    module_dir = Path(__file__).resolve().parent
    candidates = (
        module_dir / "research" / "postflop_hu_buckets.json",
        module_dir.parent / "assets" / "research" / "postflop_hu_buckets.json",
        module_dir.parent / "research" / "postflop_hu_buckets.json",
    )
    for p in candidates:
        if p.is_file():
            return p
    return None


def _normalize_freqs(raw: dict[str, Any]) -> dict[str, float]:
    """Normalize action freqs; preserve size_pot_frac separately."""
    size = float(raw.get("size_pot_frac", 0.5) or 0.5)
    size = max(0.25, min(1.0, size))
    vals = {k: max(0.0, float(raw.get(k, 0.0) or 0.0)) for k in _FREQ_KEYS}
    total = sum(vals.values())
    if total <= 0:
        # Neutral free-spot default
        vals = {"bet": 0.35, "check": 0.35, "call": 0.15, "fold": 0.10, "raise": 0.05}
        total = 1.0
    out = {k: vals[k] / total for k in _FREQ_KEYS}
    out["size_pot_frac"] = size
    return out


def load_postflop_buckets(path: Optional[Path] = None) -> Optional[dict[str, Any]]:
    """Load bucket table. Fail-open → None."""
    p = path if path is not None else resolve_postflop_buckets_path()
    if p is None or not Path(p).is_file():
        return None
    try:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception:
        return None
    if not isinstance(data, dict):
        return None
    buckets = data.get("buckets")
    if not isinstance(buckets, dict) or not buckets:
        return None
    return data


def _reset_bucket_cache() -> None:
    global _bucket_cache, _bucket_cache_key
    _bucket_cache = None
    _bucket_cache_key = None


def get_buckets_payload() -> Optional[dict[str, Any]]:
    """Cached full payload (or None)."""
    global _bucket_cache, _bucket_cache_key
    if not postflop_buckets_enabled():
        return None

    path = resolve_postflop_buckets_path()
    path_str: Optional[str] = None
    mtime: Optional[float] = None
    if path is not None:
        try:
            path_str = str(path.resolve())
            if path.is_file():
                mtime = path.stat().st_mtime
        except OSError:
            path_str = str(path)

    key = (path_str, mtime)
    if _bucket_cache is not None and _bucket_cache_key == key:
        return _bucket_cache

    data = load_postflop_buckets(path)
    _bucket_cache = data
    _bucket_cache_key = key
    return data


def lookup_freqs(
    street: str,
    role: str,
    texture: str,
    strength: str,
    *,
    payload: Optional[dict[str, Any]] = None,
) -> Optional[dict[str, float]]:
    """O(1) frequency lookup. Returns None if missing/disabled."""
    data = payload if payload is not None else get_buckets_payload()
    if not data:
        return None
    buckets = data.get("buckets") or {}
    st = street.lower().strip()
    if st not in STREETS:
        return None
    role_l = role.lower().strip()
    if role_l not in ROLES:
        return None
    tex = texture.lower().strip()
    if tex not in TEXTURES:
        return None
    strength_l = strength.lower().strip()
    if strength_l not in STRENGTH_BINS:
        strength_l = strength_bin(0.5)

    key = bucket_key(st, role_l, tex, strength_l)
    raw = buckets.get(key)
    if not isinstance(raw, dict):
        return None
    return _normalize_freqs(raw)


def lookup_slice(
    street: str,
    role: str,
    texture: str,
    *,
    payload: Optional[dict[str, Any]] = None,
) -> Optional[dict[str, dict[str, float]]]:
    """Return all strength bins for a (street, role, texture) triple."""
    data = payload if payload is not None else get_buckets_payload()
    if not data:
        return None
    out: dict[str, dict[str, float]] = {}
    for sbin in STRENGTH_BINS:
        freqs = lookup_freqs(street, role, texture, sbin, payload=data)
        if freqs:
            out[sbin] = freqs
    return out or None


def resolve_bias_generator(generator: Optional[str] = None) -> str:
    """Resolve bias provenance: explicit arg → env → loaded bucket meta.

    Returns ``texas_solver_v1`` when solver-strength scale should apply,
    otherwise a non-solver token (heuristic path / unchanged clamps).
    """
    if generator:
        return str(generator).strip()
    env = os.environ.get("CEMINI_POSTFLOP_BIAS_SCALE", "").strip().lower()
    if env in ("deepcfr", "deepcfr_lite_v1"):
        return "deepcfr_lite_v1"
    if env in ("texas_solver_v2",):
        return "texas_solver_v2"
    if env in ("solver", "texas_solver_v1", "strong", "1", "true", "yes", "on"):
        return "texas_solver_v1"
    if env in ("0", "off", "heuristic", "heuristic_bucket_v1", "false", "no"):
        return "heuristic_bucket_v1"
    # Inspect loaded table when buckets are enabled (hot path).
    if postflop_buckets_enabled():
        data = get_buckets_payload()
        if data:
            gen = (data.get("meta") or {}).get("generator")
            if gen:
                return str(gen)
    return "heuristic_bucket_v1"


def bias_scale_params(generator: Optional[str] = None) -> dict[str, float]:
    """Clamp + multipliers for bias_thresholds_from_freqs.

    Heuristic bake: clamp ±0.08, free mult 0.10, facing 0.12/0.10/0.15.
    texas_solver_v1 / v2 / deepcfr_lite_v1: Phase-1 solver scale — clamp ±0.14,
    free 0.15, facing 0.18/0.15/0.225 (Phase-2 ±0.16 stack rolled back).
    """
    gen = resolve_bias_generator(generator)
    if gen in ("texas_solver_v1", "texas_solver_v2", "deepcfr_lite_v1"):
        return {
            "clamp": 0.14,
            "free_mult": 0.15,
            "fold_mult": 0.18,
            "call_mult": 0.15,
            "raise_mult": 0.225,
        }
    return {
        "clamp": 0.08,
        "free_mult": 0.10,
        "fold_mult": 0.12,
        "call_mult": 0.10,
        "raise_mult": 0.15,
    }


def bias_thresholds_from_freqs(
    freqs: dict[str, float],
    *,
    facing_bet: bool = False,
    generator: Optional[str] = None,
) -> dict[str, float]:
    """Bounded threshold deltas from bucket frequencies.

    Free spot: higher bet freq → lower bet_bar; higher check → higher bet_bar.
    Facing: higher fold → more fold_slack; higher call → lower call_margin;
    higher raise → lower raise_bar.

    Clamp defaults ±0.08 (heuristic). When loaded meta generator is
    ``texas_solver_v1`` / ``deepcfr_lite_v1`` (or env solver scale), clamp
    ±0.14 and free_mult 0.15 / facing 0.18·0.15·0.225. Flag-off path
    never calls this with live freqs.
    """
    params = bias_scale_params(generator)
    lo = -float(params["clamp"])
    hi = float(params["clamp"])

    def clamp(x: float) -> float:
        return max(lo, min(hi, x))

    if facing_bet:
        fold_f = float(freqs.get("fold", 0.0))
        call_f = float(freqs.get("call", 0.0))
        raise_f = float(freqs.get("raise", 0.0))
        # More fold weight → fold easier (increase fold_slack)
        fold_slack_delta = clamp((fold_f - 0.35) * float(params["fold_mult"]))
        call_margin_delta = clamp((0.40 - call_f) * float(params["call_mult"]))
        raise_bar_delta = clamp((0.15 - raise_f) * float(params["raise_mult"]))
        return {
            "fold_slack_delta": fold_slack_delta,
            "call_margin_delta": call_margin_delta,
            "raise_bar_delta": raise_bar_delta,
            "size_pot_frac": float(freqs.get("size_pot_frac", 0.5)),
        }

    bet_f = float(freqs.get("bet", 0.0))
    check_f = float(freqs.get("check", 0.0))
    # More bet → lower bar (easier bet); more check → higher bar
    bet_bar_delta = clamp((check_f - bet_f) * float(params["free_mult"]))
    return {
        "bet_bar_delta": bet_bar_delta,
        "size_pot_frac": float(freqs.get("size_pot_frac", 0.5)),
    }


def build_solver_frequencies_context(
    table: dict,
    *,
    in_position: Optional[bool] = None,
) -> Optional[dict[str, Any]]:
    """Context fragment for retrieve_solver_context (no equity yet).

    Carries (street, role, texture) + by_strength slice; decide() picks
    strength_bin from already-computed equity.
    """
    if not postflop_buckets_enabled():
        return None
    street = (table.get("street") or "Preflop").lower()
    if street == "preflop":
        return None
    if street not in STREETS:
        # Map Arena street labels
        board = list(table.get("boardCards") or [])
        n = len(board)
        if n >= 5:
            street = "river"
        elif n == 4:
            street = "turn"
        elif n >= 3:
            street = "flop"
        else:
            return None

    board = list(table.get("boardCards") or [])
    texture = classify_board_texture(board)
    if in_position is None:
        try:
            from position_utils import hero_is_in_position

            in_position = hero_is_in_position(table)
        except Exception:
            in_position = False
    role = "ip" if in_position else "oop"

    by_strength = lookup_slice(street, role, texture)
    if not by_strength:
        return None

    return {
        "bucket_prefix": f"{street}|{role}|{texture}",
        "street": street,
        "role": role,
        "texture": texture,
        "by_strength": by_strength,
        "source": (
            "deepcfr_hu_buckets_v1"
            if deepcfr_enabled() and resolve_deepcfr_buckets_path() is not None
            else "postflop_hu_buckets_v1"
        ),
    }


def resolve_freqs_for_equity(
    solver_frequencies: Optional[dict[str, Any]],
    equity: float,
) -> Optional[dict[str, float]]:
    """Pick strength bin from equity and return freqs from context slice."""
    if not solver_frequencies:
        return None
    sbin = strength_bin(equity)
    by_s = solver_frequencies.get("by_strength") or {}
    raw = by_s.get(sbin)
    if isinstance(raw, dict):
        return _normalize_freqs(raw)
    # Fallback: full key lookup
    st = solver_frequencies.get("street")
    role = solver_frequencies.get("role")
    tex = solver_frequencies.get("texture")
    if st and role and tex:
        return lookup_freqs(st, role, tex, sbin)
    return None


# ---------------------------------------------------------------------------
# Offline generation (heuristic_bucket_v1)
# ---------------------------------------------------------------------------

def _heuristic_freqs(
    street: str,
    role: str,
    texture: str,
    strength: str,
) -> dict[str, float]:
    """Derive frequencies from equity-vs-pot-odds heuristics + HU tendencies."""
    # Base free-spot (check/bet) and facing (fold/call/raise) priors by strength
    free = {
        "air": (0.18, 0.82),
        "weak": (0.28, 0.72),
        "medium": (0.48, 0.52),
        "strong": (0.72, 0.28),
        "nuts": (0.88, 0.12),
    }
    face = {
        # fold, call, raise
        "air": (0.72, 0.22, 0.06),
        "weak": (0.48, 0.42, 0.10),
        "medium": (0.22, 0.58, 0.20),
        "strong": (0.08, 0.52, 0.40),
        "nuts": (0.02, 0.38, 0.60),
    }
    bet, check = free[strength]
    fold, call, raise_f = face[strength]

    # IP stabs more on dry flops
    if role == "ip" and street == "flop" and texture == "dry":
        if strength in ("air", "weak", "medium"):
            bet = min(0.92, bet + 0.12)
            check = 1.0 - bet
    # OOP fewer river bluffs
    if role == "oop" and street == "river" and strength in ("air", "weak"):
        bet = max(0.05, bet - 0.12)
        check = 1.0 - bet
        fold = min(0.90, fold + 0.08)
        call = max(0.05, call - 0.05)
    # Wet boards: smaller bluff, more pot control medium
    if texture == "wet" and strength in ("medium", "weak"):
        bet = max(0.10, bet - 0.08)
        check = 1.0 - bet
    # Paired: more checks medium, fewer thin value raises
    if texture == "paired" and strength == "medium":
        bet = max(0.15, bet - 0.10)
        check = 1.0 - bet
        raise_f = max(0.05, raise_f - 0.08)
        call = min(0.80, call + 0.05)

    # Sizing
    size_map = {
        ("dry", "flop"): 0.33,
        ("dry", "turn"): 0.50,
        ("dry", "river"): 0.66,
        ("wet", "flop"): 0.66,
        ("wet", "turn"): 0.75,
        ("wet", "river"): 0.75,
        ("paired", "flop"): 0.40,
        ("paired", "turn"): 0.55,
        ("paired", "river"): 0.66,
    }
    size = size_map.get((texture, street), 0.50)
    if strength in ("strong", "nuts"):
        size = min(1.0, size + 0.08)
    if strength == "air" and role == "ip":
        size = max(0.25, size - 0.05)

    # Pack as single distribution (free + facing actions share the vector)
    raw = {
        "bet": bet * 0.5,
        "check": check * 0.5,
        "call": call * 0.35,
        "fold": fold * 0.35,
        "raise": raise_f * 0.30,
        "size_pot_frac": size,
    }
    return _normalize_freqs(raw)


def generate_bucket_table() -> dict[str, Any]:
    """Build full ~90-key bucket table with provenance."""
    buckets: dict[str, dict[str, float]] = {}
    for street in STREETS:
        for role in ROLES:
            for texture in TEXTURES:
                for strength in STRENGTH_BINS:
                    key = bucket_key(street, role, texture, strength)
                    buckets[key] = _heuristic_freqs(street, role, texture, strength)

    payload: dict[str, Any] = {
        "schema": "postflop-hu-buckets-v1",
        "source": "examples/postflop_buckets.py",
        "meta": {
            "generator": "heuristic_bucket_v1",
            "key_count": len(buckets),
            "streets": list(STREETS),
            "roles": list(ROLES),
            "textures": list(TEXTURES),
            "strength_bins": list(STRENGTH_BINS),
        },
        "buckets": buckets,
    }

    try:
        from solver_provenance import solver_provenance, stamp_chart_provenance

        prov = solver_provenance(
            "static_chart",
            version="1",
            equilibrium_selection="heuristic",
            nash_set_singleton=None,
            notes=(
                "heuristic_bucket_v1: derived from mafp-informed equity "
                "heuristics; not a tabular solver export"
            ),
        )
        payload = stamp_chart_provenance(payload, prov)
    except Exception:
        payload["solver_provenance"] = {
            "solver_family": "static_chart",
            "notes": "heuristic_bucket_v1: derived from mafp-informed equity heuristics",
        }
    return payload


def write_postflop_buckets(
    path: Optional[Path] = None,
    *,
    force_heuristic: bool = False,
) -> Path:
    """Atomic write of **heuristic** bucket JSON.

    Refuses to overwrite an existing ``texas_solver_v1`` / ``v2`` file unless
    ``force_heuristic=True`` (CLI: ``--force-heuristic``).
    """
    root = Path(__file__).resolve().parent.parent
    out = Path(path) if path is not None else root / "research" / "postflop_hu_buckets.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.is_file() and not force_heuristic:
        try:
            existing = json.loads(out.read_text(encoding="utf-8"))
            gen = (existing.get("meta") or {}).get("generator")
            if gen in ("texas_solver_v1", "texas_solver_v2"):
                raise SystemExit(
                    f"refusing to overwrite {gen} at {out}; "
                    "pass --force-heuristic to regenerate heuristic_bucket_v1"
                )
        except SystemExit:
            raise
        except Exception:
            pass
    payload = generate_bucket_table()
    tmp = out.with_suffix(out.suffix + f".tmp.{secrets.token_hex(4)}")
    try:
        tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(tmp, out)
    finally:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass
    return out


def _self_check(path: Path) -> int:
    data = load_postflop_buckets(path)
    assert data is not None, "load failed"
    buckets = data["buckets"]
    n = len(buckets)
    assert 50 <= n <= 100, f"key count {n} not in 50–100"
    gen = (data.get("meta") or {}).get("generator")
    # Accept either heuristic self-check or solver bake
    assert gen in (
        "heuristic_bucket_v1",
        "texas_solver_v1",
        "texas_solver_v2",
    ), f"bad generator {gen}"
    # Classifier smoke
    assert classify_board_texture(["Ah", "7d", "2c"]) == "dry"
    assert classify_board_texture(["Ah", "Kh", "Qh"]) == "wet"
    assert classify_board_texture(["Ah", "Ad", "7c"]) == "paired"
    assert strength_bin(0.20) == "air"
    assert strength_bin(0.40) == "weak"
    assert strength_bin(0.55) == "medium"
    assert strength_bin(0.70) == "strong"
    assert strength_bin(0.90) == "nuts"
    print(f"postflop_hu_buckets OK: {n} keys generator={gen} @ {path}")
    return 0


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Generate heuristic postflop HU buckets")
    ap.add_argument(
        "--force-heuristic",
        action="store_true",
        help="Overwrite existing texas_solver_v1 bake with heuristic_bucket_v1",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path (default research/postflop_hu_buckets.json)",
    )
    ns = ap.parse_args()
    out = write_postflop_buckets(ns.out, force_heuristic=ns.force_heuristic)
    raise SystemExit(_self_check(out))
