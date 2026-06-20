// DID privacy demo — Move 教学：注册 + 选择性披露，仅测试网
module demo::did_privacy {
    use std::vector;

    struct DidRecord has key {
        method: vector<u8>,
        /// 可公开披露的 claim（教学：email hash 等）
        disclosed_claim: vector<u8>,
        /// 保留字段 hash，验证时不泄露原文
        withheld_claim_hash: vector<u8>,
    }

    struct DisclosureView has drop {
        claim: vector<u8>,
        proof_ok: bool,
    }

    public entry fun register(
        account: &signer,
        method: vector<u8>,
        disclosed: vector<u8>,
        withheld_hash: vector<u8>,
    ) {
        move_to(
            account,
            DidRecord {
                method,
                disclosed_claim: disclosed,
                withheld_claim_hash: withheld_hash,
            },
        );
    }

    /// 教学用：验证请求方仅看到 disclosed_claim，withheld 仅以 hash 存在
    public fun selective_disclose(record: &DidRecord, requested: vector<u8>): DisclosureView {
        let proof_ok = record.disclosed_claim == requested;
        DisclosureView {
            claim: record.disclosed_claim,
            proof_ok,
        }
    }

    public fun withheld_hash_only(record: &DidRecord): vector<u8> {
        record.withheld_claim_hash
    }
}
