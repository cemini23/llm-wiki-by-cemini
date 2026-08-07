"""K226/K257 — anytime-valid eval stop metadata (fail-open advisory).

Records why an agent comparison stopped and whether the online value
model could have peeked at the current hand. Method only — no
TrajDebug / AV-AIVAT / PTC runtime install.
"""
from __future__ import annotations

from typing import Any

SCHEMA = "devfun.eval_stop_metadata.v1"

STOP_METADATA_KEYS = (
    "n_hands",
    "estimator",
    "bound_halfwidth_bb",
    "stopped",
    "reason",
    "paired_log_path",
    "value_model_excludes_current_hand",
)


def record_stop_decision(
    *,
    n_hands: Any = None,
    estimator: Any = None,
    bound_halfwidth_bb: Any = None,
    stopped: Any = None,
    reason: Any = None,
    paired_log_path: Any = None,
    value_model_excludes_current_hand: Any = None,
) -> dict:
    """Return a stop-metadata dict with every schema key present.

    Fail-open: never raises; missing/None values coerce to neutral
    defaults so downstream rechecks always see the full schema.
    """
    return {
        "schema": SCHEMA,
        "n_hands": n_hands if n_hands is not None else 0,
        "estimator": estimator if estimator is not None else "",
        "bound_halfwidth_bb": bound_halfwidth_bb,
        "stopped": bool(stopped),
        "reason": reason if reason is not None else "",
        "paired_log_path": paired_log_path if paired_log_path is not None else "",
        "value_model_excludes_current_hand": bool(
            value_model_excludes_current_hand
        ),
    }


def assert_no_current_hand_peek(
    value_model_hands: Any, current_hand_id: Any
) -> bool:
    """True when current_hand_id is absent from the value-model hand set.

    Fail-open: an empty/None training set counts as "no peek" (nothing to
    peek at). A non-iterable set returns False — the guard cannot verify,
    so it fails closed on the check itself.
    """
    if not value_model_hands:
        return True
    try:
        return current_hand_id not in value_model_hands
    except TypeError:
        return False
