#!/usr/bin/env python3
"""Polymarket on-chain data harvester — Layer 1 per prediction-market-historical-analysis.

Wraps Dubach (2026) polydata.onchain pipeline. Requires Python >=3.11.
Target: cemini-prod. See briefs/2026-05-09_polymarket-onchain-data-pipeline.md.

Usage:
    python3 scripts/harvest_polymarket_history.py \
        --start-block 50000000 --end-block 52000000 \
        --rpc-url https://polygon-rpc.com \
        --contract-address 0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E \
        --out-dir market-dataset/prediction-markets/polymarket/onchain-trades/

Env vars (fallback): POLYGON_RPC_URL, CTF_EXCHANGE_ADDRESS,
    HARVEST_START_BLOCK, HARVEST_END_BLOCK, SCRAPE_CHUNK, SCRAPE_SLICE_BLOCKS.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Checkpoint helper — idempotent resume
# ---------------------------------------------------------------------------

CHECKPOINT_FILE = "harvest_polymarket_checkpoint.json"


def load_checkpoint(out_dir: Path) -> int | None:
    """Return last completed block, or None if no checkpoint exists."""
    cp = out_dir / CHECKPOINT_FILE
    if cp.exists():
        data = json.loads(cp.read_text())
        return int(data.get("last_block", 0))
    return None


def save_checkpoint(out_dir: Path, block: int) -> None:
    cp = out_dir / CHECKPOINT_FILE
    cp.write_text(json.dumps({
        "last_block": block,
        "updated": datetime.utcnow().isoformat(),
    }))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Polymarket on-chain trade harvester (Dubach polydata.onchain wrapper)"
    )
    parser.add_argument("--start-block", type=int,
                        default=int(os.environ.get("HARVEST_START_BLOCK", "0")))
    parser.add_argument("--end-block", type=int,
                        default=int(os.environ.get("HARVEST_END_BLOCK", "0")))
    parser.add_argument("--rpc-url",
                        default=os.environ.get("POLYGON_RPC_URL", "https://polygon-rpc.com"))
    parser.add_argument("--contract-address",
                        default=os.environ.get("CTF_EXCHANGE_ADDRESS", ""))
    parser.add_argument("--out-dir",
                        default="market-dataset/prediction-markets/polymarket/onchain-trades/")
    parser.add_argument("--chunk", type=int,
                        default=int(os.environ.get("SCRAPE_CHUNK", "200")))
    parser.add_argument("--slice-blocks", type=int,
                        default=int(os.environ.get("SCRAPE_SLICE_BLOCKS", "100000")))
    parser.add_argument("--resume", action="store_true", default=True,
                        help="Resume from last checkpoint (default: True)")
    parser.add_argument("--no-resume", action="store_false", dest="resume",
                        help="Start fresh, ignoring checkpoint")
    args = parser.parse_args()

    if not args.contract_address:
        print("Error: --contract-address or CTF_EXCHANGE_ADDRESS required", file=sys.stderr)
        return 1

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # --- Checkpoint resume ---
    start_block = args.start_block
    if args.resume:
        last = load_checkpoint(out_dir)
        if last and last > start_block:
            print(f"Resuming from checkpoint block {last}")
            start_block = last

    if args.end_block and start_block >= args.end_block:
        print(f"Already caught up: start_block={start_block} >= end_block={args.end_block}")
        return 0

    print(f"Harvesting {args.contract_address} blocks {start_block}..{args.end_block or 'HEAD'}")
    print(f"  RPC: {args.rpc_url}")
    print(f"  Chunk: {args.chunk}, Slice blocks: {args.slice_blocks}")
    print(f"  Output: {out_dir.resolve()}")

    # --- Import polydata (requires Python >=3.11) ---
    try:
        from polydata.onchain.rpc import PolygonRpcClient
        from polydata.onchain.scraper import scrape_slice_finalized
    except ImportError:
        print("Error: polydata package required. Install from:", file=sys.stderr)
        print("  https://github.com/philippdubach/polymarket-microstructure", file=sys.stderr)
        print("  pip install -e /path/to/polymarket-microstructure", file=sys.stderr)
        return 1

    # --- Run scraper ---
    with PolygonRpcClient(args.rpc_url) as client:
        produced = scrape_slice_finalized(
            client=client,
            contract_address=args.contract_address,
            from_block=start_block,
            requested_to_block=args.end_block,
            out_dir=out_dir,
            slice_blocks=args.slice_blocks,
            chunk=args.chunk,
        )

    # --- Save checkpoint ---
    if produced:
        last_block = start_block + len(produced) * args.slice_blocks  # approximate
        save_checkpoint(out_dir, last_block)
        print(f"Checkpoint saved at block ~{last_block}")

    print(f"Done. Wrote {len(produced)} slice parquets to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
