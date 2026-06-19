// NftAssetDemo — 教学 Move 资产模板，仅测试网
module demo::nft_asset {
    use std::signer;

    struct Asset has key, store {
        owner: address,
        id: u64,
    }

    public entry fun mint(account: &signer, id: u64) {
        let addr = signer::address_of(account);
        move_to(account, Asset { owner: addr, id });
    }
}
