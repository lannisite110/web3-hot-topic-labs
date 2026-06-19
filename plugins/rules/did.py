"""DID Privacy Demo Lab — 教学规则 evaluate。"""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    param = inp.params.get("did_method", "did:demo")
    return ok(
        "plugins/did/contracts/DidPrivacy.move",
        "move",
        "HOT_DID_PRIVACY_DEMO",
        ["did_method=" + str(param), "plugin_id=edu.hot.did"],
    )
