"""Web3 热点 Lab 共享合规与测试网常量。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

SEPOLIA_CHAIN_ID = 11155111
BLOCKED_MAINNET_IDS = {1, 56, 137, 42161, 10, 8453}


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


def reject_mainnet(inp: RuleInput) -> RuleOutput | None:
    if inp.params.get("target_network") == "mainnet":
        return RuleOutput("", "", [], False, "mainnet forbidden")
    for cid in inp.allowed_chain_ids:
        if isinstance(cid, int) and cid in BLOCKED_MAINNET_IDS:
            return RuleOutput("", "", [], False, f"mainnet chainId {cid} blocked")
    return None


def testnet_hints(task_type: str, extra: list[str] | None = None) -> list[str]:
    hints = [
        f"chain_id={SEPOLIA_CHAIN_ID}",
        f"task_type={task_type}",
        "testnet-only",
        "no-production-rollup",
    ]
    if extra:
        hints.extend(extra)
    return hints


def ok(template: str, language: str, task_type: str, extra: list[str] | None = None) -> RuleOutput:
    return RuleOutput(
        recommended_template=template,
        recommended_language=language,
        audit_hints=testnet_hints(task_type, extra),
        compliance_passed=True,
    )
