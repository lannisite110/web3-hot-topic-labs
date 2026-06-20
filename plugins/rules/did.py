"""DID Privacy Demo Lab — 选择性披露教学规则。"""

from __future__ import annotations

import hashlib

from plugins.rules._common import RuleInput, RuleOutput, reject_mainnet, ok


_CLAIMS = {
    "email": ("email@demo.edu", "sha256:email…redacted"),
    "age_over_18": ("age>=18", "sha256:exact-age…withheld"),
    "country": ("country=SG", "sha256:passport…withheld"),
}


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    method = str(inp.params.get("did_method", "did:demo:edu"))
    level = str(inp.params.get("disclosure_level", "email"))
    requested = str(inp.params.get("requested_claim", "email"))

    disclosed = _CLAIMS.get(requested, _CLAIMS["email"])
    revealed = disclosed[0] if level != "none" else "(withheld)"
    withheld = disclosed[1]
    proof_valid = level != "none" and requested in _CLAIMS

    claim_hash = "0x" + hashlib.sha256(revealed.encode()).hexdigest()[:32]

    return ok(
        "plugins/did/contracts/DidPrivacy.move",
        "move",
        "HOT_DID_PRIVACY_DEMO",
        [
            f"did_method={method}",
            f"disclosure_level={level}",
            f"requested_claim={requested}",
            f"revealed_field={revealed}",
            f"withheld_hash={withheld}",
            f"claim_hash={claim_hash}",
            f"proof_valid={'true' if proof_valid else 'false'}",
            "selective_disclosure=enabled",
            "plugin_id=edu.hot.did",
        ],
    )
