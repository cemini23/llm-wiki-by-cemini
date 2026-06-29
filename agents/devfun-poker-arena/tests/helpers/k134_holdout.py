"""K134 hold-out suite for RQGM ground-truth anchor evaluation.

Golden-labeled spots for evaluator promotion gate.
No PokerKit dependency - uses cemini_tables fixtures only.
"""
from __future__ import annotations

from cemini_tables import (
    hu_sb_unopened,
    hu_bb_vs_minraise,
    hu_btn_vs_shove,
    nuts_quads_facing_bet,
    second_nut_flush_river,
)

# Import FALLBACK_REASONING for generic reasoning fail cases
FALLBACK_REASONING = '{vr: "std", ke: "legal", pp: "pot control"}'


def holdout_suite_v1() -> list[dict]:
    """K134 GT anchor: HU + nuts spots with golden legal/illegal labels.

    Each row: {name, action, allowed_actions, elapsed_s, deadline_s, payload, table, gt_pass}.
    gt_pass = the action+reasoning a competent agent should produce (oracle label).

    Minimum 6 spots covering:
    - legal premium open (gt_pass=True)
    - illegal action (gt_pass=False)
    - generic-reasoning fail (gt_pass=False)
    - bad-amount fail (gt_pass=False)
    - timeout fail (gt_pass=False)
    - nuts value bet legal (gt_pass=True)
    """
    suite = []

    # 1. Legal premium open - AA SB first-in, raise 4x (within range)
    table1 = hu_sb_unopened(["As", "Ah"])
    suite.append({
        "name": "legal_premium_open_aa",
        "action": "raise",
        "allowed_actions": ["fold", "call", "raise"],
        "elapsed_s": 0.5,
        "deadline_s": 10.0,
        "payload": {
            "action": "raise",
            "amount": 4,
            "reasoning_text": "AA SB first-in, premium open 4x",
            "message": "value open",
        },
        "table": table1,
        "gt_pass": True,
    })

    # 2. Illegal action - attempt all-in when not in availableActions
    table2 = hu_sb_unopened(["7s", "2d"])
    suite.append({
        "name": "illegal_action_allin",
        "action": "all-in",
        "allowed_actions": ["fold", "call", "raise"],  # all-in not allowed
        "elapsed_s": 0.3,
        "deadline_s": 10.0,
        "payload": {
            "action": "all-in",
            "reasoning_text": "shove 72o because tilt",
            "message": "tilt shove",
        },
        "table": table2,
        "gt_pass": False,
    })

    # 3. Generic reasoning fail - uses FALLBACK_REASONING
    table3 = hu_sb_unopened(["Kh", "Qd"])
    suite.append({
        "name": "generic_reasoning_fallback",
        "action": "raise",
        "allowed_actions": ["fold", "call", "raise"],
        "elapsed_s": 0.4,
        "deadline_s": 10.0,
        "payload": {
            "action": "raise",
            "amount": 6,
            "reasoning_text": FALLBACK_REASONING,
            "message": "act",
        },
        "table": table3,
        "gt_pass": False,
    })

    # 4. Bad amount fail - raise below minimum raise range
    table4 = hu_bb_vs_minraise(["Js", "Tc"])
    suite.append({
        "name": "bad_amount_below_min",
        "action": "raise",
        "allowed_actions": ["fold", "call", "raise"],
        "elapsed_s": 0.6,
        "deadline_s": 10.0,
        "payload": {
            "action": "raise",
            "amount": 4,  # Below min raise (should be 2x = 12)
            "reasoning_text": "JTs defend with small raise",
            "message": "defend",
        },
        "table": table4,
        "gt_pass": False,
    })

    # 5. Timeout fail - elapsed exceeds deadline
    table5 = hu_btn_vs_shove(["Ac", "Kd"])
    suite.append({
        "name": "timeout_exceeded",
        "action": "call",
        "allowed_actions": ["fold", "call", "all-in"],
        "elapsed_s": 15.0,  # Exceeds 10s hard deadline
        "deadline_s": 10.0,
        "payload": {
            "action": "call",
            "reasoning_text": "AKs call vs shove, equity calc took too long",
            "message": "call",
        },
        "table": table5,
        "gt_pass": False,
    })

    # 6. Nuts value bet legal - quad aces must never fold
    table6 = nuts_quads_facing_bet()
    suite.append({
        "name": "nuts_quads_value_bet",
        "action": "raise",
        "allowed_actions": ["fold", "call", "raise"],
        "elapsed_s": 0.8,
        "deadline_s": 10.0,
        "payload": {
            "action": "raise",
            "amount": 800,
            "reasoning_text": "quad aces nuts, must value raise",
            "message": "nuts value",
        },
        "table": table6,
        "gt_pass": True,
    })

    # 7. Extra: High card on flush board - fold is correct (not nuts)
    table7 = second_nut_flush_river()
    suite.append({
        "name": "second_nut_fold_correct",
        "action": "fold",
        "allowed_actions": ["fold", "call"],
        "elapsed_s": 0.7,
        "deadline_s": 10.0,
        "payload": {
            "action": "fold",
            "reasoning_text": "AK high card on monotone board, fold to bet",
            "message": "fold",
        },
        "table": table7,
        "gt_pass": True,
    })

    return suite
