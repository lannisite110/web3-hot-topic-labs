"""Account Abstraction Wallet Lab — 教学规则 evaluate。"""

from __future__ import annotations

import hashlib

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    owner = str(inp.params.get("owner", "0x0000000000000000000000000000000000000001"))
    step = str(inp.params.get("aa_flow_step", "execute"))
    call_data = str(inp.params.get("call_data", "0x"))
    user_op_hash = "0x" + hashlib.sha256(f"{owner}:{step}:{call_data}".encode()).hexdigest()

    steps = ["build", "sign", "bundle", "validate", "execute"]
    step_index = steps.index(step) if step in steps else len(steps) - 1
    completed = ",".join(steps[: step_index + 1])

    return ok(
        "plugins/aa-wallet/contracts/AAWalletDemo.sol",
        "solidity",
        "HOT_AA_WALLET_SIM",
        [
            f"owner={owner}",
            f"user_op_hash={user_op_hash}",
            f"aa_flow_step={step}",
            f"aa_flow_completed={completed}",
            f"entry_point=0x4337demo00000000000000000000000000000001",
            f"call_data={call_data[:42]}",
            "plugin_id=edu.hot.aa-wallet",
        ],
    )
