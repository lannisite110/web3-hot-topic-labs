"""Account Abstraction Wallet Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("owner", "0x0000000000000000000000000000000000000001")
    return ok(
        "plugins/aa-wallet/contracts/AAWalletDemo.sol",
        "solidity",
        "HOT_AA_WALLET_SIM",
        ["owner=" + str(param), "plugin_id=edu.hot.aa-wallet"],
    )
