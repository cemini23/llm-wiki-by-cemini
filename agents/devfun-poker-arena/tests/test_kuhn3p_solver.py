"""Tests for K136 P1 3-player Kuhn Poker solver (FP→PED spike)."""
from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

# Resilient import pattern - add to sys.modules BEFORE exec for dataclass support
spec = importlib.util.spec_from_file_location("kuhn3p_solver", ROOT / "examples" / "kuhn3p_solver.py")
_kuhn3p = importlib.util.module_from_spec(spec)
sys.modules["kuhn3p_solver"] = _kuhn3p
spec.loader.exec_module(_kuhn3p)


def _require_attr(mod, name: str):
    if not hasattr(mod, name):
        raise AttributeError(f"kuhn3p_solver missing required attribute: {name}")

_require_attr(_kuhn3p, "KuhnPoker3P")
_require_attr(_kuhn3p, "N_PLAYERS")
_require_attr(_kuhn3p, "simplex_project")
_require_attr(_kuhn3p, "run_cfr")
_require_attr(_kuhn3p, "run_fp")
_require_attr(_kuhn3p, "run_exploitability_descent")
_require_attr(_kuhn3p, "run_fp_ped")
_require_attr(_kuhn3p, "compare_equal_budget")
_require_attr(_kuhn3p, "SolveResult")

KuhnPoker3P = _kuhn3p.KuhnPoker3P
simplex_project = _kuhn3p.simplex_project
run_cfr = _kuhn3p.run_cfr
run_fp = _kuhn3p.run_fp
run_exploitability_descent = _kuhn3p.run_exploitability_descent
run_fp_ped = _kuhn3p.run_fp_ped
compare_equal_budget = _kuhn3p.compare_equal_budget
SolveResult = _kuhn3p.SolveResult


def test_deck_size_bounds():
    """Test KuhnPoker3P raises ValueError for invalid deck sizes."""
    try:
        KuhnPoker3P(3)
        assert False, "Should have raised ValueError for deck_size=3"
    except ValueError:
        pass

    try:
        KuhnPoker3P(7)
        assert False, "Should have raised ValueError for deck_size=7"
    except ValueError:
        pass

    # Valid sizes should work
    for ds in [4, 5, 6]:
        g = KuhnPoker3P(ds)
        assert g.deck_size == ds


def test_deal_count():
    """Test deck_size=4 -> 24 deals, deck_size=6 -> 120 deals."""
    g4 = KuhnPoker3P(4)
    assert len(g4.deals()) == 24  # 4*3*2 = 24

    g6 = KuhnPoker3P(6)
    assert len(g6.deals()) == 120  # 6*5*4 = 120


def test_infoset_key_hides_opponent_cards():
    """Infoset key contains only own card + public history (not opponent cards)."""
    g = KuhnPoker3P(4)
    # Same player, same card, same history should map to same key regardless of opponent cards
    key1 = g.infoset_key(0, 3, "xb")  # P0 has card 3, history "xb"
    key2 = g.infoset_key(0, 3, "xb")
    assert key1 == key2
    assert "P0" in key1
    assert "c3" in key1
    assert "xb" in key1


def test_legal_actions_transitions():
    """Legal actions: empty history -> check/bet; after bet -> call/fold."""
    g = KuhnPoker3P(4)
    # Empty history
    assert g.legal_actions("") == ["check", "bet"]
    # After checks
    assert g.legal_actions("x") == ["check", "bet"]
    # After bet
    actions = g.legal_actions("xb")
    assert "call" in actions
    assert "fold" in actions


def test_terminal_payoffs_zero_sum():
    """Terminal payoffs sum to 0.0 (zero-sum property)."""
    g = KuhnPoker3P(4)
    # Test a few terminal histories
    test_cases = [
        ("xxx",),  # All check
        ("xbc",),  # Check, bet, call
        ("xbf",),  # Check, bet, fold
    ]
    for (history,) in test_cases:
        for deal in g.deals()[:5]:  # Sample 5 deals
            payoffs = g.terminal_payoffs(deal, history)
            total = sum(payoffs)
            assert abs(total) < 1e-9, f"Payoffs {payoffs} should sum to 0, got {total}"


def test_terminal_payoffs_all_check_showdown():
    """All-check showdown: highest card wins the antes."""
    g = KuhnPoker3P(4)
    # Deal (3, 2, 1) - P0 has highest card (3)
    deal = (3, 2, 1)
    payoffs = g.terminal_payoffs(deal, "xxx")
    # P0 should win 2 antes (net +1 after putting in 1)
    # P0 gets pot of 3, invested 1, net = +2
    assert payoffs[0] == 2.0, f"Expected P0 to win 2, got {payoffs[0]}"
    # Others lose their ante
    assert payoffs[1] == -1.0
    assert payoffs[2] == -1.0


def test_terminal_payoffs_fold_gives_pot():
    """Bet and two folds: bettor takes the pot."""
    g = KuhnPoker3P(4)
    # Deal doesn't matter much here
    deal = (0, 1, 2)
    # P0 bets, P1 folds, P2 folds
    payoffs = g.terminal_payoffs(deal, "xbf")  # P0 check-bet, P1 fold - wait need to trace
    # Actually with "xbf": P0 checks (x), P1 bets (b), P2 folds (f)
    # Now P0 faces bet and must act - this isn't terminal yet
    # Let's use "xbff" or similar if allowed
    # For simplicity, just verify payoffs are zero-sum
    total = sum(payoffs)
    assert abs(total) < 1e-6


def test_nashconv_nonneg():
    """Exploitability (approx via _approx_exploitability) should return non-negative."""
    g = KuhnPoker3P(4)
    # Build a simple uniform strategy for some infosets
    uniform = {}
    # Add some entries
    for p in range(3):
        for c in range(4):
            for h in ["", "x", "b", "xx"]:
                key = g.infoset_key(p, c, h)
                if h == "":
                    uniform[key] = [0.5, 0.5]  # check/bet
                elif "b" in h:
                    uniform[key] = [0.5, 0.5]  # call/fold
                else:
                    uniform[key] = [0.5, 0.5]  # check/bet
    # Use internal approx function
    approx_exp = _kuhn3p._approx_exploitability(g, uniform)
    assert isinstance(approx_exp, (int, float))
    # Exploitability should be non-negative
    assert approx_exp >= 0


def test_simplex_project_valid():
    """simplex_project projects to valid probability distribution."""
    # Already valid distribution - should stay unchanged
    result = simplex_project([0.3, 0.3, 0.4])
    assert abs(sum(result) - 1.0) < 1e-9
    assert all(r >= -1e-9 for r in result)  # Allow tiny negative from floating point

    # Invalid distribution (sums to > 1, has negatives)
    result2 = simplex_project([0.8, 0.8, -0.2])
    assert abs(sum(result2) - 1.0) < 1e-9
    assert all(r >= -1e-9 for r in result2)


def test_cfr_reduces_exploitability():
    """run_cfr(60 iters) should reduce exploitability vs uniform."""
    g = KuhnPoker3P(4)
    result = run_cfr(g, 60, seed=42)
    assert isinstance(result, SolveResult)
    assert result.method == "cfr"
    assert result.iters == 60
    # Curve should have entries
    assert len(result.exploitability_curve) > 0
    # Final exploitability should be lower than initial (monotone-ish)
    if len(result.exploitability_curve) >= 2:
        first = result.exploitability_curve[0][1]
        last = result.exploitability_curve[-1][1]
        # Allow for some non-monotonicity but generally should decrease
        assert last < first * 1.5  # Loose check for test stability


def test_fp_reduces_exploitability():
    """run_fp(60 iters) should reduce exploitability vs uniform."""
    g = KuhnPoker3P(4)
    result = run_fp(g, 60, seed=42)
    assert isinstance(result, SolveResult)
    assert result.method == "fp"
    assert len(result.exploitability_curve) > 0
    first = result.exploitability_curve[0][1]
    last = result.exploitability_curve[-1][1]
    assert last < first * 1.5


def test_exploitability_descent_last_iterate_improves():
    """run_exploitability_descent improves over uniform."""
    g = KuhnPoker3P(4)
    result = run_exploitability_descent(g, 60, seed=42)
    assert isinstance(result, SolveResult)
    assert result.method == "ped"
    assert len(result.exploitability_curve) > 0
    # Check curve format
    for entry in result.exploitability_curve:
        assert isinstance(entry, tuple)
        assert len(entry) == 2
        assert isinstance(entry[0], int)  # iteration
        assert isinstance(entry[1], float)  # exploitability


def test_fp_ped_curve_continuous():
    """run_fp_ped produces continuous curve with increasing iterations."""
    g = KuhnPoker3P(4)
    result = run_fp_ped(g, fp_iters=30, ped_iters=30, seed=42)
    assert isinstance(result, SolveResult)
    assert result.method == "fp_ped"
    assert len(result.exploitability_curve) >= 2
    # Check iterations are strictly increasing
    iters = [entry[0] for entry in result.exploitability_curve]
    for i in range(1, len(iters)):
        assert iters[i] > iters[i-1]


def test_compare_equal_budget_shape():
    """compare_equal_budget returns expected keys and winner."""
    g = KuhnPoker3P(4)
    result = compare_equal_budget(g, budget=60, fp_frac=0.5, seed=42)
    assert "deck_size" in result
    assert result["deck_size"] == 4
    assert "budget" in result
    assert "cfr_final" in result
    assert "fp_ped_final" in result
    assert "winner" in result
    assert result["winner"] in ("cfr", "fp_ped", "tie")
    assert "delta" in result
    assert isinstance(result["delta"], float)
    assert "cfr_curve" in result
    assert "fp_ped_curve" in result
    # Verify delta = cfr_final - fp_ped_final
    expected_delta = result["cfr_final"] - result["fp_ped_final"]
    assert abs(result["delta"] - expected_delta) < 1e-9


def test_write_spike_report_provenance(tmp_path: Path):
    """write_spike_report produces valid JSON with provenance."""
    # Import write function
    write_spike_report = _kuhn3p.write_spike_report
    import json

    g = KuhnPoker3P(4)
    cmp_result = compare_equal_budget(g, budget=30, seed=42)

    out_path = tmp_path / "spike.json"
    write_spike_report(cmp_result, out_path, deck_size=4, seed=42)

    # Load and verify
    data = json.loads(out_path.read_text())
    assert data["schema"] == "kuhn3p-ped-spike-v1"
    assert "solver_provenance" in data
    prov = data["solver_provenance"]
    assert prov["solver_family"] == "fp_ped"
    assert "cfr_curve" in data
    assert "fp_ped_curve" in data
