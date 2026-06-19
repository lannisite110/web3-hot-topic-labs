"""智能合约语言择优 — 根据业务描述自动推荐最优语言与工具链组。"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

_RULES_PATH = Path(__file__).with_name("language-choice-rules.yaml")


@dataclass
class RuleInput:
    user_prompt: str
    params: dict[str, Any]
    allowed_chain_ids: list


@dataclass
class RuleOutput:
    recommended_template: str
    recommended_language: str
    audit_hints: list[str]
    compliance_passed: bool
    rejection_reason: str | None = None
    toolchain_group: str | None = None
    tools: list[str] | None = None
    reason: str | None = None


def _load_rules() -> dict:
    with _RULES_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def _match_rule(prompt: str, params: dict, rules: list[dict]) -> dict | None:
    text = f"{prompt} {params.get('scenario', '')} {params.get('tags', '')}".lower()
    for rule in rules:
        if any(kw.lower() in text for kw in rule["keywords"]):
            return rule
    return None


def evaluate(inp: RuleInput) -> RuleOutput:
    if inp.params.get("target_network") == "mainnet":
        return RuleOutput(
            recommended_template="",
            recommended_language="",
            audit_hints=[],
            compliance_passed=False,
            rejection_reason="mainnet forbidden",
        )

    cfg = _load_rules()
    matched = _match_rule(inp.user_prompt, inp.params, cfg["rules"])
    choice = matched or cfg["default"]

    lang = choice["language"]
    template_map = {
        "solidity": "plugins/language-advisor/templates/GenericDeFi.sol",
        "vyper": "plugins/language-advisor/templates/Vault.vy",
        "huff": "plugins/language-advisor/templates/MatchKernel.huff",
        "rust": "plugins/language-advisor/templates/AnchorProgram.rs",
        "move": "plugins/language-advisor/templates/NftAsset.move",
        "cairo": "plugins/language-advisor/templates/ZkRollup.cairo",
        "clarity": "plugins/language-advisor/templates/BtcL2.clar",
        "cadence": "plugins/language-advisor/templates/GameNFT.cdc",
        "teal": "plugins/language-advisor/templates/Payment.teal",
    }
    lab_map = {
        "solidity": "edu.hot.aa-wallet",
        "vyper": "edu.hot.rwa-edu",
        "huff": "edu.hot.mev",
        "rust": "edu.hot.depin",
        "move": "edu.hot.did",
        "cairo": "edu.hot.zk-modular",
        "clarity": "edu.hot.language-advisor",
        "cadence": "edu.hot.dao",
        "teal": "edu.hot.language-advisor",
    }
    namespace_map = {
        "evm": "ns-evm",
        "solana": "ns-solana",
        "move": "ns-move",
        "zk": "ns-hot-zk",
        "btc": "ns-lang-btc",
        "flow": "ns-lang-flow",
        "algorand": "ns-lang-algorand",
    }
    group = choice["toolchain_group"]

    return RuleOutput(
        recommended_template=template_map.get(lang, template_map["solidity"]),
        recommended_language=lang,
        audit_hints=[
            f"toolchain_group={group}",
            f"namespace={namespace_map.get(group, 'ns-evm')}",
            f"tools={','.join(choice['tools'])}",
            f"suggested_lab={lab_map.get(lang, 'edu.hot.language-advisor')}",
            f"image=edu/toolchain-{group}:0.1.0",
            "testnet-only deployment",
        ],
        compliance_passed=True,
        toolchain_group=group,
        tools=choice["tools"],
        reason=choice.get("reason", ""),
    )
