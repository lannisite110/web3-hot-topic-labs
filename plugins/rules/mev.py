"""MEV PBS Simulation Lab — Proposer-Builder 分离教学规则。"""

from __future__ import annotations

import hashlib

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    try:
        block_slots = max(1, min(int(inp.params.get("block_slots", 12)), 32))
        builder_count = max(2, min(int(inp.params.get("builder_count", 3)), 8))
    except (TypeError, ValueError):
        block_slots, builder_count = 12, 3

    seed = f"{block_slots}:{builder_count}:{inp.params.get('slot_index', 0)}"
    digest = hashlib.sha256(seed.encode()).hexdigest()
    winning_idx = int(digest[:2], 16) % builder_count
    winning_bid_gwei = 10 + (int(digest[2:4], 16) % 90)

    return ok(
        "plugins/mev/contracts/MevPbsAuction.sol",
        "solidity",
        "HOT_MEV_PBS_SIM",
        [
            f"block_slots={block_slots}",
            f"builder_count={builder_count}",
            f"pbs_mode=proposer-builder-separation",
            f"winning_builder=builder-{winning_idx}",
            f"winning_bid_gwei={winning_bid_gwei}",
            f"slot_index={inp.params.get('slot_index', 0)}",
            "arbitrage_bot=forbidden",
            "plugin_id=edu.hot.mev",
        ],
    )
