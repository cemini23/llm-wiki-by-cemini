#!/usr/bin/env python3
"""K130 Track B: RLCard baseline ablation.

Runs RLCard Leduc or limit-HU environments for N episodes, computes Monte Carlo equity
using treys, logs action frequencies and simple VPIP proxies, and outputs results.
"""
from __future__ import annotations

import argparse
import json
import os
import random
from pathlib import Path
from typing import Any

import rlcard
from rlcard.agents import RandomAgent
from rlcard.utils import set_seed

try:
    from treys import Card, Deck, Evaluator
    HAS_TREYS = True
except ImportError:
    HAS_TREYS = False


def parse_rlcard_card(card_str: str) -> str:
    """Parse card_str from RLCard (e.g. 'HQ', '9S', 'Ah') and return standard Treys-compatible format ('Qh', '9s')."""
    if not card_str or len(card_str) != 2:
        return "2c"
    
    ranks = '23456789TJQKA'
    suits = 'SHDC'
    
    c1, c2 = card_str[0].upper(), card_str[1].upper()
    
    if c1 in ranks and c2 in suits:
        # e.g., '9S' -> '9s'
        return c1 + c2.lower()
    elif c1 in suits and c2 in ranks:
        # e.g., 'HQ' -> 'Qh'
        return c2 + c1.lower()
    else:
        return card_str.lower()


def compute_mc_equity(hole_cards_str: list[str], board_cards_str: list[str], num_simulations: int = 150) -> float:
    """Compute Monte Carlo equity of hole_cards_str given board_cards_str using treys."""
    if not HAS_TREYS:
        return 0.5
        
    try:
        evaluator = Evaluator()
        
        # Convert to Treys Card objects
        hole_cards = [Card.new(c) for c in hole_cards_str if c]
        board_cards = [Card.new(c) for c in board_cards_str if c]
        
        # We need a 5-card board and 2-card hole hands for Treys Evaluator.
        # If we have fewer than 2 hole cards, let's pad them with random cards from the deck.
        dead_cards = set(hole_cards) | set(board_cards)
        
        wins = 0
        splits = 0
        total = 0
        
        for _ in range(num_simulations):
            deck = Deck()
            deck.cards = [c for c in deck.cards if c not in dead_cards]
            
            sim_hole = list(hole_cards)
            while len(sim_hole) < 2:
                sim_hole.append(deck.draw(1)[0])
                
            opp_hole = deck.draw(2)
            
            sim_board = list(board_cards)
            while len(sim_board) < 5:
                sim_board.append(deck.draw(1)[0])
                
            hero_score = evaluator.evaluate(sim_board, sim_hole)
            opp_score = evaluator.evaluate(sim_board, opp_hole)
            
            if hero_score < opp_score:
                wins += 1
            elif hero_score == opp_score:
                splits += 1
            total += 1
            
        if total == 0:
            return 0.5
        return (wins + 0.5 * splits) / total
    except Exception:
        return 0.5


def get_cards_from_state(state: dict[str, Any]) -> tuple[list[str], list[str]]:
    """Extract hole cards and community board cards from an RLCard state dict."""
    raw_obs = state.get('raw_obs', {})
    hand_raw = raw_obs.get('hand')
    
    hole_cards = []
    if isinstance(hand_raw, list):
        hole_cards = [parse_rlcard_card(c) for c in hand_raw]
    elif isinstance(hand_raw, str):
        hole_cards = [parse_rlcard_card(hand_raw)]
        
    board_cards = []
    pub_card = raw_obs.get('public_card')
    if pub_card:
        if isinstance(pub_card, list):
            board_cards = [parse_rlcard_card(c) for c in pub_card]
        elif isinstance(pub_card, str):
            board_cards = [parse_rlcard_card(pub_card)]
            
    pub_cards = raw_obs.get('public_cards')
    if pub_cards:
        if isinstance(pub_cards, list):
            board_cards.extend([parse_rlcard_card(c) for c in pub_cards])
        elif isinstance(pub_cards, str):
            board_cards.append(parse_rlcard_card(pub_cards))
            
    # Deduplicate while preserving order
    seen = set()
    board_cards = [x for x in board_cards if not (x in seen or seen.add(x))]
    
    return hole_cards, board_cards


def get_action_string(state: dict[str, Any], action_id: int) -> str:
    """Map action ID to its corresponding string representation using the state legal actions list."""
    legal_actions_ids = list(state.get('legal_actions', {}).keys())
    raw_legal_actions = state.get('raw_legal_actions', [])
    if action_id in legal_actions_ids and len(raw_legal_actions) == len(legal_actions_ids):
        idx = legal_actions_ids.index(action_id)
        return raw_legal_actions[idx]
    
    mapping = {0: 'call', 1: 'raise', 2: 'fold', 3: 'check'}
    return mapping.get(action_id, str(action_id))


def main() -> None:
    parser = argparse.ArgumentParser(description="RLCard offline baseline ablation")
    parser.add_argument("--episodes", type=int, default=50, help="Number of episodes to run")
    parser.add_argument("--env", type=str, default="leduc-holdem", choices=["leduc-holdem", "limit-holdem"], help="RLCard environment ID")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()
    
    # 1. Create output directory
    reports_dir = Path("reports/rlcard-ablation")
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    log_file_path = reports_dir / "ablation_log.jsonl"
    summary_file_path = reports_dir / "summary.json"
    
    # Clear prior logs
    if log_file_path.exists():
        log_file_path.unlink()
        
    print(f"[arena-pokerkit] Initializing environment {args.env} with seed {args.seed}...")
    set_seed(args.seed)
    random.seed(args.seed)
    
    env = rlcard.make(
        args.env,
        config={
            'seed': args.seed,
            'allow_raw_data': True,
            'record_action': True,
        }
    )
    
    # Set random agents
    agents = [RandomAgent(num_actions=env.num_actions) for _ in range(env.num_players)]
    env.set_agents(agents)
    
    # Track statistics
    overall_action_counts: dict[str, int] = {'call': 0, 'raise': 0, 'fold': 0, 'check': 0}
    btn_equity_bins: dict[str, dict[str, int]] = {
        'high': {'call': 0, 'raise': 0, 'fold': 0, 'check': 0, 'total': 0},
        'med': {'call': 0, 'raise': 0, 'fold': 0, 'check': 0, 'total': 0},
        'low': {'call': 0, 'raise': 0, 'fold': 0, 'check': 0, 'total': 0}
    }
    
    total_voluntary_actions = 0
    total_actions = 0
    btn_first_action_count = 0
    btn_vpip_count = 0
    
    print(f"[arena-pokerkit] Simulating {args.episodes} episodes...")
    
    with open(log_file_path, "w", encoding="utf-8") as f_log:
        for episode in range(1, args.episodes + 1):
            trajectories, payoffs = env.run(is_training=False)
            
            # Find Player 0's first transition (pre-flop / pre-flop-like BTN first action)
            btn_first_action = "none"
            btn_mc_equity = 0.5
            btn_hole_cards: list[str] = []
            
            p0_transitions = trajectories[0] if trajectories and len(trajectories) > 0 else []
            if len(p0_transitions) >= 2:
                # First transition: state is at 0, action_id is at 1
                state = p0_transitions[0]
                action_id = p0_transitions[1]
                
                btn_hole_cards, btn_board_cards = get_cards_from_state(state)
                btn_mc_equity = compute_mc_equity(btn_hole_cards, btn_board_cards, num_simulations=100)
                btn_first_action = get_action_string(state, action_id)
                
                btn_first_action_count += 1
                if btn_first_action in ['raise', 'call']:
                    btn_vpip_count += 1
                    
                # Bin the action by MC equity
                if btn_mc_equity >= 0.6:
                    eq_bin = 'high'
                elif btn_mc_equity >= 0.4:
                    eq_bin = 'med'
                else:
                    eq_bin = 'low'
                    
                btn_equity_bins[eq_bin][btn_first_action] = btn_equity_bins[eq_bin].get(btn_first_action, 0) + 1
                btn_equity_bins[eq_bin]['total'] += 1
                
            # Count overall action frequencies across all player trajectories
            for player_id, p_transitions in enumerate(trajectories):
                for idx in range(0, len(p_transitions) - 1, 2):
                    state = p_transitions[idx]
                    action_id = p_transitions[idx + 1]
                    act_str = get_action_string(state, action_id)
                    
                    if act_str in overall_action_counts:
                        overall_action_counts[act_str] += 1
                    else:
                        overall_action_counts[act_str] = 1
                        
                    total_actions += 1
                    if act_str in ['raise', 'call']:
                        total_voluntary_actions += 1
                        
            # Log single episode record
            record = {
                "episode": episode,
                "btn_hand": btn_hole_cards,
                "btn_first_action": btn_first_action,
                "btn_mc_equity": round(btn_mc_equity, 4),
                "payoff_p0": payoffs[0] if len(payoffs) > 0 else 0.0,
                "payoff_p1": payoffs[1] if len(payoffs) > 1 else 0.0
            }
            f_log.write(json.dumps(record) + "\n")
            
    # Calculate final aggregate metrics
    vpip_proxy = total_voluntary_actions / total_actions if total_actions > 0 else 0.0
    btn_vpip_proxy = btn_vpip_count / btn_first_action_count if btn_first_action_count > 0 else 0.0
    
    action_frequencies = {}
    for act, count in overall_action_counts.items():
        action_frequencies[act] = round(count / total_actions, 4) if total_actions > 0 else 0.0
        
    summary_data = {
        "env_id": args.env,
        "episodes_run": args.episodes,
        "overall_action_counts": overall_action_counts,
        "overall_action_frequencies": action_frequencies,
        "overall_vpip_proxy": round(vpip_proxy, 4),
        "btn_first_action_vpip_proxy": round(btn_vpip_proxy, 4),
        "btn_equity_bins": btn_equity_bins
    }
    
    with open(summary_file_path, "w", encoding="utf-8") as f_sum:
        json.dump(summary_data, f_sum, indent=2)
        
    print("\n[arena-pokerkit] =========================================")
    print("[arena-pokerkit] ABLATION SUMMARY STATISTICS")
    print("[arena-pokerkit] =========================================")
    print(f"Environment:             {args.env}")
    print(f"Episodes:                {args.episodes}")
    print(f"Overall Actions Total:   {total_actions}")
    print(f"Overall VPIP Proxy:      {summary_data['overall_vpip_proxy']:.4f}")
    print(f"BTN First-Action VPIP:   {summary_data['btn_first_action_vpip_proxy']:.4f}")
    print("\nOverall Action Frequencies:")
    for act, freq in action_frequencies.items():
        print(f"  - {act.capitalize():<8}: {freq * 100:.2f}%")
        
    print("\n[arena-pokerkit] BTN Open Frequencies by Monte Carlo Equity (Static Chart Cell Proxy):")
    for eq_bin, stats in btn_equity_bins.items():
        tot = stats['total']
        print(f"  MC Equity [{eq_bin.upper()}]:")
        if tot == 0:
            print("    No occurrences")
            continue
        for act in ['raise', 'call', 'check', 'fold']:
            cnt = stats.get(act, 0)
            pct = (cnt / tot) * 100
            bar = "#" * int(pct // 5)
            print(f"    - {act.capitalize():<8}: {pct:>5.1f}%  {bar}")
            
    print("\n[arena-pokerkit] JSONL logs written to: ", log_file_path)
    print("[arena-pokerkit] Summary JSON written to: ", summary_file_path)
    
    # B3 — Cross-wiki handoff stub
    print("\n[arena-pokerkit] =========================================")
    print("[arena-pokerkit] CROSS-WIKI HANDOFF STUB")
    print("[arena-pokerkit] =========================================")
    print("Primary domain owner: gambling-wiki")
    print("Refer to gambling-wiki rlcard entity: @gambling-wiki/entities/tools/rlcard.md")
    print("Future depth mapping: briefs/2026-06-26_k130-rlcard-offline-baseline-adopt.md")
    print("[arena-pokerkit] =========================================\n")


if __name__ == "__main__":
    main()
