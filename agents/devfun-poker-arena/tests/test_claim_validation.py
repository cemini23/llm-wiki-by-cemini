"""K259 — claim validation + NL->tool arg grounding (fail-open)."""
from __future__ import annotations

import sys
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent.parent / "examples"
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))

from claim_validation import (  # noqa: E402
    ARG_SCHEMA,
    CLAIM_SCHEMA,
    MEMBERSHIP_SCHEMA,
    ground_tool_args,
    membership_match,
    normalize_action,
    tag_solver_context_claims,
    validate_directional_claim,
)


# --- membership vs claim validation ---


def test_membership_match_catalog_hit():
    result = membership_match("raise-1.5x", {"raise-1.5x", "call-1.0x"})
    assert result["schema"] == MEMBERSHIP_SCHEMA
    assert result["membership"] == "match"


def test_membership_match_no_hit():
    result = membership_match("junk-line", {"raise-1.5x", "call-1.0x"})
    assert result["membership"] == "no_match"


def test_membership_match_fail_open():
    assert membership_match(None, {"x"})["membership"] == "unknown"
    assert membership_match("x", None)["membership"] == "unknown"
    assert membership_match("", {"x"})["membership"] == "unknown"


def test_membership_match_dict_line():
    result = membership_match({"report_id": "mafp-flop"}, {"mafp-flop"})
    assert result["membership"] == "match"


def test_validate_matching_direction():
    result = validate_directional_claim(
        {"action": "raise"}, {"dominant_action": "raise"}
    )
    assert result["claim_status"] == "validated"
    assert result["repeat_ok"] is True
    assert result["direction"] == "raise"


def test_validate_conflicting_direction():
    result = validate_directional_claim(
        {"action": "raise"}, {"suggested_action": "fold"}
    )
    assert result["claim_status"] == "conflict"
    assert result["repeat_ok"] is False


def test_validate_no_independent_evidence():
    result = validate_directional_claim({"action": "raise"}, {})
    assert result["claim_status"] == "unvalidated"
    assert result["repeat_ok"] is False


def test_validate_no_claim_skipped():
    result = validate_directional_claim({}, {"dominant_action": "raise"})
    assert result["claim_status"] == "skipped"
    assert result["repeat_ok"] is False


def test_validate_fail_open_bad_input():
    for bad in (None, "raise", 5):
        result = validate_directional_claim(bad, {"action": "raise"})
        assert result["claim_status"] == "skipped"
        assert result["repeat_ok"] is False


def test_validate_membership_match_on_known_shape():
    result = validate_directional_claim({"action": "call"}, {"action": "call"})
    assert result["membership"] == "match"


def test_normalize_action_aliases():
    assert normalize_action("pf_raise") is None  # not an action token
    assert normalize_action("3-bet") == "raise"
    assert normalize_action("x") == "check"
    assert normalize_action(["call", "raise"]) == "mixed"
    assert normalize_action("") is None
    assert normalize_action(None) is None


# --- arg grounding ---


def test_ground_street_aliases():
    result = ground_tool_args({"street": "pf"})
    assert result["street"] == "preflop"
    assert result["action"] == "accept"
    assert result["ok"] is True
    assert result["ambiguous"] == []


def test_ground_ambiguous_street_refuses():
    result = ground_tool_args({"street": "f"})
    assert result["street"] is None
    assert result["action"] == "clarify"
    assert "street" in result["ambiguous"]
    # No silent default invented.
    assert result["street"] is None


def test_ground_unknown_street_refuses():
    result = ground_tool_args({"street": "turnriver"})
    assert result["street"] is None
    assert result["action"] == "refuse"


def test_ground_numeric_seat():
    result = ground_tool_args({"seat": "seat 3"})
    assert result["seat"] == 3
    assert result["action"] == "accept"
    assert result["ok"] is True


def test_ground_seat_label_needs_layout():
    result = ground_tool_args({"seat": "btn"})
    assert result["seat"] is None
    assert result["seat_label"] == "button"
    assert result["action"] == "clarify"
    assert "seat" in result["ambiguous"]


def test_ground_unknown_seat_refuses():
    result = ground_tool_args({"seat": "under-the-gun-plus-one-million"})
    assert result["seat"] is None
    assert result["action"] == "refuse"


def test_ground_solver_alias():
    result = ground_tool_args({"solver_id": "mafp"})
    assert result["solver_id"] == "mafp"
    assert result["action"] == "accept"


def test_ground_unknown_solver_refuses():
    result = ground_tool_args({"solver_id": "quantum-solver"})
    assert result["solver_id"] is None
    assert result["action"] == "refuse"


def test_ground_empty_args_accept():
    result = ground_tool_args({})
    assert result["action"] == "accept"
    assert result["ok"] is True
    assert result["ambiguous"] == []


def test_ground_fail_open_bad_input():
    result = ground_tool_args(None)
    assert result["action"] == "refuse"
    assert result["schema"] == ARG_SCHEMA


def test_ground_mixed_refuse_wins():
    result = ground_tool_args({"street": "pf", "seat": "quantum-seat"})
    assert result["street"] == "preflop"
    assert result["action"] == "refuse"
    assert "seat" not in result["ambiguous"]  # unknown, not just ambiguous


# --- advisory tag for solver context ---


def test_tag_validated_against_independent_evidence():
    ctx = {
        "preflop_chart": {"suggested_action": "raise"},
        "solver_frequencies": {"dominant_action": "raise"},
    }
    tagged = tag_solver_context_claims(ctx)
    assert "claim_validation" in tagged
    assert tagged["claim_validation"]["claim_status"] == "validated"
    assert tagged["claim_validation"]["repeat_ok"] is True
    assert tagged["claim_validation"]["claim_source"] == "preflop_chart"
    assert tagged["claim_validation"]["evidence_source"] == "solver_frequencies"


def test_tag_unvalidated_when_no_independent_evidence():
    ctx = {"preflop_chart": {"suggested_action": "raise"}}
    tagged = tag_solver_context_claims(ctx)
    assert tagged["claim_validation"]["claim_status"] == "unvalidated"
    assert tagged["claim_validation"]["repeat_ok"] is False


def test_tag_membership_only():
    ctx = {"pokerskill": {"scenario": "open_defend"}}
    tagged = tag_solver_context_claims(ctx)
    assert tagged["claim_validation"]["membership"] == "match"
    assert tagged["claim_validation"]["claim_status"] == "unvalidated"
    assert tagged["claim_validation"]["repeat_ok"] is False


def test_tag_arg_grounding_when_tool_args_present():
    ctx = {"preflop_chart": {"suggested_action": "raise"}, "tool_args": {"seat": "btn"}}
    tagged = tag_solver_context_claims(ctx)
    assert "arg_grounding" in tagged
    assert tagged["arg_grounding"]["action"] == "clarify"


def test_tag_fail_open():
    assert tag_solver_context_claims(None) is None
    assert tag_solver_context_claims({}) == {}
    assert tag_solver_context_claims("nope") == "nope"
    assert tag_solver_context_claims({"something_unrelated": 1}) == {"something_unrelated": 1}


def test_docs_mention_k259():
    refs = Path(__file__).resolve().parent.parent / "references"
    doc = (refs / "mcp-claim-validation.md").read_text(encoding="utf-8")
    assert "K259" in doc
    assert "CASCADE" in doc
    assert "claim_validation" in doc
    assert doc  # non-empty
